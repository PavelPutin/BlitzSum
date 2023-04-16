from dataclasses import dataclass

from gameLogic.Assesses import Assesses


@dataclass(frozen=True)
class SelectEvent:
    EXAM = "exam"
    CREDIT_WITH_MARK = "credit with mark"
    CREDIT = "credit"
    XALYBA = "xalyba"
    UNAVAILABLE_SELECT = "unavailable select"
    NORMAL_SELECTION = "normal selection"
    UNSELECTION = "unselection"
    GETEROGENEOUS = "heterogeneous"
    DAMMY = "dammy"

    name: str

    @staticmethod
    def create_by_assessment(assessment: float):
        match assessment:
            case Assesses.EXAM.value:
                return SelectEvent.EXAM
            case Assesses.CREDIT_WITH_MARK.value:
                return SelectEvent.CREDIT_WITH_MARK
            case Assesses.CREDIT.value:
                return SelectEvent.CREDIT
            case Assesses.XALYBA.value:
                return SelectEvent.XALYBA
            case _:
                return SelectEvent.DAMMY
