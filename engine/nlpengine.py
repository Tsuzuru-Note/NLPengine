import MeCab
from ._posmap import _jp_ko_pos_map_

class NLPEngine:
    """
    The NLP Engine

    """
    def __init__(self):
        self.mecab = MeCab.Tagger()

    def _tokenize(self, text:str):
        return self.mecab.parse(text)
