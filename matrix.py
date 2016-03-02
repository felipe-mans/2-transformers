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
  return [[1, 0, 0, 0],
          [0, math.cos(theta), math.sin(theta) * -1, 0],
          [0, math.sin(theta), math.cos(theta), 0],
          [0, 0, 0, 1]]

def make_rotY( theta ):
  return [[math.cos(theta), 0, math.sin(theta) * -1, 0],
          [0, 1, 0, 0],
          [math.sin(theta), 0, math.cos(theta), 0],
          [0, 0, 0, 1]]

def make_rotZ( theta ):
  return [[math.cos(theta), math.sin(theta) * -1, 0, 0],
          [math.sin(theta), math.cos(theta), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
  result = ''
  for x in range( len(matrix) ):
    for y in range( len(matrix[x]) ):
      result += str(matrix[x][y]) + '\t'
    result += '\n'
    print result

def ident( matrix ):
    result = new_matrix( len(matrix), len(matrix) )
    for x in range( len(matrix) ):
      m[x][x] = 1
    return result

def scalar_mult( matrix, x ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
  result = new_matrix( len(m2[0]), len(m1) )
  for x in range( len(m1) ):
    for y in range( len(m2[0]) ):
        sum = 0
        for i in range(len(m2)):
          sum += m1[x][i] * m2[i][y]
        m[x][y] = sum
  return result
