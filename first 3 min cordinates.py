def find_index(array, value):
    for i in range(len(array)):
        if array[i][0] == value:
            return i
    return -1

def find_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def find_min_in_array(array):
    min_value = array[0]
    for i in array:
        if i < min_value:
            min_value = i
    return min_value

for _ in range(int(input())):
    numberOfPoints = int(input())
    points = []
    x_cordinates_with_index = []
    y_cordinates_with_index = []
    for i in range(numberOfPoints):
        setOfPoints = tuple(map(float, input().split()))
        points.append(setOfPoints)
        x_cordinates_with_index.append((i, setOfPoints[0]))
        y_cordinates_with_index.append((i, setOfPoints[1]))
    
    #print(points, 'all points')

    # sort the points based on x cordinate
    x_cordinates_with_index.sort(key=lambda x: x[1])
    #print(x_cordinates_with_index, 'x_cordinates_with_index')
    # sort the points based on y cordinate
    y_cordinates_with_index.sort(key=lambda x: x[1])
    #print(y_cordinates_with_index, 'y_cordinates_with_index')

    sum_list = []
    for i in range(len(x_cordinates_with_index)):
        sum_list.append(find_index(x_cordinates_with_index, i) + find_index(y_cordinates_with_index, i))
    
    sorted_sum_list = sorted(sum_list)
    #print(sum_list, 'sum_list')
    #print(sorted_sum_list, 'sorted_sum_list')
    if sorted_sum_list[2] == sorted_sum_list[3]:
        indexes = []
        indexes.append(sum_list.index(sorted_sum_list[0]))
        indexes.append(sum_list.index(sorted_sum_list[1]))
        indexes.append(sum_list.index(sorted_sum_list[2]))
        indexes.append(sum_list.index(sorted_sum_list[3]))
        print('Case {}:'.format(_+1), min(find_distance(points[indexes[0]], points[indexes[1]]) + find_distance(points[indexes[1]], points[indexes[2]]) + find_distance(points[indexes[2]], points[indexes[3]]) + find_distance(points[indexes[3]], points[indexes[0]]), find_distance(points[indexes[0]], points[indexes[2]]) + find_distance(points[indexes[2]], points[indexes[1]]) + find_distance(points[indexes[1]], points[indexes[3]]) + find_distance(points[indexes[3]], points[indexes[0]])))

    else:
        indexes = []
        indexes.append(sum_list.index(sorted_sum_list[0]))
        indexes.append(sum_list.index(sorted_sum_list[1]))
        indexes.append(sum_list.index(sorted_sum_list[2]))
        print('Case {}:'.format(_+1), find_distance(points[indexes[0]], points[indexes[1]]) + find_distance(points[indexes[1]], points[indexes[2]]) + find_distance(points[indexes[2]], points[indexes[0]]))
    #print(indexes, 'indexes')
    #print(find_distance(points[indexes[0]], points[indexes[1]]), 'distance between 1 and 2')
    #print(find_distance(points[indexes[1]], points[indexes[2]]), 'distance between 2 and 3')
    #print(find_distance(points[indexes[2]], points[indexes[0]]), 'distance between 3 and 1')