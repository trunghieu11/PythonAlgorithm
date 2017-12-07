class GasStations:
    def tripCost(self, dist, price, mpg, tankSize, tripLength):
        start = 0
        end = mpg * tankSize
        answer = 0
        while end < tripLength:
            min_price = 10**10
            for location in dist:
                if start < location <= end:
                    
