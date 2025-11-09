#include <iostream>
#include <limits>
#include <chrono>
#include <thread>
using namespace std;


double m;
double StartCelcius;


//The purpose of this void is to calculate energy, show remaining time and show unit time calculations.
void calculate()
{
	string unit;
	const double J = 4.186;
	const double W = 1500;
	double temperature = StartCelcius; 
	double increment = W / (m * J);

	//required energy
	double Q = m * J * (100 - StartCelcius);    

	//required time
	double t = Q / W;
	
	//suitable time indicator
	if (t > 3600)
	{
		//hour
		double timehour = t / 3600;
		unit = " hour";
		
	}
	else if (t > 60)
	{
		//minutes
		double timemin = t / 60;
		unit = " min";
		
	}
	else
	{
		unit = " second";
		
	}

	cout << "Your water necessary time for boiling " << t << unit << " Please wait..." << "\n\n" << endl;
	
	int totalSeconds = static_cast<int>(Q / W);

	for (int remaining = totalSeconds; remaining >= 0; remaining--) {
		int hours = remaining / 3600;
		int minutes = (remaining % 3600) / 60;
		int seconds = remaining % 60;

		cout << "Time left: " << hours << " hour " << minutes << " min " << seconds << " second " << "Current temperature: " << temperature << "°C\r";
		cout.flush();

		temperature += increment;
		if (temperature > 100) temperature = 100;

		this_thread::sleep_for(chrono::seconds(1));
	}
	cout << "\nYour water is boiled!\n";
	
}


//The purpose of this main function is to create main screen for terminal and it takes water gr and celcius of water
int main()
{		
	bool massValid = false;
	bool tempValid = false;
	
	//In this piece it says the grams of water and its initial temperature.
	while (true)
	{

		if (!massValid)
		{
			cout << "Please enter water gr:" << endl;
			cin >> m;

			if (!cin)
			{
				cout << "Please enter correct water gr!\n" << endl;
				cin.clear();
				cin.ignore(numeric_limits<streamsize>::max(), '\n');
				continue;
			}
			else if (m < 0.1)
			{
				cout << "Water gr cannot be empty!\n\n";
				continue;

			}
			else
			{
				massValid = true;
			}
			cout << " \n\n";
		}

		if (!tempValid)
		{
			cout << "Please enter first celcius of water:" << endl;
			cin >> StartCelcius;

			if (!cin)
			{
				cout << "Please enter correct celcius!\n" << endl;
				cin.clear();
				cin.ignore(numeric_limits<streamsize>::max(), '\n');
				continue;
			}
			else if (StartCelcius > 99)
			{
				cout << "The water is already boiling!\n\n";
				continue;

			}
			else if (StartCelcius < 0)
			{
				cout << "The machine cannot thaw frozen water!\n\n";
			}
			else
			{
				tempValid = true;
			}
			cout << " \n\n";

			calculate();
			massValid = false;
			tempValid = false;
		}
	}
	return 0;
}
