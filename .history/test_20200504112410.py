from app import app
from flask import Flask, session, render_template, request, session, g, redirect, url_for
import os, random
import mysql.connector
from database.dbconn import Database_connection
import unittest
from unittest.mock import Mock
from donations.donations import *
from paymentAuthentication.Interceptor_contextObject import *
from food_donation.foodItems import *
from flask_testing import TestCase
from dao.dao import DataBase


class TestDonation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
    
    def tearDown(self):
        pass 


    def test_Login(self):
        result = self.app.get('/login') 
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_Register(self):
        result = self.app.get('/register') 
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_ChooseDonation(self):
        df = Donations()
        Money = df.get_donation_type("MoneyDonation")
        result1=MoneyDonation
        food = df.get_donation_type("FoodDonation")
        result2=FoodDonation
        clothes=df.get_donation_type("ClothesDonation")
        result3=ClothesDonation
        
        # assert the results
        self.assertEqual(Money,result1)
        self.assertEqual(food,result2)
        self.assertEqual(clothes,result3)

    def test_InterceptorLogger(self):

        Interceptor=ConcreteInterceptor.log(self,ContextObject("Vishal"))
        self.assertEqual(Interceptor,"Vishal")

    def test_getlocation(self):
        list=['Thomond', 'Plassey', 'Kilmurry', 'Claunlara', 'Groody']
        d=DataBase()
        db=d.getLocations()
        self.assertEqual(db,list)

    def test_getCategory(self):
        list=['Clothes', 'Footwear', 'Accessories', 'SoftToy']
        d=DataBase()
        db=d.getCategories()
        self.assertEqual(db,list)

    def test_getModes(self):
        list=['Self', 'Agent']
        d=DataBase()
        db=d.getModes()
        self.assertEqual(db,list)

    def test_getFoodItems(self):
        list=['Grains', 'Products', 'Fruits']
        d=DataBase()
        db=d.getFoodItems()
        self.assertEqual(db,list)

if __name__ == "__main__":
    unittest.main()

