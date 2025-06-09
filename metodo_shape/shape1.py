from math import sqrt, atan, acos, degrees
from typing import List

from .exeptions import TypeListError, AmountDataError, EquallyDataError

#TypeError, since points can only be defined with int or float
# a TypeError is raised with raise
class Point:
    def __init__(self, x=0, y=0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Error, invalid data type, must be int or float")
        self.x:int = x
        self.y:int = y

    def move(self, new_x, new_y):
        if not isinstance(new_x, (int, float)) or not isinstance(new_y, (int, float)):
            raise TypeError("Error, invalid data type, must be int or float")
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = 0
        self.y = 0

    def compute_distance(self, point)->float:
        return sqrt(((self.x-point.x)**2)+((self.y-point.y)**2))
    
    def __eq__(self, other:"Point"):
        return isinstance(other, Point) and (self.x == other.x) and (self.y == other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __str__(self):
        return f"[{self.x}, {self.y}]"



#Since Line iscreated with Point objects, the error is raised with a raise of
# type TypeError if the input objects are not points
class Line():
    def __init__(self, point_start:Point, point_end:Point):
        if not isinstance(point_start, Point) or not isinstance(point_end, Point):
            raise TypeError("Error, invalid data type, must be Point")
        self.point_start = point_start
        self.point_end = point_end
        self.length = self.point_start.compute_distance(self.point_end)
        #Because of the way slope and cut_point are calculated, divisions by 0
        # can occur, so a ZeroDivisionError exception is created; a TypeError
        # is not necessary.
        try:
            self.slope = (point_start.y-point_end.y)/(point_start.x-point_end.x)
        except ZeroDivisionError:
            self.slope = None
            self.cut_point = None
            return
        try:
            self.cut_point = -(point_start.y/self.slope)+point_start.x
        except ZeroDivisionError:
            self.cut_point = self.point_start.y
    
    #Due to the way in which slope and cut_point are generated, this function
    # can operate with values ​​of type None or divisor by zero, so exceptions
    # are generated and the necessary results are returned for those cases.
    def evaluate_value_function(self, x:float, reverse:bool)->float:
        try:
            if not reverse:
                return (self.slope*x)+self.cut_point
            else:
                return (x-self.cut_point)/self.slope
        except TypeError:
            return None
        except ZeroDivisionError:
            return self.point_start.y
    
    def compute_length(self)->float:
        return self.length
    
    #If slope (which is in radians) is set to None, a TypeError is generated
    # and the function returns 90 (corresponding to the slope angle of the line)
    def compute_slope(self):
        try: 
            return degrees(atan(self.slope))
        except TypeError:
            return 90
    
    #Since compute_horizontal_cross() uses evaluate_value_function(), which
    # performs operations that can generate TypeError and ZeroDivisionError
    # (which describe special lines), the exception is raised to return the correct values.
    def compute_horizontal_cross(self)->Point:
        try:
            return Point(self.evaluate_value_function(0, 1), 0)
        except TypeError:
            return Point(self.point_start.x, 0)
        except ZeroDivisionError:
            return None
            
    #Since compute_vertical_cross() uses evaluate_value_function(), which performs
    # operations that can generate TypeError and ZeroDivisionError (which describe
    # special lines), the exception is raised to return the correct values.
    def compute_vertical_cross(self)->Point:
        try:
            return Point(0, self.evaluate_value_function(0, 0))
        except TypeError:
            return None
        except ZeroDivisionError:
            return (0, self.point_start.y)
    
    def __str__(self):
        return f"   {self.point_start}-->{self.point_end}\n"

#The exception is raised if is_regular is not of type bool or number_sides is
# not of type int 
class Shape:
    def __init__(self, is_regular:bool, number_sides:int):
        if not isinstance(is_regular, bool) or not isinstance(number_sides, int):
            raise TypeError("Error, invalid data type, check the values")
        self.is_regular = is_regular
        self.number_sides = number_sides
        self._vertices = []
    
    #For this function you have to check that the list has points and that the
    # number of points different from each other needed to form the figure is
    # correct, otherwise the error simply appears.
    def check_regularity_points(self, vertices:List[Point]):
        try:
            AmountDataError.check_amount_data_list(vertices, self.number_sides)
            TypeListError.check_list_type(vertices, Point)
            EquallyDataError.check_equally_data_list(vertices)
            if(self.is_regular):
                reference = vertices[0].compute_distance(vertices[-1])
                margin_error = 1e-6
                for i in range(len(vertices)-1):
                    if(reference-vertices[i].compute_distance(vertices[i+1]) > margin_error):
                        return False
                return True
            return True
        except (AmountDataError, TypeError, EquallyDataError) as e:
            print(e)
    
    #Since set_vertices() uses check_regularity_points(), only one exception is
    # created to throw the message that the points are not going to be updated.
    def set_vertices(self, vertices:List[Point])->List[Point]:
        try:
            if(self.check_regularity_points(vertices)):
                self._vertices = vertices
                return self._vertices
        except (AmountDataError, TypeError, EquallyDataError) as e:
            print(
                "It is not possible to form the figure with the given vertices."
                "It will not be updated"
            )
    
    def get_vertices(self):
        return self._vertices
    
    @property
    def _edges(self)->List[Line]:
        _edges = []
        for i in range(len(self._vertices)-1):
            t = Line(self._vertices[i], self._vertices[i+1])
            _edges.append(t)
        _edges.append(Line(self._vertices[-1], self._vertices[0]))
        return _edges
    
    def get_edges(self):
        return self._edges
    
    @property
    def _inner_angles(self)->List[float]:
        _inner_angles = []
        if(len(self._vertices) == self.number_sides):
            for i in range(len(self._vertices)):
                ref = self._vertices[i]
                v1 = Line(ref, self._vertices[i-1])
                v2 = Line(ref, self._vertices[(i + 1)%len(self._vertices)])
                dot = (
                    (v1.point_end.x-ref.x)*(v2.point_end.x-ref.x)
                    +(v1.point_end.y-ref.y)*(v2.point_end.y-ref.y)
                    )
                _inner_angles.append(degrees(acos(dot/(v1.length*v2.length))))
        return _inner_angles
    
    def get_inner_angles(self)->List[float]:
        return self._inner_angles
    
    def compute_area(self):
        raise NotImplementedError("Method implemented by subclasses")
    
    def compute_perimeter(self):
        raise NotImplementedError("Method implemented by subclasses")
    
    @staticmethod
    def is_rectangle(vertices:List[Point])->bool:
        try:
            AmountDataError.check_amount_data_list(vertices, 4)
            TypeListError.check_list_type(vertices, Point)
            EquallyDataError.check_equally_data_list(vertices)
            margin_error = 1e-6
            lade_1 = Line(vertices[0], vertices[1])
            lade_2 = Line(vertices[1], vertices[2])
            lade_3 = Line(vertices[2], vertices[3])
            if(abs(lade_1.length-lade_3.length) < margin_error):
                if(lade_1.slope == 0 and lade_3.slope == 0 and lade_2.slope == None):
                    return True
            return False
        except (AmountDataError, TypeListError, EquallyDataError) as e:
            print("e")
            return False
    
    #An exception is added to the __str__ method to verify that the vertices
    # are well defined.
    def __str__(self):
        t1 = f"{self.__class__.__name__}:\n"
        t2, t3, t4 = "vertices: ", "edges:\n", "Inner_angles: "
        try:
            AmountDataError.check_amount_data_list(self._vertices, self.number_sides)
            for i in range(self.number_sides):
                t2 += f"P{i}{self._vertices[i]} "
                t3 += f"{self._edges[i]}"
                t4 += f"A{i}({self._inner_angles[i]}°) "
        except AmountDataError as e:
            return t1+"The vertices haven't defined correctly"
        t5 = f"Perimeter: {self.compute_perimeter()}\nArea: {self.compute_area()}"
        return f"{t1}{t2}\n{t3}{t4}\n{t5}"


""""""
#The rest of the methods of the rectangle and triangle classes along with their
# subclasses will only raise AmountDataError to verify that the vertices are
# correctly defined.
""""""

class Rectangle(Shape):
    def __init__(self, is_regular:bool, vertices:List[Point]):
        super().__init__(is_regular, 4)
        self.set_vertices(vertices)
        if(super().is_rectangle(vertices)):
            self.b_left = Point(min(i.x for i in self._vertices), 
                                min(i.y for i in self._vertices))
            self.t_right = Point(max(i.x for i in self._vertices), 
                                max(i.y for i in self._vertices))
        
    def set_vertices(self, vertices:List[Point]):
        if(super().is_rectangle(vertices)):
            super().set_vertices(vertices)
            self.b_left = Point(min(i.x for i in self._vertices), 
                                min(i.y for i in self._vertices))
            self.t_right = Point(max(i.x for i in self._vertices), 
                                max(i.y for i in self._vertices))
            return self._vertices
        print("\nThe rectangle cannot be formed. It will not be updated.\n")
    
    def compute_area(self)-> float:
        try:
            AmountDataError.check_amount_data_list(self._vertices, 4)
            return self._edges[0].length*self._edges[1].length
        except AmountDataError as e:
            return None

    def compute_perimeter(self)-> float:
        try:
            AmountDataError.check_amount_data_list(self._vertices, 4)
            return sum(i.length for i in self._edges)
        except AmountDataError as e:
            return None
    
    def compute_interference_point(self,point:Point)->bool:
        try:
            AmountDataError.check_amount_data_list(self._vertices, 4)
            val_x:bool = point.x >= self.b_left.x and point.x <= self.b_left.x+self._edges[0].length
            val_y:bool = point.y >= self.b_left.y and point.y <= self.b_left.y+self._edges[1].length
            return val_y and val_x
        except AmountDataError as e:
            return None
    
    def compute_interference_line(self,line:Line)->bool:
        try:
            AmountDataError.check_amount_data_list(self._vertices, 4)
            a:bool = self.b_left.y<=line.evaluate_value_function(self.b_left.x,0)<=self.t_right.y
            c:bool = self.b_left.y<=line.evaluate_value_function(self.t_right.x,0)<=self.t_right.y
            if(line.evaluate_value_function(self.t_right.y,1)!=None):
                b:bool = self.b_left.x<=line.evaluate_value_function(self.b_left.y,1)<=self.t_right.x
                d:bool = self.b_left.x<=line.evaluate_value_function(self.t_right.y,1)<=self.t_right.x
                return a or b or c or d
            return a or c
        except AmountDataError as e:
            return None
    

class Square(Rectangle):
    def __init__(self, vertices:List[Point]):
        super().__init__(True, vertices)

class Triangle(Shape):
    def __init__(self, is_regular:bool, vertices:List[Point]):
        super().__init__(is_regular, 3)
        super().set_vertices(vertices)

    def classify_triangle(self)->str:
        margin_error = 1e-6
        com = []
        try:
            AmountDataError.check_amount_data_list(self._vertices, 3)
            if(sum(abs(90-i) < margin_error for i in self._inner_angles) == 1):
                com.append("TriRectangle")
            if(all(abs(i.length-self._edges[0].length) < margin_error for i in self._edges)):
                com.append("Equilateral")
                return com
            elif(all(abs(i.length - self._edges[0].length) > margin_error for i in self._edges)
            and abs(self._edges[1].length - self._edges[2].length) > margin_error):
                com.append("Scalene")
                return com
            com.append("Isosceles")
            return com
        except AmountDataError as e:
            return None

    def compute_perimeter(self):
        try:
            AmountDataError.check_amount_data_list(self._vertices, 3)
            return sum(i.length for i in self._edges)
        except AmountDataError as e:
            return None
    
    def compute_area(self):
        try:
            AmountDataError.check_amount_data_list(self._vertices, 3)
            s = sum(i.length for i in self._edges)/2
            a, b, c = (i.length for i in self._edges)
            return sqrt(s*(s-a)*(s-b)*(s-c))
        except AmountDataError as e:
            return None

class Isosceles(Triangle):
    def __init__(self, vertices:List[Point]):
        try:
            super().__init__(False, vertices)
            com = super().classify_triangle()
            if com == None or com[-1] != "Isosceles":
                TypeError()
        except TypeError:
            pass

class Equilateral(Triangle):
    def __init__(self, vertices:List[Point]):
        try:
            super().__init__(True, vertices)
            com = super().classify_triangle()
            if com == None or com[-1] != "Equilateral":
                TypeError()
        except TypeError:
            pass

class TriRectangle(Triangle):
    def __init__(self, vertices:List[Point]):
        try:
            super().__init__(False, vertices)
            com = super().classify_triangle()
            if com == None or com[-1] != "TriRectangle":
                TypeError()
        except TypeError:
            pass

class Scalene(Triangle):
    def __init__(self, vertices:List[Point]):
        try:
            super().__init__(False, vertices)
            com = super().classify_triangle()
            if com == None or com[-1] != "Scalene":
                TypeError()
        except TypeError:
            pass