print('''
US Dollars --1
Euro --2
Australian Dollars --3
UAE Dirham --4
New Zealand Dollar --5 
Canadian Dollar --6
Swiss Franc --7
Japanese Yen --8
Saudi Riyal --9
Qatari Rial --10
Omani Rial --11
Bahraini Dinar --12 
Kuwaiti Dinar --13
Singapore Dollar --14
Malaysian Ringgit --15
Swedish Krona --16
Danish Krone --17
Thai Baht --18
Hong Kong Dollar --19 
South African Rand --20
Chinese Yuan --21
British Pound - --22\n''')
print("ENTER THE o or p key to exit")

while True:
    a = str(input("Enter the currency using the above table --> "))
    if a != 'o':
        if a == "1":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum1 = 0
            while True:
                b = input("Enter the currency value in INR(₹)--> \t")
                if b != 'p':
                    a1 = 80.99
                    usd = float(b) / float(a1)
                    sum1 = sum1 + float(usd)
                else:
                    print(f"The ammount in US Dollars is = ${sum1}")
                    break

        elif a == "2":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum2 = 0
            while True:
                b = input("Enter the currency value in INR(₹)--> ")
                if b != 'p':
                    a2 = 78.5
                    ero = float(b) / float(a2)
                    sum2 = sum2 + float(ero)
                else:
                    print(f"The ammount in Euro is = €{sum2}")
                    break

        elif a == "22":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum3 = 0
            while True:
                b = input("Enter the currency value in INR(₹)--> ")
                if b != 'p':
                    a3 = 87.91
                    pound = float(b) / float(a3)
                    sum3 = sum3 + float(pound)
                else:
                    print(f"The amount in Pound is = £{sum3}")
                    break

        elif a == "3":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum4 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a4 = 52.89
                    ad = float(b) / float(a4)
                    sum4 = sum4 + float(ad)
                else:
                    print(f"The ammount in Australian Dollars is = A${sum4}")
                    break

        elif a == "4":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum5 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a5 = 22.05
                    uae = float(b) / float(a5)
                    sum5 = sum5 + float(uae)
                else:
                    print(f"The ammount in UAE Dirham is = د.إ{sum5}")
                    break

        elif a == "5":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum6 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a6 = 46.53
                    nz = float(b) / float(a6)
                    sum6 = sum6 + float(nz)
                else:
                    print(f"The ammount in New Zealand Dollar is = ${sum6}")
                    break

        elif a == "6":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum7 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a7 = 59.6
                    cand = float(b) / float(a7)
                    sum7 = sum7 + float(cand)
                else:
                    print(f"The ammount in canadian dollar is = ${sum7}")
                    break

        elif a == "7":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum8 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a8 = 82.55
                    swf = float(b) / float(a8)
                    sum8 = sum8 + float(swf)
                else:
                    print(f"The ammount in Swiss Franc is = Fr{sum8}")
                    break

        elif a == "8":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum9 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a9 = 0.565
                    jyen = float(b) / float(a9)
                    sum9 = sum9 + float(jyen)
                else:
                    print(f"The ammount in japanese yen is = ¥{sum9}")
                    break

        elif a == "9":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum10 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a10 = 21.60
                    saudi = float(b) / float(a10)
                    sum10 = sum10 + float(saudi)
                else:
                    print(f"The ammount in Saudi Riyal is = SAR{sum10}")
                    break

        elif a == "10":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum11 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a11 = 22.25
                    qr = float(b) / float(a11)
                    sum11 = sum11 + float(qr)
                else:
                    print(f"The ammount in Qatari Rial is = ر.ق{sum11}")
                    break

        elif a == "11":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum12 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a12 = 210.53
                    orial = float(b) / float(a12)
                    sum12 = sum12 + float(orial)
                else:
                    print(f"The ammount in Omani Rial is = ر.ع.{sum12}")
                    break

        elif a == "12":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum13 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a13 = 216.1
                    bha = float(b) / float(a13)
                    sum13 = sum13 + float(bha)
                else:
                    print(f"The ammount in Bahraini Dinar is = دينا{sum13}")
                    break

        elif a == "13":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum14 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a14 = 261.79
                    kuwa = float(b) / float(a14)
                    sum14 = sum14 + float(kuwa)
                else:
                    print(f"The ammount in Kuwaiti Dinar is كويتي{sum14}")
                    break

        elif a == "14":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum15 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a15 = 56.63
                    sing = float(b) / float(a15)
                    sum15 = sum15 + float(sing)
                else:
                    print(f"The ammount in Singapore Dollar is = S${sum15}")
                    break

        elif a == "15":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum16 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a16 = 17.7
                    mal = float(b) / float(a16)
                    sum16 = sum16 + float(mal)
                else:
                    print(f"The ammount in malaysian ringgit is = RM{sum16}")
                    break

        elif a == "16":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum17 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a17 = 7.17
                    ssed = float(b) / float(a17)
                    sum17 = sum17 + float(ssed)
                else:
                    print(f"The ammount in Swedish Krona is = kr{sum17}")
                    break

        elif a == "17":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum18 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a18 = 10.56
                    dk = float(b) / float(a18)
                    sum18 = sum18 + float(dk)
                else:
                    print(f"The ammount in danish krone is = Kr.{sum18}")
                    break

        elif a == "18":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum19 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a19 = 2.16
                    tb = float(b) / float(a19)
                    sum19 = sum19 + float(tb)
                else:
                    print(f"The ammount in Thai Baht is = ฿{sum19}")
                    break

        elif a == "19":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum20 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a20 = 10.32
                    hkd = float(b) / float(a20)
                    sum20 = sum20 + float(hkd)
                else:
                    print(f"The ammount in Hong Kong Dollar is = HK${sum20}")
                    break

        elif a == "20":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum21 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a21 = 4.52
                    sarf = float(b) / float(a21)
                    sum21 = sum21 + float(sarf)
                else:
                    print(f"The ammount in South African Rand is = R{sum21}")
                    break

        elif a == "21":
            print("ENTER p KEY TO GET THE TOTAL SO FAR ENTERED VALUES")
            sum22 = 0
            while True:
                b = input("Enter the curency value in INR(₹)--> ")
                if b != 'p':
                    a22 = 11.36
                    chi = float(b) / float(a22)
                    sum22 = sum22 + float(chi)
                else:
                    print(f"The ammount in Chinese Yuan is = ¥{sum22}")
                    break

        elif a != '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '10' and '11' and '12' and \
                '13' and '14' and '15' and '16' and '17' and '18' and '19' and '20' and '21' and '22':
            print("INVALID choice!!!!!!")

    else:
        print("CREATED BY SOPPIN")
        break