class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Distance is {self.distance}, rate per kilometer is {self.rate_per_km} and fare is {self.fare}")


def main():
    # your program
    taxi1 = TaxiRide(5)
    fare1 = taxi1.calculate_fare(100)

    taxi2 = TaxiRide(10)
    fare2 = taxi2.calculate_fare(200)

    TaxiRide.print_receipt(taxi1)
    TaxiRide.print_receipt(taxi2) 

if __name__ == "__main__":
    main()
