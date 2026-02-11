import folium
import os

# --- 1. SETUP OUTPUT PATH (DESKTOP) ---
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, "interactive_mining_map.html")

# --- 2. EXTENDED MINING DATASET (North America, South America, Australia, Africa) ---
# Format: [Name, Lat, Lon, Metal, Operator]
mining_data = [
    # === KINROSS GOLD (COMPLETE PORTFOLIO) ===
    # North America
    ["Fort Knox", 65.00, -147.35, "Gold", "Kinross"],
    ["Manh Choh", 63.19, -142.89, "Gold", "Kinross"],             # Trucked to Fort Knox
    ["Round Mountain", 38.71, -117.07, "Gold", "Kinross"],
    ["Bald Mountain", 39.94, -115.54, "Gold", "Kinross"],
    ["Great Bear (Dixie)", 50.88, -93.64, "Gold", "Kinross"],      # Major Development
    ["Curlew Basin", 48.95, -119.65, "Gold", "Kinross"],           # Exploration Project
    # South America
    ["Paracatu", -17.22, -46.87, "Gold", "Kinross"],               # Largest Mine (Brazil)
    ["La Coipa", -26.81, -69.27, "Gold", "Kinross"],               # Restarted (Chile)
    ["Lobo-Marte", -27.17, -69.03, "Gold", "Kinross"],             # Development (Chile)
    ["Maricunga", -27.55, -69.30, "Gold", "Kinross"],              # Care & Maintenance
    # Africa
    ["Tasiast", 20.61, -15.46, "Gold", "Kinross"],                 # Mauritania (Major Asset)
    
    # === CANADA (QUEBEC) ===
    ["LaRonde Complex", 48.25, -78.44, "Gold", "Agnico Eagle"],
    ["Canadian Malartic Complex", 48.11, -78.13, "Gold", "Agnico Eagle"],
    ["Goldex Complex", 48.09, -77.87, "Gold", "Agnico Eagle"],
    ["Detour Lake Mine", 50.00, -79.70, "Gold", "Agnico Eagle"],
    ["Macassa Mine", 48.14, -80.07, "Gold", "Agnico Eagle"],
    ["Meliadine Mine", 63.03, -92.22, "Gold", "Agnico Eagle"],
    ["Meadowbank Complex", 65.02, -96.07, "Gold", "Agnico Eagle"],
    # === AUSTRALIA ===
    ["Fosterville Mine", -36.71, 144.50, "Gold", "Agnico Eagle"],
    # === FINLAND ===
    ["Kittilä Mine", 67.91, 25.40, "Gold", "Agnico Eagle"],
    # === MEXICO ===
    ["Pinos Altos Mine", 28.27, -108.30, "Gold", "Agnico Eagle"],

    # === NEWMONT (Based on your list) ===
    # Africa
    ["Ahafo North", 7.05, -2.33, "Gold", "Newmont", ],
    ["Ahafo South", 7.02, -2.35, "Gold", "Newmont", ],
    # Australia & Pacific
    ["Boddington", -32.74, 116.36, "Gold", "Newmont", ],
    ["Cadia", -33.45, 148.99, "Gold", "Newmont", ],
    ["Tanami", -19.96, 129.71, "Gold", "Newmont", ],
    ["Lihir", -3.12, 152.64, "Gold", "Newmont", ],
    # Americas
    ["Brucejack", 56.47, -130.19, "Gold", "Newmont", ],
    ["Red Chris", 57.71, -129.79, "Copper", "Newmont", ],
    ["Cerro Negro", -46.95, -70.18, "Gold", "Newmont", ],
    ["Merian", 5.12, -54.55, "Gold", "Newmont", ],
    ["Peñasquito", 23.98, -102.66, "Gold", "Newmont", ],
    ["Yanacocha", -6.98, -78.50, "Gold", "Newmont", ],
    ["Nevada Gold Mines (JV)", 40.97, -116.33, "Gold", "Newmont/Barrick JV", ], # Shared asset

    # === BARRICK GOLD (Based on your list) ===
    # Africa & Middle East
    ["Kibali", 3.12, 29.58, "Gold", "Barrick", ],
    ["Loulo-Gounkoto", 13.01, -11.48, "Gold", "Barrick", ],
    ["Bulyanhulu", -3.23, 32.48, "Gold", "Barrick", ],
    ["North Mara", -1.47, 34.52, "Gold", "Barrick", ],
    ["Lumwana", -12.24, 25.81, "Copper", "Barrick", ],
    ["Jabal Sayid", 23.85, 40.94, "Copper", "Barrick", ],
    # Americas
    ["Pueblo Viejo (JV)", 18.94, -70.17, "Gold", "Barrick", ],
    ["Veladero", -29.37, -69.95, "Gold", "Barrick", ],
    ["Zaldívar", -24.22, -69.07, "Copper", "Barrick", ],
    ["Fourmile", 40.25, -116.70, "Gold", "Barrick", ], # Near Cortez
    ["Norte Abierto", -27.55, -69.30, "Gold", "Barrick", ],
    # Asia Pacific
    ["Porgera", -5.46, 143.10, "Gold", "Barrick", ],
    ["Reko Diq", 28.97, 62.43, "Copper", "Barrick", ],

    # === ANGLOGOLD ASHANTI (Based on your list) ===
    # Africa
    ["Sukari", 24.95, 34.72, "Gold", "AngloGold Ashanti", ],
    ["Iduapriem", 5.30, -2.00, "Gold", "AngloGold Ashanti", ],
    ["Obuasi", 6.20, -1.67, "Gold", "AngloGold Ashanti", ],
    ["Siguiri", 11.57, -9.39, "Gold", "AngloGold Ashanti", ],
    ["Geita", -2.87, 32.19, "Gold", "AngloGold Ashanti", ],
    # Americas
    ["Cerro Vanguardia", -48.39, -68.26, "Gold", "AngloGold Ashanti", ],
    ["AGA Mineração (Cuiabá)", -19.86, -43.73, "Gold", "AngloGold Ashanti", ],
    ["Serra Grande", -14.24, -49.37, "Gold", "AngloGold Ashanti", ],
    # Australia
    ["Sunrise Dam", -29.08, 122.42, "Gold", "AngloGold Ashanti", ],
    ["Tropicana", -29.24, 124.54, "Gold", "AngloGold Ashanti", ],
    # === ALCOA (Bauxite & Alumina) ===
    # Australia (Western Australia)
    ["Huntly Bauxite Mine", -32.59, 116.08, "Bauxite", "Alcoa"],
    ["Willowdale Bauxite Mine", -32.92, 116.01, "Bauxite", "Alcoa"],
    # Brazil
    ["Juruti Bauxite Mine", -2.15, -56.09, "Bauxite", "Alcoa"],
    ["Poços de Caldas", -21.78, -46.56, "Bauxite", "Alcoa"],
    # Guinea
    ["CBG Sangaredi", 11.10, -14.24, "Bauxite", "Alcoa/Rio Tinto"], # Joint Venture
    # Saudi Arabia
    ["Al Ba'itha Mine", 27.67, 43.98, "Bauxite", "Alcoa/Ma'aden"],

    # === RIO TINTO (Iron Ore - Pilbara, Australia) ===
    ["Tom Price", -22.76, 117.76, "Iron Ore", "Rio Tinto"],
    ["Paraburdoo", -23.20, 117.66, "Iron Ore", "Rio Tinto"],
    ["Marandoo", -22.63, 118.11, "Iron Ore", "Rio Tinto"],
    ["Brockman 2", -22.39, 117.38, "Iron Ore", "Rio Tinto"],
    ["Brockman 4", -22.34, 117.29, "Iron Ore", "Rio Tinto"],
    ["Western Turner Syncline", -22.69, 117.60, "Iron Ore", "Rio Tinto"],
    ["Nammuldi", -22.40, 117.38, "Iron Ore", "Rio Tinto"],
    ["Silvergrass", -22.35, 117.30, "Iron Ore", "Rio Tinto"],
    ["West Angelas", -23.18, 118.82, "Iron Ore", "Rio Tinto"],
    ["Yandicoogina", -22.75, 119.23, "Iron Ore", "Rio Tinto"],
    ["Robe Valley (Mesa A/J)", -21.71, 116.00, "Iron Ore", "Rio Tinto"],
    ["Hope Downs 1", -22.95, 119.01, "Iron Ore", "Rio Tinto"],
    ["Hope Downs 4", -23.04, 119.53, "Iron Ore", "Rio Tinto"],
    ["Gudai-Darri", -22.50, 119.07, "Iron Ore", "Rio Tinto"],
    ["Rhodes Ridge", -23.08, 119.33, "Iron Ore", "Rio Tinto"], # Project

    # === RIO TINTO (Copper) ===
    ["Oyu Tolgoi", 43.01, 106.84, "Copper", "Rio Tinto"], # Mongolia
    ["Escondida", -24.27, -69.07, "Copper", "Rio Tinto/BHP"], # Chile
    ["Kennecott (Bingham)", 40.52, -112.15, "Copper", "Rio Tinto"], # USA
    ["Resolution Copper", 33.30, -111.09, "Copper", "Rio Tinto"], # USA (Project)
    ["Winu", -21.43, 122.06, "Copper", "Rio Tinto"], # Australia (Discovery)

    # === RIO TINTO (Aluminum/Bauxite) ===
    ["Weipa (Amrun/Andoom)", -12.52, 141.84, "Bauxite", "Rio Tinto"], # Australia
    ["Gove (Operations)", -12.19, 136.81, "Bauxite", "Rio Tinto"], # Australia
    ["Yarwun Refinery", -23.83, 151.15, "Alumina", "Rio Tinto"],
    ["Queensland Alumina", -23.86, 151.28, "Alumina", "Rio Tinto"],
    ["Bell Bay Aluminium", -41.13, 146.86, "Aluminium", "Rio Tinto"],
    ["Boyne Smelters", -23.93, 151.34, "Aluminium", "Rio Tinto"],
    ["Tomago Aluminium", -32.81, 151.72, "Aluminium", "Rio Tinto"],
    ["BC Works (Kitimat)", 54.00, -128.69, "Aluminium", "Rio Tinto"], # Canada
    ["Saguenay (Alma/Arvida)", 48.55, -71.65, "Aluminium", "Rio Tinto"], # Canada
    ["ISAL", 64.04, -22.03, "Aluminium", "Rio Tinto"], # Iceland
    ["New Zealand Aluminium (Tiwai)", -46.59, 168.38, "Aluminium", "Rio Tinto"],
    ["Sohar Aluminium", 24.41, 56.63, "Aluminium", "Rio Tinto"], # Oman

    # === RIO TINTO (Lithium - Includes Arcadium Assets) ===
    ["Rincon", -24.38, -67.06, "Lithium", "Rio Tinto"], # Argentina
    ["Jadar", 44.53, 19.41, "Lithium", "Rio Tinto"], # Serbia (Project)
    ["Olaroz", -24.11, -66.82, "Lithium", "Rio Tinto"], # Argentina
    ["Salar de Vida", -25.40, -66.88, "Lithium", "Rio Tinto"], # Argentina
    ["Cauchari", -24.08, -66.82, "Lithium", "Rio Tinto"], # Argentina
    ["Fénix (Hombre Muerto)", -25.48, -67.11, "Lithium", "Rio Tinto"], # Argentina
    ["Mt Cattlin", -33.58, 120.04, "Lithium", "Rio Tinto"], # Australia
    ["Naraha", 37.26, 141.00, "Lithium", "Rio Tinto"], # Japan (Plant)
    ["Nemaska Lithium (Whabouchi)", 51.72, -75.98, "Lithium", "Rio Tinto"], # Canada
    ["Bessemer City", 35.28, -81.27, "Lithium", "Rio Tinto"], # USA (Processing)
    ["James Bay", 52.12, -76.06, "Lithium", "Rio Tinto"], # Canada

    # === RIO TINTO (Diamonds & Minerals) ===
    ["Diavik", 64.49, -110.27, "Diamonds", "Rio Tinto"], # Canada
    ["Argyle (Rehab)", -16.71, 128.39, "Diamonds", "Rio Tinto"], # Australia (Closed)
    ["Boron (California)", 35.04, -117.68, "Borates", "Rio Tinto"], # USA
    ["Richards Bay Minerals", -28.78, 32.04, "Titanium", "Rio Tinto"], # South Africa
    ["QIT Madagascar", -24.96, 46.98, "Titanium", "Rio Tinto"], # Madagascar
    ["QIT Fer et Titane (Havre-St-Pierre)", 50.24, -63.59, "Titanium", "Rio Tinto"], # Canada
    ["Simandou", 8.53, -8.93, "Iron Ore", "Rio Tinto"], # Guinea (Project)
    ["Dampier Salt", -20.69, 116.71, "Salt", "Rio Tinto"], # Australia
# === NORTH AMERICA (ARIZONA - Copper) ===
    ["Morenci", 33.09, -109.37, "Copper", "Freeport-McMoRan"], # Largest in N. America
    ["Bagdad", 34.58, -113.21, "Copper", "Freeport-McMoRan"],
    ["Safford (Lone Star)", 32.95, -109.65, "Copper", "Freeport-McMoRan"],
    ["Sierrita", 31.87, -111.13, "Copper", "Freeport-McMoRan"],
    ["Miami", 33.41, -110.87, "Copper", "Freeport-McMoRan"], # Smelter & Mine
    # === NORTH AMERICA (NEW MEXICO - Copper) ===
    ["Chino (Santa Rita)", 32.79, -108.07, "Copper", "Freeport-McMoRan"],
    ["Tyrone", 32.65, -108.36, "Copper", "Freeport-McMoRan"],
    # === NORTH AMERICA (COLORADO - Molybdenum) ===
    ["Henderson", 39.77, -105.85, "Molybdenum", "Freeport-McMoRan"],
    ["Climax", 39.36, -106.17, "Molybdenum", "Freeport-McMoRan"],
    # === SOUTH AMERICA ===
    ["Cerro Verde", -16.54, -71.55, "Copper", "Freeport-McMoRan"], # Peru (Major Asset)
    ["El Abra", -21.92, -68.83, "Copper", "Freeport-McMoRan"], # Chile
    # === INDONESIA (GRASBERG DISTRICT) ===
    ["Grasberg", -4.05, 137.11, "Copper/Gold", "Freeport-McMoRan"], # World's Largest Gold Mine
    # === MEXICO (COPPER OPERATIONS) ===
    ["Buenavista del Cobre", 30.96, -110.36, "Zinc/Copper", "SCCO"], # Also known as Cananea
    ["La Caridad", 30.36, -109.57, "Copper/Moly", "SCCO"],
    ["Pilares", 30.39, -109.55, "Copper", "SCCO"], # Near La Carida
    # === MEXICO (IMMSA UNIT - ZINC/UNDERGROUND) ===
    ["Charcas", 23.13, -101.11, "Zinc", "SCCO"],
    ["Santa Barbara", 26.83, -105.83, "Zinc", "SCCO"],
    ["San Martín", 23.67, -103.78, "Zinc", "SCCO"],
    ["Santa Eulalia", 28.59, -105.84, "Zinc", "SCCO"],
    # === MEXICO (PROJECTS) ===
    ["El Arco", 28.03, -113.43, "Copper", "SCCO"], # Baja California
    ["El Pilar", 31.06, -110.55, "Copper", "SCCO"], # Near Buenavista
    # === PERU (ACTIVE MINES) ===
    ["Toquepala", -17.25, -70.61, "Copper/Moly", "SCCO"],
    ["Cuajone", -17.04, -70.70, "Copper/Moly", "SCCO"],

    # === PERU (PROJECTS) ===
    ["Tía María", -17.01, -71.76, "Copper", "SCCO"],
    ["Los Chancas", -14.10, -73.13, "Copper", "SCCO"],
    ["Michiquillay", -7.05, -78.33, "Copper", "SCCO"],

    # === ERO COPPER ===
    ["Caraíba Operations", -9.86, -39.87, "Copper", "Ero Copper"], # Bahia, Brazil
    ["Tucumã Operation", -6.72, -50.27, "Copper/Gold", "Ero Copper"], # Pará, Brazil
    ["Xavantina Operations", -14.73, -52.35, "Gold", "Ero Copper"], # Mato Grosso, Brazil

    # === HUDBAY MINERALS ===
    ["Copper Mountain", 49.34, -120.55, "Copper/Gold", "Hudbay Minerals"], # BC, Canada
    ["Snow Lake (Lalor)", 54.88, -100.02, "Cooper/Gold", "Hudbay Minerals"], # Manitoba, Canada
    ["Copper World", 31.85, -110.75, "Copper", "Hudbay Minerals"], # Arizona, USA
    ["Mason Project", 38.93, -119.23, "Copper", "Hudbay Minerals"], # Nevada, USA
    ["Constancia", -14.46, -71.76, "Copper/Moly", "Hudbay Minerals"], # Peru
    ["Pampacancha", -14.45, -71.78, "Copper/Gold", "Hudbay Minerals"], # Peru (Near Constancia)

    # === IVANHOE ELECTRIC ===
    ["Santa Cruz", 32.84, -111.83, "Copper", "Ivanhoe Electric"], # Arizona, USA
    ["Tintic", 39.95, -112.11, "Copper/Gold", "Ivanhoe Electric"], # Utah, USA
    ["Hog Heaven", 47.93, -114.57, "Copper/Gold", "Ivanhoe Electric"], # Montana, USA
    ["Ma'aden JV (Al Amar)", 23.78, 45.05, "Copper/Gold", "Ivanhoe Electric/Ma'aden"], # Saudi Arabia

    # TGB
    ["Gibraltar Mine", 52.31, -122.17, "Copper/Moly", "TGB"],
    ["Mountain Pass", 35.48, -115.53, "Rare Earths", "MP Materials"],
        # --- URANIUM ---
    ["McArthur River", 57.76, -105.05, "Uranium", "Cameco"],
    ["Cigar Lake", 58.07, -104.54, "Uranium", "Cameco"],
    ["Lost Creek", 42.12, -107.86, "Uranium", "Ur-Energy"],
    ["White Mesa", 37.47, -109.47, "Uranium", "Energy Fuels"],
    ["Smith Ranch", 43.05, -105.65, "Uranium", "Cameco"],          # NEW
    ["Willow Creek", 43.68, -106.11, "Uranium", "Uranium One"],  

    # --- Teck Resources ---
    ["Highland Valley Copper", 50.452, -121.049, "Copper", "Teck Resources"],
    ["Trail Operations", 49.096, -117.711, "Zinc/Lead", "Teck Resources"],
    ["Antamina", -9.539, -77.055, "Zinc/Copper", "Teck Resources/BHP"], # JV
    ["Quebrada Blanca", -20.615, -68.803, "Copper", "Teck Resources"],
    ["Carmen de Andacollo", -30.252, -71.085, "Copper/Gold", "Teck Resources"],
    ["Red Dog", 68.071, -162.853, "Zinc", "Teck Resources"],

    # --- BHP (Active Operations) ---
    ["Queensland Coal (Bowen Basin)", -21.800, 148.000, "Coal", "BHP"],
    ["Western Australia Iron Ore", -23.363, 119.670, "Iron Ore", "BHP"],
    ["Nickel West", -27.234, 120.537, "Nickel", "BHP"],
    ["Olympic Dam", -30.443, 136.886, "Copper", "BHP"],
    ["Mt Arthur Coal", -32.365, 150.887, "Coal", "BHP"],
    ["Samarco", -20.214, -43.513, "Iron Ore", "BHP"],
    ["Jansen Potash Project", 52.133, -105.150, "Potash", "BHP"],
    ["Escondida", -24.269, -69.070, "Copper", "BHP"],
    ["Spence", -22.783, -69.244, "Copper", "BHP"],
    ["Cerro Colorado", -20.061, -69.261, "Copper", "BHP"],

    # --- BHP (Legacy/Closed/North American Assets) ---
    ["East Kemptville", 44.116, -65.583, "Tin", "BHP (Legacy)"],
    ["Poirier", 49.833, -78.333, "Zinc/Copper", "BHP (Legacy)"],
    ["Selbaie", 49.816, -78.966, "Zinc/Copper", "BHP (Legacy)"],
    ["Island Copper", 50.600, -127.483, "Copper", "BHP (Legacy)"],
    ["Elliot Lake", 46.383, -82.650, "Uranium", "BHP (Legacy)"],
    ["Carson Hill", 38.070, -120.500, "Gold", "BHP (Legacy)"],
    ["Lisbon Valley", 38.233, -109.233, "Copper/Uranium", "BHP (Legacy)"],
    ["Ambrosia Lake", 35.412, -107.830, "Uranium", "BHP (Legacy)"],
    ["Copper Cities", 33.411, -110.860, "Copper", "BHP (Legacy)"],
    ["Miami Unit", 33.400, -110.870, "Copper", "BHP (Legacy)"],
    ["Old Dominion", 33.416, -110.850, "Copper", "BHP (Legacy)"],
    ["Solitude", 33.405, -110.875, "Copper", "BHP (Legacy)"],
    ["San Manuel", 32.613, -110.633, "Copper", "BHP (Legacy)"],
    ["Wolfsberg Lithium Project", 46.837, 14.957, "Lithium", "Critical Metals Corp"],
    ["Tanbreez Project", 60.860, -45.920, "Rare Earths", "Critical Metals Corp"],
    ["Galena Complex", 47.483, -115.973, "Silver/Lead/Antimony", "Americas Gold and Silver"],
    ["Cosalá Operations (San Rafael)", 24.413, -106.692, "Silver/Lead/Zinc", "Americas Gold and Silver"],
    # --- Development / Recent Acquisitions ---
    ["Crescent Silver Mine", 47.490, -116.070, "Silver", "Americas Gold and Silver"], # Acquired Dec 2025
    ["EC120 Project (Cosalá)", 24.408, -106.685, "Copper/Silver", "Americas Gold and Silver"],
    # --- Suspended / Residual Leaching ---
    ["Relief Canyon", 40.204, -118.170, "Gold", "Americas Gold and Silver"], # Located in Nevada, not Arizona
    #Fresnillo
    ["Fresnillo", 23.09, -102.51, "Silver", "Fresnillo"],
    ["Saucito", 23.07, -102.55, "Silver", "Fresnillo"],
    ["Juancipio", 23.07, -102.56, "Silver", "Fresnillo"],
    ["San Julian", 26.02, -106.30, "Gold/Silver", "Fresnillo"],
    ["Cienega", 24.03, -104.40, "Gold/Silver", "Fresnillo"],
    ["Herradura", 31.08, -112.51, "Gold", "Fresnillo"],
    ["Soledad-Dipolos", 31.13, -112.54, "Gold", "Fresnillo"],
    ["Noche Buena", 31.01, -112.39, "Gold", "Fresnillo"],
    #SLI lithium
    ["Southwest Arkansas Project", 33.19, -93.34, "Lithium", "Standard Lithium"],
    ["East Texas", 33.07, -95.10, "Lithium", "Standard Lithium"],
    #Hecla mining
    ["Greens Creek", 58.22, -134.36, "Silver", "Hecla Mining"],
    ["Lucky Friday", 47.28, -115.46, "Silver", "Hecla Mining"],
    ["Casa Berardi", 48.48, -79.13, "Silver", "Hecla Mining"],
    ["Keno Hill", 63.54, -135.19, "Silver", "Hecla Mining"],
    ["Don David", 16.41, -96.42, "Silver", "Gold Resources"],
    ["Back Forty", 45.19, -87.32, "Gold", "Gold Resources"],
    # === AFRICA (NEW) ===
    # Gold
    ["Kibali", 3.12, 29.58, "Gold", "Barrick"], # DRC
    ["Geita", -2.87, 32.19, "Gold", "AngloGold Ashanti"], # Tanzania
    ["Loulo-Gounkoto", 13.01, -11.48, "Gold", "Barrick"], # Mali
    ["Fekola", 12.87, -11.23, "Gold", "B2Gold"], # Mali
    ["Tasiast", 20.61, -15.46, "Gold", "Kinross"], # Mauritania
    # Copper/Cobalt
    ["Kamoa-Kakula", -10.87, 25.43, "Copper", "Ivanhoe Mines"], # DRC (Highest Grade Copper)
    ["Tenke Fungurume", -10.61, 26.17, "Copper", "CMOC"], # DRC
    ["Kansanshi", -12.09, 26.43, "Copper", "First Quantum"], # Zambia
    # Diamonds/Other
    ["Jwaneng", -24.60, 24.73, "Diamonds", "Debswana"], # Botswana (Richest Diamond Mine)
    ["Orapa", -21.30, 25.37, "Diamonds", "Debswana"], # Botswana
    ["Sishen", -27.73, 23.00, "Iron Ore", "Kumba Iron Ore"], # South Africa
    ["Husab", -22.56, 15.04, "Uranium", "Swakop Uranium"], # Namibia
    ["Mogalakwena", -23.97, 28.93, "Platinum", "Anglo American"], # South Africa
    ["Greenbushes", -33.86, 116.06, "Lithium", "Talison Lithium"],
    ["Pilgangoora", -21.03, 118.91, "Lithium", "Pilbara Minerals"],
    ["Mount Isa", -20.73, 139.49, "Zinc", "Glencore"],
    ["Ranger (Rehab)", -12.67, 132.92, "Uranium", "Energy Resources"],
    ["Silver Peak", 37.75, -117.63, "Lithium", "Albemarle"],
    ["Thacker Pass", 41.70, -118.06, "Lithium", "Lithium Americas"],
    ["Halleck Creek", 41.80, -105.20, "Rare Earths", "American Rare Earths"],
    ["Bécancour (Project)", 46.33, -72.44, "Lithium", "Sayona Mining"],
    ["Whabouchi", 51.72, -75.98, "Lithium", "Nemaska Lithium"],    # NEW
    ["North American Lithium", 48.33, -77.84, "Lithium", "Sayona"], # NEW
    ["Salar de Atacama", -23.50, -68.30, "Lithium", "SQM/Albemarle"], # NEW (Chile Major)   
    # --- IRON ORE ---
    ["Mesabi Range", 47.50, -92.54, "Iron Ore", "Cleveland-Cliffs"],
    ["Mary River", 71.32, -79.35, "Iron Ore", "Baffinland"],
    ["Bloom Lake", 52.84, -67.33, "Iron Ore", "Champion Iron"],
    ["Mont-Wright", 52.76, -67.35, "Iron Ore", "ArcelorMittal"],   # NEW
    ["Carol Lake", 52.95, -66.92, "Iron Ore", "Rio Tinto"],        # NEW
    ["Carajas", -6.06, -50.17, "Iron Ore", "Vale"],                # NEW (Brazil - World's Largest)
    #copper
    ["Mount Milligan", 55.12, -123.98, "Copper", "Centerra Gold"], # NEW
    ["Copper Mountain", 49.33, -120.53, "Copper", "Hudbay"],       # NEW
    ["Pinto Valley", 33.40, -110.96, "Copper", "Capstone Copper"], # NEW
    ["Buenavista del Cobre", 31.00, -110.37, "Copper", "Grupo México"], # NEW
    ["La Caridad", 30.34, -109.58, "Copper", "Grupo México"],      # NEW
    ["Antamina", -9.53, -77.05, "Copper", "BHP/Glencore"],         # NEW (Peru Major)
    ["Carlin Trend", 40.97, -116.33, "Gold", "Nevada Gold Mines"],
    ["Cortez", 40.25, -116.70, "Gold", "Nevada Gold Mines"],
    ["Turquoise Ridge", 41.20, -117.20, "Gold", "Nevada Gold Mines"],
    ["Las Bambas", -14.10, -72.32, "Copper", "MMG"],
        # Iron Ore (Pilbara Region)
    ["Tom Price", -22.76, 117.76, "Iron Ore", "Rio Tinto"],
    ["Newman (Mt Whaleback)", -23.36, 119.73, "Iron Ore", "BHP"],
    ["Solomon Hub", -22.22, 117.99, "Iron Ore", "Fortescue"],
    ["Roy Hill", -22.44, 119.95, "Iron Ore", "Hancock Prospecting"],
    # Gold
    ["Super Pit (Kalgoorlie)", -30.78, 121.50, "Gold", "Northern Star"],
    ["Carajas", -6.06, -50.17, "Iron Ore", "Vale"], # World's Largest Iron Ore Mine
    ["Greenbushes", -33.86, 116.06, "Lithium", "Talison Lithium"], # World's Highest Grade Lithium
    ["Pilgangoora", -21.03, 118.91, "Lithium", "Pilbara Minerals"],
    ["Mount Isa", -20.73, 139.49, "Zinc", "Glencore"],
    ["Ranger (Rehab)", -12.67, 132.92, "Uranium", "Energy Resources of Aus"],
    ["Fekola", 12.87, -11.23, "Gold", "B2Gold"], # Mali
    ["Jwaneng", -24.60, 24.73, "Diamonds", "Debswana"], # Botswana (Richest Diamond Mine)
    ["Orapa", -21.30, 25.37, "Diamonds", "Debswana"], # Botswana
    ["Sishen", -27.73, 23.00, "Iron Ore", "Kumba Iron Ore"], # South Africa
    ["Husab", -22.56, 15.04, "Uranium", "Swakop Uranium"], # Namibia
    ["Mogalakwena", -23.97, 28.93, "Platinum", "Anglo American"], # South Africa
    ["Mont-Wright", 52.76, -67.35, "Iron Ore", "ArcelorMittal"],
    ["Buenavista", 31.00, -110.37, "Copper", "Grupo México"],   
    ["Waterberg", -23.40, 27.32, "Platinum", "PGM"],
    ["Avino Mine", 24.31, -104.18, "Silver", "ASM"],
    # --- First Majestic Silver Corp (AG) ---
    ["San Dimas", 24.108, -105.933, "Gold/Silver", "First Majestic Silver"],
    ["Santa Elena", 29.989, -110.228, "Gold/Silver", "First Majestic Silver"],
    ["La Encantada", 28.356, -102.523, "Silver", "First Majestic Silver"],
    ["Cerro Los Gatos", 27.583, -106.350, "Silver/Lead/Zinc", "First Majestic Silver"], # Acquired via Gatos Silver merger
    # --- Endeavour Silver Corp (EXK/EDR) ---
    ["Guanaceví", 25.917, -105.988, "Gold/Silver", "Endeavour Silver"],
    ["Terronera", 20.761, -104.853, "Gold/Silver", "Endeavour Silver"], # Recently commissioned (Construction Journey Complete)
    ["Kolpa", -13.064, -74.962, "Silver/Lead/Zinc", "Endeavour Silver"], # New acquisition in Huancavelica, Peru
# ---------------------------------------------------------
    # ANGLO AMERICAN
    # ---------------------------------------------------------
    # --- Copper (Core) ---
    ["Los Bronces", -33.145, -70.267, "Copper", "Anglo American"],
    ["Collahuasi", -20.963, -68.614, "Copper", "Anglo American (44% JV)"],
    ["El Soldado", -32.650, -71.066, "Copper", "Anglo American"],
    ["Quellaveco", -17.106, -70.613, "Copper", "Anglo American"],
    
    # --- Iron Ore (Core) ---
    ["Minas-Rio", -18.916, -43.433, "Iron Ore", "Anglo American"],
    ["Sishen (Kumba)", -27.733, 23.000, "Iron Ore", "Anglo American"],
    ["Kolomela (Kumba)", -28.383, 22.950, "Iron Ore", "Anglo American"],
    
    # --- Crop Nutrients (Core) ---
    ["Woodsmith Project", 54.433, -0.617, "Potash", "Anglo American"],
    
    # --- Assets in Divestment / Sale Process / Dispute ---
    ["Moranbah North", -21.995, 148.068, "Coal", "Anglo American (Coal)"],
    ["Grosvenor", -21.983, 148.016, "Coal", "Anglo American (Coal)"],
    ["Aquila", -22.016, 148.033, "Coal", "Anglo American (Coal)"],
    ["Capcoal (German Creek)", -22.966, 148.550, "Coal", "Anglo American (Coal)"],
    ["Venetia", -22.433, 29.317, "Diamonds", "De Beers (Anglo)"],
    ["Jwaneng", -24.522, 24.695, "Diamonds", "De Beers (Anglo)"],
    ["Gahcho Kué", 63.433, -109.183, "Diamonds", "De Beers (Anglo)"],

    # ---------------------------------------------------------
    # VALE S.A.
    # ---------------------------------------------------------
    # --- Iron Ore (Brazil) ---
    ["S11D (Carajás)", -6.413, -50.360, "Iron Ore", "Vale"],
    ["Carajás Serra Norte", -6.066, -50.183, "Iron Ore", "Vale"],
    ["Brucutu", -19.866, -43.376, "Iron Ore", "Vale"],
    ["Itabira Complex", -19.633, -43.233, "Iron Ore", "Vale"],
    ["Timbopeba", -20.283, -43.516, "Iron Ore", "Vale"],
    ["Vargem Grande", -20.200, -43.916, "Iron Ore", "Vale"],
    
    # --- Energy Transition Metals (Copper/Nickel) ---
    ["Salobo", -5.792, -50.533, "Copper/Gold", "Vale Base Metals"],
    ["Sossego", -6.433, -50.066, "Copper", "Vale Base Metals"],
    ["Onça Puma", -6.616, -51.066, "Nickel", "Vale Base Metals"],
    ["Sudbury Operations (Creighton)", 46.476, -81.192, "Nickel/Copper", "Vale Base Metals"],
    ["Voisey's Bay", 56.333, -62.094, "Nickel/Cobalt", "Vale Base Metals"],
    ["Thompson", 55.727, -97.873, "Nickel", "Vale Base Metals"],
    ["PT Vale Indonesia (Sorowako)", -2.548, 121.352, "Nickel", "Vale (JV)"],
    # ---------------------------------------------------------
    # GLENCORE
    # ---------------------------------------------------------
    # --- Copper (South America & Africa) ---
    ["Katanga (KCC)", -10.733, 25.433, "Copper/Cobalt", "Glencore"],
    ["Mutanda", -10.793, 25.460, "Copper/Cobalt", "Glencore"],
    ["Antapaccay", -14.922, -71.286, "Copper", "Glencore"],
    ["Lomas Bayas", -22.508, -69.259, "Copper", "Glencore"],
    ["Antamina", -9.539, -77.055, "Zinc/Copper", "Glencore (33.75% JV)"],
    
    # --- Zinc / Lead ---
    ["McArthur River Mine", -16.442, 136.104, "Zinc/Lead", "Glencore"],
    ["Mount Isa (Zinc/Lead)", -20.730, 139.492, "Zinc/Lead", "Glencore"], # Copper mining ceased July 2025
    ["Kidd Operations", 48.697, -81.366, "Zinc/Copper", "Glencore"],
    ["Kazzinc (Ridder)", 50.347, 83.514, "Zinc/Gold", "Glencore"],
    
    # --- Nickel ---
    ["Raglan Mine", 61.691, -73.676, "Nickel", "Glencore"],
    ["Sudbury INO (Nickel Rim)", 46.616, -80.976, "Nickel", "Glencore"],
    ["Murrin Murrin", -28.913, 121.896, "Nickel/Cobalt", "Glencore"],
    
    # --- Coal (Energy & Steelmaking) ---
    ["Cerrejón", 11.111, -72.610, "Coal", "Glencore"],
    ["Elk Valley (Fording River)", 50.193, -114.878, "Coal", "Glencore (EVR)"],
    ["Elk Valley (Elkview)", 49.744, -114.832, "Coal", "Glencore (EVR)"],
    ["Elk Valley (Greenhills)", 50.050, -114.866, "Coal", "Glencore (EVR)"],
    ["Oaky Creek", -23.066, 148.483, "Coal", "Glencore"],
    ["Rolleston", -24.583, 148.421, "Coal", "Glencore"],
    ["Hunter Valley Ops", -32.533, 151.083, "Coal", "Glencore (JV)"],
    
    # --- Ferroalloys ---
    ["Rhovan", -25.292, 27.266, "Vanadium", "Glencore"],
    ["Lion Ferrochrome", -24.933, 30.133, "Ferrochrome", "Glencore"], # --- Silvercorp Metals (China) ---
    ["Ying Mining District (SGX/HZG/TLP/LME/DCG)", 34.156, 111.328, "Silver/Lead/Zinc", "Silvercorp Metals"],
    ["Gaocheng (GC) Mine", 22.924, 112.033, "Silver/Lead/Zinc", "Silvercorp Metals"],
    ["Kuanping Project", 34.450, 111.350, "Silver/Lead/Zinc", "Silvercorp Metals"], # ~33km North of Ying
    
    # --- New Pacific Metals (Bolivia) ---
    ["Silver Sand", -19.368, -65.523, "Silver", "New Pacific Metals"],
    ["Carangas", -18.233, -68.566, "Gold/Silver", "New Pacific Metals"],
    ["Silverstrike", -17.383, -69.116, "Gold/Silver", "New Pacific Metals"],
    
    # --- Dolly Varden Silver (Canada/USA) ---
    ["Kitsault Valley (Dolly Varden)", 55.678, -129.511, "Silver", "DVS / Contango ORE (MergeCo)"],
    ["Kitsault Valley (Homestake Ridge)", 55.761, -129.576, "Gold/Silver", "DVS / Contango ORE (MergeCo)"],
    ["Big Bulk", 55.680, -129.430, "Copper", "DVS / Contango ORE (MergeCo)"],
    
    # --- Contango ORE (Merger Assets) ---
    ["Manh Choh", 63.013, -142.238, "Gold", "DVS / Contango ORE (MergeCo)"],
    [ "Gruyere", -27.9920, 123.8560, "Gold", "Gold Fields / Gold Road Resources" ],
    [ "Agnew", -27.9170, 120.7000, "Gold", "Gold Fields" ],
    [ "St Ives", -31.3300, 121.7800, "Gold", "Gold Fields" ],
    [ "Granny Smith", -28.8100, 122.4100, "Gold", "Gold Fields" ],
    [ "Windfall", 49.0700, -75.6400, "Gold", "Osisko Mining / Gold Fields" ],
    [ "Salares Norte", -26.0117, -68.8931, "Gold", "Gold Fields" ],
    [ "Damang", 5.5100, -1.8400, "Gold", "Gold Fields" ],
    [ "Tarkwa", 5.3200, -1.9900, "Gold", "Gold Fields" ],
    [ "Cerro Corona", -6.7600, -78.6300, "Copper/Gold", "Gold Fields" ],
    [ "South Deep", -26.4170, 27.6670, "Gold", "Gold Fields" ],
    [ "Allan", 51.9300, -106.0700, "Potash", "Nutrien" ],
    [ "Bald Mountain", 39.9300, -115.5400, "Gold", "Kinross Gold" ],
    [ "Bellevue", -27.6000, 120.5400, "Gold", "Bellevue Gold" ],
    [ "Canadian Malartic", 48.1200, -78.1300, "Gold", "Agnico Eagle Mines" ],
    [ "Côté Gold", 47.5500, -81.9300, "Gold", "IAMGOLD" ],
    [ "Dolores", 29.0000, -108.5300, "Gold/Silver", "Pan American Silver" ],
    [ "Don Nicolas", -49.1744, -69.2469, "Gold/Silver", "Minera Don Nicolás" ],
    [ "El Limon", 17.9200, -99.8800, "Gold", "Torex Gold (El Limon-Guajes)" ],
    [ "Goldstrike", 40.9800, -116.3700, "Gold", "Nevada Gold Mines" ],
    [ "Granite Creek", 41.1300, -117.2700, "Gold", "i-80 Gold" ],
    [ "Gwalia", -28.9200, 121.3300, "Gold", "Genesis Minerals" ],
    [ "Johnson Camp", 32.1000, -110.0600, "Copper", "Excelsior Mining" ],
    [ "Khoemacau", -20.5000, 22.5000, "Copper/Silver", "MMG Limited" ],
    [ "King of the Hills", -28.6800, 121.1700, "Gold", "Red 5 Limited" ],
    [ "LaRonde Zone 5", 48.2500, -78.4400, "Gold", "Agnico Eagle Mines" ],
    [ "Leeville", 40.9100, -116.3200, "Gold", "Nevada Gold Mines" ],
    [ "Manh Choh", 63.1300, -142.5200, "Gold", "Kinross Gold / Contango Ore" ],
    [ "Mara Rosa", -14.0200, -49.1700, "Gold", "Hochschild Mining" ],
    [ "Marigold", 40.7500, -117.1500, "Gold", "SSR Mining" ],
    [ "Meekatharra", -26.5900, 118.4900, "Gold", "Westgold Resources" ],
    [ "Peñasquito", 24.6600, -101.7200, "Silver/Lead/Zinc", "Newmont" ],
    [ "Rainy River", 48.8500, -94.0000, "Gold", "New Gold" ],
    [ "Red Chris", 57.7000, -129.7800, "Copper/Gold", "Newcrest (Newmont)" ],
    [ "Robinson", 39.2600, -115.0100, "Copper/Gold", "KGHM Polska Miedź" ],
    [ "Ruby Hill", 39.4900, -115.9900, "Gold", "i-80 Gold" ],
    [ "Skyline", 39.6900, -111.2200, "Coal", "Wolverine Fuels" ],
    [ "South Laverton", -30.1500, 122.3400, "Gold", "Northern Star Resources (Carosue Dam)" ],
    [ "Southern Cross", -30.7500, 121.7800, "Gold", "Minjar Gold" ],
    [ "Twin Creeks", 41.2200, -117.1900, "Gold", "Nevada Gold Mines" ],
    [ "Ulysses", -29.1800, 121.3200, "Gold", "Genesis Minerals" ],
    [ "Wassa", 5.4300, -1.9000, "Gold", "Chifeng Jilong Gold" ],
    [ "Wharf", 44.3500, -103.9200, "Gold", "Coeur Mining" ],
    [ "Williams", 48.6900, -85.9300, "Gold", "Barrick Gold (Hemlo)" ],
    [ "Wonder", -28.3000, 121.0000, "Gold", "Northern Star Resources" ],
    [ "Xavantina", -14.7000, -52.3500, "Gold", "Ero Copper" ],
    # --- Pan American Silver: Silver Segment ---
    ["Juanicipio", 23.0900, -102.8500, "Gold/Silver", "Fresnillo / Pan American Silver (44%)"],
    ["La Colorada", 23.7900, -103.8300, "Silver/Lead/Zinc", "Pan American Silver"],
    ["Cerro Moro", -48.0100, -69.2300, "Gold/Silver", "Pan American Silver"],
    ["Huaron", -10.9900, -76.4300, "Silver/Lead/Zinc", "Pan American Silver"],
    ["San Vicente", -21.3100, -66.3500, "Silver/Lead/Zinc", "Pan American Silver (95%)"],
    ["Escobal", 14.4300, -90.4100, "Silver", "Pan American Silver (Suspended)"],
    ["La Colorada Skarn", 23.8000, -103.8200, "Silver/Lead/Zinc", "Pan American Silver (Dev)"],
    ["Navidad", -42.4200, -68.8300, "Silver", "Pan American Silver (Stalled)"],

    # --- Pan American Silver: Gold Segment ---
    ["Jacobina", -11.1800, -40.5100, "Gold", "Pan American Silver"],
    ["El Peñon", -24.6300, -69.8400, "Gold/Silver", "Pan American Silver"],
    ["Timmins (West/Bell Creek)", 48.3300, -81.5600, "Gold", "Pan American Silver"],
    ["Shahuindo", -7.4300, -78.0100, "Gold/Silver", "Pan American Silver"],
    ["Minera Florida", -34.0400, -70.0200, "Gold/Silver", "Pan American Silver"],
    ["Dolores", 28.9900, -108.5300, "Gold/Silver", "Pan American Silver"],

    # --- Alamos Gold (AGI) ---
    ["Island Gold District", 48.2900, -84.4300, "Gold", "Alamos Gold"],
    ["Young-Davidson", 47.9300, -80.6500, "Gold", "Alamos Gold"],
    ["Mulatos District", 28.6400, -108.7500, "Gold", "Alamos Gold"],

    # --- Coeur Mining (CDE) ---
    ["Las Chispas", 30.2200, -110.1300, "Gold/Silver", "Coeur Mining"],
    ["Palmarejo", 27.3800, -108.4300, "Gold/Silver", "Coeur Mining"],
    ["Rochester", 40.2900, -118.1500, "Gold/Silver", "Coeur Mining"],
    ["Kensington", 58.8600, -135.0800, "Gold", "Coeur Mining"],
    ["Wharf", 44.3500, -103.9200, "Gold", "Coeur Mining"],
    ["Greenstone", 49.7100, -86.9500, "Gold", "Equinox Gold"],
    ["Valentine", 48.4600, -56.8800, "Gold", "Equinox Gold"],
    ["Mesquite", 33.0500, -114.9800, "Gold", "Equinox Gold"],
    ["Nicaragua Operations (Limon/Libertad)", 12.7200, -86.6300, "Gold", "Equinox Gold"],
    ["Los Filos", 17.9600, -99.6800, "Gold", "Equinox Gold"],
    ["Castle Mountain", 35.2900, -115.1100, "Gold", "Equinox Gold"],

    # --- Eldorado Gold (EGO) ---
    ["Lamaque Complex", 48.0900, -77.7800, "Gold", "Eldorado Gold"],
    ["Olympias", 40.6100, 23.7300, "Gold/Silver", "Eldorado Gold"],
    ["Efemçukuru", 38.2900, 27.0200, "Gold", "Eldorado Gold"],
    ["Kışladağ", 38.4800, 29.1500, "Gold", "Eldorado Gold"],
    ["Skouries", 40.4700, 23.7000, "Copper/Gold", "Eldorado Gold (Dev)"],

    # --- Harmony Gold (HMY) - Australia & PNG ---
    ["Eva Copper", -19.9500, 140.1600, "Copper/Gold", "Harmony Gold (Dev)"],
    ["CSA Mine", -31.5100, 145.8200, "Copper", "Harmony Gold"],
    ["Wafi-Golpu", -6.8700, 146.4600, "Copper/Gold", "Harmony Gold (JV)"],
    ["Hidden Valley", -7.4800, 146.6500, "Gold/Silver", "Harmony Gold"],

    # --- Harmony Gold (HMY) - South Africa ---
    ["Mponeng", -26.4300, 27.4200, "Gold", "Harmony Gold"],
    ["Moab Khotsong", -26.9800, 26.7800, "Gold", "Harmony Gold"],
    ["Mine Waste Solutions", -26.8900, 26.7600, "Gold (Tailings)", "Harmony Gold"],
    ["Kalgold", -26.1300, 25.2400, "Gold", "Harmony Gold"],
    ["Doornkop", -26.2100, 27.7900, "Gold", "Harmony Gold"],
    ["Kusasalethu", -26.4500, 27.3600, "Gold", "Harmony Gold"],
    ["Tshepong North", -27.8800, 26.7000, "Gold", "Harmony Gold"],
    ["Tshepong South", -27.9100, 26.7200, "Gold", "Harmony Gold"],
    ["Target 1", -27.7300, 26.5700, "Gold", "Harmony Gold"],
    ["Joel", -28.2700, 26.8300, "Gold", "Harmony Gold"],
    ["Masimong", -27.9500, 26.8600, "Gold", "Harmony Gold"],
    ["Jamalco", 17.970, -77.230, "Bauxite", "Century Aluminum"],
]

color_map = {
    # --- Single Metals ---
    "Gold": "gold",
    "Copper": "orange",
    "Silver": "lightgray",
    "Lithium": "purple",
    "Uranium": "green",
    "Rare Earths": "darkred",
    "Bauxite": "brown",
    "Aluminium": "beige",
    "Alumina": "beige",
    "Cobalt": "blue",
    "Nickel": "darkblue",
    "Zinc": "cadetblue",
    "Iron Ore": "black",
    "Diamonds": "lightblue",
    "Platinum": "lightgray",
    "Molybdenum": "darkviolet",
    "Tin": "gray",
    "Borates": "pink",
    "Salt": "white",
    "Titanium": "darkgreen",
    "Lead": "darkblue",
    "Coal": "darkgray",
    "Potash": "lightgreen",
    "Antimony": "slategray",

    # --- Mixed Metals ---
    "Gold/Silver": ["gold", "lightgray"],
    "Copper/Gold": ["orange", "gold"],
    "Silver/Lead/Zinc": ["lightgray", "darkblue", "cadetblue"],
    "Nickel/Cobalt": ["darkblue", "blue"],
    "Copper/Silver": ["orange", "lightgray"],
    "Zinc/Gold": ["cadetblue", "gold"],
    "Zinc/Copper": ["cadetblue", "orange"],
    "Zinc/Lead": ["cadetblue", "darkblue"],
    "Copper/Cobalt": ["orange", "blue"],
    "Silver/Lead/Antimony": ["lightgray", "darkblue", "slategray"],
    "Copper/Moly": ["orange", "darkviolet"],
    
    # --- CATCH-ALL ---
    "Other": "gray" # Added this to catch errors
}

# 3. Initialize Map
m = folium.Map(location=[10, 0], zoom_start=2, tiles="CartoDB positron")

# 4. Add Legend (FIXED to handle lists of colors)
legend_items = []
for m_name, c in color_map.items():
    # If color is a list, pick the first one for the legend icon
    display_color = c[0] if isinstance(c, list) else c
    legend_items.append(f'<i class="fa fa-circle" style="color:{display_color}"></i> {m_name}<br>')

legend_html = f'''
      <div style="position: fixed; 
      bottom: 50px; left: 50px; width: 180px; height: 300px; 
      background-color: white; border:2px solid grey; z-index:9999; font-size:12px;
      padding: 10px; opacity: 0.9; overflow-y: auto;">
      <b>Metal Type</b><br>
      {"".join(legend_items)}
      </div>
      '''
m.get_root().html.add_child(folium.Element(legend_html))

# 5. Create Feature Groups
feature_groups = {}
for metal in color_map.keys():
    feature_groups[metal] = folium.FeatureGroup(name=metal)
    m.add_child(feature_groups[metal])

# 6. Add Points (FIXED to handle unknown keys and list-colors)
for name, lat, lon, metal, operator in mining_data:
    
    # Check if the metal exists in our map. If not, switch to "Other"
    if metal in feature_groups:
        group_key = metal
        raw_color = color_map[metal]
    else:
        group_key = "Other"
        raw_color = "gray"
        # Optional: Print warning to see what is missing
        # print(f"Warning: {metal} not found in color_map. Added to 'Other'.")

    # Handle if the color is a list (Pick index 0 for the marker color)
    if isinstance(raw_color, list):
        final_color = raw_color[0]
    else:
        final_color = raw_color

    popup_text = f"<b>{name}</b><br>Metal: {metal}<br>Operator: {operator}"
    
    folium.CircleMarker(
        location=[lat, lon],
        radius=6,
        popup=popup_text,
        color=final_color,       # Use the processed single color
        fill=True,
        fill_color=final_color,  # Use the processed single color
        fill_opacity=0.7
    ).add_to(feature_groups[group_key]) # Add to the valid group key

# 7. Add Layer Control
folium.LayerControl(collapsed=False).add_to(m)

# 8. Save
m.save("mining_map_fixed.html")
print(f"Success! Map saved.")