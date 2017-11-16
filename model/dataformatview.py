from model import parsedata
#import parsedata

def getValuesList(name,date):
	value = list()
	name = name.lower()
	print(name)
	datesplit = list()
	datesplit = date.split("-")
	year = datesplit[0]
	mdate = datesplit[1]+' '+datesplit[2]
	print(datesplit)
	print(year)
	print(mdate)
	count,neg,pos,neut=parsedata.getData(name,mdate,year)
	value.append(pos)
	value.append(neut)
	value.append(neg)
	return value

#getValuesList('Apple','2017-Nov-13')