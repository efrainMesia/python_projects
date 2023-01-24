


class AppleBasket():
    
    def __init__(self,color_apple='black',quantity_apple='0') -> None:
        self.color_apple = color_apple
        self.quantity_apple = int(quantity_apple)
    
    def increase(self):
        self.quantity_apple+=1
    
    def __str__(self) -> str:
        return f'A basket of {self.quantity_apple} {self.color_apple} apples'

if __name__=='__main__':
    redApple = AppleBasket('red',1)
    blueApple = AppleBasket('blue',5)
    fruit_baskets = [redApple,blueApple]
    for fruit_basket in fruit_baskets:
        print(fruit_basket)