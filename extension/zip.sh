#!/bin/bash

rm -f recursive-learning.zip
zip -r recursive-learning.zip . -x \*README \*TODO *.git* \*.sh
