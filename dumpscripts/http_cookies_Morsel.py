# http_cookies_Morsel.py

from http import cookies
import datetime


def show_cookie(c):
    print(c)
    for key, morsel in c.items():
        print()
        print('chiave =', morsel.key)
        print('   valore =', morsel.value)
        print('   valore codificato =', morsel.coded_value)
        for name in morsel.keys():
            if morsel[name]:
                print('   {} = {}'.format(name, morsel[name]))


c = cookies.SimpleCookie()

# Un cookie con un valore che deve essere codificato
# per essere inserito nell'intestazione
c['cookie_con_valore_codificato'] = '"cookie,valore;"'
c['cookie_con_valore_codificato']['comment'] = \
    'Ha punteggiatura da gestire con codici di escape'

# Un cookie che si applica solo a parte di un sito
c['cookie_limitato'] = 'valore_cookie'
c['cookie_limitato']['path'] = '/sub/path'
c['cookie_limitato']['domain'] = 'PyMOTW'
c['cookie_limitato']['secure'] = True

# Un cookie che scade in 5 minuti
c['con_durata_massima'] = 'scade fra 5 minuti'
c['con_durata_massima']['max-age'] = 300  # secondi

# Un cookie che scade ad un determinato tempo
c['scade_ad_un_dato_tempo'] = 'valore_cookie'
time_to_live = datetime.timedelta(hours=1)
expires = (datetime.datetime(2009, 2, 14, 18, 30, 14) +
           time_to_live)

# Formato data: Wdy, DD-Mon-YY HH:MM:SS GMT
expires_at_time = expires.strftime('%a, %d %b %Y %H:%M:%S')
c['scade_ad_un_dato_tempo']['expires'] = expires_at_time

show_cookie(c)


