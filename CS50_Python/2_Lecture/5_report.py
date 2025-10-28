def main():
    spacecraft = [{"name": "Voyager 1", "distance": 163, "orbit": "Sun"},
                  {"name": "James Webb Space Telescope"#, "distance": .01
                   }]
    spacecraft1 = {"name": "Voyager 1", "distance": 163}
    spacecraft[0]["time period"] = 12
    
    spacecraft1.update({"distance": 160, "orbit": "Solar System"})
    print(create_report(spacecraft[0]))
    print(create_report(spacecraft[1]))
    print(create_report(spacecraft1))
    
    
    # cover each concept covered in the code
    
# multi line string concept
    """ its a comment if its assigned to a variable then its a string 
    """
    
def create_report(spacecraft):
    return f"""
    ========= REPORT =========
    
    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    
    ==========================
    """
    
if __name__ == "__main__":
    main()
    
    #1st method  
    
    # Name: {spacecraft[1]["name"]}
    # Distance: {spacecraft[1]["distance"]} AU