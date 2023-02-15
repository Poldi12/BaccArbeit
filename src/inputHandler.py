import sys

def handle_input(inputparam):

    #check if required inputs are there
    try:
        #handle -help flag
        if(sys.argv[1] == '-help'):
            
            inputparam.Output_Yes = False

            print("Input Parameters:")
            print("#################")
            print()
            print("m = (required) maximum color for generating graph")
            print("d = (required)degree/ maximum number of neighbors, a node can have")
            print("q = (required)maximum color to color the graph with, after generating the graph")
            print("s = solver to solve the cnf formula, Default is cadical, other options:")
            print()
            print("cadical     = ('cd', 'cdl', 'cadical') \ngluecard3   = ('gc3', 'gc30', 'gluecard3', 'gluecard30') \ngluecard41  = ('gc4', 'gc41', 'gluecard4', 'gluecard41') \nglucose3    = ('g3', 'g30', 'glucose3', 'glucose30') \nglucose4    = ('g4', 'g41', 'glucose4', 'glucose41')\n lingeling   = ('lgl', 'lingeling') \nmaplechrono = ('mcb', 'chrono', 'maplechrono') \nmaplecm     = ('mcm', 'maplecm') \nmaplesat    = ('mpl', 'maple', 'maplesat') \nmergesat3   = ('mg3', 'mgs3', 'mergesat3', 'mergesat30') \nminicard    = ('mc', 'mcard', 'minicard') \nminisat22   = ('m22', 'msat22', 'minisat22') \nminisatgh   = ('mgh', 'msat-gh', 'minisat-gh')")
            print()
            print("p = path and filename to store the output (no input results in no output file) (example: C:/output/output.txt)")
            print("? = print the whole graph? possible inputs, 'y'=yes, 'n'=no , Default is no")
            print()
            print(".\main.exe [m] [d] [q] [s] [p] [?]")
            print()
            input("Press ENTER to exit program")
            return 1

        inputparam.m = int(sys.argv[1])
        inputparam.d = int(sys.argv[2])
        inputparam.q = int(sys.argv[3])

    except IndexError:
        print('Required Input Parameters missing!')
        print('For Info, call program with -help')
        inputparam.Output_Yes = False
        return 1            
    
    #simple print through file(old)
    '''
    print_graph: bool = False
    m: int = 6 #max input color
    d: int = 3 #degree
    ma: int = 5 #max output color (color for ausgabefaerbung)
    file_name = 'output.txt'
    print_graph = False
    '''

    try:
        inputparam.Solver = sys.argv[4]
    except IndexError:
        inputparam.Solver = 'cd'

    try:
        inputparam.OutputFile = sys.argv[5]
    except IndexError:
        inputparam.OutputFile = 'nooutputprovided!.txt'

    try:
        printGraph = sys.argv[6]
        if(printGraph == 'y'):
            inputparam.PrintGraph = True
    except IndexError:
        printGraph = False

    if (inputparam.d >= input.m):
        print("invalid input for generating valid Neighbourhoodgraph\n (Check max degree and number of colors input)")
        return_value += 1

    return 0