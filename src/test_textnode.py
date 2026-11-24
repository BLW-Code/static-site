import unittest
from textnode import TextNode, TextType


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
        node = TextNode("This is a text node", TextType.PLAIN, "https://www.boot.dev/dashboard")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev/dashboard")
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()