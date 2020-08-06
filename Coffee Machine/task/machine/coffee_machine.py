# # Write your code here
# k = '''Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!'''
# print(k)
print('Write how many cups of coffee you will need:')
num = int(input())

water = num * 200
milk = num * 50
beans = num * 15

print('For 25 cups of coffee you will need:')
print('%d ml of water' % water)
print('%d ml of milk' % milk)
print('%d g of coffee beans' % beans)
