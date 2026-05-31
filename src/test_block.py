import unittest

from block import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_block(self):
        md = "This is a single paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single paragraph"])

    def test_multiple_newlines(self):
        md = "Block one\n\n\n\nBlock two"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block one", "Block two"])

    def test_leading_trailing_newlines(self):
        md = "\n\nBlock one\n\nBlock two\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block one", "Block two"])

    def test_empty_string(self):
        blocks = markdown_to_blocks("")
        self.assertEqual(blocks, [])

    def test_only_whitespace(self):
        blocks = markdown_to_blocks("   \n\n   \n\n   ")
        self.assertEqual(blocks, [])

    def test_blocks_with_internal_newlines(self):
        md = "# Heading\n\nLine 1\nLine 2\nLine 3\n\n- Item 1\n- Item 2"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "# Heading",
            "Line 1\nLine 2\nLine 3",
            "- Item 1\n- Item 2",
        ])

    def test_code_block_preserved(self):
        md = "Text before\n\n```\ncode here\nmore code\n```\n\nText after"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "Text before",
            "```\ncode here\nmore code\n```",
            "Text after",
        ])


if __name__ == "__main__":
    unittest.main()
