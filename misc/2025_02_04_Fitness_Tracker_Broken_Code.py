import datetime
import random


class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.activities = {}
        self.goals = {}

    def log_activity(self, activity, duration, calories):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        if date not in self.activities:
            self.activities[date] = []
        self.activities[date].append({'activity': activity, 'duration': duration, 'calories': calories})

    def set_goal(self, activity, target):
        self.goals[activity] = target

    def view_progress(self):
        for date, logs in self.activities.items():
            print(f"Date: {date}")
            for log in logs:
                print(
                    f"  Activity: {log['activity']}, Duration: {log['duration']} mins, Calories Burned: {log['calories']}")

    def check_goal_progress(self, activity):
        total_duration = sum(log['duration'] for log in self.activities.get(activity, []))
        goal = self.goals.get(activity, 0)

        if total_duration >= goal:
            print(f"Congratulations! You have reached your goal for {activity}.")
        else:
            print(f"You have {goal - total_duration} mins left to reach your {activity} goal.")


# Main Application
tracker = FitnessTracker("Alex")

# Logging activities
tracker.log_activity("Running", 30, 300)
tracker.log_activity("Cycling", 45, 400)
tracker.log_activity("Swimming", "60", 500)
tracker.log_activity("Boxing", 60, 500)

# Setting goals
tracker.set_goal("Running", 100)
tracker.set_goal("Cycling", '150')
tracker.set_goal("Swimming", None)
tracker.set_goal("Boxing", 150)

# Viewing progress
tracker.view_progress()

# Checking progress
tracker.check_goal_progress("Running")
tracker.check_goal_progress("Yoga")

tracker.set_goal("Cycling", 150)
tracker.activities[20240101] = []

# random.shuffle(tracker.activities)

tracker.log_activity("Weightlifting", 60, 90)

tracker.goals.pop('Cycling')

print(tracker.activities[datetime.datetime.now().strftime('%Y-%m-%d')])

tracker.check_goal_progress(30)

tracker.log_activity("Rowing", -20, 200)

tracker.goals["Boxing"] += 20

print(tracker.activities)

tracker.view_progress()

print(tracker.goals)

tracker = FitnessTracker('Alex')