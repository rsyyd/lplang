# minimal html templating for lumpo

def html(strings, *values):
    """template literal‑style HTML.
    ``strings`` is a tuple of literal parts, ``values`` are interpolated.
    Returns a single string.
    """
    parts = []
    for s, v in zip(strings, values):
        parts.append(s)
        parts.append(str(v))
    parts.append(strings[-1])
    return ''.join(parts)
