class Bike:
    compose = ['frame','wheel','pedal']
    def __init__(self):
        self.other = 'Bike'
        print("bike init method {}".format(self.other))
    def use(self,time):
        print('you ride {} m '.format(time*100))
class Share_Bike(Bike):
    sharebike = "share_name"
    def __init__(self):
        self.other = 'share_bike'
        print("Share_Bike init method {}".format(self.other))
    def cost(self,hour):
        print('you spend {}'.format(hour*2))
my_bike = Bike()
print(my_bike.other)
bike = Share_Bike()
print('---------')
print(bike.other)
print('doc={}'.format(Share_Bike.__doc__))
print('name={}'.format(Share_Bike.__name__))
print('module={}'.format(Share_Bike.__module__))
print('base={}'.format(Share_Bike.__bases__))