#!/bin/bash

docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp me/py3 pytest
