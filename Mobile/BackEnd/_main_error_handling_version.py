from Database_Manipulation_error_handling_version import *
import sqlite3
from datetime import datetime
import random
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "GrabNGo_Database.db")
con= sqlite3.connect(db_path)
cus = con.cursor()

def populate_database_cameroon(cursor):
    # --- Lists for generating Cameroonian context ---
    cities = ["Douala", "Yaoundé", "Bamenda", "Bafoussam", "Garoua", "Buea"]
    neighborhoods = ["Akwa", "Bastos", "Bonapriso", "Moka", "Biyem-Assi", "Santa Barbara"]
    names = ["Jean-Pierre Atangana", "Marie Ngo", "Samuel Eto'o", "Claire Fosso", "Ibrahim Bello", 
             "Florence Biya", "Lucas Kamga", "Sali Moussa", "Esther Wouri", "Paul Ngu"]
    biz_names = ["Krystal Bakery", "Sawa Tech", "Obala Farms", "Wouri Electronics", "Bikutsi Fashion"]
    
    # 1. BUYER_ACCOUNTS (20 entries)
    buyers_data = []
    for i in range(1, 21):
        buyers_data.append((
            None, f"Buyer {names[i % 10]} {i}", f"buyer{i}@camnet.cm", 
            random.choice(neighborhoods), 670000000 + i, "password123", 
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Active"
        ))
    cursor.executemany("INSERT INTO BUYER_ACCOUNTS VALUES (?,?,?,?,?,?,?,?)", buyers_data)

    # 2. SELLER_ACCOUNTS (20 entries)
    sellers_data = []
    for i in range(1, 21):
        sellers_data.append((
            None,names[i % 10], f"{random.choice(biz_names)} {i}", "Retail", 
            690000000 + i, f"seller{i}@orange.cm", "sellpass", random.choice(cities),
            "08:00", 4.5, 10 + i, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "profile.png", "Active"
        ))
    cursor.executemany("INSERT INTO SELLER_ACCOUNTS VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", sellers_data)

    # 3. PRODUCT (20 entries)
    products_data = [
        (None, "Penja Pepper 1kg", 50), (None, "Safou (Plums) Box", 20),
        (None, "Manioc Flour Bag", 100), (None, "Plantain Bunch", 30),
        (None, "Ndole Leaves (Dried)", 40), (None, "Palm Oil 5L", 15),
        (None, "Bobolo (10pcs)", 60), (None, "Kilishi Pack", 25),
        (None, "Top Pamplemousse", 200), (None, "Kadji Beer Case", 10),
        (None, "Smartphone Charger", 15), (None, "Wax Fabric 6yds", 8),
        (None, "Cocoa Powder", 45), (None, "Dry Fish (Stock)", 12),
        (None, "Egusi 1kg", 35), (None, "Garri Yellow Bag", 50),
        (None, "Honey (Adamaoua)", 20), (None, "Kumba Bread Box", 15),
        (None, "Tomato Paste Box", 30), (None, "Sardines (Carton)", 5)
    ]
    cursor.executemany("INSERT INTO PRODUCT VALUES (?,?,?)", products_data)

    # 4. SELLER_PRODUCT (20 entries)
    seller_products = []
    for i in range(1, 21):
        seller_products.append((
            i, i, "Premium local quality", "Grocery", 1500 + (i * 100), 5, "img.jpg"
        ))
    cursor.executemany("INSERT INTO SELLER_PRODUCT VALUES (?,?,?,?,?,?,?)", seller_products)

    # 7. ORDERS (20 entries)
    orders = []
    for i in range(1, 21):
        orders.append((
            None, i, i, i, 2000, 1, 2000, "Pending", i, "Akwa", "Bonapriso"
        ))
    cursor.executemany("INSERT INTO ORDERS VALUES (?,?,?,?,?,?,?,?,?,?,?)", orders)

    # 8. HISTORY (20 entries)
    history = []
    for i in range(1, 21):
        history.append((
            None, i, i, i, 1, 2000, datetime.now().strftime("%Y-%m-%d"), i, "Yaoundé", "Douala"
        ))
    cursor.executemany("INSERT INTO HISTORY VALUES (?,?,?,?,?,?,?,?,?,?)", history)


    print("Successfully populated all tables with 20 Cameroonian entries each!")
populate_database_cameroon(cus)
def populate_perfect_yaounde_mesh(cus):
    # Neighborhoods categorized by their official Arrondissement

    yaounde_structure = {
        "Y1": ["Bastos", "Etoudi", "Nlongkak", "Olembe", "Messassi"],
        "Y2": ["Mokolo", "Tsinga", "Madagascar", "Cite Verte"],
        "Y3": ["Nsam", "Efoulan", "Ahala", "Obobogo", "Damas"],
        "Y4": ["Mvan", "Odza", "Ekounou", "Kondengui", "Mimboman"],
        "Y5": ["Essos", "Ngousso", "Omnisport", "Mvog-Ada"],
        "Y6": ["Biyem-Assi", "Mendong", "Etoug-Ebe", "Simbock", "Obili"],
        "Y7": ["Nkolbisson", "Oyom-Abang", "Etetak"]
    }

    # Inter-Arrondissement Bottleneck Matrix (Minutes)
    # The time taken to travel from the center of one district to another.
    inter_matrix = {
        ("Y1", "Y2"): 18, ("Y1", "Y3"): 35, ("Y1", "Y4"): 40, ("Y1", "Y5"): 20, ("Y1", "Y6"): 40, ("Y1", "Y7"): 35,
        ("Y2", "Y3"): 25, ("Y2", "Y4"): 35, ("Y2", "Y5"): 28, ("Y2", "Y6"): 18, ("Y2", "Y7"): 12,
        ("Y3", "Y4"): 15, ("Y3", "Y5"): 35, ("Y3", "Y6"): 12, ("Y3", "Y7"): 30,
        ("Y4", "Y5"): 25, ("Y4", "Y6"): 35, ("Y4", "Y7"): 50,
        ("Y5", "Y6"): 40, ("Y5", "Y7"): 45,
        ("Y6", "Y7"): 15
    }

    # Specific high-precision Intra-District links (Within same zone)
    # Helps differentiate long-distance vs short-distance within 1 Arrondissement
    intra_special = {
        ("Bastos", "Olembe"): 25, ("Bastos", "Nlongkak"): 8, 
        ("Mvan", "Odza"): 15, ("Mvan", "Kondengui"): 20,
        ("Biyem-Assi", "Mendong"): 12, ("Biyem-Assi", "Obili"): 10
    }

    all_hoods = []
    hood_to_dist = {}
    for d_id, hoods in yaounde_structure.items():
        for h in hoods:
            all_hoods.append(h)
            hood_to_dist[h] = d_id

    final_data = []

    # Mesh Topology Loop: O(n^2) ensures every point is linked to every point
    for i in range(len(all_hoods)):
        for j in range(i + 1, len(all_hoods)):
            h1, h2 = all_hoods[i], all_hoods[j]
            d1, d2 = hood_to_dist[h1], hood_to_dist[h2]

            # 1. Determine Time
            pair_key = tuple(sorted((h1, h2)))
            dist_pair = tuple(sorted((d1, d2)))

            if pair_key in intra_special:
                time = intra_special[pair_key]
            elif d1 == d2:
                time = 12  # Standard intra-neighborhood time
            else:
                time = inter_matrix.get(dist_pair, 35)

            # 2. Determine Traffic Level
            if time >= 30:
                traffic = "High"
            elif time >= 15:
                traffic = "Medium"
            else:
                traffic = "Low"

            final_data.append(("Yaoundé", h1, h2, time, traffic))

    # Using INSERT OR IGNORE to respect the UNIQUE constraint in your table
    cus.executemany("""
        INSERT OR IGNORE INTO NEIGHBORHOOD_DELIVERY 
        (City, Neighborhood_A, Neighborhood_B, Avg_Time_Minutes, Traffic_Level) 
        VALUES (?, ?, ?, ?, ?)""", final_data)
    
    con.commit()
    print(f"Mesh generation complete: {len(final_data)} linked routes added for Yaoundé.")
populate_perfect_yaounde_mesh(cus)


def populate_perfect_douala_mesh(cus):
    # Official Arrondissements & Neighborhoods for Douala
    # Source: Communauté Urbaine de Douala (CUD) 2025 Zoning


    douala_structure = {
        "D1": ["Akwa", "Bonanjo", "Bali", "Deido"],
        "D2": ["New Bell", "Nkololoun", "Kassalafam", "Babylone"],
        "D3": ["Ndokoti", "Bassa", "Ndogpassi", "Nyalla", "Village", "Logbaba"],
        "D4": ["Bonabéri", "Sodiko", "Mambanda", "Bekoko"],
        "D5": ["Bonamoussadi", "Makepe", "Kotto", "Logpom", "Bepanda", "Cité SIC"]
    }

    # Inter-Arrondissement Bottleneck Matrix (Minutes)
    # Calibrated for motorbike transit across Douala's heavy traffic zones.
    inter_matrix = {
        ("D1", "D2"): 12, ("D1", "D3"): 25, ("D1", "D4"): 45, ("D1", "D5"): 20,
        ("D2", "D3"): 18, ("D2", "D4"): 50, ("D2", "D5"): 30,
        ("D3", "D4"): 60, ("D3", "D5"): 25,
        ("D4", "D5"): 55
    }

    # Specific high-precision Intra-District links
    # Differentiates long-distance routes within the same Arrondissement.
    intra_special = {
        ("Akwa", "Deido"): 15, ("Bonanjo", "Deido"): 18,
        ("Ndokoti", "Nyalla"): 20, ("Ndokoti", "Village"): 25,
        ("Bonabéri", "Bekoko"): 22, ("Bonamoussadi", "Logpom"): 15,
        ("Bonamoussadi", "Bepanda"): 18
    }

    all_hoods = []
    hood_to_dist = {}
    for d_id, hoods in douala_structure.items():
        for h in hoods:
            all_hoods.append(h)
            hood_to_dist[h] = d_id

    final_data = []

    # Mesh Topology Loop: Links every neighborhood in Douala to every other neighborhood
    for i in range(len(all_hoods)):
        for j in range(i + 1, len(all_hoods)):
            h1, h2 = all_hoods[i], all_hoods[j]
            d1, d2 = hood_to_dist[h1], hood_to_dist[h2]

            pair_key = tuple(sorted((h1, h2)))
            dist_pair = tuple(sorted((d1, d2)))

            # 1. Determine Time
            if pair_key in intra_special:
                time = intra_special[pair_key]
            elif d1 == d2:
                time = 12  # Standard intra-neighborhood time
            else:
                # Get baseline from matrix, reflecting bridge or cross-town bottlenecks
                time = inter_matrix.get(dist_pair, 35)

            # 2. Determine Traffic Level
            if time >= 40:
                traffic = "Critical" # Specifically for the Wouri Bridge/Ndokoti
            elif time >= 25:
                traffic = "High"
            elif time >= 15:
                traffic = "Medium"
            else:
                traffic = "Low"

            final_data.append(("Douala", h1, h2, time, traffic))

    # Batch Insert
    cus.executemany("""
        INSERT OR IGNORE INTO NEIGHBORHOOD_DELIVERY 
        (City, Neighborhood_A, Neighborhood_B, Avg_Time_Minutes, Traffic_Level) 
        VALUES (?, ?, ?, ?, ?)""", final_data)
    
    con.commit()
    print(f"Douala Mesh generated: {len(final_data)} linked routes added.")

populate_perfect_douala_mesh(cus)



def populate_perfect_regional_mesh(cus):
    # Mapping of neighborhoods for other major regions


    regional_structure = {
        "Bafoussam": {
            "B1": ["Marché A", "Djeleng", "Banengo", "Tamodja"],
            "B2": ["Marché B", "Socada", "Tyo", "Koptchou", "Koung-Souk"]
        },
        "Bamenda": {
            "BA1": ["Commercial Avenue", "Mankon", "Old Council", "Hospital Roundabout"],
            "BA2": ["Up Station", "Nkwen", "Mile 2", "Mile 4"]
        },
        "Buea": {
            "BU1": ["Molyko", "Mile 17", "Check Point", "Muea"],
            "BU2": ["Great Soppo", "Clerks Quarters", "Bokwango", "Federal Quarters"]
        },
        "Limbe": {
            "L1": ["Down Beach", "New Town", "Mile 4", "Bota", "Ngeme"]
        },
        "Garoua": {
            "G1": ["Lidjiré", "Roumdé Adjia", "Poupounré", "Plateau", "Yelwa"]
        }
    }

    # Inter-District Bottleneck Matrix (Minutes)
    # Bamenda BA1 to BA2 includes the "Up Station" hill climb penalty.
    regional_matrix = {
        ("B1", "B2"): 12,
        ("BA1", "BA2"): 25, # Hill climb bottleneck
        ("BU1", "BU2"): 20, # Up-slope transit
        ("L1", "L1"): 10,  # Smaller urban spread
        ("G1", "G1"): 12   # Flat terrain, faster transit
    }

    final_data = []

    for city, districts in regional_structure.items():
        all_hoods = []
        hood_to_dist = {}
        for d_id, hoods in districts.items():
            for h in hoods:
                all_hoods.append(h)
                hood_to_dist[h] = d_id

        # Full Mesh Logic
        for i in range(len(all_hoods)):
            for j in range(i + 1, len(all_hoods)):
                h1, h2 = all_hoods[i], all_hoods[j]
                d1, d2 = hood_to_dist[h1], hood_to_dist[h2]

                # 1. Determine Time
                if d1 == d2:
                    time = 10 # Faster transit in smaller cities
                    traffic = "Low"
                else:
                    pair = tuple(sorted((d1, d2)))
                    time = regional_matrix.get(pair, 20)
                    traffic = "Medium"

                final_data.append((city, h1, h2, time, traffic))

    # Batch Insert
    cus.executemany("""
        INSERT OR IGNORE INTO NEIGHBORHOOD_DELIVERY 
        (City, Neighborhood_A, Neighborhood_B, Avg_Time_Minutes, Traffic_Level) 
        VALUES (?, ?, ?, ?, ?)""", final_data)
    
    con.commit()
    print(f"Regional Mesh generated: {len(final_data)} linked routes added.")

populate_perfect_regional_mesh(cus)

adder=ADD_INTO_TABLES(con)

def populate_delivery_data(db_manager):
    """
    Populates 20 Agents and 20 Seller-Agent links.
    Pass your ADD_INTO_TABLES instance (data2) here.
    """
    
    # 1. List of 20 Delivery Agents (Name, Location)
    agents_data = [
        ("James Wilson", "Downtown"), ("Sarah Chen", "North Hills"), 
        ("Marcus Brown", "West End"), ("Elena Rodriguez", "Southside"), 
        ("David Kim", "East Gate"), ("Lisa Taylor", "Midtown"),
        ("Kevin Vaughn", "Industrial Park"), ("Rachel Adams", "Highland"), 
        ("Victor Ortiz", "Riverside"), ("Omar Sy", "Green Valley"), 
        ("Chloe Smith", "Docks"), ("Ahmed Khan", "Financial District"),
        ("Sophie Martin", "University Heights"), ("Leo Garcia", "Central Park"), 
        ("Mia Wong", "Old Town"), ("Chris Evans", "Suburbia"), 
        ("Nina Patel", "Tech Hub"), ("Jason Reed", "Airport Road"),
        ("Tiffany Low", "Mall District"), ("Ben Foster", "Harbor View")
    ]

    # 2. List of 20 Seller-Agent Links (Agent_ID, Seller_ID)
    # This assigns 2 agents to each of your first 10 sellers
    seller_links = [
        (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4), 
        (9, 5), (10, 5), (11, 6), (12, 6), (13, 7), (14, 7), (15, 8), 
        (16, 8), (17, 9), (18, 9), (19, 10), (20, 10)
    ]

    print("--- Starting Delivery Population ---")
    
    # Insert Agents
    for name, loc in agents_data:
        db_manager.add_into_delivery_agent(name, loc)
    print(f"Successfully added {len(agents_data)} Delivery Agents.")

    # Insert Seller-Agent Connections
    for agent_id, seller_id in seller_links:
        db_manager.add_into_seller_delivery_agent(agent_id, seller_id)
    print(f"Successfully created {len(seller_links)} Seller-Agent links.")

    print("--- Population Complete ---")

# To run it:
populate_delivery_data(adder)