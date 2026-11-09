"""Regenerate spreadsheet exports from the canonical JSON datasets."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ["id", "name", "url", "country", "country_es", "iso2", "continent", "service_type", "registration"]
CAPABILITIES = ["text", "image", "voice", "files", "web_search"]
TAIL = ["status", "last_manual_verification", "operator_country", "duplicate_of", "country_confidence"]
ANDROID = ["id", "status", "distribution", "url", "verified", "note"]


def export(path, fields, rows):
    with (ROOT / path).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: str(value).lower() if isinstance(value, bool) else value
                             for key, value in row.items()})


def main():
    atlas = json.loads((ROOT / "data/llms.json").read_text(encoding="utf-8"))
    android = json.loads((ROOT / "data/android.json").read_text(encoding="utf-8"))
    rows = []
    for entry in atlas["entries"]:
        row = {key: entry[key] for key in BASE + TAIL}
        row.update({f"capability_{key}": entry["capabilities"][key] for key in CAPABILITIES})
        rows.append(row)
    export("data/llms.csv", BASE + [f"capability_{key}" for key in CAPABILITIES] + TAIL, rows)
    export("data/android.csv", ANDROID,
           [{key: entry.get(key, "") for key in ANDROID} for entry in android["entries"]])
    print(f"Exported {len(rows)} access points and {len(android['entries'])} Android records.")


if __name__ == "__main__":
    main()
