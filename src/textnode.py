from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = None
    ITALIC = "i"
    BOLD = "b"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode:
    def __init__(self, text:str, text_type:TextType, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, TextNode):
            return NotImplemented

        return (self.text, self.text_type, self.url) == (value.text, value.text_type, value.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match(text_node.text_type):
        case TextType.LINK:
            props = {"href": text_node.url}
            return LeafNode(text_node.text_type.value, text_node.text, props)
        case TextType.IMAGE:
            props = {
                "src": text_node.url,
                "alt": text_node.text
            }
            return LeafNode(text_node.text_type.value, "", props)
        case _:
            return LeafNode(text_node.text_type.value, text_node.text)