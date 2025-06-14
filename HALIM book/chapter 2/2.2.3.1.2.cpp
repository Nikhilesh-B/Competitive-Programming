#include <iostream>
#include <vector>

using namespace std;

void is_power_of_two(int s)
{
    if (s == 0)
    {
        return;
    }
    int s_copy = {s};
    int count = {0};
    while (s)
    {
        count++;
        s >>= 1;
    }
    count--;
    int m = 1 << count;
    cout << ((s_copy & m) == s_copy);
}

int main()
{
    int s = {512};
    is_power_of_two(s);
}