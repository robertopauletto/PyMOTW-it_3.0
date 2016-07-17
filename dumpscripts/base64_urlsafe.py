import base64

for original in [ chr(251) + chr(239), chr(255) * 2 ]:
    print 'Originale        :', repr(original)
    print 'Codifica standard:', base64.standard_b64encode(original)
    print 'Codifica URL-safe:', base64.urlsafe_b64encode(original)
    print


