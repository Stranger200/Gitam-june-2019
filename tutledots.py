import turtle as tt
al = tt.Turtle()

colors=["violet","indigo","blue","green","yellow","orange","red"]
dot_distance=10
width = 10
height = 15
al.penup()
for x in range(height):
    al.pencolor(colors[x%7])
    for i in range(width):
        al.dot()
        al.forward(dot_distance)
    al.forward(dot_distance*width)
    al.right(90)
    al.forward(dot_distance)
    al.left(90)

tt.done
