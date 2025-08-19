# # 1-masala
# ball = int(input("Iltimos, 0-100 oralig'idagi ballni kiriting: "))
#
# if 0 <= ball <= 100:
#     if 90 <= ball <= 100:
#         baho = "A"
#     elif 80 <= ball <= 89:
#         baho = "B"
#     elif 79 <= ball <= 70:
#         baho = "C"
#     elif 69 <= ball <= 60:
#         baho = "D"
#     elif 60 >= ball:
#         baho = "F"
#     print(f"Sizning bahoingiz: {baho}")
# else:
#     print("Xato: Ball 0 va 100 orasida bo'lishi kerak.")
#
# #  2-masala
# yosh = int(input("Yoshingizni kiriting: "))
# tajriba = float(input("Ish tajribangiz yillardani kiriting: "))
#
# if 18 <= yosh <= 60:
#     if tajriba > 3:
#         print("Ishga qabul qilindi")
#     elif 1 <= tajriba <= 3:
#         print("Sinov muddati bilan qabul qilindi")
#     else:
#         print("Tajriba yetarli emas")
# else:
#     print("Yosh mos emas")
#
# # 3-masala
# kun = int(input("kunni kiriting: "))
# oy = int(input("oyni kiriting(1-12): "))
# yil = int(input("yilni kiriting: "))
# if 1 <= oy <= 12 and 0 < kun < 31 and oy > 0 and yil >0 and len(str(yil)) == 2025 :
#     if oy == 2:
#         if kun > 28:
#             print("fevral oyida 28 kun bor")
#     else:
#         print("sana togri")
#
# else:
#     print("kun, oy yoki yil hato kiritildi")
#
# # 4-masala
# son1 = float(input("Birinchi sonni kiriting: "))
# amal = input("Amalni kiriting (+, -, *, /): ")
# son2 = float(input("Ikkinchi sonni kiriting: "))
#
# if amal == "+":
#     natija = son1 + son2
#     print("Natija:", natija)
# elif amal == "-":
#     natija = son1 - son2
#     print("Natija:", natija)
# elif amal == "*":
#     natija = son1 * son2
#     print("Natija:", natija)
# elif amal == "/":
#     if son2 == 0:
#         print("Xatolik: nolga bo'lish mumkin emas.")
#     else:
#         natija = son1 / son2
#         print("Natija:", natija)
# else:
#     print("Xatolik: noto‘g‘ri amal kiritildi.")
#
# # 5-masala
# harorat = float(input("Haroratni kiriting (°C): "))
# yomgir = input("Yomg'ir yog'yaptimi? (ha/yo'q): ").lower()
#
# if harorat > 30:
#     if yomgir == "ha":
#         print("Issiq, soyabon oling")
#     else:
#         print("Issiq, yengil kiyining")
# elif 10 <= harorat <= 30:
#     if yomgir == "ha":
#         print("Sovuqroq, soyabon va kurtka oling")
#     else:
#         print("Yaxshi ob-havo, kurtka kiying")
# else:
#     if yomgir == "ha":
#         print("Juda sovuq, issiq kiyim va soyabon oling")
#     else:
#         print("Juda sovuq, issiq kiyim kiying")
#
# # 6-masala
# a = float(input("1-tomon uzunligini kiriting: "))
# b = float(input("2-tomon uzunligini kiriting: "))
# c = float(input("3-tomon uzunligini kiriting: "))
#
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Bu teng tomonli uchburchak.")
#     elif a == b or a == c or b == c:
#         print("Bu teng yonli uchburchak.")
#     else:
#         print("Bu turli tomonli uchburchak.")
# else:
#     print("Bunday tomonlar bilan uchburchak hosil bo'lmaydi.")
#
# # 7-masala
# baho = float(input("O'rtacha bahoni kiriting (0-100): "))
# daromad = input("Oilaviy daromad darajasi (past, o'rta, yuqori): ").lower()
#
# if baho >= 90 and daromad == "past":
#     print("To'liq stipendiya")
# elif baho >= 80 and daromad == "o'rta":
#     print("Qisman stipendiya")
# else:
#     print("Stipendiya yo'q")
#
# # 8-masala
# soat = int(input("Soatni kiriting (0-23): "))
# minut = int(input("Minutni kiriting (0-59): "))
#
# if 0 <= soat <= 23 and 0 <= minut <= 59:
#     if soat == 0:
#         am_pm_soat = 12
#         davr = "AM"
#     elif 1 <= soat < 12:
#         am_pm_soat = soat
#         davr = "AM"
#     elif soat == 12:
#         am_pm_soat = 12
#         davr = "PM"
#     else:
#         am_pm_soat = soat - 12
#         davr = "PM"
#
#     print(f"{am_pm_soat}:{minut:02} {davr}")
# else:
#     print("Xatolik: noto‘g‘ri vaqt kiritildi.")
#
# # 9-masala
# masofa = float(input("Masofani kiriting (km): "))
# byudjet = float(input("Byudjetni kiriting: "))
#
# if masofa <= 5 and byudjet >= 10:
#     print("Piyoda yoki velosiped")
# elif 5 < masofa <= 20 and byudjet >= 50:
#     print("Avtobus")
# elif masofa > 20 and byudjet >= 100:
#     print("Taksi")
# else:
#     print("Yetarli byudjet yo'q")
#
# # 10-masala
# yil = int(input("Yilni kiriting: "))
# if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
#     print("Kabisa yili")
# else:
#     print("Kabisa yili emas")
#
# # 11-masala
# parol = input("Parolni kiriting: ")
# if len(parol) < 8:
#     print("Parol juda qisqa")
# else:
#     harf_bormi = any(c.isalpha() for c in parol)
#     raqam_bormi = any(c.isdigit() for c in parol)
#
#     if harf_bormi and raqam_bormi:
#         print("Kuchli parol")
#     elif harf_bormi and not raqam_bormi:
#         print("O'rtacha parol")
#     else:
#         print("Zaif parol")
#
# # 12-masala
# summa = float(input("Xarid summasini kiriting: "))
# karta = input("Do'kon kartangiz bormi? (ha/yo'q): ").strip().lower()
#
# if summa >= 100 and karta == "ha":
#     chegirma = summa * 0.20
#     yakuniy_summa = summa - chegirma
#     print(f"Sizga 20% chegirma berildi. To'lov summasi: {yakuniy_summa} so'm.")
# elif summa >= 50 and karta == "yo'q":
#     chegirma = summa * 0.05
#     yakuniy_summa = summa - chegirma
#     print(f"Sizga 5% chegirma berildi. To'lov summasi: {yakuniy_summa} so'm.")
# else:
#     print("Chegirma yo'q.")
#
# # 13-masala
# ball = int(input("O'yin ballini kiriting: "))
# level = int(input("O'yin levelini kiriting: "))
#
# if ball >= 1000:
#     if level >= 5:
#         print("Professional")
#     else:
#         print("Havaskor")
# else:
#     print("Yangi o'yinchi")
#
# # 14-masala
# def elektr_tolovi(kt, vaqt_sohasi):
#     if vaqt_sohasi.lower() == 'kunduzi':
#         narx_1 = 0.5
#         narx_2 = 1.0
#     elif vaqt_sohasi.lower() == 'tunda':
#         narx_1 = 0.3
#         narx_2 = 0.7
#     else:
#         return "Noto'g'ri vaqt sohasi kiritildi."
#
#     if kt <= 100:
#         tolov = kt * narx_1
#     else:
#         tolov = 100 * narx_1 + (kt - 100) * narx_2
#
#     return tolov
#
# kt = float(input("Ishlatilgan elektr energiyasi (kVt): "))
# vaqt_sohasi = input("Vaqt sohasi (kunduzi/tunda): ")
#
# natija = elektr_tolovi(kt, vaqt_sohasi)
# print(f"To'lov: {natija} so'm")
#
# # 15-masala
# ovqat_narxi = float(input("Ovqat narxini kiriting: "))
# xizmat_sifati = input("Xizmat sifati (yaxshi/o'rtacha/yomon): ").lower()
#
# if xizmat_sifati == "yaxshi":
#     choypula_foizi = 0.15
# elif xizmat_sifati == "o'rtacha" or xizmat_sifati == "ortacha":
#     choypula_foizi = 0.10
# elif xizmat_sifati == "yomon":
#     choypula_foizi = 0.0
# else:
#     print("Xizmat sifati noto'g'ri kiritildi.")
#     choypula_foizi = 0.0
#
# choypula = ovqat_narxi * choypula_foizi
# umumiy_summa = ovqat_narxi + choypula
#
# print(f"Choypula: {choypula:.2f} so'm")
# print(f"Umumiy summa: {umumiy_summa:.2f} so'm")
#
# # 16-masala
# mb = float(input("mb kiriting: "))
# fayl = float(input("fayl kiriting: "))
#
# if mb >= 10 and fayl <= 100:
#     print("Shartlar bajarildi.")
# else:
#     print("Shartlar bajarilmadi.")
#
# # 17-masala
# natija = float(input("Natijani kiriting (sekundda): "))
# jins = input("Jinsni kiriting (erkak/ayol): ").lower()
#
# if jins == "erkak":
#     if natija <= 10:
#         medal = "Oltin"
#     elif natija <= 12:
#         medal = "Kumush"
#     else:
#         medal = "Bronza"
#  elif jins == "ayol":
#     if natija <= 11:
#         medal = "Oltin"
#     elif natija <= 13:
#         medal = "Kumush"
#     else:
#         medal = "Bronza"
# else:
#     medal = "Noto'g'ri jins kiritildi."
#
# print(f"Medal: {medal}")
#
# # 18-masala
# daromad = float(input("Oylik daromadingizni kiriting: "))
# kredit = float(input("Kredit summasini kiriting: "))
#
# if daromad >= 1000:
#     if kredit <= 10000:
#         print("Kredit tasdiqlandi")
#     else:
#         print("Kredit rad etildi")
# else:
#     print("Daromad yetarli emas")
#
# # 19-masala
# daqiqani = float(input("Daqiqani kiriting: "))
# sms = float(input("SMS ni kiriting: "))
#
# if daqiqani >= 100 and sms <= 50:
#     print("Sizning tarifingiz mos keladi.")
#
# else:
#     print("Tarif mos kelmaydi.")
#
# # 20-masala
# yosh = int(input("Yoshingizni kiriting: "))
# faollik = input("Faollik darajangizni kiriting (yuqori/o'rtacha/past): ").lower()
#
# if yosh <= 18:
#     if faollik == "yuqori":
#         print("Yosh sportchi")
#     elif faollik == "o'rtacha":
#         print("Oddiy yosh")
#     else:
#         print("Passiv yosh")
# elif 19 <= yosh <= 60:
#     if faollik == "yuqori":
#         print("Sportchi")
#     else:
#         print("Oddiy kishi")
# else:
#     print("Katta yoshli")
#
# # 21-masala
# kitob_turi = input("Kitob turi (ilmiy/badiiy): ").lower()
# muddat = int(input("Ijara muddati (kunlarda): "))
#
# if kitob_turi == "ilmiy":
#     if muddat <= 7:
#         narx = muddat * 5000
#     else:
#         narx = muddat * 7000
# elif kitob_turi == "badiiy":
#     if muddat <= 10:
#         narx = muddat * 3000
#     else:
#         narx = muddat * 5000
# else:
#     narx = 0
#     print("Kitob turi noto'g'ri kiritilgan!")
#
# if narx > 0:
#     print(f"Umumiy ijara narxi: {narx} so'm")
#
# # 22-masala
# tezlik = int(input("Tezlikni kiriting (km/soat): "))
# yol_turi = input("Yo'l turini kiriting (shahar/tashqari): ").lower()
#
# if yol_turi == "shahar":
#     if tezlik <= 60:
#         print("Xavfsiz")
#     else:
#         print("Jarima")
# elif yol_turi == "tashqari":
#     if tezlik <= 90:
#         print("Xavfsiz")
#     else:
#         print("Jarima")
# else:
#     print("Noto'g'ri yo'l turi kiritildi.")
# #
# # 23-masala
# vazn = float(input("Vazningizni kiriting (kg): "))
# faollik = input("Jismoniy faolligingizni kiriting (yuqori/past): ").lower()
#
# if vazn <= 70:
#     if faollik == "yuqori":
#         print("Maslahat: Normal dieta")
#     else:
#         print("Maslahat: Kaloriya ko'paytiring")
# else:
#     if faollik == "yuqori":
#         print("Maslahat: Ozish dietasi")
#     else:
#         print("Maslahat: Jiddiy ozish kerak")
#
# # 24-masala
# yosh = int(input("Yoshingizni kiriting: "))
# vaqt = input("Vaqtni kiriting (kunduzi/tunda): ").lower()
#
# if yosh <= 12:
#     if vaqt == "kunduzi":
#         narx = 5000
#     else:
#         narx = 3000
# elif 13 <= yosh <= 60:
#     if vaqt == "kunduzi":
#         narx = 10000
#     else:
#         narx = 7000
# else:  # yosh > 60
#     if vaqt == "kunduzi":
#         narx = 7000
#     else:
#         narx = 5000
#
# print(f"Chipta narxi: {narx} so'm")
#
# # 25-masala
# ball = int(input("Suhbat ballini kiriting (0-100): "))
# tajriba = input("Tajribangiz bormi? (ha/yo'q): ").lower()
#
# if ball >= 80:
#     if tajriba == "ha":
#         natija = "Ishga qabul qilingdingiz"
#     else:
#         natija = "Sinov muddati"
# elif 50 <= ball <= 79:
#     if tajriba == "ha":
#         natija = "Sinov muddati"
#     else:
#         natija = "Rad etildi"
# else:
#     natija = "Rad etildi"
#
# print(f"Natija: {natija}")