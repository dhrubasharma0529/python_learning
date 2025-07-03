import datetime
today_dat=datetime.date.today()
def write_error(error):
    with open(f"errors/{today_dat}error.log",'a') as f:
        f.write(f'{error}\n')
a=[1,12,3,4,5,7]
try:
    for i in a:
        print(a[7])
except IndexError as e:
    write_error(str(e))

