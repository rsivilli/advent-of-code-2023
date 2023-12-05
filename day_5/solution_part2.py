from solution_part1 import parse_input,run_lookup
from tqdm import tqdm
from dataclasses import dataclass

@dataclass
class SeedRange:
    lte:int
    gte:int
    def __str__(self) -> str:
        return f"Seed Range [{self.gte},{self.lte}]"

def is_valid_seed_id(seed_id:int,seed_ranges:list[SeedRange]):
    for r in seed_ranges:
        if seed_id <= r.lte and seed_id >= r.gte:
            return True
    return False
def get_seed_ranges(seed_ids):
    seed_ranges = []
    for i in range(int(len(seed_ids)/2)):
        start = seed_ids[i*2]
        rng = seed_ids[i*2+1]
        seed_ranges.append(SeedRange(
            gte=start,
            lte=rng+start
        ))

    return seed_ranges
        
if __name__ == "__main__":
    seed_ids, processing_chain = parse_input("./day_5/puzzle_input.txt")
    seed_ranges = get_seed_ranges(seed_ids)
    updated_seed_ids = []
    min_val = None
    for location in tqdm(range(1000000000)):
        seed_id = run_lookup(location,processing_chain)
        if is_valid_seed_id(seed_id,seed_ranges):
            break
    print(seed_id)
    print(location)
    
        