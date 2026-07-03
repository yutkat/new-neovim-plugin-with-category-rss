# new-neovim-plugin-with-category-rss

RSS feed for newly added Neovim plugin repositories from
[yutkat/my-neovim-pluginlist](https://github.com/yutkat/my-neovim-pluginlist),
with the category hierarchy from the source list.

Feed: <https://yutkat.github.io/new-neovim-plugin-with-category-rss/feed>

## Overview

This repository publishes a small Jekyll site for GitHub Pages. Each generated
post represents one Neovim plugin repository, redirects to that repository on
GitHub, and keeps the plugin category in the page body so it can appear in the
RSS feed.

Generated posts live in `_posts/` and use this filename format:

```text
YYYY-MM-DD-owner--repository.html
```

## How it works

1. `.github/workflows/new_repo.yml` runs manually or from a
   `repository_dispatch` event named `trigger-new-repo`.
2. The workflow checks out `yutkat/my-neovim-pluginlist` into
   `my-neovim-pluginlist/`.
3. `scripts/get_updated_repo.sh` finds GitHub links added in the latest
   non-merge commit whose subject matches `Add`.
4. `python/generate_header_hierarchy.py` reads the Markdown heading hierarchy
   around each added link and turns it into a category path.
5. `python/create_post.py` creates a Jekyll post that redirects to the plugin
   repository and stores the category path in the HTML body.
6. `.github/workflows/pages.yml` builds and deploys the Jekyll site to GitHub
   Pages.
