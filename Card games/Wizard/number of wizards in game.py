import math

# Probability, before giving cards, that in a round with c cards there are w wizards in the hands of the players, given C total cards and W total wizards
def p(c, w, C, W):
  return math.comb(c, w)*math.comb(C-c, W-w)/math.comb(C, W)
  # equal to:
  # return math.comb(W, w)*math.comb(C-W, c-w)/math.comb(C, c)

# Print all probabilities for numbers of wizards in the players' hands, given the number of cards in a round
def P(c, C, W):
  for w in range(0,5):
    print(f"P({w} wizards|{c} cards) = {p(c, w, C, W)}")

def all_probabilities(C, W):
  for i in range(0, 61):
    if(math.gcd(i,3)==3 or math.gcd(i,4)==4 or math.gcd(i,5)==5):
      print()
      P(i, C, W)

all_probabilities(60, 4)
