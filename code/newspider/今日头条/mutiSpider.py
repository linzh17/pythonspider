from carSpider import carSpider
from entSpider import entSpider
from itSpider import itSpider
from moneySpider import moneySpider
from sportSpider import sp
from travelSpider import travelSpider
from warSpider import warSpider 
from multiprocessing import Pool,Process

def runSpider(n):
    if n == 1:
        print('爬１')
        carSpider.startSpider('carnews')
    elif n == 2:
        print('爬２')
        entSpider.startSpider('entnews')
    elif n == 3:
        itSpider.startSpider('itnews')
    elif n == 4:
        moneySpider.startSpider('moneynews')
    elif n == 5:
        sp.startSpider('sportnews')
    elif n == 6:
        travelSpider.startSpider('travelnews')
    elif n == 7:
        warSpider.startSpider('warnews')
    else:
        pass

if __name__ =='__main__':

    for i in range(1,8):
        p = Process(target=runSpider,args=(i,))
        p.start()
    #p.close()
    #p.join()
    print('结束')