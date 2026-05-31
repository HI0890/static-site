import os


def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No h1 header found in markdown")


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    from markdowntohtml import markdown_to_html_node
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(page)


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        if os.path.isfile(src_path):
            dest_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))
            generate_page(src_path, template_path, dest_path)
        else:
            generate_pages_recursive(src_path, template_path, os.path.join(dest_dir_path, item))
