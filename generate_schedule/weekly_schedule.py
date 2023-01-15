from day import Day
from activities.activity import ActivityFactory

def parse_schedule(filepath):
    # Initialize an empty list to store the day objects
    days = []

    # Open the file for reading
    with open(filepath, 'r') as f:
        # Read the file line by line
        lines = f.readlines()
        # Initialize an empty list to store the activity objects for the current day
        current_day_activities = []
        # Initialize a variable to store the name of the current day
        current_day = None
        # Iterate over the lines in the file
        for line in lines:
            # Strip leading and trailing whitespace from the line
            line = line.strip()
            # Check if the line starts with an asterisk and a space
            if line.startswith('* **'):
                # If it does, this line defines the start of a new day
                # Extract the name of the day from the line
                day_name = line[4:-3]
                # If the current_day variable is not None, this means that we have
                # finished processing the activities for the previous day
                # So, we create a Day object for the previous day using the
                # current_day_activities list, and append it to the days list
                if current_day is not None:
                    days.append(Day(current_day, current_day_activities))
                # Update the current_day variable with the name of the new day
                current_day = day_name
                # Reset the current_day_activities list
                current_day_activities = []
            else:
                # If the line does not start with an asterisk and a space, it must
                # define an activity for the current day
                # Split the line by the ':' character to extract the activity name
                # and the time range
                activity_name, time_range = line.split(':', 1)
                # Strip leading and trailing whitespace from the activity name and
                # time range
                activity_name = activity_name.strip()
                time_range = time_range.strip()
                # Create an Activity object for the current activity and append it
                # to the current_day_activities list
                current_day_activities.append(ActivityFactory(activity_name).build(time_range))
        # After the loop has completed, we still need to create a Day object for
        # the last day in the file and append it to the days list
        days.append(Day(current_day, current_day_activities))

    # Return the list of day objects
    return days
