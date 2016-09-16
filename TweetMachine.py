# -*- coding: cp1252 -*-
"""
Name:     TweetMachine.py
Author:   Brian Kingery
Created:  9/16/2016
Purpose:  Break up text into 140 character tweets
"""

import string

print 'Welcome to the Tweet Machine!\n\nThe purpose of this program is to break up text into acceptable 140 character tweets. Current character limit is 1000 meaning 9 tweets.'

method = raw_input('\n0 - Manual text entry\n1 - Text File(.txt) upload\n\nEnter 0 or 1: ')

if method == str(0):
    tweet = raw_input('\nEnter tweet...\n').strip()
    length = len(tweet)
##    print length
    
    if length <= 140:
        print '\n',tweet
        end = raw_input("\nPress 'Enter' to exit program")
    elif length > 140:
        number_of_tweets = length / 125
        number_of_tweets = number_of_tweets + 1

        # break1
        if tweet[125] == ' ':
            break1 = 125
        else:
            break1 = tweet.find(' ',125)
        try:
            # break2
            if tweet[250] == ' ':
                break2 = 250
            else:
                break2 = tweet.find(' ',250)            
            # break3
            if tweet[375] == ' ':
                break3 = 375
            else:
                break3 = tweet.find(' ',375)
            # break4            
            if tweet[500] == ' ':
                break4 = 500
            else:
                break4 = tweet.find(' ',500) 
            # break5            
            if tweet[625] == ' ':
                break5 = 625
            else:
                break5 = tweet.find(' ',625)
            # break6
            if tweet[750] == ' ':
                break6 = 750
            else:
                break6 = tweet.find(' ',750)
            # break7
            if tweet[875] == ' ':
                break7 = 875
            else:
                break7 = tweet.find(' ',875)
            # break8
            if tweet[1000] == ' ':
                break8 = 1000
            else:
                break8 = tweet.find(' ',1000)
        except:
            pass

        # print tweets with breaks
        if number_of_tweets == 2:
            print tweet[:break1]         + ' (1:2)'
            print tweet[break1+1:]       + ' (2:2)'
            end = raw_input("\nPress 'Enter' to exit program")
        elif number_of_tweets == 3:
            print tweet[:break1]         + ' (1:3)'
            print tweet[break1+1:break2] + ' (2:3)'
            print tweet[break2+1:]       + ' (3:3)'
            end = raw_input("\nPress 'Enter' to exit program")
        elif number_of_tweets == 4:
            print tweet[:break1]         + ' (1:4)'
            print tweet[break1+1:break2] + ' (2:4)'
            print tweet[break2+1:break3] + ' (3:4)'
            print tweet[break3+1:] + ' (4:4)'
            end = raw_input("\nPress 'Enter' to exit program")
        elif number_of_tweets == 5:
            print tweet[:break1]         + ' (1:5)'
            print tweet[break1+1:break2] + ' (2:5)'
            print tweet[break2+1:break3] + ' (3:5)'
            print tweet[break3+1:break4] + ' (4:5)'
            print tweet[break4+1:] + ' (5:5)'
            end = raw_input("\nPress 'Enter' to exit program")
        elif number_of_tweets == 6:
            print tweet[:break1]         + ' (1:6)'
            print tweet[break1+1:break2] + ' (2:6)'
            print tweet[break2+1:break3] + ' (3:6)'
            print tweet[break3+1:break4] + ' (4:6)'
            print tweet[break4+1:break5] + ' (5:6)'
            print tweet[break5+1:] + ' (6:6)'
            end = raw_input("\nPress 'Enter' to exit program")
        elif number_of_tweets == 7:
            print tweet[:break1]         + ' (1:7)'
            print tweet[break1+1:break2] + ' (2:7)'
            print tweet[break2+1:break3] + ' (3:7)'
            print tweet[break3+1:break4] + ' (4:7)'
            print tweet[break4+1:break5] + ' (5:7)'
            print tweet[break5+1:break6] + ' (6:7)'
            print tweet[break6+1:] + ' (7:7)'
            end = raw_input("\nPress 'Enter' to exit program")
        elif number_of_tweets == 8:
            print tweet[:break1]         + ' (1:8)'
            print tweet[break1+1:break2] + ' (2:8)'
            print tweet[break2+1:break3] + ' (3:8)'
            print tweet[break3+1:break4] + ' (4:8)'
            print tweet[break4+1:break5] + ' (5:8)'
            print tweet[break5+1:break6] + ' (6:8)'
            print tweet[break6+1:break7] + ' (7:8)'
            print tweet[break7+1:] + ' (8:8)'
            end = raw_input("\nPress 'Enter' to exit program")
        elif number_of_tweets == 8:
            print tweet[:break1]         + ' (1:9)'
            print tweet[break1+1:break2] + ' (2:9)'
            print tweet[break2+1:break3] + ' (3:9)'
            print tweet[break3+1:break4] + ' (4:9)'
            print tweet[break4+1:break5] + ' (5:9)'
            print tweet[break5+1:break6] + ' (6:9)'
            print tweet[break6+1:break7] + ' (7:9)'
            print tweet[break7+1:break8] + ' (8:9)'
            print tweet[break8+1:] + ' (9:9)'
            end = raw_input("\nPress 'Enter' to exit program")
        else:
            print 'Tweet exceeds character limit (1000)'

elif method == str(1):
    print "This method is under development"
