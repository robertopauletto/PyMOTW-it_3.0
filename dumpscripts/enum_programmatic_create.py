#enum_programmatic_create.py

import enum


BugStatus = enum.Enum(
    value='BugStatus',
    names=('fix_released fix_committed in_progress '
           'wont_fix invalid incomplete new'),
)

print('Membri: {}'.format(BugStatus.new))

print('\nTutti i membri:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))
