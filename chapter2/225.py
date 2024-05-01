'''
At the beginning of this section, you learned that you can use the input function to
collect a user’s input. Mary is an elementary school teacher who wants to write a sim-
ple toy program for her students. Suppose that she wants to ask the students about
today’s temperature in Celsius degrees, using a Python console. How can she write the
program so that it meets the following requirements? x represents the value that the
user enters:
 When the temperature is < 10 degrees, output You entered x degrees. It's
cold!
 When the temperature is between 10 and 25 degrees, output You entered x
degrees. It's cool!
 When the temperature is > 25 degrees, output You entered x degrees. It's
hot!
 The x value should have one decimal precision. If the user enters 15.75, for
example, it should be displayed as 15.8
'''

x = input('Enter the temperate in Celsius: ')

try:
    temp = float(x)
except ValueError:
    print(f"Could not cast {x} to a number")
else:
    if temp < 10:
        print(f"You entered {temp:.1f} degrees. It's cold!")
    elif temp>=10 and temp<=25:
        print(f"You entered {temp:.1f} degrees. It's cool!")
    elif temp>25:
        print(f"You entered {temp:.1f} degrees. It's hot!")