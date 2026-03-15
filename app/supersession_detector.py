import re


def detect_supersession(text):

    if not isinstance(text, str):
        return []

    patterns = [
        r"supersedes\s+(.*?)(\.|\n)",
        r"replaces\s+(.*?)(\.|\n)",
        r"superseded\s+by\s+(.*?)(\.|\n)",
        r"this\s+circular\s+supersedes\s+(.*?)(\.|\n)"
    ]

    matches = []

    for pattern in patterns:

        results = re.findall(pattern, text.lower())

        for r in results:
            matches.append(r[0].strip())

    return matches