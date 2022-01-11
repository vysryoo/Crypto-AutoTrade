import pyupbit

access = "access-key"          
secret = "secret-key"         
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW"))     
print(upbit.get_balance("KRW-BORA"))

