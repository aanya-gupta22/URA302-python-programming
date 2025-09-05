class ListProcessor:
    def distinct_elements(self, lst):
        distinct = []
        for item in lst:
            if item not in distinct:
                distinct.append(item)
        return distinct

processor = ListProcessor()
unique_list = processor.distinct_elements([1, 2, 2, 3, 4, 4, 5])
print("Distinct elements:", unique_list)
