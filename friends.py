#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 14:23:46 2019

@author: rakhil163
"""

users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    count = 0
    for i in friendship:
        if(i[0]==user or i[1]==user):
            count +=1
    username=''
    for i in users:
        if(user == i['id']):
            username=i['name']        
      
   # print (username + " has " + str(count) + " friends")    
    return count
    

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''

    for i in users:
        i.setdefault('count',0)
        k=num_friends(i['id'])
        i['count']=k
    newlist = sorted(users, key=lambda k: k['count'],reverse=True) 
    
    for i in newlist:
        print(i['name']+" has "+ str(i['count']) +" friends")
        
print("Calling num_friends for userid 0 gives count as "+str(num_friends(0)))
 

print("Calling sorted list")     
sort_by_num_friends()