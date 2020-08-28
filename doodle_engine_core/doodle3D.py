from pygame import *
from doodle_engine_core.matrix44 import*
from OpenGL.GL import *
from OpenGL.GLU import *
class Game:
    def __init__(self, size, title="<????>", fullscreen=False):
        if fullscreen:
            self.display=display.set_mode(size, FULLSCREEN|OPENGL)
        else:
            self.display=display.set_mode(size, OPENGL)
        display.set_caption(title)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_FLAT)
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLight(GL_LIGHT0, GL_POSITION,  (0, 1, 1, 0))
        w,h=size
        Game.resize(w,h)
        self.title=title
        self.size=size
    def resize(width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, float(width)/height, .1, 1000.)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    def __str__(self):
        return('main Game object title='+self.title+' size='+str(self.size)+' - doodle3D.Game instance')

class Cube(object):


    def __init__(self, position, color):

        self.position = position
        self.color = color

    # Cube information

    num_faces = 6

    vertices = [ (0.0, 0.0, 1.0),
                 (1.0, 0.0, 1.0),
                 (1.0, 1.0, 1.0),
                 (0.0, 1.0, 1.0),
                 (0.0, 0.0, 0.0),
                 (1.0, 0.0, 0.0),
                 (1.0, 1.0, 0.0),
                 (0.0, 1.0, 0.0) ]

    normals = [ (0.0, 0.0, +1.0),  # front
                (0.0, 0.0, -1.0),  # back
                (+1.0, 0.0, 0.0),  # right
                (-1.0, 0.0, 0.0),  # left
                (0.0, +1.0, 0.0),  # top
                (0.0, -1.0, 0.0) ] # bottom

    vertex_indices = [ (0, 1, 2, 3),  # front
                       (4, 5, 6, 7),  # back
                       (1, 5, 6, 2),  # right
                       (0, 4, 7, 3),  # left
                       (3, 2, 6, 7),  # top
                       (0, 1, 5, 4) ] # bottom

    def render(self):

        # Set the cube color, applies to all vertices till next call
        glColor( self.color )

        # Adjust all the vertices so that the cube is at self.position
        vertices = []
        for v in self.vertices:
            vertices.append( tuple(Vector3(v)+ self.position) )


        # Draw all 6 faces of the cube
        glBegin(GL_QUADS)

        for face_no in range(self.num_faces):

            glNormal3dv( self.normals[face_no] )

            v1, v2, v3, v4 = self.vertex_indices[face_no]

            glVertex( vertices[v1] )
            glVertex( vertices[v2] )
            glVertex( vertices[v3] )
            glVertex( vertices[v4] )

        glEnd()
class Mosaic(object):
    def __init__(self, pic):

        map_surface = image.load(pic)
        map_surface.lock()

        w, h = map_surface.get_size()

        self.cubes = []

        # Create a cube for every non-transperant pixel
        for y in range(h):
            for x in range(w):

                r, g, b, a = map_surface.get_at((x, y))

                if (r,g,b) != (255,255,255):

                    gl_col = (r/255.0, g/255.0, b/255.0)
                    position = (float(x), 0.0, float(y))
                    cube = Cube( position, gl_col )
                    self.cubes.append(cube)


        map_surface.unlock()

        self.display_list = None

    def render(self):

        if self.display_list is None:

            # Create a display list
            self.display_list = glGenLists(1)
            glNewList(self.display_list, GL_COMPILE)

            # Draw the cubes
            for cube in self.cubes:
                cube.render()

            # End the display list
            glEndList()

        else:

            # Render the display list
            glCallList(self.display_list)
####VECTOR3 CLASS####
class Vector3(object):
     
        __slots__ = ('_v',)
     
        _gameobjects_vector = 3
     
     
        def __init__(self, *args):
            """Creates a Vector3 from 3 numeric values or a list-like object
            containing at least 3 values. No arguments result in a null vector.
     
            """
            if len(args) == 3:
                self._v = map(float, args[:3])
                return
     
            if not args:
                self._v = [0., 0., 0.]
            elif len(args) == 1:
                self._v = map(float, args[0][:3])
            else:
                raise ValueError("Vector3.__init__ takes 0, 1 or 3 parameters")
     
     
        @classmethod
        def from_points(cls, p1, p2):
     
            v = cls.__new__(cls, object)
            ax, ay, az = p1
            bx, by, bz = p2
            v._v = [bx-ax, by-ay, bz-az]
     
            return v
     
        @classmethod
        def from_floats(cls, x, y, z):
            """Creates a Vector3 from individual float values.
            Warning: There is no checking (for efficiency) here: x, y, z _must_ be
            floats.
     
            """
            v = cls.__new__(cls, object)
            v._v = [x, y, z]
            return v
     
     
        @classmethod
        def from_iter(cls, iterable):
            """Creates a Vector3 from an iterable containing at least 3 values."""
            next = iter(iterable).next
            v = cls.__new__(cls, object)
            v._v = [ float(next()), float(next()), float(next()) ]
            return v
     
        @classmethod
        def _from_float_sequence(cls, sequence):
            v = cls.__new__(cls, object)
            v._v = list(sequence[:3])
            return v
     
        def copy(self):
            """Returns a copy of this vector."""
     
            v = self.__new__(self.__class__, object)
            v._v = self._v[:]
            return v
            #return self.from_floats(self._v[0], self._v[1], self._v[2])
     
        __copy__ = copy
     
        def _get_x(self):
            return self._v[0]
        def _set_x(self, x):
            try:
                self._v[0] = 1.0 * x
            except:
                raise TypeError("Must be a number")
        x = property(_get_x, _set_x, None, "x component.")
     
        def _get_y(self):
            return self._v[1]
        def _set_y(self, y):
            try:
                self._v[1] = 1.0 * y
            except:
                raise TypeError("Must be a number")
        y = property(_get_y, _set_y, None, "y component.")
     
        def _get_z(self):
            return self._v[2]
        def _set_z(self, z):
            try:
                self._v[2] = 1.0 * z
            except:
                raise TypeError("Must be a number")
        z = property(_get_z, _set_z, None, "z component.")
     
        def _get_length(self):
            x, y, z = self._v
            return sqrt(x*x + y*y + z*z)
     
        def _set_length(self, length):
            v = self._v
            try:
                x, y, z = v
                l = length / sqrt(x*x + y*y +z*z)
            except ZeroDivisionError:
                v[0] = 0.
                v[1] = 0.
                v[2] = 0.
                return self
     
            v[0] = x*l
            v[1] = y*l
            v[2] = z*l
     
        length = property(_get_length, _set_length, None, "Length of the vector")
     
        def unit(self):
            """Returns a unit vector."""
            x, y, z = self._v
            l = sqrt(x*x + y*y + z*z)
            return self.from_floats(x/l, y/l, z/l)
     
     
        def set(self, x, y, z):
            """Sets the components of this vector.
            x -- x component
            y -- y component
            z -- z component
     
            """
     
            v = self._v
            try:
                v[0] = x * 1.0
                v[1] = y * 1.0
                v[2] = z * 1.0
            except TypeError:
                raise TypeError("Must be a number")
            return self
     
     

     
     
        def __repr__(self):
     
            x, y, z = self._v
            return "Vector3(%s, %s, %s)" % (x, y, z)
     
     
        def __len__(self):
     
            return 3
     
        def __iter__(self):
            """Iterates the components in x, y, z order."""
            return iter(self._v[:])
     
        def __getitem__(self, index):
            """Retrieves a component, given its index.
     
            index -- 0, 1 or 2 for x, y or z
     
            """
            try:
                return self._v[index]
            except IndexError:
                raise IndexError("There are 3 values in this object, index should be 0, 1 or 2!")
     
        def __setitem__(self, index, value):
            """Sets a component, given its index.
     
            index -- 0, 1 or 2 for x, y or z
            value -- New (float) value of component
     
            """
     
            try:
                self._v[index] = 1.0 * value
            except IndexError:
                raise IndexError("There are 3 values in this object, index should be 0, 1 or 2!")
            except TypeError:
                raise TypeError("Must be a number")
     
     
        def __eq__(self, rhs):
     
            """Test for equality
     
            rhs -- Vector or sequence of 3 values
     
            """
     
            x, y, z = self._v
            xx, yy, zz = rhs
            return x==xx and y==yy and z==zz
     
        def __ne__(self, rhs):
     
            """Test of inequality
     
            rhs -- Vector or sequenece of 3 values
     
            """
     
            x, y, z = self._v
            xx, yy, zz = rhs
            return x!=xx or y!=yy or z!=zz
     
        def __hash__(self):
     
            return hash(self._v)
     
        def __add__(self, rhs):
            """Returns the result of adding a vector (or collection of 3 numbers)
            from this vector.
     
            rhs -- Vector or sequence of 2 values
     
            """
     
            x, y, z = self._v
            ox, oy, oz = rhs
            return self.from_floats(x+ox, y+oy, z+oz)
     
     
        def __iadd__(self, rhs):
            """Adds another vector (or a collection of 3 numbers) to this vector.
     
            rhs -- Vector or sequence of 2 values
     
            """
            ox, oy, oz = rhs
            v = self._v
            v[0] += ox
            v[1] += oy
            v[2] += oz
            return self
     
     
        def __radd__(self, lhs):
     
            """Adds vector to this vector (right version)
     
            lhs -- Left hand side vector or sequence
     
            """
     
            x, y, z = self._v
            ox, oy, oz = lhs
            return self.from_floats(x+ox, y+oy, z+oz)
     
     
     
        def __sub__(self, rhs):
            """Returns the result of subtracting a vector (or collection of
            3 numbers) from this vector.
     
            rhs -- 3 values
     
            """
     
            x, y, z = self._v
            ox, oy, oz = rhs
            return self.from_floats(x-ox, y-oy, z-oz)
     
     
        def _isub__(self, rhs):
            """Subtracts another vector (or a collection of 3 numbers) from this
            vector.
     
            rhs -- Vector or sequence of 3 values
     
            """
     
            ox, oy, oz = rhs
            v = self._v
            v[0] -= ox
            v[1] -= oy
            v[2] -= oz
            return self
     
        def __rsub__(self, lhs):
     
            """Subtracts a vector (right version)
     
            lhs -- Left hand side vector or sequence
     
            """
     
            x, y, z = self._v
            ox, oy, oz = lhs
            return self.from_floats(ox-x, oy-y, oz-z)
     
        def scalar_mul(self, scalar):
     
            v = self._v
            v[0] *= scalar
            v[1] *= scalar
            v[2] *= scalar
     
        def vector_mul(self, vector):
     
            x, y, z = vector
            v= self._v
            v[0] *= x
            v[1] *= y
            v[2] *= z
     
        def get_scalar_mul(self, scalar):
     
            x, y, z = self._v
            return self.from_floats(x*scalar, y*scalar, z*scalar)
     
        def get_vector_mul(self, vector):
     
            x, y, z = self._v
            xx, yy, zz = vector
            return self.from_floats(x * xx, y * yy, z * zz)
     
        def __mul__(self, rhs):
            """Return the result of multiplying this vector by another vector, or
            a scalar (single number).
     
     
            rhs -- Vector, sequence or single value.
     
            """
     
            x, y, z = self._v
            if hasattr(rhs, "__getitem__"):
                ox, oy, oz = rhs
                return self.from_floats(x*ox, y*oy, z*oz)
            else:
                return self.from_floats(x*rhs, y*rhs, z*rhs)
     
     
        def __imul__(self, rhs):
            """Multiply this vector by another vector, or a scalar
            (single number).
     
            rhs -- Vector, sequence or single value.
     
            """
     
            v = self._v
            if hasattr(rhs, "__getitem__"):
                ox, oy, oz = rhs
                v[0] *= ox
                v[1] *= oy
                v[2] *= oz
            else:
                v[0] *= rhs
                v[1] *= rhs
                v[2] *= rhs
     
            return self
     
        def __rmul__(self, lhs):
     
            x, y, z = self._v
            if hasattr(lhs, "__getitem__"):
                ox, oy, oz = lhs
                return self.from_floats(x*ox, y*oy, z*oz)
            else:
                return self.from_floats(x*lhs, y*lhs, z*lhs)
     
     
        def __div__(self, rhs):
            """Return the result of dividing this vector by another vector, or a scalar (single number)."""
     
            x, y, z = self._v
            if hasattr(rhs, "__getitem__"):
                ox, oy, oz = rhs
                return self.from_floats(x/ox, y/oy, z/oz)
            else:
                return self.from_floats(x/rhs, y/rhs, z/rhs)
     
     
        def __idiv__(self, rhs):
            """Divide this vector by another vector, or a scalar (single number)."""
     
            v = self._v
            if hasattr(rhs, "__getitem__"):
                v[0] /= ox
                v[1] /= oy
                v[2] /= oz
            else:
                v[0] /= rhs
                v[1] /= rhs
                v[2] /= rhs
     
            return self
     
     
        def __rdiv__(self, lhs):
     
            x, y, z = self._v
            if hasattr(lhs, "__getitem__"):
                ox, oy, oz = lhs
                return self.from_floats(ox/x, oy/y, oz/z)
            else:
                return self.from_floats(lhs/x, lhs/y, lhs/z)
     
        def scalar_div(self, scalar):
     
            v = self._v
            v[0] /= scalar
            v[1] /= scalar
            v[2] /= scalar
     
        def vector_div(self, vector):
     
            x, y, z = vector
            v= self._v
            v[0] /= x
            v[1] /= y
            v[2] /= z
     
        def get_scalar_div(self, scalar):
     
            x, y, z = self.scalar
            return self.from_floats(x / scalar, y / scalar, z / scalar)
     
        def get_vector_div(self, vector):
     
            x, y, z = self._v
            xx, yy, zz = vector
            return self.from_floats(x / xx, y / yy, z / zz)
     
        def __neg__(self):
            """Returns the negation of this vector (a vector pointing in the opposite direction.
            eg v1 = Vector(1,2,3)
            print -v1
            >>> (-1,-2,-3)
     
            """
            x, y, z = self._v
            return self.from_floats(-x, -y, -z)
     
        def __pos__(self):
     
            return self.copy()
     
     
        def __nonzero__(self):
     
            x, y, z = self._v
            return bool(x or y or z)
     
     
        def __call__(self, keys):
            """Returns a tuple of the values in a vector
     
            keys -- An iterable containing the keys (x, y or z)
            eg v = Vector3(1.0, 2.0, 3.0)
            v('zyx') -> (3.0, 2.0, 1.0)
     
            """
            ord_x = ord('x')
            v = self._v
            return tuple( v[ord(c)-ord_x] for c in keys )
     
     
        def as_tuple(self):
            """Returns a tuple of the x, y, z components. A little quicker than
            tuple(vector)."""
     
            return tuple(self._v)
     
     
        def scale(self, scale):
            """Scales the vector by onther vector or a scalar. Same as the
            *= operator.
     
            scale -- Value to scale the vector by
     
            """
            v = self._v
            if hasattr(scale, "__getitem__"):
                ox, oy, oz = scale
                v[0] *= ox
                v[1] *= oy
                v[2] *= oz
            else:
                v[0] *= scale
                v[1] *= scale
                v[2] *= scale
     
            return self
     
     
        def get_length(self):
            """Calculates the length of the vector."""
     
            x, y, z = self._v
            return sqrt(x*x + y*y +z*z)
        get_magnitude = get_length
     
        def set_length(self, new_length):
            """Sets the length of the vector. (Normalises it then scales it)
     
            new_length -- The new length of the vector.
     
            """
            v = self._v
            try:
                x, y, z = v
                l = new_length / sqrt(x*x + y*y + z*z)
            except ZeroDivisionError:
                v[0] = 0.0
                v[1] = 0.0
                v[2] = 0.0
                return self
     
            v[0] = x*l
            v[1] = y*l
            v[2] = z*l
     
            return self
     
     
        def get_distance_to(self, p):
            """Returns the distance of this vector to a point.
     
            p -- A position as a vector, or collection of 3 values.
     
            """
            ax, ay, az = self._v
            bx, by, bz = p
            dx = ax-bx
            dy = ay-by
            dz = az-bz
            return sqrt( dx*dx + dy*dy + dz*dz )
     
     
        def get_distance_to_squared(self, p):
            """Returns the squared distance of this vector to a point.
     
            p -- A position as a vector, or collection of 3 values.
     
            """
            ax, ay, az = self._v
            bx, by, bz = p
            dx = ax-bx
            dy = ay-by
            dz = az-bz
            return dx*dx + dy*dy + dz*dz
     
     
        def normalise(self):
            """Scales the vector to be length 1."""
            v = self._v
            x, y, z = v
            l = sqrt(x*x + y*y + z*z)
            try:
                v[0] /= l
                v[1] /= l
                v[2] /= l
            except ZeroDivisionError:
                v[0] = 0.0
                v[1] = 0.0
                v[2] = 0.0
            return self
        normalize = normalise
     
        def get_normalised(self):
     
            x, y, z = self._v
            l = sqrt(x*x + y*y + z*z)
            return self.from_floats(x/l, y/l, z/l)
        get_normalized = get_normalised
     
     
        def in_sphere(self, sphere):
            """Returns true if this vector (treated as a position) is contained in
            the given sphere.
     
            """
     
            return distance3d(sphere.position, self) <= sphere.radius
     
     
        def dot(self, other):
     
            """Returns the dot product of this vector with another.
     
            other -- A vector or tuple
     
            """
            x, y, z = self._v
            ox, oy, oz = other
            return x*ox + y*oy + z*oz
     
        def cross(self, other):
     
            """Returns the cross product of this vector with another.
     
            other -- A vector or tuple
     
            """
     
            x, y, z = self._v
            bx, by, bz = other
            return self.from_floats( y*bz - by*z,
                                     z*bx - bz*x,
                                     x*by - bx*y )
     
        def cross_tuple(self, other):
     
            """Returns the cross product of this vector with another, as a tuple.
            This avoids the Vector3 construction if you don't need it.
     
            other -- A vector or tuple
     
            """
     
            x, y, z = self._v
            bx, by, bz = other
            return ( y*bz - by*z,
                     z*bx - bz*x,
                     x*by - bx*y )
     
     
def distance3d_squared(p1, p2):
    x, y, z = p1
    xx, yy, zz = p2
    dx = x - xx
    dy = y - yy
    dz = z - zz
    return dx*dx + dy*dy +dz*dz
def distance3d(p1, p2):
    x, y, z = p1
    xx, yy, zz = p2
    dx = x - xx
    dy = y - yy
    dz = z - zz
    return sqrt(dx*dx + dy*dy +dz*dz)
def centre_point3d(points):
    return sum( Vector3(p) for p in points ) / len(points)
