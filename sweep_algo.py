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
        bmw=[]

        master_opening_prices=[]
        current_high_prev_close=[]
        current_low_prev_close=[]
        master_high_prices=[]
        master_low_prices=[]
        current_high_current_low=[]
        finalized_tr=[]
        atr_values=[]
        jk=[]
        lk=[]
        plus_dm=[]
        negative_dm=[]
        k=[]
        main_list=[]
        required_indices=[]
        finalized_values=[]
       

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
        

        finalized_results=[x-y for x,y in zip(master_high_prices[1:],master_closing_prices[0:-1])]
        #finalized_results.reverse()
        for v in finalized_results:
            hh=abs(v)
            current_high_prev_close.append(hh)

        ######## CURRENT_LOW_PREV_CLOSE ########


        final_results=[x-y for x,y in zip(master_low_prices[1:],master_closing_prices[0:-1])]
        #final_results.reverse()
        for gg in final_results:
            ty=abs(gg)
            current_low_prev_close.append(ty)


        ######## CURRENT_HIGH_CURRENT_LOW  ########


        final_results_=[x-y for x,y in zip(master_high_prices,master_low_prices)]
        for tt in final_results_:
            uu=abs(tt)
            current_high_current_low.append(uu)



        for x,y,z in zip(current_high_current_low,current_low_prev_close,current_high_current_low):
            maximum_values=max(x,y,z)
            finalized_tr.append(maximum_values)

        for index_,his,in enumerate(finalized_tr):
            main_data[index_+1]['TR']=abs(his)



        for sonam in finalized_tr:
            main_vals=finalized_tr.index(sonam)
            if main_vals not in main_list:
                main_list.append(main_vals)
            if main_data in main_list:
                main_list_last_value=main_list[-1]
                new_index_value=main_list_last_value+1
                main_list.append(new_index_value)
        original_length=len(finalized_tr)
        new_list_length=len(main_list)
        new_ranger=main_list[0:new_list_length-1]
        main_list.append(new_ranger)
        for new_vals in new_ranger[10:]:
            required_indices.append(new_vals)
        for r,h in zip(new_ranger,required_indices):
            master_values=sum(finalized_tr[r:h])
            finalized_values.append(master_values)



        #########  ATR CALCULATION ##########


        for finals in finalized_tr[:-1]:
            bmw.append(finals)

        finalized_values.reverse()
        bmw.reverse()

        finalized_answers=[x*9+y/10 for x,y in zip(bmw,finalized_values[0:-1])]
        for coco in finalized_answers:
            coca=abs(coco)
            atr_values.append(coca)


        for index,his_,in enumerate(atr_values):
            main_data[index+1]['ATR']=abs(his_)



        ############ +DM    & -DM  ############

        plus_dm_results=[x-y for x,y in zip(master_high_prices[1:],master_high_prices[0:-1])]
        negative_dm_results=[x-y for x,y  in zip(master_low_prices[1:],master_low_prices[0:-1])]
        for val,vals in zip(plus_dm_results,negative_dm_results):
            if val>vals:
                plus_dm.append(val)
                negative_dm.append(0)
            elif val<vals:
                negative_dm.append(vals)
                plus_dm.append(0)
            elif val==vals:
                negative_dm.append(0)
                plus_dm.append(0)

        ############## +DI AND -DI #######

        

        plus_di_values=[100*(x/y) for x,y in zip(plus_dm,atr_values)]
        negative_di_values=[100*(x/y)for x,y in zip(negative_dm,atr_values)]



        #########  DX  ######

        dx_values=[x-y  for x,y in zip(plus_di_values,negative_di_values)]
        print(dx_values)




        




        










        
        

        




          
        




        with open(r"C:\Users\dasho\divergence_test.json",'w') as ws:
            json.dump(main_data,ws,indent=4)


        


        


        


        

        





            

        



        



            
            


















        



        



        


            
        





        




        


            


            




k=KELTNER_ALGO()
k.opening_the_main_data()
k.analyzing_the_data()