#include <iostream>

int main(){

	const float healthPer1Gold = 0.375, resPer1Gold = 0.05; //0.05=only armor or magic resistance, 0.025=both armor and magic resistance

	unsigned int healthCounter = 0, resCounter = 0, gold = 0; //Counters: count how often health and/or resistance were added (at a cost of 1g)

	float effectiveHealth, health, res, diffByHealth, diffByRes;

	unsigned int toSpend=30000;

	while(toSpend > 0) {

		health	= healthCounter	* healthPer1Gold;
		res		= resCounter	* resPer1Gold;

		effectiveHealth = health * (1 + res/100);

		if(gold%10==0){
			toSpend-=10;
			//show health and resistance
			std::cout << "Health: "				<< health	<< "\t   "
				 << "Resistance: "			<< res		<< "\t\t"
				 << "Effective Health: "	<< effectiveHealth << std::endl;
		}

		// difference of effective health when adding health or resistance at a cost of 1g
		diffByHealth	= healthPer1Gold	* (1 + res/100);
		diffByRes		= health			* (resPer1Gold/100);

		diffByHealth>diffByRes ? healthCounter++ : resCounter++;
		gold++;

	}

	return 0;
}
