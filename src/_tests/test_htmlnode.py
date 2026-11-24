import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_html(self):
        answer = " href=\"https://www.boot.dev\" target=\"_blank\" class=\"btn btn-lg\""
        props = {
            "href": "https://www.boot.dev",
            "target": "_blank",
            "class": "btn btn-lg"
        }
        node = HTMLNode('a', 'read more', None, props)
        self.assertEqual(node.props_to_html(), answer)

    def test_empty_props(self):
        answer = None
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), answer)

    def test_empty_dict_props(self):
        answer = None
        props = {}
        node = HTMLNode('a', 'read more', None, props)
        self.assertEqual(node.props_to_html(), answer)

if __name__ == "__main__":
    unittest.main()