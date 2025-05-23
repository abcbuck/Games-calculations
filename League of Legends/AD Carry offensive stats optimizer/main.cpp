#include <algorithm>
#include <iostream>

/*
 * damage = ad*(1+(1+cd)*min(cs, 1))*min((1+as)*bas, 2.5)
 * --------
 *  ad  attack damage
 *  cd  additional crit damage (infinity edge)
 *  cs  critical strike chance
 *  as  additional attack speed
 * bas  base attack speed
 */
double damage(double ad, double as, double bas, double cs, double cd=0.5){ //cd=0 without infinity edge, cd=0.5 with infinity edge
	return ad*(1+(1+cd)*std::min(cs, 1.0))*std::min((1+as)*bas, 2.5);
}

int main(){

	const int
		ad_amount	=  10,
		ad_cost		= 350,
		as_amount	= .12,
		as_cost		= 300,
		cs_amount	= .10,
		cs_cost		= 400;
	
	const double
		ad_per_gold = static_cast<double>(ad_amount)/ad_cost,
		as_per_gold = static_cast<double>(as_amount)/as_cost,
		cs_per_gold = static_cast<double>(cs_amount)/cs_cost;

	/*
	We set all status values to 0. Then we keep buying the value equivalent of 1 gold that maximizes the total damage when added to our current status values.
	*/
	unsigned int gold=0;
	double ad=0, as=0, bas, cs=0;

	std::cout << "Set base attack speed: ";
	std::cin >> bas;

	unsigned int toSpend=30000;

	while(toSpend > 0) {
		const double newADDamage = damage(ad+ad_per_gold, as, bas, cs),
					 			 newASDamage = damage(ad, as+as_per_gold, bas, cs),
					 			 newCSDamage = damage(ad, as, bas, cs+cs_per_gold);
		(newADDamage > newASDamage)  ?
		((newADDamage > newCSDamage) ? ad+=ad_per_gold : cs+=cs_per_gold)  :
		((newASDamage > newCSDamage) ? as+=as_per_gold : cs+=cs_per_gold);
		gold++;
		if(gold%50==0) { //Show stats after every 50 gold spent
			toSpend-=50;
			std::cout << "Gold: " << gold << "\tAD: " << ad << "   \tAS: " << 100*as << "%\tCS: " << 100*cs << "%" << std::endl;
		}
	}

	return 0;
}