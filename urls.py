from datetime import date
from views import Index, About, Contacts


# front controller
def front(request):
    request["date"] = date.today()
    request["weather"] = get_weather()


def get_weather():
    import requests

    url = "https://api.open-meteo.com/v1/forecast?latitude=53.90&longitude=27.43&current_weather=True"
    r = requests.get(url)
    result = r.json()
    current_weather = f'Minsk, right Now: {result["current_weather"]["temperature"]} C.'
    return current_weather


fronts = [front]

routes = {
    "/": Index(),
    "/index/": Index(),
    "/examples/": About(),
    "/contact/": Contacts(),
}
