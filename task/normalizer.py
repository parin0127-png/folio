from folio.imports import get
import re

mlp = get("spacy")

FILLER_PATTERNS = [
    r"^can you\s+",
    r"^could you\s+",
    r"^would you\s+",
    r"^please\s+",
    r"^kindly\s+",
    r"^i want you to\s+",
    r"^i need you to\s+",
]

def normalizer_task(text):
    text = text.strip()
    text = text.lower()
    for p in FILLER_PATTERNS:
        text = re.sub(p, "", text)

    text = " ".join(text.split())

    return text