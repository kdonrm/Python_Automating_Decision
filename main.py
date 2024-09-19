from random import choice , choices

mood = input("What is you mood now?")
number = int(input("how many movies do you like gto watch?"))

Sequence = {
    "Happy" : ["Superbad (2007)","The Hangover (2009)","Anchorman: The Legend of Ron Burgundy (2004)",
               "Step Brothers (2008)","Dumb and Dumber (1994)"],
    "Sad" : ["Schindler's List (1993)","The Pursuit of Happyness (2006)","Requiem for a Dream (2000)"
             "Grave of the Fireflies (1988)","Atonement (2007)"],
    "Angry" : ["Falling Down (1993)","Do the Right Thing (1989)","Gladiator (2000)",
               "Taxi Driver (1976)","12 Angry Men (1957)"]
}

if number == 1 :
    print(choice(Sequence[mood]))
else:
    print(choices(Sequence[mood],k=number))