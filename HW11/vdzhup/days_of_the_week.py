def get_day(days: dict) -> str:
    user_day = input("Enter your number of day: ")
    try:
        return days[int(user_day)]
    except KeyError:
        return "Error: There are only 7 days in a week."
    except ValueError:
        return "Error: Use only integer number"


days_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}
print(get_day(days_week))
