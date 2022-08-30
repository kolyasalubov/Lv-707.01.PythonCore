import firstModule
def figureArea(figure):
    if figure == 'recktangle':
        return firstModule.recktangleArea()
    if figure == 'triangle':
        return firstModule.triangleArea()
    if figure == 'circle':
        return firstModule.circleArea()
    else:
        print('Try again')
figureArea(input('Enter figure: '))