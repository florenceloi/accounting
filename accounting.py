melon_cost = 1.00

def check_correct_payment(file):
    """Checks if customers paid the correct amount for their melons"""

    # retrieve and process data from .txt file
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split("|")

        # retrieve specific data
        customer_number = words[0]
        customer_name = words[1]
        customer_melons = int(words[2])
        customer_paid = float(words[3])

        # check if payment was correct
        customer_expected = customer_melons * melon_cost
        if customer_expected != customer_paid:
            print customer_name, "(customer #{}) paid ${:.2f}, expected ${:.2f}".format(customer_number, customer_paid, customer_expected)

    the_file.close()

check_correct_payment("customer-orders.txt")