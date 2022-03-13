#!/bin/sh

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv activate sabar_me

pip install --upgrade setuptools pip
pip install wheel pip-tools

pip-compile "$@"
pip-sync requirements.txt