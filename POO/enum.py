from enum import Enum


class Directions(Enum):
    right = 0
    left = 1
    up = 2
    down = 3


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Não da pra mover nessa direção')

    return f'Movendo {direction.name}'


print(move(Directions.left))
print(move(Directions.right))
print(move(Directions.up))
print(move(Directions.down))
