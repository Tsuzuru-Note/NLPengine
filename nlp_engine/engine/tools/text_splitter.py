import re
from typing import List
from .SentenceContext import SentenceContext

class TextSplitter:
    # ending symbol
    ENTENCE_ENDINGS = r"[。！？]"

    def __init__(self):
        pass

    def split(self, text: str) -> List[str]:
        if not text:
            return []

        text = text.strip()

        # Split sentence (including punctuation)
        sentences = re.split(
            f"({self.ENTENCE_ENDINGS})",
            text
        )

        result = []
        buffer = ""

        for chunk in sentences:
            buffer += chunk
            if re.match(self.ENTENCE_ENDINGS, chunk):
                result.append(buffer.strip())
                buffer = ""

        if buffer:
            result.append(buffer.strip())

        return result