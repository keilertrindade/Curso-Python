"""Documentação deste módulo

Typing - https://docs.python.org/3/library/typing.html
"""
from typing import Union  #Import necessário para configurarmos mais de um return nas funções

x: int = 10
y: float = 10.5
z: bool = False


def funcao(p1: float, p2: str, p3: dict)  -> float:
    return 10.12


def funcao_dois() -> Union[list, dict]:
    return []
