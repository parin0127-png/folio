class RecursiveSplitter:
    def __init__(self, chunk_size = 500, overlap = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap 
        self.separators = ["\n\n", "\n", " ", ""]


    def split(self, text, source = "unknown"):
        chunks = []
        current = ""

        separator = ""
        for sep in self.separators:
            if sep in text:
                separator = sep
                break

        pieces = text.split(separator)
        for piece in pieces:
            if len(current) + len(piece) <= self.chunk_size:
                current += piece + separator
            else:
                if current:
                    chunks.append(current.strip())

                current = current[-self.overlap:] + piece + separator

        if current.strip():
            chunks.append(current.strip())

        result = []
        for i, chunk in enumerate(chunks):
            result.append({
                "text": chunk,
                "index": i,
                "source": source
            })

        return result