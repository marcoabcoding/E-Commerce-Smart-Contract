# E-Commerce Smart Contract Simulation in Python

# Overview
This repository contains a Python script simulating a smart contract for e-commerce transactions. Designed to demonstrate the fundamental concept of a smart contract between a buyer and a seller in an e-commerce setting.

Description

The SmartContract class manages a transaction where a buyer agrees to purchase a product at a specified price from a seller. The script illustrates the basic workflow of a smart contract in an e-commerce context.
# Features

    Contract initiation with buyer, seller, and price.
    Payment handling from the buyer.
    Delivery confirmation process.
    Transaction finalization upon completion of payment and delivery.
    Tracking of the contract's current status.

# Code Structure

    __init__: Initializes the contract with default values.
    initiate_contract: Starts the contract with the specified buyer, seller, and price.
    pay: Handles payment from the buyer.
    deliver_item: Confirms the delivery of the item after payment.
    finalize_transaction: Completes the transaction after payment and delivery.
    contract_status: Provides the current status of the contract.
# Code Explanation
- `initiate_contract`: Sets up the contract with the buyer, seller, and price.
- `pay`: Simulates the payment process by the buyer.
- `deliver_item`: Checks if the payment is made before marking the item as delivered.
- `finalize_transaction`: Finalizes the transaction after confirming payment and delivery.
- `contract_status`: Provides the current status of the contract.

# Usage Example
```python
contract = SmartContract()
print(contract.initiate_contract("Alice", "Bob", 100))
print(contract.pay("Alice", 100))
print(contract.deliver_item())
print(contract.finalize_transaction())
