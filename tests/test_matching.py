from src.matching import similarity, phone_match, email_match

def test_similarity_same():
    assert similarity("Иван Петров", "Иван Петров") == 1.0

def test_similarity_high():
    assert similarity("Иван Петров", "ИванПетров") > 0.8

def test_phone_match():
    assert phone_match("+79001234567", "89001234567")

def test_email_match_case():
    assert email_match("User@Mail.RU", "user@mail.ru")
