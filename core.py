import os
import json
from datetime import datetime

class GenesisCore:
    def __init__(self):
        self.state_file = "system_evolution_state.json"
        self.load_state()

    def load_state(self):
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    self.state = json.load(f)
            except Exception:
                self.state = {"iterations": 0, "evolution_history": []}
        else:
            self.state = {"iterations": 0, "evolution_history": []}

    def execute_cycle(self):
        self.state["iterations"] += 1
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_record = f"Evolution cycle #{self.state['iterations']} executed at {now}"
        self.state["evolution_history"].append(new_record)
        
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=4, ensure_ascii=False)
            
        print(f"[+] {new_record}")

if __name__ == "__main__":
    core = GenesisCore()
    core.execute_cycle()
