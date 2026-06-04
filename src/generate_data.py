import pandas as pd

data = [
    # CLEANSERS
    {
        "product_name": "Gentle Skin Cleanser",
        "brand": "Cetaphil",
        "ingredients": "Water, Glycerin, Cetearyl Alcohol, Panthenol, Niacinamide, Pantolactone",
        "skin_type": "Dry, Sensitive, Normal",
        "concern": "Hydration, Sensitivity",
        "category": "Cleanser",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.8
    },
    {
        "product_name": "Foaming Facial Cleanser",
        "brand": "CeraVe",
        "ingredients": "Water, Cocamidopropyl Hydroxysultaine, Glycerin, Sodium Lauroyl Sarcosinate, Niacinamide, Ceramide NP, Ceramide AP, Ceramide EOP",
        "skin_type": "Oily, Combination",
        "concern": "Oiliness, Acne",
        "category": "Cleanser",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.7
    },
    {
        "product_name": "Squalane Cleanser",
        "brand": "The Ordinary",
        "ingredients": "Squalane, Aqua, Coco-Caprylate/Caprate, Glycerin",
        "skin_type": "All",
        "concern": "Hydration, Texture",
        "category": "Cleanser",
        "usage": "PM",
        "sensitive_skin_safe": True,
        "rating": 4.6
    },
    {
        "product_name": "Acne Facial Cleanser",
        "brand": "Mario Badescu",
        "ingredients": "Water, Glycerin, Sodium Laureth Sulfate, Salicylic Acid, Aloe Barbadensis Leaf Juice",
        "skin_type": "Oily, Combination",
        "concern": "Acne, Oiliness",
        "category": "Cleanser",
        "usage": "Both",
        "sensitive_skin_safe": False,
        "rating": 4.2
    },
    # TONERS
    {
        "product_name": "Glycolic Acid 7% Toning Solution",
        "brand": "The Ordinary",
        "ingredients": "Water, Glycolic Acid, Aloe Barbadensis Leaf Water, Ginseng Root Extract",
        "skin_type": "Normal, Oily, Combination",
        "concern": "Texture, Brightening",
        "category": "Toner",
        "usage": "PM",
        "sensitive_skin_safe": False,
        "rating": 4.5
    },
    {
        "product_name": "Supple Preparation Unscented Toner",
        "brand": "Klairs",
        "ingredients": "Water, Butylene Glycol, Dimethyl Sulfone, Betaine, Caprylic/Capric Triglyceride, Natto Gum, Sodium Hyaluronate",
        "skin_type": "Sensitive, Dry, All",
        "concern": "Hydration, Sensitivity",
        "category": "Toner",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.9
    },
    {
        "product_name": "BHA Liquid Exfoliant",
        "brand": "Paula's Choice",
        "ingredients": "Water, Methylpropanediol, Salicylic Acid, Polysorbate 20, Green Tea Extract",
        "skin_type": "Oily, Combination",
        "concern": "Pores, Acne, Texture",
        "category": "Toner",
        "usage": "Both",
        "sensitive_skin_safe": False,
        "rating": 4.9
    },
    {
        "product_name": "Rice Toner",
        "brand": "I'm From",
        "ingredients": "Rice Extract, Methylpropanediol, Niacinamide, Portulaca Oleracea Extract",
        "skin_type": "Dry, Normal",
        "concern": "Brightening, Hydration",
        "category": "Toner",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.8
    },
    # MOISTURIZERS
    {
        "product_name": "Hydro Boost Water Gel",
        "brand": "Neutrogena",
        "ingredients": "Water, Dimethicone, Glycerin, Sodium Hyaluronate",
        "skin_type": "Oily, Combination, Normal",
        "concern": "Hydration, Dryness",
        "category": "Moisturizer",
        "usage": "AM",
        "sensitive_skin_safe": True,
        "rating": 4.6
    },
    {
        "product_name": "CeraVe Moisturizing Cream",
        "brand": "CeraVe",
        "ingredients": "Water, Glycerin, Cetearyl Alcohol, Ceramide NP, Ceramide AP, Ceramide EOP, Hyaluronic Acid",
        "skin_type": "Dry, Normal",
        "concern": "Hydration, Barrier Repair",
        "category": "Moisturizer",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.9
    },
    {
        "product_name": "Toleriane Double Repair",
        "brand": "La Roche-Posay",
        "ingredients": "Water, Glycerin, Dimethicone, Niacinamide, Ceramide NP",
        "skin_type": "Sensitive, All",
        "concern": "Sensitivity, Redness, Barrier Repair",
        "category": "Moisturizer",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.8
    },
    {
        "product_name": "Revitalift Night Cream",
        "brand": "L'Oreal",
        "ingredients": "Water, Glycerin, Niacinamide, Retinyl Palmitate",
        "skin_type": "Normal, Dry",
        "concern": "Aging, Wrinkles",
        "category": "Moisturizer",
        "usage": "PM",
        "sensitive_skin_safe": False,
        "rating": 4.1
    },
    # SERUMS (Adding some for routine richness)
    {
        "product_name": "Vitamin C 15% Super Serum",
        "brand": "Paula's Choice",
        "ingredients": "Water, Ascorbic Acid, Ferulic Acid, Tocopherol",
        "skin_type": "All",
        "concern": "Brightening, Dark Spots",
        "category": "Serum",
        "usage": "AM",
        "sensitive_skin_safe": False,
        "rating": 4.6
    },
    {
        "product_name": "Retinol 0.5% in Squalane",
        "brand": "The Ordinary",
        "ingredients": "Squalane, Retinol, Solanum Lycopersicum Fruit Extract",
        "skin_type": "Dry, Normal",
        "concern": "Aging, Fine Lines",
        "category": "Serum",
        "usage": "PM",
        "sensitive_skin_safe": False,
        "rating": 4.4
    },
    {
        "product_name": "Hyaluronic Acid 2% + B5",
        "brand": "The Ordinary",
        "ingredients": "Water, Sodium Hyaluronate, Panthenol",
        "skin_type": "All",
        "concern": "Hydration, Dryness",
        "category": "Serum",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.8
    },
    {
        "product_name": "Advanced Night Repair",
        "brand": "Estée Lauder",
        "ingredients": "Water, Bifida Ferment Lysate, Tripeptide-32, Sodium Hyaluronate",
        "skin_type": "All",
        "concern": "Aging, Hydration",
        "category": "Serum",
        "usage": "PM",
        "sensitive_skin_safe": True,
        "rating": 4.8
    },
    {
        "product_name": "Centella Unscented Serum",
        "brand": "Purito",
        "ingredients": "Centella Asiatica Extract, Niacinamide, Sodium Hyaluronate, Peptides",
        "skin_type": "Sensitive, All",
        "concern": "Sensitivity, Redness",
        "category": "Serum",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.7
    },
    {
        "product_name": "Niacinamide 10% + Zinc 1%",
        "brand": "The Ordinary",
        "ingredients": "Water, Niacinamide, Zinc PCA",
        "skin_type": "Oily, Combination",
        "concern": "Brightening, Oiliness, Pores",
        "category": "Serum",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.7
    },
    # SUNSCREEN
    {
        "product_name": "Ultra Sheer Dry-Touch SPF 55",
        "brand": "Neutrogena",
        "ingredients": "Avobenzone, Homosalate, Octisalate, Octocrylene, Oxybenzone",
        "skin_type": "All",
        "concern": "Aging, Brightening",
        "category": "Sunscreen",
        "usage": "AM",
        "sensitive_skin_safe": False,
        "rating": 4.5
    },
    {
        "product_name": "Unseen Sunscreen SPF 40",
        "brand": "Supergoop!",
        "ingredients": "Water, Dimethicone, Avobenzone, Homosalate, Octisalate",
        "skin_type": "Oily, Combination, Normal",
        "concern": "Pores, Texture",
        "category": "Sunscreen",
        "usage": "AM",
        "sensitive_skin_safe": True,
        "rating": 4.7
    },
    {
        "product_name": "Anthelios Melt-In Milk SPF 60",
        "brand": "La Roche-Posay",
        "ingredients": "Water, Avobenzone, Homosalate, Octisalate, Glycerin, Niacinamide",
        "skin_type": "Sensitive, Dry, All",
        "concern": "Sensitivity, Aging",
        "category": "Sunscreen",
        "usage": "AM",
        "sensitive_skin_safe": True,
        "rating": 4.8
    },
    # EYE CREAM
    {
        "product_name": "Caffeine Solution 5% + EGCG",
        "brand": "The Ordinary",
        "ingredients": "Water, Caffeine, Epigallocatechin Gallatyl Glucoside",
        "skin_type": "All",
        "concern": "Aging, Brightening",
        "category": "Eye cream",
        "usage": "PM",
        "sensitive_skin_safe": True,
        "rating": 4.3
    },
    {
        "product_name": "Potent-C Eye Serum",
        "brand": "Peter Thomas Roth",
        "ingredients": "Water, Tetrahexyldecyl Ascorbate, Hyaluronic Acid, Peptides",
        "skin_type": "Normal, Dry",
        "concern": "Aging, Brightening",
        "category": "Eye cream",
        "usage": "PM",
        "sensitive_skin_safe": False,
        "rating": 4.4
    },
    {
        "product_name": "Eye Repair Cream",
        "brand": "CeraVe",
        "ingredients": "Water, Ceramide NP, Hyaluronic Acid, Niacinamide, Peptides",
        "skin_type": "Sensitive, Dry, All",
        "concern": "Hydration, Aging",
        "category": "Eye cream",
        "usage": "PM",
        "sensitive_skin_safe": True,
        "rating": 4.6
    },
    # ADDITIONAL TREATMENTS
    {
        "product_name": "Azelaic Acid Suspension 10%",
        "brand": "The Ordinary",
        "ingredients": "Azelaic Acid, Dimethicone, Polysilicone-11",
        "skin_type": "Oily, Combination, Sensitive",
        "concern": "Acne, Brightening, Texture",
        "category": "Treatment",
        "usage": "PM",
        "sensitive_skin_safe": True,
        "rating": 4.5
    },
    {
        "product_name": "Good Genes Lactic Acid Treatment",
        "brand": "Sunday Riley",
        "ingredients": "Water, Lactic Acid, Licorice Extract, Lemongrass",
        "skin_type": "Normal, Dry, Combination",
        "concern": "Texture, Brightening, Aging",
        "category": "Treatment",
        "usage": "PM",
        "sensitive_skin_safe": False,
        "rating": 4.6
    },
    {
        "product_name": "Alpha Arbutin 2% + HA",
        "brand": "The Ordinary",
        "ingredients": "Water, Alpha-Arbutin, Sodium Hyaluronate",
        "skin_type": "All",
        "concern": "Brightening, Dark Spots",
        "category": "Treatment",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.6
    },
    {
        "product_name": "Snail 96 Mucin Power Essence",
        "brand": "COSRX",
        "ingredients": "Snail Secretion Filtrate, Betaine, Sodium Hyaluronate, Panthenol",
        "skin_type": "Dry, Sensitive, Normal",
        "concern": "Hydration, Texture",
        "category": "Treatment",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.8
    },
    {
        "product_name": "Discoloration Defense Serum",
        "brand": "SkinCeuticals",
        "ingredients": "Water, Niacinamide, Tranexamic Acid, Kojic Acid, HEPES",
        "skin_type": "All",
        "concern": "Brightening, Aging",
        "category": "Treatment",
        "usage": "AM",
        "sensitive_skin_safe": True,
        "rating": 4.7
    },
    # EXTRA CLEANSERS & MOISTURIZERS
    {
        "product_name": "Hydrating Facial Cleanser",
        "brand": "CeraVe",
        "ingredients": "Water, Glycerin, Ceramide NP, Hyaluronic Acid, Niacinamide",
        "skin_type": "Dry, Sensitive, Normal",
        "concern": "Hydration, Sensitivity",
        "category": "Cleanser",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.8
    },
    {
        "product_name": "Ultra Facial Cream",
        "brand": "Kiehl's",
        "ingredients": "Water, Squalane, Glycerin, Glacial Glycoprotein",
        "skin_type": "Dry, Normal",
        "concern": "Hydration, Texture",
        "category": "Moisturizer",
        "usage": "Both",
        "sensitive_skin_safe": True,
        "rating": 4.7
    },
    {
        "product_name": "Oil-Free Moisture SPF 15",
        "brand": "Neutrogena",
        "ingredients": "Water, Glycerin, Dimethicone, Avobenzone, Octinoxate",
        "skin_type": "Oily, Combination",
        "concern": "Hydration, Acne",
        "category": "Moisturizer",
        "usage": "AM",
        "sensitive_skin_safe": True,
        "rating": 4.4
    },
]

df = pd.DataFrame(data)
df.to_csv("data/skincare_products.csv", index=False)
print(f"Enriched dataset created with {len(data)} products across CTM categories.")
