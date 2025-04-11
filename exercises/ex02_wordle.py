"""Wordle game constructed through loop"""

__author__: str = "730667645"


def contains_char(secret: str, index: str) -> bool:
    """To see if the given character is in the string or not"""
    assert len(index) == 1, f"len('{index}') is not 1"
    i: int = 0
    while i < len(secret):
        if secret[i] == index:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Return a string of emojis that visually represent the accuracy of a guess."""
    assert len(guess) == len(secret), "The guess must be the same length as the secret."
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            result = result + GREEN_BOX
        elif contains_char(secret=secret, index=guess[i]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        i = i + 1

    return result


def input_guess(length: int) -> str:
    """Keep prompting the user until a valid guess of the expected length is given."""
    guess = input(f"Enter a {length} character word: ")

    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    MAX_TURN: int = 6
    TURN: int = 1
    while TURN <= MAX_TURN:
        print(f"===Turn {TURN}/6===")
        guess = input_guess(len(secret))
        feedback = emojified(guess=guess, secret=secret)
        print(feedback)
        if guess == secret:
            return print(f"You won in {TURN}/6 turns!")
        else:
            TURN = TURN + 1
    if TURN > MAX_TURN:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
