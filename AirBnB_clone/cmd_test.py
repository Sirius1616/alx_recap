from cmd import Cmd


class Cmd_Prompt(Cmd):
    prompt = '>'

    def do_hello():
        """Thus prints the word hello to the output of the console"""
        print('He is the only one left in the library')

    def do_diagonal():
        """Gets the diagonal of a matrix that is having an arbitrary constant with the numbers"""

        return 3 + 5



if __name__ == '__main__':
    Cmd_Prompt().cmdloop()


