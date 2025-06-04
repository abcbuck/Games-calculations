#include <iostream>

int main(){
	//values taken by manual measurement, disregarding distance to depot
	const float wt=27.5; //time for 10 wood
	const float ft=29.2; //time for 10 food (farm)

	std::cout << "Time one villager needs to gather 10 wood: " << wt << "s" << std::endl
	          << "Time one villager needs to gather 10 food on a farm: " << ft << "s" << std::endl;

	float f, wf, f1v, mft; //food (per farm), wood factor (faster gathering by technology), number of farms provided with wood by 1 villager, modified food time

	for(;;){

		std::cout << "Enter food per farm: ";
		std::cin >> f;
		std::cout << "Enter research bonus speed factor: ";
		std::cin >> wf;

		f1v=(f*ft/10)/(6*wt/wf); //f*ft/10: time to work a farm until depleted; 6*wt/wf: time to work up wood for a farm (6*wt is the time for 60 wood)
		mft=ft+wt/f1v;

		std::cout << std::endl
		          << "Number of farms provided with wood by 1 villager: " << f1v << std::endl
							<< "Time one villager needs to gather 10 food on a farm, taking into account the cost of a farm: " << mft << std::endl;

	}

	return 0;
}