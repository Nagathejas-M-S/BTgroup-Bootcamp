class Cache:
    _MAX_CAPACITY = 0

    """
    Static method to get the maximum capacity of the cache
    """
    @staticmethod
    def get_max_capacity():
        if Cache._MAX_CAPACITY == 0:
            while True:
                try:
                    print("Please enter the Max Capacity of the Cache:")
                    value = int(input())
                    if value > 0:
                        Cache._MAX_CAPACITY = value
                        break
                    else:
                        print("Please enter a positive integer.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        print("Returning MAX_CAPACITY")
        return Cache._MAX_CAPACITY
