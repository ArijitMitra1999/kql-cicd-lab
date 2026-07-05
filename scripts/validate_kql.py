import sys
import glob
import re

def validate(path):
    text = open(path).read()
    if not text.strip():
        return f"{path}: file is empty"
    if '|' not in text:
        return f"{path}: no pipe operator found"
    if text.count('(') != text.count(')'):
        return f"{path}: unbalanced parentheses"
    lines = text.split('\n')
    for line in lines:
        stripped = line.strip()
        for keyword in ['where', 'project', 'order by', 'summarize', 'extend', 'join']:
            if stripped.startswith(keyword) and not stripped.startswith('|'):
                return f"{path}: '{keyword}' is missing a pipe operator"
    return None

# This runs validation against ALL .kql files in queries folder
errors = [e for f in glob.glob("queries/*.kql") if (e := validate(f))]
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"All {len(list(glob.glob('queries/*.kql')))} KQL files passed validation.")