import unittest

from markdowntohtml import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_h1(self):
        md = "# Heading One"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><h1>Heading One</h1></div>")

    def test_heading_h3(self):
        md = "### Heading Three"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><h3>Heading Three</h3></div>")

    def test_heading_h6(self):
        md = "###### Heading Six"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><h6>Heading Six</h6></div>")

    def test_heading_inline(self):
        md = "# Heading with **bold** and _italic_"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><h1>Heading with <b>bold</b> and <i>italic</i></h1></div>")

    def test_unordered_list(self):
        md = "- Item one\n- Item two\n- Item three"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>")

    def test_unordered_list_inline(self):
        md = "- Item with **bold**\n- Item with _italic_"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><ul><li>Item with <b>bold</b></li><li>Item with <i>italic</i></li></ul></div>")

    def test_ordered_list(self):
        md = "1. First\n2. Second\n3. Third"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>")

    def test_ordered_list_inline(self):
        md = "1. First **bold**\n2. Second _italic_"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><ol><li>First <b>bold</b></li><li>Second <i>italic</i></li></ol></div>")

    def test_quote(self):
        md = "> This is a quote"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><blockquote>This is a quote</blockquote></div>")

    def test_quote_multiline(self):
        md = "> Line one\n> Line two\n> Line three"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><blockquote>Line one Line two Line three</blockquote></div>")

    def test_quote_inline(self):
        md = "> A **bold** quote"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><blockquote>A <b>bold</b> quote</blockquote></div>")

    def test_multiple_blocks(self):
        md = "# Title\n\nParagraph here\n\n- List item"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><h1>Title</h1><p>Paragraph here</p><ul><li>List item</li></ul></div>")

    def test_plain_paragraph(self):
        md = "Just a plain paragraph"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><p>Just a plain paragraph</p></div>")

    def test_paragraph_with_link(self):
        md = "Click [here](https://boot.dev) to learn"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><p>Click <a href=\"https://boot.dev\">here</a> to learn</p></div>")

    def test_paragraph_with_image(self):
        md = "Look at ![alt text](https://example.com/img.png) here"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><p>Look at <img src=\"https://example.com/img.png\" alt=\"alt text\"> here</p></div>")

    def test_empty_markdown(self):
        md = ""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div></div>")


if __name__ == "__main__":
    unittest.main()
