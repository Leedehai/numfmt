#!/usr/bin/env python

import sys
from hurry.filesize import size
print size(int(sys.argv[1]))
