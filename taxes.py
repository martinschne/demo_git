from work import get_salary

TAX_FACTOR = 0.1

def get_salary_taxes(hour_pay, days_worked):
    return get_salary(hour_pay, days_worked) * TAX_FACTOR