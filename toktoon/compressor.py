import re
from .rules import DEFAULT_RULES

class ToonCompressor:
    def __init__(self, rules=None):
        self.rules = rules or DEFAULT_RULES

    def compress(self, text: str) -> str:
        compressed = text.lower()

        for long, short in self.rules.items():
            compressed = re.sub(
                r"\b" + re.escape(long.lower()) + r"\b",
                short,
                compressed
            )

        compressed  = compressed.replace(" ", "")
        return compressed
    
    