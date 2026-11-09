import json 
import pandas as pd
import csv 

from datetime import datetime
import time

class KELTNER_ALGO:
    def __init__(self):
        pass



    def opening_the_main_data(self):
        with open(r"C:\Users\dasho\divergence_test.json",'r') as lx:
            data=json.load(lx)
            return data


    def analyzing_the_data(self):
        main_data=self.opening_the_main_data()
        master_closing_prices=[]
        master_opening_prices=[]
        sma_200_list=[]
        
        for datas in main_data:
            closing_prices=datas['CLOSE']
            opening_prices=datas['OPEN']
            date_data=datas['DATE']
            time_data=datas['TIME']


            master_closing_prices.append(closing_prices)
            master_opening_prices.append(opening_prices)


        if len(master_closing_prices)<200:
            print('NOT ENOUGH DATA')
            return 

        length_of_master_list=len(master_closing_prices)
        required_range=length_of_master_list-201
        upgrade=required_range+1
        for j in master_closing_prices[upgrade:]:
            sma_200=j
            sma_200_list.append(sma_200)

        print(len(sma_200_list))




        




        


            


            




k=KELTNER_ALGO()
k.opening_the_main_data()
k.analyzing_the_data()