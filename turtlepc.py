import turtle as tt
c1=tt.Turtle()
colors=["purple","indigo","blue","green","yellow","orange","red"]
for i in range(360):
    c1.pencolor(colors[i%7])
    c1.width(i/100+1)
    c1.forward(i)
    c1.left(59)
tt.done

