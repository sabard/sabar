#!/bin/sh

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.10.14 -s
pyenv virtualenv -f 3.10.14 sabar_me
./update-deps.sh
