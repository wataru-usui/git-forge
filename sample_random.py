#!/usr/bin/env python3

import random

from core import *

if __name__ == '__main__':
    name = b'' # your name on github
    email = b'' # your email on github

    times = sorted([random.randint(0, 60 * 60 * 24 * 365 - 1) + 1672531200 for _ in range(365 * 10)])

    init()

    tree_digest = write_tree([])

    for i, time in enumerate(times):
        commit = {
            'tree_digest': tree_digest,
            'parent_commit_digests': [] if i == 0 else [commit_digest],
            'author_name': name,
            'author_email': email,
            'author_time': time,
            'author_time_offset': b'+0000',
            'committer_name': name,
            'committer_email': email,
            'committer_time': time,
            'committer_time_offset': b'+0000',
            'commit_message': b''
        }
        commit_digest = write_commit(commit)

    write_head(commit_digest)
