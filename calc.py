class FIRECalculator:
    def __init__(self, initial_amount, rate_of_return, initial_salary, salary_growth_rate, current_expenses, current_expenses_growth_rate, fire_monthly_expenses, withdrawal_rate):
        self.INITIAL_AMOUNT = initial_amount

        self.RATE_OF_RETURN = rate_of_return                                # Real rate of return (- inflation)

        self.SALARY = initial_salary                                        # After tax
        self.SALARY_GROWTH_RATE = salary_growth_rate

        self.CURRENT_EXPENSES = current_expenses                            
        self.CURRENT_EXPENSES_GROWTH_RATE = current_expenses_growth_rate    

        self.FIRE_EXPENSES = fire_monthly_expenses                          # Monthly expenses in FIRE, including capital gains tax/other taxes
        self.WITHDRAWAL_RATE = withdrawal_rate                              # Annual withdrawal rate

        self.TARGET = (self.FIRE_EXPENSES * 12) / self.WITHDRAWAL_RATE      # Target portfolio value in order to FIRE

    def calculate(self):
        print("\n////////////////////\n//// CALCULATE ////\n////////////////////\n")
        PORTFOLIO = self.INITIAL_AMOUNT

        SALARY = self.SALARY
        EXPENSES = self.CURRENT_EXPENSES

        y = 0

        while PORTFOLIO < self.TARGET:
            PORTFOLIO += SALARY - EXPENSES

            SALARY *= self.SALARY_GROWTH_RATE
            EXPENSES *= self.CURRENT_EXPENSES_GROWTH_RATE
        
            y += 1
        
        print("You can retire after ~{} year{} | Estimated net worth: {:,.0f} | Target: {:,.0f}".format(y, "" if y == 1 else "s", PORTFOLIO, self.TARGET))
    
    def simulate(self, years):
        print("\n////////////////////\n//// SIMULATION ////\n////////////////////\n")

        PORTFOLIO = self.INITIAL_AMOUNT

        SALARY = self.SALARY
        EXPENSES = self.CURRENT_EXPENSES

        print("Current net worth: {:,.0f} | Current salary (after tax): {:,.0f} | Current expenses: {:,.0f}".format(PORTFOLIO, SALARY, EXPENSES))

        for y in range(1, years + 1):
            PORTFOLIO += SALARY - EXPENSES

            SALARY *= self.SALARY_GROWTH_RATE
            EXPENSES *= self.CURRENT_EXPENSES_GROWTH_RATE

            print("After {} year{} | Current net worth: {:,.0f} | Current salary (after tax): {:,.0f} | Current expenses: {:,.0f}".format(y, "" if y == 1 else "s", PORTFOLIO, SALARY, EXPENSES))


def main():
    kwargs = {"initial_amount": 0,
              "rate_of_return": 1.07,
              "initial_salary": 55000, 
              "salary_growth_rate": 1.10, 
              "current_expenses": 35000, 
              "current_expenses_growth_rate": 1.03, 
              "fire_monthly_expenses": 1280,
              "withdrawal_rate": 0.0333}
    
    FIRECalc = FIRECalculator(**kwargs)

    FIRECalc.calculate()
    FIRECalc.simulate(15)

if __name__ == "__main__":
    main()