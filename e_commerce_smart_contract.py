class SmartContract:
    """
    A simplified smart contract for an e-commerce transaction.
    Handles the process between a buyer buying a product at a certain price from a seller.
    """
    def __init__(self):
        # Initialize the contract with default participant details and transaction status
        self.buyer = None
        self.seller = None
        self.price = 0
        self.buyer_paid = False
        self.item_delivered = False

    def initiate_contract(self, buyer, seller, price):
        # Set up the contract with buyer, seller, and price
        if not self.buyer and not self.seller:
            self.buyer = buyer
            self.seller = seller
            self.price = price
            return "Contract initiated!"
        return "Contract is already in place."

    def pay(self, buyer, amount):
        # Handle payment from the buyer
        if buyer == self.buyer and amount == self.price and not self.buyer_paid:
            self.buyer_paid = True
            return "Payment received."
        return "Payment failed."

    def deliver_item(self):
        # Confirm delivery of the item if payment was received
        if self.buyer_paid:
            self.item_delivered = True
            return "Item delivered."
        return "Payment not received. Cannot deliver item."

    def finalize_transaction(self):
        # Finalize the transaction after confirming payment and delivery
        if self.buyer_paid and self.item_delivered:
            return f"Transaction finalized. {self.price} transferred to {self.seller}."
        return "Transaction cannot be finalized yet."

    def contract_status(self):
        # Return the current status of the contract
        return {
            "buyer": self.buyer,
            "seller": self.seller,
            "price": self.price,
            "buyer_paid": self.buyer_paid,
            "item_delivered": self.item_delivered
        }

# Example usage
contract = SmartContract()
print(contract.initiate_contract("Alice", "Bob", 100))  # Initiate the contract
print(contract.pay("Alice", 100))                       # Alice makes payment
print(contract.deliver_item())                          # Item delivery process
print(contract.finalize_transaction())                  # Finalize the transaction
