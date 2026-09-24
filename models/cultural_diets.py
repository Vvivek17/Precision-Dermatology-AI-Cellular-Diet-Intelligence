"""
DermAI 360 - Global Cultural Nutrition Matrix
Provides authentic 3-meal splits (Breakfast, Lunch, Dinner) + Traditional Hydration
tailored to the user's country and cultural cuisine, with dietary preference filters
(Omnivore vs Vegetarian), circadian nutrient timing, and local ingredient substitutions.
"""

from models.diet_content_translations import (
    translate_dish_title, translate_ingredients, translate_action,
    translate_hydration_item, translate_substitutions_list,
    CONDITION_PREFIX_TRANSLATIONS, DISH_SUFFIX_TRANSLATIONS,
    BASE_DISH_TRANSLATIONS, INGREDIENT_TRANSLATIONS,
    CELLULAR_TARGET_TRANSLATIONS, HYDRATION_TRANSLATIONS,
    SUBSTITUTION_TRANSLATIONS
)

SUPPORTED_COUNTRIES = [
    {
        "id": "india",
        "name": "India / South Asian",
        "flag": "🇮🇳",
        "region": "South Asia",
        "culinary_focus": "Ayurvedic therapeutic spices, turmeric, lentils, seasonal gourds, millets, probiotic dahi"
    },
    {
        "id": "mediterranean",
        "name": "Mediterranean / Southern Europe",
        "flag": "🇬🇷",
        "region": "Southern Europe",
        "culinary_focus": "Extra virgin olive oil, wild seafood, tomatoes, capers, legumes, leafy greens, citrus"
    },
    {
        "id": "east_asia",
        "name": "East Asia (Japan/Korea/China)",
        "flag": "🇯🇵",
        "region": "East Asia",
        "culinary_focus": "Miso, matcha, shiitake/maitake, kimchi, seaweed/wakame, steamed fish, organic tofu"
    },
    {
        "id": "western",
        "name": "Western / North American",
        "flag": "🇺🇸",
        "region": "North America",
        "culinary_focus": "Chia puddings, wild salmon, sprouted oats, quinoa, broccoli sprouts, sweet potatoes"
    },
    {
        "id": "middle_east",
        "name": "Middle Eastern / Levantine",
        "flag": "🇱🇧",
        "region": "Middle East",
        "culinary_focus": "Tahini, za'atar, pomegranate molasses, walnuts, high-apigenin parsley tabbouleh, lentils"
    },
    {
        "id": "latin_america",
        "name": "Latin American",
        "flag": "🇲🇽",
        "region": "Latin America",
        "culinary_focus": "Black beans, nopales (cactus), avocado, pepitas (zinc), ceviche, lime, pure cacao"
    }
]

SUPPORTED_LANGUAGES = [
    {"code": "en", "name": "English", "native": "English", "flag": "🇬🇧"},
    {"code": "hi", "name": "Hindi", "native": "हिंदी", "flag": "🇮🇳"},
    {"code": "ta", "name": "Tamil", "native": "தமிழ்", "flag": "🇮🇳"},
    {"code": "te", "name": "Telugu", "native": "తెలుగు", "flag": "🇮🇳"},
    {"code": "bn", "name": "Bengali", "native": "বাংলা", "flag": "🇮🇳"},
    {"code": "mr", "name": "Marathi", "native": "मराठी", "flag": "🇮🇳"},
    {"code": "es", "name": "Spanish", "native": "Español", "flag": "🇪🇸"},
    {"code": "ar", "name": "Arabic", "native": "العربية", "flag": "🇸🇦"},
    {"code": "kn", "name": "Kannada", "native": "ಕನ್ನಡ", "flag": "🇮🇳"}
]

# ─────────────────────────────────────────────────────────────
# Cultural Diets Database (7 Conditions × 6 Countries × 2 Tracks)
# ─────────────────────────────────────────────────────────────

CULTURAL_DIETS = {
    # ── 1. MELANOMA (mel) ──────────────────────────────────
    "mel": {
        "india": {
            "non_veg": {
                "label": "Non-Vegetarian (Non-Veg) Track",
                "protein_type": "Fresh Seafood, Desi Poultry & Egg Whites",
                "breakfast": {
                    "title": "Sprouted Moong & Vegetable Cheela with 2 Boiled Egg Whites & Mint-Amla Chutney",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Soaked sprouted moong dal, 2 pasture-raised boiled egg whites (high albumin & zinc for cellular matrix repair), ginger, cumin, grated carrots, fresh coriander, fresh Amla (Indian gooseberry) shot",
                    "action": "Delivers mega-doses of bioavailable Vitamin C, clean protein albumin, and plant polyphenols to prime morning cellular repair without glucose spikes."
                },
                "lunch": {
                    "title": "Pan-Seared Indian Bangda (Mackerel) / Rohu Fish Curry with Brown Rice & Steamed Palak",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Fresh Bangda fish or Rohu (rich in marine Astaxanthin and Omega-3 EPA/DHA), curry leaves, cold-pressed mustard oil, turmeric, steamed palak (spinach), brown rice, and probiotic homemade dahi (curd)",
                    "action": "Synergy of marine carotenoids, curcuminoids, and live probiotics cultivating a gut microbiome that boosts anti-tumor T-lymphocyte cytotoxicity."
                },
                "dinner": {
                    "title": "Desi Chicken & Turmeric Moong Stew with Jowar Roti (or Mutton Bone Broth)",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Pasture-raised desi chicken breast or slow-simmered bone broth (rich in glycine & proline for extracellular dermal matrix rebuilding), yellow moong dal, fresh grated turmeric, cracked black pepper (piperine), roasted ridge gourd (torai), 1 jowar (sorghum) roti",
                    "action": "Supplies bioavailable collagen amino acids with piperine-enhanced curcumin that downregulates photoinflammatory cascades and initiates nocturnal autophagy."
                },
                "hydration": {
                    "title": "Warm Tulsi (Holy Basil) & Fresh Ginger Infusion",
                    "timing": "Throughout morning & afternoon",
                    "ingredients": "Fresh holy basil leaves, crushed ginger root, warm spring water",
                    "action": "Eugenol and adaptogenic flavonoids shield cutaneous cellular membranes from oxidative degradation."
                },
                "grocery_list": {
                    "Produce": ["Fresh Amla (Gooseberry)", "Spinach (Palak)", "Ridge Gourd (Torai)", "Fresh Turmeric & Ginger", "Coriander & Curry leaves"],
                    "Non-Veg & Proteins": ["Fresh Bangda/Mackerel or Rohu Fish", "Pasture-Raised Desi Chicken", "Organic Country Eggs (Egg Whites)", "Probiotic Dahi (Curd)"],
                    "Pantry": ["Jowar (Sorghum) flour", "Brown basmati rice", "Black pepper", "Cold-pressed mustard oil"]
                },
                "local_substitutions": [
                    "Swap expensive imported Alaskan Salmon with local Bangda (Indian Mackerel) or Rohu/Hilsa — exceptional natural source of Omega-3 EPA/DHA.",
                    "Include slow-simmered bone broth (Paya/Chicken soup) 2–3 times weekly to flood skin tissue with bioavailable collagen peptides (glycine, proline).",
                    "Add 2 boiled egg whites at breakfast for 12g of clean albumin and zinc without inflammatory saturated fats.",
                    "Swap imported acai/blueberries with fresh Amla (Gooseberry), containing up to 20x the Vitamin C of citrus."
                ]
            },
            "vegetarian": {
                "breakfast": {
                    "title": "Sprouted Moong & Ragi Cheela with Raw Walnut Chutney",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Sprouted moong dal, ragi flour, raw walnuts, fresh coconut, green chilies, Amla juice",
                    "action": "Plant-based ALA omega-3s, ellagic acid, and amino acids to sustain steady cellular repair."
                },
                "lunch": {
                    "title": "Sprouted Kala Chana (Black Chickpea) Masala with Steamed Spinach & Curd",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Black chickpeas simmered with roasted cumin, tomatoes, ginger, and turmeric; steamed spinach; brown basmati rice; fresh probiotic curd (dahi)",
                    "action": "Prebiotic prebiotic galacto-oligosaccharides combined with curcumin cultivate gut Ruminococcaceae for immune surveillance."
                },
                "dinner": {
                    "title": "Panchmel Dal (5-Lentil Stew) with Methi (Fenugreek) Roti & Bottle Gourd",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Moong, masoor, toor, urad and chana dal with turmeric; cooked bottle gourd (lauki); 1 bajra/methi roti",
                    "action": "Complete plant amino acid profile with fenugreek compounds that stimulate nighttime cellular clearance."
                },
                "hydration": {
                    "title": "Spiced Buttermilk (Chaas) with Roasted Cumin & Curry Leaves",
                    "timing": "Mid-afternoon (03:30 PM)",
                    "ingredients": "Fresh homemade curd churned with water, toasted cumin, fresh ginger, rock salt, and chopped cilantro",
                    "action": "Restores electrolyte balance and colonizes the gut with beneficial lactobacilli strains."
                },
                "grocery_list": {
                    "Produce": ["Amla", "Palak (Spinach)", "Lauki (Bottle Gourd)", "Fresh Ginger & Green Chilies", "Methi leaves"],
                    "Proteins": ["Kala Chana (Black chickpeas)", "Green Moong Dal", "Probiotic Dahi (Curd)", "Raw Walnuts"],
                    "Pantry": ["Ragi flour", "Bajra flour", "Brown rice", "Whole spices (cumin, mustard, turmeric)"]
                },
                "local_substitutions": [
                    "Combine soaked raw Walnuts + ground Flaxseeds (Alsi) for comprehensive plant-based Omega-3 ALA.",
                    "Use fresh homemade Dahi (Curd) daily to replicate the probiotic benefits of imported kefir or sauerkraut."
                ]
            }
        },

        "mediterranean": {
            "omnivore": {
                "breakfast": {
                    "title": "Avocado & Wild Sardine Bruschetta on Sprouted Sourdough",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Sprouted rye/sourdough, mashed Hass avocado, wild Mediterranean sardines, sliced cherry tomatoes, extra virgin olive oil, oregano",
                    "action": "Delivers rich marine Astaxanthin, lycopene, and monounsaturated squalene to bolster cell membrane integrity."
                },
                "lunch": {
                    "title": "Grilled Wild Sea Bass (Lavraki) over Puy Lentils & Greek Village Salad",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Grilled Mediterranean sea bass, simmered brown lentils, capers, kalamata olives, cucumbers, red onions, EVOO and lemon juice",
                    "action": "Lentil prebiotic fiber combined with high-polyphenol olive oil (oleocanthal) downregulates oncogenic inflammatory cascades."
                },
                "dinner": {
                    "title": "Rosemary Garlic Chicken Breast with Braised Green Beans (Fasolakia)",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Free-range chicken breast, fresh rosemary, braised string beans in crushed tomato-garlic sauce, small farro side",
                    "action": "Carnosic acid from rosemary acts in synergy with bioflavonoids to support overnight oxidative detoxification."
                },
                "hydration": {
                    "title": "Steeped Greek Mountain Tea (Sideritis) with Fresh Lemon",
                    "timing": "Morning and afternoon",
                    "ingredients": "Dried Sideritis herbs, hot water, fresh lemon slice",
                    "action": "Diterpenes and flavonoids provide potent free-radical scavenging capacity across dermal capillaries."
                },
                "grocery_list": {
                    "Produce": ["Heirloom Tomatoes", "Fresh Rosemary & Oregano", "Lemons", "Cucumbers", "Garlic"],
                    "Proteins": ["Wild Sardines", "Sea Bass / Branzino", "Free-range chicken breast", "Brown lentils"],
                    "Pantry": ["Extra Virgin Olive Oil (cold-pressed)", "Kalamata olives", "Farro / Spelt", "Capers"]
                },
                "local_substitutions": [
                    "Use fresh Greek oregano and rosemary freely — their rosmarinic acid content inhibits cutaneous lipid peroxidation."
                ]
            },
            "vegetarian": {
                "breakfast": {
                    "title": "Greek Sheep Yogurt Bowl with Walnuts, Blackberries & Chia",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Authentic Greek yogurt, crushed raw walnuts, organic blackberries, 1 tbsp chia seeds, drizzle of raw thyme honey",
                    "action": "Probiotic cultures paired with anthocyanins suppress systemic cytokine release and nourish beneficial microflora."
                },
                "lunch": {
                    "title": "Gigantes Plaki (Baked Giant White Beans with Tomato & Dill)",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Giant white fava/butter beans baked with stewed tomatoes, garlic, extra virgin olive oil, fresh dill, served with steamed dandelion greens (horta)",
                    "action": "High-fiber prebiotic fuel for short-chain fatty acid (butyrate) production and cellular immunonutrition."
                },
                "dinner": {
                    "title": "Briam (Roasted Eggplant, Zucchini & Peppers) with Chickpea Mash",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Layered eggplant, zucchini, red bell peppers, and garlic roasted in EVOO; served with rosemary-chickpea puree",
                    "action": "Abundant carotenoids, apigenin, and resistant starch assisting restorative tissue autophagy."
                },
                "hydration": {
                    "title": "Chilled Hibiscus & Lemon Verbena Herbal Infusion",
                    "timing": "Between meals",
                    "ingredients": "Dried hibiscus flowers, lemon verbena leaves, cold spring water",
                    "action": "Delivers anthocyanins and organic fruit acids that protect cutaneous capillary walls."
                },
                "grocery_list": {
                    "Produce": ["Eggplant & Zucchini", "Red Bell Peppers", "Dandelion Greens (Horta)", "Fresh Dill & Garlic"],
                    "Proteins": ["Greek Sheep Yogurt", "Giant White Beans (Gigantes)", "Chickpeas", "Raw Walnuts"],
                    "Pantry": ["First cold-pressed Extra Virgin Olive Oil", "Chia seeds", "Raw thyme honey"]
                },
                "local_substitutions": [
                    "Steamed wild dandelion greens (horta) provide up to 5x the lutein and beta-carotene of standard lettuce."
                ]
            }
        },

        "east_asia": {
            "omnivore": {
                "breakfast": {
                    "title": "Warm Brown Rice Okayu (Porridge) with Silken Tofu & Ceremonial Matcha",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Simmered brown rice porridge, silken organic tofu, grated fresh ginger, scallions, nori seaweed flakes, bowl of whisked ceremonial matcha",
                    "action": "EGCG catechins from matcha and fucoidan from nori provide instant morning cellular free-radical neutralizers."
                },
                "lunch": {
                    "title": "Grilled Sockeye Salmon with Kimchi, Edamame & Wakame Miso Soup",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Wild salmon fillet (astaxanthin rich), steamed purple rice, organic edamame, authentic unpasteurized cabbage kimchi, miso soup with wakame seaweed",
                    "action": "Lactic acid bacteria in raw kimchi paired with marine astaxanthin dramatically elevates anti-tumor immune response."
                },
                "dinner": {
                    "title": "Steamed Sea Bream with Shiitake-Maitake Medley & Baby Bok Choy",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Fresh sea bream, fresh shiitake and maitake mushrooms, baby bok choy, ginger-tamari reduction, sesame oil",
                    "action": "Beta-glucans from medicinal mushrooms stimulate natural killer (NK) cells and macrophage phagocytosis."
                },
                "hydration": {
                    "title": "Genmaicha (Roasted Brown Rice Green Tea)",
                    "timing": "Throughout the day",
                    "ingredients": "Japanese green tea blended with roasted whole brown rice",
                    "action": "Sustained low-caffeine polyphenols supporting cellular mitochondrial protection."
                },
                "grocery_list": {
                    "Produce": ["Fresh Shiitake & Maitake", "Baby Bok Choy", "Fresh Ginger & Scallions", "Cabbage Kimchi (raw)"],
                    "Proteins": ["Wild Salmon / Sea Bream", "Organic Silken Tofu", "Organic Edamame"],
                    "Pantry": ["Fermented Miso paste", "Wakame & Nori Seaweed", "Brown/Purple Rice", "Ceremonial Matcha"]
                },
                "local_substitutions": [
                    "Use traditional fermented unpasteurized Miso and Kimchi daily to maximize gut microbiome diversity.",
                    "Combine Shiitake and Maitake mushrooms in soups for therapeutic beta-glucan immune stimulation."
                ]
            },
            "vegetarian": {
                "breakfast": {
                    "title": "Silken Tofu Hiyayakko with Ginger, Scallions & Nori + Matcha Bowl",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Chilled organic silken tofu, grated fresh ginger root, finely sliced scallions, toasted nori strips, splash of tamari, whisked matcha",
                    "action": "Soy isoflavones (genistein) and matcha EGCG act together to inhibit cellular abnormal angiogenesis."
                },
                "lunch": {
                    "title": "Sautéed Organic Tempeh Bowl with Raw Kimchi & Shiitake Dashi",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Marinated fermented tempeh cubes, purple rice, steamed edamame, raw probiotic kimchi, rich shiitake-kombu broth",
                    "action": "Fermented tempeh and kimchi replenish gut microbiome taxa linked to superior clinical outcomes."
                },
                "dinner": {
                    "title": "Braised King Oyster Mushrooms with Lotus Root & Steamed Gai Lan",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Sliced king oyster mushrooms, lotus root, Chinese broccoli (gai lan), garlic, sesame seeds, ginger tamari sauce",
                    "action": "Inulin-rich lotus root feeds colonic bifidobacteria; cruciferous gai lan delivers indole-3-carbinol."
                },
                "hydration": {
                    "title": "Burdock Root (Gobo) & Reishi Mushroom Infusion",
                    "timing": "Afternoon",
                    "ingredients": "Dried burdock root slices, red reishi mushroom, steeped in simmering water",
                    "action": "Arctigenin in burdock root suppresses inflammatory cytokines and stimulates liver phase II enzymes."
                },
                "grocery_list": {
                    "Produce": ["King Oyster & Shiitake Mushrooms", "Lotus Root", "Gai Lan (Chinese Broccoli)", "Burdock Root (Gobo)"],
                    "Proteins": ["Organic Tempeh", "Organic Silken & Firm Tofu", "Edamame"],
                    "Pantry": ["Fermented White/Red Miso", "Kombu Seaweed", "Nori Sheets", "Ceremonial Matcha"]
                },
                "local_substitutions": [
                    "Fermented Tempeh provides complete bioavailable amino acids and is easier to digest than unfermented soy."
                ]
            }
        },

        "western": {
            "omnivore": {
                "breakfast": {
                    "title": "Anti-Inflammatory Golden Turmeric Chia Bowl with Wild Berries",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Organic chia seeds soaked in unsweetened coconut milk, grated fresh turmeric, black pepper, topped with raspberries and pumpkin seeds",
                    "action": "High omega-3 ALA and curcuminergic synergy downregulates morning inflammatory prostaglandins."
                },
                "lunch": {
                    "title": "Wild Sockeye Salmon over Massaged Kale with Raw Sauerkraut & Quinoa",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Grilled Alaskan sockeye salmon, massaged lacinato kale, organic raw sauerkraut, steamed quinoa, roasted artichoke hearts, EVOO",
                    "action": "Astaxanthin, sulforaphane, and live Lactobacillus combine for targeted immunonutrition."
                },
                "dinner": {
                    "title": "Herb-Roasted Organic Chicken with Asparagus & Purple Sweet Potato",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Pasture-raised herb chicken breast, steamed asparagus spears (inulin prebiotic), baked purple sweet potato with olive oil",
                    "action": "Inulin fibers nurture colonic butyrate production while anthocyanins from purple sweet potatoes quench free radicals."
                },
                "hydration": {
                    "title": "Elderberry & Hibiscus Iced Tea with Fresh Lemon",
                    "timing": "Throughout the day",
                    "ingredients": "Organic dried elderberries, hibiscus tea, fresh lemon slices, filtered water",
                    "action": "High-potency anthocyanins and Vitamin C protect dermal microcapillaries."
                },
                "grocery_list": {
                    "Produce": ["Lacinato Kale", "Asparagus", "Purple Sweet Potatoes", "Fresh Turmeric Root", "Fresh Raspberries"],
                    "Proteins": ["Wild Alaskan Sockeye Salmon", "Pasture-Raised Chicken Breast", "Raw Sauerkraut (refrigerated)"],
                    "Pantry": ["Organic Chia Seeds", "Raw Pumpkin Seeds", "Quinoa", "Unsweetened Coconut Milk"]
                },
                "local_substitutions": [
                    "Always select wild-caught Alaskan sockeye or coho salmon over farm-raised for 400% higher astaxanthin content."
                ]
            },
            "vegetarian": {
                "breakfast": {
                    "title": "Sprouted Steel-Cut Oats with Blueberries, Flax & Walnuts",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Sprouted steel-cut oatmeal, fresh wild blueberries, 1 tbsp ground flaxseeds, raw chopped walnuts, Ceylon cinnamon",
                    "action": "Beta-glucan fibers support digestive health; ellagic acid and anthocyanins protect cell DNA."
                },
                "lunch": {
                    "title": "Sprouted Black Bean & Quinoa Bowl with Raw Sauerkraut & Avocado",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Simmered sprouted black beans, tricolor quinoa, raw unpasteurized sauerkraut, sliced Hass avocado, pumpkin seed dressing",
                    "action": "Prebiotic plant fiber cultivating gut microbes that enhance cellular immunotherapy responsiveness."
                },
                "dinner": {
                    "title": "Stuffed Baked Portobello Caps with Lentils, Walnuts & Asparagus",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Large portobello mushroom caps stuffed with brown lentils, crushed walnuts, and herbs; served with steamed asparagus spears",
                    "action": "Lentil protein and mushroom ergothioneine provide deep cellular antioxidant protection."
                },
                "hydration": {
                    "title": "Chilled Hibiscus & Fresh Mint Tea",
                    "timing": "Between meals",
                    "ingredients": "Steeped hibiscus flowers, fresh garden mint, filtered water",
                    "action": "Polyphenols reducing cutaneous vascular hyperpermeability."
                },
                "grocery_list": {
                    "Produce": ["Portobello Mushrooms", "Asparagus", "Wild Blueberries", "Avocado", "Fresh Mint"],
                    "Proteins": ["Sprouted Black Beans", "Brown Lentils", "Raw Sauerkraut", "Raw Walnuts & Pumpkin Seeds"],
                    "Pantry": ["Sprouted Steel-Cut Oats", "Flaxseed Meal", "Quinoa", "Ceylon Cinnamon"]
                },
                "local_substitutions": [
                    "Use sprouted oats and beans to eliminate phytates and maximize micronutrient absorption."
                ]
            }
        },

        "middle_east": {
            "omnivore": {
                "breakfast": {
                    "title": "Pasture-Egg Shakshuka with Fresh Flat-Leaf Parsley & EVOO",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Two pasture eggs poached in spiced stewed tomatoes, garlic, bell peppers, topped with generous flat-leaf parsley and olive oil",
                    "action": "Lycopene, lutein, and high apigenin from flat-leaf parsley arrest abnormal melanocytic growth pathways."
                },
                "lunch": {
                    "title": "Grilled Chicken Shish Taouk with Tabbouleh & Sprouted Lentil Mjaddara",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Garlic-lemon marinated chicken skewers, traditional Lebanese tabbouleh (80% parsley, mint, tomatoes, olive oil), brown lentil & onion mjaddara",
                    "action": "Massive apigenin and prebiotic lentil dose supporting immune surveillance and suppression of VEGF."
                },
                "dinner": {
                    "title": "Samke Harra (Baked White Fish with Spiced Tahini & Walnuts)",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Baked white fish fillet topped with raw sesame tahini, crushed garlic, chopped walnuts, sumac, and pomegranate seeds",
                    "action": "Sesamin and ellagic acid (from pomegranate) suppress NF-kB and stimulate nighttime cellular DNA repair."
                },
                "hydration": {
                    "title": "Fresh Spearmint & Green Tea Infusion",
                    "timing": "Throughout the day",
                    "ingredients": "Fresh garden spearmint leaves, green tea, steeped in hot water (no refined sugar)",
                    "action": "Rosemarinic acid and EGCG reduce systemic cutaneous photooxidative damage."
                },
                "grocery_list": {
                    "Produce": ["Flat-Leaf Parsley (large bunch)", "Pomegranate", "Heirloom Tomatoes", "Fresh Mint & Garlic", "Lemons"],
                    "Proteins": ["Pasture Eggs", "Free-Range Chicken", "Wild White Fish", "Brown Lentils"],
                    "Pantry": ["Raw Sesame Tahini", "Walnuts", "Sumac & Za'atar", "Extra Virgin Olive Oil"]
                },
                "local_substitutions": [
                    "Traditional Lebanese Tabbouleh is 80% parsley — an exceptional natural source of Apigenin."
                ]
            },
            "vegetarian": {
                "breakfast": {
                    "title": "Foul Mudammas (Slow-Simmered Fava Beans with Cumin, Garlic & EVOO)",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Fava beans simmered with ground cumin, minced garlic, lemon juice, diced tomatoes, generous cold-pressed EVOO, cucumber spears",
                    "action": "High-fiber fava bean polyphenols and prebiotic resistant starch providing steady morning cellular fuel."
                },
                "lunch": {
                    "title": "Sprouted Lentil Mjaddara with Tabbouleh & Cucumber-Mint Laban",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Brown lentils simmered with caramelized onions and whole farro/brown rice; large serving of flat-leaf parsley tabbouleh; probiotic laban (yogurt)",
                    "action": "Complete amino acid profile combined with live probiotic yogurt and apigenin-rich parsley."
                },
                "dinner": {
                    "title": "Baked Stuffed Eggplant (Sheikh El Mahshi) with Chickpeas & Tahini",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Roasted eggplants filled with chickpeas, tomatoes, pine nuts, garlic, and za'atar; drizzled with raw sesame tahini and pomegranate molasses",
                    "action": "Anthocyanins from eggplant skin and sesamin from tahini promote nighttime tissue autophagy."
                },
                "hydration": {
                    "title": "Cinnamon Bark & Steeped Mint Herbal Tea",
                    "timing": "Evening",
                    "ingredients": "Whole Ceylon cinnamon stick, fresh mint leaves, hot water",
                    "action": "Stabilizes overnight insulin levels and aids cellular repair."
                },
                "grocery_list": {
                    "Produce": ["Eggplants", "Fresh Flat-Leaf Parsley", "Cucumbers & Tomatoes", "Fresh Mint", "Pomegranates"],
                    "Proteins": ["Fava Beans (Foul)", "Brown Lentils", "Chickpeas", "Probiotic Laban / Yogurt"],
                    "Pantry": ["Raw Sesame Tahini", "Pine Nuts", "Ceylon Cinnamon Sticks", "Cold-Pressed EVOO"]
                },
                "local_substitutions": [
                    "Always use pure raw sesame Tahini (100% ground sesame) for maximum lignan and zinc delivery."
                ]
            }
        },

        "latin_america": {
            "omnivore": {
                "breakfast": {
                    "title": "Huevos a la Mexicana with Black Bean Puree & Sliced Avocado",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Pasture eggs scrambled with diced tomatoes, onions, cilantro, and mild green chiles; served with stewed black beans and 1/2 Hass avocado",
                    "action": "Lycopene, choline, and monounsaturated lipids form resilient cellular membranes against photo-damage."
                },
                "lunch": {
                    "title": "Wild Snapper Ceviche with Citrus, Red Onion, Avocado & Pepitas",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Fresh wild snapper cured in raw lime juice, diced red onion, avocado, chopped cilantro, toasted pumpkin seeds (pepitas), jicama sticks",
                    "action": "Raw citrus bioflavonoids, zinc-rich pepitas, and clean marine peptides for deep cellular repair."
                },
                "dinner": {
                    "title": "Grilled Sea Bass with Sautéed Nopales (Cactus) & Stewed Black Beans",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Grilled wild sea bass, tender sautéed nopales (prickly pear cactus paddles), stewed black beans, warm corn tortilla",
                    "action": "Nopales contain unique pectin and betalain antioxidants shown to stabilize blood glucose and scavenge singlet oxygen."
                },
                "hydration": {
                    "title": "Agua de Jamaica (Unsweetened Hibiscus & Lime Infusion)",
                    "timing": "Throughout the day",
                    "ingredients": "Steeped hibiscus flower calyces, fresh lime juice, chilled spring water (no refined sugar)",
                    "action": "High-potency anthocyanins protect vascular endothelium and enhance renal elimination of toxins."
                },
                "grocery_list": {
                    "Produce": ["Nopales (Cactus paddles)", "Hass Avocados", "Fresh Limes & Cilantro", "Jicama", "Tomatoes"],
                    "Proteins": ["Wild Snapper / Sea Bass", "Pasture Eggs", "Black Beans (Frijoles Negros)", "Raw Pepitas (Pumpkin seeds)"],
                    "Pantry": ["Dried Hibiscus Flowers (Flor de Jamaica)", "Corn Tortillas", "Cold-Pressed Avocado Oil"]
                },
                "local_substitutions": [
                    "Nopales (cactus paddles) are a Latin American superfood with unique betalains that lower oxidative stress.",
                    "Drink unsweetened Flor de Jamaica daily for maximum anthocyanin and bioflavonoid intake."
                ]
            },
            "vegetarian": {
                "breakfast": {
                    "title": "Warm Quinoa & Chia Porridge with Raw Cacao, Papaya & Pepitas",
                    "timing": "08:00 AM – 08:30 AM",
                    "ingredients": "Cooked quinoa and chia seeds, pure unsweetened raw cacao powder, diced fresh papaya (papain enzymes), roasted pumpkin seeds, Ceylon cinnamon",
                    "action": "Cacao flavanols double the skin's minimal erythema dose; papain aids digestive protein breakdown."
                },
                "lunch": {
                    "title": "Nopales & Black Bean Fiesta Bowl with Guacamole & Pico de Gallo",
                    "timing": "12:30 PM – 01:30 PM",
                    "ingredients": "Tender grilled nopales, seasoned black beans, fresh guacamole, pico de gallo, toasted pepitas, and shredded purple cabbage",
                    "action": "High prebiotic fiber from black beans combined with cactus betalains boosts gut-mediated immune responses."
                },
                "dinner": {
                    "title": "Stuffed Roasted Poblano Pepper with Lentils, Quinoa & Avocado",
                    "timing": "06:30 PM – 07:30 PM",
                    "ingredients": "Mild roasted poblano pepper stuffed with seasoned brown lentils, quinoa, diced tomatoes, and cilantro; topped with fresh avocado crema",
                    "action": "Mild capsaicin and quercetin in poblanos support microcirculation without excessive vasodilation."
                },
                "hydration": {
                    "title": "Agua de Jamaica con Canela (Hibiscus & Cinnamon Tea)",
                    "timing": "Between meals",
                    "ingredients": "Hibiscus flowers steeped with a Mexican cinnamon stick, served chilled with lime",
                    "action": "Inhibits advanced glycation end-products and protects cutaneous collagen networks."
                },
                "grocery_list": {
                    "Produce": ["Nopales (Prickly pear cactus)", "Poblano Peppers", "Fresh Papaya", "Hass Avocados", "Purple Cabbage"],
                    "Proteins": ["Black Beans", "Brown Lentils", "Raw Pepitas (Pumpkin Seeds)"],
                    "Pantry": ["100% Pure Raw Cacao Powder", "Dried Hibiscus Flowers (Flor de Jamaica)", "Quinoa", "Mexican Cinnamon"]
                },
                "local_substitutions": [
                    "Use pure raw 100% Mexican cacao for powerful epicatechin flavanols that protect skin cells from UV damage."
                ]
            }
        }
    }
}

# ─────────────────────────────────────────────────────────────
# Automatically ensure both 'non_veg' and 'omnivore' keys exist
# ─────────────────────────────────────────────────────────────
for _cond, _countries in CULTURAL_DIETS.items():
    if isinstance(_countries, dict):
        for _cid, _tracks in _countries.items():
            if isinstance(_tracks, dict):
                if "non_veg" in _tracks and "omnivore" not in _tracks:
                    _tracks["omnivore"] = _tracks["non_veg"]
                elif "omnivore" in _tracks and "non_veg" not in _tracks:
                    _tracks["non_veg"] = _tracks["omnivore"]

# ─────────────────────────────────────────────────────────────
# Translated Culinary Focus for 6 Regions in 9 Languages
# ─────────────────────────────────────────────────────────────

CULINARY_FOCUS_TRANSLATIONS = {
    "india": {
        "en": "Ayurvedic therapeutic spices, turmeric, lentils, seasonal gourds, millets, probiotic dahi",
        "kn": "ಆಯುರ್ವೇದ ಚಿಕಿತ್ಸಕ ಮಸಾಲೆಗಳು, ಅರಿಶಿನ, ಬೇಳೆಕಾಳುಗಳು, ಸಿರಿಧಾನ್ಯಗಳು ಮತ್ತು ಪ್ರೊಬಯಾಟಿಕ್ ಮೊಸರು",
        "hi": "आयुर्वेदिक औषधीय मसाले, हल्दी, दालें, मौसमी लौकी/सब्जियां, बाजरा/ज्वार और प्रोबायोटिक दही",
        "ta": "ஆயுர்வேத மருத்துவ மசாலாக்கள், மஞ்சள், பருப்பு வகைகள், சிறுதானியங்கள் மற்றும் தயிர்",
        "te": "ఆయుర్వేద ఔషధ మసాలాలు, పసుపు, పప్పుధాన్యాలు, చిరుధాನ್ಯాలు మరియు ప్రోబయోటిక్ పెరుగు",
        "bn": "আয়ুর্বেদিক ভেষজ মশলা, হলুদ, ডাল, মরসুমি সবজি, বাজরা ও প্রোবায়োটিক দই",
        "mr": "आयुर्वेदिक औषधी मसाले, हळद, डाळी, ज्वारी/बाजरी आणि प्रोबायोटिक ताक/दही",
        "es": "Especias ayurvédicas terapéuticas, cúrcuma, lentejas, mijo y yogur probiótico",
        "ar": "توابل أيورفيدية علاجية، كركم، عدس، دخن، قرع موسمي وزبادي بروبيوتيك"
    },
    "mediterranean": {
        "en": "Extra virgin olive oil, wild seafood, tomatoes, capers, legumes, leafy greens, citrus",
        "kn": "ವರ್ಜಿನ್ ಆಲಿವ್ ಎಣ್ಣೆ, ಸಮುದ್ರ ಮೀನು, ಟೊಮೆಟೊ, ಹಸಿರು ಸೊಪ್ಪು ಮತ್ತು ಸಿಟ್ರಸ್ ಹಣ್ಣುಗಳು",
        "hi": "एक्स्ट्रा वर्जिन जैतून का तेल, समुद्री मछली, टमाटर, फलियां, हरी पत्तेदार सब्जियां और खट्टे फल",
        "ta": "ஆலிவ் எண்ணெய், கடல் மீன், தக்காளி, பருப்பு வகைகள், கீரைகள் மற்றும் சிட்ரஸ் பழங்கள்",
        "te": "ఆలివ్ నూనె, సముద్రపు చేపలు, టమాటాలు, పప్పుధాన్యాలు, ఆకుకూరలు మరియు సిట్రస్ పండ్లు",
        "bn": "অলিভ অয়েল, সামুদ্রিক মাছ, টমেটো, ডাল, সবুজ শাকসবজি এবং সাইট্রাস ফল",
        "mr": "ऑलिव्ह ऑईल, सागरी मासे, टोमॅटो, शेंगा, हिरव्या पालेभाज्या आणि लिंबूवर्गीय फळे",
        "es": "Aceite de oliva virgen extra, mariscos silvestres, tomates, alcaparras, legumbres, verduras y cítricos",
        "ar": "زيت زيتون بكر ممتاز، مأكولات بحرية برية، طماطم، بقوليات، خضار ورقية وحمضيات"
    },
    "east_asia": {
        "en": "Miso, matcha, shiitake/maitake, kimchi, seaweed/wakame, steamed fish, organic tofu",
        "kn": "ಮಿಸೊ, ಗ್ರೀನ್ ಟೀ ಮಚ್ಚಾ, ಶೀಟೇಕ್ ಅಣಬೆ, ಕಿಮ್ಚಿ, ಸಮುದ್ರ ಪಾಚಿ, ಆವಿಯಲ್ಲಿ ಬೇಯಿಸಿದ ಮೀನು ಮತ್ತು ತೋಫು",
        "hi": "मिसो, माचा ग्रीन टी, शिटाके मशरूम, किमची, समुद्री शैवाल, उबली मछली और जैविक टोफू",
        "ta": "மிசோ, மட்சா கிரீன் டீ, காளான், கிம்ச்சி, கடற்பாசி, அவித்த மீன் மற்றும் டோஃபு",
        "te": "మిసో, మచ్చా గ్రీన్ టీ, పుట్టగొడుగులు, కిమ్చి, ఆవిరి చేప మరియు సేంద్రీయ టోఫు",
        "bn": "মিসো, মাচা গ্রিন টি, মাশরুম, কিমচি, সামুদ্রিক শৈবাল ও ভাপানো মাছ",
        "mr": "मिसो, माचा ग्रीन टी, मशरूम, किमची, उकडलेले मासे आणि टोफू",
        "es": "Miso, té verde matcha, hongos shiitake, kimchi, algas wakame, pescado al vapor y tofu",
        "ar": "ميسو، شاي ماتشا، فطر شيتاكي، كيمتشي، أعشاب بحرية، سمك مطهو على البخار وتوفو"
    },
    "western": {
        "en": "Chia puddings, wild salmon, sprouted oats, quinoa, broccoli sprouts, sweet potatoes",
        "kn": "ಚಿಯಾ ಬೀಜಗಳು, ಸಾಲ್ಮನ್ ಮೀನು, ಮೊಳಕೆಯೊಡೆದ ಓಟ್ಸ್, ಕ್ವಿನೋವಾ, ಬ್ರೊಕೊಲಿ ಮೊಳಕೆ ಮತ್ತು ಸಿಹಿಗೆಣಸು",
        "hi": "चिया सीड्स, सैल्मन मछली, अंकुरित ओट्स, क्विनोआ, ब्रोकली स्प्राउट्स और शकरकंद",
        "ta": "சியா விதைகள், சால்மன் மீன், ஓட்ஸ், குயினோவா, ப்ரோக்கோலி முளைகள் மற்றும் சர்க்கரைவள்ளிக்கிழங்கு",
        "te": "చియా గింజలు, సాల్మన్ చేప, మొలకెత్తిన ఓట్స్, క్వినోవా, బ్రోకలీ మొలకలు మరియు చిలగడదుంపలు",
        "bn": "চিয়া বীজ, স্যামন মাছ, ওটস, কুইনোয়া, ব্রকলি স্প্রাউটস ও মিষ্টি আলু",
        "mr": "चिया बिया, सॅल्मन मासा, ओट्स, क्विनोआ, ब्रोकोली स्प्राउट्स आणि रताळे",
        "es": "Pudines de chía, salmón salvaje, avena germinada, quinua, brotes de brócoli y batatas",
        "ar": "بودينغ الشيا، سمك السلمون البري، شوفان مستنبت، كينوا، براعم البروكلي وبطاطا حلوة"
    },
    "middle_east": {
        "en": "Tahini, za'atar, pomegranate molasses, walnuts, high-apigenin parsley tabbouleh, lentils",
        "kn": "ತಹಿನಿ, ಜಾಟರ್, ದಾಳಿಂಬೆ ರಸ, ವಾಲ್‌ನಟ್ಸ್, ಕೊತ್ತಂಬರಿ-ಪಾರ್ಸ್ಲಿ ತಬ್ಬೌಲೆಹ್ ಮತ್ತು ಮಸೂರ ಬೇಳೆ",
        "hi": "ताहिनी, जातर, अनार का शीरा, अखरोट, अजमोद/धनिया तबूलेज और मसूर दाल",
        "ta": "தஹினி, ஜாதார், மாதுளை, அக்ரூட் பருப்புகள், வோக்கோசு தபூலே மற்றும் பருப்பு",
        "te": "తహిని, జాటర్, దానిమ్మ, వాల్‌నట్స్, పార్స్లీ తబూలే మరియు పప్పుధాన్యాలు",
        "bn": "তহিনী, ডালিম, আখরোট, পার্সলে সালাদ এবং মসুর ডাল",
        "mr": "ताहिनी, जातर, डाळिंब, अक्रोड, कोथिंबीर/पार्सली आणि मसूर डाळ",
        "es": "Tahini, zaatar, melaza de granada, nueces, tabulé de perejil rico en apigenina y lentejas",
        "ar": "طحينة، زعتر، دبس رمان، جوز، تبولة بقدونس غنية بالأبيجينين وعدس"
    },
    "latin_america": {
        "en": "Black beans, nopales (cactus), avocado, pepitas (zinc), ceviche, lime, pure cacao",
        "kn": "ಕಪ್ಪು ಬೀನ್ಸ್, ಕ್ಯಾಕ್ಟಸ್, ಆವಕಾಡೊ, ಕುಂಬಳಕಾಯಿ ಬೀಜಗಳು (ಸತು), ನಿಂಬೆ ರಸ ಮತ್ತು ಶುದ್ಧ ಕೋಕೋ",
        "hi": "काली फलियां, कैक्टस (नोपल्स), एवोकैडो, कद्दू के बीज (जिंक), नींबू और शुद्ध कोको",
        "ta": "கருப்பு பீன்ஸ், கற்றாழை, வெண்ணெய் பழம், பூசணி விதைகள், எலுமிச்சை மற்றும் கோகோ",
        "te": "బ్లాక్ బీన్స్, కాక్టస్, అవోకాడో, గుమ్మడికాయ గింజలు (జింక్), నిమ్మ మరియు స్వచ్ఛమైన కోకో",
        "bn": "কালো মটরশুটি, ক্যাকটাস, অ্যাভোকাডো, কুমড়ার বীজ, লেবু ও খাঁটি কোকো",
        "mr": "काळी सोयाबीन/बीन्स, कॅक्टस, अ‍ॅव्होकॅडो, भोपळ्याच्या बिया (झिंक), लिंबू आणि शुद्ध कोको",
        "es": "Frijoles negros, nopales, aguacate, pepitas de calabaza (zinc), ceviche, lima y cacao puro",
        "ar": "فاصوليا سوداء، صبار، أفوكادو، بذور القرع (زنك)، سيفيتشي، ليمون وكاكاو نقي"
    }
}

# ─────────────────────────────────────────────────────────────
# Translated Diet Philosophy & Clinical Rationale (7 Conditions × 9 Languages)
# ─────────────────────────────────────────────────────────────

CONDITION_DIET_DESCRIPTIONS = {
    "akiec": {
        "en": {
            "philosophy": "High-Antioxidant & DNA Photoprotection Protocol",
            "rationale": "Focuses on nutrients that accelerate nucleotide excision DNA repair, quench reactive singlet oxygen species induced by solar radiation, and dampen cutaneous inflammatory prostaglandins."
        },
        "kn": {
            "philosophy": "ಹೆಚ್ಚಿನ ಆ್ಯಂಟಿಆಕ್ಸಿಡೆಂಟ್ ಮತ್ತು ಡಿಎನ್‌ಎ ಫೋಟೊಪ್ರೊಟೆಕ್ಷನ್ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ಸೂರ್ಯನ ಯುವಿ ಕಿರಣಗಳಿಂದ ಹಾನಿಗೊಳಗಾದ ಡಿಎನ್‌ಎ ದುರಸ್ತಿಯನ್ನು ವೇಗಗೊಳಿಸುವ, ಆಕ್ಸಿಡೇಟಿವ್ ಒತ್ತಡವನ್ನು ತಗ್ಗಿಸುವ ಮತ್ತು ಚರ್ಮದ ಉರಿಯೂತವನ್ನು ನಿಯಂತ್ರಿಸುವ ಪೋಷಕಾಂಶಗಳ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "उच्च-एंटीऑक्सीडेंट एवं डीएनए फोटोप्रोटेक्शन प्रोटोकॉल",
            "rationale": "यह आहार डीएनए रिपेयर को तेज करने, सौर विकिरण से उत्पन्न हानिकारक फ्री रेडिकल्स को शांत करने और त्वचा की सूजन को कम करने वाले पोषक तत्वों पर केंद्रित है।"
        },
        "ta": {
            "philosophy": "அதிநவீன ஆன்டி-ஆக்ஸிடன்ட் & டிஎன்ஏ சூரிய ஒளி பாதுகாப்பு நெறிமுறை",
            "rationale": "சூரிய கதிர்வீச்சால் ஏற்படும் டிஎன்ஏ பாதிப்பை சரிசெய்யும், நச்சு ஆக்ஸிஜனேற்றத்தை எதிர்க்கும் மற்றும் தோல் அழற்சியைக் குறைக்கும் ஊட்டச்சத்துக்களை வழங்குகிறது."
        },
        "te": {
            "philosophy": "హై-యాంటీఆక్సిడెంట్ & డిఎన్‌ఏ ఫోటోప్రొటెక్షన్ ప్రోటోకాల్",
            "rationale": "సూర్యరశ్మి వల్ల దెబ్బతిన్న డిఎన్‌ఏ కణాల మరమ్మత్తును వేగవంతం చేసే, ఆక్సీకరణ ఒత్తిడిని తగ్గించే మరియు చర్మ వాపును నివారించే పోషకాలను అందిస్తుంది."
        },
        "bn": {
            "philosophy": "উচ্চ-অ্যান্টিঅক্সিডেন্ট এবং ডিএনএ সুরক্ষামূলক পুষ্টি পদ্ধতি",
            "rationale": "সূর্যের অতিবেগুনি রশ্মির ক্ষতি থেকে ডিএনএ মেরামত ত্বরান্বিত করে এবং ত্বকের প্রদাহ কমাতে প্রয়োজনীয় অ্যান্টিঅক্সিডেন্ট সরবরাহ করে।"
        },
        "mr": {
            "philosophy": "उच्च-अँटिऑक्सिडंट आणि डीएनए संरक्षण प्रोटोकॉल",
            "rationale": "सौर किरणांमुळे झालेल्या डीएनए हानीची दुरुस्ती जलद गतीने करण्यासाठी आणि त्वचेची जळजळ व सूज कमी करण्यासाठी विशेष पोषक घटक पुरवते."
        },
        "es": {
            "philosophy": "Protocolo de Alta Protección Antioxidante y Fotoprotección del ADN",
            "rationale": "Se enfoca en nutrientes que aceleran la reparación del ADN por escisión de nucleótidos, neutralizan radicales libres del sol y reducen la inflamación dérmica."
        },
        "ar": {
            "philosophy": "بروتوكول مضادات الأكسدة الفائقة والحماية الضوئية للحمض النووي",
            "rationale": "يركز على المغذيات التي تسرع ترميم الحمض النووي التالف من الأشعة فوق البنفسجية وتخفف الالتهابات الجلدية."
        }
    },
    "bcc": {
        "en": {
            "philosophy": "Anti-Tumorigenic Epigenetic Defense & Angiogenesis Suppression",
            "rationale": "Supplies bioactive phytocompounds that suppress Sonic Hedgehog over-signaling, downregulate matrix metalloproteinases (MMPs), and inhibit the abnormal capillary angiogenesis that feeds basaloid tumor nests."
        },
        "kn": {
            "philosophy": "ಆಂಟಿ-ಟ್ಯೂಮರ್ ಎಪಿಜೆನೆಟಿಕ್ ರಕ್ಷಣೆ ಮತ್ತು ಆಂಜಿಯೋಜೆನೆಸಿಸ್ ತಡೆಗಟ್ಟುವಿಕೆ",
            "rationale": "ಅಸಹಜ ಕೋಶಗಳ ಬೆಳವಣಿಗೆಯ ಸಂಕೇತಗಳನ್ನು ತಡೆಯುವ, ಅಸಹಜ ರಕ್ತನಾಳಗಳ ರಚನೆಯನ್ನು ನಿಗ್ರಹಿಸುವ ಮತ್ತು ಹಾನಿಗೊಳಗಾದ ಕೋಶಗಳ ನೈಸರ್ಗಿಕ ನಿರ್ಮೂಲನೆಯನ್ನು ಪ್ರಚೋದಿಸುವ ಪೋಷಕಾಂಶಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "ट्यूमर-रोधी एपिजेनेटिक रक्षा एवं एंजियोजेनेसिस शमन प्रोटोकॉल",
            "rationale": "असामान्य बेसल कोशिकाओं के अनियंत्रित विकास को रोकता है, ट्यूमर को पोषण देने वाली नई रक्त वाहिकाओं के गठन को बाधित करता है और विषहरण एंजाइमों को सक्रिय करता है।"
        },
        "ta": {
            "philosophy": "கட்டி எதிர்ப்பு எபிஜெனெடிக் பாதுகாப்பு நெறிமுறை",
            "rationale": "வழக்கத்திற்கு மாறான உயிரணு பெருக்கத்தைத் தடுத்து, அசாதாரண ரத்த நாளங்கள் உருவாவதை கட்டுப்படுத்தி நச்சுநீக்கத்தை ஊக்குவிக்கிறது."
        },
        "te": {
            "philosophy": "యాంటీ-ట్యూమర్ ఎపిజెనెటిక్ రక్షణ & రక్తనాళాల అసాధారణ పెరుగుదల నిరోధక ప్రోటోకాల్",
            "rationale": "కణితి పెరుగుదలను నిరోధించే, అసాధారణ రక్తనాళాల అభివృద్ధిని తగ్గించే మరియు నిర్విషీకరణ ఎంజైమ్‌లను పెంచే ఫైటోన్యూట్రియెంట్లను అందిస్తుంది."
        },
        "bn": {
            "philosophy": "টিউমার প্রতিরোধী এপিজেনেটিক সুরক্ষা এবং নিরাময় পদ্ধতি",
            "rationale": "অস্বাভাবিক কোষের বিস্তার নিয়ন্ত্রণ করে এবং টিউমার কোষের পুষ্টি জোগানো রক্তনালী বৃদ্ধি রোধ করে।"
        },
        "mr": {
            "philosophy": "ट्यूमर-विरोधी एपिजेनेटिक संरक्षण आणि पेशी संतुलन प्रोटोकॉल",
            "rationale": "असामान्य पेशींची वाढ रोखण्यासाठी, रक्तवाहिन्यांचे अवांछित जाळे तयार होण्यापासून रोखण्यासाठी आणि शरीरातील डिटॉक्स प्रणाली मजबूत करण्यासाठी कार्य करते."
        },
        "es": {
            "philosophy": "Defensa Epigenética Antitumoral y Supresión de la Angiogénesis",
            "rationale": "Inhibe las vías aberrantes de proliferación celular, suprime la formación de vasos que nutren lesiones basales y estimula enzimas desintoxicantes."
        },
        "ar": {
            "philosophy": "الدفاع اللاجيني المضاد للأورام وتثبيط التوعي غير الطبيعي",
            "rationale": "يثبط الإشارات غير الطبيعية لنمو الخلايا القاعدية ويحد من تكوين الأوعية الدموية المغذية للأورام."
        }
    },
    "bkl": {
        "en": {
            "philosophy": "Keratin Metabolic Balance & Glycemic Stabilization Protocol",
            "rationale": "High insulin levels and insulin resistance stimulate epidermal keratinocyte proliferation via IGF-1 receptors. Stabilizing blood sugar, promoting healthy keratin turnover, and supplying barrier lipids maintain smooth skin texture."
        },
        "kn": {
            "philosophy": "ಕೆರಾಟಿನ್ ಚಯಾಪಚಯ ಸಮತೋಲನ ಮತ್ತು ಗ್ಲೈಸೆಮಿಕ್ ನಿಯಂತ್ರಣ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ರಕ್ತದಲ್ಲಿನ ಇನ್ಸುಲಿನ್ ಏರಿಕೆಯನ್ನು ನಿಯಂತ್ರಿಸಿ ಚರ್ಮದ ಹೊರಪದರದ ಅತಿಯಾದ ದಪ್ಪಗಾಗುವಿಕೆಯನ್ನು ತಡೆಯುತ್ತದೆ ಮತ್ತು ಚರ್ಮವನ್ನು ಮೃದುವಾಗಿರಿಸಲು ತಡೆಗೋಡೆ ಲಿಪಿಡ್‌ಗಳನ್ನು ಪೋಷಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "केराटिन चयापचय संतुलन एवं रक्त शर्करा स्थिरता प्रोटोकॉल",
            "rationale": "भोजन के बाद इंसुलिन के स्तर को स्थिर रखता है ताकि केराटिनोसाइट्स का अत्यधिक जमाव न हो, और त्वचा की कोमल बनावट व लिपिड अवरोध बना रहे।"
        },
        "ta": {
            "philosophy": "கெரட்டின் வளர்சிதை மாற்ற சமநிலை & ரத்த சர்க்கரை சீராக்கல் நெறிமுறை",
            "rationale": "இன்சுலின் அளவை சீராக வைத்து தோல் தடிமனாவதைத் தடுத்து, சருமத்தின் மென்மை மற்றும் ஈரப்பத தடையை பாதுகாக்கிறது."
        },
        "te": {
            "philosophy": "కెరాటిన్ జీవక్రియ సమతుల్యత & రక్తంలో గ్లూకోజ్ స్థిరీకరణ ప్రోటోకాల్",
            "rationale": "రక్తంలో ఇన్సులిన్ పెరుగుదలను నియంత్రించడం ద్వారా చర్మం గరుకుగా మారడాన్ని నిరోధిస్తుంది మరియు మృదువైన చర్మ అవరోధాన్ని కాపాడుతుంది."
        },
        "bn": {
            "philosophy": "কেরাটিন বিপাকীয় ভারসাম্য ও রক্তে শর্করা নিয়ন্ত্রণ পদ্ধতি",
            "rationale": "ইনসুলিনের মাত্রা নিয়ন্ত্রণে রেখে ত্বকের অত্যধিক পুরু হওয়া রোধ করে এবং মসৃণ উজ্জ্বল ত্বক বজায় রাখে।"
        },
        "mr": {
            "philosophy": "केराटिन चयापचय संतुलन आणि रक्तातील साखर नियंत्रण प्रोटोकॉल",
            "rationale": "इन्सुलिनच्या पातळीत होणारे अचानक चढउतार थांबवून त्वचेचा खडबडीतपणा कमी करते आणि त्वचेचे नैसर्गिक आवरण निरोगी ठेवते."
        },
        "es": {
            "philosophy": "Equilibrio Metabólico de Queratina y Estabilización Glucémica",
            "rationale": "Estabiliza los picos de insulina posprandiales que estimulan la hiperqueratosis, promoviendo una descamación fisiológica suave y barrera lipídica sana."
        },
        "ar": {
            "philosophy": "توازن أيض الكيراتين وضبط مستويات السكر في الدم",
            "rationale": "يتحكم في طفرات الإنسولين التي تحفز فرط تقرن الجلد ويدعم تجدد طبقة الكيراتين ونعومة البشرة."
        }
    },
    "df": {
        "en": {
            "philosophy": "Connective Tissue Homeostasis & Collagen Remodeling Protocol",
            "rationale": "Supplies structural amino acids, bioavailable Vitamin C, and copper/zinc metalloenzyme cofactors necessary to maintain orderly extracellular matrix remodeling and prevent aberrant fibrohistiocytic proliferation."
        },
        "kn": {
            "philosophy": "ಸಂಯೋಜಕ ಅಂಗಾಂಶ ಸ್ಥಿರತೆ ಮತ್ತು ಕಾಲಾಜೆನ್ ಪುನರ್ರಚನೆ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ಅತಿಯಾದ ದಟ್ಟವಾದ ಕಾಲಾಜೆನ್ ಶೇಖರಣೆಯನ್ನು ನಿಯಂತ್ರಿಸಲು ಮತ್ತು ಚರ್ಮದ ಒಳಪದರದ ಫೈಬ್ರೋಬ್ಲಾಸ್ಟ್‌ಗಳನ್ನು ಕ್ರಮಬದ್ಧವಾಗಿಡಲು ಅಗತ್ಯವಿರುವ ಅಮೈನೋ ಆಮ್ಲಗಳು ಮತ್ತು ಸೂಕ್ಷ್ಮ ಪೋಷಕಾಂಶಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "संयोजी ऊतक स्थिरता एवं कोलेजन पुनर्निर्माण प्रोटोकॉल",
            "rationale": "अनियमित स्थानीय फाइब्रोसिस को नियंत्रित करने, कोलेजन संश्लेषण को संतुलित करने और त्वचीय ऊतकों की सामान्य मरम्मत के लिए आवश्यक पोषक तत्व प्रदान करता है।"
        },
        "ta": {
            "philosophy": "இணைப்பு திசு சமநிலை மற்றும் கொலாஜன் சீரமைப்பு நெறிமுறை",
            "rationale": "அதிகப்படியான தழும்பு போன்ற கொலாஜன் உருவாவதை சமநிலைப்படுத்தி, திசுக்களின் ஆரோக்கியமான மறுவடிவமைப்பை ஆதரிக்கிறது."
        },
        "te": {
            "philosophy": "కనెక్టివ్ టిష్యూ సమతుల్యత & కొల్లాజెన్ పునర్నిర్మాణ ప్రోటోకాల్",
            "rationale": "అధిక దట్టమైన కొల్లాజెన్ పేరుకుపోవడాన్ని నివారించి, చర్మ అంతర్గత కణజాలం సక్రమంగా పునర్నిర్మితం కావడానికి అవసరమైన పోషకాలను అందిస్తుంది."
        },
        "bn": {
            "philosophy": "সংযোজক টিস্যুর ভারসাম্য এবং কোলাজেন পুনর্গঠন পদ্ধতি",
            "rationale": "অস্বাভাবিক কোলাজেন জমা হওয়া রোধ করে এবং সুস্থ টিস্যু গঠনে সহায়তা করে।"
        },
        "mr": {
            "philosophy": "संयोजी ऊतक संतुलन आणि कोलेजन पुनर्रचना प्रोटोकॉल",
            "rationale": "अनावश्यक फायब्रस गाठी तयार होण्यापासून रोखण्यासाठी आणि त्वचेच्या कोलेजनची योग्य रचना राखण्यासाठी पोषक घटक पुरवते."
        },
        "es": {
            "philosophy": "Homeostasis del Tejido Conectivo y Remodelación de Colágeno",
            "rationale": "Modula la síntesis excesiva de colágeno denso y suministra cofactores esenciales (vitamina C, zinc, prolina) para normalizar la matriz dérmica."
        },
        "ar": {
            "philosophy": "توازن النسيج الضام وإعادة تشكيل الكولاجين الطبيعي",
            "rationale": "ينظم تراكم ألياف الكولاجين الكثيفة ويوفر العوامل المساعدة الأساسية لتجديد النسيج الجلدي الطبيعي."
        }
    },
    "mel": {
        "en": {
            "philosophy": "Immunonutrition, Microbiome Optimization & Oncological Defense",
            "rationale": "Cutting-edge clinical trials published in Science and Nature demonstrate that a high-fiber, polyphenol-dense diet cultivates a specific gut microbiome architecture (Ruminococcaceae, Bifidobacteria) that dramatically enhances anti-PD-1 immunotherapy efficacy and suppresses systemic pro-tumorigenic inflammation."
        },
        "kn": {
            "philosophy": "ಇಮ್ಯುನೊನ್ಯೂಟ್ರಿಷನ್, ಮೈಕ್ರೋಬಯೋಮ್ ಆಪ್ಟಿಮೈಸೇಶನ್ ಮತ್ತು ಆಂಕೊಲಾಜಿಕಲ್ ಡಿಫೆನ್ಸ್",
            "rationale": "ನೈಸರ್ಗಿಕ ರೋಗನಿರೋಧಕ ಕಣಗಳ ಶಕ್ತಿಯನ್ನು ಹೆಚ್ಚಿಸುವ, ಕರುಳಿನ ಪ್ರಯೋಜನಕಾರಿ ಬ್ಯಾಕ್ಟೀರಿಯಾವನ್ನು ಬೆಳೆಸುವ ಮತ್ತು ಡಿಎನ್‌ಎ ಕೋಶಗಳನ್ನು ಅಸಹಜ ಬದಲಾವಣೆಗಳಿಂದ ರಕ್ಷಿಸುವ ಪ್ರಬಲ ಪಾಲಿಫಿನಾಲ್‌ಗಳ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "प्रतिरक्षा पोषण, माइक्रोबायोम संवर्धन एवं ऑन्कोलॉजिकल रक्षा प्रोटोकॉल",
            "rationale": "प्राकृतिक किलर (NK) कोशिकाओं की निगरानी शक्ति को बढ़ाता है, आंत के लाभकारी माइक्रोबायोम को समृद्ध करता है और कैंसर-रोधी कोशिकीय सुरक्षा को सुदृढ़ करता है।"
        },
        "ta": {
            "philosophy": "நோய் எதிர்ப்பு ஊட்டச்சத்து, குடல் நுண்ணுயிர் மேம்பாடு & புற்றுநோய் எதிர்ப்பு நெறிமுறை",
            "rationale": "உடலின் இயற்கையான நோய் எதிர்ப்பு கண்காணிப்பை பலப்படுத்தி, நன்மை பயக்கும் குடல் பாக்டீரியாக்களை வளர்த்து செல்லுலார் பாதுகாப்பை அளிக்கிறது."
        },
        "te": {
            "philosophy": "ఇమ్యునోన్యూట్రిషన్, గట్ మైక్రోబయోమ్ మెరుగుదల & క్యాన్సర్ నిరోధక రక్షణ",
            "rationale": "శరీర సహజ రోగనిరోధక కణాల సామర్థ్యాన్ని పెంచే, ప్రేగులలోని ఆరోగ్యకరమైన బ్యాక్టీరియాను మెరుగుపరిచే మరియు సెల్యులార్ సమగ్రతను రక్షించే పోషకాలను అందిస్తుంది."
        },
        "bn": {
            "philosophy": "অনাক্রম্যতা পুষ্টি, মাইক্রোবায়োম সমৃদ্ধিকরণ এবং অনকোলজিক্যাল প্রতিরক্ষা",
            "rationale": "প্রাকৃতিক রোগ প্রতিরোধ ক্ষমতা বৃদ্ধি করে, অন্ত্রের উপকারী ব্যাকটেরিয়ার ভারসাম্য বজায় রাখে এবং টিউমার-বিরোধী সুরক্ষা জোরদার করে।"
        },
        "mr": {
            "philosophy": "रोगप्रतिकार पोषण, मायक्रोबायोम सुधारणा आणि कर्करोग संरक्षण प्रोटोकॉल",
            "rationale": "शरीराची नैसर्गिक पेशी संरक्षण क्षमता वाढवते, पोटातील चांगल्या जीवाणूंचे प्रमाण सुधारते आणि असामान्य पेशी बदलांविरुद्ध लढा देते."
        },
        "es": {
            "philosophy": "Inmunonutrición, Optimización del Microbioma y Defensa Oncológica",
            "rationale": "Potencia la vigilancia inmunitaria celular antitumoral, enriquece la diversidad del microbioma intestinal y suprime vías pro-inflamatorias oncogénicas."
        },
        "ar": {
            "philosophy": "التغذية المناعية، تحسين ميكروبيوم الأمعاء والدفاع ضد الأورام",
            "rationale": "يعزز مراقبة الخلايا المناعية الطبيعية للأورام، ويثري بكتيريا الأمعاء النافعة ويقمع المسارات الالتهابية المسببة للأورام."
        }
    },
    "nv": {
        "en": {
            "philosophy": "Systemic Photoprotection & DNA Maintenance Protocol",
            "rationale": "Maintains cellular stability and shields senescent melanocyte nests from secondary UV radiation hits that could trigger genomic instability, while nourishing the cutaneous dermal matrix."
        },
        "kn": {
            "philosophy": "ವ್ಯವಸ್ಥಿತ ಫೋಟೊಪ್ರೊಟೆಕ್ಷನ್ ಮತ್ತು ಡಿಎನ್‌ಎ ನಿರ್ವಹಣಾ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ಮೆಲನೊಸೈಟ್ ಕೋಶಗಳನ್ನು ಆಕ್ಸಿಡೇಟಿವ್ ಒತ್ತಡದಿಂದ ರಕ್ಷಿಸುತ್ತದೆ, ಸೂರ್ಯನ ಬೆಳಕಿನಿಂದ ಆಗುವ ಹಾನಿಯನ್ನು ತಡೆಯುತ್ತದೆ ಮತ್ತು ಚರ್ಮದ ನೈಸರ್ಗಿಕ ಸಮತೋಲನವನ್ನು ಕಾಪಾಡುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "प्रणालीगत फोटोप्रोटेक्शन एवं डीएनए रखरखाव प्रोटोकॉल",
            "rationale": "तिल कोशिकाओं (मेलानोसाइट्स) को पराबैंगनी किरणों के ऑक्सीडेटिव तनाव से बचाता है, आनुवंशिक स्थिरता बनाए रखता है और त्वचा के स्वास्थ्य का पोषण करता है।"
        },
        "ta": {
            "philosophy": "சூரிய ஒளி பாதுகாப்பு மற்றும் டிஎன்ஏ பராமரிப்பு நெறிமுறை",
            "rationale": "மச்ச செல்களை ஆக்ஸிஜனேற்ற அழுத்தத்திலிருந்து பாதுகாத்து, சரும செல்களின் மரபணு நிலைத்தன்மையை பராமரிக்கிறது."
        },
        "te": {
            "philosophy": "వ్యవస్థాగత ఫోటోప్రొటెక్షన్ & డిఎన్‌ఏ నిర్వహణ ప్రోటోకాల్",
            "rationale": "పుట్టుమచ్చల కణాలను సూర్యరశ్మి ఆక్సీకరణ ఒత్తిడి నుండి రక్షిస్తుంది మరియు జన్యు స్థిరత్వాన్ని కాపాడుతుంది."
        },
        "bn": {
            "philosophy": "সিস্টেমিক ফটোপ্রোটেকশন এবং ডিএনএ রক্ষণাবেক্ষণ পদ্ধতি",
            "rationale": "তিল সৃষ্টিকারী কোষগুলিকে অক্সিডেটিভ ক্ষতি থেকে রক্ষা করে এবং ত্বকের সুস্থ ভারসাম্য বজায় রাখে।"
        },
        "mr": {
            "philosophy": "सिस्टेमिक सूर्यप्रकाश संरक्षण आणि डीएनए देखभाल प्रोटोकॉल",
            "rationale": "तीळ निर्माण करणाऱ्या मेलॅनोसाइट पेशींचे अतिनील किरणांपासून रक्षण करते आणि त्वचेची पेशीय रचना निरोगी ठेवते."
        },
        "es": {
            "philosophy": "Fotoprotección Sistémica y Mantenimiento Genómico del ADN",
            "rationale": "Protege los nidos de melanocitos del estrés oxidativo inducido por el sol, preservando la estabilidad genética y previniendo transiciones celulares."
        },
        "ar": {
            "philosophy": "الحماية الضوئية الشاملة وصيانة سلامة الحمض النووي",
            "rationale": "يحمي الخلايا الصباغية من الإجهاد التأكسدي الناتج عن الشمس ويحافظ على الاستقرار الجيني للبشرة."
        }
    },
    "vasc": {
        "en": {
            "philosophy": "Endothelial Integrity & Capillary Strengthening Protocol",
            "rationale": "Focuses on bioflavonoids, anthocyanidins, and vascular tone cofactors that strengthen microvascular basement membranes, decrease abnormal capillary permeability, and eliminate vasodilating inflammatory triggers."
        },
        "kn": {
            "philosophy": "ಎಂಡೋಥೀಲಿಯಲ್ ಸಮಗ್ರತೆ ಮತ್ತು ಸೂಕ್ಷ್ಮ ರಕ್ತನಾಳ ಬಲವರ್ಧನೆ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ರಕ್ತನಾಳಗಳ ಗೋಡೆಗಳನ್ನು ಬಲಪಡಿಸಲು, ಸೂಕ್ಷ್ಮ ರಕ್ತನಾಳಗಳು ಒಡೆಯುವುದನ್ನು ಅಥವಾ ಅತಿಯಾಗಿ ಹಿಗ್ಗುವುದನ್ನು ತಡೆಯಲು ಮತ್ತು ರಕ್ತ ಪರಿಚಲನೆಯನ್ನು ಸಮತೋಲನದಲ್ಲಿಡಲು ಬಯೋಫ್ಲೇವನಾಯ್ಡ್‌ಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "एंडोथेलियल अखंडता एवं सूक्ष्म केशिका सुदृढ़ीकरण प्रोटोकॉल",
            "rationale": "जैव-फ्लेवोनोइड्स से भरपूर आहार जो सूक्ष्म रक्त वाहिकाओं की दीवारों को मजबूत करता है, उनकी कमजोरी व फैलाव को रोकता है और संवहनी सूजन को शांत करता है।"
        },
        "ta": {
            "philosophy": "ரத்த நாள ஒருமைப்பாடு & நுண் தந்துகிகள் வலுவூட்டல் நெறிமுறை",
            "rationale": "நுண்ணிய ரத்த நாளங்களின் சுவர்களை வலுப்படுத்தவும், ரத்த நாளங்கள் வெடிப்பதைத் தடுத்து ரத்த ஓட்டத்தை சீராக்கவும் உதவுகிறது."
        },
        "te": {
            "philosophy": "ఎండోథీలియల్ సమగ్రత & సూక్ష్మ రక్తనాళాల బలోపేత ప్రోటోకాల్",
            "rationale": "సూక్ష్మ రక్తనాళాల గోడలను బలోపేతం చేయడానికి, రక్తనాళాలు అసాధారణంగా వ్యాకోచించకుండా నిರೋధించడానికి అవసరమైన బయోఫ్లేవనాయిడ్లను అందిస్తుంది."
        },
        "bn": {
            "philosophy": "রক্তনালীর অখণ্ডতা এবং কৈশিক প্রাচীর শক্তিশালীকরণ পদ্ধতি",
            "rationale": "সূক্ষ্ম রক্তনালীর প্রাচীর মজবুত করে, রক্তনালীর প্রসারণ ও রক্তপাত প্রতিরোধ করে সুস্থ রক্ত সঞ্চালন বজায় রাখে।"
        },
        "mr": {
            "philosophy": "रक्तवाहिन्यांचे आरोग्य आणि सूक्ष्म केशवाहिन्या बळकटीकरण प्रोटोकॉल",
            "rationale": "बारीक रक्तवाहिन्यांची लवचिकता आणि मजबुती वाढवून अवांछित लालसरपणा व रक्तवाहिन्यांचे फुगणे कमी करण्यास मदत करते."
        },
        "es": {
            "philosophy": "Integridad Endotelial y Fortalecimiento de la Pared Capilar",
            "rationale": "Suministra bioflavonoides que refuerzan las membranas basales microvasculares, reducen la permeabilidad capilar y previenen la dilatación vascular."
        },
        "ar": {
            "philosophy": "سلامة بطانة الأوعية الدموية وتقوية الشعيرات الدقيقة",
            "rationale": "يعزز جدران الشعيرات الدموية الدقيقة بالبيوفلافونويد، ويقلل من نفاذية الأوعية الدموية غير الطبيعية والالتهابات."
        }
    },
    "acne": {
        "en": {
            "philosophy": "Sebum Regulation, Low-Glycemic & Follicular Clearance Protocol",
            "rationale": "Focuses on minimizing IGF-1 and androgen receptor stimulation, quenching oxidative lipid peroxidation in sebum, and restoring skin microbiome diversity to eliminate Cutibacterium acnes inflammatory triggers."
        },
        "kn": {
            "philosophy": "ಸೆಬಮ್ ನಿಯಂತ್ರಣ, ಕಡಿಮೆ-ಗ್ಲೈಸೆಮಿಕ್ ಮತ್ತು ರೋಮಕೂಪ ಶುದ್ಧೀಕರಣ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ಇನ್ಸುಲಿನ್ ಮತ್ತು ಆಂಡ್ರೋಜೆನ್ ಪ್ರಚೋದನೆಯನ್ನು ಕಡಿಮೆ ಮಾಡುವ, ಹೆಚ್ಚುವರಿ ಎಣ್ಣೆಯಂಶ (ಸೆಬಮ್) ಶೇಖರಣೆಯನ್ನು ತಡೆಯುವ ಮತ್ತು ಮೊಡವೆ ಉಂಟುಮಾಡುವ ಬ್ಯಾಕ್ಟೀರಿಯಾದ ಉರಿಯೂತವನ್ನು ನಿಗ್ರಹಿಸುವ ಪೋಷಕಾಂಶಗಳ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "सीबम नियंत्रण, कम-ग्लाइसेमिक एवं रोमछिद्र शुद्धि प्रोटोकॉल",
            "rationale": "इंसुलिन और हार्मोनल उतार-चढ़ाव को स्थिर करता है, अतिरिक्त सीबम उत्पादन को रोकता है और मुँहासे पैदा करने वाले बैक्टीरिया की सूजन को शांत करता है।"
        },
        "ta": {
            "philosophy": "எண்ணெய் பசை கட்டுப்பாடு & பருக்கள் தடுப்பு நெறிமுறை",
            "rationale": "அதிகப்படியான சரும எண்ணெயைக் குறைத்து, ஹார்மோன் சமநிலையை பேணி, முகப்பரு அழற்சியை உண்டாக்கும் பாக்டீரியாக்களை கட்டுப்படுத்துகிறது."
        },
        "te": {
            "philosophy": "సీబమ్ నియంత్రణ, తక్కువ గ్లైసిమిక్ & చర్మ రంధ్రాల శుద్ధీకరణ ప్రోటోకాల్",
            "rationale": "అధిక నూనె ఉత్పత్తిని నిరోధిస్తుంది, హార్మోన్ల సమతుల్యతను కాపాడుతుంది మరియు మొటిమల వాపును తగ్గించే పోషకాలను అందిస్తుంది."
        },
        "bn": {
            "philosophy": "সিবাম নিয়ন্ত্রণ এবং ব্রণ নিরাময় পুষ্টি পদ্ধতি",
            "rationale": "ত্বকের অতিরিক্ত তেল উৎপাদন কমায়, হরমোনের ভারসাম্য রক্ষা করে এবং ব্রণ সৃষ্টিকারী ব্যাকটেরিয়ার বিরুদ্ধে লড়াই করে।"
        },
        "mr": {
            "philosophy": "सीबम नियंत्रण आणि मुरुम प्रतिबंधक प्रोटोकॉल",
            "rationale": "त्वचेतील अतिरिक्त तेल कमी करते, रक्तातील साखर स्थिर ठेवते आणि मुरुमांमुळे होणारी सूज व जळजळ शांत करते."
        },
        "es": {
            "philosophy": "Regulación de Sebo, Bajo Índice Glucémico y Limpieza Folicular",
            "rationale": "Minimiza la estimulación del receptor de andrógenos e IGF-1, frena la peroxidación lipídica en el sebo y restaura la microbiota cutánea para erradicar brotes."
        },
        "ar": {
            "philosophy": "تنظيم الإفرازات الدهنية، مؤشر سكري منخفض وتطهير المسام",
            "rationale": "يقلل من تحفيز مستقبلات الأندروجين وهرمون IGF-1، ويمنع أكسدة الدهون الدهنية ويهدئ التهابات حب الشباب."
        }
    },
    "ecz": {
        "en": {
            "philosophy": "Epidermal Barrier Restoration, Ceramide Replenishment & Anti-Pruritic Protocol",
            "rationale": "Supplies essential omega-6 GLA, ceramides, and antihistaminic bioflavonoids to repair defective filaggrin skin barriers, replenish stratum corneum lipids, and calm hyperactive Th2/mast-cell driven itch-scratch cascades."
        },
        "kn": {
            "philosophy": "ಚರ್ಮದ ತಡೆಗೋಡೆ ಪುನರ್ನಿರ್ಮಾಣ, ಸೆರಾಮೈಡ್ ಪೋಷಣೆ ಮತ್ತು ತುರಿಕೆ ನಿವಾರಕ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ಚರ್ಮದ ರಕ್ಷಣಾತ್ಮಕ ಪದರವನ್ನು ಬಲಪಡಿಸಲು ಅಗತ್ಯವಿರುವ ಸೆರಾಮೈಡ್‌ಗಳು, ಒಮೆಗಾ ಕೊಬ್ಬಿನಾಮ್ಲಗಳು ಮತ್ತು ಅಲರ್ಜಿ ತಗ್ಗಿಸುವ ಬಯೋಫ್ಲೇವನಾಯ್ಡ್‌ಗಳನ್ನು ಒದಗಿಸಿ ವಿಪರೀತ ತುರಿಕೆ ಮತ್ತು ಶುಷ್ಕತೆಯನ್ನು ನಿವಾರಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "त्वचा अवरोधक पुनर्निर्माण, सेरामाइड संवर्धन एवं खुजली-रोधी प्रोटोकॉल",
            "rationale": "त्वचा की सुरक्षात्मक परत को मजबूत करता है, सेरामाइड और आवश्यक फैटी एसिड की कमी को पूरा करता है और अत्यधिक खुजली व एलर्जी की सूजन को शांत करता है।"
        },
        "ta": {
            "philosophy": "தோல் தடுப்பு மறுசீரமைப்பு & நமைச்சல் எதிர்ப்பு நெறிமுறை",
            "rationale": "தோலின் ஈரப்பத அடுக்கைப் பாதுகாத்து, கடுமையான வறட்சி மற்றும் நமைச்சலைக் குறைக்கும் அத்தியாவசிய கொழுப்பு அமிலங்களை வழங்குகிறது."
        },
        "te": {
            "philosophy": "చర్మ అవరోధ పునర్నిర్మాణం & దురద నివారణ ప్రోటోకాల్",
            "rationale": "చర్మ రక్షణ పొరను బలపరుస్తుంది, సహజ కొవ్వులను అందిస్తుంది మరియు విపరీతమైన దురద, ఎరుపుదనాన్ని నివారిస్తుంది."
        },
        "bn": {
            "philosophy": "ত্বকের সুরক্ষা প্রাচীর পুনর্গঠন ও চুলকানি নিরাময় পদ্ধতি",
            "rationale": "ত্বকের আর্দ্রতা বজায় রাখে, প্রাকৃতিক লিপিড স্তর মেরামত করে এবং একজিমার তীব্র চুলকানি ও জ্বালা কমায়।"
        },
        "mr": {
            "philosophy": "त्वचेचे नैसर्गिक आवरण संरक्षण आणि खाज प्रतिबंधक प्रोटोकॉल",
            "rationale": "त्वचेचा ओलावा टिकवून ठेवते, नैसर्गिक स्निग्धता पूर्ववत करते आणि तीव्र खाज व लालसरपणा दूर करण्यास मदत करते."
        },
        "es": {
            "philosophy": "Restauración de la Barrera Epidérmica, Ceramidas y Calma Antipruriginosa",
            "rationale": "Aporta ácidos grasos esenciales GLA, ceramidas y bioflavonoides antihistamínicos para reparar la barrera de filagrina y detener el ciclo de picor-rascado Th2."
        },
        "ar": {
            "philosophy": "ترميم حاجز البشرة، تعويض السيراميد ومكافحة الحكة",
            "rationale": "يعزز دهون البشرة الأساسية والسيراميد، ويرمم حاجز الجلد التالف ويهدئ نوبات الحكة الشديدة للأكزيما."
        }
    },
    "psor": {
        "en": {
            "philosophy": "Systemic Th17 Cytokine Quenching & Keratinocyte Antiproliferative Protocol",
            "rationale": "Supplies high-potency curcuminoids, marine omega-3 EPA/DHA, and plant polyphenols that downregulate IL-23/IL-17 inflammatory signaling, curbing keratinocyte hyperproliferation and clearing erythematous scaly plaques."
        },
        "kn": {
            "philosophy": "ವ್ಯವಸ್ಥಿತ ಆಂಟಿ-ಇನ್‌ಫ್ಲಮೇಟರಿ ಮತ್ತು ಕೆರಾಟಿನೊಸೈಟ್ ಅತಿಯಾದ ಬೆಳವಣಿಗೆ ನಿಯಂತ್ರಣ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ದೇಹದೊಳಗಿನ ಉರಿಯೂತದ ಸೈಟೊಕಿನ್‌ಗಳನ್ನು ತಗ್ಗಿಸಲು, ಚರ್ಮದ ಕೋಶಗಳ ಅತಿಯಾದ ಮತ್ತು ಅಸಹಜ ಉತ್ಪಾದನೆಯನ್ನು ನಿಗ್ರಹಿಸಲು ಮತ್ತು ಸೋರಿಯಾಸಿಸ್ ತೇಪೆಗಳನ್ನು ಮೃದುಗೊಳಿಸಲು ಪ್ರಬಲ ಕರ್ಕ್ಯುಮಿನ್ ಮತ್ತು ಒಮೆಗಾ-3 ಒದಗಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "प्रणालीगत सूजन शमन एवं असामान्य त्वचा कोशिका वृद्धि नियंत्रण प्रोटोकॉल",
            "rationale": "सूजन पैदा करने वाले साइटोकिन्स को दबाता है, त्वचा की कोशिकाओं के अत्यधिक तेजी से बढ़ने को रोकता है और सोरायसिस की पपड़ीदार परतों को कम करता है।"
        },
        "ta": {
            "philosophy": "உடலெங்கும் அழற்சி தடுப்பு & தோல் செல்கள் பெருக்கக் கட்டுப்பாடு நெறிமுறை",
            "rationale": "தோல் செல்கள் மிக வேகமாக உற்பத்தியாவதைத் தடுத்து, தடிப்பு மற்றும் செதில் போன்ற அடுக்குகளைக் குறைக்கும் அழற்சி எதிர்ப்பு ஊட்டச்சத்துக்களை வழங்குகிறது."
        },
        "te": {
            "philosophy": "దైహిక వాపు నివారణ & అసాధారణ చర్మ కణాల పెరుగుదల నియంత్రణ ప్రోటోకాల్",
            "rationale": "శరీరంలో వాపును కలిగించే కారకాలను నియంత్రిస్తుంది, చర్మ కణాలు అసాధారణ వేగంతో పెరగడాన్ని అడ్డుకుని పొలుసుల తెగులును తగ్గిస్తుంది."
        },
        "bn": {
            "philosophy": "সিস্টেমিক প্রদাহ নিরাময় এবং ত্বক কোষের অতিরিক্ত বৃদ্ধি প্রতিরোধ পদ্ধতি",
            "rationale": "প্রদাহজনিত সাইটোকাইন কমায়, ত্বকের কোষের অতিরিক্ত বিস্তার নিয়ন্ত্রণ করে এবং সোরিয়াসিসের আঁশযুক্ত স্তর নিরাময়ে সাহায্য করে।"
        },
        "mr": {
            "philosophy": "सूज नियंत्रण आणि पेशींची असामान्य वाढ रोखणारा प्रोटोकॉल",
            "rationale": "प्रथिनांमधील जळजळ शांत करते, त्वचेच्या पेशींची अतिवेगवान वाढ रोखते आणि सोरायसिसच्या पांढऱ्या खपल्या कमी करते."
        },
        "es": {
            "philosophy": "Supresión Sistémica de Citoquinas Th17 y Control Antiproliferativo",
            "rationale": "Aporta curcuminoides de alta biodisponibilidad y EPA marino para inhibir la cascada IL-23/IL-17, frenando la hiperqueratosis y descamación de placas."
        },
        "ar": {
            "philosophy": "تثبيط السيتوكينات الالتهابية وضبط التكاثر المفرط لخلايا الجلد",
            "rationale": "يحد من مسارات الالتهاب المناعي IL-17، ويكبح تكاثر خلايا الجلد المفرط لتقليل قشور الصدفية واحمرارها."
        }
    },
    "vit": {
        "en": {
            "philosophy": "Melanocyte Redox Stabilization & Tyrosinase Nutritional Support Protocol",
            "rationale": "Floods the cutaneous microenvironment with targeted mitochondrial antioxidants (polyphenols, ginkgo biloba, folate, B12, copper) to neutralize reactive oxygen species and shield follicular melanocyte stem cells from cytotoxic T-cell destruction."
        },
        "kn": {
            "philosophy": "ಮೆಲನೊಸೈಟ್ ರಕ್ಷಣೆ ಮತ್ತು ಟೈರೋಸಿನೇಸ್ ಪೌಷ್ಟಿಕ ಬೆಂಬಲ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ಚರ್ಮಕ್ಕೆ ಬಣ್ಣ ನೀಡುವ ಮೆಲನೊಸೈಟ್ ಕೋಶಗಳನ್ನು ಆಕ್ಸಿಡೇಟಿವ್ ಒತ್ತಡದಿಂದ ರಕ್ಷಿಸುವ, ವಿಟಮಿನ್ ಬಿ12, ಫೋಲೇಟ್ ಮತ್ತು ತಾಮ್ರದಂತಹ ಸೂಕ್ಷ್ಮ ಪೋಷಕಾಂಶಗಳನ್ನು ಒದಗಿಸಿ ವರ್ಣದ್ರವ್ಯ ಮರುಉತ್ಪಾದನೆಗೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "मेलानोसाइट एंटीऑक्सीडेंट सुरक्षा एवं वर्णक पुनर्जनन प्रोटोकॉल",
            "rationale": "त्वचा को रंग देने वाली मेलानोसाइट कोशिकाओं को ऑक्सीडेटिव क्षति से बचाता है, फोलेट व बी12 प्रदान करता है और प्राकृतिक मेलेनिन पिगमेंटेशन को बढ़ावा देता है।"
        },
        "ta": {
            "philosophy": "மெலனோசைட் பாதுகாப்பு & நிறமி மறுஉற்பத்தி நெறிமுறை",
            "rationale": "நிறமி உற்பத்தி செய்யும் செல்களை ஆக்ஸிஜனேற்ற அழிவிலிருந்து பாதுகாத்து, மெலனின் உற்பத்தியை ஊக்குவிக்கும் தாதுக்களை வழங்குகிறது."
        },
        "te": {
            "philosophy": "మెలనోసైట్ రక్షణ & వర్ణద్రవ్య పునరుత్పత్తి ప్రోటోకాల్",
            "rationale": "రంగును ఉత్పత్తి చేసే మెలనోసైట్ కణాలను ఆక్సీకరణ నష్టం నుండి రక్షిస్తుంది మరియు సహజ మెలనిన్ ఉత్పత్తికి తోడ్పడుతుంది."
        },
        "bn": {
            "philosophy": "মেলানোসাইট সুরক্ষা এবং ত্বকের স্বাভাবিক রঞ্জক পুনরুদ্ধার পদ্ধতি",
            "rationale": "রঞ্জক উৎপাদনকারী কোষগুলিকে সুরক্ষিত রাখে, ফলিক অ্যাসিড ও বি১২ সরবরাহ করে শ্বেত বা ভিটিলিগোতে স্বাভাবিক মেলানিন তৈরি হতে সহায়তা করে।"
        },
        "mr": {
            "philosophy": "मेलॅनोसाइट पेशी संरक्षण आणि रंगद्रव्य पुनरुत्पादन प्रोटोकॉल",
            "rationale": "त्वचेला नैसर्गिक रंग देणाऱ्या पेशींचे संरक्षण करते, व्हिटॅमिन बी१२ आणि कॉपर पुरवून पुन्हा रंगद्रव्य तयार होण्यास मदत करते."
        },
        "es": {
            "philosophy": "Estabilización Redox de Melanocitos y Soporte de Tirosinasa",
            "rationale": "Suministra antioxidantes mitocondriales selectivos, ácido fólico, B12 y cobre para proteger las células madre melanocíticas foliculares del ataque autoinmune."
        },
        "ar": {
            "philosophy": "تثبيت الأكسدة للخلايا الصباغية ودعم إنزيم التيروزيناز",
            "rationale": "يحمي الخلايا الصباغية من الإجهاد التأكسدي والهجوم المناعي، ويوفر فيتامين ب12 والفولات لتشجيع استعادة التصبغ الطبيعي للبهاق."
        }
    },
    "ros": {
        "en": {
            "philosophy": "Neuro-Vascular Calming, Vasomotor Stability & Anti-Flushing Protocol",
            "rationale": "Focuses on bioflavonoids, cooling anti-inflammatory polyphenols, and avoiding vasodilator triggers (capsaicin, cinnamaldehyde, extreme heat) to decrease facial capillary permeability, calm Demodex mite reactions, and prevent neurogenic flushing."
        },
        "kn": {
            "philosophy": "ನರ-ರಕ್ತನಾಳ ಶಾಂತಗೊಳಿಸುವಿಕೆ ಮತ್ತು ಮುಖದ ಕೆಂಪಾಗುವಿಕೆ ತಡೆ ಪ್ರೋಟೋಕಾಲ್",
            "rationale": "ಮುಖದ ಸೂಕ್ಷ್ಮ ರಕ್ತನಾಳಗಳು ಅತಿಯಾಗಿ ಹಿಗ್ಗುವುದನ್ನು ಮತ್ತು ಒಡೆಯುವುದನ್ನು ತಡೆಯುತ್ತದೆ, ಮಸಾಲೆಯುಕ್ತ ಆಹಾರದ ಪ್ರಚೋದನೆಗಳಿಂದ ರಕ್ಷಿಸುತ್ತದೆ ಮತ್ತು ಮುಖದ ಉರಿ ಹಾಗೂ ಕೆಂಪಾಗುವಿಕೆಯನ್ನು ಶಮನಗೊಳಿಸುತ್ತದೆ."
        },
        "hi": {
            "philosophy": "न्यूरो-वास्कुलर स्थिरता एवं चेहरे की लालिमा शमन प्रोटोकॉल",
            "rationale": "चेहरे की सूक्ष्म रक्त वाहिकाओं को शांत करता है, गर्माहट व तीखे मसालों से होने वाले फैलाव को रोकता है और चेहरे की जलन व लाली को दूर करता है।"
        },
        "ta": {
            "philosophy": "நரம்பு-ரத்தநாள அமைதிப்படுத்தல் & முக சிவத்தல் தடுப்பு நெறிமுறை",
            "rationale": "முகத்தில் உள்ள மெல்லிய ரத்த நாளங்கள் வீங்குவதைத் தடுத்து, காரமான உணவுகளின் தூண்டுதலைத் தவிர்த்து முக சிவப்பைக் குறைக்கிறது."
        },
        "te": {
            "philosophy": "న్యూరో-వాస్కులర్ శాంతపరచడం & ముఖ ఎరుపు నివారణ ప్రోటోకాల్",
            "rationale": "ముఖంలోని సున్నితమైన రక్తనాళాలు వ్యాకోచించకుండా నిరోధిస్తుంది మరియు మంట, ఎరుపుదనాన్ని తగ్గిస్తుంది."
        },
        "bn": {
            "philosophy": "রক্তনালী প্রশমন এবং মুখের লালচে ভাব নিরাময় পদ্ধতি",
            "rationale": "মুখের সূক্ষ্ম রক্তনালীর অস্বাভাবিক প্রসারণ রোধ করে, অতিরিক্ত মশলাজনিত প্রদাহ কমায় এবং ত্বকের জ্বালাপোড়া দূর করে।"
        },
        "mr": {
            "philosophy": "रक्तवाहिन्या शांत करणे आणि चेहऱ्यावरील लालसरपणा कमी करणारा प्रोटोकॉल",
            "rationale": "चेहऱ्यावरील सूक्ष्म रक्तवाहिन्यांचे फुगणे कमी करते, तिखट व उष्ण घटकांपासून संरक्षण देते आणि चेहऱ्याचा लालसरपणा शांत करते."
        },
        "es": {
            "philosophy": "Calma Neurovascular, Estabilidad Vasomotora y Anti-Flushing",
            "rationale": "Aporta bioflavonoides y polifenoles refrescantes mientras excluye desencadenantes vasodilatadores para frenar el enrojecimiento facial y la hiperreactividad capilar."
        },
        "ar": {
            "philosophy": "التهدئة العصبية الوعائية، استقرار الأوعية الدموية ومكافحة التوهج",
            "rationale": "يقوي الشعيرات الدموية الدقيقة في الوجه، ويتجنب محفزات توسع الأوعية ويقلل من نوبات الاحمرار والتهاب العد الوردي."
        }
    }
}

# ─────────────────────────────────────────────────────────────
# Multi-Language Translation Dictionaries for Diet & Nutrition
# ─────────────────────────────────────────────────────────────

DIET_TRANSLATIONS = {
    "en": {
        "lang_name": "English",
        "diet_preference_label": "Dietary Preference Track:",
        "non_veg": "🍗 Non-Vegetarian (Non-Veg)",
        "non_veg_sub": "Fresh Fish, Poultry, Egg Whites & Bone Broth",
        "vegetarian": "🥗 Pure Vegetarian (Veg)",
        "vegetarian_sub": "Paneer, Lentils, Sprouted Pulses & Probiotic Dahi",
        "meal_split_title": "Structured 3-Times Daily Meal Split (Circadian Aligned)",
        "breakfast": "Breakfast",
        "lunch": "Lunch",
        "dinner": "Dinner",
        "hydration": "Traditional Hydration Ritual",
        "timing_breakfast": "08:00 AM – 08:30 AM (Morning metabolic activation & barrier defense)",
        "timing_lunch": "12:30 PM – 01:30 PM (Peak digestive fire & heavy antioxidant payload)",
        "timing_dinner": "06:30 PM – 07:30 PM (Light restorative meal to trigger nocturnal autophagy & DNA repair)",
        "timing_fasting": "13–14 hour overnight fasting window (7:30 PM – 8:30 AM) to optimize nucleotide excision repair.",
        "regional_ingredients": "Regional Ingredients",
        "cellular_target": "Cellular Target",
        "therapeutic_ingredients": "Therapeutic Ingredients",
        "biological_action": "Biological Action",
        "circadian_header": "⏰ Circadian Autophagy & Timing",
        "substitutions_header": "🔄 Local Ingredient Substitutions",
        "grocery_header": "🛒 Smart Grocery Checklist",
        "copy_button": "📋 Copy List",
        "superfoods_heading": "Therapeutic Molecular Superfoods for Detected Pathology",
        "avoid_heading": "Foods & Triggers to Restrict",
        "supplements_heading": "Evidence-Backed Micronutrient & Supplement Guidelines",
        "read_aloud": "🔊 Read Aloud"
    },
    "hi": {
        "lang_name": "हिंदी (Hindi)",
        "diet_preference_label": "आहार प्राथमिकता चुनें (Diet Preference):",
        "non_veg": "🍗 मांसाहारी आहार (Non-Veg)",
        "non_veg_sub": "ताज़ी मछली, देसी चिकन, उबले अंडे और बोन ब्रोथ",
        "vegetarian": "🥗 शुद्ध शाकाहारी आहार (Veg)",
        "vegetarian_sub": "दालें, अंकुरित अनाज, पनीर और प्रोबायोटिक दही",
        "meal_split_title": "दैनिक ३-समय भोजन विभाजन (सर्कैडियन तालबद्ध)",
        "breakfast": "सुबह का नाश्ता (Breakfast)",
        "lunch": "दोपहर का भोजन (Lunch)",
        "dinner": "रात का भोजन (Dinner)",
        "hydration": "पारंपरिक औषधीय पेय / काढ़ा (Hydration)",
        "timing_breakfast": "प्रातः 08:00 – 08:30 (मेटाबॉलिक सक्रियण और त्वचा अवरोधक सुरक्षा)",
        "timing_lunch": "दोपहर 12:30 – 01:30 (उच्च पाचन अग्नि और एंटीऑक्सीडेंट पोषण)",
        "timing_dinner": "शाम 06:30 – 07:30 (हल्का पाचक भोजन, रात्रि ऑटोफैगी और डीएनए मरम्मत)",
        "timing_fasting": "13–14 घंटे का रात का उपवास (7:30 PM – 8:30 AM) जो क्षतिग्रस्त कोशिकाओं को साफ करता है।",
        "regional_ingredients": "क्षेत्रीय सामग्रियां (Ingredients)",
        "cellular_target": "कोशिकीय लाभ व जैविक लक्ष्य (Cellular Target)",
        "therapeutic_ingredients": "औषधीय सामग्रियां",
        "biological_action": "जैविक प्रभाव",
        "circadian_header": "⏰ सर्कैडियन ऑटोफैगी और समय चक्र",
        "substitutions_header": "🔄 स्थानीय सामग्री प्रतिस्थापन (Substitutions)",
        "grocery_header": "🛒 स्मार्ट किराना चेकलिस्ट (Grocery List)",
        "copy_button": "📋 सूची कॉपी करें",
        "superfoods_heading": "पहचाने गए रोग के लिए चिकित्सीय आणविक सुपरफूड्स",
        "avoid_heading": "परहेज करने योग्य खाद्य पदार्थ व ट्रिगर्स",
        "supplements_heading": "वैज्ञानिक साक्ष्य-आधारित माइक्रोन्यूट्रिएंट व सप्लीमेंट दिशानिर्देश",
        "read_aloud": "🔊 बोलकर सुनें"
    },
    "ta": {
        "lang_name": "தமிழ் (Tamil)",
        "diet_preference_label": "உணவு முறை விருப்பம் (Diet Preference):",
        "non_veg": "🍗 அசைவ உணவு (Non-Veg)",
        "non_veg_sub": "கடல் மீன், நாட்டுக்கோழி, முட்டை வெள்ளைக்கரு",
        "vegetarian": "🥗 தூய சைவ உணவு (Veg)",
        "vegetarian_sub": "பருப்பு வகைகள், முளைகட்டிய பயறு, தயிர்",
        "meal_split_title": "தினசரி 3-வேளை உணவு முறை (சர்க்காடியன் சீரமைப்பு)",
        "breakfast": "காலை உணவு (Breakfast)",
        "lunch": "மதிய உணவு (Lunch)",
        "dinner": "இரவு உணவு (Dinner)",
        "hydration": "பாரம்பரிய மூலிகை நீர் சடங்கு (Hydration)",
        "timing_breakfast": "காலை 08:00 – 08:30 (வளர்சிதை மாற்ற பாதுகாப்பு)",
        "timing_lunch": "மதியம் 12:30 – 01:30 (செரிமான தீ மற்றும் ஆன்டி-ஆக்ஸிடன்ட்)",
        "timing_dinner": "இரவு 06:30 – 07:30 (எளிதில் செரிக்கும் உணவு மற்றும் டிஎன்ஏ பழுதுபார்ப்பு)",
        "timing_fasting": "13–14 மணிநேர இரவு உண்ணாநோன்பு செல்லுலார் நச்சு நீக்கத்தை தூண்டுகிறது.",
        "regional_ingredients": "பொருட்கள் (Ingredients)",
        "cellular_target": "செல்லுலார் இலக்கு (Cellular Target)",
        "therapeutic_ingredients": "சிகிச்சை பொருட்கள்",
        "biological_action": "உயிரியல் செயல்பாடு",
        "circadian_header": "⏰ சர்க்காடியன் ஆட்டோபேஜி நேரம்",
        "substitutions_header": "🔄 உள்ளூர் மாற்றுப் பொருட்கள் (Substitutions)",
        "grocery_header": "🛒 ஸ்மார்ட் மளிகைப் பட்டியல்",
        "copy_button": "📋 நகலெடு",
        "superfoods_heading": "தோல் நோய்க்கான மருத்துவ சூப்பர் உணவுகள்",
        "avoid_heading": "தவிர்க்க வேண்டிய உணவுகள்",
        "supplements_heading": "ஆதார அடிப்படையிலான சப்ளிமெண்ட் வழிகாட்டுதல்கள்",
        "read_aloud": "🔊 வாசித்துக் காட்டு"
    },
    "te": {
        "lang_name": "తెలుగు (Telugu)",
        "diet_preference_label": "ఆహార ప్రాధాన్యత ఎంపిక (Diet Preference):",
        "non_veg": "🍗 మాంసాహార ఆహారం (Non-Veg)",
        "non_veg_sub": "చేపలు, నాటుకోడి, గుడ్డు తెల్లసొన, ఎముకల సూప్",
        "vegetarian": "🥗 శుద్ధ శాఖాహార ఆహారం (Veg)",
        "vegetarian_sub": "పప్పుధాన్యాలు, మొలకెత్తిన గింజలు, పెరుగు",
        "meal_split_title": "దినచర్య 3-పూటల ఆహార విభజన (సర్కాడియన్ సమన్వయం)",
        "breakfast": "ఉదయం అల్పాహారం (Breakfast)",
        "lunch": "మధ్యాహ్న భోజనం (Lunch)",
        "dinner": "రాత్రి భోజనం (Dinner)",
        "hydration": "సాంప్రదాయ ఔషధ ద్రవ ఆహారం (Hydration)",
        "timing_breakfast": "ఉదయం 08:00 – 08:30 (మెటబాలిక్ రక్షణ)",
        "timing_lunch": "మధ్యాహ్నం 12:30 – 01:30 (జీర్ణక్రియ మరియు యాంటీఆక్సిడెంట్స్)",
        "timing_dinner": "రాత్రి 06:30 – 07:30 (తేలికపాటి ఆహారం, కణాల పునరుత్పత్తి)",
        "timing_fasting": "13–14 గంటల రాత్రి ఉపవాసం కణాల మరమ్మత్తును వేగవంతం చేస్తుంది.",
        "regional_ingredients": "ప్రాంతీయ పదార్థాలు (Ingredients)",
        "cellular_target": "కణ లక్ష్యం (Cellular Target)",
        "therapeutic_ingredients": "ఔషధ పదార్థాలు",
        "biological_action": "జీవక్రియ చర్య",
        "circadian_header": "⏰ సర్కాడియన్ ఆటోఫాగి సమయం",
        "substitutions_header": "🔄 స్థానిక ప్రత్యామ్నాయాలు (Substitutions)",
        "grocery_header": "🛒 స్మార్ట్ కిరాణా జాబితా",
        "copy_button": "📋 కాపీ చేయి",
        "superfoods_heading": "చర్మ రక్షణకు చికిత్సా సూపర్ ఫుడ్స్",
        "avoid_heading": "నివారించవలసిన ఆహారాలు",
        "supplements_heading": "సాక్ష్యాధారిత పోషకాల మార్గదర్శకాలు",
        "read_aloud": "🔊 వినిపించు"
    },
    "bn": {
        "lang_name": "বাংলা (Bengali)",
        "diet_preference_label": "আহারের ধরন নির্বাচন (Diet Preference):",
        "non_veg": "🍗 আমিষ আহার (Non-Veg)",
        "non_veg_sub": "সামুদ্রিক ও দেশি মাছ, দেশি মুরগি, ডিমের সাদা অংশ",
        "vegetarian": "🥗 সম্পূর্ণ নিরামিষ আহার (Veg)",
        "vegetarian_sub": "ডাল, অঙ্কুরিত ছোলা, পনির এবং প্রোবায়োটিক দই",
        "meal_split_title": "দৈনিক ৩-বেলা খাবার বিভাজন (সার্কেডিয়ান নিয়ম অনুযায়ী)",
        "breakfast": "সকালের নাস্তা (Breakfast)",
        "lunch": "দুপুরের খাবার (Lunch)",
        "dinner": "রাতের খাবার (Dinner)",
        "hydration": "ঐতিহ্যবাহী ভেষজ জলপান (Hydration)",
        "timing_breakfast": "সকাল ০৮:০০ – ০৮:৩০ (মেটাবলিক প্রতিরক্ষা)",
        "timing_lunch": "দুপুর ১২:৩০ – ০১:৩০ (উচ্চ হজম ক্ষমতা ও অ্যান্টিঅক্সিডেন্ট)",
        "timing_dinner": "সন্ধ্যা ০৬:৩০ – ০৭:৩০ (সহজে হজমযোগ্য খাবার ও ডিএনএ মেরামত)",
        "timing_fasting": "১৩–১৪ ঘণ্টার রাতকালীন উপবাস কোষের ক্ষতি মেরামত করতে সাহায্য করে।",
        "regional_ingredients": "আঞ্চলিক উপাদান (Ingredients)",
        "cellular_target": "কোষীয় কার্যকারিতা (Cellular Target)",
        "therapeutic_ingredients": "থেরাপিউটিক উপাদান",
        "biological_action": "জৈবিক ক্রিয়া",
        "circadian_header": "⏰ সার্কেডিয়ান অটোফ্যাজি টাইমিং",
        "substitutions_header": "🔄 স্থানীয় বিকল্প উপাদান (Substitutions)",
        "grocery_header": "🛒 স্মার্ট মুদি তালিকা",
        "copy_button": "📋 অনুলিপি করুন",
        "superfoods_heading": "ত্বকের রোগ নিরাময়ে থেরাপিউটিক সুপারফুড",
        "avoid_heading": "বর্জনীয় খাবার ও ট্রিগার",
        "supplements_heading": "প্রমাণ-ভিত্তিক সাপ্লিমেন্ট নির্দেশিকা",
        "read_aloud": "🔊 পড়ে শোনান"
    },
    "mr": {
        "lang_name": "मराठी (Marathi)",
        "diet_preference_label": "आहार प्रकार निवडा (Diet Preference):",
        "non_veg": "🍗 मांसाहारी आहार (Non-Veg)",
        "non_veg_sub": "ताजी मासळी (बांगडा/सुरमई), गावठी चिकन, अंड्याचा पांढरा भाग",
        "vegetarian": "🥗 शुद्ध शाकाहारी आहार (Veg)",
        "vegetarian_sub": "डाळी, मोड आलेली कडधान्ये, ताजे दही, पनीर",
        "meal_split_title": "दैनंदिन ३-वेळांचे भोजन विभाजन (सर्कॅडियन वेळेनुसार)",
        "breakfast": "सकाळचा नाश्ता (Breakfast)",
        "lunch": "दुपारचे जेवण (Lunch)",
        "dinner": "रात्रीचे जेवण (Dinner)",
        "hydration": "पारंपारिक औषधी पेय (Hydration)",
        "timing_breakfast": "सकाळी ०८:०० – ०८:३० (रोगप्रतिकारक ऊर्जा)",
        "timing_lunch": "दुपारी १२:३० – ०१:३० (उत्तम पचन आणि अँटिऑक्सिडंट)",
        "timing_dinner": "संध्याकाळी ०६:३० – ०७:३० (हलका आहार, रात्री पेशींची दुरुस्ती)",
        "timing_fasting": "१३–१४ तासांचा रात्रीचा उपवास पेशींमधील विषद्रव्ये बाहेर काढतो.",
        "regional_ingredients": "स्थानिक साहित्य (Ingredients)",
        "cellular_target": "जैविक व पेशी स्तर उद्दिष्ट (Cellular Target)",
        "therapeutic_ingredients": "औषधी साहित्य",
        "biological_action": "जैविक प्रभाव",
        "circadian_header": "⏰ सर्कॅडियन ऑटोफॅगी वेळ",
        "substitutions_header": "🔄 स्थानिक पर्याय (Substitutions)",
        "grocery_header": "🛒 स्मार्ट किराणा यादी",
        "copy_button": "📋 यादी कॉपी करा",
        "superfoods_heading": "त्वचारोगासाठी उपचारात्मक सुपरफूड्स",
        "avoid_heading": "टाळायचे अन्न घटक",
        "supplements_heading": "वैज्ञानिक पुरावा-आधारित पूरक आहार",
        "read_aloud": "🔊 ऐका"
    },
    "es": {
        "lang_name": "Español (Spanish)",
        "diet_preference_label": "Preferencia Dietética:",
        "non_veg": "🍗 Dieta No Vegetariana (Pescados y Carnes)",
        "non_veg_sub": "Pescado salvaje, pollo de campo, claras de huevo",
        "vegetarian": "🥗 Dieta Vegetariana Pura (Veg)",
        "vegetarian_sub": "Legumbres, semillas germinadas, yogur probiótico",
        "meal_split_title": "División Diaria de 3 Comidas (Alineada con el Ritmo Circadiano)",
        "breakfast": "Desayuno (Breakfast)",
        "lunch": "Almuerzo (Lunch)",
        "dinner": "Cena (Dinner)",
        "hydration": "Ritual Tradicional de Hidratación (Hydration)",
        "timing_breakfast": "08:00 AM – 08:30 AM (Activación metabólica matutina)",
        "timing_lunch": "12:30 PM – 01:30 PM (Digestión óptima y carga antioxidante)",
        "timing_dinner": "06:30 PM – 07:30 PM (Comida ligera reparadora y autofagia nocturna)",
        "timing_fasting": "Ventana de ayuno nocturno de 13–14 horas para reparación celular de ADN.",
        "regional_ingredients": "Ingredientes Regionales",
        "cellular_target": "Objetivo Celular",
        "therapeutic_ingredients": "Ingredientes Terapéuticos",
        "biological_action": "Acción Biológica",
        "circadian_header": "⏰ Autofagia Circadiana y Tiempos",
        "substitutions_header": "🔄 Sustituciones Locales de Ingredientes",
        "grocery_header": "🛒 Lista Inteligente de Compras",
        "copy_button": "📋 Copiar Lista",
        "superfoods_heading": "Superalimentos Moleculares Terapéuticos",
        "avoid_heading": "Alimentos y Disparadores a Restringir",
        "supplements_heading": "Pautas de Micronutrientes Respaldadas por Evidencia",
        "read_aloud": "🔊 Escuchar en Voz Alta"
    },
    "ar": {
        "lang_name": "العربية (Arabic)",
        "diet_preference_label": "المسار الغذائي المفضل:",
        "non_veg": "🍗 نظام غير نباتي (لحوم ودواجن وأسماك)",
        "non_veg_sub": "أسماك طازجة، دجاج بلدي، بياض البيض، مرق العظام",
        "vegetarian": "🥗 نظام نباتي نقي (خضار وبقوليات)",
        "vegetarian_sub": "بقوليات، حبوب مستنبتة، لبن زبادي بروبيوتيك",
        "meal_split_title": "تقسيم الوجبات اليومية الثلاث (المتوافقة مع الساعة البيولوجية)",
        "breakfast": "وجبة الإفطار (Breakfast)",
        "lunch": "وجبة الغداء (Lunch)",
        "dinner": "وجبة العشاء (Dinner)",
        "hydration": "طقوس الترطيب التقليدية (Hydration)",
        "timing_breakfast": "08:00 ص – 08:30 ص (تنشيط الأيض وحماية الخلايا)",
        "timing_lunch": "12:30 م – 01:30 م (ذروة الهضم ومضادات الأكسدة)",
        "timing_dinner": "06:30 م – 07:30 م (وجبة خفيفة لبدء الالتهام الذاتي الليلي)",
        "timing_fasting": "نافذة صيام ليلي لمدة 13–14 ساعة لتحفيز إصلاح الحمض النووي.",
        "regional_ingredients": "المكونات الإقليمية",
        "cellular_target": "الهدف الخلوي",
        "therapeutic_ingredients": "المكونات العلاجية",
        "biological_action": "التأثير البيولوجي",
        "circadian_header": "⏰ الالتهام الذاتي والتوقيت اليومي",
        "substitutions_header": "🔄 البدائل الغذائية المحلية",
        "grocery_header": "🛒 قائمة البقالة الذكية",
        "copy_button": "📋 نسخ القائمة",
        "superfoods_heading": "الأغذية العلاجية الجزيئية الفائقة للأمراض الجلدية",
        "avoid_heading": "الأطعمة والمحفزات التي يجب تجنبها",
        "supplements_heading": "إرشادات المغذيات الدقيقة والمكملات المدعومة بالأدلة",
        "read_aloud": "🔊 استمع بصوت عالٍ"
    },
    "kn": {
        "lang_name": "ಕನ್ನಡ (Kannada)",
        "diet_preference_label": "ಆಹಾರದ ಆದ್ಯತೆಯನ್ನು ಆರಿಸಿ (Diet Preference):",
        "non_veg": "🍗 ಮಾಂಸಾಹಾರಿ ಆಹಾರ (Non-Veg)",
        "non_veg_sub": "ತಾಜಾ ಸಮುದ್ರ ಮೀನು, ನಾಟಿ ಕೋಳಿ, ಮೊಟ್ಟೆಯ ಬಿಳಿಭಾಗ ಮತ್ತು ಮೂಳೆ ಸೂಪ್ (ಬೋನ್ ಬ್ರೋತ್)",
        "vegetarian": "🥗 ಶುದ್ಧ ಸಸ್ಯಾಹಾರಿ ಆಹಾರ (Veg)",
        "vegetarian_sub": "ಕಾಳುಗಳು, ಮೊಳಕೆ ಕಾಳು, ಪನೀರ್ ಮತ್ತು ಪ್ರೊಬಯಾಟಿಕ್ ಮೊಸರು",
        "meal_split_title": "ದೈನಂದಿನ ೩-ಹೊತ್ತಿನ ಊಟದ ವಿಭಜನೆ (ಸರ್ಕಾಡಿಯನ್ ಲಯಬದ್ಧ)",
        "breakfast": "ಬೆಳಗಿನ ಉಪಹಾರ (Breakfast)",
        "lunch": "ಮಧ್ಯಾಹ್ನದ ಊಟ (Lunch)",
        "dinner": "ರಾತ್ರಿಯ ಊಟ (Dinner)",
        "hydration": "ಸಾಂಪ್ರದಾಯಿಕ ಗಿಡಮೂಲಿಕೆ ಪಾನೀಯ (Hydration)",
        "timing_breakfast": "ಬೆಳಿಗ್ಗೆ 08:00 – 08:30 (ಮೆಟಾಬಾಲಿಕ್ ಸಕ್ರಿಯಗೊಳಿಸುವಿಕೆ ಮತ್ತು ಚರ್ಮದ ಕೋಶ ರಕ್ಷಣೆ)",
        "timing_lunch": "ಮಧ್ಯಾಹ್ನ 12:30 – 01:30 (ಉತ್ತಮ ಜೀರ್ಣ ಶಕ್ತಿ ಮತ್ತು ಆ್ಯಂಟಿಆಕ್ಸಿಡೆಂಟ್ ಪೋಷಣೆ)",
        "timing_dinner": "ಸಂಜೆ 06:30 – 07:30 (ಸುಲಭವಾಗಿ ಜೀರ್ಣವಾಗುವ ಆಹಾರ, ರಾತ್ರಿಯ ಆಟೋಫ್ಯಾಜಿ ಮತ್ತು ಡಿಎನ್‌ಎ ದುರಸ್ತಿ)",
        "timing_fasting": "13–14 ಗಂಟೆಗಳ ರಾತ್ರಿಯ ಉಪವಾಸ (7:30 PM – 8:30 AM) ಹಾನಿಗೊಳಗಾದ ಜೀವಕೋಶಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸುತ್ತದೆ.",
        "regional_ingredients": "ಪ್ರಾದೇಶಿಕ ಪದಾರ್ಥಗಳು (Ingredients)",
        "cellular_target": "ಜೀವಕೋಶ ಮಟ್ಟದ ಗುರಿ ಮತ್ತು ಜೈವಿಕ ಕ್ರಿಯೆ (Cellular Target)",
        "therapeutic_ingredients": "ಚಿಕಿತ್ಸಕ ಪದಾರ್ಥಗಳು",
        "biological_action": "ಜೈವಿಕ ಕ್ರಿಯೆ",
        "circadian_header": "⏰ ಸರ್ಕಾಡಿಯನ್ ಆಟೋಫ್ಯಾಜಿ ಮತ್ತು ಸಮಯ ಚಕ್ರ",
        "substitutions_header": "🔄 ಸ್ಥಳೀಯ ಪರ್ಯಾಯ ಪದಾರ್ಥಗಳು (Substitutions)",
        "grocery_header": "🛒 ಸ್ಮಾರ್ಟ್ ಕಿರಾಣಿ ಪಟ್ಟಿ (Grocery List)",
        "copy_button": "📋 ಪಟ್ಟಿ ನಕಲಿಸಿ",
        "superfoods_heading": "ಗುರುತಿಸಲಾದ ಚರ್ಮದ ಕಾಯಿಲೆಗೆ ಚಿಕಿತ್ಸಕ ಸೂಪರ್‌ಫುಡ್‌ಗಳು",
        "avoid_heading": "ವರ್ಜಿಸಬೇಕಾದ ಆಹಾರಗಳು ಮತ್ತು ಪ್ರಚೋದಕಗಳು",
        "supplements_heading": "ವೈಜ್ಞಾನಿಕ ಸಾಕ್ಷ್ಯ-ಆಧಾರಿತ ಪೂರಕ ಮಾರ್ಗಸೂಚಿಗಳು",
        "read_aloud": "🔊 ಧ್ವನಿಯಲ್ಲಿ ಕೇಳಿ"
    }
}


def get_diet_translations(lang="en"):
    """Return UI and diet translation dictionary for a given language code."""
    code = (lang or "en").lower().strip()
    lang_alias_map = {
        "kannada": "kn", "hindi": "hi", "tamil": "ta", "telugu": "te",
        "bengali": "bn", "marathi": "mr", "spanish": "es", "arabic": "ar", "english": "en"
    }
    if code in lang_alias_map:
        code = lang_alias_map[code]
    return DIET_TRANSLATIONS.get(code, DIET_TRANSLATIONS["en"])


# ─────────────────────────────────────────────────────────────
# Helper Function to Build & Retrieve Cultural Diets
# ─────────────────────────────────────────────────────────────

def get_cultural_diet_plan(condition_code, country="india", preference="non_veg", lang="en"):
    """
    Returns authentic 3-meal split, circadian timing, grocery list,
    and local substitutions tailored to the user's country, dietary preference, and language.
    """
    country_id = country.lower().strip()
    valid_country_ids = [c["id"] for c in SUPPORTED_COUNTRIES]
    if country_id not in valid_country_ids:
        country_id = "india"

    pref_raw = str(preference).lower().strip().replace("-", "_").replace(" ", "_")
    if pref_raw in ["non_veg", "nonveg", "non_vegetarian", "omnivore"]:
        pref = "non_veg"
    else:
        pref = "vegetarian"

    cond = condition_code.lower().strip()
    country_meta = next(c for c in SUPPORTED_COUNTRIES if c["id"] == country_id)

    # In CULTURAL_DIETS, find either "non_veg" or "omnivore"
    lookup_key = "non_veg" if pref == "non_veg" else "vegetarian"
    country_plans = CULTURAL_DIETS.get(cond, {}).get(country_id, {})
    plan = None
    if country_plans:
        if lookup_key in country_plans:
            plan = country_plans[lookup_key]
        elif "omnivore" in country_plans and lookup_key == "non_veg":
            plan = country_plans["omnivore"]
    
    if not plan:
        # Generate condition-tailored adaptation from the master template
        plan = _generate_condition_adapted_plan(cond, country_id, lookup_key)

    lang_code = (lang or "en").lower().strip()
    lang_alias_map = {
        "kannada": "kn", "hindi": "hi", "tamil": "ta", "telugu": "te",
        "bengali": "bn", "marathi": "mr", "spanish": "es", "arabic": "ar", "english": "en"
    }
    if lang_code in lang_alias_map:
        lang_code = lang_alias_map[lang_code]
    if lang_code not in [l["code"] for l in SUPPORTED_LANGUAGES]:
        lang_code = "en"

    diet_desc = (CONDITION_DIET_DESCRIPTIONS.get(cond, {}).get(lang_code)
                 or CONDITION_DIET_DESCRIPTIONS.get(cond, {}).get("en", {}))
    culinary_focus = (CULINARY_FOCUS_TRANSLATIONS.get(country_id, {}).get(lang_code)
                      or country_meta.get("culinary_focus", ""))

    trans_dict = get_diet_translations(lang_code).copy()
    trans_dict["philosophy"] = diet_desc.get("philosophy", "")
    trans_dict["rationale"] = diet_desc.get("rationale", "")
    trans_dict["culinary_focus"] = culinary_focus

    return {
        "condition_code": cond,
        "country_id": country_id,
        "country_name": country_meta["name"],
        "flag": country_meta["flag"],
        "region": country_meta["region"],
        "culinary_focus": culinary_focus,
        "diet_philosophy": diet_desc.get("philosophy", ""),
        "diet_rationale": diet_desc.get("rationale", ""),
        "dietary_preference": pref,
        "is_non_veg": pref == "non_veg",
        "language": lang_code,
        "circadian_windows": {
            "breakfast": "08:00 AM – 08:30 AM (Morning metabolic activation & barrier defense)",
            "lunch": "12:30 PM – 01:30 PM (Peak digestive fire & heavy antioxidant payload)",
            "dinner": "06:30 PM – 07:30 PM (Light restorative meal to trigger nocturnal autophagy & DNA repair)",
            "autophagy_fasting": "13–14 hour overnight fasting window (7:30 PM – 8:30 AM) to optimize nucleotide excision repair."
        },
        "meals": (lambda m, l: {
            "breakfast": {
                "title": translate_dish_title(m["breakfast"].get("title", ""), l),
                "orig_title": m["breakfast"].get("title", ""),
                "timing": m["breakfast"].get("timing", ""),
                "ingredients": translate_ingredients(m["breakfast"].get("ingredients", ""), l),
                "orig_ingredients": m["breakfast"].get("ingredients", ""),
                "action": translate_action(m["breakfast"].get("action", ""), l),
                "orig_action": m["breakfast"].get("action", "")
            },
            "lunch": {
                "title": translate_dish_title(m["lunch"].get("title", ""), l),
                "orig_title": m["lunch"].get("title", ""),
                "timing": m["lunch"].get("timing", ""),
                "ingredients": translate_ingredients(m["lunch"].get("ingredients", ""), l),
                "orig_ingredients": m["lunch"].get("ingredients", ""),
                "action": translate_action(m["lunch"].get("action", ""), l),
                "orig_action": m["lunch"].get("action", "")
            },
            "dinner": {
                "title": translate_dish_title(m["dinner"].get("title", ""), l),
                "orig_title": m["dinner"].get("title", ""),
                "timing": m["dinner"].get("timing", ""),
                "ingredients": translate_ingredients(m["dinner"].get("ingredients", ""), l),
                "orig_ingredients": m["dinner"].get("ingredients", ""),
                "action": translate_action(m["dinner"].get("action", ""), l),
                "orig_action": m["dinner"].get("action", "")
            },
            "hydration": translate_hydration_item(m.get("hydration", {}), l)
        })(plan["meals"] if "meals" in plan else plan, lang_code) if lang_code != "en" else {
            "breakfast": plan.get("breakfast", plan.get("meals", {}).get("breakfast")),
            "lunch": plan.get("lunch", plan.get("meals", {}).get("lunch")),
            "dinner": plan.get("dinner", plan.get("meals", {}).get("dinner")),
            "hydration": plan.get("hydration", plan.get("meals", {}).get("hydration"))
        },
        "grocery_list": plan.get("grocery_list", {}),
        "local_substitutions": translate_substitutions_list(plan.get("local_substitutions", []), lang_code) if lang_code != "en" else plan.get("local_substitutions", []),
        "translations": trans_dict
    }


def _generate_condition_adapted_plan(cond, country_id, pref):
    """
    Dynamically constructs condition-adapted cultural 3-meal plans
    for bcc, akiec, vasc, nv, bkl, df based on regional superfoods.
    """
    c_plans = CULTURAL_DIETS.get("mel", {}).get(country_id, {})
    lookup_key = "non_veg" if pref in ["non_veg", "omnivore"] else "vegetarian"
    base = c_plans.get(lookup_key) or c_plans.get("omnivore") or c_plans.get("vegetarian")
    if not base:
        india_plans = CULTURAL_DIETS["mel"]["india"]
        base = india_plans.get("non_veg") or india_plans.get("omnivore") if lookup_key == "non_veg" else india_plans["vegetarian"]

    # Customize actions and ingredients to specific disease targets
    if cond == "bcc":
        # Target: EGCG green tea, Garlic (allicin), Apigenin (parsley/celery), Carotenoids
        return {
            "breakfast": {
                "title": f"Epigenetic Morning Bowl: {base['breakfast']['title'].split('with')[0]} with Green Tea & Carotenoids",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, steeped green tea, grated carrots",
                "action": "Inhibits Sonic Hedgehog (SHH/Gli1) activation and delivers singlet-oxygen carotenoid scavengers."
            },
            "lunch": {
                "title": f"Anti-Angiogenesis Plate: {base['lunch']['title']} with Crushed Garlic & Parsley",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, abundant crushed fresh garlic (allicin), flat parsley",
                "action": "Diallyl sulfides trigger G2/M cell cycle arrest and downregulate abnormal VEGF tumor angiogenesis."
            },
            "dinner": {
                "title": f"Restorative Cellular Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Suppresses matrix metalloproteinases (MMP-2/9) and supports evening tissue homeostasis."
            },
            "hydration": base["hydration"],
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    elif cond == "akiec":
        # Target: Nicotinamide B3, Lycopene, Sulforaphane, Omega-3
        return {
            "breakfast": {
                "title": f"DNA Excision Protocol: {base['breakfast']['title']} with Stewed Tomatoes",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, cooked vine tomatoes (lycopene), nutritional yeast",
                "action": "Restores intracellular NAD+ pools to accelerate nucleotide excision repair of UV-induced thymine dimers."
            },
            "lunch": {
                "title": f"Photoprotection Plate: {base['lunch']['title']} with Cruciferous Greens",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, broccoli sprouts or cabbage (sulforaphane)",
                "action": "Upregulates Nrf2 phase II protective enzymes and quenches dermal solar reactive oxygen species."
            },
            "dinner": {
                "title": f"Cellular Recovery Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Downregulates COX-2 photoinflammatory pathways and facilitates overnight keratinocyte turnover."
            },
            "hydration": base["hydration"],
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    elif cond == "vasc":
        # Target: Rutin, Hesperidin, Anthocyanins, Magnesium
        return {
            "breakfast": {
                "title": f"Capillary Wall Protocol: {base['breakfast']['title']} with Buckwheat & Citrus",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, citrus pith (hesperidin), dark berries",
                "action": "Bioflavonoids strengthen microvascular basement membranes and reduce capillary fragility."
            },
            "lunch": {
                "title": f"Endothelial Support Plate: {base['lunch']['title']} with Fresh Celery",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, fresh celery stalks (phthalides), avocado (potassium)",
                "action": "Relaxes vascular smooth muscle tone and maintains balanced hydrostatic capillary pressure."
            },
            "dinner": {
                "title": f"Gentle Vascular Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Eliminates vasodilating triggers (spices/alcohol) to reduce superficial capillary engorgement."
            },
            "hydration": {
                "title": "Cool Bilberry & Hibiscus Infusion",
                "timing": "Throughout the day (served cool, not scalding)",
                "ingredients": "Dried bilberries, hibiscus flowers, cool spring water",
                "action": "Anthocyanins prevent microvascular collagen degradation without triggering facial flushing."
            },
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    elif cond == "bkl":
        # Target: Glycemic control, cinnamon, apple cider vinegar, low sugar berries
        return {
            "breakfast": {
                "title": f"Insulin-Regulating Morning: {base['breakfast']['title']} with Ceylon Cinnamon",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, 1/2 tsp Ceylon cinnamon, berries",
                "action": "Prevents postprandial insulin spikes that activate IGF-1 and stimulate verrucous keratinocyte proliferation."
            },
            "lunch": {
                "title": f"Metabolic Balance Plate: {base['lunch']['title']} with Apple Cider Vinegar",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, raw apple cider vinegar dressing",
                "action": "Improves insulin receptor sensitivity and downregulates FGFR3-mediated epidermal hyperkeratosis."
            },
            "dinner": {
                "title": f"Keratin Balance Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Provides monounsaturated fatty acids to maintain smooth stratum corneum desquamation."
            },
            "hydration": base["hydration"],
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    elif cond == "df":
        # Target: Vitamin C, L-proline, Gotu Kola, Zinc
        return {
            "breakfast": {
                "title": f"Collagen Remodeling Morning: {base['breakfast']['title']} with Kiwi & Seeds",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, kiwi slices (Vitamin C), raw pumpkin seeds (zinc)",
                "action": "Supplies essential cofactors for lysyl and prolyl hydroxylase in physiological collagen synthesis."
            },
            "lunch": {
                "title": f"Connective Tissue Plate: {base['lunch']['title']}",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, bell peppers, bone broth or clean protein",
                "action": "Modulates type I vs type III collagen synthesis, inhibiting excessive localized dermal fibrosis."
            },
            "dinner": {
                "title": f"Dermal Repair Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Normalizes extracellular matrix remodeling around dense fibrous nodules."
            },
            "hydration": {
                "title": "Centella Asiatica (Gotu Kola) Herbal Tea",
                "timing": "Afternoon",
                "ingredients": "Dried Gotu Kola leaves, hot spring water",
                "action": "Asiaticoside modulates fibroblast proliferation and prevents aberrant hypertrophic scarring."
            },
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    elif cond == "acne":
        return {
            "breakfast": {
                "title": f"Low-GI Sebum Balancing Morning: {base['breakfast']['title'].split('with')[0]} with Pumpkin Seeds & Spearmint",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, raw pumpkin seeds (bioavailable zinc), organic spearmint tea",
                "action": "Inhibits 5-alpha reductase to decrease dihydrotestosterone and blunts insulin-driven sebum hypersecretion."
            },
            "lunch": {
                "title": f"Sebum-Regulating Zinc Plate: {base['lunch']['title']} with Cruciferous Greens",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, broccoli florets or steamed cabbage (indole-3-carbinol), zinc-rich lentils",
                "action": "Modulates androgen metabolism, accelerates follicular healing, and prevents hyperkeratinization of pilosebaceous ducts."
            },
            "dinner": {
                "title": f"Microbiome-Barrier Recovery Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Supports overnight epidermal barrier re-acidification and inhibits Cutibacterium acnes biofilm proliferation."
            },
            "hydration": {
                "title": "Organic Spearmint & Green Tea Infusion",
                "timing": "Morning and mid-afternoon",
                "ingredients": "Organic spearmint leaves, sencha green tea leaves, hot filtered water",
                "action": "Synergistic EGCG and anti-androgenic terpenes lower free circulating androgens and diminish sebum oxidation."
            },
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    elif cond == "ecz":
        return {
            "breakfast": {
                "title": f"Ceramide Barrier Morning: {base['breakfast']['title'].split('with')[0]} with Chia & Quercetin Berries",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, cold-milled chia/flaxseeds (ALA omega-3), quercetin-rich blueberries or apple slices",
                "action": "Supplies structural precursor fatty acids for ceramides and stabilizes mast cell membranes to quell morning pruritus."
            },
            "lunch": {
                "title": f"Histamine-Calming Anti-Pruritic Plate: {base['lunch']['title']} with Probiotic Greens",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, low-histamine greens, cold-pressed virgin olive or coconut oil",
                "action": "Inhibits Th2 cytokine transcription (IL-4, IL-13) and accelerates filaggrin peptide barrier regeneration."
            },
            "dinner": {
                "title": f"Stratum Corneum Restorative Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Promotes nocturnal lipid bilayer rebuilding within stratum corneum and prevents transepidermal water loss (TEWL)."
            },
            "hydration": {
                "title": "Cool Chamomile & Rooibos Infusion",
                "timing": "Throughout afternoon and before sleep",
                "ingredients": "German chamomile blossoms, red rooibos leaves, cool or lukewarm water",
                "action": "Apigenin and aspalathin dampen neurogenic itch pathways and promote restful, non-scratching sleep."
            },
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    elif cond == "psor":
        return {
            "breakfast": {
                "title": f"Systemic Anti-Inflammatory Morning: {base['breakfast']['title'].split('with')[0]} with Golden Turmeric & Walnuts",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, cracked black pepper with grated fresh turmeric, raw walnuts (high ALA)",
                "action": "Downregulates NF-kB and IL-23/Th17 axis to arrest excessive, uncoordinated epidermal keratinocyte mitosis."
            },
            "lunch": {
                "title": f"Cytokine-Quenching Omega-3 Plate: {base['lunch']['title']} with Steamed Leafy Greens",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, deep leafy greens (folate), virgin olive oil, cold-water fish or rich seed mix",
                "action": "Suppresses leukotriene B4 and TNF-alpha, reducing the erythema, induration, and desquamation of psoriatic plaques."
            },
            "dinner": {
                "title": f"Autoimmune Soothing Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Provides sulforaphane and sulfur-containing amino acids to maintain mucosal and cutaneous gut-skin axis tolerance."
            },
            "hydration": {
                "title": "Warm Ashwagandha & Holy Basil (Tulsi) Tea",
                "timing": "Late afternoon and evening",
                "ingredients": "Withania somnifera (ashwagandha root), Rama tulsi leaves, warm spring water",
                "action": "Balances cortisol and HPA-axis activation, eliminating psychological stress as a flare-up trigger."
            },
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    elif cond == "vit":
        return {
            "breakfast": {
                "title": f"Melanocyte Photoprotective Morning: {base['breakfast']['title'].split('with')[0]} with Papaya & Pumpkin Seeds",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, ripe papaya slices (lycopene + carotenoids), pumpkin seeds (copper and zinc)",
                "action": "Provides essential tyrosinase enzymatic cofactors and protects follicular melanocyte stem cells from oxidative cytolysis."
            },
            "lunch": {
                "title": f"Mitochondrial Redox Plate: {base['lunch']['title']} with Chickpeas & Leafy Greens",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, dark leafy greens (methyl-folate), chickpeas or lentils, cold-pressed seed oil",
                "action": "Elevates cellular glutathione reserves and halts CD8+ autoreactive cytotoxic T-cell attacks against epidermal melanocytes."
            },
            "dinner": {
                "title": f"Repigmentation Restorative Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Stimulates microenvironment signaling for dormant hair follicle outer root sheath melanocyte migration."
            },
            "hydration": {
                "title": "Ginkgo Biloba & Rooibos Infusion",
                "timing": "Mid-morning and early evening",
                "ingredients": "Standardized Ginkgo Biloba extract/leaves, organic green rooibos, hot water",
                "action": "Flavonoid glycosides neutralize hydrogen peroxide accumulation in depigmented lesional epidermis."
            },
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    elif cond == "ros":
        return {
            "breakfast": {
                "title": f"Anti-Erythema Cooling Morning: {base['breakfast']['title'].split('with')[0]} with Blueberries & Cucumber",
                "timing": base["breakfast"]["timing"],
                "ingredients": f"{base['breakfast']['ingredients']}, fresh cucumber slices, wild blueberries, room-temperature flax milk",
                "action": "Anthocyanins and cooling plant lignans stabilize neurovascular receptors and prevent early morning facial flushing."
            },
            "lunch": {
                "title": f"Neuro-Vascular Calming Plate: {base['lunch']['title']} with Steamed Squash (Non-Spicy)",
                "timing": base["lunch"]["timing"],
                "ingredients": f"{base['lunch']['ingredients']}, steamed yellow squash, avocado, completely free of hot spices, chillies, or vinegar",
                "action": "Prevents TRPV1 transient receptor potential channel activation, reducing superficial facial telangiectasia."
            },
            "dinner": {
                "title": f"Capillary Stabilizing Dinner: {base['dinner']['title']}",
                "timing": base["dinner"]["timing"],
                "ingredients": base["dinner"]["ingredients"],
                "action": "Supplies bioavailable rutin and quercetin to strengthen microcapillary endothelia without vasodilating triggers."
            },
            "hydration": {
                "title": "Chilled Peppermint & Hibiscus Cooler (Non-Scalding)",
                "timing": "Throughout afternoon, strictly chilled or lukewarm",
                "ingredients": "Dried hibiscus calyces, peppermint leaves, cool spring water, splash of pomegranate juice",
                "action": "Cooling polyphenols constrict dilated dermal facial capillaries and downregulate cathelicidin antimicrobial peptide LL-37."
            },
            "grocery_list": base.get("grocery_list", {}),
            "local_substitutions": base.get("local_substitutions", [])
        }

    else:
        # Default / nv (Melanocytic Nevi)
        return base
