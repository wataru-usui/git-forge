#!/usr/bin/env python3

from core import *

if __name__ == '__main__':
    name = b'' # your name on github
    email = b'' # your email on github

    # github activity heatmap won't show you contributions made in the future anymore.
    # time calculation looks complicated because python doesn't even have standard library support for proper date arithmetic,
    # but what this is doing is stepping y years since 1970-01-01T12:00:00 while taking leap days into account.
    # the github activity heatmap shows contributions adjusted to the viewer's local timezone.
    # in order to have them appear in the days we want across different timezones, we need to add an extra 12 hours.
    times = [60 * 60 * (24 * (365 * y + (y + 1973) // 4 - (y + 2069) // 100 + (y + 2369) // 400 - 478) + 12) for y in range(130)]

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
