import datetime as dt
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'
goods = {}

def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    expiration_date = dt.datetime.strptime(
        expiration_date, 
        DATE_FORMAT
    ).date() if expiration_date else expiration_date
    list.append(
        items[title],
        {'amount': amount, 'expiration_date': expiration_date}
    )


def add_by_note(items, note):
    parts = str.split(note, ' ')
    if len(str.split(parts[-1], '-')) == 3:
        expiration_date = parts[-1]
        good_amount = Decimal(parts[-2])
        title = str.join(' ', parts[0:-2])
    else:
        expiration_date = None
        good_amount = Decimal(parts[-1])
        title = str.join(' ', parts[0:-1])
    add(items, title, good_amount, expiration_date)


def find(items, needle):
    search = []
    for x in items.keys():
        if needle.lower() in x.lower():
            search.append(x)
    return search


def get_amount(items, needle):
    summa = Decimal('0')
    search = find(items, needle)
    
    if len(search) == 0:
        return summa

    for y in search:
        for product in items[y]:
            summa += product['amount']

    return summa

def get_expired(items, in_advance_days=0):
    result = []
    today = dt.date.today()
    for title in items.keys():
        summa = Decimal('0')
        for parts in items[title]:
            if parts['expiration_date'] is None:
                continue
            finish_time = parts['expiration_date']
            time = (finish_time - today).days
            count = Decimal(str(parts.get('amount', 0)))
            if time <= 0:
                summa += count
            elif time <= in_advance_days:
                summa += count
        if summa == Decimal('0'):
            continue
        result.append((title, summa))
    
    return result
