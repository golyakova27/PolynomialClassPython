class Polynomial(object):

     #constructor
     def __init__ (self, coeffs):

          if isinstance(coeffs, list):
               if len(coeffs) != 0:
                    for c in coeffs:
                         if isinstance(c, (int, float)):
                              
                              while coeffs[0] == 0 and len(coeffs) > 1:
                                   coeffs.pop(0)
                              if coeffs[0] == 0:
                                   self.coeffs = [0]
                                   self.degree = 0
                              else:
                                   self.coeffs = coeffs[:]
                                   self.degree = len(coeffs) - 1
                         else:
                              raise TypeError("List must have float or integer values.")
               else:
                    raise TypeError("Your list is empty.")
          elif isinstance(coeffs, Polynomial):
               self.coeffs = coeffs.coeffs[:]
               self.degree = coeffs.degree
          else:
               raise TypeError("This type of variable task is not vaild, enter the list.")
         

     #sum
     def __add__(self, obj):
          if isinstance(obj, Polynomial):
               if self.degree > obj.degree:
                    sum = self.coeffs[:]
                    i = 0
                    while i <= obj.degree:
                         sum[i + self.degree - obj.degree] += obj.coeffs[i]
                         i += 1
               else:
                    sum = obj.coeffs[:]
                    i = 0
                    while i <= self.degree:
                         sum[i + obj.degree - self.degree] += self.coeffs[i]
                         i += 1
          elif isinstance(obj, (int, float)):
                    self.coeffs[-1] += obj
                    sum = self.coeffs[:]
          else:
               raise TypeError("Incorrect parameter input.")
          return sum

     def __radd__(self, obj):
          return self + obj


     #negative
     def __neg__(self):
          i = 0
          while i < len(self.coeffs):
               self.coeffs[i] *= -1
               i += 1
          return self

     #subtraction
     def __sub__(self, obj):
          if isinstance(arg, (int, float, Polynomial)):
               return self.__add__(-obj)
          else:
               raise TypeError("Incorrect parameter input.")

     def __rsub__(self, obj):
          if isinstance(arg, (int, float, Polynomial)):
               return(self.__neg__()).__add__(obj)
          else:
               raise TypeError("Incorrect parameter input.")


     #eguals
     def __eq__(self, obj):
          if isinstance(obj, Polynomial):
               return self.coeffs == obj.coeffs
          elif isinstance(obj, (int, float)):
               return self.degree == 0 and self.coeffs[0] == obj
          else:
               return False

     def __ne__(self, obj):
          return not self.__eq__(obj)


     #multiplication
     def __mul__(self, obj):
          if isinstance(obj, Polynomial):
               mul = [0] * (self.degree + obj.degree + 1)
               i = 0
               while i <= self.degree:
                    j = 0
                    while j <= obj.degree:
                         mul[i + j] += self.coeffs[i] * obj.coeffs[j]
                         j += 1
                    i += 1
          elif isinstance(obj, (int, float)):
               mul = self.coeffs[:]
               i = 0
               while i <= self.degree:
                    mul[i] *= obj
                    i += 1
          else:
               raise TypeError("Incorrect parameter input.")
          return Polynomial(mul)

     def __rmul__(self, obj):
          self * obj


     #toString
     def __str__(self): 
          string = "" 
          if (self.degree > 1): 
               if (self.coeffs[0] != 1 and self.coeffs[0] != -1):
                    string += str(self.coeffs[0]) + 'x^' + str(self.degree) 
               elif (self.coeffs[0] == 1): 
                    string += 'x^' + str(self.degree) 
               elif (self.coeffs[0] == -1): 
                    string = '-x^' + str(self.degree)
                    
               i = 1
               while i < (self.degree - 1): 
                    if (self.coeffs[i] != 1 and self.coeffs[i] != -1): 
                         if (self.coeffs[i] > 0): 
                              string += '+' + str(self.coeffs[i]) + 'x^' + str(self.degree - i) 
                         elif (self.coeffs[i] < 0): 
                              string += str(self.coeffs[i]) + 'x^' + str(self.degree - i)
                    elif (self.coeffs[i] == 1): 
                         string += '+x^' + str(self.degree - i) 
                    elif (self.coeffs[i] == -1): 
                         string += '-x^' + str(self.degree - i)
                    i += 1
               if (self.coeffs[self.degree - 1] != 1 and self.coeffs[self.degree - 1] != -1): 
                    if (self.coeffs[self.degree - 1] < 0): 
                         string += str(self.coeffs[self.degree - 1]) + 'x' 
                    elif (self.coeffs[self.degree - 1] > 0): 
                         string += '+' + str(self.coeffs[self.degree - 1]) + 'x' 
               elif (self.coeffs[self.degree - 1] == 1): 
                    string += '+x' 
               elif (self.coeffs[self.degree - 1] == -1): 
                    string += '-x' 
               if (self.coeffs[self.degree] > 0): 
                    string += '+' + str(self.coeffs[self.degree]) 
               elif (self.coeffs[self.degree] < 0): 
                    string += str(self.coeffs[self.degree])
                    
          elif (self.degree == 1): 
               if (self.coeffs[0] != 1 and self.coeffs[0] != -1): 
                    string += str(self.coeffs[1]) + 'x' 
               elif (self.coeffs[0] == 1): 
                    string += 'x'
                    if (self.coeffs[1] > 0):
                         string += '+' + str(self.coeffs[1])
                    elif (self.coeffs[1] < 0):
                         string += str(self.coeffs[1])
               elif (self.coeffs[0] == -1):
                    string = '-x'
                    if (self.coeffs[1] > 0):
                         string += '+' + str(self.coeffs[1])
                    elif (self.coeffs[1] < 0):
                         string += str(self.coeffs[1])
          elif (self.degree == 0): 
                    string = str(self.coeffs[0]) 
          return string if string else '0'
