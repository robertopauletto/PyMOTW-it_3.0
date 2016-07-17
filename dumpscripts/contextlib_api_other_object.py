# contextlib_api_other_object.py

class DentroIlContesto(object):

    def __init__(self, context):
        print('DentroIlContesto.__init__({})'.format(context))

    def do_something(self):
        print('DentroIlContesto.do_something()')

    def __del__(self):
        print('DentroIlContesto.__del__')


class Context:

    def __init__(self):
        print('Context.__init__()')

    def __enter__(self):
        print('Context.__enter__()')
        return DentroIlContesto(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context.__exit__()')

with Context() as c:
    c.do_something()
