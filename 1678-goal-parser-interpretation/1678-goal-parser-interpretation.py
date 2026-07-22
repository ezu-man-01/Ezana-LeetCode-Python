class Solution:
    def interpret(self, command: str) -> str:
        goal = ""
        for i in range(len(command)):
            if command[i] == "G":
                goal += "G"
            elif command[i] == "(":
                if command[i + 1] == ")":
                    goal += "o"
                    i +=2
                elif command[i + 1] == "a":
                    goal += "al"
                    i += 3
        
        return goal
        