from enum import Enum

class Environment(Enum):
    LOCAL = 'local'
    DEV = 'development'
    STG = 'staging'
    PROD = 'production'
