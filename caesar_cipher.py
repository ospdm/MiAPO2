#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Шифр Цезаря: сдвиг букв в строке на заданное количество позиций.
"""

def caesar_cipher(text: str, shift: int) -> str:
    """Возвращает результат шифрования text сдвигом shift."""
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    text = input("Введите текст: ")
    try:
        shift = int(input("Введите шаг сдвига (целое число): "))
        print("Результат шифрования:", caesar_cipher(text, shift))
    except ValueError:
        print("Ошибка: шаг должен быть целым числом.")
