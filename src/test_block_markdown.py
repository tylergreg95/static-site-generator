import unittest

from htmlnode import HTMLNode

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_heading,
    block_type_code,
    block_type_ordered_list,
    block_type_paragraph,
    block_type_quote,
    block_type_unordered_list,
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown ="""This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        expected = ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"]
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(expected, blocks)

    def test_markdown_to_blocks_multiple_blank_lines(self):
        markdown ="""This is **bolded** paragraph

        
This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items"""
        expected = ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"]
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(expected, blocks)
    
    def test_block_to_block_type_paragraph(self):
        markdown = """This is a paragraph
and this is another part of the same"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_paragraph)

    def test_block_to_block_type_heading(self):
        markdown = "# This is a heading"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_heading)

    def test_block_to_block_type_code(self):
        markdown = "``` This is some code that does things\nand some more things```"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_code)

    def test_block_to_block_type_quote(self):
        markdown = "> This is a quote\n> And here is the second part\n>And here is the last part"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_quote)
    
    def test_block_to_block_type_not_quote(self):
        markdown = "> This is a quote\n> And here is the second part\nAnd here is the last part"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_paragraph)

    def test_block_to_block_type_unordered_list(self):
        markdown = "* This is an item in an unordered list\n* And here is the second item\n* And here is the last item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_unordered_list)

    def test_block_to_block_type_unordered_list_hyphen(self):
        markdown = "- This is an item in an unordered list\n- And here is the second item\n- And here is the last item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_unordered_list)

    def test_block_to_block_type_not_unordered_list(self):
        markdown = "* This is an item in an unordered list\n And here is the second item\n* And here is the last item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_paragraph)

    def test_block_to_block_type_ordered_list(self):
        markdown = "1. This is an item in an unordered list\n2. And here is the second item\n3. And here is the last item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_ordered_list)
    
    def test_block_to_block_type_skip_number_ordered_list(self):
        markdown = "1. This is an item in an unordered list\n3. And here is the second item\n4. And here is the last item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_paragraph)
    
    def test_block_to_block_type_missing_number_ordered_list(self):
        markdown = "1. This is an item in an unordered list\n. And here is the second item\n3. And here is the last item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_paragraph)
    
    def test_block_to_block_type_misordered_number_ordered_list(self):
        markdown = "1. This is an item in an unordered list\n3. And here is the second item\n2. And here is the last item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_paragraph)
    
if __name__ == "__main__":
    unittest.main()