import random

class Population:
    def __init__(self, num, min, max):
        self.num = num
        self.min = min
        self.max = max
    
    def population(self, chr):
        chro = []
        
        for i in range(self.num):
            chro.append(self.generateChromosome(chr))
            
        return chro
    
    def generateChromosome(self, lth):
        chromosome = []

        for i in range(lth):
            chromosome.append(round(random.uniform(self.min, self.max), 4))
            
        return chromosome
    
    def fx(self, chro):
        fx_result = []
        
        for x in range(len(chro)):
            i = chro[x]
            
            fx = round(((i[0] / 25) + (i[1] / 15)) * 3, 4)
            fx_result.append(fx)
            
        return fx_result
            
    def fitness(self, chro, fx):
        fit = []
        sum_fit = 0
        
        for y in range(len(fx)):
            res = round(1 / fx[y], 4)
            
            fit.append([chro[y], res])
            sum_fit += res
            
        sum_fit = round(sum_fit, 4)
        
        return fit, sum_fit
            
    def fittest_chro(self, fit = [], min = 2):
        arr_fit = []
        fittest = []
        
        for i in range(len(fit[0])):
            arr_fit.append(fit[0][i][1])
            
        arr_fit.sort(reverse=True)
        
        for x in range(min):
            for y in range(len(fit[0])):
                if(arr_fit[x] == fit[0][y][1]):
                    fittest.append(fit[0][y][0])
                    
        return fittest
                
    def crossover(self, fittest = []):
        a = random.uniform(-0.25, 1.25)
        
        c1x1 = round(fittest[0][0] + a * (fittest[1][0] - fittest[0][0]), 4)
        c1x2 = round(fittest[0][1] + a * (fittest[1][1] - fittest[0][1]), 4)
        c2x1 = round(fittest[1][0] + a * (fittest[0][0] - fittest[1][0]), 4)
        c2x2 = round(fittest[1][1] + a * (fittest[0][1] - fittest[1][1]), 4)
        
        child = [[c1x1, c1x2], [c2x1, c2x2]]
        
        return child
        
    # def mutation(self, x):
    #     for i in range(len(x)):
    #         prob = random.random()
    #         if(prob > 0.7): 
    #             if(x[i] == "0"):
    #                 x[i] == "1"
    #             else:
    #                 x[i] == "0"
            
    #     return x