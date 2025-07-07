from typing import List, Dict

def get_cricket_players() -> List[Dict]:
    """Return a list of 100 cricket players with realistic stats"""
    players = [
        # Legendary Batsmen
        {"id": 1, "name": "Sachin Tendulkar", "batting": 96, "bowling": 45, "fielding": 85},
        {"id": 2, "name": "Virat Kohli", "batting": 94, "bowling": 30, "fielding": 88},
        {"id": 3, "name": "Brian Lara", "batting": 93, "bowling": 25, "fielding": 80},
        {"id": 4, "name": "Ricky Ponting", "batting": 91, "bowling": 35, "fielding": 92},
        {"id": 5, "name": "Steve Smith", "batting": 90, "bowling": 55, "fielding": 85},
        
        # Great All-rounders
        {"id": 6, "name": "Jacques Kallis", "batting": 88, "bowling": 82, "fielding": 90},
        {"id": 7, "name": "Ben Stokes", "batting": 82, "bowling": 85, "fielding": 88},
        {"id": 8, "name": "Kapil Dev", "batting": 75, "bowling": 88, "fielding": 82},
        {"id": 9, "name": "Shane Watson", "batting": 80, "bowling": 78, "fielding": 85},
        {"id": 10, "name": "Chris Cairns", "batting": 78, "bowling": 80, "fielding": 83},
        
        # Elite Bowlers
        {"id": 11, "name": "Shane Warne", "batting": 35, "bowling": 98, "fielding": 75},
        {"id": 12, "name": "Muttiah Muralitharan", "batting": 25, "bowling": 97, "fielding": 70},
        {"id": 13, "name": "Glenn McGrath", "batting": 20, "bowling": 95, "fielding": 78},
        {"id": 14, "name": "Wasim Akram", "batting": 45, "bowling": 94, "fielding": 80},
        {"id": 15, "name": "Dale Steyn", "batting": 30, "bowling": 93, "fielding": 82},
        
        # Modern Stars
        {"id": 16, "name": "Joe Root", "batting": 92, "bowling": 50, "fielding": 85},
        {"id": 17, "name": "Kane Williamson", "batting": 91, "bowling": 45, "fielding": 88},
        {"id": 18, "name": "Babar Azam", "batting": 89, "bowling": 35, "fielding": 82},
        {"id": 19, "name": "David Warner", "batting": 87, "bowling": 25, "fielding": 80},
        {"id": 20, "name": "Rohit Sharma", "batting": 90, "bowling": 40, "fielding": 85},
        
        # Wicket-keepers
        {"id": 21, "name": "MS Dhoni", "batting": 82, "bowling": 30, "fielding": 98},
        {"id": 22, "name": "Adam Gilchrist", "batting": 85, "bowling": 20, "fielding": 95},
        {"id": 23, "name": "Jos Buttler", "batting": 83, "bowling": 25, "fielding": 92},
        {"id": 24, "name": "Rishabh Pant", "batting": 80, "bowling": 15, "fielding": 90},
        {"id": 25, "name": "Quinton de Kock", "batting": 78, "bowling": 20, "fielding": 88},
        
        # Fast Bowlers
        {"id": 26, "name": "Jasprit Bumrah", "batting": 25, "bowling": 96, "fielding": 80},
        {"id": 27, "name": "Pat Cummins", "batting": 35, "bowling": 91, "fielding": 85},
        {"id": 28, "name": "Kagiso Rabada", "batting": 30, "bowling": 90, "fielding": 82},
        {"id": 29, "name": "Mitchell Starc", "batting": 32, "bowling": 89, "fielding": 78},
        {"id": 30, "name": "Trent Boult", "batting": 28, "bowling": 88, "fielding": 83},
        
        # Spinners
        {"id": 31, "name": "Ravichandran Ashwin", "batting": 55, "bowling": 87, "fielding": 75},
        {"id": 32, "name": "Nathan Lyon", "batting": 45, "bowling": 85, "fielding": 78},
        {"id": 33, "name": "Ravindra Jadeja", "batting": 68, "bowling": 84, "fielding": 95},
        {"id": 34, "name": "Shakib Al Hasan", "batting": 75, "bowling": 83, "fielding": 80},
        {"id": 35, "name": "Rashid Khan", "batting": 40, "bowling": 86, "fielding": 85},
        
        # Solid Batsmen
        {"id": 36, "name": "Cheteshwar Pujara", "batting": 86, "bowling": 25, "fielding": 75},
        {"id": 37, "name": "Ajinkya Rahane", "batting": 82, "bowling": 30, "fielding": 85},
        {"id": 38, "name": "Angelo Mathews", "batting": 80, "bowling": 65, "fielding": 78},
        {"id": 39, "name": "Dean Elgar", "batting": 78, "bowling": 35, "fielding": 72},
        {"id": 40, "name": "Dimuth Karunaratne", "batting": 76, "bowling": 30, "fielding": 75},
        
        # Aggressive Batsmen
        {"id": 41, "name": "AB de Villiers", "batting": 94, "bowling": 40, "fielding": 92},
        {"id": 42, "name": "Chris Gayle", "batting": 88, "bowling": 55, "fielding": 70},
        {"id": 43, "name": "Brendon McCullum", "batting": 84, "bowling": 35, "fielding": 88},
        {"id": 44, "name": "Shahid Afridi", "batting": 72, "bowling": 78, "fielding": 80},
        {"id": 45, "name": "Andre Russell", "batting": 75, "bowling": 80, "fielding": 85},
        
        # Emerging Players
        {"id": 46, "name": "Shubman Gill", "batting": 82, "bowling": 25, "fielding": 80},
        {"id": 47, "name": "Prithvi Shaw", "batting": 80, "bowling": 20, "fielding": 75},
        {"id": 48, "name": "Devon Conway", "batting": 78, "bowling": 30, "fielding": 82},
        {"id": 49, "name": "Will Young", "batting": 76, "bowling": 35, "fielding": 78},
        {"id": 50, "name": "Harry Brook", "batting": 84, "bowling": 25, "fielding": 85},
        
        # Veteran All-rounders
        {"id": 51, "name": "Jason Holder", "batting": 70, "bowling": 82, "fielding": 85},
        {"id": 52, "name": "Kyle Jamieson", "batting": 50, "bowling": 85, "fielding": 82},
        {"id": 53, "name": "Cameron Green", "batting": 72, "bowling": 78, "fielding": 88},
        {"id": 54, "name": "Daryl Mitchell", "batting": 74, "bowling": 65, "fielding": 85},
        {"id": 55, "name": "Marco Jansen", "batting": 45, "bowling": 80, "fielding": 80},
        
        # Quality Bowlers
        {"id": 56, "name": "Josh Hazlewood", "batting": 25, "bowling": 88, "fielding": 78},
        {"id": 57, "name": "Jimmy Anderson", "batting": 30, "bowling": 86, "fielding": 75},
        {"id": 58, "name": "Stuart Broad", "batting": 35, "bowling": 84, "fielding": 80},
        {"id": 59, "name": "Tim Southee", "batting": 40, "bowling": 82, "fielding": 78},
        {"id": 60, "name": "Neil Wagner", "batting": 25, "bowling": 81, "fielding": 75},
        
        # Middle-order Specialists
        {"id": 61, "name": "Faf du Plessis", "batting": 85, "bowling": 30, "fielding": 88},
        {"id": 62, "name": "Ross Taylor", "batting": 83, "bowling": 35, "fielding": 85},
        {"id": 63, "name": "Temba Bavuma", "batting": 78, "bowling": 25, "fielding": 90},
        {"id": 64, "name": "Rassie van der Dussen", "batting": 80, "bowling": 40, "fielding": 82},
        {"id": 65, "name": "Marnus Labuschagne", "batting": 88, "bowling": 50, "fielding": 85},
        
        # Utility Players
        {"id": 66, "name": "Mitchell Marsh", "batting": 74, "bowling": 75, "fielding": 82},
        {"id": 67, "name": "Moeen Ali", "batting": 68, "bowling": 76, "fielding": 80},
        {"id": 68, "name": "Sam Curran", "batting": 65, "bowling": 78, "fielding": 85},
        {"id": 69, "name": "Chris Woakes", "batting": 62, "bowling": 80, "fielding": 88},
        {"id": 70, "name": "Ashton Agar", "batting": 55, "bowling": 74, "fielding": 85},
        
        # Specialist Fielders
        {"id": 71, "name": "Jonty Rhodes", "batting": 70, "bowling": 25, "fielding": 99},
        {"id": 72, "name": "Paul Collingwood", "batting": 75, "bowling": 45, "fielding": 95},
        {"id": 73, "name": "Herschelle Gibbs", "batting": 78, "bowling": 30, "fielding": 92},
        {"id": 74, "name": "Mohammad Kaif", "batting": 68, "bowling": 25, "fielding": 94},
        {"id": 75, "name": "Suresh Raina", "batting": 72, "bowling": 50, "fielding": 90},
        
        # Young Talents
        {"id": 76, "name": "Yashasvi Jaiswal", "batting": 78, "bowling": 20, "fielding": 80},
        {"id": 77, "name": "Ruturaj Gaikwad", "batting": 76, "bowling": 25, "fielding": 78},
        {"id": 78, "name": "Ishan Kishan", "batting": 74, "bowling": 15, "fielding": 85},
        {"id": 79, "name": "Shreyas Iyer", "batting": 80, "bowling": 30, "fielding": 82},
        {"id": 80, "name": "KL Rahul", "batting": 84, "bowling": 20, "fielding": 88},
        
        # Solid Players
        {"id": 81, "name": "Mushfiqur Rahim", "batting": 76, "bowling": 20, "fielding": 85},
        {"id": 82, "name": "Dinesh Chandimal", "batting": 74, "bowling": 25, "fielding": 82},
        {"id": 83, "name": "Asad Shafiq", "batting": 72, "bowling": 30, "fielding": 78},
        {"id": 84, "name": "Azhar Ali", "batting": 70, "bowling": 35, "fielding": 75},
        {"id": 85, "name": "Mominul Haque", "batting": 75, "bowling": 25, "fielding": 72},
        
        # Balanced Players
        {"id": 86, "name": "Colin de Grandhomme", "batting": 65, "bowling": 70, "fielding": 80},
        {"id": 87, "name": "Jimmy Neesham", "batting": 68, "bowling": 72, "fielding": 85},
        {"id": 88, "name": "Daniel Vettori", "batting": 60, "bowling": 85, "fielding": 82},
        {"id": 89, "name": "Scott Styris", "batting": 72, "bowling": 68, "fielding": 80},
        {"id": 90, "name": "Jacob Oram", "batting": 65, "bowling": 75, "fielding": 85},
        
        # Current Indian Stars (Enhanced)
        {"id": 91, "name": "Shubman Gill", "batting": 87, "bowling": 25, "fielding": 88},
        {"id": 92, "name": "Hardik Pandya", "batting": 79, "bowling": 83, "fielding": 90},
        {"id": 93, "name": "Suryakumar Yadav", "batting": 85, "bowling": 30, "fielding": 92},
        {"id": 94, "name": "Mohammed Siraj", "batting": 28, "bowling": 86, "fielding": 82},
        {"id": 95, "name": "Kuldeep Yadav", "batting": 35, "bowling": 84, "fielding": 75},
        
        # Pakistani Current Stars
        {"id": 96, "name": "Mohammad Rizwan", "batting": 84, "bowling": 20, "fielding": 93},
        {"id": 97, "name": "Fakhar Zaman", "batting": 82, "bowling": 25, "fielding": 78},
        {"id": 98, "name": "Shaheen Afridi", "batting": 32, "bowling": 89, "fielding": 85},
        {"id": 99, "name": "Haris Rauf", "batting": 26, "bowling": 86, "fielding": 78},
        {"id": 100, "name": "Shadab Khan", "batting": 68, "bowling": 83, "fielding": 88},
        
        # Australian Modern Stars
        {"id": 101, "name": "Travis Head", "batting": 86, "bowling": 45, "fielding": 83},
        {"id": 102, "name": "Glenn Maxwell", "batting": 82, "bowling": 79, "fielding": 90},
        {"id": 103, "name": "Josh Hazlewood", "batting": 22, "bowling": 88, "fielding": 80},
        {"id": 104, "name": "Marcus Stoinis", "batting": 77, "bowling": 76, "fielding": 87},
        {"id": 105, "name": "Alex Carey", "batting": 78, "bowling": 20, "fielding": 91},
        
        # English Current Squad
        {"id": 106, "name": "Harry Brook", "batting": 88, "bowling": 25, "fielding": 85},
        {"id": 107, "name": "Jonny Bairstow", "batting": 85, "bowling": 20, "fielding": 90},
        {"id": 108, "name": "Liam Livingstone", "batting": 80, "bowling": 74, "fielding": 87},
        {"id": 109, "name": "Mark Wood", "batting": 25, "bowling": 87, "fielding": 78},
        {"id": 110, "name": "Adil Rashid", "batting": 48, "bowling": 85, "fielding": 80},
        
        # South African Stars
        {"id": 111, "name": "Aiden Markram", "batting": 84, "bowling": 67, "fielding": 87},
        {"id": 112, "name": "David Miller", "batting": 81, "bowling": 25, "fielding": 90},
        {"id": 113, "name": "Heinrich Klaasen", "batting": 79, "bowling": 20, "fielding": 87},
        {"id": 114, "name": "Anrich Nortje", "batting": 24, "bowling": 87, "fielding": 82},
        {"id": 115, "name": "Tabraiz Shamsi", "batting": 30, "bowling": 83, "fielding": 75},
        
        # New Zealand Current
        {"id": 116, "name": "Devon Conway", "batting": 87, "bowling": 30, "fielding": 86},
        {"id": 117, "name": "Rachin Ravindra", "batting": 81, "bowling": 70, "fielding": 84},
        {"id": 118, "name": "Tim Southee", "batting": 35, "bowling": 85, "fielding": 82},
        {"id": 119, "name": "Mitchell Santner", "batting": 60, "bowling": 80, "fielding": 92},
        {"id": 120, "name": "Tom Latham", "batting": 83, "bowling": 25, "fielding": 90},
        
        # West Indies Current
        {"id": 121, "name": "Nicholas Pooran", "batting": 81, "bowling": 20, "fielding": 87},
        {"id": 122, "name": "Shai Hope", "batting": 84, "bowling": 25, "fielding": 84},
        {"id": 123, "name": "Jason Holder", "batting": 70, "bowling": 82, "fielding": 87},
        {"id": 124, "name": "Andre Russell", "batting": 74, "bowling": 77, "fielding": 84},
        {"id": 125, "name": "Shimron Hetmyer", "batting": 78, "bowling": 25, "fielding": 80},
        
        # Afghanistan Stars
        {"id": 126, "name": "Rashid Khan", "batting": 48, "bowling": 93, "fielding": 87},
        {"id": 127, "name": "Mohammad Nabi", "batting": 72, "bowling": 82, "fielding": 84},
        {"id": 128, "name": "Rahmanullah Gurbaz", "batting": 77, "bowling": 20, "fielding": 87},
        {"id": 129, "name": "Ibrahim Zadran", "batting": 75, "bowling": 25, "fielding": 82},
        {"id": 130, "name": "Mujeeb Ur Rahman", "batting": 32, "bowling": 85, "fielding": 80},
        
        # Bangladesh Current
        {"id": 131, "name": "Litton Das", "batting": 81, "bowling": 20, "fielding": 90},
        {"id": 132, "name": "Najmul Hossain", "batting": 78, "bowling": 25, "fielding": 84},
        {"id": 133, "name": "Mehidy Hasan", "batting": 60, "bowling": 80, "fielding": 87},
        {"id": 134, "name": "Mustafizur Rahman", "batting": 22, "bowling": 86, "fielding": 80},
        {"id": 135, "name": "Taskin Ahmed", "batting": 27, "bowling": 83, "fielding": 77},
        
        # Sri Lankan Current  
        {"id": 136, "name": "Pathum Nissanka", "batting": 82, "bowling": 25, "fielding": 84},
        {"id": 137, "name": "Kusal Mendis", "batting": 80, "bowling": 30, "fielding": 87},
        {"id": 138, "name": "Wanindu Hasaranga", "batting": 57, "bowling": 87, "fielding": 90},
        {"id": 139, "name": "Dushmantha Chameera", "batting": 27, "bowling": 84, "fielding": 77},
        {"id": 140, "name": "Charith Asalanka", "batting": 76, "bowling": 47, "fielding": 82},
        
        # Associates & Emerging
        {"id": 141, "name": "Paul Stirling", "batting": 80, "bowling": 35, "fielding": 82},
        {"id": 142, "name": "Curtis Campher", "batting": 74, "bowling": 72, "fielding": 84},
        {"id": 143, "name": "Gerhard Erasmus", "batting": 72, "bowling": 67, "fielding": 87},
        {"id": 144, "name": "Sikandar Raza", "batting": 76, "bowling": 77, "fielding": 87},
        {"id": 145, "name": "Ryan Burl", "batting": 70, "bowling": 74, "fielding": 82},
        
        # Recent Legends (Balanced)
        {"id": 146, "name": "AB de Villiers", "batting": 93, "bowling": 45, "fielding": 96},
        {"id": 147, "name": "Kumar Sangakkara", "batting": 88, "bowling": 15, "fielding": 89},
        {"id": 148, "name": "Hashim Amla", "batting": 87, "bowling": 20, "fielding": 83},
        {"id": 149, "name": "Mahela Jayawardene", "batting": 86, "bowling": 30, "fielding": 91},
        {"id": 150, "name": "Younis Khan", "batting": 84, "bowling": 40, "fielding": 79}
    ]
    
    return players
