
# a = [ 1, 2, 3, 5, 6, 7, 8, 10]
#    find_N_missing_number(a, 10)
def find_N_missing_number(data, total):    
    if isinstance(data, list):
        x = [0] * total
        for d in data: x[d-1] = 1        
        for (index, val) in enumerate(x, start=1):            
            if val == 0: print(index)
            #print(index, val)
        
        #d = list(filter(lambda z: z==0, x))
        #print(d)

if __name__ == "__main__":
    a = [ 1, 2, 3, 5, 6, 7, 8, 10]
    find_N_missing_number(a, 10)
