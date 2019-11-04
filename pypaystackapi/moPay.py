#!/usr/bin/env python
# -*- coding: utf-8 -*-
from private import config
import requests
GET, POST, url= requests.get, requests.post, config.url
headers={"Authorization":"Bearer" +" " + config.secret_key, "Content-Type": "application/json"}
class Transaction:
    headers=headers
    url=config.url
    def charge(self, amount, email, first_name=None, phone=None, last_name=None, callback_url=None, end_point='initialize'):
        """
        args:
        amount(string): amount to be charged
        email(string): email address
        kwarg:
        first_name(string) --> None
        last_name(string) --> None
        phone(string) --> None
        callback_url(string) --> None: url to redirect to after successful transaction
        """
        data={"amount": amount, "email": email, "first_name":first_name, "last_name":last_name,'callback_url':callback_url}
        request=POST(self.url + end_point, headers=self.headers, json=data)
        response=request.json()
        return response['status'], response['data']['authorization_url'], response['data']['reference']

    def verify(self, ref, end_point='verify'):
        """
        For Verifying Transactions Before giving value to your customer, you \
        should verify the status of the transaction by passing the reference to the API.\
        args:
        ref: reference code
        ref(string) --> Unique transaction reference. It is a one-time key generated after initializing transaction.
        """
        request=GET(self.url+end_point+ref, headers=headers)
        data=request.json()
        return data['status'], data['data']['status']
    
    def fetch(self, transaction_id=None):
        """
        For retrieving previous transaction details.
        args:
        transaction_id: id of the transaction(int32)
        kwargs:
        transaction_id=None
        Example:
        fetch()--> Retrieves all previous transactions
        fetch(transaction_id)--> Retrieves a single transactions 
        """
        if transaction_id:
            request=GET(self.url+transaction_id, headers=headers)
            data=request.json()
            return data
        else:
            self.__fetch_all__()

    def __fetch_all__(self):
        request=GET(self.url, headers=headers)
        data=request.json()
        return data
