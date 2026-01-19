import json
from engine.nlpengine import NLPEngine
from engine.tools.jsonpayload import sentence_context_to_json
text = """
私は毎朝コーヒーを飲みます。
今日は天気が良いですね。
日本語の勉強は難しいですが、楽しいです。
来週、友達と東京へ行く予定です。
この本を読み終わったら、次の本を買うつもりです。
"""


if __name__ == '__main__':
    engine = NLPEngine()
    engine._split_into_sentences(text)
    # result_tokenize = engine._tokenize(text)
    # print(f"_tokenize test : {result_tokenize}")
    print("-------------------------------------------")
    print(f"_split_into_sentences test : {engine.sentences}")

    print("--------- analyze all sentences ---------")

    results = {
        "sentences": []
    }

    for sentence in engine.sentences:
        engine._analyze_sentence(sentence)
        sentence_json = sentence_context_to_json(sentence)
        results["sentences"].append(sentence_json)

    with open("analyze_result.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("-- Done to analyze all sentences --")