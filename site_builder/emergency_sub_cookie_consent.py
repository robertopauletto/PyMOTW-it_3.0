
import os.path
import codecs

OLD = r'//s3.amazonaws.com/cc.silktide.com/cookieconsent.latest.min.js'
NEW = r'//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/cookieconsent.min.js'


for f in os.listdir(r'../html'):
    if f.endswith('html'):
        body = 
