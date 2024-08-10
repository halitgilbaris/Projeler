flag = False
şifre = ""

sayılar = "abcçdefgğhiıjklmnoöprsştuüvyz0123456789_-?\*=}])}])&{[(/%+$#'!é<>|.:,;"

for basamak0 in sayılar:
    for basamak1 in sayılar:
        for basamak2 in sayılar:
            for basamak3 in sayılar:
                for basamak4 in sayılar:
                    for basamak5 in sayılar:
                        for basamak6 in sayılar:
                            deneme = (basamak0+basamak1+basamak2+basamak3+basamak4+basamak5+basamak6)
                            print(deneme)
                            if deneme == şifre:
                                print("Parolanız: " + deneme)
                                flag = True
                        if flag == True:
                            break
                    if flag == True:
                        break
                if flag == True:
                    break
            if flag == True:
                break
        if flag == True:
            break
    if flag == True:
        break
