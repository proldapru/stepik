#include <iostream>
using namespace std;

int main() {
    // put your code here
    int h, a, b;
    cin >> h >> a >> b;
    int daily_path = a - b;
    int last_day_start = h - a;
    cout << ((last_day_start + daily_path - 1)/daily_path) + 1;
    return 0;
}