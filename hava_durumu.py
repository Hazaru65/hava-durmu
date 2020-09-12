import requests

fail = False

secilen_il = str(input("İl: "))


for i in secilen_il:
    if i.isdigit():
        print("İnput rakamlardan oluşamaz")
        fail = True
        break

if not fail:
    r = requests.get(f"http://api.weatherapi.com/v1/current.json?key=ba6be5d0eb084ea5b33103041201209&q={secilen_il}")

    try:
        durum = r.json()["current"]["condition"]["text"]
        sicaklik = r.json()["current"]["temp_c"]
        hissedilen_sicaklik = r.json()["current"]["feelslike_c"]
        if r.json()["current"]["is_day"]:
            gunduz_mu = "Gündüz"
        else:
            gunduz_mu = "Gece"
        son_guncelleme = r.json()["current"]["last_updated"]
        ulke = r.json()["location"]["country"]
        yerel_saat = r.json()["location"]["localtime"]
        il = r.json()["location"]["name"]
    except:
        print("Aradığınız il bulunamadı")
    else:
        print(f"{ulke}/{il} {gunduz_mu} Son Güncelleme: {son_guncelleme}",f"Yerel Saat: {yerel_saat}",f"Hava Durumu: {durum}",f"Sıcaklık(C): {sicaklik} Hissedilen Sıcaklık(C): {hissedilen_sicaklik}",sep="\n")


