import numpy as np
import matplotlib.pyplot as plt
import time


def calc_accelerations_1(positions, masses, gravitational_constant=1.0):
    """
    Calculates accelerations due to gravitational forces
    :param positions: numpy array of size (n, 3)
    :param masses: numpy array of size (n,)
    :param gravitational_constant:
    :return: accelerations, numpy array of size (n, 3)
    """

    n_bodies = masses.shape[0]
    accels = np.zeros(shape=(n_bodies, 3)) # n_bodies * (x,y,z)

    for i in range(n_bodies):
        for j in range(n_bodies):
            if i != j:
                distance = positions[j] - positions[i]
                accels[i] += gravitational_constant * masses[j] * distance / np.linalg.norm(distance)**3

    return accels


def calc_accelerations_2(positions, masses, gravitational_constant=1.0):
    """
    Calculates accelerations due to gravitational forces
    :param positions: numpy array of size (n, 3)
    :param masses: numpy array of size (n,)
    :param gravitational_constant:
    :return: accelerations, numpy array of size (n, 3)
    """
    mass_matrix = masses.reshape((1, -1, 1)) * masses.reshape((-1, 1, 1))
    displacements = positions.reshape((1, -1, 3)) - positions.reshape((-1, 1, 3))
    distances = np.linalg.norm(displacements, axis=2)
    distances[distances == 0] = 0.001 # avoid divide by zero
    forces = gravitational_constant * displacements * mass_matrix / np.expand_dims(distances, 2)**3
    return forces.sum(axis=1) / masses.reshape(-1, 1)


def move_bodies(positions, velocities, accelerations, dt):
    """
    Moves bodies using naive integration scheme
    :param positions: numpy array of size (n, 3)
    :param velocities: numpy array of size (n, 3)
    :param accelerations: numpy array of size (n, 3)
    :param dt: time step
    """
    positions += (velocities * dt + accelerations * dt * dt / 2.0)
    velocities += (accelerations * dt)


def calculate(positions, masses, velocities, dt, steps):
    n_bodies = masses.shape[0]
    locations = np.zeros(shape=(n_bodies, 3, steps))

    for s in range(steps):
        locations[:, :, s] = np.copy(positions)
        accels = calc_accelerations_2(positions, masses)
        move_bodies(positions, velocities, accels, dt)

    return locations


def get_small_problem():
    n = 3
    positions = np.array([[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, -1.0, 0.0]])
    masses = np.array([1000000, 1, 1])
    velocities = np.array([[0.0, 0.0, 0.0], [1000.0, 0.0, 0.0], [-1250.0, 0.0, 0.0]])
    return n, positions, masses, velocities


def get_large_problem(n = 2):
    angles = np.random.uniform(0, 2*np.pi, n)

    positions = np.zeros(shape=(n + 1, 3))
    positions[1:, 0] = np.sin(angles)
    positions[1:, 1] = np.cos(angles)

    masses = np.ones(shape=(n + 1, 1))
    masses[0] = 1000000

    v_modules = np.random.uniform(1000, 1100, n)
    velocities = np.zeros(shape=(n + 1, 3))
    velocities[1:, 0] = v_modules * np.cos(angles)
    velocities[1:, 1] = - v_modules * np.sin(angles)

    return n + 1, positions, masses, velocities


n_bodies, positions, masses, velocities = get_large_problem(100)
dt = 1e-6
steps = 10000

start_time = time.time()
locations = calculate(positions, masses, velocities, dt, steps)
print("Calc time: ", time.time() - start_time)

start_time = time.time()

fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
for i in range(n_bodies):
    ax.scatter(locations[i, 0, ::100], locations[i, 1, ::100], s = 1 * np.power(masses[i], 0.333))

print("Draw time: ", time.time() - start_time)

plt.show()
