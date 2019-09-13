#include "Prime.h"

#include <math.h> 

// 计算数组的元素个数  
#define NELEMS(x) ((sizeof(x)) / (sizeof((x)[0])))  // 素数序列, 至少保存前6543个素数!  
static const int primes[] = {
	2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103, 107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211, 223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331, 337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449, 457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587, 593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709, 719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853, 857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991 };


// make primes in 2 ... n, this is enough for common case
void makePrimes(int n, vector<int> & primes)
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

bool isPrime_chart(int n, vector<int> &primes)
{
	primes.clear();
	if (n < 2) { return false; }
	else if (n == 2) {  return true; }
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

// naive check of isPrime
bool isPrime_naive(int n)
{
	if (n < 2)	return false;
	if (n == 2)	return true;
	if (n % 2 == 0)	return false;
	for (int i = 3; (i*i) <= n; i += 2)
	{
		if (n%i == 0)	return false;
	}
	return true;
}
