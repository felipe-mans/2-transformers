import math

def make_translate( x, y, z ):
  return [[1, 0, 0, x],
          [0, 1, 0, y],
          [0, 0, 1, z],
          [0, 0, 0, 1]]

def make_scale( x, y, z ):
  return [[x, 0, 0, 0],
          [0, y, 0, 0],
          [0, 0, z, 0],
          [0, 0, 0, 1]]

def make_rotX( theta ):
  deg = math.radians( theta )
  return [[1, 0, 0, 0],
          [0, math.cos(deg), math.sin(deg) * -1, 0],
          [0, math.sin(deg), math.cos(deg), 0],
          [0, 0, 0, 1]]

def make_rotY( theta ):
  deg = math.radians( theta )
  return [[math.cos(deg), 0, math.sin(deg) * -1, 0],
          [0, 1, 0, 0],
          [math.sin(deg), 0, math.cos(deg), 0],
          [0, 0, 0, 1]]

def make_rotZ( theta ):
  deg = math.radians( theta )
  return [[math.cos(deg), math.sin(deg) * -1, 0, 0],
          [math.sin(deg), math.cos(deg), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

def print_matrix( matrix ):
  result = '\n'
  for x in range( len(matrix) ):
    for y in range( len(matrix[x]) ):
      result += str(matrix[x][y]) + '\t'
    result += '\n'
  print result

def ident( matrix ):
  result = new_matrix( len(matrix), len(matrix) )
  for x in range( len(matrix) ):
    result[x][x] = 1
  return result

def scalar_mult( matrix, x ):
  scale = make_scale( x, x, x)
  return matrix_mult(scale, matrix)

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
  result = new_matrix( len(m1), len(m2[0]) )
  for x in range( len(m1) ):
    for y in range( len(m2[0]) ):
        sum = 0
        for i in range(len(m2)):
          sum += m1[x][i] * m2[i][y]
        result[x][y] = sum
  return result
