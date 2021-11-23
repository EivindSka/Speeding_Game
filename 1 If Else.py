from time import sleep

popo = "Wioouu Wioouu Wioouu Honk Honk!!"
loading = "..."
crash = "Skrrrt kabooom!"
paramedics = "Wiuu Wiuu Wiuu"
increase_speed = []
crashed = "Everything is black and you hear a ringing sound"

print("Cars Available")
cars = [
    "Ferrari Enzo",
    "BMW M5",
    "Lamborghini Aventador",
    "Toyota Avensis",
    "Tesla Model S Plaid+ ",
]
chosenCar = ""
for i in range(len(cars)):
    print(i + 1, cars[i])
i0 = input("What car do you want to drive? ")

print("")
if i0 == "1":
    chosenCar = cars[0]
elif i0 == "2":
    chosenCar = cars[1]
elif i0 == "3":
    chosenCar = cars[2]
elif i0 == "4":
    chosenCar = cars[3]
elif i0 == "5":
    chosenCar = cars[4]
else:
    chosenCar = input("Self Defined car: ")
print("You picked to drive the " + chosenCar)

l = True
while l:
    speed = input(
        "You're driving in a 80 km/t zone in the " + chosenCar + "!"
        "\nWhat is your current speed? "
    )
    if speed.isdecimal():
        l = False
        speed = int(speed)
    else:
        print("Wrong Input, type a speed in km/t")
        sleep(0.5)

fake_speed = speed
for x in range(8):
    fake_speed += 3
    increase_speed.append(fake_speed)
    is_string = " ".join([str(l) for l in increase_speed])

if speed >= 110:
    i2 = input("Are you Barry Allen?\n ")
    if i2 == "yes":
        print("Gimme Autograph")
    else:
        print("Imposter")

elif speed >= 86:
    print("Expect the police you god damn street racer!\n")
    sleep(1)
    for i in range(3):
        print(loading[i], sep=" ", end=" ", flush=True)
        sleep(0.5)
    print("")
    for i in range(32):
        print(popo[i], sep=" ", end=" ", flush=True)
        sleep(0.1)

    print("\n\nDo you see the police? you're going down\n")
    i3 = input("Do you try to run or stop ?\n\n")

    if i3 == "stop":
        print("You got away with a 200$ ticket")
        print("You countiniue and travel to your desired destination")
        for i in range(3):
            print(loading[i], sep=" ", end=" ", flush=True)
            sleep(0.5)
        print("Congratulations! You arrived")

    elif i3 == "run":  # Her også ^^
        print("You're speeding up!")
        sleep(1)

        for i in range(16):
            print(is_string[i], sep="", end="", flush=True)
            sleep(0.05)
        sleep(0.5)
        print("\nYour speed is now drastically increased")
        print("Your adrenaline is pumping through your veins")

        i4 = input("\nDo you take the next exit? ")
        if i4 == "yes":
            for i in range(15):
                print(crash[i], sep=" ", end=" ", flush=True)
                sleep(0.1)
        print("\n\n You forgot to brake and crashed!\n")
        for i in range(48):
            print(crashed[i], sep=" ", end=" ", flush=True)
            sleep(0.07)
        print("You wake up...")
        i11 = input("\nDo you try to flee on foot? ")
        if i11 == "yes":  # Yes, get the escape / need for speed
            print("Impossible to run with a broken leg")
            for i in range(3):
                print(loading[i], sep=" ", end=" ", flush=True)
                sleep(0.5)
            print("\nYou arrived in jail")

        elif i11 == "no":
            print(
                "You lay on the ground when the police arrives and calls paramedics to get you fixed up"
            )
            sleep(2)
            for i in range(14):
                print(paramedics[i], sep=" ", end=" ", flush=True)
                sleep(0.05)
            for i in range(3):
                print(loading[i], sep=" ", end=" ", flush=True)
                sleep(0.5)
            print("\n You arrived at the hospital and got fixed up")
        elif i4 == "no":
            print("You're driving for 2 minutes and it seems like you escaped the popo")
            i6 = input("Do you stop and pull yourself togheter or keep driving? ")
            if i6 == "stop":
                for i in range(32):
                    print(popo[i], sep=" ", end=" ", flush=True)
                    sleep(0.05)
                    print("They caught up to you and you are going to jail")
                for i in range(3):
                    print(loading[i], sep=" ", end=" ", flush=True)
                    sleep(0.5)
                    print("You arrived in jail")

elif speed == 85:
    print("Keep driving that speed and you will be stapeled as a good samaritan")
    i7 = input(
        "Do you increase the speed or keep driving within the speed limit? [increase or keep]"
    )
    if i7 == "increase":
        print("You increase the speed, watch out for the police")
    else:
        print("Youre a law obeying individual, keep it up")

elif speed < 80:
    print("Get the hell off the road")
    i8 = input("Do you wish to increase your speed? ")
    if i8 == "yes":
        i9 = int(input("You increase the speed to: "))
        if i9 > 86:
            print("Expect the police you god damn street racer!")
            sleep(1)
            for i in range(3):
                print(loading[i], sep=" ", end=" ", flush=True)
                sleep(0.5)
            for i in range(32):
                print(popo[i], sep=" ", end=" ", flush=True)
                sleep(0.1)
            i10 = input("\nDo you try to escape? ")
            if i10 == "yes":
                print("You increase the speed")
                for i in range(16):
                    print(is_string[i], sep="", end="", flush=True)
                    sleep(0.05)
            else:
                print("You got off with a slap on the wrist")

    elif input == "no":
        print("Take the license again")

elif speed <= 84:
    print("Youre traveling in a ok tempo")
