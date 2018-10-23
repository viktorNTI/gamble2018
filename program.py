import random
kort = 0
tal = random.randint(0,12) 
hand = "" 

while kort != 100: 
    try: 
        kort = int(input("Välj ett kort"))
    except:
        print("Du måste ange en siffra")
    tal = random.randint(0,12)
    if kort == tal:
        print("Den har jag.")
    else:
        print("Finns i sjön.")
    hand = hand + str(kort)
    print(hand)
    

#Jens lösning för att spara hand (med fel?):
#hand = []
#kort = 0
#while kort !=100:
    #kort = int(input("Välj ett kort: "))
    #hand.append(kort)
    #for k in hand:
            #print(k)
