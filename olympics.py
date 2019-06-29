import turtle as tt

for i in range(5):
    al=tt.circle(25)
    if i%2==0:
        tt.penup() 
        tt.sety(-15)
    else:
        tt.penup()
        tt.sety(+5)
    tt.forward(25)
    tt.pendown()
tt.done
        
    
