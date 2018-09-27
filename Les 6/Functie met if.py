def lang_genoeg (Lengte):
    if Lengte >= 120:
        print("Je bent lang genoeg")
    else:
        print("je bent niet lang genoeg")
    return

lang_genoeg(int(input("Vul je lengte in (Centimeters):" )))