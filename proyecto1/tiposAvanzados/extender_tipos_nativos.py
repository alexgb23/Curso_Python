class Lista(list):
    def prepend(self, value):
        self.insert(0, value)

lista=Lista([1, 2, 3, 4])
lista.append(5)


lista.prepend(0)
print(lista)

