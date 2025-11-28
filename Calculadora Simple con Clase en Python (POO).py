'''
# ============================================
# DEFINICIÓN DE UNA CLASE "Calculator"
# ============================================
'''
class Calculator:  
  '''
   Método constructor de la clase
   Se ejecuta automáticamente al crear un objeto de tipo Calculator
  '''
  def __init__(self,a,b):
    '''
     Se guardan los valores recibidos en variables internas (atributos del objeto)
     Se usan con guion bajo para indicar que son "privadas" (convención en Python)
    '''
    self._a = a  
    self._b = b
        
  # Método para sumar los dos números
  def suma(self):
    r = self._a + self._b  # Se suman los atributos a y b
    return r  # Se devuelve el resultado
    
  # Método para restar los dos números
  def resta(self):
    r = self._a - self._b  # Se resta a - b
    return r  # Se devuelve el resultado

  # Método para multiplicar los dos números
  def multiplicacion(self):
    r = self._a * self._b  # Se multiplican a y b
    return r  # Se devuelve el resultado
    
  # Método para dividir los dos números
  def divison(self):
    r = self._a / self._b  # Se divide a entre b
    return r  # Se devuelve el resultado
    
'''
 ============================================
 CREACIÓN DE UN OBJETO DE LA CLASE Calculator
 ============================================
'''
# Aquí se crea una "instancia" de Calculator con los valores 5 y 8
op = Calculator(5,8)

'''
 ============================================
 USO DE LOS MÉTODOS DE LA CLASE
 ============================================
'''
# Se llaman a las funciones definidas en la clase y se muestran los resultados
print("La suma es:", op.suma())              # Llama al método suma()
print("La resta es:", op.resta())            # Llama al método resta()
print("La multiplicación es:", op.multiplicacion())  # Llama al método multiplicacion()
print("La división es:", op.divison())       # Llama al método division()
