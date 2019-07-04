# 选择排序
# 班级：数字媒体技术夏季班 学号：17321140032 姓名：徐博昱 题目：第二题
import sys 

Array = [62, 40 ,65, 71, 15, 87, 22, 53] 

def select(arr):
    for i in range(len(arr)): 
          
       
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                    
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    return arr

arrary_2 = select(Array)
print(arrary_2)