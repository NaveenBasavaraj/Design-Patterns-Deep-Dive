class PaymentProcessorBruteForce:
    '''
    This violates Open and closed Principle
    Adding new payment method, requires modifying
    this class
    '''
    def process_payment(self, amount, method):
        if method == "credit card":
            print(f"Chargin {amount} to credit card")
        elif method == "debit card":
            print(f"Redirecting to debit payments")
        elif method == "UPI":
            print(f"Redirecting to UPI payments")
        elif method == "Paypal":
            print(f"Redirecting to Paypal payments")
        else:
            pass ## For other options

########### Solution ######################

# 1. Create individual strategy interface
# 2. Call unified context
# 3. Adding new payment method has no impact to existing code

from abc import ABC, abstractmethod
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount:float) -> None:
        pass

class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        print(f"Processing {amount} through {self.card_number}")

class DebitCardStrategy(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        print(f"Processing {amount} through {self.card_number}")

class PayPalStrategy(PaymentStrategy):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        print(f"Processing {amount} through Paypal account{self.email}")

class UPIStrategy(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id
    
    def pay(self, amount):
        print(f"Processing {amount} through Paypal account{self.upi_id}")

# Context

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy) -> None:
        self.strategy = strategy
    
    def set_strategy(self, startegy: PaymentProcessor) -> None:
        self.strategy = startegy
    
    def process_payment(self, amount):
        self.strategy.pay(amount)
    

if __name__ == "__main__":
    processor = PaymentProcessor(CreditCardStrategy("4111111111111234"))
    processor.process_payment(100)

    processor.set_strategy(PayPalStrategy("user@example.com"))
    processor.process_payment(50)

    
    
        