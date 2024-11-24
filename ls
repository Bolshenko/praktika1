import numpy as np
import matplotlib.pyplot as plt

def generate_cities(num_cities, size):
    """Генерация координат случайных городов на полигоне."""
    return np.random.rand(num_cities, 2) * size

def calculate_distance(city1, city2):
    """Расчет евклидова расстояния между двумя городами."""
    return np.linalg.norm(city1 - city2)

def greedy_tsp(cities, size):
    """Жадный алгоритм для решения задачи коммивояжера."""
    num_cities = len(cities)
    visited = [False] * num_cities
    current_city = 0
    tour = [current_city]
    visited[current_city] = True

    total_distance = 0  # Переменная для суммирования длины маршрута

    # Визуализация начальной точки
    update_plot(cities, tour, size, total_distance)

    for _ in range(num_cities - 1):
        closest_city = -1
        closest_distance = float('inf')

        for city in range(num_cities):
            if not visited[city]:
                distance = calculate_distance(cities[current_city], cities[city])
                if distance < closest_distance:
                    closest_distance = distance
                    closest_city = city

        # Добавляем длину между текущим городом и ближайшим
        distance_to_closest = calculate_distance(cities[current_city], cities[closest_city])
        total_distance += distance_to_closest

        tour.append(closest_city)
        visited[closest_city] = True
        current_city = closest_city

        # Визуализируем текущее состояние маршрута
        update_plot(cities, tour, size, total_distance)

    # Вернуться в начальный город
    distance_to_start = calculate_distance(cities[current_city], cities[tour[0]])
    total_distance += distance_to_start
    tour.append(tour[0])

    update_plot(cities, tour, size, total_distance)  # Финальная визуализация
    return tour, total_distance

def update_plot(cities, tour, size, total_distance):
    """Обновление графика с текущим маршрутом."""
    plt.clf()  # Очистка текущего графика
    plt.plot(cities[:, 0], cities[:, 1], 'ro')  # Рисуем города

    for i in range(len(tour) - 1):
        plt.plot(cities[tour[i:i+2], 0], cities[tour[i:i+2], 1], 'b-')  # Рисуем маршрут

        # Рассчитываем и отображаем длину между городами
        city1 = cities[tour[i]]
        city2 = cities[tour[i + 1]]
        length = calculate_distance(city1, city2)
        mid_point = (city1 + city2) / 2  # Находим середину отрезка
        plt.text(mid_point[0]+0.5, mid_point[1], f"{length:.2f}", fontsize=10, ha='center', va='bottom')

    # Добавление подписей к каждому городу
    for index, city in enumerate(cities):
        plt.text(city[0]+0.5, city[1]+0.2, f"{index + 1} город", fontsize=10, ha='right', color="red")

    plt.title("Текущий маршрут")
    plt.xlim(0, size)  # Установка пределов по оси X
    plt.ylim(0, size)  # Установка пределов по оси Y


    # Добавление текста с общей длиной маршрута ниже графика
    plt.figtext(0.5, 0.01, f"Сумма длины маршрута: {total_distance:.2f}", ha='center', fontsize=12)

def main():
    num_cities = 6
    size = 6

    cities = generate_cities(num_cities, size)
    greedy_tsp(cities, size)
    plt.savefig('my_plot.png')


if __name__ == "__main__":
    main()
