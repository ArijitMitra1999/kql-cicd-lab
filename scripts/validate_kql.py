import re

def validate(path):
    text = open(path).read()
    if not text.strip():
        return f"{path}: file is empty"
    if '|' not in text:
        return f"{path}: no pipe operator found"
    if text.count('(') != text.count(')'):
        return f"{path}: unbalanced parentheses"
    # Check every KQL keyword has a pipe prefix
    for keyword in ['where', 'project', 'order by', 'summarize', 'extend', 'join']:
        pattern = rf'(?<!\|)\s*\b{keyword}\b'
        lines = text.split('\n')
        for line in lines:
            stripped = line.strip()
            if stripped.startswith(keyword) and not stripped.startswith('|'):
                return f"{path}: '{keyword}' is missing a pipe operator"
    return None