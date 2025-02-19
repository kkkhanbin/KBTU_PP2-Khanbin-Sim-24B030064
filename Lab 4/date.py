import datetime as dt


def main():
    cur = dt.datetime.now()

    # substract 5 days from today
    print((cur - dt.timedelta(5)).strftime("%d/%m/%Y - %A"))

    # yesterday, today, tomorrow
    days = [cur - dt.timedelta(1), cur, cur + dt.timedelta(1)]
    print("; ".join([day.strftime("%d/%m/%Y - %A") for day in days]))

    # microseconds - do I have to delete microseconds or in opposite, show them?
    print(cur.microsecond)
    print(cur.strftime("%H:%M:%S"))

    # date difference
    date1, date2 = cur, dt.datetime(2025, 2, 19, 16, 40, 33)
    print(f"Difference in seconds = {abs((date1 - date2).seconds)}")


if __name__ == "__main__":
    main()
