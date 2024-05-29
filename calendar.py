while True:
    a = input("ENTER A NUMBER (or 'E' to exit): ")
    if a.lower() == 'e' :
        break
    aa = int(a)

    b = aa // 31536000  # 365.25 days (4 years)
    c = aa % 31536000
    d = c // 2629743  # average number of seconds in a month
    e = c % 2629743
    f = e // 86400  # 1 day
    g = e % 86400
    h = g // 3600  # 1 hour
    i = g % 3600
    j = i // 60  # 1 minute
    k = i % 60  # 60 seconds

    print(b, "years,", d, "months,", f, "days,", h, "hours,", j, "minutes,", k, "seconds")
