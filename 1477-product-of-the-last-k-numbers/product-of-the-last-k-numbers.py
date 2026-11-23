class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 to act as a neutral multiplier for prefix products
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Any product including this zero will be 0, so reset the stream
            self.prefix = [1]
        else:
            # Multiply the new number by the running product
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is greater than or equal to the length of prefix, 
        # a zero occurred within the last k elements
        if k >= len(self.prefix):
            return 0
        
        # Divide the total running product by the product before the last k elements
        return self.prefix[-1] // self.prefix[-1 - k]