name = 'Max', 'Andrei', 'Artyom', 'Alona', 'Liza'
phone_number = (380930385662,380930219500,380930923241,380934672257,380939685216)

phone_book = {i: item for i, item in zip(name, phone_number)}
#phone_book = dict(zip(name, phone_number))

print (phone_book)