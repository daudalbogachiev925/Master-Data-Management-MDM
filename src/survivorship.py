def survivorship_most_recent(records, field):
    """Берём значение из последней записи (updated_at)."""
    sorted_recs = sorted(records, key=lambda r: r.get("updated_at", ""), reverse=True)
    for r in sorted_recs:
        v = r.get(field)
        if v not in (None, ""):
            return v
    return None

def survivorship_longest(records, field):
    """Берём самое длинное значение."""
    values = [str(r.get(field, "")) for r in records]
    return max(values, key=len) if values else None

def survivorship_priority(records, field, source_priority):
    """Берём из источника с наивысшим приоритетом."""
    for src in source_priority:
        for r in records:
            if r.get("source") == src and r.get(field):
                return r[field]
    return None
