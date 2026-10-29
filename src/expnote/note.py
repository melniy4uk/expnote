class Note:
    def __init__(
        self,
        name: str,
        description: str | None = None,
    ) -> None:
        if not isinstance(name, str):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError("name должен быть строкой")

        if not name.strip():
            raise ValueError("name не может быть пустой строкой")

        if description is not None and not isinstance(description, str):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError("description должен быть строкой или None")

        self._name = name
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str | None:
        return self._description
