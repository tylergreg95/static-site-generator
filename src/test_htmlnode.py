import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "This is a heading", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("h1", "This is a heading", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
    
    def test_props_to_html(self):
        node = HTMLNode("h1", "This is a heading", None, {"href": "https://www.google.com", "target": "_blank"})
        html = node.props_to_html()
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", html) 

class TestLeafNode(unittest.TestCase):

    def test_leaf_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        return self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_leaf_prop_eq(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        return self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

class TestParentNode(unittest.TestCase):
    def test_parent_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold ext"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
        )

        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold ext"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
        )

        self.assertEqual(node, node2)
    
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nested_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ]),
            ],
        )

        self.assertEqual(node.to_html(), "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")

    def test_multiple_nested_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ]),
                ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ]),
            ],
        )

        self.assertEqual(node.to_html(), "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")

    def test_multi_layer_nested_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                ParentNode("p", [
                    ParentNode("p", [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text")
                    ]),
                ]),
            ],
        )

        self.assertEqual(node.to_html(), "<p><p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p></p>")

if __name__ == "__main__":
    unittest.main()