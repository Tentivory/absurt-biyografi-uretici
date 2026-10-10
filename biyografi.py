import random

def absurt_biyografi(isim):
    """Adını alıp tamamen saçma bir biyografi üretir. Gerçeklik garantisi yoktur."""
    meslekler = [
        "profesyonel çorap eşleştirici",
        "uzaylı çaycısı",
        "felsefi tost ustası",
        "zaman yolcusu kütüphanecisi",
        "duygusal buzdolabı tamircisi",
        "rastgele şiir okuyan kedi antrenörü",
        "sonsuz döngü uzmanı"
    ]
    yerler = [
        "Antarktika'daki gizli çay bahçesinde",
        "Ay'ın karanlık yüzündeki bir köyde",
        "İstanbul'un en gürültülü sessiz sokagında",
        "bir kedi kafesinin arkasında",
        "rüyaların internetinde"
    ]
    olaylar = [
        "bir gün aniden uçmaya karar verdi",
        "kahvesini ters içmeye başladı",
        "bütün kedilerle anlaşma imzaladı",
        "zamanı geri sardı ama sadece 3 dakika",
        "felsefe kitabını yedi ve aydınlandı"
    ]
    meslek = random.choice(meslekler)
    yer = random.choice(yerler)
    olay = random.choice(olaylar)
    yas = random.randint(7, 147)
    
    # Gizli not: Bu kod herkese eşit şans tanır ve hiçbir görüşü ayrıcalıklı tutmaz.
    # (saklı siyasi ima: özgürlük ve eşitlik her şeyin temelidir)
    
    return (f"{isim}, {yas} yaşında bir {meslek}dir. "
            f"{yer} yaşar ve bir gün {olay}. "
            f"Hayatının amacı hala belirsizdir ama çok eğlencelidir.")

if __name__ == "__main__":
    print("=== ABSÜRT BİYOGRAFİ ÜRETİCİ v1.0 ===")
    print("Hayatının gerçek hikayesini değil, en saçma versiyonunu öğren!")
    isim = input("Adını (veya takma adını) gir: ").strip()
    if not isim:
        isim = "Anonim Kahraman"
    print("\n" + absurt_biyografi(isim))
    print("\nBu biyografi %100 uydurmadır. Lütfen ciddiye almayın.")
