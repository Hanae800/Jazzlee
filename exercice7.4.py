#%%
def to_c(f):
    """ returns the temperature in degrees celsius """
    return ((f - 32 ) * 5/9)  
    if f < -459.67 :
        raise ValueError("Temperature value is below absolute zero.")

for t in (72.6, 98.8, 30.3, 100.8):
    print(t, ": ", celsius(t))


#%%

#%%
