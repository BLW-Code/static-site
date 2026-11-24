from textnode import *
markdown_wrapper_delimiters = [
    "**",
    "_",
    "`",
]
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            new_nodes.append(node)
        node_text = node.text
        while delimiter in node_text:
            before_delimiter, after_delimiter = node_text.split(maxsplit=1)
            if before_delimiter:
                new_node = TextNode(before_delimiter, TextType.TEXT)
                new_nodes.append(new_node)

            if delimiter in markdown_wrapper_delimiters and delimiter not in after_delimiter:
                raise ValueError(f"Invalid Markdown: {node_text}")

            if delimiter in markdown_wrapper_delimiters and delimiter in after_delimiter:
                pass
            elif delimiter in after_delimiter:
                pass
            else:
                pass


            

    return new_nodes

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE) 
answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
for i, node in enumerate(new_nodes):
    print(node)
    print(answer[i] == new_nodes[i])      