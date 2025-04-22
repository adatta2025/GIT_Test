from datetime import datetime
curr_date = datetime.today()
print("\n====================================")
print("\nCurrent date and time\t:", curr_date)
print("\nCurrent year in full\t:", curr_date.strftime("%Y"))
print("\nMonth of year full name\t:", curr_date.strftime("%B"))
print("\nWeekday of the week\t:", curr_date.strftime("%w"))
print("\nDay of the month\t:", curr_date.strftime("%d"))
print("\nDay of week in full name:", curr_date.strftime("%A"), '\n')
