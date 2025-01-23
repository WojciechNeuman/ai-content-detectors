import re

def text_process(mess):
    """
    Process text to:
    1. Remove punctuation (including all Unicode quotes)
    2. Convert text to lowercase
    3. Return cleaned text without removing stopwords
    """
    mess = re.sub(r"[^\w\s]", "", mess)

    mess = mess.lower()

    return mess