def main():
   print("welcome")
   not1=int(input("please enter the number of trees :"))
   tree_price =int(input("please enter the price : "))
   the_cost = int(not1) * int(tree_price)
   crop_price = int(input("please enter the crop price : "))
   PP = int(crop_price) / 10
   fst_h = 2 * int(not1)
   Sec_h = 3 * int(not1)
   third_h = 4 * int(not1)
   fourth_h = 5 * int(not1)
   fst_hp = int(fst_h) * PP
   Sec_hp = int(Sec_h) * PP
   third_hp = int(third_h) * PP
   fourth_hp = int(fourth_h) * PP
   the_total = int(fst_hp) + int(Sec_hp) + int(third_hp) + int(fourth_hp)
   net_profit = int(the_total) - int(the_cost)   
  
  
   print("  ")
   print("The number of trees : {}" .format(int(not1)) )
   print("The price of one tree : {}" .format(int(tree_price)) )
   print("The Crop price : {} ".format(int(crop_price)) )
   print("The first harvest : {} ".format(int(fst_h)) ) 
   print("The price is : {} " .format(int(fst_hp)) )
   print("The Second harvest : {} " .format(int(Sec_h)) )
   print("The price is : {} " .format(int(Sec_hp)) )
   print("The Third harvest : {} " .format(int(third_h)) )
   print("The price is : {} " .format(int(third_hp)) )
   print("The Fourth harvest : {} " .format(int(fourth_h)) )
   print("The price is : {} " .format(int(fourth_hp)) )
   print("The total : {} ".format(int(the_total)) )
   print("The cost : {} ".format(int(the_cost)) )
   print("The net_profit : {} ".format(int(net_profit)) )
   print(PP)
if __name__ == '__main__':main()