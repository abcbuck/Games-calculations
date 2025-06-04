import collections

# record total wins and wins per animal
wins = collections.Counter()

animals = {
  0: {'name': 'Pferd',   'points': 1000}, 
  1: {'name': 'Kuh',     'points':  850},
  2: {'name': 'Schwein', 'points':  650},
  3: {'name': 'Esel',    'points':  500},
  4: {'name': 'Ziege',   'points':  350},
  5: {'name': 'Schaf',   'points':  250},
  6: {'name': 'Hund',    'points':  160},
  7: {'name': 'Katze',   'points':   90},
  8: {'name': 'Gans',    'points':   40},
  9: {'name': 'Hahn',    'points':   10}
}

startMoney = 90
additionalMoney = [50, 100, 200, 500]

# calculate average money per player in different phases
averageMoney = [startMoney]
for m in additionalMoney:
  averageMoney.append(averageMoney[-1]+m)

# a list of animals (numbers from 0 to 9) for each player
# the first player always gets the most valuable animal (to discount distributions symmetric to the one where the first player has the most valuable animal and decrease the amount of counting to be done)
numberOfPlayers = 4
players = [[] for i in range(0, numberOfPlayers)]
players[0].append(0)

# only count games where every player has between these numbers of animals
minimumNumberOfAnimals = 2
maximumNumberOfAnimals = 4

def evaluateGame():
  # calculate scores
  scores = []
  for i in range(0, numberOfPlayers):
    scores.append(0)
    for j in players[i]:
      scores[i]+=animals[j]['points']
    scores[i]*=len(players[i])
  
  # compare scores
  maxIndex = 0
  for i in range(1, numberOfPlayers):
    if scores[i] > scores[maxIndex]:
      maxIndex = i
  
  # check if every player has the minimum number of animals 
  for i in range(0, numberOfPlayers):
    if len(players[i]) < minimumNumberOfAnimals or len(players[i]) > maximumNumberOfAnimals:
      return
  # count total wins ...
  wins['total']+=1
  # and wins per animal ...
  for j in players[maxIndex]:
    wins[j]+=1
  # and wins per animal where that animal was the most valuable animal of that player
  wins[' '.join(list([str(players[maxIndex][0]), 'first']))]+=1

def tryAnimal(number):
  if number==len(animals):
    evaluateGame()
    return

  for i in range(0, numberOfPlayers):
    players[i].append(number)
    tryAnimal(number+1)
    del players[i][-1]

tryAnimal(1)

# show results

print("Total wins:", wins['total'])
print()
print('animal : number of wins : number of wins where that animal is the most valuable of that player')
print()
for animal in range(0, len(animals)):
  print(' : '.join([str(animal), str(wins[animal]).rjust(7), str(wins[' '.join([str(animal), 'first'])]).rjust(7)]))
print()
sumOfWinsPerAnimal=0
for animal in range(0, len(animals)):
  sumOfWinsPerAnimal += wins[animal]
averageNumberOfWinsPerAnimal = sumOfWinsPerAnimal/len(animals)
buyFactorPerAnimal = [wins[animal]/averageNumberOfWinsPerAnimal for animal in range(0, len(animals))]
print("".rjust(7), *[str(m).rjust(4).ljust(7) for m in averageMoney])
print("".rjust(7), *[str(numberOfPlayers*m).rjust(4).ljust(7) for m in averageMoney])
print()
for i in range(0, len(animals)):
  f=buyFactorPerAnimal[i]
  print(animals[i]['name'].rjust(7), *["{0:0.2f}".format(m*f/(numberOfPlayers-1)).rjust(7) for m in averageMoney])


'''
values:

>>> [x/9842 for x in [6149,5582,5237,4903,4602,4410,4231,4099,4016,3960]]
[0.6247713879292827, 0.5671611461085145, 0.53210729526519, 0.49817110343426135, 0.4675878886405202, 0.4480796586059744, 0.42989229831335096, 0.4164803901646007, 0.40804714488925015, 0.40235724446250765]
>>> [x/4718.9 for x in [6149,5582,5237,4903,4602,4410,4231,4099,4016,3960]]
[1.303057916039755, 1.1829027951429358, 1.109792536396194, 1.0390133293776094, 0.9752272775434954, 0.9345398291974826, 0.8966072601665643, 0.8686346394286805, 0.8510457945707687, 0.839178622136515]
>>> 1000+800+650+500+350+250+160+90+40+10
3850
>>> import random
>>> random.sample(range(0,6), 6)
[3, 5, 0, 1, 4, 2]


program output:

3 players:

Total wins: 19683

animal : number of wins : number of wins where that animal is the most valuable of that player

0 :   12199 :   12199
1 :   11349 :    5460
2 :   10459 :    1708
3 :    9774 :     300
4 :    9163 :      16
5 :    8799 :       0
6 :    8451 :       0
7 :    8182 :       0
8 :    8051 :       0
9 :    7916 :       0

          90     140     240     440     940
         270     420     720    1320    2820

  Pferd   58.19   90.51  155.17  284.47  607.73
    Kuh   54.13   84.21  144.35  264.65  565.39
Schwein   49.89   77.60  133.03  243.90  521.05
   Esel   46.62   72.52  124.32  227.92  486.92
  Ziege   43.71   67.99  116.55  213.67  456.48
  Schaf   41.97   65.29  111.92  205.19  438.35
   Hund   40.31   62.70  107.49  197.07  421.01
  Katze   39.03   60.71  104.07  190.80  407.61
   Gans   38.40   59.74  102.41  187.74  401.09
   Hahn   37.76   58.73  100.69  184.59  394.36


4 players:

Total wins: 262144

animal : number of wins : number of wins where that animal is the most valuable of that player

0 :  148366 :  148366
1 :  135541 :   76341
2 :  121285 :   29046
3 :  111454 :    7467
4 :  102715 :     900
5 :   97063 :      24
6 :   92335 :       0
7 :   88477 :       0
8 :   85849 :       0
9 :   84163 :       0

          90     140     240     440     940
         360     560     960    1760    3760

  Pferd   41.71   64.87  111.21  203.89  435.59
    Kuh   38.10   59.27  101.60  186.27  397.93
Schwein   34.09   53.03   90.91  166.68  356.08
   Esel   31.33   48.73   83.54  153.17  327.22
  Ziege   28.87   44.91   76.99  141.16  301.56
  Schaf   27.28   42.44   72.76  133.39  284.97
   Hund   25.96   40.37   69.21  126.89  271.09
  Katze   24.87   38.69   66.32  121.59  259.76
   Gans   24.13   37.54   64.35  117.98  252.04
   Hahn   23.66   36.80   63.09  115.66  247.09


5 players:

Total wins: 1953125

animal : number of wins : number of wins where that animal is the most valuable of that player

0 : 1043749 : 1043749
1 :  935973 :  577836
2 :  819565 :  243960
3 :  742095 :   75472
4 :  672969 :   11604
5 :  628721 :     504
6 :  590181 :       0
7 :  560219 :       0
8 :  539505 :       0
9 :  528451 :       0

          90     140     240     440     940
         450     700    1200    2200    4700

  Pferd   33.26   51.73   88.69  162.59  347.35
    Kuh   29.82   46.39   79.53  145.80  311.49
Schwein   26.11   40.62   69.64  127.67  272.75
   Esel   23.65   36.78   63.05  115.60  246.96
  Ziege   21.44   33.36   57.18  104.83  223.96
  Schaf   20.03   31.16   53.42   97.94  209.23
   Hund   18.81   29.25   50.15   91.94  196.41
  Katze   17.85   27.77   47.60   87.27  186.44
   Gans   17.19   26.74   45.84   84.04  179.54
   Hahn   16.84   26.19   44.90   82.32  175.87
'''