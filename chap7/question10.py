

class Point:
    def slope(P1, P2):
        return(P2[1] - P1[1]) / (P2[0] - P1[0])
    def y_intercept(P1, slope):
        return P1[1] - slope * P1[0]
    def line_intersect(m1, b1, m2, b2):
        if m1 == m2:
            print ("These lines are parallel!!!")
            return None
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        return x,y

    A1 = [2.0,2.0]
    A2 = [0,0]
    B1 = [0,2.0]
    B2 = [2.0,0]
    slope_A = slope(A1, A2)
    slope_B = slope(B1, B2)
    y_int_A = y_intercept(A1, slope_A)
    y_int_B = y_intercept(B1, slope_B)
    print("Enter the endpoints of the first line segment: ",A1)
    print("Enter the endpoints of the second line segment: ",A2)
    print("The intersecting point is:",line_intersect(slope_A, y_int_A, slope_B, y_int_B))