from fastapi.testclient import TestClient
from nlp_engine.server import app

client = TestClient(app)

def test_nlpengine_server_ok():
    res = client.post(
        "/nlpengine/",
        json={"text": "今日はうどんを食べました。"}
    )

    print(res.json())

    assert res.status_code == 200
    assert "sentences" in res.json()

def test_nlpengine_server_error():
    res = client.post(
        "/nlpengine/",
        json={"text": ""}
    )

    data = res.json()
    print("\nNLP server None data ERROR Test")
    print(data)

    assert res.status_code == 400
    assert "detail" in data
    assert data["detail"] == "Bad Request..."