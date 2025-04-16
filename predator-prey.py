import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Lotka-Volterra equations
def predator_prey_system(state, t, alpha, beta, delta, gamma):
    x, y = state
    dxdt = alpha*x - beta*x*y
    dydt = delta*x*y - gamma*y
    return [dxdt, dydt]

# Parameters
alpha = 0.6    # Prey birth rate
beta = 0.02    # Predation rate
delta = 0.01   # Predator reproduction rate
gamma = 0.3    # Predator death rate

# Initial populations
x0 = 40  # Prey
y0 = 9   # Predator
state0 = [x0, y0]

# Time points
t = np.linspace(0, 200, 1000)

# Solve the differential equations
solution = odeint(predator_prey_system, state0, t, args=(alpha, beta, delta, gamma))
x_values, y_values = solution.T

# Plot results
plt.figure(figsize=(10,5))
plt.plot(t, x_values, label="Prey", color="blue")
plt.plot(t, y_values, label="Predators", color="red")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.title("Predator-Prey Model")
plt.show()
