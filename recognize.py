import numpy as np

def getL(y1, m_female, m_male, dispersion):
    res = 1/(2*dispersion)*((y1-m_female)**2 - (y1-m_male)**2)
    return res

def getL0(probability_f, probability_m):
    return np.log(probability_f/probability_m)

N = 70     # number of experiments

m_female = 60   # average weight of women (kg)
m_male = 85   # average weight of men (kg)

dispersion = 9     # dispersion of weight dispersion (kg^2)

probability_f = 0.48   # probability for women
probability_m = 0.52   # probability for men


L0 = getL0(probability_f, probability_m)

nM = 0

with open("text_recognize.txt", "w") as o:
    for i in range(N):
        y1 = np.random.normal(m_female, dispersion)

        L = getL(y1, m_female, m_male, dispersion)

        if(L >= L0):
            o.write(f'Man {y1}\n')
            nM += 1
        else:
            o.write(f'Woman {y1}\n')

    error = nM/N*100
    o.write(f'Eror {np.round(error, 2)}%\n')
    o.close()
