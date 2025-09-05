class RangeTester:
    def test_range(self, n):
        if (100 <= n <= 1000) or (n == 2000):
            return True
        else:
            return False

tester = RangeTester()

print(tester.test_range(150))   
print(tester.test_range(2000))  
print(tester.test_range(50))   
print(tester.test_range(1500))  
