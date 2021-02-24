# Polymorphyism
# 1. Duck Typing
# If a bird swimming like duck and if a bird quacking like a duck. It is Duck

class PyCharm: 
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor: 
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell Checkin")
        print("Convention check")
class Laptop:
    def code(self,ide):
        ide.execute()
# Wow it is very goodD
ide = PyCharm()
ide2 = MyEditor()
lap1 = Laptop()
lap1.code(ide)
lap1.code(ide2)
