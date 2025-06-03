def get_day_of_week(year, month, day):
    leap_years = (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    normal_years = (year - 1) - leap_years

    odd_days_from_years = (normal_years * 1 + leap_years * 2) % 7

    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    month_odd_days = {
        1: 3, 2: 0 if not is_leap else 1, 3: 3, 4: 2, 5: 3, 6: 2,
        7: 3, 8: 3, 9: 2, 10: 3, 11: 2, 12: 3
    }
    odd_days_from_months = sum(month_odd_days[m] for m in range(1, month)) % 7

    odd_days_from_days = day % 7

    total_odd_days = (odd_days_from_years + odd_days_from_months + odd_days_from_days) % 7

    weekday_lookup = {
        0: "Sunday", 1: "Monday", 2: "Tuesday",
        3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"
    }

    return weekday_lookup[total_odd_days]
