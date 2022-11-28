import wikipedia

search = input("Enter page title: ")
wiki_page = wikipedia.page(search, auto_suggest=False)
while search != '':
    try:
        print(wiki_page.title)
        print(wiki_page.url)
        print(wikipedia.summary(search))

    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search = input("Enter page title: ")

