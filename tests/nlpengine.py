from engine.nlpengine import NLPEngine

text = """
私は毎朝コーヒーを飲みます。
今日は天気が良いですね。
日本語の勉強は難しいですが、楽しいです。
来週、友達と東京へ行く予定です。
この本を読み終わったら、次の本を買うつもりです。
"""

if __name__ == '__main__':
    engine = NLPEngine()
    result = engine._tokenize(text)
    print(result)