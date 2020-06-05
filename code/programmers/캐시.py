def solution(cacheSize, cities):
    if cacheSize >= len(cities):
        return len(cities) + len(set(cities)) * 4
    if cacheSize == 0:
        return len(cities) * 5
    cities = [city.lower() for city in cities]
    cache = []
    time = 0
    for city in cities:
        if city in cache:
            time += 1
            cache.pop(cache.index(city))
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
        cache.append(city)
    return time
