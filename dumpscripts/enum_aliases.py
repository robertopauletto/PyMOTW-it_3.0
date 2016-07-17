#enum_aliases.py

import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1


for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

print('\nUguale: by_design è wont_fix: ',
      BugStatus.by_design is BugStatus.wont_fix)
print('Uguale: closed è fix_released: ',
      BugStatus.closed is BugStatus.fix_released)
