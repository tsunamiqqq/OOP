#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

class Function {
public:
    double *x, *y;
    int size;

    Function(int n) : size(n) {
        x = new double[size];
        y = new double[size];
    }
    ~Function() {
        delete[] x;
        delete[] y;
    }
};

void saveFormatted(const Function &f, const char* filename) {
    ofstream out(filename);
    
    out.setf(ios::fixed | ios::showpos); 
    out.precision(3);
    
    for (int i = 0; i < f.size; i++) {
        out << setw(10) << f.x[i] << "\t" << setw(10) << f.y[i] << endl;
    }
    out.close();
}

int main() {
    int n = 3;
    Function f1(n);
    
    f1.x[0] = 1.1; f1.y[0] = 2.0;
    f1.x[1] = 5.0; f1.y[1] = -1.25;
    f1.x[2] = 10.0; f1.y[2] = 0.0;

    saveFormatted(f1, "output.txt");
    cout << "Файл успішно збенежено з форматуванням" << endl;

    return 0;
}
