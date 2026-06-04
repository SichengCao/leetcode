import heapq
from collections import defaultdict


class RentalCarSystem:

    def __init__(self, cleaning_time=0):

        # heap:
        # (available_time, usage_count, car_id)
        self.heap = []

        self.next_car_id = 0

        self.cleaning_time = cleaning_time

        # rental_id -> car_id
        self.assignment = {}

        # car_id -> usage_count
        self.usage = defaultdict(int)

        # car_id -> rental list
        self.schedule = defaultdict(list)

    def assign_rentals(self, records):

        """
        records:
        [
            [rental_id, pickup_time, return_time]
        ]
        """

        # sort by pickup time
        records.sort(key=lambda x: x[1])

        for rental_id, pickup, ret in records:

            chosen_car = None

            reusable = []

            # -------------------------------------------------
            # Find ALL reusable cars
            # -------------------------------------------------

            while self.heap and self.heap[0][0] <= pickup:

                available_time, usage_count, car_id = heapq.heappop(self.heap)

                reusable.append(
                    (usage_count, available_time, car_id)
                )

            # -------------------------------------------------
            # FOLLOW UP:
            # prefer least-used car
            # -------------------------------------------------

            if reusable:

                reusable.sort()

                usage_count, available_time, car_id = reusable[0]

                chosen_car = car_id

                # push remaining reusable cars back
                for item in reusable[1:]:
                    heapq.heappush(
                        self.heap,
                        (item[1], item[0], item[2])
                    )

            # -------------------------------------------------
            # no reusable car
            # -------------------------------------------------

            else:

                chosen_car = self.next_car_id
                self.next_car_id += 1

            # -------------------------------------------------
            # assignment
            # -------------------------------------------------

            self.assignment[rental_id] = chosen_car

            # -------------------------------------------------
            # usage count
            # -------------------------------------------------

            self.usage[chosen_car] += 1

            # -------------------------------------------------
            # car schedule
            # -------------------------------------------------

            self.schedule[chosen_car].append(rental_id)

            # -------------------------------------------------
            # cleaning time follow-up
            # -------------------------------------------------

            next_available = ret + self.cleaning_time

            # -------------------------------------------------
            # push back into heap
            # -------------------------------------------------

            heapq.heappush(
                self.heap,
                (
                    next_available,
                    self.usage[chosen_car],
                    chosen_car
                )
            )

    def print_summary(self):

        print("=" * 50)
        print("TOTAL CARS:", self.next_car_id)
        print("=" * 50)

        print("\nRental Assignment")
        print("-" * 50)

        for rental_id in sorted(self.assignment):
            print(
                f"Rental {rental_id} -> Car {self.assignment[rental_id]}"
            )

        print("\nCar Usage")
        print("-" * 50)

        for car_id in sorted(self.usage):
            print(
                f"Car {car_id} used {self.usage[car_id]} times"
            )

        print("\nCar Schedule")
        print("-" * 50)

        for car_id in sorted(self.schedule):
            print(
                f"Car {car_id}: {self.schedule[car_id]}"
            )


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

records = [
    [101, 1, 4],
    [102, 2, 5],
    [103, 4, 6],
    [104, 5, 8],
    [105, 6, 9],
    [106, 7, 10]
]

# cleaning time = 1
system = RentalCarSystem(cleaning_time=1)

system.assign_rentals(records)

system.print_summary()