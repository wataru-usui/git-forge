#!/usr/bin/env python3

from core import *

if __name__ == '__main__':
    init()

    blob_bytes = b''
    blob_digest = write_blob(blob_bytes)

    # git gives error on commit if you specify dates outside the range [0, 4102444800) via git commit --date or GIT_* environment variables.
    times = [0, 2 ** 63 - 1] # valid range is [0, 2^63), otherwise git gives error on push.

    tree = []

    for i, time in enumerate(times):
        tree.append({
            'type': b'100644',
            'name': b'%d' % time,
            'digest': blob_digest
        })
        tree_digest = write_tree(tree)

        commit = {
            'tree_digest': tree_digest,
            'parent_commit_digests': [] if i == 0 else [commit_digest],
            'author_name': b'',
            'author_email': b'',
            'author_time': time,
            'author_time_offset': b'+0000',
            'committer_name': b'',
            'committer_email': b'',
            'committer_time': time,
            'committer_time_offset': b'+0000',
            'commit_message': b''
        }
        commit_digest = write_commit(commit)

    write_head(commit_digest)
