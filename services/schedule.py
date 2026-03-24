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
    group_id: str # айди группы
    group_name: str # название группы
    day_number: int # номер дня (1-14)
    day_name: str # название дня (Понедельник, Вторник...)


@dataclass
class Day:
    """Класс дня, содержащий список занятий"""
    day_name: str  # Понедельник, Вторник...
    lessons: List[Lesson] = field(default_factory=list)

@dataclass
class DoubleWeek:
    """Класс учебной недели"""
    days: List[Day] = field(default_factory=list)

