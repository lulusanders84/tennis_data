def to_file(data: list[tuple], filepath: str, write_action: str):
    with open(filepath, write_action) as file:
        file.write("\n")
        for item in data:
            file.write(",".join(item) + "\n")

def append_to_file(data: list[tuple], filepath: str):
    to_file(data, filepath, "a")
    
def replace_file(data: list[tuple], filepath: str):
    to_file(data, filepath, "w")