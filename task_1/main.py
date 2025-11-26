# Гурский
print("start code")
n=1

books=[{"title":"Преступление и наказание","author":"Фёдор Достоевский","year":"1866"},
       {"title":"Мастер и Маргарита","author":"Михаил Булгаков","year":"1928–1940"},
       {"title":"Война и мир","author":"Лев Толстой","year":"1869"},
       {"title":"1984","author":"Джордж Оруэлл","year":"1949"},
       {"title":"Убить пересмешника","author":"Харпер Ли","year":"1960"},
       ]
for book in books:
    
    print((f"Книга {n}").center(50,"-"))
    print(f"Название: {book["title"]}, Автор:{book["author"]},")
    print(f"{(book["year"]).center(50,"-")}\n")
    n+=1
print("end code")