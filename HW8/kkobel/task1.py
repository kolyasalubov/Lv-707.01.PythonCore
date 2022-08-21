import areas_of_figures


def calculating_areas(user_input: str):
    if user_input == 'rectangle':
        print(f"Area of Rectangle is: {areas_of_figures.rectangle(int(input('Enter number first: ')), int(input('Enter number second: ')))}")
    elif user_input == 'triangle':
        print(f"Area of Triangle is: {areas_of_figures.triangle(int(input('Enter side_a: ')), int(input('Enter heights: ')))}")
    elif user_input == 'circle':
        print(f"Area of Circle is: {areas_of_figures.circle(int(input('Enter radius: ')))}")
    else:
        print('You entered not correct function')
        print('Try again, please')
        user_input = calculating_areas(input('Enter function (rectangle, triangle, circle) to calculate areas : '))        

user_input = calculating_areas(input('Enter function (rectangle, triangle, circle) to calculate areas : '))
