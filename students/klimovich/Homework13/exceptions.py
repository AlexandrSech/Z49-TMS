class Error(Exception):
    """Базовый класс для других исключений"""
    pass

class DevisionByZero(Error):
    """Вызывается, когда b = 0"""
    pass

class IntCheck(Error):
    """Вызывается, когда входное значение не int"""
    pass

