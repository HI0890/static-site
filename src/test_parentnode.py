import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "text")]).to_html()

    def test_to_html_no_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_to_html_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "hello")],
            {"class": "container", "id": "main"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main"><p>hello</p></div>',
        )

    def test_to_html_deeply_nested(self):
        inner = LeafNode("b", "deep")
        mid = ParentNode("span", [inner])
        outer = ParentNode("section", [mid])
        root = ParentNode("main", [outer])
        self.assertEqual(
            root.to_html(),
            "<main><section><span><b>deep</b></span></section></main>",
        )

    def test_to_html_multiple_parents_as_children(self):
        node = ParentNode(
            "ul",
            [
                ParentNode("li", [LeafNode(None, "Item 1")]),
                ParentNode("li", [LeafNode(None, "Item 2")]),
                ParentNode("li", [LeafNode(None, "Item 3")]),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>",
        )

    def test_to_html_mixed_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("h1", "Title"),
                LeafNode(None, "Some plain text"),
                ParentNode("p", [LeafNode("a", "link", {"href": "https://example.com"})]),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<div><h1>Title</h1>Some plain text<p><a href="https://example.com">link</a></p></div>',
        )

    def test_repr(self):
        node = ParentNode("div", [LeafNode("p", "hi")], {"class": "wrapper"})
        self.assertEqual(
            repr(node),
            "ParentNode(div, [LeafNode(p, hi, None)], {'class': 'wrapper'})",
        )


if __name__ == "__main__":
    unittest.main()
