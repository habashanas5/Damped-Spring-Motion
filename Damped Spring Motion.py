import matplotlib.pyplot as plt

# Constants
mass = 0.5  # Mass of the object (kg)
k = 10.0    # Spring constant (N/m)
acceleration_due_to_gravity = 9.81
weight = mass * acceleration_due_to_gravity
unweighted_length = 0.5  # Damping coefficient (N*s/m)
initial_position = 1.0  # Initial position (m)
initial_velocity = 0.0  # Initial velocity (m/s)
time_step = 0.01  # Time step (s)

# Arrays to store the simulation data
t = []
p = []
v = []

# Initial conditions
time = 0.0
position = initial_position
velocity = initial_velocity
duration = 10.0
iteration = int(duration / time_step)
for time in range(iteration):
    t.append(time)
    p.append(position)
    v.append(velocity)

    # Calculate acceleration using F = ma

    acceleration = (-k * position - unweighted_length * velocity + weight) / mass

    # Update position and velocity using the Euler method
    position += velocity * time_step
    velocity += acceleration * time_step

    time += time_step

# Plot the damped spring motion
plt.figure(figsize=(10, 6))
plt.plot(t, p, label='Position (m)')
plt.plot(t, v, label='Velocity (m/s)')
plt.xlabel('Time (s)')
plt.title('Damped Spring Motion')
plt.legend()
plt.grid(True)
plt.show()
