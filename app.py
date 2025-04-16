from flask import Flask, render_template, request
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint

app = Flask(__name__)

def predator_prey_system(state, t, alpha, beta, delta, gamma, K, epsilon):
    x, y = state
    dxdt = alpha * x * (1 - x/K) - beta * x * y
    dydt = delta * x * y - gamma * y - epsilon * y**2
    return [dxdt, dydt]

@app.route("/", methods=["GET", "POST"])
def index():
    alpha = float(request.form.get("alpha", 0.6))
    beta = float(request.form.get("beta", 0.02))
    delta = float(request.form.get("delta", 0.01))
    gamma = float(request.form.get("gamma", 0.3))
    K = int(request.form.get("K", 100))
    epsilon = float(request.form.get("epsilon", 0.01))

    x0, y0 = 40, 9
    t = np.linspace(0, 200, 5000)
    solution = odeint(predator_prey_system, [x0, y0], t, args=(alpha, beta, delta, gamma, K, epsilon))
    x_values, y_values = solution.T

    matplotlib.use("Agg")
    plt.figure(figsize=(10, 5))
    plt.plot(t, x_values, label="Prey", color="blue")
    plt.plot(t, y_values, label="Predators", color="red")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("Predator-Prey Simulation")
    plt.legend()
    plt.savefig("static/plot.png")
    plt.close()

    return render_template("index.html", img_url="static/plot.png")

if __name__ == "__main__":
    app.run(debug=False, threaded=False, port=5000)
