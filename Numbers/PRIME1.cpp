
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

#define num 10000000
#define debug(x) cout << x << "\n";
vector<unsigned int> primes;

long ciel(long item)
{
    unsigned long long l, r;
    l = 0;
    r = primes.size(); // 100000;
    //debug(r);
    long mid;
    while (r - l > 1)
    {
        mid = l + (r - l) / 2;
        //	debug(mid);
        if (primes[mid] <= item)
            l = mid;
        else
            r = mid;
    }
    return l;
}

bool check(unsigned int number)
{
    for (unsigned int i = 2; i <= (unsigned int)sqrt(number); i++)
    {
        if (number % i == 0)
            return false;
    }
    return true;
}

void primefinder(long m, long n)
{
    bool find = false;
    if (m < 2)
        m = 2;
    for (unsigned int i = m; i <= n; i++)
    {
        find = check(i);
        if (find)
            primes.push_back(i);
    }
}

void printprime(long m, long n)
{
    long i, j;
    //debug("in print");
    i = ciel(m);
    j = ciel(n) + 1;

    for (; i < j; i++)
        cout << primes[i] << "\n";
}

void print(long m, long n)
{
    long i, j;
    i = ciel(m);
    debug(m);
}

void print(vector<unsigned int> v)
{
    for (long i = 0; i < v.size(); i++)
        debug(primes[i]);
}

int main()
{
    //primefinder();
    //print(primes);
    int T;
    long m, n;
    cin >> T;
    while (T--)
    {
        cin >> m >> n;
        //cout<<m<<n;
        primefinder(m, n);
        printprime(m, n);
        primes.clear();
        cout << "\n";
    }
    return 0;
}