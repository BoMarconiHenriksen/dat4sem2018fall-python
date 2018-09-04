paragraph_1 = """Sherlock Holmes took his bottle from the corner of the mantel-piece and
his hypodermic syringe from its neat morocco case. With his long,
white, nervous fingers he adjusted the delicate needle, and rolled back
his left shirt-cuff.  For some little time his eyes rested thoughtfully
upon the sinewy forearm and wrist all dotted and scarred with
innumerable puncture-marks. Finally he thrust the sharp point home,
pressed down the tiny piston, and sank back into the velvet-lined
arm-chair with a long sigh of satisfaction.

"""

paragraph_2 = """Three times a day for many months I had witnessed this performance, but
custom had not reconciled my mind to it.  On the contrary, from day to
day I had become more irritable at the sight, and my conscience swelled
nightly within me at the thought that I had lacked the courage to
protest.  Again and again I had registered a vow that I should deliver
my soul upon the subject, but there was that in the cool, nonchalant
air of my companion which made him the last man with whom one would
care to take anything approaching to a liberty.  His great powers, his
masterly manner, and the experience which I had had of his many
extraordinary qualities, all made me diffident and backward in crossing
him.

"""

# print(len(paragraph_1.split(" "))

# for element in paragraph_1.split(" "):
#    print(element)

# while True:
#    pass  # gør ikke noget

big_words = []
for elememt in paragraph_1.split():
    if elememt[0].istitle():
        # print(elememt)
        big_words.append(elememt)

        print(big_words)

    elif elememt.isupper():
        print(elememt)

# Samme som ovenstående
print([len(elememt) for elememt in paragraph_1.split()])

#big_words2 = [ for elememt in paragraph_1.split() if elememt.istitle() ]
#print(big_words2)