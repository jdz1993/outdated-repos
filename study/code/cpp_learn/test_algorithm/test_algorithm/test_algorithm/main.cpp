#include <iostream>
#include "test_algorithm.h"

using namespace std;



int main()
{

#if 1
	{
		using namespace test_algorithm;
		cout<<KMP("longlongstr", "sst");

		
	}
#endif

#if 0
	{
		using namespace dezhi_test;
		test();
	}
#endif
	system("pause");
	return 0;
}