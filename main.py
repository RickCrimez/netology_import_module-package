from app.salary import calculate_salary
from app.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print("Текущая дата:", datetime.now().date())
    calculate_salary()
    get_employees()