from cmd import Cmd

class MyPrompt(Cmd):
  prompt = ">>"
  intro = "Welcome to LoboSh! Type ? to list all commands"

  def do_exit(self, inp):
    '''Exit the shell prompt'''
    print("Process ended")
    return True

  def do_echo(self, inp):
    '''Repeate anything that the user inputs as an argument'''
    print("{}".format(inp))

  def do_yes(self, inp):
    '''Repeate anything that the user inputs as an argument an infinite number of times'''
    while True:
      print("{}".format(inp))
    
MyPrompt().cmdloop()
print("Successfully")
