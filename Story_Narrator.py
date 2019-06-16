import random
import time


def gen():
    i = 0
    while i < 5:
        i += 1
        words1 = ["Surprize", "Tears", "Smile", "Sadness", "Rage", "love"]
        words2 = [" against the", "over the", "of the", "for the"]
        words3 = [" shadow", " light", " star", "sun", "moon"]
        words4 = ["for the money", " in a lifetime", "in the shadow", "in a reflection", "for the star", "for the love", "in the darkness"]
        one = random.choice(words1)
        two = random.choice(words2)
        three = random.choice(words3)
        four = random.choice(words4)
        print(one + two + three + four)

while True:
    print("Generating a story one after the another in 3 seconds of time interval")
    time.sleep(3)
    gen()
