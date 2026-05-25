#include <iostream>

using namespace std;

class Vect {
public:
    Vect(char n);
    ~Vect();
    int& operator[](int i) {
        if (i < 0 || i >= size) throw "Вихід за межі масиву!";
        return p[i];
    }
    void Print();

private:
    int* p;
    char size;
    void Destroy();
};

Vect::Vect(char n) : size(n) {
    if (size < 0) {
        throw "Некоректний розмір масиву";
    }

    p = new int[size];
    if (!p) {
        throw "Error of Vect constructor";
    }

    for (int i = 0; i < size; ++i) {
        p[i] = int();
    }
}

void Vect::Destroy() {
    if (p != nullptr) {
        delete[] p;
        p = nullptr;
    }
}

Vect::~Vect() {
    try {
        Destroy();
    } catch (...) {
        cerr << "Виникла помилка під час роботи деструктора" << endl;
    }
}

void Vect::Print() {
    for (int i = 0; i < size; ++i) {
        cout << p[i] << " ";
    }
    cout << endl;
}

int main() {
    try {
        cout << "Створюємо масив 'a' розміром 3..." << endl;
        Vect a(3);
        a[0] = 0;
        a[1] = 1;
        a[2] = 2;
        a.Print();

        cout << "\nСтворюємо масив 'a1' розміром 200..." << endl;
        Vect a1(200);
        a1[10] = 5;
        a1.Print();

    } catch (const char* msg) {
        cerr << "Перехоплено виняток: " << msg << endl;
    } catch (...) {
        cerr << "Перехоплено невідомий виняток" << endl;
    }

    return 0;
}
