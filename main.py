from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import pytz

def time_view():
    current_time = datetime.datetime.now().time()
    return current_time

def moscow_time():
    dt_moscow = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    return dt_moscow