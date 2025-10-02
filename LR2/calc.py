import os
"""
1  Напишите функцию (calculate), которая принимает на вход 2 операнда,
возможно целые, возможно дробные , выполняет деление операнда 1 на операнд 2
и точность (epsilon, ключевой аргумент) по умолчанию 0.0001
(диапазон: 10**-1 < epsilon < 10**-9)
2 Напишите функцию (load_params), которая считывает значение точности
из конфигурационного файла settings.ini и задает точность для функции 1
3 Напишите тесты для тестирования работы функции 1 (
1/2, epsilon = 0.1 = 0.5, 1/1000 = 0.001 epsilon = 0.001, деление на ноль)
и функции 2 (виды тестов: проверить ситуацию открытия файла на чтение,
epsilon входит в диапазон значений, формат числа в конф. файле )
"""


def calculate(devidend, divider, epsilon=0.0001):

    if not (10**-9 < epsilon < 10**-1):
        raise ValueError("Точность должна быть в диапазоне от 10^-1 до 10^-9")

    if divider == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")

    # Сначала предполагалось использовать len(str(eps)) - 2 для округления.
    # После чего, при сверке с нейросетью оказалось, что маленькие
    # числа в python записываются с помощью научной нотации
    # (epsilon=0.00001, str=1e-05, len-2=3  ПРОБЛЕМА!)
    return round(devidend / divider, len(str(epsilon)) - 2 if '.'
                 in str(epsilon) else int(str(epsilon).split('e-')[1]))


def load_params(config_file='C:/Codes/p/3 sem/lab2/settings.ini'):
    """
    Считывает значение точности из конфигурационного файла
    Raises:
        FileNotFoundError: если файл не найден
        ValueError: если некорректный формат файла или значения
    """
    # Проверяем существование файла
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Конфигурационный файл {config_file}не найден"
                                )

    try:
        with open(config_file, 'r', encoding='utf-8') as file:

            content = file.read()

            for line in content.split('\n'):
                line = line.strip()

                if not line or line.startswith('#') or line.startswith(';'):
                    continue

                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()

                    if key == 'epsilon':
                        epsilon = float(value)

                        if not (10**-9 < epsilon < 10**-1):
                            raise ValueError("Точность должна быть в диапазоне\
                            от 10^-1 до 10^-9")

                        return epsilon
            # Если epsilon не найден, возвращаем значение по умолчанию
            return 0.0001

    except ValueError:
        raise ValueError("Некорректный формат числа в конфигурационном файле")
    except Exception:
        raise Exception("Ошибка при чтении конфигурационного файла")


print(calculate(10, 3, load_params()))
print(10**-11)
