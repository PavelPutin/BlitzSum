from gameLogic.Field import Field
from gameLogic.SelectEvent import SelectEvent
from gameLogic.Subject import Subject

"""
На поле 10х10 находятся аттестации по предметам. За каждую аттестацию начисляются баллы.
Игрок может выбирать аттестацию и снимать с неё выделение.
Если сумма баллов выбранных аттестаций равна 100, то клетки с аттестациями исчезают а игроку начисляются очки по определённой схеме.
На месте исчезнувших клеток появляются новые.
Если игрок не выбрал ни одной аттестации, он может выбрать любую. Если игрок выбрал аттестацию, то он может выбрать только клетки,
соседние с выбранными.
Игра ограничена таймером. По истечению T секунд игра заканчивается.

данные игры:
поле 10х10
аттестация
предмет
"""


class BlitzSum:
    DAYS_LEFT = 138 # дней в 4 семестре
    TARGET_MARK = 100

    def __init__(self):
        self.field = Field()
        self.score = 0
        self._current_tick = BlitzSum.DAYS_LEFT
        self._is_running = True

    def decrease_tick(self):
        if self._current_tick > 0:
            self._current_tick -= 1
        if self._current_tick <= 0:
            self.stop()

    @property
    def current_day(self):
        return self._current_tick

    def start(self):
        if self._current_tick > 0:
            self._is_running = True

    def stop(self):
        self._is_running = False

    @property
    def is_running(self):
        return self._is_running

    """
    правила:
    1) если баллы по аттестациям дают в сумме 100 
    И все предметы одинаковые 
    И этот предмет является джокером
    - счёт += 100 * joker_mult ** 2

    2) если баллы по аттестациям дают в сумме 100 
    И все предметы одинаковые
    И этот предмет не является джокером
    - счёт += 100 * subj_mult

    3) если баллы по аттестациям дают в сумме 100 
    И предметы разнородные
    И среди предметов есть джокер
    - счёт += max(subj_mult)

    4) если баллы по аттестациям дают в сумме 100 
    И предметы разнородные
    И среди предметов нет джокера
    - счёт += 100

    5) если баллы по аттестациям дают в сумме 100 
    И предметы разнородные
    И всего 2 типа
    И один из типов является джокером
    - счёт += 100 * subj_mult * joker_mult
    """

    def select(self, r, c):
        if not self._is_running:
            self.field.clear_selected()
            return False, SelectEvent.UNAVAILABLE_SELECT
        result = self.field.select(r, c)

        attestations = self.field.selected_attestations
        marks_sum = sum([a.mark for a in attestations])
        is_target_mark = marks_sum == self.TARGET_MARK
        att_subjects = set([a.subject for a in attestations])
        multipliers = [a.subject.assess.value for a in attestations]
        is_homogeneous_selection = len(att_subjects) == 1
        has_xalyba = any(att_subject.joker for att_subject in att_subjects)

        if not is_target_mark:
            if result:
                return result, SelectEvent.NORMAL_SELECTION
            return result, SelectEvent.UNSELECTION

        event = SelectEvent.DAMMY
        if is_homogeneous_selection and has_xalyba:
            self.score += marks_sum * len(attestations) * Subject.JOKER_MULTIPLIER ** 2
            event = SelectEvent.XALYBA
        if is_homogeneous_selection and not has_xalyba:
            subj_multiplier = multipliers[0]
            event = SelectEvent.create_by_assessment(subj_multiplier)
            self.score += marks_sum * len(attestations) * subj_multiplier
        if not is_homogeneous_selection and has_xalyba:
            subj_multiplier = max(multipliers)
            event = SelectEvent.create_by_assessment(subj_multiplier)
            self.score += marks_sum * len(attestations) * subj_multiplier
        if not is_homogeneous_selection and not has_xalyba:
            self.score += marks_sum * len(attestations)
            event = SelectEvent.GETEROGENEOUS
        if not is_homogeneous_selection and len(att_subjects) == 2 and has_xalyba:
            subj_multiplier = max(multipliers)
            event = SelectEvent.create_by_assessment(subj_multiplier)
            self.score += marks_sum * len(attestations) * subj_multiplier * Subject.JOKER_MULTIPLIER

        self.field.clear_selected()
        return result, event

    def unselect(self, r, c):
        return self.field.unselect(r, c)