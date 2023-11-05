#!/usr/bin/env python3

from core import *

if __name__ == '__main__':
    name = b'Linus Torvalds'
    email = b'torvalds@linux-foundation.org'

    init()

    blob_bytes = b'content\n'
    blob_digest = write_blob(blob_bytes)

    tree = [
        {
            'type': b'100644',
            'name': b'note.txt',
            'digest': blob_digest
        }
    ]
    tree_digest = write_tree(tree)

    commit = {
        'tree_digest': tree_digest,
        'parent_commit_digests': [],
        'author_name': name,
        'author_email': email,
        'author_time': 0,
        'author_time_offset': b'+0000',
        'committer_name': name,
        'committer_email': email,
        'committer_time': 0,
        'committer_time_offset': b'+0000',
        'commit_message': b'initial commit'
    }
    commit_digest = write_commit(commit)

    write_head(commit_digest)
