from dinosay import dinoprint, DINO_TYPE

msg = "Hello from Dinosay!"
dinoprint(msg, DINO_TYPE['tyrannosaurus'])

val = 0
while(val!=-1):
    val = int(input("Enter your bet:"))
    if (val >= 0):
        print("Oops! you lost!")