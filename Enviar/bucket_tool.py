def ChangeColor (array, x, y, newColor):
    currentColor = array[x][y] # supose array[x][y] is the color of the pixel at x, y
    return changeTo (array, x, y, newColor, currentColor)

def changeTo (array, x, y, newColor, currentColor):
    if currentColor == array[x][y]:
        array[x][y] = newColor
    else:
        return
    changeTo (array, x + 1, y, newColor, currentColor)
    changeTo (array, x - 1, y, newColor, currentColor)
    changeTo (array, x, y + 1, newColor, currentColor)
    changeTo (array, x, y - 1, newColor, currentColor)
    return array