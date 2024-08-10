#!/bin/bash

export GITHUB_TOKEN
VENV="$(pwd)/venv"
export VENV

make clean
make clean-docs
make venv
make api
"$VENV/bin/pip" install -e '.[docs]'

export PYTHONPATH="$(pwd):$PYTHONPATH"

"$VENV/bin/python" compiler/docs/compiler.py

"$VENV/bin/sphinx-build" -b html "docs/source" "docs/build/html" -j auto

git clone https://5hojib:"$GITHUB_TOKEN"@github.com/5hojib/Electrogram-docs.git
cd Electrogram-docs

rm -rf _includes api genindex.html intro py-modindex.html sitemap.xml \
       support.html topics _static faq index.html objects.inv \
       searchindex.js start telegram

cp -r ../docs/build/html/* .
git config --local user.name "5hojib"
git config --local user.email "yesiamshojib@gmail.com"
git add --all
git commit -m "Update docs" --signoff
git checkout --orphan x
git commit -m "Update docs" --signoff
git branch -D main
git branch -m main
git push --force origin main