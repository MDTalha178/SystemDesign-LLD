class TextEditor:
    text:str

    def __init__(self):
        self.text = ''

    def type(self, text):
        self.text += text

    def delete(self, length):
        self.text = self.text[:len(self.text)-length]

    def read(self):
        return self.text