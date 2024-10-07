class ProductManager():
    def __init__(self, file) -> None:
        self.file = file
        fh = open(self.file, 'r')
        self.products = fh.read().split('\n')
        fh.close()

    def printProducts(self):
        print('-'*40)
        print(f'{'ID'.center(10, ' ')}{'Name'.center(20, ' ')}{'Price'.center(10, ' ')}')
        print('-'*40)

        for product in self.products:
            product = product.split(',')
            print(f'{product[0].center(10, ' ')}{product[1].center(20, ' ')}{product[2].center(10, ' ')}')
        
        print('-'*40)

    def writeProducts(self):
        fh = open(self.file, 'w')
        for product in self.products[:-1]:
            fh.write(product+'\n')
        fh.write(self.products[-1])
        fh.close()
        print('Inventory updated')

    def sellProducts(self):
        self.printProducts()

        id = int(input('Enter product id: ')) - 1
        if (id >= len(self.products)):
            print('Product with given id is not available')
            return
        
        qty = int(input('Enter quantity: '))
        product = self.products[id].split(',')
        pqty = int(product[3])
        if (qty > pqty):
            print(f'Sorry, we only have {pqty} items in stock')
            inp = input(f'Do you want to buy only {pqty} items?').lower()
            
            while(inp not in ['yes', 'y', 'no', 'n']):
                inp = input('Please enter valid input')
            
            if (inp in ['n', 'no']):
                print('Thank you for visiting')
                print('Please come again')
                return

            qty = pqty

        self.generateBill(id, qty)

    def generateBill(self, id, qty):
        print('-'*40)
        product = self.products[id].split(',')
        print(f'{product[1]}\t{qty} * {product[2]}\t=\t{qty*int(product[2])}')
        print('-'*40)

        product = f'{product[0]},{product[1]},{product[2]},{int(product[3])-qty}'
        self.products[id] = product
        self.writeProducts()

class SalesManager():
    def __init__(self, file) -> None:
        self.file = file
        self.manager = ProductManager(file)

    def start(self):
        flag = True
        while flag:
            self.manager.sellProducts()

            in_val = input('\nDo you want to buy anything else? (y/n): ')
            if in_val != 'y':
                flag = False
                print('Please visit again')
