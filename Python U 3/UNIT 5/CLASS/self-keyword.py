# In python code inside a class works for many things,not just one.
# So python needs away too know:
            #which things way to know.
# that is why self exists.
# What is self?
# SElf means "this one" or "current".
# You can think self as me,my,this.
#imagine to people.
#meet says my name is meet.
#akshay says my name is akshay.
# the word my changes for each person.
# self.name means my name.
# what does this line mean?
#  self.name = name: # save the value of name inside this one.
class person():
    def set_name(self,name):
        self.name=name
p1=person()
p2=person()
p1.set_name("Ansari")
p2.set_name("Abduu")
print(p1.name)
print(p2.name)