from pulp import LpProblem, LpMaximize, LpVariable, value, LpStatus

# --- 1. DATI E OBIETTIVI (Dizionario Python, sostituisce MySQL) ---
# Scores (Punteggio di soddisfazione 1-10) per le categorie
SATISFACTION_SCORES = {
    'Food': 8,
    'Transport': 3,
    'Entertainment': 9,
    'Savings': 10 
}

def calculate_optimized_budget(max_budget, min_savings, scores=SATISFACTION_SCORES):
    """
    Uses Linear Programming (PuLP) to optimize future spending based on constraints.
    Returns the optimal allocation and the status of the solution.
    """
    
    # Initialize the LP problem (Maximization)
    prob = LpProblem("BudgetOptimizer", LpMaximize)
    
    # Decision Variables: x_category = amount to spend in that category
    x_vars = LpVariable.dicts("Spend", scores.keys(), lowBound=0)
    
    # --- Objective Function: Maximize total satisfaction ---
    prob += sum([x_vars[cat] * score for cat, score in scores.items()]), "Total Satisfaction"

    # --- Constraints ---
    
    # 1. Total Budget Constraint
    prob += sum(x_vars.values()) <= max_budget, "Max Budget Constraint"
    
    # 2. Minimum Savings Constraint
    prob += x_vars['Savings'] >= min_savings, "Min Savings Constraint"
    
    # 3. Max Limit for Entertainment (Example constraint)
    prob += x_vars['Entertainment'] <= 50, "Max Entertainment Spend"

    # --- Solve the problem ---
    prob.solve()
    
    # --- Format Results ---
    results = {
        "status": LpStatus[prob.status],
        "total_satisfaction": value(prob.objective),
        "allocation": {}
    }
    
    for v in prob.variables():
        if value(v) is not None and value(v) > 0:
            results["allocation"][v.name.replace('Spend_', '')] = value(v)
            
    return results

def run_test_case():
    """Runs a single test case for demonstration."""
    
    print("\n--- RUNNING STANDALONE OPTIMIZATION MODULE ---")
    
    # TEST CASE
    budget = 300
    savings = 50
    
    result = calculate_optimized_budget(budget, savings)
    
    print(f"\nOptimization Parameters: Max Budget €{budget}, Min Savings €{savings}")
    print(f"Solution Status: {result['status']}")
    
    if result['status'] == 'Optimal':
        print(f"Max Satisfaction Achieved: {result['total_satisfaction']:.2f}")
        print("\nOptimal Allocation Suggestion:")
        total_spent = 0
        for category, amount in result['allocation'].items():
            print(f"- {category}: {amount:.2f} €")
            total_spent += amount
        print(f"\nTotal Budget Allocated: {total_spent:.2f} €")
    else:
        print("Optimization failed or is infeasible.")


if __name__ == "__main__":
    run_test_case()