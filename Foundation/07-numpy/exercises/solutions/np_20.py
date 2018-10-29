Z = np.random.uniform(0,1,10) * 10
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

find_nearest(Z,5)