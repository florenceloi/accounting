melon_cost = 1.00

def get_customer_info(file):
    """Gets customer's name, number of melons purchased, and payment"""

    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split("|")
        words[1] = words[1].split()

        name = words[1][0]
        melons = words[2]
        paid = words[3]

    the_file.close()

get_customer_info("customer-orders.txt")


# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print customer1_name, "paid {:.2f}, expected {:.2f}".format(
#         customer1_paid, customer1_expected)

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print customer2_name, "paid {:.2f}, expected {:.2f}".format(
#         customer2_paid, customer2_expected)

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print customer3_name, "paid {:.2f}, expected {:.2f}".format(
#         customer3_paid, customer3_expected)

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print customer4_name, "paid {:.2f}, expected {:.2f}".format(
#         customer4_paid, customer4_expected)

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print customer5_name, "paid {:.2f}, expected {:.2f}".format(
#         customer5_paid, customer5_expected)

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print customer6_name, "paid {:.2f}, expected {:.2f}".format(
#         customer6_paid, customer6_expected)
