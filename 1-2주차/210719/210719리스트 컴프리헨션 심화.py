alist=['1','2','3','4']
blist=['11','22','33','44']

varList = [x for x in dir() if x.find('__')==-1]
valList = [globals()[z] for z in varList]