from deap import base,creator,tools,algorithms
import random
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

# problem constants:
ONE_MAX_LENGTH =    8  # length of bit string to be optimized

# Genetic Algorithm constants:
POPULATION_SIZE = 9
P_CROSSOVER = 0.9  # probability for crossover
P_MUTATION = 0.1   # probability for mutating an individual
MAX_GENERATIONS = 50
HALL_OF_FAME_SIZE = 10


# set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

toolbox = base.Toolbox()
toolbox.register("zeroOrOne", random.randint, 0, 1)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.zeroOrOne, ONE_MAX_LENGTH)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

def Fitness_func(individual):
    length = len(individual)
    i = 0
    fitness = 0
    while length !=0:
       fitness = fitness + (individual[length-1] * pow(2 , i))
       i=i+1
       length =length-1
    return fitness,


toolbox.register("evaluate", Fitness_func)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/ONE_MAX_LENGTH)

def main():
    
    i = 4
    while i <= 10:
        population = toolbox.populationCreator(n=i)
        i = i + 1
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("max", numpy.max)
        stats.register("avg", numpy.mean)
        hof = tools.HallOfFame(HALL_OF_FAME_SIZE)
        population, logbook = algorithms.eaSimple(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)

        # extract statistics:
        maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")

        # plot statistics:
    sns.set_style("whitegrid")
    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Average Fitness')
    plt.title('Max and Average Fitness over Generations \n (Max fitness = red, Average fitness = green) \n with varying population of 4 to 10 \n BITLENGTH Fixed to 8')
    plt.show()

if __name__ == "__main__":
    main()
