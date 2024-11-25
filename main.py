from adding import add
from subtracting import subtract
from multiplying import multiply
from division import divide
from greeting import greet
from barking import bark
from celebration import celebrate
from reversion import revert_text
from lengthy import get_len
from age import is_adult
from work import get_salary
from taxes import get_salary_taxes


def main():
    # adding feature
    # output should be 5
    print(add(2, 3))

    # subtracting feature
    # output should be 5
    print(subtract(10, 5))

    # multiplying feature
    # output should be 50
    print(multiply(10, 5))

    # division feature
    # output should be 2
    print(divide(10, 5))

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

    # length of the string
    # output should be 2
    print(get_len("hi"))

    # age verifier
    # output should be False
    print(is_adult(15))

    # get salary of worker working for 15 EUR/hour
    # for 31 days
    # expected salary = (depends on how many hours you work per day)
    # we will do two implementations of 'get_salary'
    # for demonstration purposes
    hour_pay = 15
    days_worked = 31

    print("Bill earned: ", end="")
    print(get_salary(hour_pay, days_worked))

    print("Taxes from Bill's salary: ", end="")
    print(get_salary_taxes(hour_pay, days_worked))


if __name__ == "__main__":
    main()