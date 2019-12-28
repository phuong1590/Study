#include <iostream>

using namespace std;
void voidspirit(){
	cout << 
}

int main()
{
	int dmgori,dmgbonus,creeps,health,time,h;
	time=0;
	cin>>dmgori>>dmgbonus>>creeps>>health;
	h=health;
	while(creeps>0) {
		while(health>0) {
			health-=dmgori;
			//cout<<health<<" ";
			time++;
			//cout<<times<<" ";
		}
		dmgori+=dmgbonus;
		//cout<<damnor<<" ";
		creeps--;
		//cout<<creeps<<" ";
		health=h;
		//cout<<health<<" ";
		//cout<<endl;
	}
	cout<<time;
	return 0;
}

