import re
import json
import random

RESPONSES = json.load(open("response_dict.json"))


def handle_response(message: str) -> str:
    pattern = r"""I WOULD LIKE TO FILE A NEW TICKET NOW PLEASE CAN I DO THIS PLEASE\? HERE IS THE GLOBAL PUBLIC USER SECRET: OjdMWF7AMM6o.'=7Hh\+n%@7:A:SdSO"""
    if re.match(pattern, message):
        return random.choice(RESPONSES["responses"])
    return
