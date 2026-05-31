import unittest

from block import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    # --- Headings ---
    def test_heading_h1(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)

    def test_heading_h6(self):
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_heading_h7_not_heading(self):
        self.assertEqual(block_to_block_type("####### Not a heading"), BlockType.PARAGRAPH)

    def test_heading_no_space(self):
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)

    def test_heading_h3(self):
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)

    # --- Code ---
    def test_code_block(self):
        block = "```\ncode here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_multiline(self):
        block = "```\nline 1\nline 2\nline 3\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_no_closing(self):
        block = "```\ncode here"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block_no_opening(self):
        block = "code here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # --- Quote ---
    def test_quote_single(self):
        self.assertEqual(block_to_block_type("> Quote text"), BlockType.QUOTE)

    def test_quote_multiline(self):
        block = "> Line 1\n> Line 2\n> Line 3"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_no_space(self):
        self.assertEqual(block_to_block_type(">Quote"), BlockType.QUOTE)

    def test_quote_one_line_missing_prefix(self):
        block = "> Line 1\nLine 2\n> Line 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # --- Unordered list ---
    def test_unordered_list_single(self):
        self.assertEqual(block_to_block_type("- Item"), BlockType.UNORDERED_LIST)

    def test_unordered_list_multiline(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_missing_space(self):
        self.assertEqual(block_to_block_type("-Item"), BlockType.PARAGRAPH)

    def test_unordered_list_one_line_missing_dash(self):
        block = "- Item 1\nItem 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # --- Ordered list ---
    def test_ordered_list_single(self):
        self.assertEqual(block_to_block_type("1. Item"), BlockType.ORDERED_LIST)

    def test_ordered_list_multiline(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_start(self):
        block = "2. First\n3. Second"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_skipped_number(self):
        block = "1. First\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_missing_space(self):
        self.assertEqual(block_to_block_type("1.Item"), BlockType.PARAGRAPH)

    def test_ordered_list_many_items(self):
        block = "\n".join(f"{i}. Item {i}" for i in range(1, 6))
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    # --- Paragraph ---
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph"), BlockType.PARAGRAPH)

    def test_paragraph_multiline(self):
        block = "Line 1\nLine 2\nLine 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
