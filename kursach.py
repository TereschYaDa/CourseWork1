class Product:
    def __init__(self, storeId, model, manufacturer, guarantee, price):
        self.__storeId = storeId
        self.__model = model
        self.__manufacturer = manufacturer
        self.__guarantee = guarantee
        self.__setPrice(price)

    def __setPrice(self, value):
        self.__price = float('{:.2f}'.format(float(value)))

    def getStoreId(self): return self.__storeId
    def getModel(self): return self.__model
    def getManufacturer(self): return self.__manufacturer
    def getGuarantee(self): return self.__guarantee
    def getPrice(self): return self.__price
    
    def changePrice(self, share):
        self.__setPrice(self.__price * (1 - share))

class Store:
    def __init__(self):
        self.__arr = []
        self._invalidateIterator()
        self.__nextId = 0

    def _invalidateIterator(self):
        self.__i = -1

    def add(self, model, manufacturer, guarantee, price):
        product = Product(self.__nextId, model, manufacturer, guarantee, price)
        self.__nextId += 1
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
        for i in range(self.getQuantity()):
            if str(self.__arr[i].getStoreId()) == id:
                self.__arr.pop(i)
                self._invalidateIterator()
                return True
        return False
             
    def sortBy(self, prop):
        if prop == 'модель':
            self.__arr.sort(key=lambda product: product.getModel())
            return True
        elif prop == 'производитель':
            self.__arr.sort(key=lambda product: product.getManufacturer())
            return True
        elif prop == 'гарантия':
            self.__arr.sort(key=lambda product: product.getGuarantee())
            return True
        elif prop == 'цена':
            self.__arr.sort(key=lambda product: product.getPrice())
            return True
        else: 
            return False

    def filterByManufacturer(self, manufacturer):
        filteredStore = Store()
        for i in range(store.getQuantity):
            if manufacturer.lower() == self.__arr[i].getManufacturer().lower():
                filteredStore.add(self.__arr[i])
        return filteredStore

    def changeAllPrices(self, share):
        curIdx = self.__i
        elem = self.getFirstElem()
        while elem != None:
            elem.changePrice(share)
            elem = self.getNextElem()
        self.__i = curIdx
                    
###################################################################################
'''Functions'''

def printSelectionMenu():
    print('Выберите задачу:')
    print('0 - Выход из программы')
    print('1 - Вывод всех товаров               4 - Сортировка')
    print('2 - Добавление нового товара         5 - Фильтрация по производителю')
    print('3 - Удаление выбранного товара       6 - Преобразование цен')

def instantiation():
    store.add('27EA63', 'LG', 12, 35000)
    store.add('BTM2360', 'Philips', 6, 9000)
    store.add('F1', 'Pocophone', 6, 23000)
    store.add('Fen', 'Dyson', 10, 10000)
    store.add('Ryzen 5 5600X', 'AMD', 18, 25000)

def AppendSpacesRight(string, targetLen): 
    return str(string) + ' ' * (abs(targetLen - len(str(string))) + 3) 

def printTableRow(id, model, maxLenModel, manufacturer, maxLenManufacturer, guarantee, maxLenGuarantee, price, maxLenPrice):
    print(' ' + id + '  ' + AppendSpacesRight(model, maxLenModel) + AppendSpacesRight(manufacturer, maxLenManufacturer) + AppendSpacesRight(guarantee, maxLenGuarantee) + AppendSpacesRight(price, maxLenPrice))

def printProductsTable(arr):
    modelHeader = 'Модель:'
    manufacturerHeader = 'Производитель:'
    guaranteeHeader = 'Гарантия:'
    priceHeader = 'Цена:'
    maxLenModel = len(modelHeader) + 1
    maxLenManufacturer = len(manufacturerHeader) + 1
    maxLenGuarantee = len(guaranteeHeader) + 1
    maxLenPrice = len(priceHeader) + 1
    elem = arr.getFirstElem()
    while elem != None:
        if maxLenModel < len(elem.getModel()): maxLenModel = len(elem.getModel())
        if maxLenManufacturer < len(elem.getManufacturer()): maxLenManufacturer = len(elem.getManufacturer())
        if maxLenGuarantee < len(str(elem.getGuarantee())): maxLenGuarantee = len(str(elem.getGuarantee()))
        if maxLenPrice < len(str(elem.getPrice())): maxLenPrice = len(str(elem.getPrice()))
        elem = arr.getNextElem()

    printTableRow('ID:',
                    modelHeader, maxLenModel,
                    manufacturerHeader, maxLenManufacturer,
                    guaranteeHeader, maxLenGuarantee,
                    priceHeader, maxLenPrice)
    elem = arr.getFirstElem()
    while elem != None:
        printTableRow(elem.getStoreId(),
                      elem.getModel(), maxLenModel,
                      elem.getManufacturer(), maxLenManufacturer,
                      elem.getGuarantee(), maxLenGuarantee,
                      elem.getPrice(), maxLenPrice)
        elem = arr.getNextElem()
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
        
        store.add(model, manufacturer, guarantee, price)
    
def processDeleteProduct():
    responseForDelete = input('Введите ID товара, который хотите удалить:\n')
    while store.deleteElem(responseForDelete) != True:
        print('Неправильный ввод.')
        responseForDelete = input('Введите ID товара, который хотите удалить:\n')

def processSort():
    prop = input('Введите свойство товара, по которому хотите осуществить сортировку (модель, производитель, гарантия, цена):\n')
    while store.sortBy(prop.lower()) != True:
        print('Неправильный ввод.')
        prop = input('Введите свойство товара, по которому хотите осуществить сортировку (модель, производитель, гарантия, цена):\n')

def processFilt():
    manufacturer = input('Введите производителя товара, по которому хотите осуществить фильрацию:\n')
    if not store.filterByManufacturer(manufacturer):
        print('Товары производителя ' + manufacturer + ' отсутствуют\n')
    else:
        printProductsTable(store.filterByManufacturer(manufacturer))

def processChangePrice():
    share = input('Введите процент, на который хотите снизить цену всех товаров:\n')
    if share.isdigit():
        share = int(share)
        share /= 100
        store.changeAllPrices(share)
    else:
        print('Неправильный ввод.')
        processChangePrice()

###################################################################################
'''Executing code'''

store = Store()
instantiation()
responseForMenu = ''
print('Вас приветствует приложение "Магазин бытовой техники"\n')
while responseForMenu != '0':
    printSelectionMenu()
    responseForMenu = input()
    if responseForMenu == '1':
        if store.getQuantity() > 0:
            printProductsTable(store)
        else:
            print('Нет товаров')
    elif responseForMenu == '2': processAddProduct()
    elif responseForMenu == '3':
        printProductsTable(store)
        processDeleteProduct()
    elif responseForMenu == '4': processSort()
    elif responseForMenu == '5':
        processFilt()
    elif responseForMenu == '6': processChangePrice()
    elif responseForMenu == '0': print('До свидания!')
    else: print('Вероятно, ввод был выполнен неправильно. Попробуйте еще раз:')
    






