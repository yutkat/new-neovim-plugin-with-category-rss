import os
import glob
import datetime
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process some repos.')
    parser.add_argument('repo', type=str, help='')
    parser.add_argument('category', type=str, help='Path to the file containing repos')
    args = parser.parse_args()
    repo = args.repo
    category = args.category
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    output_file = args.repo.replace('/','--')
    cwd = os.getcwd()
    if glob.glob(f'{cwd}/_posts/????-??-??-{output_file}.html'):
        exit(1)
    filename = f'{cwd}/_posts/{date}-{output_file}.html'
    # Create a new file with the given name
    with open(filename, 'w') as f:
        f.write(f"""---
layout: default
title: {repo}
---
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; url='https://github.com/{repo}'" />
  </head>
  <body>
    {category}
  </body>
</html>
""")
        print(f"Add: {repo}")

if __name__ == "__main__":
    main()
