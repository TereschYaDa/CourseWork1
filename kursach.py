class Product:
    def __init__(self, storeId, model, manufacturer, guarantee, price):
        self.__storeId = storeId
        self.__model = model
        self.__manufacturer = manufacturer
        self.__guarantee = guarantee
        self.__setPrice(price)

    def __setPrice(self, value):
        self.__price = float('{:.2f}'.format(float(value)))    # better have decimal cents here and convert to .2f during printing out

    def getStoreId(self): return self.__storeId
    def getModel(self): return self.__model
    def getManufacturer(self): return self.__manufacturer
    def getGuarantee(self): return self.__guarantee
    def getPrice(self): return self.__price
    
    def discount(self, share):
        self.__setPrice(self.__price * (1 - share))

class Store:
    def __init__(self, size):
        self.__arr = []
        self._invalidateIterator()
        self.__size = size
        self.__nextId = 0
    
    def getSize(self): return self.__size

    def _invalidateIterator(self):
        self.__i = -1

    def add(self, model, manufacturer, guarantee, price):
        product = Product(self.__nextId, model, manufacturer, guarantee, price)
        self.__arr.append(product)
        self.__nextId += 1
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
        filteredStore = Store(12)
        for i in range(self.getQuantity()):
            if manufacturer.lower() == self.__arr[i].getManufacturer().lower():
                filteredStore.add(self.__arr[i].getModel(), self.__arr[i].getManufacturer(), self.__arr[i].getGuarantee(), self.__arr[i].getPrice())
        return filteredStore

    def discountAll(self, share):
        curIdx = self.__i
        elem = self.getFirstElem()
        while elem != None:
            elem.discount(share)
            elem = self.getNextElem()
        self.__i = curIdx
                    
###################################################################################
'''Functions'''

def processMainMenu():
    print('Выберите задачу:')
    print('0 - Выход из программы')
    print('1 - Вывод всех товаров               4 - Сортировка')
    print('2 - Добавление нового товара         5 - Фильтрация по производителю')
    print('3 - Удаление выбранного товара       6 - Преобразование цен')
    responseForMenu = input()
    return responseForMenu

def createStore():
    store = Store(12)
    store.add('27EA63', 'LG', 12, 35000)
    store.add('BTM2360', 'Philips', 6, 9000)
    store.add('F1', 'Pocophone', 6, 23000)
    store.add('Fen', 'Dyson', 10, 10000)
    store.add('Ryzen 5 5600X', 'AMD', 18, 25000)
    return store

def AppendSpacesRight(string, targetLen): 
    return str(string) + ' ' * (abs(targetLen - len(str(string))) + 3) 

def printTableRow(id, maxLenId, model, maxLenModel, manufacturer, maxLenManufacturer, guarantee, maxLenGuarantee, price, maxLenPrice):
    print(AppendSpacesRight(id, maxLenId) +
          AppendSpacesRight(model, maxLenModel) +
          AppendSpacesRight(manufacturer, maxLenManufacturer) +
          AppendSpacesRight(guarantee, maxLenGuarantee) +
          AppendSpacesRight(price, maxLenPrice))

def printProductsTable(arr):
    idHeader = "ID:"
    modelHeader = 'Модель:'
    manufacturerHeader = 'Производитель:'
    guaranteeHeader = 'Гарантия:'
    priceHeader = 'Цена:'
    maxLenId = len(idHeader) + 1
    maxLenModel = len(modelHeader) + 1
    maxLenManufacturer = len(manufacturerHeader) + 1
    maxLenGuarantee = len(guaranteeHeader) + 1
    maxLenPrice = len(priceHeader) + 1
    elem = arr.getFirstElem()
    while elem != None:
        if maxLenId < len(str(elem.getStoreId())): maxLenId = len(str(elem.getStoreId()))
        if maxLenModel < len(elem.getModel()): maxLenModel = len(elem.getModel())
        if maxLenManufacturer < len(elem.getManufacturer()): maxLenManufacturer = len(elem.getManufacturer())
        if maxLenGuarantee < len(str(elem.getGuarantee())): maxLenGuarantee = len(str(elem.getGuarantee()))
        if maxLenPrice < len(str(elem.getPrice())): maxLenPrice = len(str(elem.getPrice()))
        elem = arr.getNextElem()

    printTableRow(idHeader, maxLenId,
                  modelHeader, maxLenModel,
                  manufacturerHeader, maxLenManufacturer,
                  guaranteeHeader, maxLenGuarantee,
                  priceHeader, maxLenPrice)
    elem = arr.getFirstElem()
    while elem != None:
        printTableRow(elem.getStoreId(), maxLenId,
                      elem.getModel(), maxLenModel,
                      elem.getManufacturer(), maxLenManufacturer,
                      elem.getGuarantee(), maxLenGuarantee,
                      elem.getPrice(), maxLenPrice)
        elem = arr.getNextElem()
    print()

def processAddProductMenu():
    if store.getQuantity() == store.getSize():
        print('В программе не может содержаться больше '+ store.getSize +' товаров!\nЧтобы добавить новый товар, сначала удалите уже имеющийся. Ну или попросите программиста, ответсвенного за выполнение этого задания, чтобы не делал таких дурацких ограничеений :-D')
    else:
        model = input('Введите название модели:\n')
        manufacturer = input('Введите название производителя:\n')
	
    correct = False
    while not correct:
        guarantee = input('Введите время гарантии(в месяцах):\n')
        if guarantee.isdigit() == True: correct = True
        else: print('Введены некорректные данные. Попробуйте еще раз.')

    correct = False
    while not correct:
        price = input('Введите цену:\n')
        if price.isdigit() == True: correct = True
        else: print('Введены некорректные данные. Попробуйте еще раз.')
    store.add(model, manufacturer, guarantee, price)
    
def processDeleteProductMenu():
    correct = False
    while not correct:
        responseForDelete = input('Введите ID товара, который хотите удалить:\n')
        if store.deleteElem(responseForDelete) != True: print('Неправильный ввод.')
        else: correct = True
    store.deleteElem(responseForDelete)

def processSortMenu():
    correct = False
    while not correct:
        prop = input('Введите свойство товара, по которому хотите осуществить сортировку (модель, производитель, гарантия, цена):\n')
        if store.sortBy(prop.lower()) != True: print('Неправильный ввод.')
        else: correct = True
    store.sortBy(prop)

def processFilterProductsMenu():
    manufacturer = input('Введите производителя товара, по которому хотите осуществить фильрацию:\n')
    filteredStore = store.filterByManufacturer(manufacturer) 
    if filteredStore.getQuantity() == 0:
        print('Товары производителя ' + manufacturer + ' отсутствуют\n')
    else:
        printProductsTable(filteredStore)

def processDiscountProductsMenu():
    share = input('Введите процент, на который хотите снизить цену всех товаров:\n')
    if share.isdigit():
        share = int(share)
        share /= 100
        store.discountAll(share)
    else:
        print('Неправильный ввод.')
        processDiscountProductsMenu()

###################################################################################
'''Executing code'''

store = createStore()
responseForMenu = ''
print('Вас приветствует приложение "Магазин бытовой техники"\n')
while responseForMenu != '0':
    responseForMenu = processMainMenu()
    if responseForMenu == '1':
        if store.getQuantity() > 0:
            printProductsTable(store)
        else:
            print('Нет товаров')
    elif responseForMenu == '2': processAddProductMenu()
    elif responseForMenu == '3':
        printProductsTable(store)
        processDeleteProductMenu()
    elif responseForMenu == '4': processSortMenu()
    elif responseForMenu == '5': processFilterProductsMenu()
    elif responseForMenu == '6': processDiscountProductsMenu()
    elif responseForMenu == '0': print('До свидания!')
    else: print('Вероятно, ввод был выполнен неправильно. Попробуйте еще раз:')
    






