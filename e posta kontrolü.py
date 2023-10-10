while True:
    # Doğru e-posta ve parola bilgileri
    correct_email = 'Bhalitgil250708@gmail.com'
    correct_password = '2507halitgil08'
    # Kullanıcıdan e-posta ve parola bilgilerini al
    email = input('E-posta: ')
    password = input('Parola: ')
    # Kullanıcının girdiği bilgileri, doğru bilgilerle karşılaştır
    if email == correct_email and password == correct_password:
        print('Giriş başarılı!')
    else:
        print('Hatalı e-posta veya parola!')