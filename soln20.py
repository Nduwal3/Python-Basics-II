# Write a Python class to find the three elements that sum to zero 
# from a list of n real numbers. Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]] 

class SumZero:
    result_list = []
    def __init__(self, list_of_real_num):
        self.list_of_real_num = list_of_real_num

    def get_numbers_sum_to_zero(self):
        sorted_list = sorted(self.list_of_real_num) 
        array_len = len(sorted_list)          
        for i in range(array_len):
            for j in range(i+1, array_len):
                for k in range(j+1, array_len):
                    if sorted_list[i] + sorted_list[j] + sorted_list[k] == 0 :
                        self.result_list.append([sorted_list[i], sorted_list[j] , sorted_list[k]])
                    else:
                        continue
        print(self.result_list)


    
list_of_numbers = SumZero([-25, -10, -7, -3, 2, 4, 8, 10])
list_of_numbers.get_numbers_sum_to_zero()
