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
