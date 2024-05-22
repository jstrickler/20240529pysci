import logging

logging.basicConfig(filename="simple.log")
x = 5
y = "cheese"

try:  # Execute code that might have a problem
    z = x + y
    print("Bottom of try")

except TypeError as err:    # Catch the expected error; assign error object to err
    logging.exception("values %s %s -- %s", x, y, err)

print("After try-except")  # Get here whether or not exception occurred
