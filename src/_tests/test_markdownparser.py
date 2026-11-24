import unittest
from src.textnode import *
from src.markdownparser import split_nodes_delimiter

class TestMarkdownParser(unittest.TestCase):
    def test_delimiter_not_present(self):
        answer = [
            TextNode("This is text with a code block word", TextType.TEXT)
        ]
        node = TextNode("This is text with a code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, answer)

    def test_single_code_block(self):
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        for i, node in enumerate(new_nodes):
            self.assertEqual(answer[i], new_nodes[i])