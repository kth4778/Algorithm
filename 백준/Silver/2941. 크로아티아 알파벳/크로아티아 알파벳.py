a=input()
if 'c=' in a:
    a=a.replace('c=','*')    
if 'c-' in a:
    a=a.replace('c-','*')    
if 'dz=' in a:
    a=a.replace('dz=','*')   
if 'd-' in a:
    a=a.replace('d-','*')    
if 'lj' in a:
    a=a.replace('lj','*')   
if 'nj' in a:
    a=a.replace('nj','*')    
if 's=' in a:
    a=a.replace('s=','*')    
if 'z=' in a:
    a=a.replace('z=','*')
print(len(a))
        