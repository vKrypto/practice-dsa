def getMaximumPoints_space_optimized(days, k):
    def get_point(index):
        try:
            return points[index]
        except:
            temp = 0
            for num_days in days:
                if temp + num_days > index:
                    return index - temp
                temp += num_days
    
    points = []
    for num_days in days:
        if len(points) + num_days >= 5000:
            break
        points.extend(range(1, num_days + 1))
    
    total_days = sum(days)

    max_points = 0
    current_window_sum = sum(points[:k])
    max_points = current_window_sum
    
    i = 1
    for i in range(1, total_days):
        current_window_sum = current_window_sum - get_point((i - 1) % total_days) + get_point((i + k - 1) % total_days)
        max_points = max(max_points, current_window_sum)

    return max_points
    
def getMaximumPoints(days, k):
    total_days = sum(days)
    
    points = []
    for day_index, num_days in enumerate(days):
        points.extend(range(1, num_days + 1))
        if len(points) >= k:
            break
    max_points = 0
    current_window_sum = sum(points[:k])
    max_points = current_window_sum


    data = {'size': len(points), "index": day_index}    
    def get_point(index):
        if index >= len(points):
            while data['size']  + days[data['index']+1] <= index:
                data['size']  += days[data['index']+1]    
                data['index'] += 1
            return index - data['size']
                
        return points[index]
    
    for i in range(1, total_days):
        a = get_point((i - 1) % total_days)
        b = get_point((i + k - 1) % total_days)
        current_window_sum = current_window_sum - a + b
        max_points = max(max_points, current_window_sum)
    
    return max_points

days = [2,3,2]
k = 2
print(getMaximumPoints(days, k)) 