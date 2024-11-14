def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() # здесь внутренняя функция ничего не возвращает


inner_function() # здесь внутренняя функция не работает,
                # потому что мы не можем доставать значения внутри функции извне.
                # Это связано с различием пространства имён


test_function() # тест функция работает