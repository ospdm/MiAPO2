#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Простая валидация e-mail адреса с помощью регулярного выражения.
"""

import re

_EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

def validate_email(email: str) -> bool:
    """Возвращает True, если email соответствует шаблону."""
    return bool(_EMAIL_REGEX.match(email))

if __name__ == "__main__":
    email = input("Введите email: ")
    if validate_email(email):
        print("Email корректен.")
    else:
        print("Email некорректен.")
