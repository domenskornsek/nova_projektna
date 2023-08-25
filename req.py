import requests

for i in range(7):
    stran = requests.get(
        f"https://www.bolha.com/bazeni-in-oprema?page={i}"
    )
    with open(f"stran{i}.html", "w") as dat:
        dat.write(stran.text)