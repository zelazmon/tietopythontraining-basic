# Function print age average for adults and child number
from create_lists import list_elements


def check_avg_age(ages):
    adults = [ages[x] for x in range(len(ages)) if ages[x] >= 18]
    if len(adults) > 0:
        average_adults = sum(adults) / len(adults)
    else:
        average_adults = "Missing adults."
    print("Average of adults: ", average_adults)
    child = [ages[x] for x in range(len(ages)) if ages[x] < 18]
    count_child = len(child)
    print("Number of child: ", count_child)


print("Put data for list: number of people, and age for these people.")
check_avg_age(list_elements())
