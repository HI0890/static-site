from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    # Heading: starts with 1-6 # followed by a space
    if lines[0].startswith("#"):
        prefix = lines[0].split(" ")[0]
        if 1 <= len(prefix) <= 6 and all(c == "#" for c in prefix):
            return BlockType.HEADING

    # Code block: starts and ends with 3 backticks
    if block.startswith("```") and block.endswith("```") and len(lines) >= 2:
        return BlockType.CODE

    # Quote: every line starts with >
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list: every line starts with - followed by a space
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list: every line starts with N. where N increments from 1
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]
