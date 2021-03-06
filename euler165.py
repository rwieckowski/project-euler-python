"""
A segment is uniquely defined by its two endpoints
 By considering two line segments in plane geometry there are three 
possibilities
 the segments have zero points one point or infinitely many points in 
common

Moreover when two segments have exactly one point in common it might 
be the case that that common point is an endpoint of either one of the 
segments or of both If a common point of two segments is not an 
endpoint of either of the segments it is an interior point of both 
segments
We will call a common point T of two segments L<sub>1</sub> and L<sub>
2</sub> a true intersection point of L<sub>1</sub> and L<sub>2</sub>  
if T is the only common point of L<sub>1</sub> and L<sub>2</sub>  and 
T is an interior point of both segments

Consider the three segments L<sub>1</sub> L<sub>2</sub> and L<sub>3
</sub>

L<sub>1</sub> 27 44 to 12 32
L<sub>2</sub> 46 53 to 17 62
L<sub>3</sub> 46 70 to 22 40

It can be verified that line segments L<sub>2</sub> and L<sub>3</sub> 
have a true intersection point We note that as the one of the end 
points of L<sub>3</sub> 2240 lies on L<sub>1</sub> this is not 
considered to be a true point of intersection L<sub>1</sub> and L<sub>
2</sub> have no common point So among the three line segments we find 
one true intersection point

Now let us do the same for 5000 line segments To this end we generate 
20000 numbers using the socalled quotBlum Blum Shubquot pseudorandom 
number generator

s<sub>0</sub>  290797

s<sub>n1</sub>  s<sub>n</sub>timess<sub>n</sub> modulo 50515093

t<sub>n</sub>  s<sub>n</sub> modulo 500

To create each line segment we use four consecutive numbers t<sub>n
</sub> That is the first line segment is given by

t<sub>1</sub> t<sub>2</sub> to t<sub>3</sub> t<sub>4</sub>

The first four numbers computed according to the above generator 
should be 27 144 12 and 232 The first segment would thus be 27144 to 
12232

How many distinct true intersection points are found among the 5000 
line segments
"""

def euler165():
    """
    >>> euler165()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()