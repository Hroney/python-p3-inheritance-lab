#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first, last, knowledge = []):
        super().__init__(first, last)
        self.knowledge = knowledge
    
    def learn(self, subject):
        self.knowledge.append(subject)
        pass