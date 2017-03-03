#FUNCTIONS

#def = gives a function a definition
#def greet():
#    return 'Good evening, master'

#temp = greet()
#print temp 
#    Good evening, master

#def greet(name):
#    answer = 'hello, ' + name
#    return answer

#temp = 'doctor'
#result = greet(temp)

#question 1

def double_it(number):
    return 2 * number

print double_it(2)

print double_it(3.5)

print double_it("hi")

#question 2

def calc_hypo(a, b):
    hypo = (a**2 + b**2)**0.5 #**0.5 is the same as the squared root
    return hypo

print calc_hypo(3, 4)

#question 3

def calc_hypo(a, b):
    if type (a) not in (int, float) or type (b) not in (int, float):
        print 'bad argument'
        return False
    if a <= 0 or b <= 0:
        print 'bad argument'
        return False
    hypo = (a**2 + b**2)**0.5
    return hypo

print calc_hypo(15, 18)








