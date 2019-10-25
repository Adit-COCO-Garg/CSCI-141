from dataclasses import dataclass


@dataclass(frozen=True)
class Birthday:
    month: str
    day: int
    year: int


def build_dictionary(filename):
    bd_counts = dict()
    with open(filename) as file:
        for line in file:
            birthday_fields = line.strip().split()
            month = birthday_fields[0]
            day = int(birthday_fields[1])
            year = int(birthday_fields[2])
            if Birthday(month, day, year) in bd_counts:
                bd_counts[Birthday(month, day, year)] += 1
            else:
                bd_counts[Birthday(month, day, year)] = 1
    return bd_counts


def birthdays_atleast(bd_counts, min_count):
    return [birthday for birthday, count in bd_counts.items() if count >=
            min_count]


def to_strings(lst):
    months = dict(JAN="1", FEB="2", MAR="3", APR="4", MAY="5", JUN="6", JUL="7",
                  AUG="8", SEP="9", OCT="10", NOV="11", DEC="12")
    # return ['{months[birthday.month]}/{birthday.day}/birthday.year' for
    #  birthday in lst] # this might be hard to read?
    str_lst = []
    for birthday in lst:

        a = birthday.month
        string_bday = [months[a] + "/" + str(birthday.day) + "/" +
                       str(birthday.year)]  # .append is faster then +=
        str_lst += string_bday
    return str_lst


def main():
    bd_counts = build_dictionary("birthday20000.txt")
    min_count = int(input("Enter a minimum count: "))
    list_birthdays = birthdays_atleast(bd_counts, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    list_strings = to_strings(list_birthdays)
    print(list_strings)


if __name__ == '__main__':
    main()
