from enum import Enum
from random import choice

from gameLogic.Assesses import Assesses
from gameLogic.Subject import Subject


class Subjects(Enum):
    PHILOSOPHY = Subject("philosophy", Assesses.EXAM, False)
    ENGLISH = Subject("english", Assesses.EXAM, False)
    MATEQ = Subject("mateq", Assesses.EXAM, False)
    LANGUAGES = Subject("languages", Assesses.EXAM, False)
    HMI = Subject("hmi", Assesses.CREDIT_WITH_MARK, False)
    CALCULATION_METHODS = Subject("calculation_methods", Assesses.CREDIT, False)
    TIPIS = Subject("tipis", Assesses.CREDIT, False)
    UNIX = Subject("unix", Assesses.CREDIT, False)
    ELECTRONICS = Subject("electronics", Assesses.CREDIT, False)
    PE = Subject("pe", Assesses.CREDIT, False)
    XALYBA = Subject("xalyba", Assesses.XALYBA, True)

    @staticmethod
    def rand_subject():
        return choice(list(Subjects))
