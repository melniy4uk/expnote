from .base import Block


class TextBlock(Block):
    def __init__(self, content: str) -> None:

        if not isinstance(content, str):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError("content должен быть строкой")

        self._content = content

    @property
    def content(self) -> str:
        return self._content
