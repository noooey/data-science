class Matrix:
    def __init__(self, data):
      self.data = data
    
    def __repr__(self):
      return f"Matrix({self.data})"
    
    def __add__(self, other):
      assert len(self.data) == len(other.data)
      mrx = []
      tmp = []
      for row_x, row_y in zip(self.data, other.data):
        assert len(row_x) == len(row_y)
        tmp = [x + y for x, y in zip(row_x, row_y)]
        mrx.append(tmp)
      return Matrix(mrx)
    
    def __sub__(self, other):
      assert len(self.data) == len(other.data)
      mrx = []
      tmp = []
      for row_x, row_y in zip(self.data, other.data):
        assert len(row_x) == len(row_y)
        tmp = [x - y for x, y in zip(row_x, row_y)]
        mrx.append(tmp)
      return Matrix(mrx)
    
    def __mul__(self, other):
      mrx = []
      if type(other) == Matrix:  # 행렬 간의 연산
        for i in range(len(self.data)):
          tmp = []
          assert len(self.data[i]) == len(other.data)
          for k in range(len(other.data[i])):
            tmp.append(sum(self.data[i][j] * other.data[j][k] for j in range(len(self.data[i]))))
          mrx.append(tmp)
        return Matrix(mrx)
      else:  # 스칼라 값이 있는 연산
        for row_x in self.data:
          tmp = []
          tmp = [x * other for x in row_x]
          mrx.append(tmp)
        return Matrix(mrx)
  
    def __rmul__(self, other):   #  스칼라 값이 앞에 있는 연산
      mrx = []
      tmp = []
      for row_x in self.data:
        tmp = [x * other for x in row_x]
        mrx.append(tmp)
      return Matrix(mrx)

