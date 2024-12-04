import pygame
import mysql.connector 

mydb = mysql.connector.connect(host = "", user = "", password="")
mydb.cursor().execute("CREATE DATABASE models")
