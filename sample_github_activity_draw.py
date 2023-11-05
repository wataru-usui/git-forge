#!/usr/bin/env python3

from core import *

if __name__ == '__main__':
    name = b'' # your name on github
    email = b'' # your email on github

    mask = [
        0, 0, 0,

        0, 1, 1, 1, 1, 1, 0,
        1, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 1, 0, 0, 1,
        1, 0, 0, 1, 0, 0, 1,
        0, 1, 0, 1, 1, 1, 1,

        0, 0, 0, 0, 0, 0, 0,

        0, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 1, 0, 0,
        1, 0, 0, 0, 1, 0, 0,
        1, 0, 0, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1,

        0, 0, 0, 0, 0, 0, 0,

        1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 1, 1,
        0, 0, 0, 1, 0, 0, 0,
        1, 1, 1, 0, 0, 0, 0,

        0, 0, 0, 0, 0, 0, 0,

        0, 1, 1, 0, 0, 1, 0,
        1, 0, 0, 1, 0, 0, 1,
        1, 0, 0, 1, 0, 0, 1,
        1, 0, 0, 1, 0, 0, 1,
        0, 1, 0, 0, 1, 1, 0,

        0, 0, 0, 0, 0, 0, 0,

        1, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 1, 0, 0, 1,
        1, 0, 0, 1, 0, 0, 1,
        1, 0, 0, 1, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 1,

        0, 0, 0, 0, 0, 0, 0,

        1, 1, 0, 0, 0, 1, 1,
        0, 0, 1, 0, 1, 0, 0,
        0, 0, 0, 1, 0, 0, 0,
        0, 0, 1, 0, 1, 0, 0,
        1, 1, 0, 0, 0, 1, 1,

        0, 0, 0, 0, 0, 0, 0,

        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,

        0, 0, 0, 0, 0, 0, 0,

        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,

        0, 0, 0, 0, 0, 0, 0,

        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,

        0, 0, 0, 0, 0
    ]

    # the github activity heatmap shows contributions adjusted to the viewer's local timezone.
    # in order to have them appear in the days we want across different timezones, we need to add an extra 12 hours.
    times1 = [60 * 60 * (24 * d + 12) for d in range(365)]

    times = []
    for i in range(365):
        if mask[i] != 0:
            times.append(times1[i])

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
