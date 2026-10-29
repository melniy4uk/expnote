import pytest

from expnote.note import Note


def test_note_creation() -> None:
    note = Note(name="Имя", description="Описание")

    assert note.name == "Имя"
    assert note.description == "Описание"


def test_note_without_description() -> None:
    note = Note(name="Имя")

    assert note.name == "Имя"
    assert note.description is None


def test_note_empty_description() -> None:
    note = Note(name="Имя", description="")

    assert note.description == ""


@pytest.mark.parametrize(
    "name",
    ["", " ", "   ", "\t", "\n"],
)
def test_note_invalid_name(name: str) -> None:
    with pytest.raises(ValueError):
        Note(name=name)


@pytest.mark.parametrize(
    "name",
    [None, 123, 1.5, True, [], {}],
)
def test_note_invalid_name_type(name: object) -> None:
    with pytest.raises(TypeError):
        Note(name=name)  # pyright: ignore[reportArgumentType]


@pytest.mark.parametrize(
    "description",
    [123, 1.5, True, [], {}],
)
def test_note_invalid_description_type(description: object) -> None:
    with pytest.raises(TypeError):
        Note(name="Имя", description=description)  # pyright: ignore[reportArgumentType]


def test_note_preserves_name() -> None:
    note = Note(name="  Исследование  ")

    assert note.name == "  Исследование  "


def test_note_read_only_name() -> None:
    note = Note(name="Имя")

    with pytest.raises(AttributeError):
        note.name = "Новое имя"  # pyright: ignore[reportAttributeAccessIssue]


def test_note_read_only_description() -> None:
    note = Note(name="Имя", description="Описание")

    with pytest.raises(AttributeError):
        note.description = "Новое описание"  # pyright: ignore[reportAttributeAccessIssue]
