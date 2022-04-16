d1={"Physics":40,"Chemistry":70,"Maths":70}
d2={"Physics":40,"Chemistry":50,"Maths":60}
d3={"Physics":70,"Chemistry":80,"Maths":90}
d4={"Suniti":d1,"Ryna":d2,"Zeba":d3}
for x in d4.keys():
    print("Name")
    print(x)
    print("Subject(key)",'\t',"Marks(value)")
    for y in d4[x].keys():
        print("",y,'\t\t',d4[x][y])
    print()
