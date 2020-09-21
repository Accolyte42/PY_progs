# Работа с исключениями Exceptions.
# Это проблемы, допускающие возможность дальнейшей работы в рамках
# Основного алгоритма. Деление на ноль, отсутствие доступной памяти...

# a = 10
# b = 0
# print(a/b)

# Для нужной обработки исключений нужно заключить потенциально опасное
# место в конструкцию try ...  и добавить само исключение except
print("start")
try:
    val = int(input("input number: "))
    tmp = 10/val
    print(tmp)
except Exception as e:
    print("Error! " + str(e))
print("stop")

# Для обработки разных исключений можно использовать  разные except
print("Start!")
try:
    val = int(input("input number: "))
    tmp = 10/val
    print(tmp)
# except (ValueError, ZeroDivisionError):
except (ValueError):
    print("value error")
except (ZeroDivisionError):
    print("zero division error")
# Для ошибок, которые не указаны
except:
    print("Error!")
print("End")

# Есть возможность передать подробную информацию об исключении в код внутри except
print("start")
try:
    val = int(input("input number: "))
    tmp = 10 / val
    print(tmp)
except ValueError as ve:
    print("valueerror! {0}".format(ve))
except ZeroDivisionError as zde:
    print("ZeroDivErr! {0}".format(zde))
except Exception as ex:
    print("Error! {0}".format(ex))
# finally показывает окончание try-except. Будет независимо от появления
# исключений.
finally:
    print("end")
























