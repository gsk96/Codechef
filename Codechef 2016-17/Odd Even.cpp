#include <iostream>
using namespace std;

int main()
{
    int a;
    cin>>a;
    for(int i=0;i<=a;i++)
        if (i%2==0) //for odd (i%2==1)
            cout<<i<<"\t";
        else 
            cout<<"";
return 0;
}