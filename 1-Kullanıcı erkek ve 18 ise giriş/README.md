// Bu proje kullanıcıdan yaş ve cinsiyet alarak
// giriş kontrolü yapan basit bir C++ uygulamasıdır.

#include <iostream>
using namespace std;


string cinsiyet;
int yas;
bool erkekmi = false;

int main() {
	while (true) {
		cout << "Lütfen yaşınızı giriniz: " << endl;
		cin >> yas;
		cout << "Lütfen cinsiyetinizi giriniz: " << endl;
		cin >> cinsiyet;

		if (cinsiyet == "Erkek" || cinsiyet == "erkek") {
			erkekmi = true;
		}
		else if (cinsiyet == "Kız" || cinsiyet == "kız") {
			erkekmi = false;
		}
		else {
			cout << "Geçersiz cinsiyet tekrar deneyiniz cümlede Erkek, erkek, Kız, kız kullanınız." << endl;
			continue;
		}
		if (yas >= 18 and erkekmi == true) {
			cout << "Hoşgeldiniz..." << endl;

		}
		else if (yas >= 18 and erkekmi == false) {
			cout << "Erkek olmadıgınız için giriş yapamazsınız." << endl;

		}
		else if (yas < 18 and erkekmi == true) {
			cout << "Reşit olmadığın için giriş yapamazsın." << endl;

		}
		else if (yas < 18 and erkekmi == false) {
			cout << "Reşit olmadığın ve erkek olmadığın için giriş yapamazsın." << endl;

		}
		
	}
		

}
