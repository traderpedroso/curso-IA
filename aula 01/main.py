import ejtrader as ej 

count = 0

while True:
    can = ej.economic_calendar(from_date='01/01/2021',to_date='10/01/2021')
    count += 1
    for cad in can['importance']:
        if cad == 'low':
            livre = True
            print(f'tranquilo: {count}')
        else:
            livre = False
            print(f'atenção: {count}')





