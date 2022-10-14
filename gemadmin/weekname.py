import datetime 
from typing import Iterable
import pandas as pd 
def printSeq(func):
        print(func())

@printSeq
def get_term_name():
    year = datetime.datetime.now().strftime('%Y') + '/' + ((datetime.datetime.now( ) + datetime.timedelta(days=365)).strftime('%Y'))
    div_one = [datetime.datetime(2022,1,1), datetime.datetime(2022,3,31)]
    div_two = [datetime.datetime(2022,4,1), datetime.datetime(2022,7,31)]
    div_three = [datetime.datetime(2022,8,1), datetime.datetime(2022,12,31)]

    if pd.DatetimeIndex([datetime.datetime.now()]) in pd.date_range(div_one[0], div_one[1]):
        return f"second term {year} session"
    elif pd.DatetimeIndex([datetime.datetime.now()]) in pd.date_range(div_two[0], div_two[1]):
        return f"third term {year} session"
    elif pd.DatetimeIndex([datetime.datetime.now()]) in pd.date_range(div_three[0], div_three[1]):
        return f"first term {year} session"

def sort_weeks(wk_list: "list[datetime.datetime]", other:Iterable ):
    wkdict = {}
    wkbox = []
    i = 1
    for idx, dateobj in enumerate(wk_list):
        print(dateobj.strftime('%A'))
        if not dateobj.strftime('%A') == "Saturday":
            # wkbox.append(dateobj.strftime('%A'))
            wkbox.append(other[idx])
            try:
                wk_list[idx+1]
            except:
                print('weekend without saturday entry')
                wkdict[f'week {i}'] = wkbox 
                wkbox = []
                i+=1
            else:
                continue
        
        elif dateobj.strftime('%A') == 'Saturday':
            #wkbox.append(dateobj.strftime('%A'))
            wkbox.append(other[idx])
            wkdict[f'week {i}'] = wkbox 
            wkbox = []
            i+=1
            continue

        
    return wkdict

# import pandas as pd
#print(sort_weeks(pd.date_range(datetime.datetime.now(), periods=12), ['feyi', 'lolly', 'mean', 'roan','fgh','ghj','tyui','rowan','lopi','lupus','feyi', 'lolly', 'mean', 'roan','fgh','fgg']))

