import random
import time

number = 2
setnum = 2

scoreper1 = 0
scoreper2 = 0

wantplay = True

print("Spieler 1 wie ist dein Name?")

spieler1 = input()

print("Spieler 2 wie ist dein Name?")

spieler2 = input()

scorename1 = spieler1
scorename2 = spieler2


current = spieler1

notcurrent = spieler2

zahl = 2



while wantplay == True:

    zahl = random.randint(0,1)

    print(f"{current} Wähle Kopf oder Zahl")



    while setnum != 1:

        input1 = input()

        if input1 == "Kopf":

            number = 0
            setnum = 1
            #break

        elif input1 == "Zahl": 

            number = 1
            setnum = 1
            #break

        else:
            print("Du hast dich vertippt")
            print(f"{current} Wähle Kopf oder Zahl")

    if zahl == 0:
        print("Spring")
        time.sleep(1)
        print("Kling")
        time.sleep(1)
        print("Flip")
        time.sleep(1)
        print("Das Ergenbniss ist Kopf")

    else:
        print("Spring")
        time.sleep(1)
        print("Kling")
        time.sleep(1)
        print("Flip")
        time.sleep(1)
        print("Das Ergenbniss ist Zahl")

    time.sleep(1)

    if number == zahl:
        print(f"{current} hat gewonnen")
        if current == scorename1:
            scoreper1 = scoreper1 + 1
        else:
            scoreper2 = scoreper2 + 1
        
    else: 
        print(f"{notcurrent} hat gewonnen")
        if current != scorename1:
            scoreper1 = scoreper1 + 1
        else:
            scoreper2 = scoreper2 + 1
        
    time.sleep(0.5)

    print(f"{scorename1} Score: {scoreper1}")
    time.sleep(0.5)
    print(f"{scorename2} Score: {scoreper2}")
    
    time.sleep(1)
    
    buffer = spieler1
    spieler1 = spieler2
    spieler2 = buffer

    current = spieler1

    notcurrent = spieler2

    time.sleep(0.5)

    print("")

    time.sleep(0.5)

    print("Wollt ihr weiterpielen? Ja/Nein")

    wantplay = input()

    setnum = 0

    if wantplay == "Ja":

        wantplay = True

        # break

    elif wantplay == "Nein": 

        wantplay = False

        # break

    else:
        print("Du hast dich vertippt")
        print("Viel Spaß bei einer weiteren Runde")
        wantplay = True

print("bb")

#Does break completely break out of all loops.

    




