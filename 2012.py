cheklov = int(input("belgilangan tezlikni kiriting:  "))
tezlik = int(input("haqiqiy tezikni kiriting:  "))
qoyda_buzilish_soni = int(input("nechinchi marotaba qoida buzilmoqda:  "))

BHM = 375_000

farq = tezlik-cheklov


if farq <= 0:
    print("jarima qollanilmaydi!")
elif 0 < farq <= 20:
    if qoyda_buzilish_soni == 1:
        print(f"jarima: {BHM} so'm!")
    elif qoyda_buzilish_soni == 2:
        print(f"jarima: {BHM * 5} so'm!")
    else:
        print(f"jarima: {BHM * 15} so'm va 1 yil haydovchilik guvohnomadan mahrum qilish belgilansin!")
elif 21 <= farq <= 40:
    if qoyda_buzilish_soni ==1:
        print(f"jarima: {BHM * 5} so'm!")
    else:
        print(f"jarima: {BHM * 15} so'm va 1 yil haydovchilik guvohnomadan mahrum qilish belgilansin!")
else:
    if qoyda_buzilish_soni ==1:
        print(f"jarima: {BHM * 9} so'm!")
    else:
        print(f"jarima: {BHM * 25} so'm va 2 yil haydovchilik guvohnomadan mahrum qilish belgilansin!")