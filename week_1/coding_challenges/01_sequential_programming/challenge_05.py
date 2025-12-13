# Coding Challenge 5: Farmer Problem Statement 
'''
Mahesh is a farmer and owns 80 acres of land. His land is equally divided into 5 segments. He grows  
tomatoes in the 1st segment, potatoes in the 2nd segment, cabbage in the 3rd segment, sunflower in  
the 4th segment and sugarcane in the 5th segment. He is converting his land from chemical-driven  
farming to chemical-free farming. Mahesh starts with the conversion of vegetables into chemical-free  
produce. He spends the first 6 months doing the same. He then converts the sunflower land bank 
into chemical-free farming. This takes him another 4 months. Finally, he converts sugarcane into 
chemical-free farming over the next 4 months. He gets a yield of the following for tomatoes. 30% of 
his tomato land gives him 10 tonne yield per acre. The remaining 70% of his tomato land gives him 
12 tonnes yield per acre. The selling price of tomato is Rs. 7 per Kg. The yield of potatoes is 10 tonnes 
per acre. He sells each kg at Rs. 20. The yield of cabbage is 14 tonnes per acre. He sells each kg at Rs. 
24. The yield of sunflowers is 0.7 tonnes per acre. He sells each kg at Rs. 200. The yield of sugarcane 
is 45 tonnes per acre. He sells each tonne at Rs. 4,000. All the crops are sowed at the same time. 
Mahesh gets the above yield at the above-mentioned rate in one crop cycle across his entire land of 
80 acres.  
What is  
a. The overall sales achieved by Mahesh from the 80 acres of land.  
b. Sales realisation from chemical-free farming at the end of 11 months
'''

# Function to compute revenue from all crops
def compute_revenue(total_acres = 80):
    segments = 5
    # tomato , potato, cabbage, sunflower, sugarcane
    acre_per_segment = total_acres / segments
    
    crops = {} # dictionary to hold crop details
    
    # Tomato details
    tomato_acre = acre_per_segment
    t1_acre = 0.30 * tomato_acre
    t2_acre = 0.70 * tomato_acre
    t1_yield = t1_acre * 10 # in tonnes
    t2_yield = t2_acre * 12 # in tonnes
    tomato_yield = t1_yield + t2_yield
    tomato_price_per_ton = 7 * 1000 # converting to per tonne
    tomato_revenue = tomato_yield * tomato_price_per_ton
    
    crops['tomato'] = {
        'acre': tomato_acre,
        'yield_tonnes': tomato_yield,
        'price_per_tonne': tomato_price_per_ton,
        'revenue': tomato_revenue
    }
    
    # Potato details
    potato_acre = acre_per_segment  
    potato_yield = potato_acre * 10 # in tonnes
    potato_price_per_ton = 20 * 1000 # converting to per tonne
    potato_revenue = potato_yield * potato_price_per_ton
    
    crops['potato'] = {
        'acre': potato_acre,
        'yield_tonnes': potato_yield,
        'price_per_tonne': potato_price_per_ton,
        'revenue': potato_revenue
    }
    
    # Cabbage details
    cabbage_acre = acre_per_segment     
    cabbage_yield = cabbage_acre * 14 # in tonnes
    cabbage_price_per_ton = 24 * 1000 # converting to per tonne
    cabbage_revenue = cabbage_yield * cabbage_price_per_ton
    
    crops['cabbage'] = {
        'acre': cabbage_acre,   
        'yield_tonnes': cabbage_yield,
        'price_per_tonne': cabbage_price_per_ton,
        'revenue': cabbage_revenue
    }
    
    # Sunflower details
    sunflower_acre = acre_per_segment
    sunflower_yield = sunflower_acre * 0.7 # in tonnes
    sunflower_price_per_ton = 200 * 1000 # converting to per tonne
    sunflower_revenue = sunflower_yield * sunflower_price_per_ton   
    
    crops['sunflower'] = {
        'acre': sunflower_acre,
        'yield_tonnes': sunflower_yield,
        'price_per_tonne': sunflower_price_per_ton,
        'revenue': sunflower_revenue
    }
    
    # Sugarcane details
    sugarcane_acre = acre_per_segment   
    sugarcane_yield = sugarcane_acre * 45 # in tonnes
    sugarcane_price_per_ton = 4000 # already per tonne
    sugarcane_revenue = sugarcane_yield * sugarcane_price_per_ton
    
    crops['sugarcane'] = {
        'acre': sugarcane_acre,
        'yield_tonnes': sugarcane_yield,
        'price_per_tonne': sugarcane_price_per_ton,
        'revenue': sugarcane_revenue
    }

    # Calculate total tonnes, total revenue
    total_tonnes = sum(crop['yield_tonnes'] for crop in crops.values())
    total_revenue = sum(crop['revenue'] for crop in crops.values())
    
    # Calculate chemical-free revenue after 11 months
    chemical_free_crops = ['tomato', 'potato', 'cabbage', 'sunflower']
    chemical_free_revenue = sum(crops[crop]['revenue'] for crop in chemical_free_crops)
    
    return {
        'crops': crops,
        'total_tonnes': total_tonnes,
        'total_revenue': total_revenue,
        'chemical_free_revenue': chemical_free_revenue
    }
    
    
# Function to print the revenue report    
def print_revenue_report(revenue_data):
    
    crops = revenue_data['crops']
    
    print("Crop Revenue Details:")
    for crop, details in crops.items():
        print(f"{crop.capitalize()}:")
        print(f"  Acreage: {details['acre']:.2f} acres")
        print(f"  Yield: {details['yield_tonnes']:.2f} tonnes")
        print(f"  Price per Tonne: Rs. {details['price_per_tonne']:.2f}")
        print(f"  Revenue: Rs. {details['revenue']:.2f}")
        print("-----------------------------")
        print()
    
    print(f"Total Tonnes from all crops: {revenue_data['total_tonnes']:.2f} tonnes")
    print(f"Total Revenue from all crops: Rs. {revenue_data['total_revenue']:.2f}")
    print(f"Revenue from Chemical-Free Farming after 11 months: Rs. {revenue_data['chemical_free_revenue']:.2f}")

# Main block to execute the program
if __name__ == "__main__":
    revenue_data = compute_revenue()
    print_revenue_report(revenue_data)
