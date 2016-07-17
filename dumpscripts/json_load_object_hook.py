import json

def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        print 'MODULO:', module
        class_ = getattr(module, class_name)
        print 'CLASSE:', class_
        args = dict( (key.encode('ascii'), value) for key, value in d.items())
        print 'PARAMETRI ISTANZA:', args
        inst = class_(**args)
    else:
        inst = d
    return inst

encoded_object = '[{"s": "Il valore di istanza va qui", "__module__": "json_myobj", "__class__": "MyObj"}]'

myobj_instance = json.loads(encoded_object, object_hook=dict_to_object)
print myobj_instance
