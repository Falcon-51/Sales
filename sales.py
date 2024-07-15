import matplotlib.pyplot as plt
from collections import defaultdict


def read_sales_data(file_path:str) -> list[dict]:

    """
    Функция читает данные о продажах с файла и возвращает список словарей.
    Каждая строка отражает отдельную запись о продажах.

    Параметры:
    -file_path:str: Путь до файла с данными.

    Возвращает: list[dict]
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        sales = []
        for line in file:
            data = line.strip().split(', ')
            sale = {
                'product_name': data[0],
                'quantity': int(data[1]),
                'price': int(data[2]),
                'date': data[3]
            }
            sales.append(sale)

    return sales



def total_sales_per_product(sales_data:list[dict]) -> dict:
    """
    Функция сумму продаж для каждого продукта и возвращает словарь.

    Параметры:
    -sales_data:list[dict]: Cписок продаж.

    Возвращает: dict
    """
    total_sales = defaultdict(int)

    for sale in sales_data:
        total_sales[sale['product_name']] += (sale['quantity'] * sale['price'])

    return total_sales




def sales_over_time(sales_data:list[dict]) -> dict:
    """
    Функция считает общую сумму продаж за каждую дату продукта и возвращает словарь.

    Параметры:
    -sales_data:list[dict]: Cписок продаж.

    Возвращает: dict
    """
    total_sales_per_date = defaultdict(int)

    for sale in sales_data:
        total_sales_per_date[sale['date']] += (sale['quantity'] * sale['price'])

    return total_sales_per_date




def main() -> None:

    # Преобразуем данные из файла
    file_path = 'sales_data.txt'
    sales_data = read_sales_data(file_path)

    # Считаем продажи для каждого продукта и узнаём продукт с наибольшей выручкой
    total_sales_per_product_data = total_sales_per_product(sales_data)
    max_revenue_product = max(total_sales_per_product_data, key=total_sales_per_product_data.get)
    print("Продукт с наибольшей выручкой:", max_revenue_product)

    # Считаем продажи для каждой даты и узнаём день с наибольшей суммой продаж
    sales_over_time_data = sales_over_time(sales_data)
    max_sales_date = max(sales_over_time_data, key=sales_over_time_data.get)
    print("День с наибольшей суммой продаж:", max_sales_date)

    # Построение графиков
    plt.figure(1)
    plt.bar(total_sales_per_product_data.keys(), total_sales_per_product_data.values())
    plt.title('Общая сумма продаж по каждому продукту')
    plt.xlabel('Название продукта')
    plt.ylabel('Сумма продаж')

    plt.figure(2)
    plt.bar(sales_over_time_data.keys(), sales_over_time_data.values())
    plt.title('Общая сумма продаж по дням')
    plt.xlabel('Дата')
    plt.ylabel('Сумма продаж')

    plt.show()


if __name__ == "__main__":
    main()
