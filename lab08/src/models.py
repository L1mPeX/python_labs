from dataclasses import dataclass, field
from datetime import datetime, date
from typing import ClassVar


@dataclass
class Student:
    """
    Класс модели студента с валидацией, методами сериализации и вспомогательными функциями.
    
    Поля:
    - fio: ФИО студента (str)
    - birthdate: дата рождения в формате YYYY-MM-DD (str)
    - group: группа, например 'SE-01' (str)
    - gpa: средний балл от 0 до 5 (float)
    """

    fio: str
    birthdate: str
    group: str
    gpa: float
    
    DATE_FORMAT: ClassVar[str] = "%Y-%m-%d"

    def __post_init__(self):
        """Валидация формата даты и диапазона среднего балла при создании объекта."""
        try:
            datetime.strptime(self.birthdate, self.DATE_FORMAT)
        except ValueError:
            raise ValueError(f"birthdate format must be {self.DATE_FORMAT}")
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        """Возвращает количество полных лет студента на текущую дату."""
        b_date = datetime.strptime(self.birthdate, self.DATE_FORMAT).date()
        today = date.today()
        return today.year - b_date.year - ((today.month, today.day) < (b_date.month, b_date.day))

    def to_dict(self) -> dict:
        """Сериализация объекта Student в словарь."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        """Создание объекта Student из словаря с валидацией."""
        required_keys = {"fio", "birthdate", "group", "gpa"}
        if not required_keys.issubset(data):
            missing = required_keys - data.keys()
            raise KeyError(f"Missing keys for Student: {missing}")
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"]),
        )

    def __str__(self):
        """Красивое строковое представление объекта."""
        return (f"Student(fio='{self.fio}', group='{self.group}', "
                f"birthdate='{self.birthdate}', gpa={self.gpa:.2f}, age={self.age()})")
