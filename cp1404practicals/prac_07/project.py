import datetime


class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __repr__(self):
        """Return string representation of Project"""
        return f"{self.name} start: {self.startdate.strftime('%d/%m/%y')}  {self.priority}"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        """Determine if Project is complete."""
        return self.percent_complete == 100
