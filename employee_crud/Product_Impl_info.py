from abc import ABC,abstractmethod

class ProductService(ABC):

    @abstractmethod
    def addProduct(self,prod):
        pass

    @abstractmethod
    def getProduct(self,pid):
        pass

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def deleteProduct(self,pid):
        pass

    @abstractmethod
    def updateProduct(self,prod):
        pass


from employee_crud.Product import db,Product_Info

class ProductImpl(ProductService):

    def addProduct(self, prod):
        db.session.add(prod)
        db.session.commit()
        db.session.remove()
        print('Product Added Successfully....!')

    def getProduct(self, pid):
        prod = Product_Info.query.filter_by(id=pid).first()
        print(prod)
        return prod

    def getAllProducts(self):
        products = Product_Info.query.all()
        print(products)

    def deleteProduct(self, pid):
        dbProduct = self.getProduct(pid)
        db.session.delete(dbProduct)
        db.session.commit()
        print('product deleted successfully...!')

    def updateProduct(self, prod):
        dbProduct = self.getProduct(prod.id)
        dbProduct.name=prod.name
        dbProduct.price=prod.price
        dbProduct.desc=prod.desc
        dbProduct.cat=prod.cat
        dbProduct.qty=prod.qty
        db.session.commit()
        print('Product Updated Successfully...!')

if __name__ == '__main__':
    db.create_all()
    p1 = Product_Info(name="Mobile1", cat="ET", qty=22, price=23943.4, desc="personal use")
    p2 = Product_Info(name="Mobile2", cat="ET", qty=4, price=23943.4, desc="personal use")
    p3 = Product_Info(name="Mobile3", cat="ET", qty=4, price=23943.4, desc="personal use")
    p4 = Product_Info(name="Mobile4", cat="ET", qty=50, price=23943.4, desc="personal use")
    p5 = Product_Info(id=3,name="Mobile5", cat="XX", qty=30, price=23943.4, desc="personal use")

    impl = ProductImpl()
    #impl.addProduct(p1)
    #impl.addProduct(p2)
    #impl.addProduct(p3)
    #impl.addProduct(p4)
    #impl.addProduct(p5)
    impl.deleteProduct(5)


'''
	
	
	1-1
	1-M -- M-1
	M-M
	
	
	PERSON -- ID NM				ADDRESS -- PIN CITY
	
	1-1
	
	
	PID  NAME	PIN						PIN CITY 
	PID  NAME							PIN CITY PID
	PID  NAME			PIN CITY		PID PIN



	1 --M
	
	PID  NAME				PIN CITY  PID
	PID  NAME PIN			PIN CITY  ---- NOT POSSIBLE
	
	
	P -- 1/A     101 pUNE  102 MUMBAI
	
	
	1   A			101	PUNE	1	
					102	MUMBAI	1
					
					
					
	1  A  101
	2  A  102	

'''