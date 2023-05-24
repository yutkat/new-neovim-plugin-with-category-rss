import argparse
import re

def get_header_hierarchy(file_path, line_number):
    with open(file_path, 'r') as f:
        lines = f.read().split("\n")

    if line_number > len(lines) or line_number < 1:
        return "Invalid line number"

    hierarchy = []
    for line in lines[:line_number]:
        if line.startswith("#"):
            level = line.count("#")
            header = line.lstrip("# ").strip()
            if header == "Table of Contents":
                continue
            if '[' in header and ']' in header and '(' in header and ')' in header:
                header_no_link = re.findall(r'\[(.*?)\]\(.*?\)', header)
                hierarchy = hierarchy[:level - 1] + [header_no_link[0]]
            else:
                hierarchy = hierarchy[:level - 1] + [header]

    return " > ".join(hierarchy)

def main():
    parser = argparse.ArgumentParser(description='Get header hierarchy from markdown.')
    parser.add_argument('file_path', type=str, help='Path to the markdown file')
    parser.add_argument('line_number', type=int, help='Line number to get header hierarchy')
    args = parser.parse_args()

    print('"' + get_header_hierarchy(args.file_path, args.line_number) + '"')

if __name__ == "__main__":
    main()
