class singleton:
    """ simple singleton implementation"""
    _instance=None
    
    def __new__(cls):
        #if no instance exists create one.
        if cls._instance is None :
            cls._instance=super().__new__(cls)
        return cls._instance
        
ob1=singleton()
ob2=singleton()
if (ob1 is ob2):
    print("both objects are the same instance.")
    