from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    # 1. Створюємо екземпляри клієнтів та продаємо їм їжу через статичний метод бару
    customer_instances = []
    for person_data in customers:
        customer = Customer(person_data["name"], person_data["food"])
        CinemaBar.sell_product(customer.food, customer)
        customer_instances.append(customer)

    # 2. Створюємо персонал (прибиральника) та зал
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)

    # 3. Запускаємо кіносеанс (він сам запустить перегляд та прибирання)
    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
