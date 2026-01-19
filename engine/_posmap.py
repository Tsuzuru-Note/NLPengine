_jp_ko_pos_map_ = {
    # Nominals
    "名詞": "명사",
    "代名詞": "대명사",
    "数詞": "수사",
    "固有名詞": "고유명사",

    # Predicatives
    "動詞": "동사",
    "形容詞": "형용사",
    "形容動詞": "형용사",# な adjective
    "助動詞": "동사",

    # Modifiers
    "副詞": "부사",
    "連体詞": "관형사",

    # Particles
    "助詞": "조사",
    "係助詞": "조사",
    "接続助詞": "조사",
    "格助詞": "조사",
    "副助詞": "조사",
    "終助詞": "조사",

    # Independents
    "接続詞": "접속사",
    "感動詞": "감탄사",

    # Other
    "記号": "기호",
    "補助記号": "기호",
    "フィラー": "기타",
    "その他": "기타",
    "未知語": "기타",
}

def jp_pos_to_kr(pos: str) -> str:
    """
    Convert POS JP -> KR

    FIXME: Mecab pos DB 참고하기.
    """
    return _jp_ko_pos_map_.get(pos, pos)