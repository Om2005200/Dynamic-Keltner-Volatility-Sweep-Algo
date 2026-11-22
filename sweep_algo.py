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
        #print(len(main_data))
        master_closing_prices=[]
        bmw=[]
        master_dx=[]
        initialized_dx=[]
        main_vol_1=[]
        master_vwap_data=[]
        ema_master=[]


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
        master_volume_data=[]
        vma_master=[]
       

        sma_200_list=[]
        
        for datas in main_data:
            closing_prices=datas['CLOSE']
            opening_prices=datas['OPEN']
            high_prices=datas['HIGH']
            low_prices=datas['LOW']

            date_data=datas['DATE']
            time_data=datas['TIME']
            volume_data=datas['VOLUME_DATA']


            master_closing_prices.append(closing_prices)
            master_opening_prices.append(opening_prices)
            master_high_prices.append(high_prices)
            master_low_prices.append(low_prices)
            master_volume_data.append(volume_data)



        ######### 200 SMA OPERATIONS ########
        if len(master_closing_prices)<200:
            #print('NOT ENOUGH DATA')
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



        for x,y,z in zip(current_high_current_low,current_low_prev_close,current_high_prev_close):
            maximum_values=max(x,y,z)
            finalized_tr.append(maximum_values)

        for index_,his,in enumerate(finalized_tr):
            main_data[index_+1]['TR']=abs(his)



        for sonam in finalized_tr:
            main_vals=finalized_tr.index(sonam)
            if main_vals not in main_list:
                main_list.append(main_vals)
            if main_vals in main_list:
                main_list_last_value=main_list[-1]
                new_index_value=main_list_last_value+1
                main_list.append(new_index_value)
        original_length=len(finalized_tr)
        new_list_length=len(main_list)
        new_ranger=main_list[0:new_list_length-1]
        main_list.append(new_ranger)

        #print(len(main_list))

        required_indices.extend(new_ranger[:10])
        for new_vals in new_ranger[10:]:
            required_indices.append(new_vals)


        for r,h in zip(new_ranger,required_indices):
            master_values=sum(finalized_tr[r:h])
            finalized_values.append(master_values)



        #########  ATR CALCULATION ##########


        for finals in finalized_tr:
            bmw.append(finals)

        finalized_values.reverse()
        bmw.reverse()
        

    #     finalized_answers=[x*9+y/10 for x,y in zip(bmw,finalized_values)]
    #     #print(len(finalized_answers))
    #     for coco in finalized_answers:
    #         coca=abs(coco)
    #         atr_values.append(coca)


    #     for index,his_,in enumerate(atr_values):
    #         main_data[index+1]['ATR']=abs(his_)


        

    #     ############ +DM    & -DM  ############

    #     plus_dm_results=[x-y for x,y in zip(master_high_prices[1:],master_high_prices[0:-1])]
    #     negative_dm_results=[x-y for x,y  in zip(master_low_prices[1:],master_low_prices[0:-1])]
    #     for val,vals in zip(plus_dm_results,negative_dm_results):
    #         if val>vals:
    #             plus_dm.append(val)
    #             negative_dm.append(0)
    #         elif val<vals:
    #             negative_dm.append(vals)
    #             plus_dm.append(0)
    #         elif val==vals:
    #             negative_dm.append(0)
    #             plus_dm.append(0)

    #     ############## +DI AND -DI #######





    #     plus_di_values=[100*(x/y) if y!=0 else 0 for x,y in zip(plus_dm,atr_values)]

    #     negative_di_values=[100*(x/y) if y!=0 else 0 for x,y in zip(negative_dm,atr_values)]

        
                
    #     # plus_di_values=[100*(x/y) for x,y in zip(plus_dm,atr_values)]
    #     # negative_di_values=[100*(x/y)for x,y in zip(negative_dm,atr_values)]



    #     ########  DX  ######

    #     dx_values=[x-y  for x,y in zip(plus_di_values,negative_di_values)]
    #     master_dx.append(dx_values)
       




    #     ##### INTIALIZED ADX VALUES #####


    #     for initialized_values in dx_values[:14]:
    #         initialized_dx__=initialized_values
    #         lk.append(initialized_dx__)


        

    #     basic_values=sum(lk)/14
    #     initialized_dx.append(basic_values)
      

    #     ######## ADX CALCULATION #####

        



    #     for jk in dx_values[14:]:
    #         for adx in initialized_dx:
    #             main_values=((adx * 13) + jk) / 14
    #         initialized_dx.append(main_values)

        

    #     for i,hs,in enumerate(initialized_dx):
    #         main_data[i+14]['ADX']=abs(hs)



    #     #### VWAP CALCULATION #####
    #     for ki in master_volume_data:
    #         main_m=master_volume_data.index(ki)

    #         if main_m not in main_vol_1:
    #             main_vol_1.append(main_m)
    #         if main_m in main_vol_1:
    #             main_list_values=main_vol_1[-1]

    #             new_index_pro=main_list_values+1
    #             main_vol_1.append(new_index_pro)

    #     for gulu in main_vol_1[2:]:
    #         minus_data=gulu-20
    #         main_values_main=sum(master_volume_data[minus_data:gulu])/20
    #         master_vwap_data.append(main_values_main)

    #     for ci,ct,in enumerate(master_vwap_data[:len(main_data)-19]):
    #         main_data[ci+19]['VWAP']=abs(ct)



    #     ##########  20 EMA ################

    #     master_closing_prices_data=sum(master_closing_prices[:20])//20
    #     main_value_data=master_closing_prices_data
    #     ema_master.append(main_value_data)
    #     multiplier=0.095238
    #     for james in master_closing_prices[19:]:
    #         for bond in ema_master:
    #             main_value_list=(james-bond)*multiplier+bond
    #         ema_master.append(main_value_list)

        
    #     for ici,ict,in enumerate(ema_master[:len(main_data)-19]):
    #         main_data[ici+19]['EMA_20']=abs(ict)


    #     #######  20 VMA ###########

    #     master_volume_data_values=sum(master_volume_data[:20])//20
    #     main_volume_data=master_volume_data_values
    #     vma_master.append(main_volume_data)
    #     for pat in master_volume_data[19:]:
    #         for son in vma_master:
    #             main_vol_list=(pat-son)+son
    #         vma_master.append(main_vol_list)

    #     for tc,jh in enumerate(vma_master[:len(main_data)-19]):
    #         main_data[tc+19]['VMA_20']=abs(jh)







        
        


            
    #     #new_ranger_data

    #     with open(r"C:\Users\dasho\divergence_test.json",'w') as ws:
    #         json.dump(main_data,ws,indent=4)






    # def taking_the_live_positions(self):
    #     main_data=self.opening_the_main_data()
    #     master_close_values=[]
    #     master_open_values=[]
    #     master_vwap_values=[]
    #     master_adx_values=[]
    #     master_vol_values=[]
    #     master_ema_values=[]
    #     master_atr_values=[]
    #     upper_band_data=[]
    #     lower_band_data=[]
    #     time_master_data=[]
    #     date_master_data=[]
    #     vma_master_data=[]


        
    
    #     for datas in main_data:
    #         closing_prices=datas['CLOSE']
    #         opening_prices=datas['OPEN']
    #         adx_values=datas['ADX']
    #         vol_values=datas['VOLUME_DATA']
    #         vwap_values=datas['VWAP']
    #         ema_values=datas['EMA_20']
    #         atr_values=datas['ATR']
    #         time_data=datas['TIME']
    #         date_data=datas['DATE']
    #         vma_data=datas['VMA_20']


    #         master_close_values.append(closing_prices)
    #         master_open_values.append(opening_prices)
    #         master_vwap_values.append(vwap_values)
    #         master_atr_values.append(atr_values)
    #         master_adx_values.append(adx_values)
    #         master_vol_values.append(vol_values)
    #         master_ema_values.append(ema_values)
    #         time_master_data.append(time_data)
    #         vma_master_data.append(vma_data)



    #         if date_data not in date_master_data:
    #             date_master_data.append(date_data)


        
    #     upper_band=[a+(2*b) for a,b in zip(master_ema_values,master_atr_values)]
    #     #upper_band_data.append(upper_band)

    #     lower_band=[a-(2*b) for a,b in zip(master_ema_values,master_atr_values)]
    #     #lower_band_data.append(lower_band)

    #     original_closing_price=master_close_values[-1]
    #     current_date_data=date_master_data[-1]
    #     current_time_data=time_master_data[-1]
    #     current_upper_band_data=upper_band[-1]
    #     print(current_upper_band_data)
        
    #     current_lower_band_data=lower_band[-1]
    #     print(current_lower_band_data)
    #     current_vma_value=vma_master_data[-1]


    #     for data in main_data:
    #         main_closing_price=data['CLOSE']
    #         main_opening_price=data['OPEN']
    #         main_date_data=data['DATE']
    #         main_time_data=data['TIME']
    #         main_vwap=data['VWAP']
    #         main_adx=data['ADX']
    #         main_vol=data['VOLUME_DATA']

    #         if main_closing_price==original_closing_price:
    #             if main_date_data==current_date_data:
    #                 if main_time_data==current_time_data:



                        
    #                     if main_closing_price>main_opening_price:


    #                         if main_closing_price>current_upper_band_data:
    #                             if main_closing_price>main_vwap:
    #                                 if 

                               











                            
















            







        
            





        


        


        


        

        





            

        



        



            
            


















        



        



        


            
        





        




        


            


            




k=KELTNER_ALGO()
k.opening_the_main_data()
k.analyzing_the_data()


k.taking_the_live_positions()