import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_image, split_nodes_link


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_single(self):
        node = TextNode("Text before ![alt](https://example.com/img.png) text after", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("Text before ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" text after", TextType.TEXT),
        ], new_nodes)

    def test_split_images_no_images(self):
        node = TextNode("Just plain text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("Just plain text", TextType.TEXT)], new_nodes)

    def test_split_images_non_text_passed_through(self):
        node = TextNode("Already bold", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_images_only_image(self):
        node = TextNode("![alt](https://example.com/img.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
        ], new_nodes)

    def test_split_images_image_at_start(self):
        node = TextNode("![alt](https://example.com/img.png) then text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" then text", TextType.TEXT),
        ], new_nodes)

    def test_split_images_image_at_end(self):
        node = TextNode("text then ![alt](https://example.com/img.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("text then ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
        ], new_nodes)

    def test_split_images_empty_list(self):
        new_nodes = split_nodes_image([])
        self.assertListEqual([], new_nodes)

    def test_split_images_mixed_nodes(self):
        nodes = [
            TextNode("![pic](https://example.com/a.png) text", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual([
            TextNode("pic", TextType.IMAGE, "https://example.com/a.png"),
            TextNode(" text", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ], new_nodes)


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ], new_nodes)

    def test_split_links_single(self):
        node = TextNode("Click [here](https://example.com) now", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("Click ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://example.com"),
            TextNode(" now", TextType.TEXT),
        ], new_nodes)

    def test_split_links_no_links(self):
        node = TextNode("Just plain text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("Just plain text", TextType.TEXT)], new_nodes)

    def test_split_links_non_text_passed_through(self):
        node = TextNode("Already bold", TextType.BOLD)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links_only_link(self):
        node = TextNode("[anchor](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("anchor", TextType.LINK, "https://example.com"),
        ], new_nodes)

    def test_split_links_link_at_start(self):
        node = TextNode("[anchor](https://example.com) then text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("anchor", TextType.LINK, "https://example.com"),
            TextNode(" then text", TextType.TEXT),
        ], new_nodes)

    def test_split_links_link_at_end(self):
        node = TextNode("text then [anchor](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("text then ", TextType.TEXT),
            TextNode("anchor", TextType.LINK, "https://example.com"),
        ], new_nodes)

    def test_split_links_empty_list(self):
        new_nodes = split_nodes_link([])
        self.assertListEqual([], new_nodes)

    def test_split_links_does_not_match_images(self):
        node = TextNode("![image](https://example.com/img.png) and [link](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("![image](https://example.com/img.png) and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ], new_nodes)

    def test_split_links_mixed_nodes(self):
        nodes = [
            TextNode("[link](https://example.com) text", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual([
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" text", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ], new_nodes)


if __name__ == "__main__":
    unittest.main()
