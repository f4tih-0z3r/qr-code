import cv2
import pyzbar.pyzbar as pyzbar

Ogrenciler=["Fatih", "Ahmet", "Mehmet", "Ayse"]
Numaralar=["1", "2", "3", "4"]
Durumlar=[False, False, False, False]
GenelDurumlar=[False, False, False, False]

cap=cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame=cap.read()

    d=pyzbar.decode(frame)
    for obj in d:
        Val=d[0].data.decode("ascii")

        Num=0
        for i in Val:
            if i=="g":
                break

            Num+=1

        if Val[:Num]in Numaralar and Val[Num:]=="giris":
            ONum=int(Val[:Num])
            OIsim=Ogrenciler[ONum-1]
            ODurum=Durumlar[ONum-1]
            
            cv2.putText(frame, str("Giris Basarili"), (50, 50), font, 3, (0, 255, 0), 3)
            cv2.putText(frame, str(OIsim), (50, 100), font, 3, (0, 255, 0), 3)

            Durumlar[ONum-1]=True

        elif Val=="goster":
            print("")
            print(Ogrenciler)
            print(Numaralar)
            print(Durumlar)

        elif Val=="sifirla":
            cv2.putText(frame, str("Islem Basarili"), (50, 50), font, 3, (0, 255, 0), 3)
            Durumlar=GenelDurumlar

        else:
            cv2.putText(frame, str("Gecersiz"), (50, 50), font, 3, (0, 0, 255), 3)

    cv2.imshow("Frame", frame)

    key=cv2.waitKey(1)
    if key==0:
       break
