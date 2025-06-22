from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value

model = LpProblem("Optimization_of_Production", LpMaximize)

x1 = LpVariable("Lemonade", lowBound=0, cat="Continuous")
x2 = LpVariable("Fruit_Juice", lowBound=0, cat="Continuous")

model += x1 + x2, "Total_Production"

model += 2 * x1 + 1 * x2 <= 100, "Water_Constraint"
model += 1 * x1 <= 50, "Sugar_Constraint"
model += 1 * x1 <= 30, "Lemon_Juice_Constraint"
model += 2 * x2 <= 40, "Fruit_Puree_Constraint"

model.solve()

results = {
    "Status": LpStatus[model.status],
    "Lemonade": x1.varValue,
    "Fruit_Juice": x2.varValue,
    "Total Production": value(model.objective),
}

print(results)