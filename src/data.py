import pandas as pd
import numpy as np

def generate_duplicates(n=200, seed=42):
    """Генерирует клиентов с дублями."""
    np.random.seed(42)
    names = ["Иван Петров", "Мария Сидорова", "John Smith",
             "Anna Müller", "Пётр Иванов", "Kate Johnson"]
    rows = []
    for i in range(n):
        base = np.random.choice(names)
        # искажение
        name_variant = base
        if np.random.random() > 0.7:
            name_variant = base.replace(" ", "") if np.random.random() > 0.5 else base.lower()
        phone = f"+7900{np.random.randint(1000000, 9999999)}"
        rows.append({
            "id": f"C{i:05d}",
            "name": name_variant,
            "phone": phone if np.random.random() > 0.3 else phone[:-2],
            "email": f"user{i}@{np.random.choice(['mail.ru','gmail.com','ex.com'])}",
            "city": np.random.choice(["Moscow", "Berlin", "London"]),
            "updated_at": f"2024-{np.random.randint(1,13):02d}-{np.random.randint(1,28):02d}",
        })
    return pd.DataFrame(rows)
