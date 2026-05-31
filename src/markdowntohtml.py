from block import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from splitnodes import text_to_textnodes
from textnode import TextNode, TextType
from texttohtml import text_node_to_html_node


def text_to_children(text: str) -> list[HTMLNode]:
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]


def _heading_block(block: str) -> HTMLNode:
    level = len(block.split(" ")[0])
    text = block[level + 1:]
    return ParentNode(f"h{level}", text_to_children(text))


def _code_block(block: str) -> HTMLNode:
    lines = block.split("\n")
    code_text = "\n".join(lines[1:-1]) + "\n"
    text_node = TextNode(code_text, TextType.TEXT)
    code_node = text_node_to_html_node(text_node)
    code_node.tag = "code"
    return ParentNode("pre", [code_node])


def _quote_block(block: str) -> HTMLNode:
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        if line.startswith("> "):
            cleaned.append(line[2:])
        else:
            cleaned.append(line[1:])
    text = " ".join(cleaned)
    return ParentNode("blockquote", text_to_children(text))


def _unordered_list_block(block: str) -> HTMLNode:
    items = block.split("\n")
    children = [ParentNode("li", text_to_children(item[2:])) for item in items]
    return ParentNode("ul", children)


def _ordered_list_block(block: str) -> HTMLNode:
    items = block.split("\n")
    children = [ParentNode("li", text_to_children(item[3:])) for item in items]
    return ParentNode("ol", children)


def _paragraph_block(block: str) -> HTMLNode:
    text = " ".join(block.split("\n"))
    return ParentNode("p", text_to_children(text))


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            children.append(_heading_block(block))
        elif block_type == BlockType.CODE:
            children.append(_code_block(block))
        elif block_type == BlockType.QUOTE:
            children.append(_quote_block(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(_unordered_list_block(block))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(_ordered_list_block(block))
        else:
            children.append(_paragraph_block(block))
    return ParentNode("div", children)
