#include <iostream>
#include <limits>
#include <string>

using namespace std;

struct Distance {
    int meters;
    double centimeters;
};

class CasinoInput {
public:
    static void clearStream() {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    static int readInt(const string& prompt) {
        int value;
        while (true) {
            cout << prompt;
            cin >> value;

            if (!cin.fail()) {
                return value;
            }

            cout << "Потрібно ввести ціле число.\n";
            clearStream();
        }
    }

    static double readDouble(const string& prompt) {
        double value;
        while (true) {
            cout << prompt;
            cin >> value;

            if (!cin.fail()) {
                return value;
            }

            cout << "Потрібно ввести дійсне число.\n";
            clearStream();
        }
    }

    static int readPower(double base) {
        int p;
        while (true) {
            cout << "Введіть показник степеня p: ";
            cin >> p;

            if (!cin.fail()) {
                if (base == 0 && p < 0) {
                    cout << "0 не можна підносити до від’ємного степеня.\n";
                }
                else {
                    return p;
                }
            }
            else {
                cout << "Показник степеня має бути цілим числом.\n";
                clearStream();
            }
        }
    }

    static Distance readDistance(const string& title) {
        Distance d;

        while (true) {
            cout << title << endl;
            cout << "  Метри: ";
            cin >> d.meters;
            cout << "  Сантиметри: ";
            cin >> d.centimeters;

            if (!cin.fail() && d.meters >= 0 && d.centimeters >= 0 && d.centimeters < 100) {
                return d;
            }

            cout << "Некоректно введена дистанція. ";
            clearStream();
        }
    }
};

double power(double n, int p = 2) {
    double result = 1.0;
    int absPower = (p < 0) ? -p : p;

    for (int i = 0; i < absPower; i++) {
        result *= n;
    }

    if (p < 0) {
        return 1.0 / result;
    }

    return result;
}

void zeroSmaller(int& first, int& second) {
    if (first < second) {
        first = 0;
    }
    else if (second < first) {
        second = 0;
    }
}

Distance biggerDistance(Distance d1, Distance d2) {
    double total1 = d1.meters * 100 + d1.centimeters;
    double total2 = d2.meters * 100 + d2.centimeters;

    if (total1 >= total2) {
        return d1;
    }

    return d2;
}

void runPowerTask() {
    cout << "Завдання 1: Функція power()\n";

    double betMultiplier = CasinoInput::readDouble(
        "Введіть число n: "
    );
    char choosePower;
    cout << "Бажаєте ввести показник степеня? (t/n): ";
    cin >> choosePower;
    if (choosePower == 't' || choosePower == 'T' || choosePower == 'y' || choosePower == 'Y') {
        int exponent = CasinoInput::readPower(betMultiplier);
        cout << "Результат power(" << betMultiplier << ", " << exponent << ") = "
             << power(betMultiplier, exponent) << "\n\n";
    }
    else {
        cout << "Результат power(" << betMultiplier << ") = "
             << power(betMultiplier) << "\n\n";
    }
}

void runZeroSmallerTask() {
    cout << "Завдання 2: Функція zeroSmaller()\n";

    int playerOneChips = CasinoInput::readInt("Введіть кількість фішок першого гравця: ");
    int playerTwoChips = CasinoInput::readInt("Введіть кількість фішок другого гравця: ");

    zeroSmaller(playerOneChips, playerTwoChips);
    cout << "Фішки першого гравця: " << playerOneChips << endl;
    cout << "Фішки другого гравця: " << playerTwoChips << "\n\n";
}

void runDistanceTask() {
    cout << "Завдання 3: Порівняння двох Distance\n";

    Distance zoneA = CasinoInput::readDistance(
        "Введіть першу дистанцію:"
    );
    Distance zoneB = CasinoInput::readDistance(
        "Введіть другу дистанцію:"
    );
    Distance maxD = biggerDistance(zoneA, zoneB);
    cout << "Більша дистанція: "
         << maxD.meters << " м, "
         << maxD.centimeters << " см\n";
}

int main() {
    system("chcp 65001 > nul");

    runPowerTask();
    runZeroSmallerTask();
    runDistanceTask();

    return 0;
}
