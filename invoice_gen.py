from datetime import datetime


class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.cost = 0
        self.items = []

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }

        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)

    def calculate_total(self, discount):
        # determine how much the invoice total should be by summing all individual item totals
        total = 0
        totalWithTax = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]
            total += price
            totalWithTax += price + price * tax

        discountAmount = total * discount / 100
        finalTotal = totalWithTax - discountAmount
        return finalTotal, totalWithTax, discount, discountAmount

    def showDetails(self):
        print("Invoice Details")
        print("----------------")
        print("Sender: " + self.sender_name)
        print("Recipient: " + self.recipient_name)
        print("Date: " + str(self.date)+"\n")
        for item in self.items:
            print("Item: " + item["name"])
            print("Price: $" + str(item["price"]))
            print("Tax: " + str(item["tax"]*100)+"%\n")
        print("-----------------")

if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)
    invoice.showDetails()
    invoice_total,total_with_tax,discount,discount_amount = invoice.calculate_total(20)

    print("Total amount $"+str(invoice_total)+"\n"+ "Total with tax $"+str(total_with_tax)+"\n"+"Discount "+str(discount)+"%"+"\n"+"Discount amount $"+str(discount_amount))