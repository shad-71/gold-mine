/*This program was written as solution for hackerearth coding challenge */

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;
//fast gcd finder , For Details : https://github.com/lemire/Code-used-on-Daniel-Lemire-s-blog/blob/77e5335ef0091426aeee10a6780740626ae118a8/2013/12/26/gcd.cpp
long gcd(long u, long v)
{
	int shift, uz, vz;
     if ( u == 0) return v;
     if ( v == 0) return u;
     uz = __builtin_ctz(u);
     vz = __builtin_ctz(v);
     shift = uz > vz ? vz : uz;
     u >>= uz;
     do {
       v >>= vz;
       int diff = v;
       diff -= u;
       vz = __builtin_ctz(diff);
       if ( diff == 0 ) break;
       if ( v <  u ) 
         u = v;
       v = abs(diff);

     } while( 1 );
     return u << shift;
}
//Fast poweroftwo finder , Details : http://www.exploringbinary.com/ten-ways-to-check-if-an-integer-is-a-power-of-two-in-c/
bool isPowerOfTwo(int x)
{	return x && (!(x&(x-1))); }

int fun(long N , int PIN)
{
	if(N%PIN != 0)
	return 0;
	
	long M ;
	M = N/PIN;
	
	int value = 0;
	
	for(long i = 1;i<=M;i++)
	{
		if(__gcd(i,M)==i)
			value++;
	}
	if(isPowerOfTwo(value))
		return value;
	else
		return 0;
	
}

int main()
{
  //To Do : Fast IO	
  long N,T;
  cin>>T;
  while(T--)
  {
  	cin>>N;
  	long temp, max=0;
  	for(int i =1 ;i<=13;i++)
  		{
			temp = fun(N,i);  
			if(temp > max)
  				max = temp;
		  }
  	cout<<max<<"\n";
  }
  return 0;
}