#include <iostream>
#include <list>
#include <vector>

using namespace std;

class SequenceHandler {
private:
    vector<double> inputData;
    list<double> resultList;

public:
    void readNumbers(int count) {
        double value;
        for (int i = 0; i < count; i++) {
            cin >> value;
            inputData.push_back(value);
        }

        for (double x : inputData) {
            resultList.push_back(x);
        }
    }

    bool checkCondition() const {
        for (double x : resultList) {
            if (x < -3) {
                return true;
            }
        }
        return false;
    }

    void transformData() {
        bool hasSmallElement = checkCondition();

        for (double& x : resultList) {
            if (hasSmallElement) {
                if (x < 0) {
                    x = x * x;
                }
            } else {
                x = x * 0.1;
            }
        }
    }

    void showReverse() const {
        for (auto it = resultList.rbegin(); it != resultList.rend(); ++it) {
            cout << *it << " ";
        }
        cout << endl;
    }
};

int main() {
    int n;
    SequenceHandler obj;

    cout << "Введіть кількість елементів: ";
    cin >> n;

    if (n <= 0) {
        cout << "Кількість елементів повинна бути натуральним числом." << endl;
        return 1;
    }

    cout << "Введіть елементи послідовності: ";
    obj.readNumbers(n);

    obj.transformData();

    cout << "Результат у зворотному порядку: ";
    obj.showReverse();

    return 0;
}