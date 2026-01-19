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


if __name__ == "__main__":
    splitter = TextSplitter()

    text = "今日は雨です。明日は晴れるでしょう！本当ですか？"
    sentences = splitter.split(text)

    print(sentences)
    print(type(sentences))
    print(len(sentences))

    contexts = [
        SentenceContext(sentence_id=i, text=s)
        for i, s in enumerate(sentences)
    ]

    print("=== SentenceContext Test ===")
    print(f"type: {type(contexts)}")
    print(f"count: {len(contexts)}")

    for ctx in contexts:
        print(ctx)