import unittest
import os
import calc


class TestCalculateFunction(unittest.TestCase):

    def test_division_normal_case(self):
        # Тест обычного деления
        self.assertEqual(calc.calculate(1, 2, epsilon=0.01), 0.5)

    def test_division_small_numbers(self):
        # Тест деления маленьких чисел
        self.assertEqual(calc.calculate(1, 1000, epsilon=0.001), 0.001)

    def test_division_by_zero(self):
        # Тест деления на ноль
        with self.assertRaises(ZeroDivisionError):
            calc.calculate(1, 0)

    def test_epsilon_out_of_range(self):
        # Тест epsilon вне диапазона
        with self.assertRaises(ValueError):
            calc.calculate(1, 2, epsilon=0.5)  # Слишком большой
        with self.assertRaises(ValueError):
            calc.calculate(1, 2, epsilon=10**-10)  # Слишком маленький

    def test_float_operands(self):
        # Тест деления дробных
        self.assertAlmostEqual(calc.calculate(1.5, 3, epsilon=0.0001), 0.5)

    def test_default_epsilon(self):
        # Тест значения по умолчанию
        result = calc.calculate(1, 3)
        self.assertIsInstance(result, float)


class TestLoadParamsFunction(unittest.TestCase):

    def setUp(self):
        # Создаем тестовый конфиг-файл
        self.test_config = 'test_settings.ini'

    def tearDown(self):
        # Удаляем его после выполнения тестов
        if os.path.exists(self.test_config):
            os.remove(self.test_config)

    def test_valid_config_file(self):
        # Тест файла
        with open(self.test_config, 'w', encoding='utf-8') as f:
            f.write("epsilon=0.01\n")

        epsilon = calc.load_params(self.test_config)
        self.assertEqual(epsilon, 0.01)

    def test_file_not_found(self):
        # Тест отсутствия файла
        with self.assertRaises(FileNotFoundError):
            calc.load_params('non_existent_file.ini')

    def test_epsilon_in_range(self):
        # Штатные тесты
        test_values = [0.01, 0.001, 0.0001, 0.00001, 0.00000001]

        for value in test_values:
            with open(self.test_config, 'w') as f:
                f.write(f"epsilon={value}\n")

            # Проверяем, что функция не выбрасывает исключение
            try:
                epsilon = calc.load_params(self.test_config)
                self.assertEqual(epsilon, value)
            except ValueError:
                self.fail(f"Epsilon {value} должен быть в допустимом диапазоне")

    def test_epsilon_out_of_range_in_file(self):
        # Тест вне диапазона в файле
        with open(self.test_config, 'w') as f:
            f.write("epsilon=0.5\n")

        with self.assertRaises(ValueError):
            calc.load_params(self.test_config)

    def test_invalid_number_format(self):
        # Тест некорректного формата
        with open(self.test_config, 'w') as f:
            f.write("epsilon=abc\n")

        with self.assertRaises(ValueError):
            calc.load_params(self.test_config)

    def test_missing_epsilon(self):
        # Тест отсутствия epsilon
        with open(self.test_config, 'w') as f:
            f.write("smth=4\n")

        # Должен вернуть значение по умолчанию
        epsilon = calc.load_params(self.test_config)
        self.assertEqual(epsilon, 0.0001)

    def test_comments_in_file(self):
        # Тест файла с комментариями
        with open(self.test_config, 'w', encoding='utf-8') as f:
            f.write("; Это комментарий\n")
            f.write("# Это тоже комментарий\n")
            f.write("epsilon=0.005\n")
            f.write("; Конец файла\n")

        epsilon = calc.load_params(self.test_config)
        self.assertEqual(epsilon, 0.005)


# Интеграционный тест
class TestIntegration(unittest.TestCase):

    def test_integration(self):
        # Использование обеих функций
        test_config = 'test_integration.ini'
        with open(test_config, 'w') as f:
            f.write("epsilon=0.01\n")

        try:
            # Загружаем epsilon из файла
            epsilon = calc.load_params(test_config)

            # Используем в calc.calculate
            result = calc.calculate(1, 4, epsilon=epsilon)
            self.assertEqual(result, 0.25)

        finally:
            # Удаляем тестовый файл
            if os.path.exists(test_config):
                os.remove(test_config)


if __name__ == '__main__':
    unittest.main()
