# digitalwalletsystem
Technical Exam

# Overview
This document provides a detailed explanation of the **Digital Wallet System**, its APIs, how to access it, and how to use the implementation uploaded on GitHub.

# Features
1. **Balance Inquiry** - Check the current balance of the wallet.
2. **Cash-in** - Add funds to the wallet.
3. **Debit** - Deduct funds from the wallet.
The project is implemented in Python using only default libraries, ensuring simplicity and portability.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Code Documentation
# File: `digitalwalletsystem.py`

1. HTTP Server
The script uses Python's `http.server` module to create an HTTP server.
- **Port**: 8000 (default)
- **Endpoints**:
  - `/balance`: GET request to retrieve the current wallet balance.
  - `/cash-in`: POST request to add funds.
  - `/debit`: POST request to deduct funds.
  
2. Key Functions
# `_send_response(self, response, status=200)`
- Sends HTTP responses with the given JSON `response` and status code.
# `do_GET(self)`
- Handles GET requests.
- Endpoint `/balance`:
  - Returns the current wallet balance.
# `do_POST(self)`
- Handles POST requests.
- Endpoint `/cash-in`:
  - Accepts a JSON payload with `amount` and adds it to the wallet balance.
  - Example Payload: `{ "amount": 100 }`
- Endpoint `/debit`:
  - Deducts the specified `amount` from the wallet if sufficient funds exist.
  - Example Payload: `{ "amount": 50 }`
# `run()`
- Initializes and starts the HTTP server.

3. Wallet Data
The wallet balance is stored in a dictionary:
wallet = {"balance": 0.0}
This ensures simple management of the wallet state during runtime.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# How to Access the Project on GitHub
# Step 1: Clone the Repository
1. Open your terminal or command prompt.
2. Run the following command:
   git clone https://github.com/clnalinea/digitalwalletsystem.git
   
# Step 2: Navigate to the Directory
cd digitalwalletsystem
# Step 3: Run the Script
1. Ensure Python is installed (version 3.x).
2. Run the script:
   python digitalwalletsystem.py
3. The server will start on `http://localhost:8000`.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# To test the script in Postman
1. Start the Server
Make sure the Python server is running by executing the script you provided in your terminal:
python digitalwalletsystem.py
This will start a server on http://localhost:8000.
2. Test GET Request for Balance
To check the current balance:
Open Postman.
Set the request type to GET.
Enter the URL: http://localhost:8000/balance.
Click Send.
You should receive a response showing the balance, like:
{
    "balance": 0.0
}
3. Test POST Request for Cash-in
To add funds (cash-in) to the wallet:
In Postman, set the request type to POST.
Enter the URL: http://localhost:8000/cash-in.
In the Body tab, select raw and set the type to JSON.
Enter a JSON payload like:
{
    "amount": 50.0
}
Click Send.
You should receive a response like:
{
    "message": "Cash-in successful",
    "new_balance": 50.0
}
4. Test POST Request for Debit
To subtract funds (debit) from the wallet:
Set the request type to POST.
Enter the URL: http://localhost:8000/debit.
In the Body tab, select raw and set the type to JSON.
Enter a JSON payload like:
{
    "amount": 20.0
}
Click Send.
You should receive a response like:
{
    "message": "Debit successful",
    "new_balance": 30.0
}
5. Test Invalid Requests
You can also test invalid requests, such as:
Invalid amount for cash-in or debit (e.g., amount: -5).
Insufficient funds (e.g., requesting a debit of 100 when the balance is 50).
The server will respond with appropriate error messages like:
{
    "error": "Invalid amount"
}
or
{
    "error": "Invalid or insufficient funds"
}
These steps will help you test the basic functionality of the digital wallet API using Postman.
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Notes
- Ensure that `git` is installed to clone the repository.
