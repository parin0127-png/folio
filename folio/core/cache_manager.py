import pickle, os, time
from folio.imports import get
from folio._mcp.client import get_tool_dict, ready

model = None


BM25OKapi = get("bm25")
CACHE_FILE = "cache/tool_cache.pkl"
CACHE_TTL = 5 * 60 * 60

def _load_cache():
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "rb") as f:
                data = pickle.load(f)
            if time.time() - data["timestamp"] < CACHE_TTL:
                print("> [Cache] Loaded from disk.")
                return data
        return None
    except Exception as e:
        return f"> [Error] as [{e}]"

def _save_cache(data):
    try:
        os.makedirs("cache", exist_ok = True)
        with open(CACHE_FILE, "wb")as f:
            pickle.dump(data, f)
        print("> [Cache] Saved to disk.")
    except Exception as e:
        return f"> [Error] as [{e}]"

def load():
    ready.wait()
    cache = _load_cache()
    if cache:
        return cache

    print("> [Cache] Building fresh cache...")
    tool_dict = get_tool_dict()
    tool_name = list(tool_dict.keys())
    tool_descs = list(tool_dict.values())
    bm25 = BM25OKapi([d.split() for d in tool_descs])
    tool_embd = get("sentence_transformer").encode(tool_descs)
    data = {
        "timestamp": time.time(),
        "tool_dict": tool_dict,
        "tool_names": tool_name,
        "tool_descs": tool_descs,
        "bm25": bm25,
        "tool_embd": tool_embd
    }
    _save_cache(data)
    return data
