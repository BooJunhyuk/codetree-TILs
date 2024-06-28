#include <iostream>

using namespace std;
int main() {
    int arr_2d[2][4];
    int sum;

    for(int i = 0; i<2; i++){
        for(int j = 0; j < 4; j++){
            cin >> arr_2d[i][j];
        }
    }
    cout << fixed;
    cout.precision(1);

    for(int i = 0; i < 2; i++){
        sum = 0;
        for(int j = 0; j < 4; j++){
            sum += arr_2d[i][j];

        }

        cout << (double)sum / 4 <<" ";
    }
    cout<< endl;
    for(int j = 0; j < 4; j++){
        sum = 0;
        for(int i = 0; i < 2; i++){
            sum += arr_2d[i][j];
        }
        cout<<(double)sum/2 << " ";
    }
    cout<< endl;
    sum = 0;
    for(int i = 0; i < 2; i++){
        for(int j = 0; j <4; j++){
            sum += arr_2d[i][j];
        }
    }
    cout<<(double)sum / 8 <<" ";

    return 0;
}