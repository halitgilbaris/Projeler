//Kütüphaneler
#include <iostream>
#include <limits>
using namespace std;

//Değişkenler
const float PI = 3.1415;
int number = 2;
int seçim;


//Alan Hesaplaması
void alan()
{
	float r;
	//ALAN = PI * r * r
	while(true)
	{
		cout << "(Çıkmak için 0 giriniz) Lütfen dairenin yarıçapını giriniz: " << endl;
		cin >> r;


		//r için girilen ve girilemeyen komutları hesaplama
		if (!cin)
		{
			cout << "Lütfen sayı giriniz.";
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			continue;

		}
		else if (r < 0)
		{
			cout << "Negatif işlem kabul edilmez lütfen tekrar deneyiniz\n\n";
		}
		else if (r == 0)
		{
			break;
		}
		else
		{
			double Alan = PI * r * r;
			cout << "Dairenizin alanı -----> " << Alan << endl;
			break;
			
		
		}
	}
	
	
}


//Çevre Hesaplaması
void çevre()
{
	float r;
	//Çevre = 2 * PI * r
	while (true)
	{
		cout << "(Çıkmak için 0 giriniz) Lütfen dairenin yarıçapını giriniz: " << endl;
		cin >> r;


		//r için girilen ve girilmeyen değerler
		if (!cin)
		{
			cout << "Lütfen sayı giriniz.\n\n";
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			continue;
		}
		else if (r < 0)
		{
			cout << "Yarı çap negatif bir değer alamaz.\n\n";
		}
		else if (r == 0)
		{
			break;
		}
		else
		{
			double Çevre = number * PI * r;
			cout << "Dairenizin çevresi -----> " << Çevre << endl;
			break;
		}
	}
	

}




int main()
{
	while (true) {
		//Soru İşlemi
		cout << "Lütfen girmek istediğiniz işlemi giriniz: " << endl << "1-Daire alan bulma" << endl << "2-Daire çevre bulma" << endl << "3-Çıkış\n";
		cin >> seçim;
		cout << "\n";


		//Cin Hata Almaması İçin Veya Yanliş Değer Girmemesi İçin

		if (!cin)
		{
			cout << "Lütfen seçeneklerden birini seçiniz (1 - 2 - 3)\n\n";
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			continue;
		}
		else if (seçim > 3 || seçim < 1)
		{
			cout << "Lütfen seçiminiz için doğru sayıyı giriniz (1 - 2 - 3)\n\n";
			continue;
		}
		
		

		//Seçim İşleminin Başlaması
		if (seçim == 1)
		{
			alan();
		}
		else if (seçim == 2)
		{
			çevre();
		}
		else if (seçim == 3)
		{
			break;
		}





	}


	return 0;
}
