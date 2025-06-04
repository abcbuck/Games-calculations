# The game

"Kuhhandel" is a German card game about bidding for animals and trading them. Let's call it "Cattle Trade" in the following discussion, by direct translation, although the translators decided to give it a different name.\
Manuals: [German](https://www.ravensburger.de/spieleanleitungen/ecm/Spielanleitungen/20753%20anl%201534225.pdf) | [English](https://www.ravensburger.de/spielanleitungen/ecm/Spielanleitungen/Youre_Bluffing.pdf)

# Evaluation

During play, it turns out the actual values of the cards in terms of how valuable a card is to a player are different from the values that are written on them, so I pondered how to quantify this difference. I had the idea to look at all possible outcomes of a game of Cattle Trade and assign a point to each card for every outcome in which it belongs to the winning player. Then we might adjust our bidding according to these scores.\
This isn't, however, a very sensible way to assign scores, as a lot of the possible outcomes will never happen during actual play (e.g. the outcome where all cards end up at one player and all other players end up with none probably won't happen), so I added the assumption that there is a range in the number of cards such that every player gets a number in this range.

When playing with three players, every player will probably get at least three animals, with decent play.\
Playing with four, everyone will get at least two and at most three or four.\
And with five players everyone wants to get at least two cards. And if everyone has at least two cards with five players, everyone has exactly two cards.

This way, the resulting score for each animal is something like the winning probability of each animal, with the horse being that much more likely to win than the rooster as given by the ratio of their scores calculated this way.

Of course, these assumptions won't always turn out true during a game. Someone might get more or less cards still. They are an experimental try to make the game calculatable. During a real game the values would also change, because as one player completes a set or gets close to completion, my method of evaluation would give different results as then the implied question changes from "How likely is each animal to win?" to "How likely is each of the remaining animals to win for any of the players?" with different results for each player, as the set of cards that let you win changes.

# Results

Using my script, I calculated a cheat sheet of bidding values depending on the number of players and how money (yes, how *money*) donkeys are in play, as this changes the amount of ... well. The values should be right relative to each other taking into account above assumptions but might be better placed higher or lower. I calculated them to be `[the average player money]*[winning score of animal relative to average winning score of all animals]/([number of players]-1)`. The last division is there so that you don't spend all your money (or more) at once. A different divisor might be a better fit for the formula.\
Of course, you'll never pay values exactly as calculated. Round some up and some down and hope it's right. It's all experimental anyway.

I tried the second sheet for four players once and got second place. I might have gotten first had I done better on the cattle trades and got more money by auctioning. The game definitely has its elements of luck.
