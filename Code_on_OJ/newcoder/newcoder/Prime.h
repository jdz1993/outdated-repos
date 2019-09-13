#pragma once
#ifndef JDZ_PRIME_H_
#define JDZ_PRIME_H_


#include <vector>
using namespace std;

//extern void makePrimes(int n, vector<int> &v);
//extern bool isPrime_chart(int n, vector<int> &v); 
//
//extern void makePrimes(int n, vector<long long int> &v);
//extern bool isPrime_chart(int n, vector<long long int> &v);



extern bool isPrime_naive(int n);

template<typename T>
void makePrimes(int n, vector<T> & primes)
{
	primes.clear();
	if (n < 2) { return; }
	else if (n == 2) { primes.push_back(2); return; }
	else if (n == 3) { primes.push_back(2); primes.push_back(3); return; }
	primes.push_back(2); primes.push_back(3);

	for (int i = 5; i <= n; i += 2)
	{
		bool flag = false;
		for (int j = 1; primes[j] * primes[j] <= i; j++)
		{
			if (i%primes[j] == 0) { flag = true; break; }
		}
		if (!flag) { primes.push_back(i); }
	}
}

template<typename T>
bool isPrime_chart(int n, vector<T> &primes)
{
	primes.clear();
	if (n < 2) { return false; }
	else if (n == 2) { return true; }
	else if (n == 3) { return true; }
	primes.push_back(2); primes.push_back(3);

	for (int i = 5; i <= n; i += 2)
	{
		bool flag = false;
		for (int j = 1; primes[j] * primes[j] <= i; j++)
		{
			if (i%primes[j] == 0) { flag = true; break; }
		}
		if (!flag) { primes.push_back(i); }

		if (i == n)
		{
			return primes.back() == n;
		}
	}
	return false;
}



#endif