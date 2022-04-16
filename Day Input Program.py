days={'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
n=int(input("Enter the day of the year : "))
added=(n-1)%7
first=input("First day of the year : ")
while first not in days:
    print("Please enter a correct day with first letter capital,e.g.Sunday,Monday etc.")
    first=input("First day of the year : ")

current_day=days[first]+added
for day in days:
    if days[day]==current_day:
        print(day)
        break
