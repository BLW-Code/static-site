import unittest
from src.htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_exception(self):
        node = LeafNode(None, "Hello, world!")
        node.value = ""
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_a(self):
        answer = "<a href=\"https://www.boot.dev\" target=\"_blank\" class=\"btn btn-lg\">read more</a>"
        props = {
            "href": "https://www.boot.dev",
            "target": "_blank",
            "class": "btn btn-lg"
        }
        node = LeafNode('a', 'read more', props)
        self.assertEqual(node.to_html(), answer)