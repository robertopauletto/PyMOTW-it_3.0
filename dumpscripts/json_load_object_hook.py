# json_load_object_hook.py

import json


def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        print('MODULO:', module.__name__)
        class_ = getattr(module, class_name)
        print('CLASSE:', class_)
        args = {
            key: value
            for key, value in d.items()
        }
        print('ARGOMENTI DELL\'ISTANZA:', args)
        inst = class_(**args)
    else:
        inst = d
    return inst


encoded_object = '''
    [{"s": "Il valore dell'istanza va qui",
      "__module__": "json_myobj", "__class__": "MyObj"}]
    '''

myobj_instance = json.loads(
    encoded_object,
    object_hook=dict_to_object,
)
print(myobj_instance)
