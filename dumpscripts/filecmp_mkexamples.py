import os

def mkfile(filename, body=None):
    f = open(filename, 'w')
    try:
        f.write(body or filename)
    finally:
        f.close()
    return

def make_example_dir(top):
    if not os.path.exists(top):
        os.mkdir(top)
    curdir = os.getcwd()
    os.chdir(top)

    os.mkdir('dir1')
    os.mkdir('dir2')

    mkfile('dir1/file_solo_in_dir1')
    mkfile('dir2/file_solo_in_dir2')

    os.mkdir('dir1/dir_solo_in_dir1')
    os.mkdir('dir2/dir_solo_in_dir2')

    os.mkdir('dir1/dir_comune')
    os.mkdir('dir2/dir_comune')

    mkfile('dir1/file_comune', 'questo file è lo stesso')
    mkfile('dir2/file_comune', 'questo file è lo stesso')

    mkfile('dir1/non_lo_stesso')
    mkfile('dir2/non_lo_stesso')

    mkfile('dir1/file_in_dir1', 'Questo è un file in dir1')
    os.mkdir('dir2/file_in_dir1')
    
    os.chdir(curdir)
    return

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__) or os.getcwd())
    make_example_dir('esempio')
    make_example_dir('esempio/dir1/dir_comune')
    make_example_dir('esempio/dir2/dir_comune')