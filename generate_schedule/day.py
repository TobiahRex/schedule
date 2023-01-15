from activities import *
from abstracts import AbstarctDay

class Day(AbstarctDay):
    def __str__(self):
        # Implement the __str__ method here
        pass

    def __init__(self, day: str):
        super().__init__()
        self.day = day
        self.schedule = [
            {
                'activity': WakeUp,
                'start_time': "5:00am",
                'end_time': ''
            },
            {
                'activity': MorningRoutine,
                'start_time': "5:15am",
                'end_time': "6:15am"
            },
            {
                'activity': UltimateFrisbee,
                'start_time': "7:00am",
                'end_time': "9:00am"
            },
            {
                'activity': Work,
                'start_time': "9:30am",
                'end_time': "12:00pm"
            },
            {
                'activity': LunchBreak,
                'start_time': "12:00pm",
                'end_time': "12:45pm"
            },
            {
                'activity': Focus,
                'start_time': "12:45pm",
                'end_time': "1:30pm"
            },
            {
                'activity': WorkBreak,
                'start_time': "1:30pm",
                'end_time': "1:40pm"
            },
            {
                'activity': Focus,
                'start_time': "1:40pm",
                'end_time': "2:25pm"
            },
            {
                'activity': WorkBreak,
                'start_time': "2:25pm",
                'end_time': "2:35pm"
            },
            {
                'activity': Focus,
                'start_time': "2:35pm",
                'end_time': "3:20pm"
            },
            {
                'activity': WorkBreak,
                'start_time': "3:20pm",
                'end_time': "3:30pm"
            },
            {
                'activity': Focus,
                'start_time': "3:30pm",
                'end_time': "4:15pm"
            },
            {
                'activity': WorkBreak,
                'start_time': "4:15pm",
                'end_time': "4:25pm"
            },
            {
                'activity': Focus,
                'start_time': "4:25pm",
                'end_time': "5:00pm"
            },
            {
                'activity': Dinner,
                'start_time': "5:10pm",
                'end_time': "5:40pm"
            },
            {
                'activity': Focus,
                'start_time': "5:40pm",
                'end_time': "6:20pm"
            },
            {
                'activity': WorkBreak,
                'start_time': "6:20pm",
                'end_time': "6:30pm"
            },
            {
                'activity': Focus,
                'start_time': "6:30pm",
                'end_time': "7:15pm"
            },
            {
                'activity': BedTime,
                'start_time': "10:00pm",
                'end_time': ""
            },
        ]

    def generate(self):
        generated_schedule = []
        for block in self.schedule:
            activity = block.get('activity').build(block.get('start_time'), block.get('end_time'))
            generated_schedule.append(activity)
        [print(s) for s in generated_schedule]

if __name__ == '__main__':
    monday = Monday()
    monday.generate()