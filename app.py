#ACOG = 0.35
#HOLO = 0.6
#GlazFlip Sight = 0.3


num1 = float(input("Enter your Veticle and Horizontal sens (It has to be the same number) : "))
num2 = float(3.84)
num3 = float(0.35)
num4 = float(0.6)
num5 = float(0.3)


print("Select Operation")
print("1.ACOG")
print("2.Iron Sights/Holo/Reflex")
print("3.GlazFlip Sight")

choice = input("Enter choice(1/2/3): ")

if choice == '1':
   print((num1 * num3) / num2)
elif choice == '2':
    print((num1 * num4) / num2)
elif choice == '3':
    print((num1 * num5) / num2)


print("Now set your kovaac's Sensitivity Scale to Quake/Source, and use the number that came out as your sensitivity")

print("To work out the FOV needed do Your current FOV * Modifier (ACOG = 0.35 / Iron Sights/Holo/Reflex = 0.9 / GlazFlip Sight = 0.3) and that will be the FOV you need ot use")


k=input("press close to exit")