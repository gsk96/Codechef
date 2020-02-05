#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int tc,q;
	float r,p;
cin>>tc;
	for(int i=0;i<tc;i++)
{
		cin>>q>>p;
	    r=q*p;
	if(q>1000) 
	{
	
		cout<<fixed<<setprecision(6)<<r*0.9<<endl;
	
	}
else
	 	cout<<fixed<<setprecision(6)<<r<<endl;

}
return 0;
}