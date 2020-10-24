import random
import time

animals = [
    "Tiger", "Panther", "Eagle", "Cardinal", "Snowy Owl",
    "Blue and Gold Macaw", "Green Sea Turtle", "Hermit Crab",
    "Great White Shark", "Hammerhead Shark", "Florida Manatee", "Wolf",
    "Domestic Dog", "Domestic Cat"
]
animalpicker = random.randint(0, len(animals))
TheKey = """
1. Goes on land?
   YES……………………………………………………………………………….go to 2
   NO………………………………………………………………………………...go to 10
2. Has wings or feathers?
   YES…………………………………………………………………………….go to 3
   NO……………………………………………………………………………….go to 6 
3. Has vibrant colors?
   YES…………………………………………………………………………….go to 4
   NO……………………………………………………………………………...go to 5
4. Is red?
   YES…………………………………………………….Cardinal(Cardinalis cardinalis)
   NO……………………………………………...Blue and Gold Macaw(Ara ararauna)
5. Lives in the cold North?
   YES……………………………………………………..Snowy Owl(Bubo scandiacus
   NO……………………………………………………...Eagle(Hieraatus Spilogaster)
6. Part of the cat family?
   YES……………………………………………………………………..go to 7
   NO……………………………………………………………………….go to 9
7. Lives in the wild?
   YES……………………………………………………………………….go to 8
   NO…………………………………………………..Domestic Cat(Felis catus)
8. Is orange?
   YES………………………………………………………...Tiger(Panthera Tigris)
   NO………………………………………………………Panther(Panthera pardus)
9. Lives in the wild?
   YES…………………………………………………………...Wolf(Canis Lupus)
   NO………………………………………..Domestic Dog(Canis lupus familiaris)
10. Has a shell?
   YES……………………………………………………………………….go to 11
   NO………………………………………………………………………...go to 12
11. Has fins?
   YES………………………………………………Green Sea Turtle(Chelonia mydas)
   NO………………………………………………...Hermit Crab(Pagurus samuelis)
12. Is a herbivore?
   YES……………………………..Florida Manatee(Trichechus Manatus Latirostris)
   NO………………………………………………………………………..go to 13
13. Has an irregular head?
   YES…………………………………………Hammerhead Shark(Sphyrna Zygaena)
   No……………………………………..Great White Shark(Carcharodon carcharias)
"""


def Key():
    print(TheKey)


input(
    "Welcome to the Dichotomous Key Quiz! You will have to figure out which animal is being described using the key. You have to follow the steps to find the right animal and type it in the box. You do NOT have to type in the Scientific name. You will be given a set of facts about the animal to help you. There are 14 animals in total. You may have to scroll up to see the whole key depending on how large your screen is."
)

currentanimal = animals[animalpicker]
while len(animals) > 0:
    animalpicker = random.randint(0, len(animals) - 1)
    currentanimal = animals[animalpicker]
    animals.remove(animals[animalpicker])
    print("Key:")
    Key()
    if currentanimal == "Tiger":
        print("""
    - Is Orange
    - Is part of the cat family
    - Lives in the jungle
    - Is a mammal
        """)
    elif currentanimal == "Panther":
        print("""
    - Black or brown fur
    - A type of cat
    - Lives in the jungle
    - Is a mammal
        """)
    elif currentanimal == "Eagle":
        print("""
    - Type of bird
    - Brown feathers
    - Live from mexico to canada
        """)
    elif currentanimal == "Cardinal":
        print("""
    - Type of bird
    - Bright red feathers
        """)
    elif currentanimal == "Snowy Owl":
        print("""
    - Type of bird
    - White feathers
    - live cold places
        """)
    elif currentanimal == "Blue and Gold Macaw":
        print("""
    - Type of bird
    - Blue and gold feathers
        """)
    elif currentanimal == "Green Sea Turtle":
        print("""
    - Underwater creature
    - Has a hard shell
    - Uses fins to swim
    - Has a beak-like head
        """)
    elif currentanimal == "Hermit Crab":
        print("""
    - Lives underwater
    - Uses its shell for protection
    - Has claws
        """)
    elif currentanimal == "Great White Shark":
        print("""
    - Lives in the sea
    - Has fins to swim
    - has a head with many large teeth
    - Only eats meat(carnivore)
        """)

    elif currentanimal == "Hammerhead Shark":
        print("""
    - Lives underwater
    - has a head shaped like a hammer
    - Only eats meat(carnivore)
    - smooth back
        """)
      

    elif currentanimal == "Florida Manatee":
        print("""
    - Lives underwater
    - only eats plants
    - has fins
    - has a smooth back
        """)
    elif currentanimal == "Wolf":
        print("""
    - Lives in a pack
    - Doesnt live in the water
    - Canis Lupus
        """)
    elif currentanimal == "Domestic Dog":
        print("""
    - Is not a Cat
    - Lives on land
    - Not in the wild
        """)
    elif currentanimal == "Domestic Cat":
        print("""
    - Is part of the Cat family 
    - Is typically a pet
    - Lives on the land
        """)
    userguess = input("What is the animal?:  ")
    while userguess != currentanimal:
      print("Incorrect, try again!")   
      userguess = input("What is the animal?:  ")
    print("Correct!")
    time.sleep(3)
    print("""
  ------------------------------------------
  
  """)
print("Well done! You found all of the animals!")
