# week 10
import time
# arr = [64, 18, ]
#
# for i in range (len(arr())):
#     print(arr[i])
#
#     for j in range (len(arr()-1)):
#         print(arr[j], j)

def bubbleSort(arr):

    ## swap işini bir for içerisinde yapabilirsek direkt 100 vercekmiş hoca. öyle dedi. çünkü öyle yapılmıyomuş, imkansızmış.
    # hoca imkansız falan demedi de, ben öyle dedim. o dedi diye dedim diye yazıyordum ki ingilizce açıklarken
    # "its impossible" dedi vallaha :d
    # ğğ
    # sinirim bozuk
    ## swap işlemini adımız gibi bilmeliymişiz, ayn knk

    n = len(arr)
    for i in range (n):
        swapped = False ### bu olmasa da olur ama bubble sort algoritmasını iyileştirmek için bunu kullanıyoruz
        # ama kapa çeneni artık ya aaaa -hocaya değil, derse hocayı dinlemeye geldik zaten-

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break

def bubblesort2(arr):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                swapped = True
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp




ar1 = [12, 15, 14, 6, 3]
print(ar1)
t1 = time.time()
bubblesort2(ar1)
t2 = time.time()
print(ar1)
print(t2-t1)


## yorum satırlarına laf edenlerin kafasına sazla, bağlamayla, kemençeyle, kopuzla vurup kafalarında kırasım var