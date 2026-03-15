RELATION_KEYWORDS = {
    "supersedes": ["supersedes", "replaces"],
    "amends": ["amends", "modifies"],
    "clarifies": ["clarifies", "explains"]
}


def detect_policy_relations(text):

    relations = []

    lower = text.lower()

    for relation, words in RELATION_KEYWORDS.items():

        for w in words:

            if w in lower:
                relations.append(relation)

    return list(set(relations))