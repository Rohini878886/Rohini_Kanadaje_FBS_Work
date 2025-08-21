area = float(input("Enter the area of one wall:"))
cost_interior = float(input("Enter the cost of interior wall:"))
cost_exterior = float(input("enetr the cost of exterior wall:"))

interior_wall_cost = area * cost_interior
exterior_wall_cost = area * cost_exterior
total_cost = interior_wall_cost + exterior_wall_cost

print(f"cost of interior wall:{interior_wall_cost}")
print(f"cost of exterior wall:{exterior_wall_cost}")
print(f"totsl cost is :{total_cost}")