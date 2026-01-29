import json
from .SentenceContext import SentenceContext


def sentence_context_to_json(ctx: SentenceContext) -> dict:
    return {
            "sentenceId": ctx.sentence_id,
            "sentence": ctx.text,
            "tokens": ctx.tokens
    }
