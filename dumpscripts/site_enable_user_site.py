# site_enable_user_site.py

import site

status = {
    None: 'Disabilitato, ragioni di sicurezza',
    True: 'Abilitato',
    False: 'Disabilitato da opzione riga di comando',
}

print('Flag       :', site.ENABLE_USER_SITE)
print('Significato:', status[site.ENABLE_USER_SITE])
