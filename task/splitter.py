from folio.imports import get

nlp = get("spacy")

def split_task(task):
    if not isinstance(task, str):
        return [task]

    task = task.strip()

    if not task:
        return [task]

    doc = nlp(task)

    # for t in doc:
    #     print(
    #         t.text,
    #         "POS:", t.pos_,
    #         "DEP:", t.dep_,
    #         "HEAD:", t.head.text
    #     )

    split_positions = []
    for t in doc:
        if t.pos_ == "VERB" and t.dep_ == "conj":
            previous_t = t.nbor(-1)
            if previous_t.dep_ == "cc":
                split_positions.append(previous_t.idx)

    if not split_positions:
        return [task]


    parts = []
    start = 0

    for pos in split_positions:
        part = task[start:pos].strip()

        if part:
            parts.append(part)

        start = pos

    last_part = task[start:].strip()

    if last_part.startswith("and "):
        last_part = last_part[4:].strip()

    if last_part:
        parts.append(last_part)

    if len(parts) <= 1:
        return [task]

    return parts
