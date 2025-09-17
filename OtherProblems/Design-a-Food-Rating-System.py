class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToCuisine = {}
        self.foodToRating = {}
        self.cuisineRanking = {}

        for f, c, r in zip (foods, cuisines, ratings):
            self.foodToCuisine[f] = c
            self.foodToRating[f] = r
            if c not in self.cuisineRanking:
                self.cuisineRanking[c] = []
            heapq.heappush(self.cuisineRanking[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.foodToRating[food] = newRating
        c = self.foodToCuisine[food]
        heapq.heappush(self.cuisineRanking[c], (-newRating,food))


    def highestRated(self, cuisine: str) -> str:
        top = self.cuisineRanking[cuisine]

        while top and -top[0][0] != self.foodToRating[top[0][1]]:
            heapq.heappop(top)
        return top[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)