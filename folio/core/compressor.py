def compress(history):
    try:
        lines = []
        for h in history:
            lines.append(f"-{h['user'][:60]} → {h['agent'][:60]}")
        return "\n".join(lines[-3:])
    except Exception as e:
        return "ERROR"