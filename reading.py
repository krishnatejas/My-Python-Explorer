flag = False
with open("D:\python_ESI_sriram\T_MULTI.prj",'r') as f:
    for line in f.readlines():
        line = line.split('\n')
        if 'WELDLINES' in line:
            flag = True

print(flag)
            
        
    
    
