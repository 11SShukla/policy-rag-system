import re

RELATION_PATTERNS = {
    "supersedes": r"supersedes\s+(RBI\/\d{4}-\d{2}\/\d+)",
    "amends": r"amends\s+(RBI\/\d{4}-\d{2}\/\d+)",
    "modifies": r"modifies\s+(RBI\/\d{4}-\d{2}\/\d+)",
    "replaces": r"replaces\s+(RBI\/\d{4}-\d{2}\/\d+)"
}


def extract_policy_relations(text, doc_id):

    relations = []

    for relation, pattern in RELATION_PATTERNS.items():

        matches = re.findall(pattern, text, re.IGNORECASE)

        for target in matches:

            relations.append({
                "source": doc_id,
                "target": target,
                "relation": relation
            })

    return relations