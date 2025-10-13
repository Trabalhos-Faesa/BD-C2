from typing import Type, Any


class Singleton(type):
    """
    Singleton Metaclass

    Based on: https://plainenglish.io/blog/better-python-singleton-with-a-metaclass
    """
    _instances: dict[Type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            instance = cls._instances[cls]
            if hasattr(cls, '__allow_reinitialization') and cls.__allow_reinitialization:
                instance.__init__(*args, **kwargs)
        return instance
