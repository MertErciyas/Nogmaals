weekDict = {'ma':1,'di':2,'wo':3,'do':4,'vr':5,'za':6,'zo':7}
#list of weekdays for printing in while loop
weekList = ['ma','di','wo','do','vr','za','zo']

i = 0 

target = input('Welke dag van de week\n').replace('dag','').replace('an','').replace('ens','').replace('ns','').replace('nder','').replace('ij','').replace('ter','').replace('n','')
while i < weekDict[target]:
    print(weekList[i])
    i += 1 