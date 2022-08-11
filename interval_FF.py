import pandas as pd
import dateutil.parser

##### script to find interval between contacts regarding ReTiMo and relevant ground stations from FreeFlyer output data #####

df = pd.read_csv("FF_ContactTimes.txt", usecols=[3, 4, 5, 6,7,8,9,10], names=['col1', 'col2', 'col3', 'col4','col5','col6','col7','col8'],delim_whitespace=True)  # read exported FreeFlyer epoch text, specify columns picked from .txt, no headers

timestamp1 = []
timestamp2 = []
gap = []

a = df['col1']
b = df['col2']
c = df['col3']
d = df['col4']

e = df['col5']
f = df['col6']
g = df['col7']
h = df['col8']

for i in range (a.size):

    s = "{} 0{} {} {}".format(a.iloc[i], b.iloc[i], c.iloc[i], d.iloc[i]) #read GMAT epoch text as string
    s = dateutil.parser.parse(s) #optional : convert to datetime object
    timestamp1.append(s)

    x = "{} 0{} {} {}".format(e.iloc[i], f.iloc[i], g.iloc[i], h.iloc[i])  # read GMAT epoch text as string
    x = dateutil.parser.parse(x)  # optional : convert to datetime object
    timestamp2.append(x)

print(timestamp1[0])
print(timestamp2[0])

for i in range (1,len(timestamp1)):
    if timestamp1[i]>timestamp2[i-1]:
        gap.append(timestamp1[i] - timestamp2[i-1])
print (gap[0])

gap.sort()
df = pd.DataFrame(gap)  # create pandas dataframe
df.to_csv('gap_FF_sorted.txt', index=False, header = None)

print (df.max())