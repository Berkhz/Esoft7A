from dataclasses import dataclass
from services.euclidean_distance import euclidean_distance
from typing import Tuple


@dataclass
class Student:
    name: str
    age: int
    grade_avg: float
    absences: float
    
    def calculate_euclidean_distance(self, centroid: Tuple[int, float, float]):
        return euclidean_distance(centroid, (self.age, self.grade_avg, self.absences))
    
    def __str__(self):
        return f"{self.name} {self.age} {self.grade_avg} {self.absences}"
