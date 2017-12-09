class GasStations:
    def tripCost(self, dist, price, mpg, tankSize, tripLength):
        dist = list(dist)
        price = list(price)
        dist = dist + [tripLength]
        price = price + [0]

        start = 0
        remain_gas = tankSize
        answer = 0
        n = len(dist)

        # if tankSize * mpg >= tripLength:
        #     return 0

        cur_index = self.find_cheapest(start, start + remain_gas * mpg, dist, price)
        remain_gas = remain_gas - (dist[cur_index] - start) / mpg
        start = dist[cur_index]

        for i in range(n):
            cheaper_index = -1
            for j in range(n):
                if dist[j] > dist[cur_index] and price[j] < price[cur_index] and dist[j] - dist[cur_index] <= tankSize * mpg:
                    cheaper_index = j
                    break

            if cheaper_index >= 0:
                total_gas = (dist[cheaper_index] - dist[cur_index]) / mpg  # calc total gas need to next stop
                need_gas = max(total_gas - remain_gas, 0)  # how many gas need
                answer += need_gas * price[cur_index]  # buy gas

                remain_gas += need_gas  # add gas
                remain_gas -= total_gas  # use gas
                start = dist[cheaper_index]  # update next stop
                cur_index = cheaper_index

                if cheaper_index == n - 1:
                    break
            else:
                cheapest_index = self.find_cheapest(start, start + tankSize * mpg, dist, price)
                answer += (tankSize - remain_gas) * price[cur_index]
                remain_gas = tankSize

                need_gas = (dist[cheapest_index] - dist[cur_index]) / mpg
                remain_gas -= need_gas
                start = dist[cheapest_index]
                cur_index = cheapest_index

                if cheapest_index == n - 1:
                    break

        return answer

    def find_cheapest(self, start, end, dist, price):
        cheapest_index = -1
        cheapest_price = 10 ** 10

        for i, (cur_dist, cur_price) in enumerate(zip(dist, price)):
            if not start < dist[i] <= end:
                continue

            if cheapest_index < 0 or cheapest_price > cur_price:
                cheapest_index = i
                cheapest_price = cur_price

        return cheapest_index


if __name__ == '__main__':
    solver = GasStations()
    print(solver.tripCost((100, 100), (1000, 1500), 20, 10, 300))
    print(solver.tripCost((300,450,525), (1659,1529,1439), 20, 20, 600))
    print(solver.tripCost((300, 450, 525), (1659,1439,1529), 20, 20, 600))
    print(solver.tripCost((300,125,450,525), (1659,1729,1439,1529), 20, 20, 600))
    print(solver.tripCost((200,), (1000,), 20, 20, 400))
    print(solver.tripCost((100, 400), (1549,1649), 25, 16, 600))