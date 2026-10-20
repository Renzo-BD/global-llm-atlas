"""Validate canonical data, exports, references, and browser-script syntax."""
import csv
import json
import re
import subprocess
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def cell(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def check_export(path, expected):
    with (ROOT / path).open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames
        actual = list(reader)
    if not fields or set(fields) != set(expected[0]):
        raise ValueError(f"{path}: unexpected columns")
    normalized = [{key: cell(row.get(key)) for key in fields} for row in expected]
    if actual != normalized:
        raise ValueError(f"{path}: JSON/CSV mismatch")


atlas = read_json("data/llms.json")
android = read_json("data/android.json")
for dataset, schema_path in [(atlas, "data/schema.json"), (android, "data/android-schema.json")]:
    validator = Draft202012Validator(read_json(schema_path), format_checker=FormatChecker())
    validator.validate(dataset)
    ids = [entry["id"] for entry in dataset["entries"]]
    if len(ids) != len(set(ids)):
        raise ValueError(f"{schema_path}: duplicate IDs")

atlas_ids = {entry["id"] for entry in atlas["entries"]}
for entry in atlas["entries"]:
    if entry["duplicate_of"] and entry["duplicate_of"] not in atlas_ids:
        raise ValueError(f'{entry["id"]}: missing duplicate target')
for entry in android["entries"]:
    if entry["id"] not in atlas_ids or not entry["url"].strip():
        raise ValueError(f'{entry["id"]}: missing atlas ID or Android URL')

capabilities = ["text", "image", "voice", "files", "web_search"]
base_fields = ["id", "name", "url", "country", "country_es", "iso2", "continent", "service_type", "registration"]
tail_fields = ["status", "last_manual_verification", "operator_country", "duplicate_of", "country_confidence"]
llm_rows = []
for entry in atlas["entries"]:
    row = {key: entry[key] for key in base_fields + tail_fields}
    row.update({f"capability_{key}": entry["capabilities"][key] for key in capabilities})
    llm_rows.append(row)
check_export("data/llms.csv", llm_rows)
check_export("data/android.csv", [
    {key: entry.get(key, "") for key in ["id", "status", "distribution", "url", "verified", "note"]}
    for entry in android["entries"]
])

for html_path in ["index.html", "android.html"]:
    html = (ROOT / html_path).read_text(encoding="utf-8")
    for attrs, script in re.findall(r"<script([^>]*)>(.*?)</script>", html, re.DOTALL | re.IGNORECASE):
        if not re.search(r"\bsrc\s*=", attrs):
            subprocess.run(["node", "--check"], input=script, text=True, check=True)
subprocess.run(["node", "--check", str(ROOT / "android-main.js")], check=True)
print(f'Validated {len(atlas["entries"])} access points and {len(android["entries"])} Android records; schemas, CSV exports, references and JavaScript syntax passed.')
