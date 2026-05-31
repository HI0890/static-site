import unittest

from generatepage import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_h1_with_extra_whitespace(self):
        self.assertEqual(extract_title("#   Hello World  "), "Hello World")

    def test_h1_among_other_lines(self):
        md = "Some text\n# My Title\nMore text"
        self.assertEqual(extract_title(md), "My Title")

    def test_h1_first_line(self):
        md = "# Tolkien Fan Club\n\nSome paragraph"
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    def test_no_h1_raises(self):
        md = "Just a paragraph\n## Heading 2"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_h2_not_h1(self):
        md = "## Not an h1"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            extract_title("")

    def test_h1_with_inline_markdown(self):
        md = "# **Bold Title**"
        self.assertEqual(extract_title(md), "**Bold Title**")


if __name__ == "__main__":
    unittest.main()
