import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "This is a heading", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("h1", "This is a heading", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
    
    def test_props_to_html(self):
        node = HTMLNode("h1", "This is a heading", None, {"href": "https://www.google.com", "target": "_blank"})
        html = node.props_to_html()
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", html) 

    def test_leaf_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        return self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_leaf_prop_eq(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        return self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == "__main__":
    unittest.main()