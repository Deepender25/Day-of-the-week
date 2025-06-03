# 🗓️ Day of the Week Calculator - Odd Days Method

This repository contains a Python solution to calculate the **day of the week** for any given date using the classic **Odd Days** method.

## 🔗 Problem Link

Inspired by [LeetCode 1185. Day of the Week](https://leetcode.com/problems/day-of-the-week/)

## 💡 Problem Statement

> Given a date represented by `year`, `month`, and `day`, return the **name of the day of the week** for that date.

## 🧠 Approach

This method calculates the total **odd days** contributed by:
- All the years before the given year,
- The months passed in the current year,
- The days passed in the current month.

It uses:
- The count of leap years for accuracy,
- Hardcoded odd days per month depending on whether it’s a leap year or not.

By summing all odd days modulo 7, it determines the correct weekday without using Python’s built-in `datetime` module.

## ✅ Python Code

```python
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

