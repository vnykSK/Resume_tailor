import re
from collections import Counter

STOPWORDS = {
    "the", "a", "an", "and", "or", "is", "are",
    "to", "for", "of", "with", "in", "on", "at"
}



def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)

    return text



def extract_keywords(text):

    text = clean_text(text)

    words = text.split()

    filtered = [
        word for word in words
        if word not in STOPWORDS and len(word) > 2
    ]

    freq = Counter(filtered)

    keywords = [
        word for word, count in freq.most_common(20)
    ]

    return keywords