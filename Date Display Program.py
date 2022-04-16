date=input("Enter date in DDMMYYYY format : ")
def prettyPrint(date):
    months={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    month=months[int(date[2:4])]
    day=date[:2]
    year=date[4:]
    prettyDate=month+" "+day+","+year
    print(prettyDate)
prettyPrint(date)
