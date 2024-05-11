def make_car(manufacturer, model, **numbers):
    car_dict = {
        "manufacturer": manufacturer.title(),
        "model": model.title(),
    }
    for number, value in numbers.items():
        car_dict[number] = value
    return car_dict


my_outback = make_car("sabaru", "outback", color="blue", tow_package=True)
print(my_outback)

my_old_accord = make_car(
    "honda", "accord", year=1941, color="write", headlights="popup"
)
print(my_old_accord)
