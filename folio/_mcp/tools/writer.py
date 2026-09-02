import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def write_file(query: str) -> str:
    """Write and save content, research, summaries, or results to a file on disk."""
    path = os.path.join(BASE_DIR, "outputs/output.txt")
    os.makedirs(os.path.dirname(path) , exist_ok = True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(query)

    return  f"Written to {path}"
