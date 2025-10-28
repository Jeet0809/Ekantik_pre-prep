# utility features of dictionary

# try to cover every concept used in the code

distances = {
    "Voyager 1": 163, 
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}


def main():
    
    # whats the difference between these methods
    
    for _ in distances :
        print(f"{_} is {distances[_]} AU from Earth")
        
    print()
    
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")
    
    print()
        
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")
    
def convert(au):
    return f"{ au * 149597870700: ,}"
    
main()