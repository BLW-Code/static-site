import unittest
from src.htmlnode import HTMLNode, ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_to_html_without_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        parent_node.children = []

        with self.assertRaises(ValueError):
            parent_node.to_html()

        parent_node.children = None
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_siblings(self):
        answer = "<div><span>child number 1</span><span>child number 2</span><span>child number 3</span><span>child number 4</span><span>child number 5</span></div>"
        children_list : list[HTMLNode] = []
        for i in range(0, 5):
            new_child = LeafNode("span", f"child number {i + 1}")
            children_list.append(new_child)

        parent_node = ParentNode("div", children_list)
        self.assertEqual(parent_node.to_html(), answer)

    def test_to_html_with_cousins(self):
        answer = "<div><div class=\"d-flex justify-content-center\"><p class=\"text-bold\">Cousin 1</p></div><div class=\"d-flex justify-content-center\"><p class=\"text-bold\">Cousin 2</p></div><div class=\"d-flex justify-content-center\"><p class=\"text-bold\">Cousin 3</p></div><div class=\"d-flex justify-content-center\"><p class=\"text-bold\">Cousin 4</p></div><div class=\"d-flex justify-content-center\"><p class=\"text-bold\">Cousin 5</p></div></div>"
        children = []
        for i in range(0, 5):
            child_node = LeafNode("p", f"Cousin {i+1}", {"class":"text-bold"})
            parent_node = ParentNode("div", [child_node], {"class":"d-flex justify-content-center"})
            children.append(parent_node)
        grandparent_node = ParentNode("div", children)

        self.assertEqual(
            grandparent_node.to_html(),
            answer
        )

    def test_to_html_without_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        parent_node.tag = None

        with self.assertRaises(ValueError):
            parent_node.to_html()

        parent_node.tag = " "
        with self.assertRaises(ValueError):
            parent_node.to_html()

        parent_node.tag = ""
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()      