# n = int(input("Son kiriting: "))
# i = 1
# yigindi = 0
#
# while i <= n:
#     yigindi += i
#     i += 1
#
# print(f"{n} gacha bo'lgan sonlar yig'indisi: {yigindi}")
#
# while mavzusidan 10 talig masala yechilishi
#
# 1
# son = int(input("sonni kiriting(0 stop): "))
# yigindi = 0
# while son != 0 :
#     yigindi+=son
#     son = int(input("Sonni kiriting(0 stop): "))
#
# print(f"Siz bergan raqamlar yigindisi {yigindi}")
#
#
# 2
# max_son = 0
# son = int(input("..."))
# while True:
#     son = int(input("..."))
#     if son ==  0:
#         break
#     if son > max_son:
#         max_son = son
#
# print(f"eng katta son {max_son}")
#
#
# 3
# parol = input("parolni kiriting: ").lower()
# while parol != "python123":
#     h = "parol togri kiritildi"
#     parol = input("parolni kiriting: ").lower()
#
# print(f"{h}")
#
#
# 4
# son = int(input("Son kiriting: "))
# h = ''
# while son > 0:
#     h += str(son)
#     break
# print(f"son {len(h)} raqamdan iborat")
#
#
# 5
# son = int(input("Son kiriting: "))
# teskari = 0
# while son > 0:
#     qoldiq = son % 10
#     teskari = teskari * 10 + qoldiq
#     son //= 10
# print("Teskari:", teskari)
#
#
# 6
# # Foydalanuvchidan son kiritish so'raladi va kiritilgan matn butun songa aylantiriladi
# son = int(input("Son kiriting: "))
#
# # Agar son 2 dan kichik bo'lsa, u tub son emas
# if son < 2:
#     print("Tub emas")
# else:
#     # Tekshiruv uchun boshlang'ich qiymat sifatida x=2 olinadi
#     x = 2
#     # Tub ekanligini ko'rsatuvchi o'zgaruvchi, boshlang'ich qiymati True
#     tub = True
#     # x * x <= son sharti bilan tsikl boshlanadi (optimallashtirish uchun ildizigacha tekshirish kifoya)
#     while x * x <= son:
#         # Agar son x ga qoldiqsiz bo'linsa, demak u tub emas
#         if son % x == 0:
#             tub = False
#             break  # Tsiklni to'xtatish, chunki tub emasligi aniqlandi
#         x += 1  # Keyingi x qiymatiga o'tish
#     # tub o'zgaruvchisiga qarab "Tub son" yoki "Tub emas" chiqariladi
#     print("Tub son" if tub else "Tub emas")
#
#
# 7
# s = input("maxsus sozni kiriting: ").lower()
# d = ''
# while s != "stop":
#     d += s
#     s = input("maxsus sozni kiriting: ").lower()
#
#
# print(f"harflar soni {len(d)}")
#
#
# 8
# son = int(input("sonni kiriting: "))
# y = 0
# while son != 0:
#     if son % 2 != 0:
#         y += son
#     son = int(input("sonni kiriting: "))
#
# print(f"toq sonar yigindisi {y}")
#
#
# 9
# soni = 0
# yigindi = 0
# harorat = int(input("Haroratni kiriting (-100 - to‘xtatish): "))
# while harorat != -100:
#     yigindi += harorat
#     soni += 1
#     harorat = int(input("Yana harorat kiriting (-100 - to‘xtatish): "))
# if soni > 0:
#     print("O‘rtacha harorat:", yigindi / soni)
# else:
#     print("Hech qanday harorat kiritilmadi.")
#
#
# 10
# foyda = input("(ha/yoq): ")
# while foyda != "ha":
#     foyda = input("(ha/yoq): ")
#
# print("rahmat")
#
#
# While tsikli mavzusidan qiziqarli 50 ta algoritmik masala yechilishi
#
# 1
# vazn = float(input("Boshlang‘ich vazn va maqsad vaznni kiritish: "))
# maqsad = 10
# yoqolgan = 0.7
# hafta_son = 0
# while vazn > maqsad:
#     vazn -= yoqolgan
#     hafta_son += 1
#
# print(f"maqsadga yetishingiz uchun {hafta_son} hafta kerak")
#
#
# 2
# daraxt = 1
# osish = 1.2
# maqsad = 5
# yil = 0
# while daraxt < maqsad:
#     daraxt *= osish
#     yil += 1
#
# print(f"daraxt 5 metr bolishi uchun {yil} yil kerak")
#
#
# 3
# bor = 100
# kun = 5
# kunlar = 0
# while bor > 0:
#     bor -= kun
#     kunlar += 1
#
#
# print(f"uyingizdagi energiya zaxirasi {kunlar} kunda tugaydi")
#
#
# 4
# umumiy = 100
# kunlik = 2
# hafta = 1
# joriy = 0
# kun = 0
# while joriy < umumiy:
#     joriy += kunlik
#     kun += 1
#     if kun % 7 == 0:
#         joriy -= hafta
#
# print(f"maqsadingizga yetish uchun {kun} kun kerak ")
#
#
# 5
# bosh = 5000
# kunlik = 200
# kun = 0
# while bosh > 0:
#     bosh -= kunlik
#     kun +=1
#
# print(f"umbordagi suv {kun} kunda tugaydi")
#
#
# 6
# umumiy = 10_000_000
# kunlik = 250_000
# kun = 0
# while umumiy > 0:
#     umumiy -= kunlik
#     kun += 1
#
# print(f"{kun} kun sayohat qila olasiz")
#
#
# 7
# masqad = 1_000
# yuzduzlar =  0
# kechalar = 0
# while yuzduzlar < masqad:
#     yuzduzlar += 50
#     kechalar += 1
#
# print(f"1000 ta yulduz katalogini {kechalar} kechada to‘ldiradi")
#
#
# 8
# maqsad = 500
# ball = 0
# oyin = 0
# while maqsad > ball:
#     ball += 25
#     oyin += 1
#
# print(f"500 ballga yaetish uchun {oyin} oyin kerak")
#
#
# 9
# maqsad = 1000
# kunlik = 50
# hozir = 0
# kun = 0
# while hozir < maqsad:
#     hozir += kunlik
#     kun += 1
#
# print(f"qurulish {kun} kunda tugaydi")
#
#
# 10
# harorat = 30
# pas = 2
# soat = 0
# while harorat > 0:
#     harorat -= pas
#     soat += 1
#
# print(f"harorat 0℃ ga yetguncha  {soat} soat otadi")
#
#
# 11
# maqsad = 50_000_000
# har = 2_000_000
# joriy = 0
# film = 0
# while joriy < maqsad:
#     joriy += har
#     film += 1
#
# print(f"50 million jamgarish uchun {film} filmda oynash kerak")
#
#
# 12
# jami = 100
# har_s = 2
# yuklangan = 0
# soniya = 0
# while yuklangan < jami:
#     yuklangan += har_s
#     soniya += 1
#
# print(f"yuklash {soniya} soniyada tugaydi")
#
#
# 13
# jami_m = 500
# har_k = 20
# kunlik = 0
# kun = 0
# while kunlik < jami_m:
#     kunlik += har_k
#     kun += 1
#
# print(f"{kun} kundan keyin bogdagi mevalar boshaydi")
#
#
# 14
# mashina = 20_000_000
# maqsad = 5_000_000
# yil_f = 0.1
# yil = 0
# while maqsad < mashina:
#     mashina = mashina - (mashina * yil_f)
#     yil += 1
#
# print(f"5 million somgacha {yil} yil kerak ")
#
#
# 15
# maqsad = 200
# har_k = 10
# kun = 0
# joriy = 0
# while joriy < maqsad:
#     joriy += har_k
#     kun += 1
#
# print(f"200 km yugurish uchun {kun} kun kerak")
#
#
# 16
# maqsad = 50
# joriy = 0
# har_y = 3
# yil = 0
# while joriy < maqsad:
#     joriy += har_y
#     yil += 1
#
# print(f"50 mm ga yetishi uchun {yil} yil kerak")
#
# 17
# maqsad = 1_000_000
# har_v = 50_000
# joriy = 0
# video = 0
# while joriy < maqsad:
#     joriy += har_v
#     video += 1
#
# print(f"1 million topish uchun {video} video kerak")
#
#
# 18
# maqsad = 5000
# kunlik = 100
# joriy = 0
# kun = 0
# while joriy < maqsad:
#     joriy +=kunlik
#     kun += 1
#
# print(f"5000 ta testni {kun} kuncha yakunlaydi")
#
#
# 19
# jami = 2000
# kunlik = 150
# kun = 0
# while 0 < jami:
#     jami -= kunlik
#     kun += 1
#
# print(f"{kun} kundan keyin mahsulot tugaydi")
#
#
# 20
# maqsad = 50_000
# har_s = 1_000
# joriy = 0
# soat = 0
# while joriy < maqsad:
#     joriy += har_s
#     soat += 1
#
# print(f"50,000 km masofani {soat} soatda bosib o‘tadi")
#
#
# 21
# boshlangich = 10_000_000
# foiz = 0.07
# maqsad = 20_000_000
# yechib = 400_000
# yil = 0
# while boshlangich < maqsad:
#     boshlangich = boshlangich * (1 + foiz)
#     boshlangich -= yechib
#     yil += 1
#     if boshlangich < 10_000_000:
#         print("maqsadga erishib olmaydi")
#         break
#
# else:
#     print(f"maqsad ga {yil} yilda erishiladi")
#
#
# 22
# maqsad = 5000
# kasalla = 1000
# foiz = 0.15
# kunlik = 50
# kun = 0
# while kasalla < maqsad:
#     kasalla = kasalla * (1+foiz)
#     kasalla -= kunlik
#     kun += 1
#
# print(f"kassalar soni 5000 ga {kun} kunda yetadi")
#
#
# 23
# kunlik = 2
# hafta = 0.5
# maqsad = 10
# joriy = 0
# kun = 0
# while joriy < maqsad:
#     joriy += kunlik
#     kun += 1
#     if kun % 7 == 0:
#         joriy -= hafta
#
# print(f"10 tonna yetkuncha {kun}  kun kerak")
#
#
# 24
# tolov = 50_000_000
# yillik = 0.01
# har = 1_000_000
# oy = 0
# while 0 < tolov:
#     tolov -= har
#     yillik = yillik * 0.01
#     tolov += yillik
#     oy += 1
#     if oy % 12 == 0:
#         tolov *= 1.2
#
# print(f"kreditni {oy} oyda tolab bolasiz")
#
#
# 25
# batarya = 4000
# har_s = 150
# har = 50
# soat = 0
# while 0 < batarya:
#     batarya -= har_s
#     soat += 1
#     if soat % 3 == 0:
#         batarya += har
#
# else:
#     print(f"quvvat tugashigacha {soat} soat ishlaydi")
#
#
# 26
# bor = 10_000
# foiz = bor * 0.05
# yangi = 200
# maqsad = 5000
# yil = 0
# while bor > maqsad:
#     bor -= foiz
#     bor += yangi
#     yil += 1
#
# print(f"daraxtlar 5000 tagacha kamayguncha {yil} yil otadi")
#
# 27
# bosh = 50
# ha_km = 0.1
# har = 2
# maqsad = 600
# km = 0
# while bosh > 0:
#     bosh -= ha_km
#     if km % 100 == 0:
#         bosh += har
#     km += 1
#
# print(f"{km} km dan yoqilgi tugaydi")
#
#
# 28
# bizda = 10
# har_k = 0.5
# bonus = 1
# kun = 0
# while bizda > 0:
#     bizda -= har_k
#     if kun % 7 == 0:
#         bizda += bonus
#     kun += 1
#
# print(f"trafik {kun} kunda tugaydi")
#
#
# 29
# bosh = 5000
# kunlik = 200
# keladi = 300
# kun = 0
# while bosh > 0:
#     bosh -= kunlik
#     if kun % 5 == 0:
#         bosh += keladi
#     kun += 1
#
# print(f"ombor boshashigacha {kun} kun kerak")
#
#
# 30
# bosh = 100
# h_soat = 100 * 0.2
# yoq = 10
# maqsad = 500
# soat = 0
# while bosh < maqsad:
#     bosh += h_soat
#     if soat % 10 == 0:
#         bosh -= 10
#     soat += 1
#
# print(f"Hujayralar 500 taga yetguncha {soat} soat kerak")
#
#
# 31
# bosh = 5_000_000
# foiz = bosh * 0.1
# hafta = 0
# while bosh > 0:
#     if hafta % 4 == 0:
#         bosh += foiz
#     bosh -= 200000
#     hafta += 1
#
# print(f"qarzni {hafta} haftada tolab tugatasiz")
#
#
# 32
# bosh = 0
# daslabki = 80
# har = 2
# maqsad = 1000
# soat = 0
# while bosh < maqsad:
#     bosh += 80
#     if soat % 2 == 0:
#         daslabki += 10
#     soat += 1
#
# print(f"1000 km ga yetguncha {soat} soat kerak")
#
#
# 33
# suv = 90
# har_d = 2
# har_b = 3
# maqsad = 50
# daqiqa = 0
# while suv > maqsad:
#     suv -= har_d
#     if daqiqa % 5 == 0:
#         suv += har_b
#     daqiqa += 1
#
# print(f"50°C ga yetguncha {daqiqa} daqiqa kerak")
#
#
# 34
# bor = 10
# har_k = 0.8
# har_u = 5
# kun = 0
# while bor > 0:
#     bor -= har_k
#     if kun % 3 == 0:
#         bor += 0.5
#     kun+= 1
#
# print(f" Yuk tugashigacha {kun} kun kerak")
#
#
# 35
# umumiy = 1000
# joriy = 0
# kunlik = 50
# hafta_s = 20
# kun = 0
# while joriy< umumiy:
#     joriy += kunlik
#     if kun % 7 == 0:
#         joriy -= hafta_s
#     kun += 1
#
# print(f"Kursni {kun} kunda tugatasiz")
#
#
# 36
# bosh = 50
# har_k = 10
# har_t = 15
# maqsad = 100
# kun = 0
# while bosh < maqsad:
#     bosh += har_k
#     if kun % 4 == 0:
#         bosh -= har_t
#     kun += 1
#
# print(f"100 PM2.5 ga yetguncha {kun} kun kerak")
#
#
# 37
# bosh = 2000
# kunlk = 100
# hafta = 50
# kun = 0
# while bosh > 0:
#     bosh -= kunlk
#     if kun % 7 == 0:
#         bosh += hafta
#     kun += 1
#
# print(f'Hosil tugashigacha {kun} kun kerak')
#
#
# #38
# server = 0
# soat = 5
# har = 20
# soat = 0
# maqsad = 80
# while server < maqsad:
#     server += soat
#     if soat % 6 == 0:
#         server -= har
#     soat += 1
#
# print(f"80% ga yetguncha {soat} soat kerak")
#
#
# #39
# bosh = 0
# kunlik = 5
# har = 2
# maqsad = 100
# kun = 0
# while bosh < maqsad:
#     bosh += kunlik
#     if kun % 3 == 0:
#         bosh -= har
#     kun += 1
#
# print(f"100 km ga yetguncha {kun} kun kerak")
#
#
# 40
# bosh = 10000
# kunlik = 500
# hafta = 200
# kun = 0
# while bosh > 0:
#     bosh -= kunlik
#     if kun % 7 == 0:
#         bosh += hafta
#     kun += 1
#
# print(f"Energiya tugashigacha {kun} kun kerak")
#
#
# 41
# bosh = 0
# har = 100
# besh = 20
# maqsad = 2000
# soat = 0
# while bosh < maqsad:
#     bosh += har
#     if soat % 5 == 0:
#         bosh -= besh
#     soat += 1
#
# print(f"2000 sahifa chop etish uchun {soat} soat kerak")
#
#
# 42
# bosh = 20
# har = 1
# maqsad = 10
# kun = 0
# while bosh > maqsad:
#     bosh -= har
#     if kun % 4 == 0:
#         bosh += 2
#     kun += 1
#
# print(f"10°C ga yetguncha {kun} kun kerak")
#
#
# 43
# bosh = 1000000
# har = 200000
# foiz = bosh * 0.8
# maqsad = 2000000
# yil = 0
# while bosh < maqsad:
#     bosh += foiz
#     bosh -= har
#     yil += 1
#
# print(f"2 million so‘mga yetguncha {yil} yil kerak")
#
#
# 44
# bosh = 5000
# soat = 200
# har = 50
# soats = 0
# while bosh > 0:
#     bosh -= soat
#     if soats % 3 == 0:
#         bosh += har
#     soats += 1
#
# print(f"Jarayon {soats} soatda tugaydi")
#
#
# 45
# bosh = 50
# h_soat = 2
# har = 3
# maqsad = 20
# soat = 0
# while bosh > maqsad:
#     bosh -= h_soat
#     if soat % 5 == 0:
#         bosh += har
#     soat += 1
#
# print(f"Tezlik 20 MB/s ga yetguncha {soat} soat kerak")
#
#
# 46
# bosh = 50
# yillik = bosh * 1.1
# maqsad = 100
# yil = 0
# while bosh < maqsad:
#     bosh += yillik
#     bosh -= 10
#     yil += 1
#
# print(f"100 xodimga yetguncha {yil} yil kerak")
#
#
# 47
# bosh = 1000
# kunlik = 50
# hafta = 10
# kun = 0
# while bosh > 0:
#     bosh -= 50
#     if kun % 7 == 0:
#         bosh += hafta
#     kun += 1
#
# print(f"Ta’mir {kun} kunda tugaydi")
#
#
# 48
# bosh = 80
# har_d = 3
# maqsad = 50
# minut = 0
# while bosh > maqsad:
#     bosh -= har_d
#     if minut % 4 == 0:
#         bosh += 5
#     minut += 1
#
# print(f"50 dB ga yetguncha {minut} daqiqa kerak")
#
#
# 49
# bosh = 100
# kunlik = 5
# maqsad = 50
# kun = 0
# while bosh > maqsad:
#     bosh -= kunlik
#     if kun % 3 == 0:
#         bosh += 10
#     kun += 1
#
# print(f"50 mg/l ga yetguncha {kun} kun kerak")
#
#
# 50
# bosh = 0
# kunlik = 2
# maqsad = 100
# kun = 0
# while bosh < maqsad:
#     bosh += kunlik
#     if kun % 7 == 0:
#         bosh -= 1
#     kun += 1
#
# print(f"100% ga yetguncha {kun} kun kerak")
#
#
# while mavzusidan 25 taglig masala
#
# 1
# summa = int(input("boshlangich summa: "))
# foiz = float(input("foizni stavkasini: "))
# maqsad = summa * 2
# foiz_h = foiz / 100
# yil = 0
# while summa < maqsad:
#     summa = summa + (summa * foiz_h)
#     yil += 1
#
# print(f"{yil} yildan keyin pullaringiz ikki baravar kopayadi")
#
#
# 2
# bosh = 1
# maqsad = 1000000
# kopayish = 20
# daqiqa = 0
# soat = 0
# while bosh < maqsad:
#     daqiqa += 20
#     bosh += 2
#     if daqiqa % 60 == 0:
#         soat += 1
#
# print(f"1 million bakteriya bo'lishi uchun {soat} soat daqiqada esa {daqiqa} daqiqa")
#
#
# 3
# qarz = int(input("qarzingizni kiriting: "))
# foiz = float(input("oylik foizni kiriting: "))
# oylik = int(input("oylik tolov miqdori: "))
# foiz_h = foiz / 100
# oy = 0
# while qarz > 0:
#     if foiz > oylik:
#         print(f"foiz juda yuqori qarzdan qutula olmaysiz")
#         break
#     qarz = qarz + (qarz * foiz_h)
#     qarz -= oylik
#     oy += 1
#
# print(f"{oy} oyda qarzdan qutulasiz")
#
#
# 4
# bosh = 100
# yoq = 15
# minmal = 20
# soat = 0
# while bosh > minmal:
#     bosh -= yoq
#     soat += 1
#
# print(f"{soat} soatdan keyin telefon o'chadi (20% dan past)")
#
#
# 5
# bosh = int(input(f"boshlangich mahsulot miqdorini kiritish: "))
# kunlik = int(input("kunlik sotish miqdorini kiriting: "))
# kunlik_k = int(input("kunlik kelish miqdorini kiriting: "))
# kun = 0
# while bosh > 0:
#     if kunlik <= kunlik_k:
#         print(f"ombordagi mahsulot tugamaydi: ")
#         break
#     bosh -= kunlik
#     bosh += kunlik_k
#     kun += 1
#
# else:
#     print(f"{kun} kundan keyin ombor bo'shaydi")
#
#
# 6
# hajm = 2000
# ketish = 50
# kelish = 200
# hozir = 0
# daqiqa = 0
# while hajm > hozir:
#     hozir -= 50
#     hozir += 200
#     daqiqa += 1
#
# print(f"2 litrlik idish {daqiqa} daqiqada to'ladi")
#
#
# 7
# bak = int(input("avtomobilingizda necha litr benzin bor: "))
# km = 0
# while bak > 1:
#     km += 10
#     if km % 100 == 0:
#         bak -= 8
#
# print(f"{km} kmgacha borasiz benzin juda oz qoldi")
#
#
# 8
# yashaydi = 100_000
# osish = yashaydi * 0.03
# maqsad = 200_000
# yil = 0
# while yashaydi < maqsad:
#     yashaydi += osish
#     yil += 1
#
# print(f"{yil} yildan keyin populyatsiya 200,000 ga yetadi")
#
#
# 9
# umumiy = 50
# har_k = 2.5
# kun = 0
# while umumiy > 0:
#     umumiy -= har_k
#     kun += 1
#
# print(f"{kun} kundan keyin trafik tugaydi")
#
#
# 10
# def maktab_baxosi():
#     maqsad_ortacha = float(input("Maqsad ortacha baxo: "))
#     baholar = []
#     print("Mavjud baxoni kiriting (0-tugash uchun): ")
#     while True:
#         baho = float(input("Baho: "))
#         if baho == 0:
#             break
#
#         if 2 <= baho <= 5:
#             baholar.append(baho)
#
#         else:
#             print(f"baho 2 dan 5 gacha bolishi kerak: ")
#
#
#     if not baholar:
#         print(f"baxolar kiritilmadi: ")
#         return
#     joriy_ortacha = sum(baholar) / len(baholar)
#     hafta = len(baholar)
#     print(f"boshlangich ortacha: {joriy_ortacha:.2f}")
#
#
#     while joriy_ortacha < maqsad_ortacha:
#         hafta += 1
#         print(f"/n{hafta}-hafta. kerakli minimum baxo: {(maqsad_ortacha * hafta - sum(baholar)):.2f}")
#
#
#         yangi_baxo = float(input("yangi baxo: "))
#         if 2 <= yangi_baxo <= 5:
#             baholar.append(yangi_baxo)
#             joriy_ortacha = sum(baholar) / len(baholar)
#             print(f"yangi ortacha: {joriy_ortacha:.2f}")
#         else:
#             print(f"baxo 2 dan 5 gacha bolishi kerak")
#             hafta -= 1
#     print(f"maqsadga erishildi ortacha baxo")
# maktab_baxosi()
#
#
# # 11
# def restoran():
#     buyutma = int(input("buyurtmalar soni (0-soni): "))
#     vaqt = 5
#     kutish = 0
#     buytma_s = 0
#     while buyutma > 0:
#         if buyutma == 0:
#             print(f"buyurtmalar soni min 1 bolishi keral")
#         buyutma -= 1
#         buytma_s += 1
#         buyutma = int(input("buyurtmalar soni (0-soni): "))
#         kutish += vaqt
#         if buyutma == 0:
#             print(f"{buytma_s} ta buyutmangiz {kutish} daqiqada tayyor boldi ")
#
# restoran()
#
#
# def restaran():
#     buyurtmalar = int(input("buyurma soni (0-stop): "))
#     navbat = 0
#     kutish = 0
#     b_vaqti = 5
#     tayyor = 0
#     while True:
#         if buyurtmalar <= 0:
#             print(f"buyrtmalar soni kamida 1 bolishi kerak")
#             break
#         tayyor += 1
#         navbat += buyurtmalar
#         kutish += b_vaqti
#         while navbat > 0:
#             buyurtma2 = int(input("buyurma soni (0-stop): "))
#             if buyurtma2 < 0:
#                 print(f"buyrtmalar soni kamida 1 bolishi kerak")
#                 continue
#
#             navbat += buyurtma2
#             tayyor += 1
#             navbat -= 1
#
#             if navbat <= 0:
#                 print(f"{tayyor - 1} ta buyurtmangiz tayyor boldi ketgan vaht {kutish}")
#                 break
#             kutish += b_vaqti
#
#             if buyurtma2 == 0:
#                 print(f"tayyor bolgan buyrtma soni {tayyor} va qolgan buyrtma {navbat - 1} ta (tashrifingiz uchun katta rahmat😊) ")
#                 print(f"ketgan vaht {kutish} daqiqa (qolgan buytmangiz {(navbat - 1)*5} daqiqada tayyor boladi)")
#                 continue
#
#
# restaran()
#
#
# 12 variant 1
# kredit = int(input("kredit miqdori: "))
# oyda = int(input("oylik tolov: "))
# oy = 0
# jami = 0
# jadval = []
# if kredit > oyda:
#     while kredit > 0:
#         kredit -= oyda
#         jami += oyda
#         oy += 1
#         jadval.append(oyda)
#
# print(f"jami tolangan pul {jami} tolangan oy {oy} ")
# print(f"tolov jadvali {jadval} ")
#
#
# variant 2
# kredit = int(input("kredit miqdori: "))
# oyda = int(input("oylik tolov: "))
# jami_kredit = kredit - oyda
# oy = 0
# jami = 0
# yil = 0
# oy2 = 0
# jadval = []
# jadval.append(oyda)
# if kredit > oyda:
#     while jami_kredit > 0:
#         oyda2 = int(input("oylik tolov (0-qolgan kreditingni korish uchun: ): "))
#         jami_kredit -= oyda2
#         jami += oyda2
#         oy += 1
#         oy2 += 1
#         if not oyda2 == 0:
#             jadval.append(oyda2)
#         if oyda2 == 0:
#             print(f"tolangan kredit {jami+oyda} so'm qolgan {jami_kredit} so'm")
#         if oy % 12 == 0:
#             yil += 1
#             oy -= 12
#         if jami + oyda > kredit:
#             print(f"siz ortiqcha {(jami + oyda)-kredit} som toladingiz ")
#
#
#     print(f"jami tolangan pul {jami + oyda} tolangan vaht {yil} yili {oy +1} oy ")
#     print(f"tolov jadvali {jadval}",end="")
#
#
# 13
# bosh = int(input("sonni kiriting: "))
# if bosh < 0:
#     print(f"manfiy son kirtdingiz")
# qadam = 0
# while bosh != 1:
#     if bosh % 2 == 0:
#         bosh = bosh / 2
#         qadam += 1
#     else:
#         bosh = bosh * 3 + 1
#         qadam += 1
#
# print(f"{qadam} qadamlar soni")
#
#
# 14
# def kaprekar(son):
#     son = f"{son:04}"
#     qadamlar = []
#
#     while son != "6174":
#         if son in qadamlar:
#             return qadamlar + {son}, "tsikl paydo bo'ldi"
#
#         qadamlar.append(son)
#
#         raqamlar = list(son)
#         katta_tartib = ''.join(sorted(raqamlar, reverse=True))
#         kichik_tartib = ''.join(sorted(raqamlar))
#
#         natija = int(katta_tartib) - int(kichik_tartib)
#         son = f"{natija:04d}"
#
#     qadamlar.append("6174")
#     return qadamlar, "muvaffaqiyatli"
#
# son =  input("sonni kiriting: ")
# qadamlar, holat = kaprekar(son)
# print(f"qadamlar: {qadamlar}")
# print(f"holat: {holat}")
#
#
# 15
# def paskal_uchburchagi(n):
#     if n <= 0:
#         return []
#
#     uchburchak = [[1]]  # Birinchi qator
#     qator_raqami = 1
#
#     while qator_raqami < n:
#         oldingi_qator = uchburchak[qator_raqami - 1]
#         yangi_qator = [1]  # Har qator 1 bilan boshlanadi
#
#         i = 1
#         while i < len(oldingi_qator):
#             yangi_qator.append(oldingi_qator[i-1] + oldingi_qator[i])
#             i += 1
#
#         yangi_qator.append(1)  # Har qator 1 bilan tugaydi
#         uchburchak.append(yangi_qator)
#         qator_raqami += 1
#
#     return uchburchak
#
# qator = int(input("paskal uchuburchagi uchun qator: "))
# natija = paskal_uchburchagi(qator)
# qator_raqami = 0
# while qator_raqami < len(natija):
#     print(f"Qator {qator_raqami + 1}: {natija[qator_raqami]}")
#     qator_raqami += 1
#
#
# def sehrli_kvadrat(n):
#     if n % 2 == 0:
#         return "Faqat toq sonlar uchun!"
#
#     kvadrat = []
#     i = 0
#     while i < n:
#         qator = []
#         j = 0
#         while j < n:
#             qator.append(0)
#             j += 1
#         kvadrat.append(qator)
#         i += 1
#
#     qator = 0
#     ustun = n // 2
#
#     son = 1
#     while son <= n * n:
#         kvadrat[qator][ustun] = son
#
#         yangi_qator = (qator - 1) % n
#         yangi_ustun = (ustun + 1) % n
#
#         if kvadrat[yangi_qator][yangi_ustun] != 0:
#             qator = (qator + 1) % n
#         else:
#             qator = yangi_qator
#             ustun = yangi_ustun
#         son += 1
#
#     return kvadrat
#
# n = int(input("sonni kiriting: "))
# kvadrat = sehrli_kvadrat(n)
#
# if isinstance(kvadrat, list):
#     i = 0
#     while i < len(kvadrat):
#         print(kvadrat[i])
#         i += 1
#
# else:
#     print(kvadrat)