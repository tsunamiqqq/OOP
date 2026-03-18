#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double C(int n, int k) {
    double res = 1;
    for (int i = 1; i <= k; i++) {
        res *= (n - k + i);
        res /= i;
    }
    return res;
}

int main() {
    cout << fixed << setprecision(4);

    double p = 0.75, q = 1 - p;
    double P1 = C(6, 4) * pow(p, 4) * pow(q, 2);
    cout << "Задача №1.";
    cout << " Ймовірність того, що за 6 діб норма не буде перевищена рівно 4 рази:\n";
    cout << "P = C(6,4) * 0.75^4 * 0.25^2 = " << P1 << "\n\n";

    double maxPQ = 0.25;
    double left = 6.0;
    double right = 20.0 * maxPQ;

    cout << "Задача №2. Два різні шахісти грають в шахи, що ймовірніше виграти 2 партії із 4, або 3 із 6 партій.\nПорівняння:\n";
    cout << "P(2 з 4) = 6p^2q^2\n";
    cout << "P(3 з 6) = 20p^3q^3\n";
    cout << "Максимум 20pq = 20 * 0.25 = " << right << "\n";

    if (left > right)
        cout << "Отже, ймовірніше виграти 2 партії із 4.\n\n";
    else
        cout << "Отже, ймовірніше виграти 3 партії із 6.\n\n";

    double total = 5 * 4;
    double evenEven = 2 * 1;
    double secondEven = 2 * 4;

    cout << "Задача №3. Із цифр 1, 2, 3, 4, 5 вибирають по черзі 2 цифри. Знайти ймовірність того, що: \n";
    cout << "а) двічі підряд випала парна цифра\n";
    cout << "б) другий раз випала парна цифра\n\n";
    cout << "a) P = " << evenEven << " / " << total << " = " << evenEven / total << "\n";
    cout << "б) P = " << secondEven << " / " << total << " = " << secondEven / total << "\n\n";

    double p1 = 0.6, p2 = 0.7, p3 = 0.8;
    double q1 = 1 - p1, q2 = 1 - p2, q3 = 1 - p3;

    double onlyOne = p1 * q2 * q3 + q1 * p2 * q3 + q1 * q2 * p3;
    double onlyTwo = p1 * p2 * q3 + p1 * q2 * p3 + q1 * p2 * p3;
    double allThree = p1 * p2 * p3;
    double atLeastOne = 1 - q1 * q2 * q3;

    cout << "Задача №4. Студент розшукує потрібну йому формулу у трьох довідниках. Ймовірність того, що формула міститься у першому довіднику дорівнює 0,6, у другому 0,7, в третьому 0,8. Знайти ймовірність того, що формула міститься: \n";
    cout << "а) лише в одному довіднику\n";
    cout << "б) лише в двох довідника\n";
    cout << "в) в усіх трьох довідниках\n";
    cout << "г) хоча б в одному із довідників\n\n";
    cout << "a) Лише в одному довіднику: " << onlyOne << "\n";
    cout << "б) Лише в двох довідниках: " << onlyTwo << "\n";
    cout << "в) В усіх трьох довідниках: " << allThree << "\n";
    cout << "г) Хоча б в одному довіднику: " << atLeastOne << "\n";

    return 0;
}
