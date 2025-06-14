#include <iostream>
#include <vector>

using namespace std;

int main(){
    int mask = 18;
    for (int subset = mask; subset; subset = (mask & (subset-1)))
        cout << subset << "\n";

    return 0;
}