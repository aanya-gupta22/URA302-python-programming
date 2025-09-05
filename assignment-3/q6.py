class EvenNumbers:
    def get_even(self, lst):
        evens = []
        for num in lst:
            if num % 2 == 0:
                evens.append(num)
        return evens

even_finder = EvenNumbers()
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = even_finder.get_even(sample_list)
print("Even numbers:", even_numbers)
