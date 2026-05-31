import unittest

from textnode import TextNode, TextType
from splitnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_full_markdown(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_plain_text(self):
        text = "Just plain text nothing special"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("Just plain text nothing special", TextType.TEXT),
        ])

    def test_only_bold(self):
        self.assertListEqual(text_to_textnodes("**bold**"), [
            TextNode("bold", TextType.BOLD),
        ])

    def test_only_italic(self):
        self.assertListEqual(text_to_textnodes("_italic_"), [
            TextNode("italic", TextType.ITALIC),
        ])

    def test_only_code(self):
        self.assertListEqual(text_to_textnodes("`code`"), [
            TextNode("code", TextType.CODE),
        ])

    def test_only_image(self):
        self.assertListEqual(text_to_textnodes("![alt](https://example.com/img.png)"), [
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
        ])

    def test_only_link(self):
        self.assertListEqual(text_to_textnodes("[click](https://example.com)"), [
            TextNode("click", TextType.LINK, "https://example.com"),
        ])

    def test_bold_and_italic(self):
        self.assertListEqual(text_to_textnodes("**bold** and _italic_"), [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ])

    def test_empty_string(self):
        self.assertListEqual(text_to_textnodes(""), [])


if __name__ == "__main__":
    unittest.main()
