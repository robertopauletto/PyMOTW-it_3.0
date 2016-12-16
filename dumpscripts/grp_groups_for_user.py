# grp_groups_for_user.py

import grp

username = 'robby'
group_names = set(
    g.gr_name
    for g in grp.getgrall()
    if username in g.gr_mem
)
print(username, 'appartiene a:', ', '.join(sorted(group_names)))
