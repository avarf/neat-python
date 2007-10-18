# Receives a chromosome and returns a graphical representation of its phenotype
# This is a draft solution - works only with linux
import os
try:
    import pydot
    import biggles
except ImportError:
    print "You do not have the required packages"
    

def draw_net(chromosome):
    output = 'digraph G {\n node [shape = circle]'
    for cg in chromosome.conn_genes:
        output += '\n\t'+str(cg.innodeid)+' -> '+str(cg.outnodeid)
        if cg.enabled is False:
            output += ' [style=dotted, color=cornflowerblue]'
        
    output += '\n }'
    
    g = pydot.graph_from_dot_data(output)
    g.write('phenotype.svg', prog='dot', format='svg') 
    os.system('eog phenotype.svg')
    
#    try:
#        #os.system('dot -Tsvg output -o network.svg')
#        os.system('echo "'+output+'" | dot -Tsvg > phenotype.svg')
#        os.system('eog phenotype.svg')
#    except OSError:
#        print 'Can\'t find graphviz package'
    
    return output

def plot_best(stats): 
    fitness = [c.fitness for c in stats]
    generation = [i for i in xrange(len(fitness))]
    
    plot = biggles.FramedPlot()
    plot.title = "Best fitness"
    plot.xlabel = r"Generations"
    plot.ylabel = r"Fitness"

    plot.add(biggles.Curve(generation, fitness, color="red"))
         
    #plot.show() # X11
    plot.write_img(600, 300, 'best_fitness.svg')
    # width and height doesn't seem to affect the output! 
    os.system('eog best_fitness.svg')
    
def plot_stats(stats): 
    generation = [i for i in xrange(len(stats[0]))]
    
    fitness = [c.fitness for c in stats[0]]
    avg_pop = [avg for avg in stats[1]]
    
    plot = biggles.FramedPlot()
    plot.title = "Population's average and best fitness"
    plot.xlabel = r"Fitness"
    plot.ylabel = r"Generations"

    plot.add(biggles.Curve(generation, fitness, color="red"))
    plot.add(biggles.Curve(generation, avg_pop, color="blue"))
         
    #plot.show() # X11
    plot.write_img(600, 300, 'avg_fitness.svg')
    # width and height doesn't seem to affect the output! 
    os.system('eog avg_fitness.svg')