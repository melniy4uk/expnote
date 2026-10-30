import pytest

from expnote.blocks.base import Block
from expnote.blocks.text import TextBlock


def test_text_block_creation() -> None:
    block = TextBlock("Текст")

    assert block.content == "Текст"


def test_text_block_empty() -> None:
    block = TextBlock("")

    assert block.content == ""


def test_text_block_whitespace() -> None:
    block = TextBlock("   ")

    assert block.content == "   "


@pytest.mark.parametrize("content", [None, 123, 1.5, True, [], {}])
def test_text_block_invalid_type(content: object) -> None:
    with pytest.raises(TypeError):
        TextBlock(content)  # pyright: ignore[reportArgumentType]


def test_text_block_read_only() -> None:
    block = TextBlock("Текст")

    with pytest.raises(AttributeError):
        block.content = "Новый текст"  # pyright: ignore[reportAttributeAccessIssue]


def test_text_block_inheritance() -> None:
    block = TextBlock("Текст")

    assert isinstance(block, Block)
