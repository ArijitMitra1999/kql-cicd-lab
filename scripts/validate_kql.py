import sys
import glob

def validate(path):
    text = open(path).read()
    if not text.strip():
        return f"{path}: file is empty"
    if '|' not in text:
        return f"{path}: no pipe operator found, likely invalid KQL"
    if text.count('(') != text.count(')'):
        return f"{path}: unbalanced parentheses"
    return None

errors = [e for f in glob.glob("queries/*.kql") if (e := validate(f))]
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("All KQL files passed validation.")