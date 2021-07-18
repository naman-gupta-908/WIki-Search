import wikipedia
query=wikipedia.page(input("what do you want to search on wikipedia? : "))
print(query.summary)