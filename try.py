#fruits=["banana","apple","graps"]
#x,y,z=fruits
#y="hello world
#print(x , y , z )
x='awesome'

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)