# calendar_secondthursday.py

import calendar

# Show every month
for month in range(1, 13):

    # Calcola le date per ogni settimana che si sovrappone nel mese
    c = calendar.monthcalendar(2015, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]

    # Se abbiamo un giovedì nella prima settimana,
    # il secondo giovedì è nella seconda settimana.
    # Altrimenti il secondo giovedì deve essere nella
    # terza settimana.
    if first_week[calendar.THURSDAY]:
        meeting_date = second_week[calendar.THURSDAY]
    else:
        meeting_date = third_week[calendar.THURSDAY]

    print('{:>3}: {:>2}'.format(calendar.month_abbr[month],
                                meeting_date))
