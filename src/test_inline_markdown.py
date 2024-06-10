import unittest
from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_italic,
    text_type_bold,
    text_type_code
)

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        self.assertListEqual(new_nodes, expected)
    
    def test_split_nodes_italic_delimiter(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_nodes_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_nodes_bold_double_delimiter(self):
        node = TextNode("This is text with a **bold** word and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word and ", text_type_text),
            TextNode("another", text_type_bold),
            TextNode("", text_type_text),
        ]
        self.assertListEqual(new_nodes, expected)