from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import urlopen


class ContmanAnalyser:
    """
    Instance of contman crawler class enables parsing webpage and counting
    keyword occurencies in document.
    """
    def __init__(self, uri = None):
        """
        Create intance of crawler object
        :param uri: document uri for parsing
        """
        if uri is None or uri == "":
            self.quote_page = "https://www.w3schools.com/tags/tag_meta.asp"
        else:
            self.quote_page = uri
        content = urlopen(self.quote_page).read()
        self.soup = BeautifulSoup(content, "html.parser")
        self.keywords_set = None
        self.visible_text = None

    def get_keywords(self):
        """
        :return: distinct list (set) of keywords from keyword meta tags in document
        """
        if self.keywords_set is not None:
            return self.keywords_set
        self.keywords_set = set()
        meta_keyword_tags = self.soup.find_all('meta', attrs={'name': lambda x: x and x.lower() == 'keywords'})
        for tag in meta_keyword_tags:
            tag_attr = tag.attrs['content'].replace(", ",",")
            self.keywords_set.update(tag_attr.split(','))
        return self.keywords_set

    def visible_tags(self, elmnt):
        """
        Filter function for determining if HTML node contain visible text
        :param elmnt: bs4.element
        :return: True if contains visible content
        """
        if elmnt.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(elmnt, Comment):
            return False
        return True

    def get_visible_text(self):
        """
        Create string with whole visible text from document
        :return: string
        """
        text = self.soup.findAll(text=True)
        visible_texts = filter(self.visible_tags, text)
        self.visible_text = u" ".join(t.strip() for t in visible_texts)
        return self.visible_text

    def count_words(self, word_list = None):
        """
        If necessary, generate keyword list for the frist time and filtering visible text.
        Counting occurencies of keywords in document.
        :return:
        """
        if self.keywords_set is None:
            self.get_keywords()
        if self.visible_text is None:
            self.get_visible_text()

        if word_list is None:
            word_list = self.keywords_set
        keywords_count = dict()
        for word in word_list:
            keywords_count[word] = 0
        for word in self.get_visible_text().split(" "):
            if word in word_list:
                keywords_count[word] += 1
        return keywords_count


if __name__ == "__main__":
    analyser = ContmanAnalyser("https://www.w3schools.com/tags/tag_meta.asp")
    tmp = analyser.count_words()
    print(analyser.count_words())
