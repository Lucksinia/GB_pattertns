import json

SOLID = [
    "SOLID - is an abbreviation of the 5 basic design principles in object-oriented programming",
    "1. The Single responsibility principle. For each class, a single purpose must be defined. All resources necessary for its implementation should be encapsulated in this class and subordinated only to this task",
    "2. The Open-closed principle. Software entities should be open for expansion, but closed for modification",
    "3. The Liskov substitution principle. Functions that use the base type should be able to use subtypes of the base type without knowing about it",
    "4. The Interface segregation principle. Many interfaces specifically designed for clients are better than one general-purpose interface",
    "5. The Dependency inversion principle. Dependency on Abstractions. There should be no dependence on something specific",
]

KISS = [
    "KISS - is an abbreviation of simplisity principle in object-oriented programming",
    "Keep it simple, stupid. Do not use convoluted way when implementing features",
]


def save_data(params, dict_name):
    """
    :param params: what to save
    :param dict_name:  "GET" or "POST"
    :return:
    """
    with open("data.json", "r", encoding="utf-8") as f_r:
        data = json.load(f_r)

    with open("data.json", "w", encoding="utf-8") as f_w:
        order = data[dict_name]
        order.append(params)
        json.dump(data, f_w, indent=4, ensure_ascii=False)
