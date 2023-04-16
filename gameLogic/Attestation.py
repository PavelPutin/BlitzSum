from dataclasses import dataclass
from random import choice

from gameLogic.Subject import Subject
from gameLogic.Subjects import Subjects


@dataclass
class Attestation:
    MARKS = [i for i in range(10, 100, 10)]

    subject: Subject
    mark: int

    @staticmethod
    def create_random():
        return Attestation(
            Subjects.rand_subject().value,
            Attestation.rand_mark(),
        )

    @staticmethod
    def rand_mark():
        return choice(Attestation.MARKS)
