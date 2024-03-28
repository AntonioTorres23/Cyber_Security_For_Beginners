import art

print(art.text2art(font="graffiti", text="Documentation"))

file = open("README.txt", 'r')

convert = file.readlines()

for x in convert:
    print(x)
input("\nPress any key to exit this window")


