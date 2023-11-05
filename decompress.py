#!/usr/bin/env python3

import sys
import zlib

if __name__ == '__main__':
    sys.stdout.buffer.write(zlib.decompress(sys.stdin.buffer.read()))
