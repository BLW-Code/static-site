import unittest
from src.textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("This is a text node", TextType.CODE, None)
        node2 = TextNode("This is a text node", TextType.CODE, None)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev/dashboard")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev/dashboard")
        self.assertEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text nodes", TextType.ITALIC, "https://www.boot.dev/dashboard")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev/dashboard")
        self.assertNotEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev/dashboard")
        self.assertNotEqual(node, node2)

    def test_neq_text_type(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev/dashboard")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev/dashboard")
        self.assertNotEqual(node, node2)

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_to_html(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic_to_html(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>This is a italic node</i>")

    def test_code_to_html(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link_to_html(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<a href=\"https://www.boot.dev\">This is a link node</a>")

    def test_img_to_html(self):
            node = TextNode("This is a image node", TextType.IMAGE, "https://www.boot.dev")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.to_html(), "<img src=\"https://www.boot.dev\" alt=\"This is a image node\"></img>")
    

if __name__ == "__main__":
    unittest.main()