#!/usr/bin/env python3

import hashlib
import os
import shutil
import subprocess
import zlib

def init():
    shutil.rmtree('.git', ignore_errors=True)
    subprocess.check_output('git init -b master'.split())

def encode_header(t, size):
    return b'%s %d\0' % (t, size)

def hash(obj_bytes):
    return hashlib.sha1(obj_bytes).digest()

def encode_commit(content):
    content_bytes = b''
    content_bytes += b'tree %s\n' % content['tree_digest'].hex().encode('ascii')
    for parent_commit_digest in content['parent_commit_digests']:
        content_bytes += b'parent %s\n' % parent_commit_digest.hex().encode('ascii')
    content_bytes += b'author %s <%s> %d %s\n' % (content['author_name'], content['author_email'], content['author_time'], content['author_time_offset'])
    content_bytes += b'committer %s <%s> %d %s\n' % (content['committer_name'], content['committer_email'], content['committer_time'], content['committer_time_offset'])
    content_bytes += b'\n' # probably marks the beginning of the commit message.
    content_bytes += b'%s\n' % content['commit_message']
    return content_bytes

def encode_tree(content):
    content_sorted = sorted(content, key=lambda x: x['name']) # tree object entries have to be sorted, otherwise git gives error on push.
    content_bytes = b''
    for entry in content_sorted:
        content_bytes += b'%s %s\0%s' % (entry['type'], entry['name'], entry['digest'])
    return content_bytes

def write(obj_bytes, digest):
    digest_hex = digest.hex().encode('ascii')
    dirname = os.path.join(b'.git/objects', digest_hex[:2])
    path = os.path.join(dirname, digest_hex[2:])
    os.makedirs(dirname, exist_ok=True)
    with open(path, 'wb') as f:
        f.write(zlib.compress(obj_bytes))

def write_head(digest):
    digest_hex = digest.hex().encode('ascii')
    with open('.git/refs/heads/master', 'wb') as f:
        f.write(b'%s\n' % digest_hex)

def write_commit(content):
    content_bytes = encode_commit(content)
    header_bytes = encode_header(b'commit', len(content_bytes))
    obj_bytes = header_bytes + content_bytes
    digest = hash(obj_bytes)
    write(obj_bytes, digest)
    return digest

def write_tree(content):
    content_bytes = encode_tree(content)
    header_bytes = encode_header(b'tree', len(content_bytes))
    obj_bytes = header_bytes + content_bytes
    digest = hash(obj_bytes)
    write(obj_bytes, digest)
    return digest

def write_blob(content_bytes):
    header_bytes = encode_header(b'blob', len(content_bytes))
    obj_bytes = header_bytes + content_bytes
    digest = hash(obj_bytes)
    write(obj_bytes, digest)
    return digest
