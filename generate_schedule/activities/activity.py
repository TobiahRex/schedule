from activities import *

# Abstarct Factory that maps activity types to their respective classes
class ActivityFactory:
    def __init__(self):
        self.activity_map = {
            'Work': Work,
            'LunchBreak': LunchBreak,
            'Focus': Focus,
            'WorkBreak': WorkBreak,
            'Dinner': Dinner,
            'WakeUp': WakeUp,
            'MorningRoutine': MorningRoutine,
            'UltimateFrisbee': UltimateFrisbee,
        }

    # Map activity type to class
    def get_activity(self, activity_type):
        return self.activity_map.get(activity_type)