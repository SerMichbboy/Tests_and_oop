"""" В задаче нужно написать класс лифт, который по нажатию нопки вверх поедет на этаж выше,
по нажатию вниз - поедет на 1 этаж ниже.
Если лифт стоит на минимальном этаже, то ниже уехать он не сможет.
Если лифт занимает верхний этаж, он сообщит нам о том, что выше уже некуда.
"""


class Elevator:
    def __init__(self, floors=5, current_floor=3):
        self.floors = floors
        self.current_floor = current_floor

    def up(self):
        if self.current_floor < self.floors:
            self.current_floor += 1
            print(f'Лифт поднимется на {self.current_floor + 1} этаж')
        else:
            print(f'Лифт не может подняться выше')

    def down(self):
        if self.current_floor > 2:
            self.current_floor -= 1
            print(f'Лифт опускается на {self.current_floor - 1} этаж')
        else:
            print(f'Лифт не может опуститься ниже')


""" Помимо основной задачи я написал тесты к данному коду..."""
