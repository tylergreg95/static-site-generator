import unittest

from block_markdown import (
    markdown_to_blocks,
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