#Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.
#
#Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states: q1, q2, and q3. Here is the description of the states:
#
#q1 is our start state, we begin reading commands from here
#q2 is our accept state, we return true if this is our last state
#And the transitions:
#
#
#q1 moves to q2 when given a 1, and stays at q1 when given a 0
#q2 moves to q3 when given a 0, and stays at q2 when given a 1
#q3 moves to q2 when given a 0 or 1
#The automaton should return whether we end in our accepted state (q2), or not (true/false).
#
#Your task
#You will have to design your state objects, and how your Automaton handles transitions. Also make sure you set up the three states, q1, q2, and q3 for the myAutomaton instance. The test fixtures will be calling against myAutomaton.
#
#As an aside, the automaton accepts an array of strings, rather than just numbers, or a number represented as a string, because the language an automaton can accept isn't confined to just numbers. An automaton should be able to accept any 'symbol.'
#
#Here are some resources on DFAs (the automaton this Kata asks you to create):
#
#http://en.wikipedia.org/wiki/Deterministic_finite_automaton
#http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/dfa-definitions.html
#http://www.cse.chalmers.se/~coquand/AUTOMATA/o2.pdf
#Example
#a = Automaton()
#a.read_commands(["1", "0", "0", "1", "0"])  ==> False
#We make these transitions:
#
#input: ["1", "0", "0", "1", "0"]
#
#1: q1 -> q2
#0: q2 -> q3
#0: q3 -> q2
#1: q2 -> q2
#0: q2 -> q3
#We end in q3 which is not our accept state, so we return false
class Automaton(object):

    def __init__(self):
        self.states = q1()

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        for x in commands:
            self.states = self.states.trans(x)
        if str(self.states.getName()) == "q2":
            return True
        else:
            return False



# Do anything necessary to set up your automaton's states, q1, q2, and q3.
class State(object):
    def getName(self):
        return self.__class__.__name__

class q1(State):

    def trans(self, command):
        if command == "1":
            return q2()
        else:
            return self
    
class q2(State):

    def trans(self, command):
        if command == "0":
            return q3()   
        else: 
            return self

class q3(State):

    def trans(self, command):
        if command == "1" or command == "0":
            return q2()
        else: 
            return self
            
            
my_automaton = Automaton()
