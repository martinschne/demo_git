from adding import add
from subtracting import subtract
from greeting import greet
from barking import bark
from celebration import celebrate
from reversion import revert_text


def main():
    # adding feature
    # output should be 5
    print(add(2, 3))

    # subtracting feature
    # output should be 5
    print(subtract(10, 5))

    # greeting.py feature
    # output should be 'Hello Martin'
    print(greet("Martin"))

    # barking feature
    # output should be 'I am a bad dog'
    print(bark())

    # celebrating feature
    # output should be 'Yupi'
    print(celebrate("Yupi"))

    # string reverting feature
    # output should be 'olleh'
    print(revert_text("hello"))


if __name__ == "__main__":
    main()