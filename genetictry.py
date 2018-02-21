import random

def create_population(self, count):
    pop=[]
    for _ in range(0,count):
        network=Network(self.nn_param_choices)
        network.create_random()
        pop.append(network)
    return pop

def breed(self, mom, dad):
    children=[]
    for _ in range(2):
        child={}
        for param in self.nn_param_choices:
            child[param]=random.choice(
                    [mom.network[param],dad.network[param]]
            )
        network=Network(self.nn_param_choices)
        network.create_set(child)
        children.append(network)
    return children

def mutate(self, network):
    mutation = random.choice(list(self.nn_param_choices.keys()))
    network.network[mutation]=random.choice(self.nn_param_choices[mutation])
    return network

def evolve(self, pop):
    graded = [(self.fitness(network), network) for network in pop]
    graded = [x[1] for x in sorted(graded, key=lambda x:x[0],reverse=True)]
    retain_length=int(len(graded)*self.retain)
    parents=graded[:retain_length]
    for individual in graded[retain_length:]:
        if self-random_select>random.random():
            parents.append(individual)
    for individual in parents:
        if self.mutate_chance>random.random():
            individual = self.mutate(individual)