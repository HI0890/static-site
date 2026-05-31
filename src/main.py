import os
import shutil

from copydir import copy_directory_contents
from generatepage import generate_pages_recursive


def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(root_dir, "static")
    dst = os.path.join(root_dir, "public")
    copy_directory_contents(src, dst)

    content_dir = os.path.join(root_dir, "content")
    template_path = os.path.join(root_dir, "template.html")

    generate_pages_recursive(content_dir, template_path, dst)


if __name__ == "__main__":
    main()
