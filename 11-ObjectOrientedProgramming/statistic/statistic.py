class Statistic():
    def __init__(self):
        self.numbers = []
    
    def add_num(self):
        while True:

            value = input("Podaj liczbę lub napisz \"quit\" żeby zakończyć: ")
            if value == "quit":
                break

            try:
                self.numbers.append(int(value))
            except ValueError:
                print("Podaj poprawną liczbę")
    
    def display_num(self):
        print("Zestaw liczb: "," ".join(map (str, self.numbers)))

    def greatest_num(self):
        self.greatest = max(self.numbers)
    
    def smallest_num(self):
        self.smallest = min(self.numbers)
    
    def arithmetic_mean(self):
        self.arithmetic = sum(self.numbers)/len(self.numbers)

    def median(self):
        sort_num = sorted(self.numbers)

        liczba_el = len(sort_num)

        if liczba_el % 2 != 0:
            self.med = sort_num[liczba_el//2]
        else:
            index1 = liczba_el // 2
            index2 = index1 - 1
            self.med = (sort_num[index1] + sort_num[index2])/2  

    def outsource(self):
        print(f"Max value: {self.greatest}")      
        print(f"Min value: {self.smallest}")      
        print(f"Arithmetic mean: {self.arithmetic}")      
        print(f"Median: {self.med}")      
            
