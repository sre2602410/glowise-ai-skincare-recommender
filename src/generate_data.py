import pandas as pd

data = [
    {
        "product_name": "Ultra Hydrating Gel",
        "brand": "AquaGlow",
        "ingredients": "Water, Glycerin, Hyaluronic Acid, Aloe Vera, Phenoxyethanol",
        "skin_type": "Dry, Normal",
        "concern": "Hydration, Dryness",
        "sensitive_skin_safe": True
    },
    {
        "product_name": "Salicylic Acid Cleanser",
        "brand": "ClearSkin",
        "ingredients": "Water, Sodium Laureth Sulfate, Salicylic Acid, Cocamidopropyl Betaine, Glycerin",
        "skin_type": "Oily, Combination",
        "concern": "Acne, Pores",
        "sensitive_skin_safe": False
    },
    {
        "product_name": "Niacinamide 10% Serum",
        "brand": "BrightenUp",
        "ingredients": "Water, Niacinamide, Zinc PCA, Pentylene Glycol, Xanthan Gum",
        "skin_type": "All",
        "concern": "Brightening, Acne, Oil Control",
        "sensitive_skin_safe": True
    },
    {
        "product_name": "Retinol Night Cream",
        "brand": "YouthRenew",
        "ingredients": "Water, Caprylic/Capric Triglyceride, Retinol, Glycerin, Cetearyl Alcohol, Stearic Acid",
        "skin_type": "Dry, Normal",
        "concern": "Aging, Fine Lines",
        "sensitive_skin_safe": False
    },
    {
        "product_name": "Mineral Sunscreen SPF 50",
        "brand": "SunShield",
        "ingredients": "Zinc Oxide, Titanium Dioxide, Water, Cyclopentasiloxane, Dimethicone",
        "skin_type": "All, Sensitive",
        "concern": "Sun Protection, Sensitivity",
        "sensitive_skin_safe": True
    },
    {
        "product_name": "Vitamin C Serum",
        "brand": "GlowBoost",
        "ingredients": "Water, Ascorbic Acid, Ethoxydiglycol, Ferulic Acid, Panthenol",
        "skin_type": "All",
        "concern": "Brightening, Dark Spots",
        "sensitive_skin_safe": False
    },
    {
        "product_name": "Centella Soothing Cream",
        "brand": "CalmCare",
        "ingredients": "Water, Centella Asiatica Extract, Glycerin, Squalane, Madecassoside",
        "skin_type": "Sensitive, Dry",
        "concern": "Sensitivity, Redness",
        "sensitive_skin_safe": True
    },
    {
        "product_name": "Glycolic Acid Toner",
        "brand": "Exfoli8",
        "ingredients": "Water, Glycolic Acid, Arginine, Aloe Barbadensis Leaf Juice, Propanediol",
        "skin_type": "Oily, Normal",
        "concern": "Texture, Brightening",
        "sensitive_skin_safe": False
    },
    {
        "product_name": "Ceramide Barrier Balm",
        "brand": "BarrierFix",
        "ingredients": "Water, Ceramide NP, Ceramide AP, Ceramide EOP, Cholesterol, Phytosphingosine",
        "skin_type": "Dry, Sensitive",
        "concern": "Barrier Repair, Dryness",
        "sensitive_skin_safe": True
    },
    {
        "product_name": "Benzoyl Peroxide Spot Treatment",
        "brand": "AcneStop",
        "ingredients": "Water, Benzoyl Peroxide, Glycerin, Carbomer, Sodium Hydroxide",
        "skin_type": "Oily",
        "concern": "Acne",
        "sensitive_skin_safe": False
    }
]

df = pd.DataFrame(data)
df.to_csv("data/skincare_products.csv", index=False)
print("Dataset created successfully at data/skincare_products.csv")
