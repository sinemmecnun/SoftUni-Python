def start_spring(**kwargs):
    spring_time = {}
    for key, value in kwargs.items():
        if value not in spring_time.keys():
            spring_time[value] = []
        spring_time[value].append(key)
    sorted_spring = sorted(spring_time.items(), key=lambda kvpt: (- len(kvpt[1]), kvpt[0]))
    result = ''
    for key, value in sorted_spring:
        result += key + ':\n'
        for flower in sorted(value):
            result += f'-{flower}\n'
    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


