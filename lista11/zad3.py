# data yoinked from
# https://pe2019.pkw.gov.pl/pe2019/pl/dane_w_arkuszach
# > wykaz_list.csv.zip
# Since this is data science (I think) "pandas" would be use
# quite useful but I don't know it, so vanilla python it is
import csv
from itertools import groupby
from operator import itemgetter
import operator


def dhondt_method(entries: list[int], num_of_seats: int) -> list[int]:
    seats = [0] * len(entries)
    for _ in range(num_of_seats):
        pos, maxval = max(enumerate(entries), key=itemgetter(1))
        entries[pos] = round(maxval / 2)
        seats[pos] += 1

    return seats


with open("data/wykaz_list.csv", "r") as f:
    csv_reader = csv.DictReader(f, delimiter=";")
    data = list(csv_reader)


# smart thing would be to parse the data and store them as proper types
# ie ints as ints, etc... , but for our task, it's not necessary

# oh and and in these elections representatives don't matter as much,
# they are chosen by the party itself, which is voted on, contrary to
# the instruction in the task given
assert data

# grouping comitees by their counties
data.sort(key=itemgetter("Numer okręgu"))
grouped_by_comitees_iter = groupby(data, key=itemgetter("Numer okręgu"))
# after we've grouped by comitees, we can
# filter out electoral threshold (which is 5% or more)
# reading about how law works is painful
# https://en.wikipedia.org/wiki/Electoral_threshold
# thoretically the threshold is 8% for comitees, but that's
# relevant to our task I think

# there is a column which tells me whether a comitee is eligible
# I'll use this one instead of the 5% threshold, and leave that logic
# commented out here:
# def parse_and_calc_percent(line) -> float:
# is_over_5_percent = lambda x: parse_and_calc_percent(x) >= 5.0
# grouped_by_comitees = [list(filter(is_over_5_percent, group))
#                        for _, group in grouped_by_comitees_iter]


grouped_by_comitees = [list(group) for _key, group in grouped_by_comitees_iter]
is_eligible = lambda entry: entry["Udział w podziale mandatów"] == "Tak"
grouped_by_comitees_filtered = [list(filter(is_eligible, gr)) for gr in grouped_by_comitees]

# basic testing here:
wrongly_distributed_seats_counter = 0

for group in grouped_by_comitees_filtered:
    if len(group) == 0:
        # empty group lol
        continue

    # parse vote counts for our method
    votes = list(map(int, map(itemgetter("Liczba głosów"), group)))
    # run our d'hondt method to distribute seats
    # actually I have absolutely no clue where can I find info
    # about how many seats each county gets, so I'll cheat a little
    # and sum up the number of seat which were officialy distributed

    # we can get the actual seat dist from out data:
    real_seat_dist = list(map(int, map(itemgetter("Liczba mandatów"), group)))
    real_num_of_seats = sum(real_seat_dist)

    seat_distribution = dhondt_method(votes, real_num_of_seats)

    sum_of_differences = sum(map(abs, map(operator.sub, seat_distribution, real_seat_dist)))
    # real world is different from our formulas, I think
    # it's still impressive that I've got most of them correct
    if sum_of_differences > 0:
        group_name = group[0]["Siedziba OKW"]
        group_num = group[0]["Numer okręgu"]
        print(f"Made mistake in calculating seats in {group_name}, group nr: {group_num}")
        print(seat_distribution)
        print(real_seat_dist)
        print(votes)
        wrongly_distributed_seats_counter += sum_of_differences
