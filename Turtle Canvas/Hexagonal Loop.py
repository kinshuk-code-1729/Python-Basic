import turtle as ttl
c=ttl.Turtle()
l=["purple","orange","red","green","orange"]
ttl.bgcolor("black")
for k in range(200):
    c.color(l[k%5])
    c.pensize(k/10+1)
    c.forward(k)
    c.left(59)
