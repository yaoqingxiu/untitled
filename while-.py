print("We have sold all pastrami sandwiches")
sandwich_orders = ['火腿三明治', 'pastrami sandwiches', '猪肉三明治', '芝士三明治', 'pastrami sandwiches', '普通牛肉三明治']
finished_sandwiches = []
while 'pastrami sandwiches' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwiches')
print('\n修改过后的三明治菜单：')
print(sandwich_orders)
print('\n')
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your "+sandwich_order+".")
    finished_sandwiches.append(sandwich_order)
print(finished_sandwiches)

aa = True
ad = []
while aa == True:
    pr = "If you could visit one place in the world, where would you go?"
    pr += "\nIf you input the places all you want to go,please input 'quit':"
    pp = input(pr)
    if pp == 'quit':
        aa = False
    else:
        ad.append(pp)
print("人们最想去的地方总集：")
print(ad)