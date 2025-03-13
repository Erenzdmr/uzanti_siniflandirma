# Dosyaları Uzantılara Göre Sınıflandırma

import os

def duzenle():
    klasor = input("düzenleneecek klasör : ")
    dosyalar = []     #Dosaylar depolanacak
    uzantilar = []    #Uzantılar depolanacak  
    
    def list_dir():
        for dosya in os.listdir(klasor):     #icerigini gosterecek     
            if os.path.isdir(os.path.join(klasor,dosya)):   #klasör olup olmadığı 
                continue
            if dosya.startswith("."):        #Dosyamız gizlimi
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
    
    # Uzntılarını almak
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        if uzanti in uzantilar:            #Uzantı daha önce eklendi mi
            continue
        else:
            uzantilar.append(uzanti)
    
    for uzanti in uzantilar:              # Klasorler olusturuluyor
        if os.path.isdir(os.path.join(klasor, uzanti)):
            continue
        else :
            os.mkdir(os.path.join(klasor,uzanti))
            
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        os.rename(os.path.join(klasor,dosya),os.path.join(klasor,uzanti,dosya))
        
# if __name__ == "main":
duzenle()
    
        
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
    
