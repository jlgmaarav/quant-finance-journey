import math
import random

NUM_PHARMACIES = 100
NUM_CLIENTS = 3000      
CITY_SIZE = 10.0        
NUM_DAYS = 365          

# Economic constants
COST_PRICE = 6.0       
SALE_PRICE = 10.0       
INITIAL_CAPITAL = 1000  


class Pharmacy:
    def __init__(self, pharmacy_id, position, strategy, initial_stock):
        self.pharmacy_id = pharmacy_id
        self.position = position
        self.strategy = strategy
        
        self.stock = {"unusual": initial_stock}
        self.target_stock = initial_stock
        self.daily_sales = 0  

        self.money = INITIAL_CAPITAL
    
        self.b2b_memory = {}

    def try_sell(self):
        """Attempts to sell one unit to a client."""
        if self.stock["unusual"] > 0:
            self.stock["unusual"] -= 1
            self.money += SALE_PRICE
            self.daily_sales += 1
            return True
        else:
            return False

    def register_referral(self, from_pharmacy_id):
        """Registers that another pharmacy sent us a client (Reputation system)."""
        current_favors = self.b2b_memory.get(from_pharmacy_id, 0)
        self.b2b_memory[from_pharmacy_id] = current_favors + 1

    def choose_referral(self, neighbors_list):
        """
        Decides whether to refer a client to another pharmacy based on strategy.
        neighbors_list must be ordered by distance.
        """
        if self.strategy == "selfish":
            return None
        
        elif self.strategy == "cooperative":
            for neighbor in neighbors_list:
                if neighbor.stock["unusual"] > 0:
                    return neighbor
            return None 
            
        elif self.strategy == "tit_for_tat":
            for neighbor in neighbors_list:
                if (neighbor.pharmacy_id in self.b2b_memory) and (neighbor.stock["unusual"] > 0):
                    return neighbor
            return None

    def restock_logic(self):
        """
        Dynamic control system for inventory.
        Predicts demand for tomorrow based on sales today + 20% safety margin.
        """
        if self.daily_sales > 0:
            prediction = int(self.daily_sales * 1.2)
        else:
            prediction = 2 
            
        self.target_stock = prediction
        
        current_stock = self.stock["unusual"]
        needed = self.target_stock - current_stock
        
        if needed > 0:
            cost = needed * COST_PRICE
            self.money -= cost
            self.stock["unusual"] += needed
            
        self.daily_sales = 0


class Client:
    def __init__(self, customer_id, position):
        self.customer_id = customer_id
        self.position = position
        self.memory = {}

    def choose_pharmacy(self, pharmacies_list):
        """
        Minimizes Cost Function: Cost = Distance + (1 - Trust) * Penalty_Factor
        """
        best_pharmacy = None
        min_score = float('inf')

        for pharmacy in pharmacies_list:
            dist = math.sqrt((self.position[0] - pharmacy.position[0]) ** 2 + 
                             (self.position[1] - pharmacy.position[1]) ** 2)
            
            trust = self.memory.get(pharmacy.pharmacy_id, 0.5)
            
            penalty = (1 - trust) * 10
            final_score = dist + penalty
            
            if final_score < min_score:
                min_score = final_score
                best_pharmacy = pharmacy
                
        return best_pharmacy

    def update_memory(self, pharmacy_id, impact):
        """Reinforcement Learning: Adjusts trust score."""
        current_trust = self.memory.get(pharmacy_id, 0.5)
        new_trust = current_trust + impact
        
        new_trust = max(0.0, min(1.0, new_trust))
        
        self.memory[pharmacy_id] = new_trust

print("--- Generating City Simulation Environment ---")

pharmacies_list = []
clients_list = []

for i in range(NUM_PHARMACIES):
    x = random.gauss(CITY_SIZE/2, CITY_SIZE/4)
    y = random.gauss(CITY_SIZE/2, CITY_SIZE/4)
    x = max(0, min(CITY_SIZE, x))
    y = max(0, min(CITY_SIZE, y))
    
    strat = random.choice(["selfish", "cooperative", "tit_for_tat"])
    
    initial_stock = 5
    new_pharmacy = Pharmacy(i, (x, y), strat, initial_stock)
    pharmacies_list.append(new_pharmacy)

for i in range(NUM_CLIENTS):
    x = random.gauss(CITY_SIZE/2, CITY_SIZE/4)
    y = random.gauss(CITY_SIZE/2, CITY_SIZE/4)
    x = max(0, min(CITY_SIZE, x))
    y = max(0, min(CITY_SIZE, y))
    
    new_client = Client(i, (x, y))
    clients_list.append(new_client)

print("Pre-calculating distances between pharmacies...")
neighbors_map = {}

for p1 in pharmacies_list:
    others = []
    for p2 in pharmacies_list:
        if p1.pharmacy_id != p2.pharmacy_id:
            d = math.sqrt((p1.position[0]-p2.position[0])**2 + (p1.position[1]-p2.position[1])**2)
            others.append((d, p2))
    
    others.sort(key=lambda x: x[0])
    
    neighbors_map[p1.pharmacy_id] = [x[1] for x in others]

print(f"Starting Simulation: {NUM_DAYS} Days...")

for day in range(NUM_DAYS):
    if day > 0:
        for p in pharmacies_list:
            p.restock_logic()

    for client in clients_list:
        
        target_pharmacy = client.choose_pharmacy(pharmacies_list)
        
        success = target_pharmacy.try_sell()
        
        if success:
            client.update_memory(target_pharmacy.pharmacy_id, 0.1)
            
        else:
            my_neighbors = neighbors_map[target_pharmacy.pharmacy_id]
            recommended_pharmacy = target_pharmacy.choose_referral(my_neighbors)
            
            if recommended_pharmacy is not None:
                success_2 = recommended_pharmacy.try_sell()
                
                if success_2:
                    client.update_memory(target_pharmacy.pharmacy_id, 0.0)
                    client.update_memory(recommended_pharmacy.pharmacy_id, 0.1)
                    
                    if random.random() < 0.5:
                        recommended_pharmacy.register_referral(target_pharmacy.pharmacy_id)
                else:
                    client.update_memory(target_pharmacy.pharmacy_id, -0.1)
            else:

                client.update_memory(target_pharmacy.pharmacy_id, -0.2)

    if day % 50 == 0:
        print(f"-> Day {day} completed.")


print("\n--- FINAL RESULTS (Average Profit) ---")
results = {"selfish": [], "cooperative": [], "tit_for_tat": []}


for p in pharmacies_list:
    profit = p.money - INITIAL_CAPITAL 
    results[p.strategy].append(profit)

for strat, profits in results.items():
    if len(profits) > 0:
        avg = sum(profits) / len(profits)
        count = len(profits)
        print(f"Strategy {strat.upper().ljust(12)} | Count: {count} | Avg Profit: {avg:.2f} €")



