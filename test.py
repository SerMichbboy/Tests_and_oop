from main import Elevator


def test_elevator_up():
    elevator = Elevator(3, 2)
    elevator.up()
    assert elevator.current_floor == 3


def test_elevator_up_max_floor_reached():
    elevator = Elevator(3, 3)
    elevator.up()
    assert elevator.current_floor == 3


def test_elevator_down():
    elevator = Elevator(3, 3)
    elevator.down()
    assert elevator.current_floor == 2


def test_elevator_down_first_floor_reached():
    elevator = Elevator(3, 1)
    elevator.down()
    assert elevator.current_floor == 1


def test_elevator_default_floors_and_current_floor():
    elevator = Elevator()
    assert elevator.floors == 5
    assert elevator.current_floor == 3
