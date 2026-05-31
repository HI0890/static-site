import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ])

    def test_italic_delimiter(self):
        node = TextNode("This is text with an _italic phrase_ in the middle", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic phrase", TextType.ITALIC),
            TextNode(" in the middle", TextType.TEXT),
        ])

    def test_non_text_node_passed_through(self):
        node = TextNode("Already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [node])

    def test_no_delimiter_present(self):
        node = TextNode("Just plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [TextNode("Just plain text", TextType.TEXT)])

    def test_unmatched_delimiter_raises(self):
        node = TextNode("This has `an unmatched delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_multiple_delimiters(self):
        node = TextNode("Text `code1` and `code2` end", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("Text ", TextType.TEXT),
            TextNode("code1", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("code2", TextType.CODE),
            TextNode(" end", TextType.TEXT),
        ])

    def test_mixed_nodes(self):
        nodes = [
            TextNode("Normal text with **bold** inside", TextType.TEXT),
            TextNode("Already italic", TextType.ITALIC),
            TextNode("More `code` here", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        # First node gets split, second passes through, third has no ** so stays as-is
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], TextNode("Normal text with ", TextType.TEXT))
        self.assertEqual(result[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(result[2], TextNode(" inside", TextType.TEXT))
        self.assertEqual(result[3], TextNode("Already italic", TextType.ITALIC))
        self.assertEqual(result[4], TextNode("More `code` here", TextType.TEXT))

    def test_delimiter_at_start(self):
        node = TextNode("**bold** then text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("bold", TextType.BOLD),
            TextNode(" then text", TextType.TEXT),
        ])

    def test_delimiter_at_end(self):
        node = TextNode("text then **bold**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("text then ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ])

    def test_empty_list(self):
        result = split_nodes_delimiter([], "`", TextType.CODE)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
