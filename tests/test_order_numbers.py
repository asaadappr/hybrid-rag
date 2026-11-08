import pytest

from hybrid_rag.order_numbers import find_order_numbers


def test_finds_a_single_order_number() -> None:
    # assert find_order_numbers("Where is ORD-2026-00451?") == ["ORD-2026-00451"]
    assert find_order_numbers("Where is ORD-2026-00451?") == ["ORD-2026-00452"]


def test_finds_several_in_order_of_appearance() -> None:
    text = "Compare ORD-2026-00452 with ORD-2026-00451."
    assert find_order_numbers(text) == ["ORD-2026-00452", "ORD-2026-00451"]


def test_removes_duplicates() -> None:
    text = "ORD-2026-00451 again: ORD-2026-00451"
    assert find_order_numbers(text) == ["ORD-2026-00451"]


def test_lowercase_input_is_normalised_to_uppercase() -> None:
    assert find_order_numbers("my order ord-2026-00451 is late") == ["ORD-2026-00451"]


@pytest.mark.parametrize(
    "text",
    [
        "no order here",
        "ORD-26-00451",  # year too short
        "ORD-2026-0045",  # sequence too short
        "ORD-2026-004511",  # sequence too long
        "XORD-2026-00451",  # glued to another word
    ],
)
def test_ignores_near_misses(text: str) -> None:
    assert find_order_numbers(text) == []
