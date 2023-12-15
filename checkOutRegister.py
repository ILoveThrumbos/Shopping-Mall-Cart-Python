from datetime import date
from product import Product


class CheckoutRegister:
    """
    The CheckoutRegister class is the checkout stage used to determine the price of the products
    after the barcode has been inputted by the user.
    It will print out a receipt after the total amount due is paid by the customer and show their remaining balance
    (over-payed) given.
    The checkout system will save the transaction details  into a .txt file as a temporary database.
    """
    def __init__(self):
        self.customer_pay = 0
        self.balance = 0
        self.due = 0
        self.products = []


    def read_barcode(self, barcode):
        """
        Reads barcode and retrieves the product information from the database.


        :param barcode: The barcode being scanned
        :return: The Product object will be returned if the barcode is found (True), else will return False.
        """
        found = False
        with open('product.txt', 'rt') as find_barcode:
            for each_product in find_barcode:
                product_found = each_product.strip().split(',')
                if barcode == product_found[0]:
                    barcode, name, desc, price = product_found
                    found = True

                    print('\n' + name + ',' + desc + ' - $' + price + '\n')
                    p = Product(barcode, name, desc, price)
                    return p

        if found:
            return found
        else:
            return False

    def scan_item(self, product_barcode):
        """
        Scan a product item by reading the barcode and adds it to the list of products (product[])

        :param product_barcode: The barcode that will be scanned
        :return: N/A
        """
        p1 = self.read_barcode(product_barcode)  # Retrieve the Product object using read_barcode method
        if p1:
            self.products.append(p1)  # Append the Product object to the products list
            self.scan_again()  # Will prompt scan_again
        else:
            print('ERROR!! - scanned barcode is incorrect.\n')
            self.scan_again()

    def scan_again(self):
        """
        Prompts user to scan another product item with input y, or finishing scanning with input n.
        Else, the input will be invalid.
        Both y and n inputs will be .lower() meaning not case-sensitive.

        :return: N/A
        """
        while True:
            scan_again_input = input('Would you like to scan another item? (Y/N):')

            if scan_again_input.lower() == 'y':
                product_barcode = input('\nPlease enter the barcode of your item: ')
                self.scan_item(product_barcode)
                break
            elif scan_again_input.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

    # adds the price of the products by checking the item added to the cart(product added into system)
    # reads the data from the database product.txt in the Product class to determine price
    def calculate_payment_due(self):
        cart_totals = 0
        # enumerate help read product.txt (tuple) without incrementing the file from the Product class
        for index, product in enumerate(self.products):
            # if self.cart_totals == product.price:
            # print(product.price)
            cart_totals += float(product.price)  # {'barcode': barcode, 'name': name, 'desc': desc, 'price': price}
        self.due = cart_totals
        return cart_totals

    # use the price found from the Products class to create the payment
    def payment(self, total):
        # use the price found from the Products class to create the payment
        amount = total
        if amount == 0:
            balance = 0
        else:
            # prints the sum total price/s of the products
            print('\nPayment due: $' + str(amount))
            balance = self.accept_payment(amount)
        self.balance = balance
        return balance

    # creates a floating (decimal values) input to be paid by the customer.
    # Does not accept negative values and only accepts integers
    def accept_payment(self, amount_paid):
        paid = float(0.0)
        customer_pay = float(0.0)
        due = float(0.0)
        total = amount_paid
        balance = 0.0  # Initialize the balance variable

        while True:
            try:
                # presents an input for the user
                paid = float(input('Please enter an amount to pay: '))

                # if the amount paid is less than 0 print an error message
                if paid < 0.0:
                    print('ERROR!! – Negative amounts are not accepted')

                # else customer entered a valid payment
                else:
                    customer_pay += paid
                    self.customer_pay = customer_pay

                    # if the amount paid (total) is greater than 0.0 (paid)
                    if paid < total:
                        due = total - paid
                        # due is the sum of the product cost needed to be paid by the customer
                        total = due
                        # prints the amount due for the customer
                        print('Payment due: $' + str(due))
                        continue

                    # else determines the balance left for the customer
                    balance = paid - total
                    self.balance = balance
                    break

            # must enter the correct value (an integer)
            except ValueError:
                print('ERROR!! – Please enter the correct value.')

        return balance

    # prints out the receipt for the customer with the products and their prices
    # also prints out the total cost of the products (Total amount due), the amount paid (amount received),
    # and the change (balance)
    def print_receipt(self, balance):
        print('\n----- Final Receipt -----\n')
        # enumerate help read product.txt (tuple) without incrementing the file from the Product class
        for index, item in enumerate(self.products):
            print(item.name, ',', item.desc, '     $' + str(item.price))
        print('\n')
        print('Total amount due:', '     $' + str(self.due))
        print('Amount received', '       $' + str(self.customer_pay))
        print('Balance given', '         $' + str(self.balance))

    # saves the transactions made in the self_service checkout system into a .txt file with the date, barcode and amount
    def save_transaction(self, today):
        # finds today's date from the datetime import
        today = date.today()
        # opens the transaction.txt file and appends/store (adds) values into the file (save)
        with open('transaction.txt', 'a') as save:
            # enumerate helps read product.txt (tuple) without incrementing the file from the Product class
            for index, product in enumerate(self.products):
                # prints the save file and appends it to the database (file=save)
                # printed files saved to the .txt database are the current date, barcode, and product price
                print(str(today), str(product.barcode), str(product.price), file=save)

