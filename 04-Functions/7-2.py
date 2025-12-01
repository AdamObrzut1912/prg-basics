def months(month):
    arr_month = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    month_string = arr_month[month]
    return month_string

def main():
    month_input = int(input("Enter the month number: "))
    print(f"For name of {month_input} is {months(month_input)}")
    return

if __name__ == "__main__":
        main()
