#include "universal_2017.h"
#include "Prime.h"


namespace universal
{

	int i;
	//------------------------------------------------------ private ------------------------------------------------------

	//1
	bool isFood(int i1, int i2)
	{
		// i1 is the bigger one
		if (i1 < i2) { swap(i1, i2); }

		int tmp = i1 / i2;
		if (tmp == 10) { return (i1%i2) == 0; }

		return tmp >= 2 && tmp < 10;

	}

	int go_1(vector<int> &fishSize, int minSize, int maxSize)
	{
		int count = 0;
		bool isFoodtmp = false;
		for (size_t i = minSize; i <= maxSize; i++)
		{
			isFoodtmp = false;
			for (size_t j = 0; j < fishSize.size(); j++)
			{
				if (!isFoodtmp && isFood(i, fishSize[j]))
				{
					isFoodtmp = true;
				}
			}
			if (!isFoodtmp)
			{
				count++;
				//fishSize.push_back((int)i);
				//cout << "fishSize:" << fishSize.size() << "\ti:" << i << endl;
			}
		}
		return count;
	}


	// 2
	bool isCircleFromStart(const string &s1, int pos1, const string &s2, int pos2)
	{
		if (s1.size() != s2.size()) { return false; }
		size_t sz = s1.size();
		size_t flag = s1.size();
		while (flag > 0)
		{
			if (s1.at(pos1) != s2.at(pos2))
			{
				return false;
			}
			pos1++;
			pos2++;
			if (pos1 == sz) { pos1 = 0; }
			if (pos2 == sz) { pos2 = 0; }
			flag--;
		}
		return true;

	}

	bool isCircle(const string &s1, const  string &s2)
	{
		if (s1.size() != s2.size()) { return false; }
		size_t sz = s1.size();

		for (size_t i = 0; i < sz; i++)
		{
			if (isCircleFromStart(s1, 0, s2, i))
			{
				return true;
			}
		}
		return false;
	}

	int go_2(const vector<string> &data)
	{
		unordered_set<string> s_set;
		bool match = false;
		for (const string& s : data)
		{
			match = false;
			for (const string & model : s_set)
			{
				if (isCircle(s, model))
				{
					match = true;
				}
			}
			if (!match)
			{
				s_set.insert(s);
			}
		}
		return s_set.size();
	}

	//3
	bool match(char c1, char c2)
	{
		// c1 is smaller one
		if (c1 > c2) { swap(c1, c2); }

		return (c1 == 'A'&& c2 == 'T') || (c1 == 'C'&&c2 == 'G');
	}

	int go_3(const string & s1, const string &s2)
	{
		int count = 0;
		for (size_t i = 0; i < s1.size(); i++)
		{
			if (!match(s1.at(i), s2.at(i)))
			{
				count++;
			}
		}
		return count;
	}


	// 4
	template<typename Out>
	void split(const std::string &s, char delim, Out result) {
		std::stringstream ss;
		ss.str(s);
		std::string item;
		while (std::getline(ss, item, delim)) {
			*(result++) = item;
		}
	}
	std::vector<std::string> split(const std::string &s, char delim) {
		std::vector<std::string> elems;
		split(s, delim, std::back_inserter(elems));
		return elems;
	}

	string go_4(const vector<int> &data)
	{


		int len = (int)data.size() + 1;
		int* arr = new int[len];
		memset(arr, 0, sizeof(int)*len);

		const auto p = minmax_element(data.begin(), data.end());

		int min = *p.first;
		int max = *p.second;
		if (max - min > data.size()) { return "mistake"; }
		if (min < 1) { return "mistake"; }

		// handle single number
		if (data.size() == 1)
		{
			int tmp = data[0];
			return to_string(tmp - 1) + " " + to_string(tmp + 1);
		}

		int pos = 0;
		for (const int i : data)
		{
			pos = i - min;
			if (pos < 0 || (pos > max - min)) { return "mistake"; }
			if (arr[pos] == 1) { return "mistake"; }
			arr[pos] = 1;
		}



		// head and tail
		if (arr[0] == 0)
		{
			return to_string(min - 1) + " " + to_string(max + 1);
		}
		else if (arr[data.size()] == 0)
		{
			return to_string(min - 1) + " " + to_string(max + 1);
		}

		for (size_t i = 0; i < data.size() + 1; i++)
		{
			if (arr[i] == 0)
			{
				return to_string(i + min);
			}
		}

		return "mistake";

	}


	//5
	//bool isPrime_naive(int n)
	//{
	//	if (n < 2)	return false;
	//	if (n == 2)	return true;
	//	if (n % 2 == 0)	return false;
	//	for (int i = 3; (i*i) <= n; i += 2)
	//	{
	//		if (n%i == 0)	return false;
	//	}
	//	return true;
	//}


	string go_5(const long long int &n)
	{
		//long long int p = pow(10, 9);
		//cout << p << endl;

		if (n < 4) { return "No"; }
		int q = 0;

		for (long long int i = 2; i*i <= n; i++)
		{
			if (isPrime_naive(i) && (n%i == 0))
			{
				q = log(n) / log(i);
				if (pow(i, q) == n) { return to_string(i) + " " + to_string(q); }
				else if (pow(i, q + 1) == n) { return to_string(i) + " " + to_string(q + 1); }
				else { return "No"; }
			}
		}

		return "No";
	}

	//------------------------------------------------------ public ------------------------------------------------------
	void f_1()
	{
		int minSize, maxSize;
		cin >> minSize >> maxSize;
		int n;
		cin >> n;
		vector<int> fishSize;
		int tmp = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> tmp;
			fishSize.push_back(tmp);
		}

		cout << go_1(fishSize, minSize, maxSize) << endl;
	}

	void f_2()
	{
		int n;
		cin >> n;
		string tmp;
		vector<string> data;
		for (size_t i = 0; i < n; i++)
		{
			cin >> tmp;
			data.push_back(tmp);
		}

		cout << go_2(data) << endl;
	}

	void f_3()
	{
		string s1, s2;
		cin >> s1 >> s2;
		cout << go_3(s1, s2);
	}

	void f_4()
	{
		int n;
		cin >> n;
		int tmp;
		vector<int> data;
		for (size_t i = 0; i < n; i++)
		{
			cin >> tmp;
			data.push_back(tmp);
		}

		string res = go_4(data);

		// handle <0
		auto v = split(res, ' ');
		if (v.size() == 1)
		{
			if (isdigit(v[0].at(0)))
			{
				int tmp = atoi(v[0].c_str());
				if (tmp < 1) { res = "mistake"; }
			}
		}
		else if (v.size() == 2)
		{
			if (isdigit(v[0].at(0)))
			{
				int tmp = atoi(v[0].c_str());
				if (tmp < 1) { res = v[1]; }
			}
		}
		cout << res << endl;

	}

	void f_5()
	{
		long long int n;
		cin >> n;
		cout << go_5(n) << endl;
	}

}