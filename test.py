import pyupbit

access = "noaHpCDsB8CiRrL4z4kvrLzx9dcQUweqotnuCIBy"          
secret = "vEZkSkdLbxJcWvql0jJOSfzJzJI6zIHjLNYI8A7W"         
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW"))     
print(upbit.get_balance("KRW-BORA"))

