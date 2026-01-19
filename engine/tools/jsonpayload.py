import json
from .SentenceContext import SentenceContext


def sentence_context_to_json(ctx: SentenceContext) -> dict:
    return {
        "sentence": {
            "id": ctx.sentence_id,
            "text": ctx.text
        },
        "tokens": ctx.tokens
    }
