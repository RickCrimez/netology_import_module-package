from app.salary import *
from app.db.people import *
from datetime import datetime

if __name__ == '__main__':
    print("Текущая дата (dirty_main):", datetime.now().date())
    calculate_salary()
    get_employees()