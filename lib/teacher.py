#!/usr/bin/env python

from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]


class Teacher(User):

    def __init__(self, first, last, knowledge = knowledge):
        super().__init__(first, last)
        self.knowledge = knowledge


    def teach(self):
        return knowledge[random.randint(1,len(knowledge))]