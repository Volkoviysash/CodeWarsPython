import collections

def main():
    source_array = [5, 8, 6, 3, 4]    
    oddnumb = []    
 
    for elmnt in source_array:
        if elmnt%2!=0:            
            oddnumb.append(elmnt)                
    
    ind = 0;
    output = []

    for elmnt in source_array:
        if elmnt%2!=0:        
            output.append(sorted(oddnumb)[ind])
            ind += 1
        else:
            output.append(elmnt)
    
    print(output)

if __name__ == "__main__":
    main()
