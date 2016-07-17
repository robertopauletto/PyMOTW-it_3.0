import os
import tempfile

directory_name = tempfile.mkdtemp()
print directory_name
# Lo script elimina la directory
os.removedirs(directory_name)
