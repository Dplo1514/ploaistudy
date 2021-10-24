empty_list=[]
weekdays=['monday','tuesday','wednesday','thursday','friday']
big_birds=['emu','ostrich','cassowary']
first_names=['graham','john','terry','terry','michael']
leap_years=[2000,2004,2008]
randomness=['Pinxatawney',{'groundhog':'phil'},'Feb.w']

t = [globals()[z] for z in [y for y in[x for x in dir() if x.find('__')== -1]]]
for a in t:
    print(a)