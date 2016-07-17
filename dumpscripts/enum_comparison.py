#enum_comparison.py

import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Uguaglianza:',
      actual_state == desired_state,
      actual_state == BugStatus.wont_fix)
print('Identità   :',
      actual_state is desired_state,
      actual_state is BugStatus.wont_fix)
print('Ordinati per valore:')
try:
    print('\n'.join('  ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print('  Non ordinabili: {}'.format(err))
