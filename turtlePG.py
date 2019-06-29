import turtle as tt
al=tt.Turtle()
colors=["indigo","green","yellow","orange","red"]
for x in range(10000):
    al.pencolor(colors[x%5])
    al.width(x/100+1)
    al.forward(x*1.1)
    al.right(144)
tt.done()
