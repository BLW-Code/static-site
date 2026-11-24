class HTMLNode:
    def __init__(self, tag:str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None ) -> None:
        self.tag = tag.strip() if isinstance(tag, str) else None
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
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError(f"LeafNode does not have a value: {self}")
        if self.tag is None or len(self.tag.strip()) == 0:
            return self.value
        if self.props_to_html() is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] = None) -> None:
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def to_html(self) -> str:
        if self.tag is None or len(self.tag.strip()) == 0:
            raise ValueError(f"ParentNode must have a tag value: {self}")

        if self.children is None or len(self.children) == 0:
            raise ValueError(f"ParentNode must have children: {self}")

        if self.props_to_html():
            start_tag = f"<{self.tag}{self.props_to_html()}>"
        else:
            start_tag = f"<{self.tag}>"
        end_tag = f"</{self.tag}>"

        inner_content = ""
        for child in self.children:
            inner_content += child.to_html()

        return start_tag + inner_content + end_tag