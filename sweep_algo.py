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
        current_high_prev_close=[]
        current_low_prev_close=[]
        master_high_prices=[]
        master_low_prices=[]
        jk=[]
        k=[]
        o=[]

        sma_200_list=[]
        
        for datas in main_data:
            closing_prices=datas['CLOSE']
            opening_prices=datas['OPEN']
            high_prices=datas['HIGH']
            low_prices=datas['LOW']

            date_data=datas['DATE']
            time_data=datas['TIME']


            master_closing_prices.append(closing_prices)
            master_opening_prices.append(opening_prices)
            master_high_prices.append(high_prices)
            master_low_prices.append(low_prices)



        ######### 200 SMA OPERATIONS ########
        if len(master_closing_prices)<200:
            print('NOT ENOUGH DATA')
            return 

        length_of_master_list=len(master_closing_prices)
        required_range=length_of_master_list-201
        upgrade=required_range+1
        for j in master_closing_prices[upgrade:]:
            sma_200=j
            sma_200_list.append(sma_200)

        ####### CURRENT HIGH PREV_CLOSE ########
        for master_prices in master_high_prices[:-1]:
            k.append(master_prices)
        master_closing_prices.reverse()
        k.reverse()

        finalized_results=[x-y for x,y in zip(k,master_closing_prices[0:-1])]
        for v in finalized_results:
            hh=abs(v)
            current_high_prev_close.append(hh)



        for price in master_low_prices[:-1]:
            jk.append(price)

        master_closing_prices.reverse()
        jk.reverse()

        final_results=[x-y for x,y in zip(jk,master_closing_prices[0:-1])]
        for gg in final_results:
            ty=abs(gg)
            current_low_prev_close.append(ty)



            










        



        



        


            
        





        




        


            


            




k=KELTNER_ALGO()
k.opening_the_main_data()
k.analyzing_the_data()