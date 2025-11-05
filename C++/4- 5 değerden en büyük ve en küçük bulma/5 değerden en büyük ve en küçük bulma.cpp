#include <iostream>
using namespace std;

int sayı;
int büyük_sayı;
int küçük_Sayı;


int main() {
    cout << "1. Sayıyı giriniz: ";
    cin >> sayı;

    büyük_sayı = sayı;
    küçük_Sayı = sayı;

    for (int i = 2; i <= 5; i++) {
        cout << i << ". Sayıyı giriniz: ";
        cin >> sayı;

        if (sayı > büyük_sayı) {
            büyük_sayı = sayı;
        }
        if (sayı < küçük_Sayı) {
            küçük_Sayı = sayı;
        }
    }

    cout << "En buyuk sayi: " << büyük_sayı << endl;
    cout << "En kucuk sayi: " << küçük_Sayı << endl;

    return 0;

}


