"""Find order numbers like ORD-2026-00451 inside free text."""

import re

# ORD, a 4-digit year, a 5-digit sequence. The lookarounds stop us matching
# inside a longer token such as XORD-2026-00451 or ORD-2026-004511.
ORDER_NUMBER_PATTERN = re.compile(r"(?<![A-Za-z0-9])ORD-\d{4}-\d{5}(?!\d)", re.IGNORECASE)


def find_order_numbers(text: str) -> list[str]:
    """Return every order number in ``text``, upper-cased, de-duplicated, in order of appearance."""
    seen: dict[str, None] = {}
    for match in ORDER_NUMBER_PATTERN.finditer(text):
        seen.setdefault(match.group(0).upper(), None)
    return list(seen)
