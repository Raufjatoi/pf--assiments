mat1 = [[1,2,3,4],[5,6,7,8]]
mat2 = [[9,10,11,12],[13,14,15,16]]

# Initialize mat3 with appropriate dimensions:
mat3 = [[0 for col in range(len(mat1[0]))] for row in range(len(mat1))]

# Iterate through rows and columns using numerical indices:
for i in range(len(mat1)):
  for j in range(len(mat1[0])):  # Use j for column index
    mat3[i][j]= mat1[i][j] + mat2[i][j]  # Add corresponding elements

print(mat3)
