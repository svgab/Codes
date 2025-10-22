class DivisionWithEpsException(Exception):
    def __str__(self):
        return "General Exception for Division with Epsilon Project"


class SettingsFileNotFoundError(DivisionWithEpsException):
    def __str__(self):
        return "Отсутствует конфигурационный файл"


class EpsilonKeyNotFound(DivisionWithEpsException):
    def __str__(self):
        return "Отсутствует ключ epsilon"
