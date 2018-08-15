# with_os.sh

#!/bin/sh

export PYTHONPATH=so_${1}
echo "PYTHONPATH=$PYTHONPATH"
echo

python3 pkgutil_os_specific.py
