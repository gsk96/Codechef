#include<iostream>
using namespace std;
int main()
{
		int n,m,sum,ld;
		cin>>n;
		for(int i=1;i<=n;i++)
			{
				cin>>m;
				sum=0;
				while (m!=0)
					{
						ld = m%10;
						sum = sum+ld;
						m = m/10;
					}
				cout<<sum<<endl;
			}
		return 0;
}

