from datetime import datetime
from functools import wraps


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('main.log', 'a') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            name_function = old_function.__name__
            args_param = f' {args}'.replace(',)',')')
            kwargs_param = f'{kwargs}'
            f.write(f'Время вызова функции: {timestamp}\n'
                    f'Имя функции: {name_function}\n'
                    f'Неименованные параметры функции: {args_param}\n'
                    f'Именованные параметры функции: {kwargs_param}\n'
                    f'Возвращаемое значение функции: {result}\n')

        return result

    return new_function