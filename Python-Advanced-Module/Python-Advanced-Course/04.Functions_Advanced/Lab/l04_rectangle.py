def rectangle(length, width):
    def area():
        rect_area = length * width
        return rect_area

    def perimeter():
        rect_perimeter = 2 * length + 2 * width
        return rect_perimeter

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle('2', 10))