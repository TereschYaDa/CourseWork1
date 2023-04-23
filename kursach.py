class Product:
    def __init__(self, model, manufacturer, guarantee, price):
        self.__model = model
        self.__manufacturer = manufacturer
        self.__guarantee = guarantee
        self.__price = price

    def getModel(self): return self.__model
    def getManufacturer(self): return self.__manufacturer
    def getGuarantee(self): return self.__guarantee
    def getPrice(self): return float('{:.2f}'.format(float(self.__price)))   # здесь должен быть просто возврат значения. вся конвертация должна производиться при присвоении значения
    
    def changePrice(self, percent): # заменить процент на долю, либо название, либо значение
        self.__price = self.__price * (1 - percent)

    def __setPrice(self, value):
	self.__price = float('{:.2f}'.format(float(value)))

class Array: # переименовать в Store
    def __init__(self):
        self.__arr = []
        self._invalidateIterator()

    def _invalidateIterator(self):
        self.__i = -1

    def add(self, product):
        self.__arr.append(product)
        self._invalidateIterator()
    
    def getQuantity(self): return len(self.__arr)

    def getFirstElem(self):
        if self.__arr:
            self.__i = 0
            return self.__arr[0]
        else:
            return None
        
    def getNextElem(self):
        if self.__i != -1 and self.__i < self.getQuantity() - 1:
            self.__i += 1
            return self.__arr[self.__i]
        else:
            return None
        
    def deleteElem(self, id):
        flag = False # лучше использовать говорящее название: success, elemDeleted и т.п.
        while flag == False:
            if self.__i >= int(id): # сранивать надо с длиной внутреннего массива! внутренний счётчик тут не используется
                self.__arr.pop(int(id))
                self._invalidateIterator() # нужен, так как контейнер поменялся
                flag = True
            else: # Нельзя смешивать ввод с работой "потрохов". Цикл надо уносить наверх. while not store.deleteElem(...): ...
                print('Неправильный ввод.')
                id = input('Введите ID товара, который хотите удалить:\n')
    
    def sortArr(self, prop): # см. предыдущий метод + rename to sortBy
        flag = True
        while flag == True:
            if prop == 'модель':
                self.__arr.sort(key=lambda product: product.getModel())
                flag = False
            elif prop == 'производитель':
                self.__arr.sort(key=lambda product: product.getManufacturer())
                flag = False
            elif prop == 'гарантия':
                self.__arr.sort(key=lambda product: product.getGuarantee())
                flag = False
            elif prop == 'цена':
                self.__arr.sort(key=lambda product: product.getPrice())
                flag = False
            else: 
                print('Неправильный ввод.')
                prop = input('Введите свойство товара из перечисленных: модель, производитель, гарантия, цена\n')

    def filterArr(self, manufacturer): # переименовать в filterByManufacturer
        missed = 0
        for i in range(len(self.__arr)): # getQuantity()
            if manufacturer.lower() == self.__arr[i].getManufacturer().lower():
                filteredStore.add(self.__arr[i]) # ужас ужасный. здесь нужна своя (локальная) переменная и возврат её из метода
            else:
                missed += 1
        if missed == len(self.__arr): return False # а где return True?.. снести всё это нахер
#	else: return True
# or	
#	return True

    def changeAllPrice(self, percent): # rename to changeAllPrices
        for i in range(len(self.__arr)): # getQuantity()
            self.__arr[i].changePrice(percent)

#	curIdx = self.__i
#	elem = self.getFirstElem()
#	while elem != None:
#	    elem.changePrice(percent)
#	    elem = self.getNextElem()
#	self.__i = curIdx

    def clearArr(self): # rename to clear()
        self.__arr.clear() # invalidateIterator() !!!
                    
###################################################################################
'''Functions'''

def printSelectionMenu():
    print('Выберите задачу:')
    print('0 - Выход из программы')
    print('1 - Вывод всех товаров               4 - Сортировка')
    print('2 - Добавление нового товара         5 - Фильтрация по производителю')
    print('3 - Удаление выбранного товара       6 - Преобразование цен')

def returnPartStr(elemget, maxlen): # rename to AppendSpacesRight(str, targetLen)
    return str(elemget) + ' ' * (abs(maxlen - len(str(elemget))) + 3) 

def printAllObjProp(arr): # переименовать в printProductsTable
    i = 0
#   modelHeader = 'Модель:'
#   maxLenModel = len(modelHeader)
#   и далее везде вместо 'Модель:' -- modelHeader !!!
    maxLenModel = 7
    maxLenManufacturer = 14
    maxLenGuarantee = 9
    maxLenPrice = 5
    elem = arr.getFirstElem()
    while elem != None:
        if maxLenModel < len(elem.getModel()): maxLenModel = len(elem.getModel())
        if maxLenManufacturer < len(elem.getManufacturer()): maxLenManufacturer = len(elem.getManufacturer())
        if maxLenGuarantee < len(str(elem.getGuarantee())): maxLenGuarantee = len(str(elem.getGuarantee()))
        if maxLenPrice < len(str(elem.getPrice())): maxLenPrice = len(str(elem.getPrice()))
        elem = arr.getNextElem()

#   этот принт лучше загнать в функцию printTableRow(id, model, ...)
    print('ID:' + ' ' + returnPartStr('Модель:', maxLenModel) + returnPartStr('Производитель:', maxLenManufacturer) + returnPartStr('Гарантия:', maxLenGuarantee) + returnPartStr('Цена:', maxLenPrice))
    elem = arr.getFirstElem()
    while elem != None:
        print(' ' + str(i) + '  ' + returnPartStr(elem.getModel(), maxLenModel) + returnPartStr(elem.getManufacturer(), maxLenManufacturer) + returnPartStr(elem.getGuarantee(), maxLenGuarantee) + returnPartStr(elem.getPrice(), maxLenPrice))
        elem = arr.getNextElem()
        i += 1 # нельзя ни в коем случае! идентификаторы должны возвращаться из Store, а не считаться снаружи
    print()

def processAddProduct():
    if store.getQuantity() == 12:
        print('В программе не может содержаться больше 12 товаров!\nЧтобы добавить новый товар, сначала удалите уже имеющийся. Ну или попросите программиста, ответсвенного за выполнение этого задания, чтобы не делал таких дурацких ограничеений :-D')
    else:
        model = input('Введите название модели:\n')
        manufacturer = input('Введите название производителя:\n')
        guarantee = input('Введите время гарантии(в месяцах):\n')
        f = False
        while f == False:
            if guarantee.isdigit() == False:
                print('Введены некорректные данные. Попробуйте еще раз.')
                guarantee = input('Введите время гарантии(в месяцах):\n')
            else: f = True
        price = input('Введите цену:\n')
        f = False
        while f == False:
            if price.isdigit() == False:
                print('Введены некорректные данные. Попробуйте еще раз.')
                price = input('Введите цену:\n')
            else: f = True
        
        product = Product(model, manufacturer, guarantee, price)
        store.add(product)
    
def processDeleteProduct():
    responseForDelete = input('Введите ID товара, который хотите удалить:\n')
    store.deleteElem(responseForDelete)

def processSort():
    prop = input('Введите свойство товара, по которому хотите осуществить сортировку (модель, производитель, гарантия, цена):\n')
    store.sortArr(prop.lower())

def processFilt():
    manufacturer = input('Введите производителя товара, по которому хотите осуществить фильрацию:\n')
    if store.filterArr(manufacturer) == False:
        print('Товары производителя ' + manufacturer + ' отсутствуют\n')
    else:
        printAllObjProp(filteredStore)

def processChangePrice():
    percent = input('Введите процент, на который хотите снизить цену всех товаров:\n')
    if percent.isdigit():
        percent = int(percent)
        percent /= 100
        store.changeAllPrice(percent)
    else:
        print('Неправильный ввод.')
        processChangePrice()

###################################################################################
'''Executing code'''

store = Array()
filteredStore = Array() # already noted
# better move to function Init()
choto0 = Product('27EA63', 'LG', 12, 35000)
choto1 = Product('BTM2360', 'Philips', 6, 9000)
choto2 = Product('F1', 'Pocophone', 6, 23000)
choto3 = Product('Fen', 'Dyson', 10, 10000)
choto4 = Product('Ryzen 5 5600X', 'AMD', 18, 25000)
store.add(choto0)
store.add(choto1)
store.add(choto2)
store.add(choto3)
store.add(choto4)
# store.add(Product(...))

responseForMenu = ''
print('Вас приветствует приложение "Магазин бытовой техники"\n')
while responseForMenu != '0':
    printSelectionMenu()
    responseForMenu = input()
    if responseForMenu == '1':
        if store.getQuantity() > 0:
            printAllObjProp(store)
        else:
            print('Нет товаров')
    elif responseForMenu == '2': processAddProduct()
    elif responseForMenu == '3':
        printAllObjProp(store)
        processDeleteProduct()
    elif responseForMenu == '4': processSort()
    elif responseForMenu == '5':
        processFilt()
        filteredStore.clearArr()
    elif responseForMenu == '6': processChangePrice()
    elif responseForMenu == '0': print('До свидания!')
    else: print('Вероятно, ввод был выполнен неправильно. Попробуйте еще раз:')
    






