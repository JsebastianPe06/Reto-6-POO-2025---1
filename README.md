Los paquetes poseen módulos con las exepciones especiales creadas, el módulos
shape1 posee comentarios para las exepciones aplicadas y en el main.py se pueden
probar las exepciones (para shape1 hay un ejemplo con triángulo equilatero de
como funcionan la exepciones)
```python
from metodo_shape.shape1 import (
    Point, Line, Rectangle, Square,
    Triangle, Isosceles, Equilateral, Scalene, TriRectangle
)
from reto_1.Exercise1 import run as run1
from reto_1.Exercise2 import run as run2
from reto_1.Exercise3 import run as run3
from reto_1.Exercise4 import run as run4
from reto_1.Exercise5 import run as run5

def prueba_shape():
    # Crear puntos
    print("\n Puntos:")
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(f"Distancia entre {p1} y {p2} = {p1.compute_distance(p2)}")
    p2.move(1, 1)
    print(f"P2 movido a: {p2}")
    p2.reset()
    print(f"P2 reiniciado: {p2}")

    # Crear líneas
    print("\n Línea:")
    l1 = Line(Point(0, 0), Point(2, 2))
    print(f"Longitud: {l1.length}, Pendiente: {l1.slope}")
    print(f"Y para X=3: {l1.evaluate_value_function(3, False)}")

    # Crear rectángulo
    print("\n Rectángulo:")
    rect = Rectangle(False, [Point(0, 0), Point(3, 0), Point(3, 2), Point(0, 2)])
    print(rect)

    # Crear cuadrado
    print("\n Cuadrado:")
    square = Square([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
    print(square)

    # Triángulo equilátero
    print("\n Triángulo Equilátero:")
    equi = Equilateral([
        Point(0, 0), Point(1, 1.732), Point(2, 0)
    ])
    print(equi)

    # Triángulo isósceles
    print("\n Triángulo Isósceles:")
    iso = Isosceles([
        Point(0, 0), Point(2, 0), Point(1, 1.732)
    ])
    print(iso)

    # Triángulo escaleno
    print("\n Triángulo Escaleno:")
    sc = Scalene([
        Point(0, 0), Point(1, 0), Point(0, 2)
    ])
    print(sc)

    # Triángulo rectángulo
    print("\n Triángulo Rectángulo:")
    tr = TriRectangle([
        Point(0, 0), Point(3, 0), Point(0, 4)
    ])
    print(tr)

if __name__ == "__main__":
    print("PRUEBA EXERCISE 1")
    run1()
    print("PRUEBA EXERCISE 2")
    run2()
    print("PRUEBA EXERCISE 3")
    run3()
    print("PRUEBA EXERCISE 4")
    run4()
    print("PRUEBA EXERCISE 5")
    run5()
    print("\n\n PRUEBA SHAPE")
    prueba_shape()
