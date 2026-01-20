import MeCab
from . import tools
from .tools.SentenceContext import SentenceContext
from ._posmap import jp_pos_to_kr


class NLPEngine:
    """
    The NLP Engine
    Mecab based NLPEngine
    """

    def __init__(self, mecab_args: str | None = None):
        self.splitter = tools.TextSplitter()
        self.sentences: list[SentenceContext] = []
        self.mecab = MeCab.Tagger(mecab_args) if mecab_args else MeCab.Tagger()

    def _split_into_sentences(self, text: str) -> None:
        """
        Split text into SentenceContext class
        """
        sentences = self.splitter.split(text)
        self.sentences = [
            SentenceContext(sentence_id=i, text=s)
            for i, s in enumerate(sentences)
            if tools.is_valid_sentence(s)
        ]

    def _analyze_sentence(self, ctx: SentenceContext) -> None:
        raw = self.mecab.parse(ctx.text)
        ctx.mecab_raw = raw

        tokens: list[dict] = []

        for line in raw.splitlines():
            if line == "EOS" or not line.strip():
                continue

            cols = line.split("\t")

            # Skip malformed
            if len(cols) < 5:
                continue

            surface = cols[0]
            reading = cols[1] if cols[1] else ""
            base = cols[3] if cols[3] and cols[3] != "*" else surface

            pos_full = cols[4]
            pos = pos_full.split("-")[0]

            token = {
                "surface": surface,  # 표면형
                "kanji": base,  # 표기
                "reading": reading,  # 읽는법
                "pos": jp_pos_to_kr(pos),  # 품사
            }

            tokens.append(token)

        ctx.tokens = tokens

    def analyze(self, text: str) -> None:
        """
        Public API
        """
        self.sentences.clear()
        self._split_into_sentences(text)

        for ctx in self.sentences:
            self._analyze_sentence(ctx)

    def pop_sentence(self) -> SentenceContext | None:
        """
        Pop an analyzed sentence result.
        """
        if not self.sentences:
            return None

        return self.sentences.pop(0)
