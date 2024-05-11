def make_car(manufactions, model, **options):
    car_dict = {
        "manufactions": manufactions.title(),
        "model": model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value
        return car_dict


my_outback = make_car("subaru", "outback", color="blue", tow_package=True)
print(my_outback)

my_old_accord = make_car(
    "honda", "accord", year=1991, color="white", headlights="popup"
)
print(my_old_accord)
