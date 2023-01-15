from abc import ABC, abstractmethod

# Abstract base class for activities
class Activity(ABC):
    def __init__(self, start_time: str, end_time: str):
        self.start_time = start_time
        self.end_time = end_time

    @abstractmethod
    def __str__(self):
        pass

# Concrete activity class for wake up
class WakeUp(Activity):
    def __init__(self, start_time: str, end_time: str = ''):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time}: Wake up"

    @staticmethod
    def  build(start_time, end_time):
        return WakeUp(start_time, end_time)

# Concrete activity class for morning routine
class MorningRoutine(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Morning routine (shower, getting dressed, breakfast)"

    @staticmethod
    def  build(start_time, end_time):
        return MorningRoutine(start_time, end_time)

# Concrete activity class for Ultimate Frisbee
class UltimateFrisbee(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Ultimate Frisbee/Shower @ Gym"

    @staticmethod
    def  build(start_time, end_time):
        return UltimateFrisbee(start_time, end_time)

# Concrete activity class for work
class Work(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Work"

    @staticmethod
    def  build(start_time, end_time):
        return Work(start_time, end_time)

# Concrete activity class for lunch break
class LunchBreak(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Lunch Break"

    @staticmethod
    def  build(start_time, end_time):
        return LunchBreak(start_time, end_time)

# Concrete activity class for focus blocks
class Focus(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Focus"

    @staticmethod
    def  build(start_time, end_time):
        return Focus(start_time, end_time)

# Concrete activity class for breaks
class WorkBreak(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Focus"

    @staticmethod
    def  build(start_time, end_time):
        return WorkBreak(start_time, end_time)

# Concrete activity class for dinner
class Dinner(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Dinner"

    @staticmethod
    def  build(start_time, end_time):
        return Dinner(start_time, end_time)

# Concrete activity class for walks
class Walk(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Walk"

    @staticmethod
    def  build(start_time, end_time):
        return Walk(start_time, end_time)

# Concrete activity class for personal projects
class PersonalProjects(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Personal projects"

    @staticmethod
    def  build(start_time, end_time):
        return PersonalProjects(start_time, end_time)

# Concrete activity class for audio books
class AudioBooks(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Audio Books"

    @staticmethod
    def  build(start_time, end_time):
        return AudioBooks(start_time, end_time)

# Concrete activity class for cigar
class Cigar(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Cigar"

    @staticmethod
    def  build(start_time, end_time):
        return Cigar(start_time, end_time)

# Concrete activity class for relax time
class RelaxTime(Activity):
    def __init__(self, start_time: str, end_time: str):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}: Relax Time"

    @staticmethod
    def  build(start_time, end_time):
        return RelaxTime(start_time, end_time)

# Concrete activity class for bedtime
class BedTime(Activity):
    def __init__(self, start_time: str, end_time: str = ''):
        super().__init__(start_time, end_time)

    def __str__(self):
        return f"{self.start_time}: Bedtime"

    @staticmethod
    def  build(start_time, end_time):
        return BedTime(start_time, end_time)


# Object of all activities
activities = {
    "wake_up": WakeUp,
    "morning_routine": MorningRoutine,
    "ultimate_frisbee": UltimateFrisbee,
    "work": Work,
    "lunch_break": LunchBreak,
    "focus": Focus,
    "work_break": WorkBreak,
    "dinner": Dinner,
    "walk": Walk,
    "personal_projects": PersonalProjects,
    "audio_books": AudioBooks,
    "cigar": Cigar,
    "relax_time": RelaxTime,
    "bed_time": BedTime,
}