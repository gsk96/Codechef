#include<iostream>
using namespace std;
int main()
{
int w;
double b;
cin>>w>>b;
if(w%5==0)
{
if((b-w)<0.5)
cout<<b;
else
cout<<(b-(w+0.5));
}
else
cout<<b;
return 0;
}
