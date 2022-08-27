#!/bin/sh

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.8.12 -s
pyenv virtualenv -f 3.8.12 sabar_me
./update-deps.sh
