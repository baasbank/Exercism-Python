from string import ascii_uppercase as upper
import random


class Robot(object):

    def __init__(self, name=None):
        self.name = ''.join(random.choices(upper, k=2)) + str(random.randint(100, 999))
        if self.name == name:
            self.reset()

    def reset(self):
        self.__init__(self.name)





