class StringAnalyser:
    def count_case(self, s):
        counts = {"uppercase": 0, "lowercase": 0}
        for char in s:
            if 'A' <= char <= 'Z':
                counts["uppercase"] += 1
            elif 'a' <= char <= 'z':
                counts["lowercase"] += 1
        return counts

analyzer = StringAnalyser()
result = analyzer.count_case("Hello World!")
print("Uppercase and lowercase counts:", result)
