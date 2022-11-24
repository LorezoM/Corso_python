import random
from statistics import mean
from statistics import mode


TARGET = 100 # Target "smartness" for our population
POP_SIZE = 40 # The size of the population at the start of each iteration (keepthis even if you change it)
INIT_MIN_SMART = 1 # The minimum smartness of a dog at ITER 0
INIT_MAX_SMART = 10 # The maximum smartness of a dog at ITER 0
INIT_MODE_SMART = 3 # The most comon smartness value of a dog at ITER 0
MUTATE_ODDS = 0.01 # Probability of mutation for a new puppy
MUTATE_MIN_FACTOR = 0.4 # Lower bound for the the product factor we multuplysmartness for, if mutation happens
MUTATE_MAX_FACTOR = 1.3 # Upper bound for the the product factor we multuplysmartness for, if mutation happens
LITTER_SIZE = 5 # Puppies born from each pair of adult dogs
MAX_ITER = 1000 # Max number of iterations

def QI(INIT_MIN_SMART, INIT_MAX_SMART, INIT_MODE_SMART):
    qi = random.triangular(INIT_MIN_SMART, INIT_MAX_SMART, INIT_MODE_SMART)
    return(qi)

def populate(POP_SIZE, INIT_MIN_SMART, INIT_MAX_SMART, INIT_MODE_SMART):
    dogs = []
    for i in range(POP_SIZE):
        dogs.append([])
        dogs[i].append(0 if (i<POP_SIZE/2) else 1) # definizione sesso (0 femmina 1 mschio) random.randint(0, 1)
        dogs[i].append(random.triangular(INIT_MIN_SMART, INIT_MAX_SMART, INIT_MODE_SMART) * (1 if random.random() <= (1-MUTATE_ODDS) else random.uniform(MUTATE_MIN_FACTOR,MUTATE_MAX_FACTOR) ) )#definizione inteligenza
    return (dogs)

def fitness(dogs):
    QI = [sublist[1] for sublist in dogs ]
    QI_mean=mean(QI)
    QI_mode = mode(QI)
    QI_max = max(QI)
    QI_min = min(QI)
    return (QI_mean,QI_mode,QI_max,QI_min)

def select_new_gen(dogs):
    dogs.sort(key=lambda x: -x[1])
    female, male = [], []
    for i in range(len(dogs)):
        if (dogs[i][0] == 0) & (len(female) < POP_SIZE / 2):
            female.append(dogs[i])
        elif (len(male) < POP_SIZE / 2):
            male.append(dogs[i])
        elif ((len(male) == POP_SIZE / 2) & (len(female) == POP_SIZE / 2)):
            break
        else:
            pass
    return(female,male)

def new_gen(LITTER_SIZE,female,male):
    random.shuffle(female)
    random.shuffle(male)
    puppy = []
    counter = 0
    for j in range(POP_SIZE//2):
        mamma = female[j]
        pappa = male[j]
        QI_max = max(mamma[1], pappa[1])
        QI_min = min(mamma[1], pappa[1])
        for i in range(LITTER_SIZE):
            puppy.append([])
            puppy[counter].append(random.randint(0, 1))
            puppy[counter].append(random.uniform(QI_min,QI_max) * (1 if random.random() <= (1-MUTATE_ODDS) else random.uniform(MUTATE_MIN_FACTOR,MUTATE_MAX_FACTOR)))
            counter += 1
    return (puppy)


if __name__ == '__main__':
    dogs = populate(POP_SIZE, INIT_MIN_SMART, INIT_MAX_SMART, INIT_MODE_SMART)
    h = 0
    while h < MAX_ITER:
        (QI_mean, QI_mode, QI_max, QI_min) = fitness(dogs)
        print(QI_mean)
        if QI_mean >= TARGET:
            break
        (female, male) = select_new_gen(dogs)
        puppy = new_gen(LITTER_SIZE, female, male)
        dogs = female + male + puppy

