import re
from difflib import SequenceMatcher

def normalize(s):
    if not isinstance(s, str):
        return ""
    return re.sub(r"\s+", "", s.lower().strip())

def similarity(a, b):
    a, b = normalize(a), normalize(b)
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()

def exact_match(a, b):
    return normalize(a) == normalize(b)

def fuzzy_match(a, b, threshold=0.85):
    return similarity(a, b) >= threshold

def phone_match(a, b):
    a = re.sub(r"\D", "", str(a))
    b = re.sub(r"\D", "", str(b))
    return a and b and a == b

def email_match(a, b):
    return normalize(a) == normalize(b)
