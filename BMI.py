# create a function to compute body mass index
def bodymassindex(height, weight):
    bmi = weight / (height/100)**2
    return round(bmi, 2)

# call the main function
if __name__ == '__main__':
    bodymassindex()