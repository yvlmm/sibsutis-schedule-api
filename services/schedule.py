import parser.pars
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Lesson:
    """Аналог одной строки в таблице БД 'Lessons'"""
    time_start: str
    time_end: str
    discipline: str
    lesson_type: str # лекции, практики, лабы
    teacher: str
    classroom: str # аудитория
    groups: List[str] # группы (удалить?????)

@dataclass
class Day:
    """Класс дня, содержащий список занятий"""
    day_name: str  # Понедельник, Вторник...
    lessons: List[Lesson] = field(default_factory=list)

@dataclass
class Week:
    """Класс учебной недели"""
    days: List[Day] = field(default_factory=list)