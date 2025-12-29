import pandas as pd

# List of locations with names and coordinates (latitude, longitude)
locations = [
    ("Depoh Environment Idaman Langkawi", 6.365312, 99.779810),
    ("Langkawi Landfill", 6.395312, 99.859310),
    ("JALAN 1", 6.320843, 99.848460),
    ("JALAN AIRPORT CHENANG", 6.350335, 99.730500),
    ("JALAN BATU ASAH", 6.343856, 99.810250),
    ("JALAN BATU BELAH-BATU BERTANGKUP", 6.320636, 99.746660),
    ("JALAN BEHOR TEMPOYAK", 6.298007, 99.730200),
    ("JALAN BENDANG BARU", 6.315015, 99.857080),
    ("JALAN BUKIT HANTU", 6.362556, 99.786222),
    ("JALAN CHANDEKURA", 6.329416, 99.743910),
    ("JALAN DAHLIA", 6.331417, 99.851917),
    ("JALAN DATAI", 6.409967, 99.716500),
    ("JALAN DATARAN LANG", 6.307500, 99.853000),
    ("JALAN DINDONG", 6.336361, 99.813750),
    ("JALAN INDERALOKA", 6.306156, 99.861010),
    ("JALAN KAMPUNG BUKIT PUTIH", 6.334722, 99.874750),
    ("JALAN KEDAWANG", 6.311093, 99.736750),
    ("JALAN KELIBANG", 6.327359, 99.834870),
    ("JALAN KENYUM", 6.341325, 99.759220),
    ("JALAN KUAH - PADANG MATSIRAT", 6.328972, 99.83103),
    ("JALAN KUAH AYER HANGAT SELATAN", 6.330778, 99.856556),
    ("JALAN KUAH-AYER HANGAT UTARA", 6.421997, 99.816510),
    ("JALAN KUALA MELAKA", 6.351111, 99.722611),
    ("JALAN KUALA MUDA", 6.331283, 99.724090),
    ("JALAN LUBUK SETUL", 6.360496, 99.737110),
    ("JALAN MAKAM MAHSURI", 6.340360, 99.786920),
    ("JALAN MATA AYER", 6.331805, 99.773460),
    ("JALAN NYIOR CABANG", 6.362239, 99.745850),
    ("JALAN PADANG MATSIRAT", 6.323974, 99.786660),
    ("JALAN PADANG PUTIH", 6.287028, 99.733778),
    ("JALAN PANDAK MAYAH 1", 6.322172, 99.849320),
    ("JALAN PANDAK MAYAH 2", 6.323056, 99.849222),
    ("JALAN PANDAK MAYAH 6", 6.321584, 99.850590),
    ("JALAN PANDAK MAYAH 7", 6.321854, 99.852350),
    ("JALAN PANTAI CENANG", 6.292503, 99.726130),
    ("JALAN PANTAI DATO SYED OMAR", 6.302940, 99.851770),
    ("JALAN PANTAI KOK SELATAN", 6.366004, 99.71224),
    ("JALAN PANTAI KOK UTARA", 6.3664092, 99.6862393),
    ("JALAN PANTAI TENGAH", 6.295222, 99.739778),
    ("JALAN PASIR HITAM", 6.429361, 99.796722),
    ("JALAN PENARAK", 6.313083,99.857056),
    ("JALAN PERSIARAN NILAM 3", 6.378305, 99.869970),
    ("JALAN PERSIARAN PUTRA", 6.315729, 99.853860),
    ("JALAN SERI LAGENDA", 6.318605, 99.856860),
    ("JALAN TANJUNG RHU", 6.446715, 99.810670),
    ("JALAN TELUK BURAU", 6.367088, 99.676430),
    ("JALAN TELUK EWA", 6.419722, 99.761167),
    ("JALAN TELUK YU", 6.396408, 99.741800),
    ("JALAN TEMOYONG", 6.282945, 99.747060),
    ("JALAN TERIANG", 6.367525, 99.725670),
    ("JALAN TIARA", 6.324861, 99.843680),
    ("JALAN ULU MELAKA (SELATAN)", 6.354710, 99.770750),
    ("JALAN ULU MELAKA (UTARA)", 6.413222, 99.801167),
    ("KAMPUNG JALAN MASUK PADANG LUNAS", 6.328222, 99.863667),
    ("LORONG PENARAK", 6.317583,99.855611)
]

# Conversion factor from degrees to kilometers
DEGREE_TO_KM = 111

def manhattan_distance(loc1, loc2):
    """
    Calculate the Manhattan distance between two locations (latitude, longitude) in kilometers, rounded to 2 decimal places.
    """
    lat1, lon1 = loc1[1], loc1[2]
    lat2, lon2 = loc2[1], loc2[2]
    
    # Calculate the Manhattan distance in degrees and convert to kilometers
    distance = abs(lat1 - lat2) + abs(lon1 - lon2)
    return round(distance * DEGREE_TO_KM, 2)  # Round to 2 decimal places

# List to hold location names
location_names = [loc[0] for loc in locations]

# Create a matrix to store the distances
distance_matrix = []

# Iterate through all pairs of locations
for loc1 in locations:
    row = []
    for loc2 in locations:
        # Calculate the distance between loc1 and loc2
        distance = manhattan_distance(loc1, loc2)
        row.append(distance)
    distance_matrix.append(row)

# Convert the distance matrix to a pandas DataFrame
distance_df = pd.DataFrame(distance_matrix, columns=location_names, index=location_names)

# Save the DataFrame to an Excel file
distance_df.to_excel("distance_matrix.xlsx", engine="openpyxl")

# Inform the user that the matrix has been saved
print("Distance matrix has been saved to 'distance_matrix.xlsx' with distances rounded to 2 decimal places.")
