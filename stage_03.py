
with open("artifacts.txt","r") as f:
    text=f.read()
    
with open("artifacts.txt","w") as f:
    txt=f.write("i have added one line")
    
    
print(txt)
print("it is a end of stage 3")