import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisini oluşturunuz

numbers1 = np.array([10,15,30,45,60])


# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz

numbers1 = np.arange(0,15)


# 3- (50-100) arasında 5'er 5'er artacak şekilde numpy dizisi oluştur

numbers1 = np.arange(50,100,5)


# 4- 10 elemanlı sıfırlardan ve birlerden oluşan iki dizi oluştur

numbers1 = np.zeros(10)
numbers1 = np.ones(10)


# 5- (0-100) arasında eşit aralıklı 5 sayı üretin.

numbers1 = np.linspace(0,100,5)


# 6- (10-30) arasında rastgele 5 tane tamsayı üretin.

numbers1 = np.random.randint(10,30,5)


# 7- [-1 ile 1] arasında 10 adet sayı üretin.

numbers1 = np.random.randn(10)


# 8- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturun.

numbers3 = np.random.randint(10,50,15).reshape(3,5)


# 9- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız

numbers2 = numbers3.sum(axis=0)
numbers2 = numbers3.sum(axis=1)


# 10- Üretilen matrisin en büyük,en küçük ve ortalama değerlerini  bulunuz.

# print(numbers1)

# numbers1 = numbers1.max()
# numbers1 = numbers1.min()
# numbers1 = numbers1.mean()


# 11- Üretilen matrisin en büyük değerinin indeksini bulunuz.

# numbers1 = numbers1.argmax()


# 12- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

np_array = np.arange(10,20)
numbers1 = np_array[:3]


# 13- Üretilen dizinin elemanlarını tersten yazınız.

numbers1 = np_array[::-1]


# 14- Üretilen matrisin ilk satırını seçiniz.

print(numbers3)

numbers1 = numbers3[0]


# 15- Üretilen matrisin 2.satır ve 3.sütundaki elemanını bulunuz.

numbers1 = numbers3[2,3]

numbers1 = numbers3[1,(1,3)]   # 1.satırdaki 1. ve 3. elemanı al.


# 16- Üretilen matrisin tüm satırlardaki ilk elemanları seçiniz.

numbers1 = numbers3[:,0]


# 17- Üretilen matrisin her bir elemanının karesini alınız.

numbers1 = numbers3**2


# 18- Üretilen matris elemanlarının hangisi pozitif çitf sayıdır..

numbers1 = numbers3[numbers3 % 2 == 0]


# print(numbers2)
print(numbers1)



# np.full((4,5),5)   # 4'e 5'lik matrisin içinin hepsi 5 olan matris

# np.full(2,3)    # [3,3]


# np.eye(3,4)           # Birim matris oluşturma


# numbers1 = np.zeros(2,3,5)       # 2 tane 3'e 5'lik matris verir
                                   # numbers1.ndim -> kaç boyutlu olduğunu verir
                                   # numbers1.size -> kaç elemanlı olduğunu verir