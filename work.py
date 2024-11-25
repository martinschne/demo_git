HOURS_NORMAL_DAY = 8
HOURS_LONG_DAY = 10


def get_salary(hour_pay, days):
    """
    Calculates salary based on hour pay and days worked.
    Please use appropriate constant defined above.
    """
    return days * HOURS_NORMAL_DAY * hour_pay