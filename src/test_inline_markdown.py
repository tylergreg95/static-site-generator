import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_links,
    split_nodes_images,
    text_to_textnodes
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_italic,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_link
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
        ]
        self.assertListEqual(new_nodes, expected)
    
    def test_extract_mardown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        result = extract_markdown_images(text)
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertListEqual(result, expected)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        result = extract_markdown_links(text)
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertListEqual(result, expected)

    def test_split_nodes_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png) and finally ![third image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsykjfd.png)"
        result = split_nodes_images([TextNode(text, text_type_text)])
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png"),
            TextNode(" and finally ", text_type_text),
            TextNode("third image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsykjfd.png")   
        ]
        self.assertListEqual(result, expected)

    def test_split_nodes_links(self):
        text = "This text contains a link [link](https://www.google.com) and another [link](https://www.website.com)."
        result = split_nodes_links([TextNode(text, text_type_text)])
        expected = [
            TextNode("This text contains a link ", text_type_text),
            TextNode("link", text_type_link, "https://www.google.com"),
            TextNode(" and another ", text_type_text),
            TextNode("link", text_type_link, "https://www.website.com"),
            TextNode(".", text_type_text)
        ]
        self.assertListEqual(result, expected)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertListEqual(nodes, expected)

if __name__ == "__main__":
    unittest.main()