# PyPaystackAPI
A python API to easily access important paystack services.


  - Initializes transaction and generate payment link
  - Verify Transaction
  - Get a single or all transaction
  
## Installation
Register on the paystack website and get your Authorization key.
Store your authorization key in your environment variable.
#### Windows

```sh
pip install PyPaystackAPI
or
python -m pip install PyPaystackAPI
```
#### Mac or Linux
```sh
sudo pip install PyPaystackAPI
```
## Usage
```sh
# Log your Secret key and you public key into pypaystack/private/config.py
from pypaystack.moPay import transaction
import os
initialize=transaction.Transaction()

#----------Method: charge----------#
---- initialize.verify(reference)
-- Response:
---- verification status(True/False), payment status(abandoned/successful/etc)

---- initialize.charge(amount, email)#amount and email is enough information to rapidly transfer fund.
# OR
---- initialize.charge(amount, email, first_name, last_name, phone)
### redirect option after successful transaction
---- initialize.charge(amount, email, callback_url)
# OR
---- initialize.charge(amount, email, first_name, last_name, phone, callback_url)
-- Response:
---- status, authorization url, reference

#----------Method: verify----------#
---- initialize.verify(reference)
-- Response:
---- verification status(True/False), payment status(abandoned/successful/etc)

#----------Method: fetch----------#
---- initialize.fetch()#fetches all transaction
-- Response:
---- All Tansaction history
---- initialize.fetch(transaction_id)#fetches a single transaction
-- Response:
---- Single transaction history





```
