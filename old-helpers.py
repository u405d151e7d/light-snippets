"""Quick helpers."""

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

if __name__ == "__main__":
    print(clamp(11, 0, 28))
