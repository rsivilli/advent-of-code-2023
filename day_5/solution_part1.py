from pathlib import Path
import re
from pprint import pprint

HEADER_SEARCH = r'(?P<source>\w+)-to-(?P<destination>\w+) map'

class GenericTransform:
    source:str
    destination:str
    source_gte:int
    source_lte:int
    destination_gte:int
    destination_lte:int
    
    def __init__(self, source:str,destination:str,source_gte:int, destination_gte:int, count:int) -> None:
        self.source = source
        self.destination = destination
        self.source_gte = source_gte
        self.source_lte = source_gte+count-1
        self.destination_gte = destination_gte
        self.destination_lte = destination_gte+count-1
    def get_lookup(self,destination_val):
        if destination_val<self.destination_gte or destination_val > self.destination_lte:
            raise ValueError(f"This is not a valid mapping for source {destination_val}. Must be between {self.destination_gte}-{self.destination_gte}")
        return destination_val-self.destination_gte+self.source_gte
    def get_output(self,source_val):
        if source_val<self.source_gte or source_val>self.source_lte:
            raise ValueError(f"This is not a valid mapping for source {source_val}. Must be between {self.source_gte}-{self.source_lte}")
        return source_val-self.source_gte+self.destination_gte
    def __str__(self) -> str:
        return f"{self.source}->{self.destination} for sources in the range of [{self.source_gte},{self.source_lte}] and destinations in the range of [{self.destination_gte},{self.destination_lte}]"

class Link:
    source:str
    destination:str
    destination_transforms:list[GenericTransform]
    def __init__(self, source:str,destination:str) -> None:
        self.destination = destination
        self.source = source
        self.destination_transforms = []

        
    def transform(self,source_val:int) -> int:
        for trans in self.destination_transforms:
            if source_val >= trans.source_gte and source_val <= trans.source_lte:
                out = trans.get_output(source_val)
                # print(f"For {self.source} val of {source_val} using transform with {trans.source_gte} and {trans.source_lte} received {self.destination} value of {out}")
                return out
        # print(f"For {self.source} val of {source_val} using transform with {trans.source_gte} and {trans.source_lte} received {self.destination} value of {source_val}")
        return source_val
    def lookup(self,destination_val:int)->int:
        for trans in self.destination_transforms:
            if destination_val >= trans.destination_gte and destination_val <= trans.destination_lte:
                out = trans.get_lookup(destination_val)
                return out
        return destination_val 

def parse_seed_ids(str_in:str)->list[int]:
    return [int(m) for m in re.findall("\d+",str_in)]

def parse_entry(entry:list[str]):
    """Assumes first line defines the map and following lines define transforms"""
    m = re.search(HEADER_SEARCH,entry[0]).groupdict()
    source = m.get("source")
    destination = m.get("destination")
    link = Link(source = source, destination = destination)
    print(f"{source}->{destination}")

    for line in entry[1:]:
        tmp = [int(s) for s in line.split(" ")]
        link.destination_transforms.append(
            GenericTransform(source,destination,source_gte=tmp[1],destination_gte=tmp[0],count=tmp[2])
        )
    return link
def run_transform(seed_id:int, links:list[Link])->int:
    val = seed_id
    for link in links:
        val = link.transform(val)
    return val 
def run_lookup(location:int, links:list[Link])->int:
    val = location
    for link in links[::-1]:
        val = link.lookup(val)
    return val

def parse_input(file_str="./day_5/small_input.txt"):
    file = Path(file_str)
    if not file.exists():
        raise FileNotFoundError(f"Could not find puzzle input file at {file.as_posix()}")
    
    with open(file) as f:
        seed_ids = parse_seed_ids(f.readline())
        processing_chain:list[Link] = []
        buffer = []
        f.readline()
        for line in f:
            if line != "\n":
                buffer.append(line)
            else:
                processing_chain.append(parse_entry(buffer))
                buffer.clear()
        processing_chain.append(parse_entry(buffer))

    return seed_ids, processing_chain
        

if __name__ == "__main__":
    seed_ids, processing_chain = parse_input("./day_5/puzzle_input.txt")
    locations = []
    for seed_id in seed_ids:
        print(f"------Seed Lookup {seed_id}-------")
        locations.append(run_transform(seed_id,processing_chain))
    print(min(locations))
        