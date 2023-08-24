def preberi(n):
    besedila = []
    for i in range(n):
        with open(f"stran{i}.html") as dat:
            besedilo = dat.read()
            besedila.append(besedilo)

    return besedila