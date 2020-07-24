from enum import Enum

class Environment(Enum):
    LOCAL = 'local'
    DEV = 'development'
    STG = 'staging'
    TEST = 'testing'
    PROD = 'production'
