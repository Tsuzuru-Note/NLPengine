import json
import pytest
from nlp_engine.engine.nlpengine import NLPEngine

text = """
私は毎朝コーヒーを飲みます。
今日は天気が良いですね。
日本語の勉強は難しいですが、楽しいです。
来週、友達と東京へ行く予定です。
この本を読み終わったら、次の本を買うつもりです。
"""

engine = NLPEngine()

"""
    Part of PYTEST
"""
def test_nlpengine_basic():

    engine.analyze(text)

    sentences = engine.get_sentences()
    assert sentences is not None
    assert len(sentences) > 0

def test_nlpengine_pop_one_text():
    engine.analyze(text)

    result = engine.pop_sentence()

    assert result is not None

    if isinstance(result, str):
        text_value = result
    else:
        text_value = getattr(result, "text", None)

    assert isinstance(text_value, str)
    assert len(text_value) > 0

    print(f"[Result of col 1.] {text_value}")


if __name__ == '__main__':
    print(f"--------- analyze & pop test ---------")
    engine.analyze(text)
    while True:
        sentence = engine.pop_sentence()
        if sentence is None:
            break

        print(sentence)
    print("-------------------------------------------")
    print("--------- analyze all sentences ---------")
    engine.analyze(text)

    results = engine.get_sentences()
    #
    # for sentence in engine.sentences:
    #     engine._analyze_sentence(sentence)
    #     sentence_json = sentence_context_to_json(sentence)
    #     results["sentences"].append(sentence_json)
    #
    with open("analyze_result.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("-- Done to analyze all sentences --")