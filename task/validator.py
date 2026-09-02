from folio.imports import get

nlp = get("spacy")

ACTION_WORDS = {
    "search",
    "find",
    "make",
    "send",
    "upload",
    "save",
    "generate",
    "get",
    "run",
    "create",
    "write",
    "fetch",
}
def is_valid(task):
    if not isinstance(task, str):
        return [task]

    task = task.strip()

    word = task.split()


    first_Word = word[0].lower().strip(".,!?")

    if first_Word in ACTION_WORDS:
        return True
    
    if len(word) <= 2:
        return False
    doc = nlp(task)
    for token in doc:
        if token.pos_ == "VERB":
            return True

    return False

def validate_tasks(tasks, og_task):
    valid_task = []
    for task in tasks:
        if is_valid(task):
            if task not in valid_task:
                valid_task.append(task)

    if not valid_task:
        return [og_task]

    return valid_task