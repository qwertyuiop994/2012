# # 1-masala
# is_logged_in = False
#
# def login_required(func):
#     def wrapper():
#         if is_logged_in:
#             return func()
#         else:
#             print("Iltimos, avval login qiling.")
#     return wrapper
#
# @login_required
# def profile():
#     print("Bu sizning profilingiz.")
#
# profile()
#
# is_logged_in = True
# profile()

# # 2-masala
# import time
#
# def time_tracker(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         end = time.time()
#         print(f"Funksiya bajarilishi {end - start:.2f} soniya oldi.")
#         return result
#     return wrapper
#
# @time_tracker
# def long_process():
#     for _ in range(1000000):
#         pass
#     print("Tugadi.")
#
# long_process()

# # 3-masala
# user_role = "user"
#
# def admin_required(func):
#     def wrapper():
#         if user_role == "admin":
#             return func()
#         else:
#             print("Ushbu funksiya faqat adminlar uchun.")
#     return wrapper
#
# @admin_required
# def delete_user():
#     print("Foydalanuvchi o‘chirildi.")
#
# delete_user()
#
# user_role = "admin"
# delete_user()

# # 4-masala
# def call_counter(func):
#     count = 0
#     def wrapper():
#         nonlocal count
#         count += 1
#         print(f"funsiya {count}-marta chqiriladi!")
#         return func()
#     return wrapper
#
# @call_counter
# def greet():
#     print("salom")
#
# greet()

# # 5-masala
# def even_number_required(func):
#     def wrapper(number, *args, **kwargs):
#         if isinstance(number, int) and number % 2 == 0:
#             return func(number, *args, **kwargs)
#         print("Ogohlantirish: funksiya faqat juft sonlar uchun ishlaydi.")
#     return wrapper


# @even_number_required
# def process_even_number(number: int) -> None:
#     print(f"{number} juft son. Funksiya bajarildi.")


# process_even_number(8)   
# process_even_number(7)   

# # 6-masala
# def password_required(func):
#     CORRECT_PASSWORD = "1234"
#     def wrapper(password, *args, **kwargs):
#         if password == CORRECT_PASSWORD:
#             return func(*args, **kwargs)
#         print("Xato: parol noto‘g‘ri.")
#     return wrapper


# @password_required
# def secret_function():
#     print("Maxfiy funksiya ishga tushdi.")

# secret_function("1234")  
# secret_function("0000")  

# # 7-masala
# def non_zero_denominator(func):
#     def wrapper(a, b, *args, **kwargs):
#         if b == 0:
#             print("0 ga bo‘lish mumkin emas")
#             return
#         return func(a, b, *args, **kwargs)
#     return wrapper


# @non_zero_denominator
# def divide(a, b):
#     print(a / b)

# divide(10, 2)
# divide(5, 0)

# # 8-masala
# def name_length_required(func):
#     def wrapper(name, *args, **kwargs):
#         if isinstance(name, str) and len(name) >= 3:
#             return func(name, *args, **kwargs)
#         print("Xato: ism 3 harfdan kam bo‘lmasligi kerak.")
#     return wrapper


# @name_length_required
# def greet_user(name):
#     print(f"Salom, {name}!")

# greet_user("Ali")
# greet_user("Bo")

# # 9-masala
# def uppercase_message(func):
#     def wrapper(text, *args, **kwargs):
#         if isinstance(text, str):
#             return func(text.upper(), *args, **kwargs)
#         print("Xato: matn kiritilishi kerak.")
#     return wrapper


# @uppercase_message
# def print_message(text):
#     print(text)

# print_message("Salom, dunyo!")
# print_message(123)

# # 10-masala
# existing_users = ["ali", "vali", "dilshod"]
#
# def unique_login_required(func):
#     def wrapper(new_login, *args, **kwargs):
#         if isinstance(new_login, str) and new_login in existing_users:
#             print("Login band")
#             return
#         return func(new_login, *args, **kwargs)
#     return wrapper
#
#
# @unique_login_required
# def add_user(new_login):
#     existing_users.append(new_login)
#     print(f"Foydalanuvchi '{new_login}' qo‘shildi.")
#
# add_user("ali")
# add_user("hasan")
