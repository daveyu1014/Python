
import csv,os        

class item_shop():
    shop='商品庫存'
    
    def __init__(self,shop):
        self.items={}
        self.name=shop

    def menu(self):
        print('{:*^20}'.format(f'{self.name}管理程式'))
        print('{:^20}'.format('(1).新增品項'))
        print('{:^20}'.format('(2).刪除品項'))
        print('{:^20}'.format('(3).修改品項'))
        print('{:^20}'.format('(4).目前品項'))
        print('{:^20}'.format('(5).儲存檔案'))
        print('{:^20}'.format('(6).離開'))
        print('{:*^20}'.format(f'{self.name}管理程式'))
    
    def exit_app(self):
        global shop    
        print(f'離開{self.name}管理程式')
        
    
    # 新增品項
    def add(self):
        while True:
            item=input('請輸入新品項(q:exit)')
            if item.lower()=='q':
                break
            
            if item in shopItem:
                if input('已有該品項，是否修改價格(y/n)').lower()=='y':
                    shop.update(item)
            else:   
                while True:
                    try:
                        price=eval(input('請輸入價格:'))
                        shopItem[item]=price
                        break
                    except:
                        print('價格輸入錯誤!')
            
        shop.view()
        
    
    def delete(self):
        item=input('請輸入刪除品項:')
        if item not in shopItem:
            print('無此品項')
            return 
        
        if input(f'確定要刪除{item}品項(y/n)').lower()=='y':            
            del shopItem[item]                    
            print(f'{item}商品刪除完成')     
    
    def update(item=None):
        if item!=None:    
            item=input('請輸入修改品項:')
            
        if item not in shopItem:
            print('無此品項')
            return    
        
        price=float(input('請輸入新價格:'))
        oldPrice=shopItem[item] 
        shopItem[item]=price
        
        print(f'{item}商品修改完成 {oldPrice}==>{price}')
    
    def view(self):
        if len(shopItem)==0:
            print('目前資料為空，請先新增資料....')                               
            return 
                   
        for name,price in shopItem.items():
            print(f'{name}={price}',end='\t') 

shop=item_shop('商品庫存')
shopItem={}
fileName='items.csv'

if os.path.exists(fileName):
    with open(fileName,'r',encoding='utf-8-sig') as f:
        datas=list(csv.reader(f))
        #print(datas)
        for data in datas:
            shopItem[data[0]]=int(data[1])            

while True:
    shop.menu()
        
    select=input('請輸入選擇:')
    
    if select=='6':
        shop.exit_app()
        break
    
    elif select=='5':        
        with open(fileName,'w',newline='',encoding='utf-8-sig') as f:
            writer=csv.writer(f)            
            #print(shopItem.items())
            writer.writerows(shopItem.items())
            
        print('檔案儲存成功!')
    
    # 新增品項
    elif select=='1':
        shop.add()
   
    # 檢視資料
    elif select=='4':        
        shop.view()
    
    # 修改品項
    elif select=='3':
        shop.update()
        
    # 刪除品項
    elif select=='2':
       shop.delete()      
       
    else:
        print('輸入錯誤!')
        input('請按Enter繼續...')
        continue
    
    input('請按Enter繼續...')  
    
        
   




