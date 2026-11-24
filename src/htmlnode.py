class HTMLNode:
    def __init__(self, tag:str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str | None:
        if self.props is None or not self.props:
            return
        prop_html = ""
        for key, value in self.props.items():
            prop_html += f" {key}=\"{value}\""

        return prop_html

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("leaf node does not have a value")
        if self.tag is None or len(self.tag) == 0:
            return self.value
        if self.props_to_html() is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"