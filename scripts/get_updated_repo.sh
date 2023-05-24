#!/bin/bash

list=$(cd my-neovim-pluginlist && git diff --minimal -u --unified=0 $(git log --grep="Add" --no-merges --oneline -1 --pretty=%H)^\! [a-z]*.md | grep github.com | grep "^+" | grep -oP '\(https://github.com/[^)]+\)' | tr -d '()')

for l in $list; do
	r=$(echo $l | sed 's#https://github.com/##g')
	target=$(grep -n $l my-neovim-pluginlist/[a-z]*.md | awk -F: '{print " " $1, $2}')
	args=$(python python/generate_header_hierarchy.py $target)
	echo "$r $args"
	python python/create_post.py $r "${args}"
done
