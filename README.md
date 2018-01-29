# URI keyword analyser
Basic keyword analyser written in Python3. GUI build with tkinter, parser
based on BeautifulSoup4.

## How to use
Run ``python app.py``. Enter URI in entry field, than press **Analyse**.
Application will download document, find keywords in `<meta>` tags and count
words occurrences in visible part of website.

## Architecture
`app.py` contains GUI. Main module is located in `analyser.py`. It contains
one class `ContmanAnalyser`. After initialization, constructor set only URI
address in the object. `count_words()` method could call all necessary
functions to run (``get_keywords()``, ``get_visible_text()``) and download,
parse and extract data.