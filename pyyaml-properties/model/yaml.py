import yaml, os

class Yaml(object):
    def __init__(self, environment=None):
        self.environment = environment
        if environment:
            self.environment = environment.name.lower()

    def name(self):
        if self.environment:
            return "application-{}.yaml".format(self.environment)
        return 'application.yaml'

    def absoluteName(self):
        location = os.path.dirname(os.path.abspath(self.name()))
        return os.path.join(location, 'properties/{}'.format(self.name()))

    def load(self, prop):
        items = [prop]
        if '.' in prop:
            items = prop.split('.')
        return self.find(items)

    def find(self, items):
        with open(self.absoluteName()) as f:
            docs = yaml.load_all(f, Loader=yaml.FullLoader)
            for doc in docs:
                for k, v in doc.items():
                    if k != items[0]:
                        continue
                    for i in items[1:]:
                        if isinstance(v, dict):
                            v = v[i]
                    return v
