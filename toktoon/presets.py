from .rules import DEFAULT_RULES
from .compressor import ToonCompressor

def llm_prompt():
    return ToonCompressor(DEFAULT_RULES)

