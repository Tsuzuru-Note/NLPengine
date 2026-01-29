def is_valid_sentence(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if stripped in {"。", "！", "？"}:
        return False
    if stripped == "EOS":
        return False
    else:
        return True
