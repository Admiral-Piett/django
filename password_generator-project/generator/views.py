import random
import uuid
from copy import deepcopy

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

PWD_LENGTHS = [8, 9, 10, 11, 12, 13, 14, 15, 16]
CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CHARACTERS = deepcopy(CHARACTERS).upper()
NUMBERS = "12345678910"
SPECIAL = "!@#$%&*"


def index(request):
    return render(request, "generator/index.html", {"pwd_lengths": PWD_LENGTHS})


def password(request):
    length = int(request.GET.get("length"))

    uppercase = request.GET.get("uppercase")
    numbers = request.GET.get("numbers")
    special = request.GET.get("special")

    character_set = [CHARACTERS]
    if uppercase:
        character_set.append(UPPER_CHARACTERS)
    if numbers:
        character_set.append(NUMBERS)
    if special:
        character_set.append(SPECIAL)

    password = ""
    for i in range(length):
        characters = random.choice(character_set)
        password += random.choice(characters)

    return render(request, "generator/password.html", {"password": password})
