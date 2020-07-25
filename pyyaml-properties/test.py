from model.yaml import Yaml
from model.environment import Environment

file = Yaml()
print(file.name())
print(file.load('version'))

file = Yaml(Environment.DEV)
print(file.load('version'))