from cmd import Cmd
import os

class MyPrompt(Cmd):
  # prompt = "|" + os.getcwd() + " >> "

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

  def do_clear(self, inp):
    os.system('clear')

  def do_cd(self, inp):
    os.chdir(inp)
    os.getcwd()

  def do_ls(self, inp):
    for i in os.listdir():
      print(i)

  do_EOF = do_exit

  prompt = os.getcwd() + " >> "

MyPrompt().cmdloop()
print("successfully")
