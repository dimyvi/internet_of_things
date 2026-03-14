from abc import ABC, abstractmethod


class StorageUnit(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def remove_item(self, item):
        pass


class Warehouse(StorageUnit):
    def __init__(self, name, address, total_items):
        self.name = name
        self.address = address
        self.total_items = total_items

    def add_item(self, item):
        if item < 0:
            raise ValueError("Количество товаров для добавления не может быть отрицательным")
        self.total_items += item

    def remove_item(self, item):
        if item < 0:
            raise ValueError("Количество товаров для удаления не может быть отрицательным")
        self.total_items -= item

    def get_info(self):
        return self.name, self.address, self.total_items


class Employee:
    def __init__(self, name: str, position: str, current_task: str) -> None:
        self.name = name
        self.position = position
        self.current_task = current_task

    def assign_task(self, task):
        self.current_task = task

    def cancel_task(self):
        self.current_task = None

    def get_status(self):
        return self.current_task


class Product:
    def __init__(self, name, status, price, category):
        self.name = name
        self.status = status
        self.price = price
        self.category = category

    def mark_as_shipped(self):
        self.status = "Отгружен"

    def mark_as_received(self):
        self.status = "Принят"

    def info(self):
        return self.name, self.status, self.price, self.category


class Task:
    def __init__(self, task_type, employee, status, product):
        self.task_type = task_type
        self.employee = employee
        self.status = status
        self.product = product

    def start_task(self):
        self.employee.assign_task(self.task_type)
        self.status = "Выполняется"

    def finish_task(self):
        self.employee.cancel_task()
        self.status = "Завершена"
        if self.task_type == "Отгрузка":
            self.product.mark_as_shipped()
        elif self.task_type == "Приемка":
            self.product.mark_as_received()

    def get_details(self):
        return self.task_type, self.employee.name, self.product.name, self.status


class Database:
    def __init__(self):
        self.warehouses = []
        self.employees = []
        self.products = []
        self.tasks = []
        self.logs = []

    def save_warehouse(self, warehouse):
        self.warehouses.append(warehouse)
        self.logs.append(f"Склад {warehouse.name} сохранен в БД")

    def save_employee(self, employee):
        self.employees.append(employee)
        self.logs.append(f"Сотрудник {employee.name} сохранен в БД")

    def save_product(self, product):
        self.products.append(product)
        self.logs.append(f"Товар {product.name} сохранен в БД")

    def save_task(self, task):
        self.tasks.append(task)
        self.logs.append(f"Задача {task.task_type} сохранена в БД")

    def get_all_products(self):
        return [p.info() for p in self.products]

    def get_logs(self):
        return self.logs


def main():
    db = Database()

    # Создаем начальные данные
    warehouse = Warehouse("Склад 1", "Ленина 10", 50)
    db.save_warehouse(warehouse)

    emp1 = Employee("Анна", "Кладовщик", None)
    emp2 = Employee("Олег", "Грузчик", None)
    db.save_employee(emp1)
    db.save_employee(emp2)

    prod1 = Product("Ноутбук", "На складе", 45000, "Техника")
    prod2 = Product("Мышка", "На складе", 1500, "Аксессуары")
    db.save_product(prod1)
    db.save_product(prod2)

    while True:
        print("\n" + "=" * 40)
        print("СКЛАДСКАЯ СИСТЕМА")
        print("=" * 40)
        print("1. Показать все товары")
        print("2. Показать сотрудников")
        print("3. Создать задачу")
        print("4. Выполнить задачу")
        print("5. Добавить товар на склад")
        print("6. Показать логи")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("\n--- ТОВАРЫ ---")
            for p in db.products:
                print(f"{p.name} | {p.status} | {p.price} руб.")

        elif choice == "2":
            print("\n--- СОТРУДНИКИ ---")
            for e in db.employees:
                print(f"{e.name} | {e.position} | Текущая задача: {e.current_task}")

        elif choice == "3":
            print("\n--- СОЗДАНИЕ ЗАДАЧИ ---")
            print("Тип: 1 - Приемка, 2 - Отгрузка")
            t = input("Выберите тип: ")
            task_type = "Приемка" if t == "1" else "Отгрузка"

            print("Сотрудники:")
            for i, e in enumerate(db.employees):
                print(f"{i + 1}. {e.name}")
            emp_idx = int(input("Выберите номер сотрудника: ")) - 1

            print("Товары:")
            for i, p in enumerate(db.products):
                print(f"{i + 1}. {p.name}")
            prod_idx = int(input("Выберите номер товара: ")) - 1

            task = Task(task_type, db.employees[emp_idx], "Создана", db.products[prod_idx])
            db.save_task(task)
            print("Задача создана!")

        elif choice == "4":
            print("\n--- ВЫПОЛНЕНИЕ ЗАДАЧ ---")
            for i, t in enumerate(db.tasks):
                print(f"{i + 1}. {t.task_type} | {t.product.name} | {t.status}")
            task_idx = int(input("Выберите номер задачи: ")) - 1

            task = db.tasks[task_idx]
            task.start_task()
            print("Задача начата...")
            input("Нажмите Enter для завершения")
            task.finish_task()
            print("Задача завершена!")

        elif choice == "5":
            print("\n--- ДОБАВЛЕНИЕ ТОВАРА ---")
            name = input("Название: ")
            price = int(input("Цена: "))
            cat = input("Категория: ")
            new_product = Product(name, "На складе", price, cat)
            db.save_product(new_product)
            warehouse.add_item(1)
            print("Товар добавлен!")

        elif choice == "6":
            print("\n--- ЛОГИ ---")
            for log in db.logs[-5:]:  # последние 5 логов
                print(log)

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный ввод!")


if __name__ == "__main__":
    main()