print("Hello Django Girls")
Dic={"Numero":"26", "Mes":"Diciembre", "Año":"1995"}
print(Dic)
print(Dic["Mes"])

if 3 > 2:
    print("It Works!")

a="2"
b="3"

a!=b

if 5 > 2:
    print("5 is indeed greater than 2")

else:
    print("5 is not greater than 2")

name = "Sonja"
if name == "Ola":
    print("Hey Ola!")
elif name == "Sonja":
    print("Hey Sonja!")
else:
    print("Hey anonymous!")

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")

def hi():
    print("Hi there!")
    print("How are you?")

hi()

def hi(name):
    if name == "Ola":
        print("Hey Ola!")
    elif name == "Sonja":
        print("Hey Sonja!")
    else:
        print("Hey anonymous!")

hi("Ola")

def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']


def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1,6):
    print(i)
