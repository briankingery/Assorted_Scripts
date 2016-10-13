import random
def flip():
    total_heads = 0
    total_tails = 0
    count = 0
    while count < 100:
        coin = random.randint(1, 2)
        if coin == 1:
            total_heads += 1
        elif coin == 2:
            total_tails += 1
        count += 1
    print "Heads =", total_heads
    print "Tails =", total_tails
flip()
