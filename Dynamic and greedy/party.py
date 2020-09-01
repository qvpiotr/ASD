class Employee:
    def __init__(self, fun, name):
        self.emp = [] #subordinates
        self.fun = fun
        self.f = -1
        self.g = -1
        self.name = name

def f(v):
    if v.f >= 0: return v.f
    x = v.fun
    for vi in v.emp:
        x += g(vi)
    y = g(v)
    v.f = max(x,y)
    return v.f

def g(v):
    if v.g >= 0: return v.g
    v.g = 0
    for vi in v.emp:
        v.g += f(vi)
    return v.g

def party(v,array):
    if v.f > v.g:
        array.append(v.name)
        for vi in v.emp:
            for vs in vi.emp:
                party(vs, array)
    else:
        for vi in v.emp:
            party(vi, array)

Gabi = Employee(20, "Gabi")
Piter = Employee(21, "Piter")
Roberto = Employee(12, "Roberto")
Rympałek = Employee(3, "Rympałek")
Marchewa = Employee(4, "Marchewa")
Krakowiak = Employee(31, "Krakowiak")
Pershing = Employee(1, "Pershing")
Misiek_z_Nadarzyna = Employee(42, "Misiek z Nadarzyna")
Słowik = Employee(13, "Słowik")
Parasol = Employee(4, "Parasol")
Gabi.emp.append(Rympałek)
Gabi.emp.append(Marchewa)
Rympałek.emp.append(Roberto)
Rympałek.emp.append(Krakowiak)
Krakowiak.emp.append(Parasol)
Marchewa.emp.append(Piter)
Marchewa.emp.append(Misiek_z_Nadarzyna)
Piter.emp.append(Pershing)
Piter.emp.append(Słowik)
print(f(Gabi))
array = []
party(Gabi, array)
print(array)