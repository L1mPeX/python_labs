from dataclasses import dataclass
from datetime import date


@dataclass
class Student:
    fio: str
    birthdate: date
    group: str
    gpa: float

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        # ожидаем строки из CSV: birthdate в формате YYYY-MM-DD
        bd = date.fromisoformat(data["birthdate"])
        gpa = float(data["gpa"])
        return cls(
            fio=data["fio"],
            birthdate=bd,
            group=data["group"],
            gpa=gpa,
        )

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate.isoformat(),
            "group": self.group,
            "gpa": str(self.gpa),
        }
