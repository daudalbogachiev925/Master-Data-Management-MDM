from src.survivorship import survivorship_most_recent

def build_golden_record(records, strategy="most_recent"):
    if not records:
        return None
    fields = set()
    for r in records:
        fields.update(r.keys())
    golden = {
        "source_ids": [r.get("id") for r in records],
        "record_count": len(records),
        "strategy": strategy,
    }
    for field in fields:
        if field in ("id", "updated_at", "source"):
            continue
        if strategy == "most_recent":
            golden[field] = survivorship_most_recent(records, field)
    return golden

def build_all_golden_records(df, groups, strategy="most_recent"):
    golden = []
    for group in groups:
        records = [df.loc[i].to_dict() for i in group]
        golden.append(build_golden_record(records, strategy))
    return golden
