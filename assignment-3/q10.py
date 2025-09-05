class TemperatureClassifier:
    def classify_temperature(self, temp):
        if temp < 15:
            return "Cold"
        elif 15 <= temp <= 30:
            return "Moderate"
        else:
            return "Hot"

# Example
classifier = TemperatureClassifier()
print(classifier.classify_temperature(10))  
print(classifier.classify_temperature(25))  
print(classifier.classify_temperature(35))  
