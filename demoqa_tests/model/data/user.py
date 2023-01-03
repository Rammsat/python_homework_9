from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    birthday_year: str
    birthday_month: str
    birthday_day: int
    subject: str
    hobby: str
    image: str
    address: str
    state: str
    city: str
