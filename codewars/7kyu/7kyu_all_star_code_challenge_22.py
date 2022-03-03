def to_time(seconds):
    # template = "{} hour(s) and {} minute(s)"
    # return template.format(sec//3600, sec%3600//60)
    return "{} hour(s) and {} minute(s)".format(seconds//3600, seconds%3600//60)


def test_to_time():
    result = to_time(3600)
    assert result == "1 hour(s) and 0 minute(s)", f"Wrong answer {result} !"
    print(result)
    result = to_time(3601)
    assert result == "1 hour(s) and 0 minute(s)", f"Wrong answer {result} !"
    print(result)
    result = to_time(3500)
    assert result == "0 hour(s) and 58 minute(s)", f"Wrong answer {result} !"
    print(result)
    result = to_time(323500)
    assert result == "89 hour(s) and 51 minute(s)", f"Wrong answer {result} !"
    print(result)
    result = to_time(0)
    assert result == "0 hour(s) and 0 minute(s)", f"Wrong answer {result} !"
    print(result)


if __name__ == "__main__":
    test_to_time()