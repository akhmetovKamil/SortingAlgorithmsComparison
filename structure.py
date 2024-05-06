from dataclasses import dataclass
@dataclass
class Student:
    name: str
    average_score: float
    def __lt__(self, other: Student) -> bool:
        return self.average_score < other.average_score
    def __le__(self, other: Student) -> bool:
        return self.average_score <= other.average_score
