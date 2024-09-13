import datetime
current_time = datetime.datetime.now()
def my_brand(assignment_name):
    embellishment = '=*=*=*='
    name = 'Sohan Chatterjee'
    course = 'Course 2024S-SSW567-WS'

    print(embellishment + name + embellishment)
    print(embellishment + course + embellishment)
    print(embellishment + assignment_name + embellishment)
    print(embellishment, current_time, embellishment)

my_brand("HW 00 Tools Setup")