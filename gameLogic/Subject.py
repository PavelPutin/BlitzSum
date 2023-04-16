from dataclasses import dataclass

from gameLogic.Assesses import Assesses


@dataclass(frozen=True)
class Subject:
    JOKER_MULTIPLIER = 10.0

    title: str
    assess: Assesses
    joker: bool
