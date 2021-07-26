class Family:
    def __init__(self, last_name,  members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]):
        self.members = members
        self.last_name = last_name
    def born(self, **kwargs):
        self.members.append(kwargs)

    def is_18(self, name):
        for i in self.members:
            if i['name'] == name:
                if i['age'] > 18:
                    return True
                else:
                    return False

    def family_members(self):
        for i in self.members:
            print(i)

child1 = Family('doe')
man1 = Family('doe')
child1.born(name = 'joe',age = 0, gender = 'Male', is_child = True)
man1.born(name = 'Goerge',age = 33, gender = 'Male', is_child = True)
man1.is_18('Michael')
child1.family_members()





class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        if self.is_18(name):
            for i in self.members:
                return 'using ' + i['power']
        else:
            raise Exception("not 18")
            
    def incredible_presentation(self):
        for i in self.members:
            print(i['incredible_name'] ,i['power'])


bob = TheIncredibles('Bob Parr',[
    {'name':'Bob Parr','age':43,'gender':'Male','is_child':False ,'incredible_name' : 'Mr.incredible', 'power' : 'super-strength'}])
print(bob.use_power('Bob Parr'))
bob.incredible_presentation()
bob.family_members()


helen = TheIncredibles('Helen parr',[
    {'name':'Helen parr','age':43,'gender':'Female','is_child':False ,'incredible_name' : 'Elastigirl', 'power' : 'super-strech'}])
print(helen.use_power('Helen parr'))
helen.incredible_presentation()
helen.family_members()



violet = TheIncredibles('Violet parr',[
    {'name':'Violet parr','age':16,'gender':'Female','is_child':False ,'incredible_name' : 'Vi', 'power' : 'invisibility'}])
# print(violet.use_power('Violet parr'))
violet.incredible_presentation()
violet.family_members()




dashiell = TheIncredibles('Dashiel parr',[
    {'name':'Dashiel parr','age':13,'gender':'Male','is_child':False ,'incredible_name' : 'Dash', 'power' : 'super-speed'}])
# print(dashiell.use_power('Dashiel parr'))
dashiell.incredible_presentation()
dashiell.family_members()


jack = TheIncredibles('Baby Jack', [
    {'name':'Baby Jack','age':1,'gender':'Male','is_child':True ,'incredible_name' : 'Baby Jack', 'power' : 'unknown'}])

jack.born(name = 'Baby Jack', age = 1, gender = 'Male', is_child = True ,incredible_name = 'Baby Jack', power = 'unknown')
# print(jack.use_power('Baby Jack'))
jack.incredible_presentation()
jack.family_members()

