/**
 * DermAI 360 - Client-Side Clinical Age-Stratified Medical & Nutritional Intelligence Engine
 * Provides immediate browser-side age protocol resolution for 12 skin conditions & 5 demographics.
 */

window.getAgeGroupInfo = function(age) {
  const a = parseFloat(age) || 28;
  if (a < 13) return { key: 'pediatric', label: 'Pediatric (Child 0–12 yrs)', icon: '👶', name: 'Child' };
  if (a < 20) return { key: 'adolescent', label: 'Adolescent / Teenage (13–19 yrs)', icon: '🧑‍🎓', name: 'Teen' };
  if (a < 40) return { key: 'young_adult', label: 'Young Adult (20–39 yrs)', icon: '🧑', name: 'Young Adult' };
  if (a < 65) return { key: 'adult', label: 'Adult / Mid-Life (40–64 yrs)', icon: '👨‍💼', name: 'Mid-Life' };
  return { key: 'geriatric', label: 'Senior / Geriatric (65+ yrs)', icon: '👴', name: 'Senior' };
};

window.CLIENT_AGE_MATRIX = {
  acne: {
    pediatric: {
      medications: {
        first_line: "Topical Benzoyl Peroxide 2.5% aqueous wash/gel daily + Clindamycin 1% topical lotion.",
        second_line: "Topical Adapalene 0.1% cream (nightly for children ≥9 years).",
        contraindications: "STRICTLY AVOID oral Tetracyclines/Doxycycline under 8 years (causes permanent enamel hypoplasia and teeth staining). Avoid high-strength chemical peels and oral isotretinoin.",
        dosage_guidelines: "Apply pea-sized amount over entire facial field (not just spot-treating). Use gentle non-comedogenic foaming cleanser.",
        safety_monitoring: "Monitor for skin irritation or contact dermatitis; titrate topical frequency to alternate nights if erythema occurs."
      },
      diet: {
        focus: "Pediatric Insulin Sensitivity & Barrier Lipids",
        key_micronutrients: "Zinc Gluconate (10–15 mg/day), Omega-3 DHA (250 mg), Vitamin A (food-derived beta-carotene).",
        superfoods: ["Pure pumpkin seed butter", "Wild salmon or flaxseed puree", "Blueberry antioxidant oatmeal"],
        foods_to_restrict: ["High-fructose corn syrup beverages", "Skim milk / non-fat dairy", "Ultra-processed sugary breakfast cereals"]
      }
    },
    adolescent: {
      medications: {
        first_line: "Fixed-dose combination Adapalene 0.1% + Benzoyl Peroxide 2.5% (Epiduo) nightly + Clindamycin 1% gel AM.",
        second_line: "Oral Doxycycline Hyclate 100mg daily (with food and a full glass of water, maximum 12 weeks to limit resistance) OR oral Isotretinoin (0.5–1.0 mg/kg/day) for severe nodulocystic/scarring acne.",
        contraindications: "Isotretinoin requires strict iPLEDGE / pregnancy prevention program due to extreme teratogenicity. Avoid lying down for 30 min after doxycycline to prevent pill-induced esophagitis.",
        dosage_guidelines: "Oral antibiotics MUST always be paired with topical Benzoyl Peroxide to prevent bacterial resistance.",
        safety_monitoring: "Monthly fasting lipid panel, liver function tests (LFTs), and qualitative hCG if on oral isotretinoin. Monitor mood and suicidal ideation."
      },
      diet: {
        focus: "IGF-1 & Androgen Downregulation Protocol",
        key_micronutrients: "Zinc Picolinate (30 mg/day), EGCG Green Tea Extract (300 mg), Chromium (200 mcg), Spearmint (anti-androgen).",
        superfoods: ["Sprouted pumpkin seeds (high bioavailable zinc)", "Organic unsweetened matcha / spearmint tea", "Cruciferous broccoli sprouts (diindolylmethane/DIM)"],
        foods_to_restrict: ["Whey protein isolate powders/shakes (potent mTORC1 trigger)", "Skim and low-fat commercial dairy", "High glycemic white bakery carbs"]
      }
    },
    young_adult: {
      medications: {
        first_line: "Topical Tretinoin 0.05% or Tazarotene 0.05% cream nightly + Topical Dapsone 5% / 7.5% gel (ideal for adult female hormonal acne).",
        second_line: "Oral Spironolactone (50–100 mg daily for adult females) OR Combined Oral Contraceptives (FDA-approved ethinyl estradiol + drospirenone/norgestimate) OR oral Sarecycline 60–150 mg.",
        contraindications: "Spironolactone is contraindicated in males (gynecomastia risk) and pregnancy (feminization of male fetus). Do not use Tazarotene/Retinoids in pregnancy.",
        dosage_guidelines: "Tretinoin applied 20 minutes after cleansing to dry skin; follow with ceramide-based non-comedogenic moisturizer to counteract retinization.",
        safety_monitoring: "Check serum potassium periodically if starting Spironolactone, particularly in patients with borderline renal function."
      },
      diet: {
        focus: "Hormonal Equilibrium & Liver Phase II Clearance",
        key_micronutrients: "Diindolylmethane (DIM 100 mg), Inositol / Myo-inositol (2g), Omega-3 EPA/DHA (2000 mg), Berberine (500 mg).",
        superfoods: ["Avocado and extra virgin cold-pressed olive oil", "Fermented kimchi and wild Alaskan salmon", "Ground organic golden flaxseeds"],
        foods_to_restrict: ["Commercial whey protein bars", "High-glycemic cocktails and refined sugars", "Pro-inflammatory hydrogenated seed oils"]
      }
    },
    adult: {
      medications: {
        first_line: "Topical Azelaic Acid 15% gel / 20% cream BID + Topical Tretinoin 0.025% cream at night (addresses acne and concurrent photoaging/hyperpigmentation).",
        second_line: "Oral Spironolactone (25–50 mg) for persistent submandibular jawline adult acne OR low-dose anti-inflammatory sub-antimicrobial doxycycline (40 mg modified release).",
        contraindications: "Screen for concurrent perioral dermatitis or rosacea; avoid harsh salicylic scrubs that compromise mature lipid barrier.",
        dosage_guidelines: "Prioritize gentle hydrating lipid vehicles over alcohol-based gels to avoid accentuating fine lines.",
        safety_monitoring: "Blood pressure and potassium monitoring if on spironolactone; annual skin cancer screening."
      },
      diet: {
        focus: "Anti-Inflammatory Barrier & Cellular Longevity",
        key_micronutrients: "Nicotinamide (500 mg BID), CoQ10 (100 mg), Resveratrol (100 mg), Curcumin with piperine.",
        superfoods: ["Turmeric-curcumin golden milk with coconut oil", "Deep colorful berries (blackberries, wild blueberries)", "Steamed artichokes & organic dandelion greens"],
        foods_to_restrict: ["Ultra-processed late-night snacks", "Excess alcohol (triggers facial vasodilation and sebum flares)", "Refined trans-fats"]
      }
    },
    geriatric: {
      medications: {
        first_line: "Topical Azelaic Acid 10%–15% cream OR gentle low-concentration Adapalene 0.1% cream 2–3 nights weekly in a heavy ceramide vehicle.",
        second_line: "Topical Clindamycin 1% lotion. Avoid systemic antibiotics and systemic retinoids unless severe and under specialist care.",
        contraindications: "Avoid drying alcohol/astringent formulations. Geriatric skin is prone to xerosis, skin tearing, and delayed re-epithelialization.",
        dosage_guidelines: "Layer moisturizer FIRST ('sandwich technique') before applying mild topical retinoids to prevent xerotic dermatitis.",
        safety_monitoring: "Check skin fragility, purpura, and evaluate for Favre-Racouchot syndrome (nodular elastosis with cysts/comedones)."
      },
      diet: {
        focus: "Hydration, Sarcopenia Prevention & Barrier Regeneration",
        key_micronutrients: "Bioactive Collagen Peptides (10g), Vitamin C (500 mg), Zinc Bisglycinate (15 mg), Vitamin D3 (2000 IU).",
        superfoods: ["Slow-simmered bone broth with sea vegetables", "Soft stewed wild salmon with olive oil", "Hydrating chia seed compote with papaya"],
        foods_to_restrict: ["Dehydrating caffeinated excess", "Excess dietary sodium", "Hard-to-digest dry fried foods"]
      }
    }
  },

  ecz: {
    pediatric: {
      medications: {
        first_line: "Liberal thick barrier emollients (50/50 white soft paraffin/liquid paraffin) applied within 3 min of bathing + Topical Hydrocortisone 1%–2.5% or Desonide 0.05% ointment for acute flares.",
        second_line: "Topical Calcineurin Inhibitors: Pimecrolimus 1% cream or Tacrolimus 0.03% ointment (for children ≥2 years, steroid-sparing on face/folds).",
        contraindications: "Avoid potent Class I/II fluorinated topical steroids (risk of cutaneous atrophy, striae, and systemic adrenal axis suppression on thin infant skin). Never use oral steroids.",
        dosage_guidelines: "Fingertip Unit (FTU) dosing method. Bathe in lukewarm water for max 5–10 mins; pat dry without rubbing.",
        safety_monitoring: "Watch for signs of secondary bacterial (Staphylococcus aureus honey-crusting) or viral infection (Eczema herpeticum - emergency)."
      },
      diet: {
        focus: "Gut-Skin Axis Diversity & Filaggrin Lipogenesis",
        key_micronutrients: "Lactobacillus rhamnosus GG probiotic (10 billion CFU), Omega-3 DHA/EPA (500 mg), Vitamin D3 (800 IU).",
        superfoods: ["Organic whole-milk kefir or coconut yogurt", "Mashed avocado with cold-pressed olive oil", "Pureed wild salmon & butternut squash"],
        foods_to_restrict: ["Artificial food colorings (tartrazine, sunset yellow)", "Refined sugary snacks", "Common pediatric allergens only if clinically confirmed"]
      }
    },
    adolescent: {
      medications: {
        first_line: "Mid-potency topical steroids (Triamcinolone acetonide 0.1% ointment) for body + Tacrolimus 0.03% or 0.1% ointment for face/neck/flexures.",
        second_line: "Subcutaneous Dupilumab (Dupixent) 200mg or 300mg every 2 weeks (for moderate-to-severe eczema refractory to topicals; approved for ages 6+).",
        contraindications: "Avoid continuous uninterrupted topical steroid use (>2 weeks) without drug holidays to prevent tachyphylaxis and rebound.",
        dosage_guidelines: "Apply topical steroid to active erythematous plaques; maintain unaffected skin with barrier ceramide creams.",
        safety_monitoring: "Screen for allergic conjunctivitis/blepharitis on Dupilumab. Monitor mental health and sleep disturbance caused by intense itch."
      },
      diet: {
        focus: "Th2 Cytokine (IL-4 / IL-13) Suppression Protocol",
        key_micronutrients: "Quercetin (500 mg), Bromelain (200 mg), Omega-3 Fatty Acids (2000 mg), Zinc (25 mg).",
        superfoods: ["Wild oily sardines / mackerel", "Purple cabbage with raw apple cider vinegar", "Steeped chamomile & organic green tea"],
        foods_to_restrict: ["Ultra-processed junk food and refined vegetable oils", "High-histamine aged cheeses and cured meats", "Commercial energy drinks"]
      }
    },
    young_adult: {
      medications: {
        first_line: "Topical Betamethasone valerate 0.1% or Mometasone furoate 0.1% ointment for body + Crisaborole 2% ointment (non-steroidal PDE4 inhibitor) or Tacrolimus 0.1% for delicate skin.",
        second_line: "Targeted biologic Dupilumab 300mg Q2W OR Tralokinumab (IL-13 inhibitor) OR oral JAK inhibitor (Upadacitinib 15mg or Abrocitinib 100mg) for severe cases.",
        contraindications: "JAK inhibitors carry black box warnings for thrombosis, cardiovascular events, and serious infections. Avoid live vaccines during systemic biologic therapy.",
        dosage_guidelines: "Use 'soak and seal' method: 15-minute lukewarm bath followed immediately by ointment application within 3 minutes.",
        safety_monitoring: "Baseline TB screening, hepatitis B/C, and routine CBC/lipids if starting oral JAK inhibitors."
      },
      diet: {
        focus: "Mast Cell Stabilization & Histamine Clearance",
        key_micronutrients: "Vitamin C (1000 mg), Quercetin Dihydrate (1000 mg), Magnesium Glycinate (400 mg), Probiotic spore-forming organisms.",
        superfoods: ["Extra virgin olive oil (high oleocanthal)", "Fermented prebiotic foods (sauerkraut, natto)", "Fresh wild caught cod & organic broccoli"],
        foods_to_restrict: ["Histamine liberators (aged wine, cured sausages)", "Artificial artificial sweeteners and emulsifiers", "Excessive nightshade vegetables if reactive"]
      }
    },
    adult: {
      medications: {
        first_line: "Mometasone furoate 0.1% ointment pulsed 2–3 days/week + Crisaborole 2% ointment OR Roflumilast 0.15% cream.",
        second_line: "Dupilumab or systemic oral Methotrexate (10–15 mg weekly with 5mg folic acid) OR oral Cyclosporine short-course for crisis control.",
        contraindications: "Caution with systemic immunosuppressants in patients with hypertension, hepatic dysfunction, or chronic latent infections.",
        dosage_guidelines: "Always prefer ointment vehicles over creams to prevent stinging from preservative emulsifiers in dry mature skin.",
        safety_monitoring: "Blood pressure and serum creatinine monitoring every 2–4 weeks if using Cyclosporine; liver function with Methotrexate."
      },
      diet: {
        focus: "Systemic Anti-Inflammatory & Lipid Membrane Restoration",
        key_micronutrients: "Evening Primrose Oil (GLA 500 mg), CoQ10 (150 mg), Curcumin C3 Complex (1000 mg), L-Glutamine (5g).",
        superfoods: ["Flaxseed and chia seed puddings", "Wild salmon with steamed asparagus", "Turmeric and ginger golden root elixirs"],
        foods_to_restrict: ["Processed red meats and bacon", "Refined seed and vegetable oils (corn, canola, soybean)", "Excess commercial alcohol"]
      }
    },
    geriatric: {
      medications: {
        first_line: "Ultra-rich ceramide/cholesterol/free fatty acid barrier creams applied 3–4 times daily + Low-to-mild potency topical steroids (Desonide 0.05% or Alclometasone 0.05%) used strictly short-term.",
        second_line: "Topical Tacrolimus 0.03% or Pimecrolimus 1% ointment. Subcutaneous Dupilumab if severe, with individualized dose scheduling.",
        contraindications: "AVOID SEDATING 1st-generation antihistamines (Hydroxyzine, Diphenhydramine) due to extreme risk of falls, delirium, urinary retention, and cognitive impairment. Avoid potent steroids on paper-thin elderly skin (causes purpura and tears).",
        dosage_guidelines: "Apply emollients in the direction of hair growth to prevent steroid/emollient-induced folliculitis.",
        safety_monitoring: "Check for skin tears, senile purpura, cutaneous atrophy, and screen for occult drug-induced eczema (e.g. calcium channel blockers, diuretics)."
      },
      diet: {
        focus: "Xerosis Prevention, Sarcopenia & Microvascular Hydration",
        key_micronutrients: "Hydration Electrolytes, Hydrolyzed Marine Collagen (10g), Vitamin D3 + K2 (2000 IU), Vitamin B12 (1000 mcg).",
        superfoods: ["Nutrient-rich bone broths with softened root vegetables", "Pureed avocado soups with extra virgin olive oil", "Soft stewed berries with full-fat Greek yogurt"],
        foods_to_restrict: ["Excess diuretic beverages (black tea/coffee without water)", "High sodium preserved snacks", "Hard, dry foods that cause dehydration"]
      }
    }
  },

  psor: {
    pediatric: {
      medications: {
        first_line: "Topical Calcipotriene 0.005% ointment combined with mild topical corticosteroid (Hydrocortisone 2.5% or Desonide 0.05%).",
        second_line: "Narrow-band UVB (NB-UVB) phototherapy. For severe pediatric plaque psoriasis (≥6 yrs), Etanercept (Enbrel 0.8 mg/kg weekly) or Ixekizumab.",
        contraindications: "Avoid oral systemic corticosteroids (prednisone) due to severe risk of triggering life-threatening generalized pustular psoriasis on withdrawal.",
        dosage_guidelines: "Calcipotriene maximum dose 50g/week in children under 12 to avoid hypercalcemia.",
        safety_monitoring: "Serum calcium levels if using high surface area calcipotriene; pediatric growth curves."
      },
      diet: {
        focus: "Systemic Anti-Inflammatory & Metabolic Balance",
        key_micronutrients: "Vitamin D3 (1000 IU/day), Omega-3 Fish Oil (1000 mg), Zinc (15 mg), Prebiotic inulin.",
        superfoods: ["Wild salmon fish cakes", "Colorful fruit and vegetable smoothies with flax", "Whole fat yogurt with honey"],
        foods_to_restrict: ["Ultra-processed snacks", "Gluten-rich refined white flour goods", "Sugary sodas"]
      }
    },
    adolescent: {
      medications: {
        first_line: "Fixed-combination Calcipotriene + Betamethasone dipropionate (Enstilar foam or Taclonex suspension) once daily for up to 4 weeks.",
        second_line: "Biologics: Secukinumab (IL-17A inhibitor, approved for pediatric/adolescent psoriasis ≥6 yrs) OR Adalimumab 40mg biweekly.",
        contraindications: "Never abruptly taper or discontinue high-dose systemic steroids (pustular flare risk). Check latent TB before starting any biologic.",
        dosage_guidelines: "Shake foam can vigorously; apply directly to plaque scales without rubbing excessively.",
        safety_monitoring: "Annual QuantiFERON-TB Gold test, baseline viral hepatitis panel, and assessment for psoriatic arthritis (joint stiffness/dactylitis)."
      },
      diet: {
        focus: "Th17 / IL-23 Inflammatory Cascade Inhibition",
        key_micronutrients: "Curcumin with piperine (1000 mg), Omega-3 EPA/DHA (2500 mg), Vitamin D3 (2000 IU), Magnesium.",
        superfoods: ["Steamed wild salmon and rainbow trout", "Steamed leafy greens (kale, Swiss chard) with olive oil", "Turmeric, black pepper, and ginger elixirs"],
        foods_to_restrict: ["Fried fast foods and trans-fats", "Refined wheat/gluten products (often triggers symptom flares)", "Sugary energy drinks"]
      }
    },
    young_adult: {
      medications: {
        first_line: "Fixed-dose Calcipotriene/Betamethasone foam + Topical Roflumilast 0.3% cream (Zoryve, once daily non-steroidal PDE4 inhibitor).",
        second_line: "Targeted modern biologics: IL-23 inhibitors (Guselkumab/Risankizumab Q8-12 weeks) OR IL-17 inhibitors (Ixekizumab/Bimekizumab) OR oral Deucravacitinib (TYK2 inhibitor).",
        contraindications: "IL-17 inhibitors (Secukinumab, Ixekizumab) can exacerbate inflammatory bowel disease (Crohn's/ulcerative colitis). Screen gastrointestinal history.",
        dosage_guidelines: "Rotate injection sites (thighs, abdomen, upper arm); store biologics refrigerated between 2°C–8°C.",
        safety_monitoring: "Screen for metabolic syndrome (blood pressure, fasting glucose, lipid profile) as psoriasis is an independent cardiovascular risk factor."
      },
      diet: {
        focus: "Cardiometabolic & Endothelial Anti-Inflammatory Protocol",
        key_micronutrients: "High-dose Omega-3 (3000 mg EPA/DHA), Curcumin (1500 mg), Resveratrol (200 mg), CoQ10 (200 mg).",
        superfoods: ["Extra virgin polyphenol olive oil (2 tbsp/day)", "Wild sardines and wild Atlantic mackerel", "Raw organic walnuts and chia seeds"],
        foods_to_restrict: ["Alcohol (potent trigger for systemic psoriasis cascades)", "Red meat high in arachidonic acid", "Gluten-containing processed grains"]
      }
    },
    adult: {
      medications: {
        first_line: "Topical Tapinarof 1% cream (Vtama, AhR agonist) once daily OR Roflumilast 0.3% cream + targeted pulsed Class I topical steroids.",
        second_line: "IL-23 Biologics (Risankizumab, Guselkumab) offering >85% PASI-90 clearance OR oral Apremilast (30mg BID) for patients preferring oral therapy.",
        contraindications: "Apremilast is associated with depression and weight loss; dose titrate carefully over initial 5 days to minimize GI nausea.",
        dosage_guidelines: "Combine topical therapies with regular physical activity and weight management to optimize biologic pharmacokinetics.",
        safety_monitoring: "Regular joint assessments for Psoriatic Arthritis (CASPAR criteria); screen for non-alcoholic fatty liver disease (NAFLD)."
      },
      diet: {
        focus: "Arachidonic Acid Downregulation & Visceral Adiposity Reduction",
        key_micronutrients: "Alpha-Lipoic Acid (300 mg), Berberine (1000 mg), Vitamin D3 (3000 IU), Zinc Picolinate (30 mg).",
        superfoods: ["Mediterranean green salads with arugula, radish & olive oil", "Shiitake and maitake medicinal mushrooms", "Steamed wild cod and organic crucifers"],
        foods_to_restrict: ["High-glycemic processed starches", "Commercial beer, wine, and spirits", "High-fat dairy and grain-fed beef"]
      }
    },
    geriatric: {
      medications: {
        first_line: "Topical Roflumilast 0.3% cream OR Tapinarof 1% cream (both non-steroidal, safe for thin geriatric skin with zero atrophy risk) + Calcipotriene ointment.",
        second_line: "IL-23 Biologics (Risankizumab / Guselkumab) have the cleanest safety profile in seniors with minimal injection frequency (once every 8–12 weeks) and no organ toxicity.",
        contraindications: "AVOID systemic Methotrexate (high risk of bone marrow suppression and renal failure in seniors) and Cyclosporine (nephrotoxicity/hypertension). Avoid prolonged potent steroids (senile purpura risk).",
        dosage_guidelines: "Inquire about caregiver assistance if patient has difficulty reaching dorsal or lower leg plaques.",
        safety_monitoring: "Check renal function (eGFR), monitor for signs of occult infections, review all concomitant cardiology/anticoagulant medications."
      },
      diet: {
        focus: "Microvascular Health, Renal Sparing & Gentle Anti-Inflammatory Nutrition",
        key_micronutrients: "Hydrolyzed Collagen (10g), Vitamin D3 + K2 (2000 IU), Magnesium Citrate (250 mg), Tart cherry extract.",
        superfoods: ["Pureed vegetable soups with turmeric and olive oil", "Steamed soft salmon fillets with sweet potato", "Warm golden almond milk with cinnamon and nutmeg"],
        foods_to_restrict: ["Dehydrating salty snacks", "Heavy inflammatory processed sausages", "Excess sugary desserts"]
      }
    }
  },

  akiec: {
    pediatric: {
      medications: {
        first_line: "Extremely rare in children (investigate Xeroderma Pigmentosum). Strict total UV avoidance, physical mineral sunscreens (Zinc oxide 20%+ SPF 50+).",
        second_line: "Lesion-directed gentle liquid nitrogen cryotherapy under pediatric dermatological supervision.",
        contraindications: "Avoid aggressive 5-FU field therapy in pediatric age unless biopsy-proven and geneticist approved.",
        dosage_guidelines: "Broad-brimmed UPF 50+ clothing and UV-blocking sunglasses.",
        safety_monitoring: "Full-body dermatoscopy mapping every 3–6 months."
      },
      diet: {
        focus: "Endogenous DNA Photoprotection & Excision Repair",
        key_micronutrients: "Oral Nicotinamide (250 mg), Beta-carotene from food, Vitamin C.",
        superfoods: ["Cooked tomato paste (lycopene)", "Carrot and sweet potato puree", "Wild blueberries"],
        foods_to_restrict: ["Pro-oxidant fried foods", "Refined sugars"]
      }
    },
    adolescent: {
      medications: {
        first_line: "Physical mineral SPF 50+ daily + Lesion-directed liquid nitrogen cryotherapy (5–10 second freeze-thaw cycle).",
        second_line: "Topical Imiquimod 3.75% cream (applied 2 weeks on, 2 weeks off) or Diclofenac 3% gel in 2.5% hyaluronan.",
        contraindications: "Avoid sunbed tanning and deliberate UV tanning without photoprotection.",
        dosage_guidelines: "Apply sunscreen 15 minutes before UV exposure; reapply every 90 minutes outdoors.",
        safety_monitoring: "Educate on ABCDE self-exams and evolution of rough, persistent scaly spots."
      },
      diet: {
        focus: "Free Radical Quenching & UV Nucleotide Repair",
        key_micronutrients: "Oral Nicotinamide (Vitamin B3 500 mg daily), Astaxanthin (4 mg), Vitamin E (mixed tocopherols).",
        superfoods: ["Wild Alaskan sockeye salmon (high astaxanthin)", "Cooked organic tomato sauces (bioavailable lycopene)", "Organic matcha green tea"],
        foods_to_restrict: ["Tanning salon acceleration gummies", "Hydrogenated vegetable oils", "High-sugar sodas"]
      }
    },
    young_adult: {
      medications: {
        first_line: "Cryotherapy with liquid nitrogen + Photodynamic Therapy (PDT) with 5-aminolevulinic acid (ALA) and blue/red light activation.",
        second_line: "Topical Fluorouracil 5% cream (5-FU) or combination 5-FU 0.5% + Salicylic Acid 10% for hyperkeratotic lesions.",
        contraindications: "5-FU is contraindicated in dihydropyrimidine dehydrogenase (DPD) deficiency and pregnancy. Avoid application near eyelids and lips without protection.",
        dosage_guidelines: "Expect brisk inflammatory reaction (erythema, erosion, crusting) during 5-FU; this is the therapeutic endpoint indicating clearance.",
        safety_monitoring: "Annual full-body skin examination; monitor treated fields for non-healing indurated ulcers (suspect SCC)."
      },
      diet: {
        focus: "NEJM DNA Excision Repair & Nrf2 Antioxidant Activation",
        key_micronutrients: "Nicotinamide (500 mg BID — proven in Phase 3 NEJM trials to reduce new non-melanoma skin lesions by 23%), Polypodium leucotomos extract (480 mg), Lycopene (15 mg).",
        superfoods: ["Broccoli sprouts (sulforaphane)", "Stewed vine-ripened tomatoes in extra virgin olive oil", "Organic dark berries (anthocyanins)"],
        foods_to_restrict: ["Charred barbecue meats (heterocyclic amines)", "Excessive alcohol consumption", "Refined seed oils"]
      }
    },
    adult: {
      medications: {
        first_line: "Field cancerization therapy: 5-FU 5% cream applied BID for 2–4 weeks OR combination 5-FU + Calcipotriol cream twice daily for 4 days (accelerated immune clearance).",
        second_line: "Photodynamic Therapy (PDT) with Daylight PDT or Red Light PDT OR Topical Imiquimod 5% cream 2 nights/week for 16 weeks.",
        contraindications: "Do not treat suspected invasive Squamous Cell Carcinoma (SCC) with topical field therapy alone; mandatory biopsy required.",
        dosage_guidelines: "Apply thin film to entire affected cosmetic field (scalp, forehead, forearms). Soothe post-treatment with pure white petrolatum.",
        safety_monitoring: "Bi-annual skin exams for high-risk patients. Immediate biopsy for any lesion with induration, tenderness, or rapid growth."
      },
      diet: {
        focus: "Cutaneous Photocarcinogenesis Defense Protocol",
        key_micronutrients: "Oral Nicotinamide (500 mg BID), Resveratrol (100 mg), Curcumin C3 (1000 mg), Astaxanthin (8 mg), Vitamin D3 (2000 IU).",
        superfoods: ["Pomegranate arils and pure pomegranate extract (ellagic acid)", "Steamed cruciferous medley (kale, broccoli, Brussels sprouts)", "Wild Alaskan sockeye salmon & mackerel"],
        foods_to_restrict: ["Commercial processed meats with nitrates", "Excessive alcohol intake", "High-glycemic bakery carbohydrates"]
      }
    },
    geriatric: {
      medications: {
        first_line: "Tirabanibulin 1% ointment (Klisyri, modern tubulin inhibitor applied once daily for 5 consecutive days — gentle with low ulceration risk in seniors) OR lesion-directed liquid nitrogen cryotherapy.",
        second_line: "Photodynamic Therapy (PDT) OR Topical Diclofenac 3% in hyaluronic acid gel for 60–90 days (very low irritation profile for frail skin).",
        contraindications: "Avoid aggressive prolonged 4-week 5-FU courses on frail lower legs of elderly patients due to risk of secondary non-healing stasis ulcers.",
        dosage_guidelines: "Tirabanibulin single-dose packet applied once daily at bedtime to up to 25 cm² area on face or scalp for 5 days only.",
        safety_monitoring: "Examine for cutaneous horn formation, invasive SCC transformation, and monitor healing over atrophic dermal tissue."
      },
      diet: {
        focus: "Cellular Longevity, Epigenetic Repair & Wound Healing",
        key_micronutrients: "Oral Nicotinamide (500 mg BID), Hydrolyzed Marine Collagen (10g), Zinc Bisglycinate (20 mg), Vitamin C (500 mg), Vitamin D3 (2000 IU).",
        superfoods: ["Slow-cooked vegetable and fish stew with olive oil", "Soft steamed carrots, squash, and sweet potato with grass-fed butter", "Pureed antioxidant berry compote with Greek yogurt"],
        foods_to_restrict: ["Heavily salted cured meats", "Hard dry foods that compromise oral intake", "Excess commercial sugar"]
      }
    }
  },

  bcc: {
    pediatric: {
      medications: {
        first_line: "Rare in childhood (evaluate for Gorlin syndrome / Nevoid Basal Cell Carcinoma Syndrome). Surgical excision with primary closure under pediatric surgery.",
        second_line: "Mohs micrographic surgery for facial/periorbital lesions.",
        contraindications: "Avoid therapeutic ionizing radiation (causes secondary neoplasms in Gorlin syndrome).",
        dosage_guidelines: "Histologically controlled margins are mandatory.",
        safety_monitoring: "Genetic counseling, odontogenic keratocyst screening, whole-body skin mapping."
      },
      diet: {
        focus: "Genetic Stability & Total UV Shielding",
        key_micronutrients: "Oral Nicotinamide, Vitamin A/Carotenoids, Zinc, Vitamin C.",
        superfoods: ["Cooked tomato lycopene puree", "Organic broccoli sprouts", "Wild salmon mash"],
        foods_to_restrict: ["Ultra-processed snack foods", "Refined inflammatory oils"]
      }
    },
    adolescent: {
      medications: {
        first_line: "Complete surgical excision with 4mm margins OR Mohs micrographic surgery for critical aesthetic zones (nose, eyelids, lips).",
        second_line: "Topical Imiquimod 5% cream (strictly for superficial BCC only, 5 nights/week for 6 weeks, confirmed by biopsy).",
        contraindications: "Never treat nodular, morpheaform, or infiltrative BCC with topical therapies alone.",
        dosage_guidelines: "Pathology report must confirm negative peripheral and deep margins.",
        safety_monitoring: "Complete whole-body skin check every 6–12 months."
      },
      diet: {
        focus: "DNA Photoprotection & Nrf2 Activation",
        key_micronutrients: "Nicotinamide (500 mg BID), Astaxanthin (4 mg), EGCG (300 mg).",
        superfoods: ["Steamed wild salmon", "Green tea matcha", "Cooked tomatoes in olive oil"],
        foods_to_restrict: ["Charred meats", "Excess alcohol", "Refined sugars"]
      }
    },
    young_adult: {
      medications: {
        first_line: "Mohs Micrographic Surgery (gold standard for high-risk facial 'H-zone' tumors, morpheaform subtype, and recurrent tumors) OR standard surgical excision (4–5mm margins).",
        second_line: "For superficial BCC: Topical Imiquimod 5% (5x/week for 6 weeks) OR Photodynamic Therapy (PDT).",
        contraindications: "Do not leave margins unchecked; superficial cryosurgery without biopsy confirmation is not recommended for high-risk sites.",
        dosage_guidelines: "Mohs provides 99% 5-year cure rate while sparing maximal healthy dermal tissue.",
        safety_monitoring: "40%–50% risk of developing a secondary BCC within 5 years; adhere to 6-month dermatological surveillance."
      },
      diet: {
        focus: "Hedgehog Pathway Modulation & Cellular Repair",
        key_micronutrients: "Oral Nicotinamide (500 mg BID), Curcumin (1000 mg), Lycopene (20 mg), Resveratrol (100 mg).",
        superfoods: ["Cruciferous sulforaphane sprouts", "Cooked tomato sauces with extra virgin olive oil", "Wild sardines & walnuts"],
        foods_to_restrict: ["Heterocyclic amines in charred grilled meats", "Refined commercial seed oils", "Alcohol"]
      }
    },
    adult: {
      medications: {
        first_line: "Mohs Micrographic Surgery for head/neck, high-risk histology, or recurrent lesions; standard surgical excision with margins for trunk/extremities.",
        second_line: "Hedgehog Pathway Inhibitors (Vismodegib 150mg daily or Sonidegib 200mg daily) for locally advanced, inoperable, or metastatic BCC OR Cemiplimab (anti-PD-1 immunotherapy).",
        contraindications: "Hedgehog inhibitors cause muscle spasms, alopecia, dysgeusia (taste loss), and are highly teratogenic.",
        dosage_guidelines: "Surgical excision margins: 4mm for low-risk tumors <2cm; 6–10mm or Mohs for high-risk features.",
        safety_monitoring: "Dermatology surveillance every 6 months for 3 years, then annually."
      },
      diet: {
        focus: "Anti-Angiogenesis & Immunosurveillance Support",
        key_micronutrients: "Nicotinamide (500 mg BID), Epigallocatechin gallate (EGCG 500 mg), Curcumin (1500 mg), CoQ10 (150 mg).",
        superfoods: ["Pomegranate extract / fresh arils", "Steamed wild salmon and Atlantic mackerel", "Organic green tea & cruciferous vegetables"],
        foods_to_restrict: ["Nitrate-preserved processed meats", "High-glycemic refined carbohydrates", "Excess alcohol"]
      }
    },
    geriatric: {
      medications: {
        first_line: "Mohs surgery under local anesthesia (exceptionally well-tolerated in outpatients) OR gentle curettage and electrodesiccation (ED&C) for low-risk trunk/limb lesions.",
        second_line: "Superficial radiotherapy / electronic brachytherapy for patients unable to tolerate surgical reconstruction OR topical Imiquimod for superficial lesions.",
        contraindications: "Avoid aggressive reconstruction in frail patients with severe cardiovascular compromise or anticoagulant risks without multidisciplinary review.",
        dosage_guidelines: "Local lidocaine with epinephrine (safe with modern monitoring; epinephrine minimizes intraoperative hematoma).",
        safety_monitoring: "Assess wound healing over thin skin, monitor lower extremity edema and stasis."
      },
      diet: {
        focus: "Surgical Wound Re-epithelialization & Frailty Prevention",
        key_micronutrients: "Oral Nicotinamide (500 mg BID), Bioactive Collagen Peptides (10g), Vitamin C (500 mg), Zinc (15 mg), Vitamin D3 (2000 IU).",
        superfoods: ["Nutrient-rich bone broths with softened vegetables", "Soft-flaked wild salmon with sweet potato", "Steamed golden squash with extra virgin olive oil"],
        foods_to_restrict: ["Dehydrating salty snacks", "Processed sausages and bacon", "Hard dry foods"]
      }
    }
  },

  mel: {
    pediatric: {
      medications: {
        first_line: "Extremely rare; urgent pediatric oncology / dermatopathology referral. Wide local excision with depth-adjusted margins (0.5–2 cm).",
        second_line: "Sentinel Lymph Node Biopsy (SLNB) for Breslow depth >0.8 mm. Pediatric oncology evaluation for systemic targeted/immunotherapy.",
        contraindications: "Never perform shave or partial biopsy on suspected melanoma; full-thickness excisional biopsy is mandatory.",
        dosage_guidelines: "Margin guidelines: In situ (0.5 cm), <1 mm depth (1 cm), 1–2 mm depth (1–2 cm), >2 mm depth (2 cm).",
        safety_monitoring: "Whole-body lymph node ultrasound, pediatric oncology surveillance."
      },
      diet: {
        focus: "Metabolic Homeostasis & Immunological Support",
        key_micronutrients: "Vitamin D3 (1000 IU), Natural Mixed Carotenoids, Zinc, Omega-3 EPA/DHA.",
        superfoods: ["Pureed berry compotes", "Wild salmon puree", "Bone broths with soft carrots"],
        foods_to_restrict: ["High-sugar foods", "Processed deli meats"]
      }
    },
    adolescent: {
      medications: {
        first_line: "Immediate full-thickness excisional biopsy, followed by Wide Local Excision (1–2 cm margins) and SLNB if Breslow depth >0.8 mm (or >0.5 mm with ulceration/high mitotic rate).",
        second_line: "BRAF V600 mutation testing. Adjuvant anti-PD-1 immunotherapy (Nivolumab or Pembrolizumab) for resected Stage IIB/IIC/III.",
        contraindications: "Avoid cautery or incomplete destructive methods prior to definitive histological staging.",
        dosage_guidelines: "Immunotherapy dosing: Pembrolizumab 200mg IV Q3W or 400mg IV Q6W for 1 year.",
        safety_monitoring: "Monitor for immune-related adverse events (irAEs): colitis, thyroiditis, hypophysitis, hepatitis, pneumonitis."
      },
      diet: {
        focus: "Gut Microbiome Diversity for Immunotherapy Responsiveness",
        key_micronutrients: "High Dietary Fiber (>30g/day — clinically shown in Science to double anti-PD-1 response rates), Vitamin D3 (3000 IU), Nicotinamide (500 mg BID).",
        superfoods: ["Legumes and black beans", "Chia seeds, flaxseeds and raw walnuts", "Dark purple berries and fermented yogurt"],
        foods_to_restrict: ["Commercial probiotic pills without medical advice (can decrease immunotherapy diversity)", "Ultra-processed junk food", "Charred grilled meats"]
      }
    },
    young_adult: {
      medications: {
        first_line: "Definitive Wide Local Excision (WLE) with Sentinel Lymph Node Biopsy (SLNB). Adjuvant Pembrolizumab or Nivolumab for Stage IIB/C and Stage III.",
        second_line: "Targeted combination therapy for BRAF V600E/K positive melanoma: Dabrafenib (Tafinlar 150mg BID) + Trametinib (Mekinist 2mg daily) OR Encorafenib + Binimetinib.",
        contraindications: "Do not delay surgical excision. Progesterone/estrogen oral contraceptives need specialist review if on systemic kinase inhibitors.",
        dosage_guidelines: "Adjuvant immunotherapy typically administered for 12 months post-surgical resection.",
        safety_monitoring: "Baseline PET-CT or brain MRI for Stage III/IV. Check thyroid panel (TSH/free T4), ACTH/cortisol, and LFTs before every immunotherapy infusion."
      },
      diet: {
        focus: "Microbiome-Immuno-Oncology Optimization Protocol",
        key_micronutrients: "Dietary Insoluble/Soluble Fiber (>35g/day), Nicotinamide (500 mg BID), Polypodium leucotomos (480 mg), Curcumin (1500 mg).",
        superfoods: ["Steamed artichoke hearts and lentils", "Wild Alaskan sockeye salmon and sardines", "Organic green tea and wild elderberries"],
        foods_to_restrict: ["Processed delicatessen meats (nitrosamines)", "Excess alcohol", "Refined pro-inflammatory vegetable oils"]
      }
    },
    adult: {
      medications: {
        first_line: "Wide Local Excision with depth-directed margins + SLNB. Dual checkpoint inhibition (Nivolumab + Ipilimumab) for high-risk Stage IV / metastatic disease.",
        second_line: "BRAF + MEK targeted inhibitors for BRAF-mutant metastatic disease OR Tumor-Infiltrating Lymphocyte (TIL) therapy (Lifileucel).",
        contraindications: "Dual immunotherapy (Nivo + Ipi) carries a ~55% Grade 3/4 immune toxicity rate. Requires emergency access to high-dose systemic steroids (Methylprednisolone).",
        dosage_guidelines: "Administer under board-certified medical oncology care in an infusion center equipped for irAE management.",
        safety_monitoring: "Serial CT chest/abdomen/pelvis and brain MRI every 3–6 months for high-risk stages."
      },
      diet: {
        focus: "Immune Surveillance, Nrf2 Activation & Anti-Inflammatory Nutrition",
        key_micronutrients: "Oral Nicotinamide (500 mg BID), Vitamin D3 (target serum 25-OH-D >40 ng/mL), Resveratrol, Sulforaphane.",
        superfoods: ["Cruciferous broccoli sprouts and Brussels sprouts", "Cooked organic tomato paste with olive oil", "Pomegranate extract & green tea"],
        foods_to_restrict: ["Charred barbecue meats and bacon", "Processed high-sugar bakery goods", "Commercial seed oils"]
      }
    },
    geriatric: {
      medications: {
        first_line: "Wide local excision with margin clearance under local/regional anesthesia. Sentinel lymph node biopsy considered based on biological age, performance status, and comorbidity index.",
        second_line: "Anti-PD-1 monotherapy (Pembrolizumab or Nivolumab) has shown equal efficacy and manageable safety in geriatric patients compared to dual checkpoint blockade.",
        contraindications: "High-dose dual immunotherapy (Nivo + Ipi) is frequently poorly tolerated in elderly patients with pre-existing autoimmune, cardiovascular, or renal compromise.",
        dosage_guidelines: "Careful attention to wound tension and reconstructive flaps over atrophic geriatric donor sites.",
        safety_monitoring: "Close monitoring of fluid balance, endocrine auto-immunity (hypophysitis / adrenal insufficiency can present subtly as lethargy/falls in seniors)."
      },
      diet: {
        focus: "Nutritional Resilience, Sarcopenia Prevention & Hydration",
        key_micronutrients: "High-Quality Protein (1.2–1.5 g/kg/day), Oral Nicotinamide (500 mg BID), Marine Collagen Peptides (10g), Vitamin D3 (2000 IU).",
        superfoods: ["Nutrient-dense bone broth with stewed fish and soft leeks", "Mashed avocado with cold-pressed olive oil", "Soft wild berry compote with organic Greek yogurt"],
        foods_to_restrict: ["Dehydrating salty processed meats", "Dry unpalatable meals that reduce caloric intake", "Refined inflammatory sweets"]
      }
    }
  },

  ros: {
    pediatric: {
      medications: {
        first_line: "Topical Metronidazole 0.75% gel/lotion OR Azelaic Acid 10% cream applied once daily. Physical mineral sunscreens (Zinc oxide).",
        second_line: "Oral Erythromycin (if ocular rosacea present). Avoid tetracyclines under 8 years.",
        contraindications: "Avoid topical fluorinated corticosteroids (causes steroid-induced rosacea and skin atrophy).",
        dosage_guidelines: "Use gentle soap-free cleansers; avoid vigorous scrubbing.",
        safety_monitoring: "Pediatric ophthalmology consult if ocular irritation, photophobia, or stye-like chalazia present."
      },
      diet: {
        focus: "Capillary Calming & Gut Microbiome Integrity",
        key_micronutrients: "Zinc, Lutein, Bioflavonoids, Vitamin C.",
        superfoods: ["Sweet potatoes", "Cucumber and mint water", "Steamed squash"],
        foods_to_restrict: ["Spicy foods", "Cinnamaldehyde-containing treats", "Very hot temperature foods"]
      }
    },
    adolescent: {
      medications: {
        first_line: "Topical Ivermectin 1% cream (Soolantra) once daily at bedtime + Azelaic Acid 15% gel AM.",
        second_line: "Low-dose anti-inflammatory Doxycycline (40mg modified release) OR Minocycline 50mg daily.",
        contraindications: "Avoid astringents, witch hazel, chemical sunscreens (oxybenzone), and rough exfoliating scrubs.",
        dosage_guidelines: "Apply gentle broad-spectrum mineral SPF 50+ daily.",
        safety_monitoring: "Evaluate for ocular rosacea (foreign body sensation, blepharitis)."
      },
      diet: {
        focus: "Vasomotor Stability & Mast Cell Quenching",
        key_micronutrients: "Quercetin (500 mg), Omega-3 (1500 mg), Vitamin C with bioflavonoids.",
        superfoods: ["Matcha green tea (cool/iced)", "Chia pudding with blueberries", "Celery juice"],
        foods_to_restrict: ["Spicy chili peppers and hot sauces", "Energy drinks with excess niacin", "Steaming soups"]
      }
    },
    young_adult: {
      medications: {
        first_line: "Topical Ivermectin 1% cream + Topical Brimonidine 0.33% gel (Mirvaso) OR Oxymetazoline 1% cream (Rhofade) for persistent centrofacial erythema.",
        second_line: "Pulsed Dye Laser (595nm PDL) or Intense Pulsed Light (IPL) for telangiectasias OR oral Doxycycline 40mg modified release.",
        contraindications: "Avoid potent topical steroids (induces rebound erythema and pustules). Warn patients of possible rebound erythema with brimonidine.",
        dosage_guidelines: "Apply pea-sized amount of ivermectin once daily across forehead, chin, nose, and cheeks.",
        safety_monitoring: "Monitor for ocular involvement and cutaneous stinging."
      },
      diet: {
        focus: "Endothelial Stabilization & Flushing Trigger Reduction",
        key_micronutrients: "Rutin (500 mg), Hesperidin (200 mg), Zinc (20 mg), Magnesium.",
        superfoods: ["Cold-pressed extra virgin olive oil", "Fresh pomegranate arils", "Steamed wild cod & leafy greens"],
        foods_to_restrict: ["Red wine and spirits", "Thermal hot drinks (let cool before sipping)", "Capsaicin-rich foods"]
      }
    },
    adult: {
      medications: {
        first_line: "Minocycline 1.5% topical foam (Amzeeq) OR Ivermectin 1% cream + Azelaic Acid 15% foam.",
        second_line: "Vascular lasers (PDL / 532nm KTP) for fixed telangiectasias + low-dose oral Isotretinoin (10–20 mg daily) for refractory papulopustular/early phymatous rosacea.",
        contraindications: "Screen for alcohol-related flushing vs dermatological flushing; avoid vasodilatory medications if possible.",
        dosage_guidelines: "Laser treatments spaced 4–6 weeks apart; strict post-procedure photoprotection.",
        safety_monitoring: "LFTs and triglycerides if on low-dose isotretinoin; ophthalmology review for corneal vascularization."
      },
      diet: {
        focus: "Microvascular Integrity & Thermoregulatory Control",
        key_micronutrients: "CoQ10 (100 mg), Curcumin C3 (1000 mg), Omega-3 EPA/DHA (2000 mg), Resveratrol.",
        superfoods: ["Cold cucumber and mint gazpacho", "Steamed salmon with dill and lemon", "Chamomile and rooibos tea (chilled)"],
        foods_to_restrict: ["Aged cheeses (histamine)", "Cured meats", "Hard liquor"]
      }
    },
    geriatric: {
      medications: {
        first_line: "Topical Metronidazole 0.75% cream (gentle moisturizing vehicle) OR Azelaic Acid 10% cream + heavy ceramide emollient.",
        second_line: "Electrosurgery or CO2 laser ablation for advanced rhinophyma (sebaceous gland hyperplasia of nose).",
        contraindications: "Avoid Brimonidine in patients with severe cardiovascular disease or unstable angina due to peripheral vasoconstrictive alpha-2 activity.",
        dosage_guidelines: "Pat gently onto fragile facial skin without friction.",
        safety_monitoring: "Examine for concurrent actinic keratoses or BCC in sun-exposed centrofacial zones."
      },
      diet: {
        focus: "Gentle Cooling Nutrition & Barrier Lipid Replenishment",
        key_micronutrients: "Bioactive Collagen (10g), Vitamin C (500 mg), Zinc Bisglycinate (15 mg), Vitamin D3 (2000 IU).",
        superfoods: ["Cool bone broth soup with soft carrots", "Pureed avocado with cold-pressed olive oil", "Stewed blueberries with Greek yogurt"],
        foods_to_restrict: ["Piping hot beverages", "High-sodium processed snacks", "Alcoholic spirits"]
      }
    }
  },

  vit: {
    pediatric: {
      medications: {
        first_line: "Topical Tacrolimus 0.03% ointment OR Pimecrolimus 1% cream BID (steroid-sparing) + Targeted narrowband UVB (NB-UVB) phototherapy.",
        second_line: "Low-to-mid potency topical corticosteroids (Desonide 0.05% or Hydrocortisone butyrate 0.1%) limited to 2–4 weeks cycles.",
        contraindications: "Avoid prolonged potent fluorinated steroids on pediatric facial skin.",
        dosage_guidelines: "Apply thin layer to depigmented macules only.",
        safety_monitoring: "Monitor repigmentation (follicular perifollicular islands); pediatric thyroid screen if familial."
      },
      diet: {
        focus: "Antioxidant Melanocyte Shielding & Mitochondrial Support",
        key_micronutrients: "Ginkgo Biloba extract (standardized), Vitamin B12, Folic Acid, Copper, Zinc.",
        superfoods: ["Fresh figs and black raisins", "Soaked almonds and walnuts", "Cooked dark leafy greens"],
        foods_to_restrict: ["Excess sour/acidic citrus if clinically reactive", "Artificial food dyes", "High-sugar candies"]
      }
    },
    adolescent: {
      medications: {
        first_line: "Topical Ruxolitinib 1.5% cream (Opzelura, FDA-approved JAK1/JAK2 inhibitor for vitiligo in patients ≥12 yrs) applied BID to affected areas up to 10% BSA.",
        second_line: "Narrow-band UVB (NB-UVB) full-body phototherapy 2–3 times weekly OR Excimer laser (308nm) for localized recalcitrant lesions.",
        contraindications: "Do not exceed 10% BSA for topical JAK inhibitors without specialist approval. Avoid intentional sunburns on depigmented spots.",
        dosage_guidelines: "Rub cream gently into depigmented patches until absorbed; allow 6 months for noticeable repigmentation.",
        safety_monitoring: "Screen for autoimmune thyroid disease (anti-TPO antibodies, TSH) and alopecia areata."
      },
      diet: {
        focus: "JAK-STAT Downregulation & Melanocyte Defense",
        key_micronutrients: "Vitamin D3 (2000 IU), Vitamin B12 (1000 mcg), Alpha-Lipoic Acid (300 mg), Quercetin (500 mg).",
        superfoods: ["Wild blueberries and blackberries", "Sprouted pumpkin seeds and walnuts", "Steeped green tea and turmeric milk"],
        foods_to_restrict: ["Excessive ascorbic acid mega-doses (>2g/day may impair tyrosinase)", "Fast-food oxidized oils", "Refined sugars"]
      }
    },
    young_adult: {
      medications: {
        first_line: "Topical Ruxolitinib 1.5% cream BID combined with Excimer laser (308 nm) or targeted NB-UVB.",
        second_line: "Systemic oral mini-pulse (OMP) Dexamethasone (4–5 mg on two consecutive days per week for 3–6 months) strictly for rapidly progressive spreading vitiligo.",
        contraindications: "Avoid continuous daily oral corticosteroids (Cushingoid risk). Check pregnancy precautions with systemic immunomodulators.",
        dosage_guidelines: "OMP requires careful blood pressure and glucose monitoring.",
        safety_monitoring: "Annual thyroid panel, fasting glucose, vitamin B12 level, and whole-body Wood's lamp examination."
      },
      diet: {
        focus: "Redox Equilibrium & Tyrosinase Activation Protocol",
        key_micronutrients: "Alpha-Lipoic Acid (600 mg), CoQ10 (200 mg), L-Phenylalanine (500 mg with sunlight), Vitamin B12 + Folate.",
        superfoods: ["Brazil nuts (selenium cofactor)", "Wild caught Alaskan salmon", "Steamed asparagus and broccoli"],
        foods_to_restrict: ["High-stress pro-inflammatory diets", "Excessive alcohol consumption", "Refined seed oils"]
      }
    },
    adult: {
      medications: {
        first_line: "Topical Ruxolitinib 1.5% cream BID + NB-UVB phototherapy OR Tacrolimus 0.1% ointment.",
        second_line: "Surgical autologous non-cultured epidermal cell suspension (NCES) or punch grafting for stable, refractory segment vitiligo.",
        contraindications: "Surgery is strictly contraindicated in active, spreading vitiligo (causes Koebner phenomenon).",
        dosage_guidelines: "Disease must be clinically stable for at least 12 months before considering autologous grafting.",
        safety_monitoring: "Screen for autoimmune polyendocrine syndromes, pernicious anemia, and diabetes mellitus."
      },
      diet: {
        focus: "Systemic Immunomodulation & Melanin Precursors",
        key_micronutrients: "Oral Polypodium Leucotomos (480 mg), Curcumin (1000 mg), Zinc Picolinate (30 mg), Vitamin D3 (3000 IU).",
        superfoods: ["Black sesame seeds", "Pomegranate arils", "Extra virgin olive oil with rosemary"],
        foods_to_restrict: ["Pro-inflammatory processed meats", "Refined grains", "Excess commercial sweeteners"]
      }
    },
    geriatric: {
      medications: {
        first_line: "Topical Tacrolimus 0.1% ointment OR mild topical steroids + Strict physical mineral SPF 50+ (Zinc Oxide 20%+) to prevent severe sunburn on amelanotic skin.",
        second_line: "Gentle targeted NB-UVB phototherapy under clinical guidance.",
        contraindications: "Avoid aggressive systemic steroid mini-pulses due to osteoporosis, hypertension, and cataract exacerbation in seniors.",
        dosage_guidelines: "Sunscreen application mandatory every 2 hours outdoors on depigmented skin (melanin absence elevates burn risk).",
        safety_monitoring: "Skin cancer screening in chronically sun-exposed vitiligo macules; review for drug-induced depigmentation."
      },
      diet: {
        focus: "DNA Protection, Barrier Hydration & Sarcopenia Nutrition",
        key_micronutrients: "Vitamin B12 (methylcobalamin 1000 mcg), Hydrolyzed Collagen (10g), Vitamin D3 (2000 IU), Zinc (15 mg).",
        superfoods: ["Nutrient-rich bone broths", "Soft stewed berries with Greek yogurt", "Mashed avocado and sweet potatoes"],
        foods_to_restrict: ["Dehydrating salty snacks", "Dry processed crackers", "Excess sugar"]
      }
    }
  }
};

window.getClientDefaultAgeProtocol = function(code, age_key, age) {
  const isPediatric = (age_key === 'pediatric');
  const isSenior = (age_key === 'geriatric');

  if (code === 'vasc') {
    if (isPediatric) {
      return {
        medications: {
          first_line: "Oral Propranolol solution (1–3 mg/kg/day under pediatric cardiology/dermatology monitoring for infantile hemangiomas) OR Topical Timolol maleate 0.5% gel-forming solution BID.",
          second_line: "Pulsed Dye Laser (595nm PDL) for residual superficial vascular erythema.",
          contraindications: "Monitor for hypoglycemia, bradycardia, and hypotension with beta-blockers. Administer oral propranolol immediately after feeding.",
          dosage_guidelines: "Timolol: 1–2 drops applied directly to lesion surface; avoid systemic absorption in neonates by pressing gently with gauze.",
          safety_monitoring: "Baseline heart rate, blood pressure, and blood glucose check."
        },
        diet: {
          focus: "Endothelial Health & Maternal Nutrition Support",
          key_micronutrients: "Vitamin C, Bioflavonoids, Zinc, Omega-3 DHA.",
          superfoods: ["Pureed sweet potato", "Mashed avocado", "Blueberry puree"],
          foods_to_restrict: ["Artificial food dyes", "High-sugar syrups"]
        }
      };
    } else {
      return {
        medications: {
          first_line: "Pulsed Dye Laser (PDL 595nm) or Long-Pulsed Nd:YAG (1064nm) for cherry angiomas / vascular ectasias OR gentle electrodessication.",
          second_line: "Surgical excision or shave removal if repeatedly traumatized or bleeding.",
          contraindications: "Rule out amelanotic melanoma or Kaposi sarcoma before destructive physical therapy.",
          dosage_guidelines: "Spot-size and pulse duration adjusted to vessel diameter.",
          safety_monitoring: "Recheck any lesion with irregular border, spontaneous hemorrhage, or rapid enlargement."
        },
        diet: {
          focus: "Capillary Wall Elasticity & Bioflavonoid Stabilization",
          key_micronutrients: "Rutin (500 mg), Hesperidin (250 mg), Vitamin C (500 mg), Quercetin.",
          superfoods: ["Pomegranate arils", "Citrus bioflavonoid peel infusions", "Organic dark berries"],
          foods_to_restrict: ["Excessive alcohol (promotes facial and trunk telangiectasias)", "Extreme hot spices"]
        }
      };
    }
  }

  // Default benign protocol (nv, bkl, df)
  return {
    medications: {
      first_line: "Clinical dermatoscopic surveillance + Full-spectrum mineral SPF 50+ (Zinc oxide / Titanium dioxide). Lesion is benign; no aggressive systemic pharmacotherapy indicated.",
      second_line: "Surgical shave excision, gentle cryotherapy, or electrocautery if lesion is subject to repetitive mechanical irritation, friction, or cosmetic concern.",
      contraindications: "Do not perform incomplete destructive procedures on atypical or evolving lesions without prior histological biopsy.",
      dosage_guidelines: "Apply SPF 50+ generously 15 minutes before UV exposure; reapply every 2 hours outdoors.",
      safety_monitoring: "Perform monthly skin self-exams using the ABCDE criteria (Asymmetry, Border, Color, Diameter, Evolution)."
    },
    diet: {
      focus: isSenior ? "Geriatric Sarcopenia & Barrier Hydration" : "Cellular DNA Photoprotection & General Skin Integrity",
      key_micronutrients: isSenior ? "Collagen Peptides (10g), Vitamin B12 (1000 mcg), Vitamin D3 (2000 IU), Zinc (15 mg)." : "Nicotinamide (500 mg BID), Omega-3 EPA/DHA (1000 mg), Vitamin D3 (1000–2000 IU), Vitamin C.",
      superfoods: ["Cooked tomato paste with extra virgin olive oil", "Wild Alaskan salmon or flaxseed porridge", "Organic green tea & wild blueberries"],
      foods_to_restrict: ["Ultra-processed pro-inflammatory foods", "Refined sugars and trans-fats", "Excessive alcohol"]
    }
  };
};

window.getClientAgeProtocol = function(disease_code, age) {
  const info = window.getAgeGroupInfo(age);
  const code = (disease_code || 'bcc').toLowerCase().trim();
  const diseaseData = window.CLIENT_AGE_MATRIX[code] || {};
  let ageData = diseaseData[info.key];
  if (!ageData) {
    ageData = window.getClientDefaultAgeProtocol(code, info.key, age);
  }
  return {
    age: parseFloat(age) || 28,
    age_group_key: info.key,
    age_group_label: info.label,
    age_icon: info.icon,
    medications: ageData.medications || {},
    diet_modulations: ageData.diet || {}
  };
};
