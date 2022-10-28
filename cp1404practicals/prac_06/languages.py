"""
Prac 06
Intermediate Exercises
Programming languages class exercise

Estimated time for completion: 25 mins
Current time: 12:11pm
Time when completed: 12:24pm
Time taken: 13 minutes
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]
# print(languages)
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)