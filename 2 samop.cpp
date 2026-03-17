#include <iostream>
#include <string>
#include <limits>

using namespace std;

double readPositiveDouble(const string& message) {
    double value;

    while (true) {
        cout << message;
        cin >> value;

        if (!cin.fail() && value > 0) {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return value;
        }

        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Введіть додатне число.\n";
    }
}

int readIntInRange(const string& message, int minValue, int maxValue) {
    int value;

    while (true) {
        cout << message;
        cin >> value;

        if (!cin.fail() && value >= minValue && value <= maxValue) {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return value;
        }

        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Введіть число в межах від "
             << minValue << " до " << maxValue << ".\n";
    }
}

class CasinoBonus {
public:
    virtual double calculateBonus(double deposit) const = 0;
    virtual string getBonusName() const = 0;
    virtual ~CasinoBonus() {}
};

class WelcomeBonus : public CasinoBonus {
public:
    double calculateBonus(double deposit) const override {
        double bonus = deposit * 0.50;
        if (bonus > 3000) {
            bonus = 3000;
        }
        return bonus;
    }

    string getBonusName() const override {
        return "Вітальний бонус";
    }
};

void task1() {
    cout << "Завдання 1: Поліморфізм для двох класів. Виклик через покажчик ->\n";

    double deposit = readPositiveDouble("Введіть суму першого поповнення: ");

    CasinoBonus* bonusPtr;
    WelcomeBonus welcome;
    bonusPtr = &welcome;

    cout << "\nТип бонусу: " << bonusPtr->getBonusName() << "\n";
    cout << "Сума бонусу: " << bonusPtr->calculateBonus(deposit) << " грн\n";
    cout << "Загальний баланс після нарахування: "
         << deposit + bonusPtr->calculateBonus(deposit) << " грн\n";
}

class CasinoGame {
public:
    virtual double calculatePossibleWin(double bet, int level) const = 0;
    virtual string getGameTitle() const = 0;
    virtual ~CasinoGame() {}
};

class SlotMachine : public CasinoGame {
public:
    double calculatePossibleWin(double bet, int level) const override {
        double coefficient = 1.2 + level * 0.6;
        return bet * coefficient;
    }

    string getGameTitle() const override {
        return "Слоти";
    }
};

class Roulette : public CasinoGame {
public:
    double calculatePossibleWin(double bet, int level) const override {
        double coefficient = 1.5 + level * 0.8;
        return bet * coefficient;
    }

    string getGameTitle() const override {
        return "Рулетка";
    }
};

void showGameResult(CasinoGame* gamePtr, double bet, int level) {
    cout << "\nОбрана гра: " << gamePtr->getGameTitle() << "\n";
    cout << "Ставка: " << bet << " грн\n";
    cout << "Рівень ризику: " << level << "\n";
    cout << "Можливий виграш: "
         << gamePtr->calculatePossibleWin(bet, level) << " грн\n";
}

void task2() {
    cout << "Завдання 2: Поліморфізм для трьох класів. Передача покажчика на базовий клас у функцію\n";

    double bet = readPositiveDouble("Введіть суму ставки: ");
    int level = readIntInRange("Введіть рівень ризику (1-5): ", 1, 5);
    int choice = readIntInRange("Оберіть гру (1 - Слоти, 2 - Рулетка): ", 1, 2);

    SlotMachine slots;
    Roulette roulette;

    if (choice == 1) {
        showGameResult(&slots, bet, level);
    } else {
        showGameResult(&roulette, bet, level);
    }
}

class PaymentMethod {
public:
    virtual double calculateFee(double amount) const = 0;
    virtual string getMethodName() const = 0;
    virtual ~PaymentMethod() {}

    void printReceipt(double amount) const {
        double fee = calculateFee(amount);
        double credited = amount - fee;

        cout << "\nСпосіб поповнення: " << getMethodName() << "\n";
        cout << "Сума поповнення: " << amount << " грн\n";
        cout << "Комісія: " << fee << " грн\n";
        cout << "До зарахування на рахунок: " << credited << " грн\n";
    }
};

class CardPayment : public PaymentMethod {
public:
    double calculateFee(double amount) const override {
        return amount * 0.015;
    }

    string getMethodName() const override {
        return "Банківська картка";
    }
};

class CryptoPayment : public PaymentMethod {
public:
    double calculateFee(double amount) const override {
        return amount * 0.01;
    }

    string getMethodName() const override {
        return "Криптогаманець";
    }
};

void processDeposit(const PaymentMethod& method, double amount) {
    method.printReceipt(amount);
}

void task3() {
    cout << "Завдання 3: Поліморфізм для трьох класів. Передача посилання на базовий клас\n";

    double amount = readPositiveDouble("Введіть суму поповнення: ");
    int choice = readIntInRange("Оберіть спосіб (1 - Картка, 2 - Криптогаманець): ", 1, 2);

    CardPayment card;
    CryptoPayment crypto;

    if (choice == 1) {
        processDeposit(card, amount);
    } else {
        processDeposit(crypto, amount);
    }
}

int main() {
    task1();
    task2();
    task3();
    cout << "\nПрограму завершено.\n";
    return 0;
}