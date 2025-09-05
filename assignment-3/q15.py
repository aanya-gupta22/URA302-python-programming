class StringHandler:
    def __init__(self):
        self.text = ""

    def get_String(self):
        self.text = input("Enter a string: ")

    def print_String(self):
        print(self.text.upper())

handler = StringHandler()
handler.get_String()
handler.print_String()
