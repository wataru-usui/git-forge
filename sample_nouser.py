#!/usr/bin/env python3

from core import *

if __name__ == '__main__':
    init()

    tree_digest = write_tree([])

    # git gives error on commit if you specify empty name or email via git config or GIT_* environment variables.
    commit = {
        'tree_digest': tree_digest,
        'parent_commit_digests': [],
        'author_name': b'',
        'author_email': b'',
        'author_time': 0,
        'author_time_offset': b'+0000',
        'committer_name': b'',
        'committer_email': b'',
        'committer_time': 0,
        'committer_time_offset': b'+0000',
        'commit_message': b''
    }
    commit_digest = write_commit(commit)

    write_head(commit_digest)
