studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]


def gemiddeldperstudent(studentencijfers):
    for i in studentencijfers:
        print(sum(i) / 3)

def gemiddeldestudenten(studentencijfers):
    cijfers = 0
    for i in studentencijfers:
        cijfers = cijfers + sum(i)
    print(cijfers / (len(studentencijfers) *3))


gemiddeldperstudent(studentencijfers)
gemiddeldestudenten(studentencijfers)