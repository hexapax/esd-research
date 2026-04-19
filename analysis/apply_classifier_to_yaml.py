#!/usr/bin/env python3
"""
Patch the YAML frontmatter of every ESD-*.md file with two new flags:

  is_freshwater_private_dock: true|false
  is_freshwater_marina: true|false
  setting_classifier_confidence: high|medium|low
  setting_classifier_reasoning: "..."

Insert them as a new block after the existing 'water_type:' / 'fault_description:'
field (the Electrical Details group in SCHEMA.md). If the block already exists,
update it in place.

Preserves everything else — the markdown body, comments, ordering.
"""
import glob, json, os, re

DATASET_DIR = "/opt/repos/esd-research/esd-dataset"
CLASSIF = "/opt/repos/esd-research/analysis/classifier_output.json"

BLOCK_KEYS = [
    "is_freshwater_private_dock",
    "is_freshwater_marina",
    "setting_classifier_confidence",
    "setting_classifier_reasoning",
]

def yaml_escape(s):
    if s is None:
        return '""'
    s = str(s).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'

def build_block(rec):
    lines = [
        f"is_freshwater_private_dock: {'true' if rec['is_freshwater_private_dock'] else 'false'}",
        f"is_freshwater_marina: {'true' if rec['is_freshwater_marina'] else 'false'}",
        f"setting_classifier_confidence: {rec['confidence']}",
        f"setting_classifier_reasoning: {yaml_escape(rec['reasoning'])}",
    ]
    return "\n".join(lines)

def split_frontmatter(text):
    m = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n?)", text, re.DOTALL)
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3), text[m.end():]

def apply(fp, rec):
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()
    parts = split_frontmatter(text)
    if parts is None:
        return False, "no frontmatter"
    head, body, tail, rest = parts

    # Remove existing occurrences of any of BLOCK_KEYS (and subsequent continuation lines)
    out_lines = []
    skip_continuations = False
    for line in body.split("\n"):
        stripped = line.lstrip()
        is_block_key = any(stripped.startswith(k + ":") for k in BLOCK_KEYS)
        if is_block_key:
            skip_continuations = True
            continue
        if skip_continuations:
            # If the line looks like a continuation (starts with whitespace, not a key) skip it
            if line.startswith(" ") or line.startswith("\t"):
                continue
            skip_continuations = False
        out_lines.append(line)
    cleaned_body = "\n".join(out_lines).rstrip("\n")

    # Insertion point: right after the line containing 'fault_description:'
    # (fallback: after 'water_type:')
    insertion_anchor = None
    for anchor in ("fault_description:", "water_type:"):
        idx = cleaned_body.find(f"\n{anchor}")
        if idx == -1 and cleaned_body.startswith(anchor):
            idx = 0
        if idx == -1:
            continue
        # Find end of that (possibly multi-line) value — scan forward to next top-level key
        start = idx + 1 if idx != 0 else 0
        # Move to end-of-line
        nl = cleaned_body.find("\n", start)
        if nl == -1:
            nl = len(cleaned_body)
        # If the next line is indented (continuation), keep scanning
        while nl < len(cleaned_body):
            next_nl = cleaned_body.find("\n", nl + 1)
            if next_nl == -1:
                next_nl = len(cleaned_body)
            line = cleaned_body[nl+1:next_nl]
            if line.startswith(" ") or line.startswith("\t") or line == "":
                nl = next_nl
                continue
            break
        insertion_anchor = nl
        break

    block = build_block(rec)
    if insertion_anchor is None:
        # Append at end
        new_body = cleaned_body + "\n" + block
    else:
        new_body = (cleaned_body[:insertion_anchor] + "\n"
                    + block + cleaned_body[insertion_anchor:])

    new_text = head + new_body.strip("\n") + "\n" + tail + rest
    with open(fp, "w", encoding="utf-8") as f:
        f.write(new_text)
    return True, None

def main():
    classif = {r["incident_id"]: r for r in json.load(open(CLASSIF))}
    files = sorted(glob.glob(os.path.join(DATASET_DIR, "ESD-*.md")))
    wrote = 0
    errors = []
    for fp in files:
        # Read incident_id from frontmatter
        with open(fp, "r", encoding="utf-8") as f:
            text = f.read()
        m = re.search(r"^incident_id:\s*(\S+)", text, re.M)
        if not m:
            errors.append((fp, "no incident_id"))
            continue
        iid = m.group(1).strip().strip('"\'')
        rec = classif.get(iid)
        if rec is None:
            errors.append((fp, f"no classifier output for {iid}"))
            continue
        ok, err = apply(fp, rec)
        if ok:
            wrote += 1
        else:
            errors.append((fp, err))
    print(f"Wrote {wrote}/{len(files)} files")
    for e in errors[:10]:
        print("  ERROR:", e)

if __name__ == "__main__":
    main()
