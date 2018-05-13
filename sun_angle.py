def sun_angle(time):
    hour, minutes = time.split(":")
    if int(hour) < 6 or int(hour) > 18:
        return "I don't see the sun!"
    angle = (((int(hour) * 60 + int(minutes)) * 90) / 720)
    print("angle = " + str(angle))
    return angle


if __name__ == '__main__':
    # print("Example:")
    print(sun_angle("06:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert sun_angle("07:00") == 15
    # assert sun_angle("01:23") == "I don't see the sun!"
    # print("Coding complete? Click 'Check' to earn cool rewards!")
