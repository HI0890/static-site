import os
import sys
import shutil

from copydir import copy_directory_contents
from generatepage import generate_pages_recursive


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(root_dir, "static")
    dst = os.path.join(root_dir, "docs")
    copy_directory_contents(src, dst)

    content_dir = os.path.join(root_dir, "content")
    template_path = os.path.join(root_dir, "template.html")

    generate_pages_recursive(content_dir, template_path, dst, basepath)


if __name__ == "__main__":
    main()
