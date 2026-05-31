import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some raw text")
        self.assertEqual(node.to_html(), "Just some raw text")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Bold text")
        self.assertEqual(node.to_html(), "<b>Bold text</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Italic text")
        self.assertEqual(node.to_html(), "<i>Italic text</i>")

    def test_leaf_to_html_no_value_raises(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode(
            "a",
            "Link",
            {"href": "https://example.com", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://example.com" target="_blank">Link</a>',
        )

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello", {"class": "bold"})
        self.assertEqual(repr(node), "LeafNode(p, Hello, {'class': 'bold'})")

    def test_leaf_repr_no_props(self):
        node = LeafNode("b", "Bold")
        self.assertEqual(repr(node), "LeafNode(b, Bold, None)")


if __name__ == "__main__":
    unittest.main()
