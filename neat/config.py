# sets the configuration parameters for NEAT
       
def load(file):
    try:
        parameters = open('file','r')
    except IOError:
        print 'Error: file %s not found!' %file
    #else:
        # set class attributes
        

class Config: # read from file
    # phenotype config
    input_nodes = 2
    output_nodes = 1
    allow_recurrent = False
    
    # mutation probabilities
    prob_crossover = 0.7
    prob_mutation = 0.25
    prob_addlink = 0.05
    prob_addnode = 0.03
    prob_mutatebias = 0.3
    prob_togglelink = 0.0
    prob_weightreplaced = 0.0
    max_pertubation = 0.5
    max_bias_pertubation = 0.1
    
    # genetic algorithm parameters
    pop_size = 50
    number_epochs = 1000
    
    # genotype compatibility 
    compatibility_threshold = 0.5
    compatibility_change = 0.1
    excess_coeficient = 1.0
    disjoint_coeficient = 1.0
    weight_coeficient = 0.4
    
    # species
    species_size = 3
    survival_threshold = 0.2
    species_age_threshold = 80
    species_youth_threshold = 10
    species_old_penalty = 1.2
    species_youth_boost = 0.7
    species_max_fitness = 15
    
    # for future release
    #ele_event_time = 1000
    #ele_events = False            
                