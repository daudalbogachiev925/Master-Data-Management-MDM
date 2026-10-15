from src.matching import similarity, phone_match, email_match
from collections import defaultdict

def find_duplicates(df, threshold=0.85):
    """Блокировка по первым буквам имени + fuzzy match внутри блока."""
    blocks = defaultdict(list)
    for idx, row in df.iterrows():
        key = str(row["name"])[:2].lower()
        blocks[key].append(idx)

    duplicate_groups = []
    for key, indices in blocks.items():
        used = set()
        for i in indices:
            if i in used:
                continue
            group = [i]
            for j in indices:
                if j <= i or j in used:
                    continue
                score = 0
                score += similarity(df.loc[i, "name"], df.loc[j, "name"])
                score += phone_match(df.loc[i, "phone"], df.loc[j, "phone"])
                score += email_match(df.loc[i, "email"], df.loc[j, "email"])
                if score / 3 >= threshold * 0.5 or \
                   similarity(df.loc[i, "name"], df.loc[j, "name"]) >= threshold:
                    group.append(j)
                    used.add(j)
            if len(group) > 1:
                duplicate_groups.append(group)
                used.add(i)
    return duplicate_groups
