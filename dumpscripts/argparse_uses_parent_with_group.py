# argparse_uses_parent_with_group.py

import argparse
import argparse_parent_with_group

parser = argparse.ArgumentParser(
    parents=[argparse_parent_with_group.parser],
)

parser.add_argument('--locale-arg',
                    action="store_true",
                    default=False)

print(parser.parse_args())
