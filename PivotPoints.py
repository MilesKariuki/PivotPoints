class PivotPoints:
    def __init__(self):
        self.open = float(input('Enter the Opening price for the session: '))
        self.high = float(input('Enter the Highest price reached for the session: '))
        self.low = float(input('Enter the Lowest price reached for the session: '))
        self.close = float(input('Enter the Closing price for the session: '))

    def pivot_point(self):
        pivot = (self.high + self.low + self.close)/3
        first_support = (2*pivot) - self.high
        second_support = pivot - (self.high - self.low)
        first_resistance = (2*pivot) - self.low
        second_resistance = pivot + (self.high - self.low)
        print(f"""Results for the Pivot Points include:
Second_Resistance: {second_resistance}
First_Resistance: {first_resistance}
Pivot Point: {pivot}
First_Support: {first_support}
Second_Support: {second_support}
        """)


if __name__ == "__main__":
    app = PivotPoints()
    app.pivot_point()
