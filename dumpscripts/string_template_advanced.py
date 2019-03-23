# string_template_advanced.py

import string


class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'


template_text = '''
  Delimitatore: %%
  Sostituito  : %with_underscore
  Ignorato    : %notunderscored
'''

d = {
    'with_underscore': 'sostituito',
    'notunderscored': 'non sostituito',
}

t = MyTemplate(template_text)
print('Modificato il modello ID:')
print(t.safe_substitute(d))
