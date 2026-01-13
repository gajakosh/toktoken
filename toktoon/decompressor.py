class ToonDecompressor:
    def __init__(self, rules):
        self.reverse = {v: k for k, v in rules.items()}

    def decompress(self, text: str) -> str:
        out = text
        for short, long in self.reverse.items():
            out = out.replace(short, long)

        return out