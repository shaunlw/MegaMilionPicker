
import requests
import pandas as pd
from collections import Counter
import sys

# check commandline input
if len(sys.argv) != 2:
	print('Usage: python MegPicker.py <year>')
else:
	year = int(sys.argv[1])

# get and organize data
url = 'http://txlottery.org/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/megamillions.csv'
r = requests.get(url)
with open('meganumbers.csv','wb') as code:
    code.write(r.content)
df = pd.read_csv('meganumbers.csv', header=None, usecols=[1,2,3,4,5,6,7,8,9])
df.columns = ['month','day','year','b1','b2','b3','b4','b5','pb']
df['date'] = pd.to_datetime((df.year*10000 + df.month*100 +df.day).apply(str), format = '%Y%m%d')
df=df[df['year'] >= year]

# regular balls
regballs = [i for j in [list(df[x]) for x in ['b1','b2','b3','b4','b5']] for i in j]
count = Counter(regballs)
print('Most frequent five numbers:')
print([i for (i,_) in count.most_common(5)], end='\n\n')
print('Least frequent five numbers:n')
print([i for (i, _) in count.most_common()[-5:]])


# power ball
countPB = Counter(df['pb'])
print('Most frequent power ball:')
print(countPB.most_common(1)[0][0],end='\n')
print('Least frequent powerball:')
print(countPB.most_common()[-1:][0][0],end='\n')

