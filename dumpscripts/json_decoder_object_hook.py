# json_decoder_object_hook.py

import json


class MyDecoder(json.JSONDecoder):

    def __init__(self):
        json.JSONDecoder.__init__(
            self,
            object_hook=self.dict_to_object,
        )

    def dict_to_object(self, d):
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
[{"s": "I valori dell'instanza vanno qui",
  "__module__": "json_myobj", "__class__": "MyObj"}]
'''

myobj_instance = MyDecoder().decode(encoded_object)
print(myobj_instance)
