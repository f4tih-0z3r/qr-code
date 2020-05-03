import cv2
import pyzbar.pyzbar as pyzbar
import time

Ogrenciler=["Fatih", "Ahmet", "Mehmet", "Ayse"]
Numaralar=["1", "2", "3", "4"]
Durumlar=[False, False, False, False]
GenelDurumlar=[False, False, False, False]
Gelmeyenler=[]

Kapatiliyor=False

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
            Gelmeyenler=[]

        elif Val=="gelmeyenler":
            Gelmeyenler=[]
            Sayac=0

            for i in Durumlar:
                if i==False and not Ogrenciler[Sayac] in Gelmeyenler:
                    Gelmeyenler.append(Ogrenciler[Sayac])

                Sayac+=1

            if len(Gelmeyenler)==0:
                print("Herkes Tam")

            else:
                print(Gelmeyenler)

        elif Val=="kapat":
            cv2.putText(frame, str("Program Kapatiliyor"), (50, 50), font, 3, (0, 255, 0), 3)
            time.sleep(2)

            Kapatiliyor=True
            break

        else:
            cv2.putText(frame, str("Gecersiz"), (50, 50), font, 3, (0, 0, 255), 3)

    cv2.imshow("Frame", frame)

    if Kapatiliyor==True:
        cap.release()
        cv2.destroyAllWindows()
        break

    key=cv2.waitKey(1)
    if key==0:
       break
