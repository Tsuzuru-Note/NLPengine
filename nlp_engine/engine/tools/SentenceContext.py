class SentenceContext:
    def __init__(self, sentence_id: int, text: str):
        self.sentence_id = sentence_id
        self.text = text

        self.mecab_raw: str | None = None
        self.tokens: list[dict] = []


    def __repr__(self):
        return (
            f"SentenceContext("
            f"sentence_id={self.sentence_id}, "
            f"text={repr(self.text)}, "
            f"tokens={len(self.tokens)}"
            f")\n"
        )