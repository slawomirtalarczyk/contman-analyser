# URI keyword analyser
Basic keyword analyser written in Python3. GUI build with tkinter, parser
based on BeautifulSoup4.

## How to use
1. Obtain repository with ``git clone https://github.com/slawomirtalarczyk/contman-analyser.git``
2. *(optional)* Run ``pip install -c .\requirements.txt`` to install bs4 if needed  
3. Run ``python app.py``
4. Enter URI in entry field, than press **Analyse**

Application will download document, find keywords in `<meta>` tags and count
words occurrences in visible part of website. Application is not using
JavaScript engine (like V8 in node.js) so it cannot work on dynamic
websites (using AJAX for example).

## Architecture
`app.py` contains GUI. Main module is located in `analyser.py`. It contains
one class `ContmanAnalyser`. After initialization, constructor set only URI
address in the object. `count_words()` method could call all necessary
functions to run (``get_keywords()``, ``get_visible_text()``) and download,
parse and extract data.
