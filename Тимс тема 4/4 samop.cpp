#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

double binomialProbability(int n, int k, double p) {
    double logC = lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1);
    return exp(logC + k * log(p) + (n - k) * log(1 - p));
}

double binomialRangeProbability(int n, int k1, int k2, double p) {
    double sum = 0.0;
    for (int k = k1; k <= k2; k++) {
        sum += binomialProbability(n, k, p);
    }
    return sum;
}

int main() {
    cout << fixed << setprecision(10);

    int n1 = 100;
    double p1 = 0.8;
    int k1 = 75;

    double task1 = binomialProbability(n1, k1, p1);

    cout << "Задача 1. Ймовірність попадання в ціль при одному пострілі дорівнює 0,8. Знайти ймовірність того, що із 100 пострілів буде влучено в ціль рівно 75 разів.\n";
    cout << "Відповідь: " << task1 << "\n\n";

    int n2 = 100;
    double p2 = 0.8;

    double task2a = binomialRangeProbability(n2, 75, 90, p2);
    double task2b = binomialRangeProbability(n2, 75, 100, p2);
    double task2c = binomialRangeProbability(n2, 0, 74, p2);

    cout << "Задача 2. Ймовірність попадання в ціль при одному пострілі дорівнює 0,8 проведено 100 пострілів. Знайти ймовірність того, що: \n";
    cout << "а) влучено буде не менше 75 разів і не більше 90 разів\n";
    cout << "б) влучено буде не менше 75 разів\n";
    cout << "в) влучено буде не більше 74 разів\n\n";
    cout << "а) "
         << task2a << "\n";
    cout << "б) "
         << task2b << "\n";
    cout << "в) "
         << task2c << "\n\n";

    int n3 = 100;
    double p3 = 0.01;

    double task3a = binomialProbability(n3, 3, p3);
    double task3b = binomialRangeProbability(n3, 0, 2, p3);
    double task3c = binomialRangeProbability(n3, 4, 100, p3);
    double task3d = 1.0 - binomialProbability(n3, 0, p3);

    cout << "Задача 3. Комутатор обслуговує 100 абонентів, ймовірність того, що на впродовж хвилини абонент зателефонує на комутатор дорівнює 0,01. Знайти ймовірність того, що впродовж хвилини: \n";
    cout << "а) зателефонує три абоненти\n";
    cout << "б) зателефонує менше трьох абонентів\n";
    cout << "в) зателефонує більше трьох абонентів\n";
    cout << "г) зателефонує хоча б один абонент\n\n";
    cout << "а) "
         << task3a << "\n";
    cout << "б) "
         << task3b << "\n";
    cout << "в) "
         << task3c << "\n";
    cout << "г) "
         << task3d << "\n";

    return 0;
}
