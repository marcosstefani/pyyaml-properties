class File(object):
    def __init__(self, environment):
        self.environment = environment.name.lower()

    def name(self):
        return "application-{}.yaml".format(self.environment)
