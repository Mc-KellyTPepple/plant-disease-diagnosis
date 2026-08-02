# ============================================================
# DISEASE INFORMATION DATABASE
# Part 1 (Classes 0–9)
# ============================================================

DISEASE_INFO = {

    # --------------------------------------------------------
    # APPLE
    # --------------------------------------------------------

    "Apple___Apple_scab": {

        "name": "Apple Scab",

        "description":
            "Apple Scab is one of the most common fungal diseases affecting apple trees. "
            "It primarily attacks leaves and fruits, producing dark olive-green or black lesions "
            "that reduce fruit quality and yield.",

        "cause":
            "Caused by the fungus Venturia inaequalis.",

        "symptoms": [
            "Olive-green spots on young leaves",
            "Dark velvety lesions on fruits",
            "Premature leaf drop",
            "Cracked and deformed apples",
            "Reduced fruit quality"
        ],

        "treatment": [
            "Remove infected leaves and fruits.",
            "Apply recommended fungicides during the growing season.",
            "Prune trees to improve air circulation.",
            "Dispose of fallen leaves to reduce fungal spores."
        ],

        "prevention": [
            "Plant resistant apple varieties.",
            "Maintain proper tree spacing.",
            "Avoid prolonged leaf wetness.",
            "Practice regular orchard sanitation."
        ]
    },

    "Apple___Black_rot": {

        "name": "Apple Black Rot",

        "description":
            "Black Rot is a fungal disease that affects apple fruits, leaves, and branches. "
            "It can cause serious fruit decay and branch cankers if left unmanaged.",

        "cause":
            "Caused by the fungus Botryosphaeria obtusa.",

        "symptoms": [
            "Purple spots on leaves",
            "Black circular fruit rot",
            "Shriveled 'mummified' fruits",
            "Dark branch cankers",
            "Leaf yellowing"
        ],

        "treatment": [
            "Remove infected fruits and branches.",
            "Prune dead wood during dormancy.",
            "Apply fungicides where recommended.",
            "Destroy infected plant debris."
        ],

        "prevention": [
            "Maintain orchard hygiene.",
            "Avoid tree injuries.",
            "Prune regularly.",
            "Monitor trees throughout the season."
        ]
    },

    "Apple___Cedar_apple_rust": {

        "name": "Cedar Apple Rust",

        "description":
            "Cedar Apple Rust is a fungal disease that alternates between apple trees "
            "and cedar or juniper trees. It mainly damages leaves and reduces fruit production.",

        "cause":
            "Caused by the fungus Gymnosporangium juniperi-virginianae.",

        "symptoms": [
            "Bright yellow-orange leaf spots",
            "Orange lesions on fruits",
            "Leaf drop",
            "Reduced photosynthesis",
            "Poor fruit development"
        ],

        "treatment": [
            "Apply fungicides early in the growing season.",
            "Remove nearby infected cedar galls if possible.",
            "Prune infected branches."
        ],

        "prevention": [
            "Plant resistant cultivars.",
            "Avoid planting apples near cedar trees.",
            "Inspect orchards regularly."
        ]
    },

    "Apple___healthy": {

        "name": "Healthy Apple",

        "description":
            "The apple plant appears healthy with no visible signs of disease.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy green leaves",
            "Normal fruit development",
            "No lesions",
            "No discoloration",
            "No wilting"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Continue routine monitoring.",
            "Maintain balanced fertilization.",
            "Prune when necessary.",
            "Practice good orchard sanitation."
        ]
    },

    # --------------------------------------------------------
    # BLUEBERRY
    # --------------------------------------------------------

    "Blueberry___healthy": {

        "name": "Healthy Blueberry",

        "description":
            "The blueberry plant appears healthy without visible disease symptoms.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy foliage",
            "Normal berry growth",
            "Uniform green leaves",
            "No spots",
            "No discoloration"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Maintain proper soil acidity.",
            "Water consistently.",
            "Apply fertilizer as recommended.",
            "Inspect plants regularly."
        ]
    },

    # --------------------------------------------------------
    # CHERRY
    # --------------------------------------------------------

    "Cherry_(including_sour)___Powdery_mildew": {

        "name": "Cherry Powdery Mildew",

        "description":
            "Powdery mildew is a fungal disease that forms white powdery growth on leaves, "
            "young shoots, and fruits, reducing plant vigor.",

        "cause":
            "Caused by Podosphaera species.",

        "symptoms": [
            "White powdery coating",
            "Leaf curling",
            "Stunted shoots",
            "Distorted leaves",
            "Reduced fruit quality"
        ],

        "treatment": [
            "Apply sulfur or approved fungicides.",
            "Remove infected shoots.",
            "Improve air circulation."
        ],

        "prevention": [
            "Avoid overcrowding.",
            "Prune trees regularly.",
            "Avoid excessive nitrogen fertilizer."
        ]
    },

    "Cherry_(including_sour)___healthy": {

        "name": "Healthy Cherry",

        "description":
            "The cherry plant appears healthy with no visible disease symptoms.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy leaves",
            "Healthy fruits",
            "No fungal growth",
            "No discoloration",
            "Normal development"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Continue proper orchard management.",
            "Inspect plants regularly.",
            "Maintain balanced nutrition."
        ]
    },

    # --------------------------------------------------------
    # CORN
    # --------------------------------------------------------

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {

        "name": "Corn Gray Leaf Spot",

        "description":
            "Gray Leaf Spot is one of the most damaging fungal diseases of maize, reducing "
            "photosynthesis and grain yield.",

        "cause":
            "Caused by Cercospora zeae-maydis.",

        "symptoms": [
            "Long rectangular gray lesions",
            "Leaf blighting",
            "Premature leaf death",
            "Reduced grain filling",
            "Lower yield"
        ],

        "treatment": [
            "Apply fungicides where economically justified.",
            "Rotate crops.",
            "Destroy infected crop residue."
        ],

        "prevention": [
            "Plant resistant hybrids.",
            "Practice crop rotation.",
            "Improve field sanitation."
        ]
    },

    "Corn_(maize)___Common_rust_": {

        "name": "Corn Common Rust",

        "description":
            "Common Rust is a fungal disease characterized by reddish-brown pustules on maize leaves.",

        "cause":
            "Caused by Puccinia sorghi.",

        "symptoms": [
            "Brown raised pustules",
            "Leaf yellowing",
            "Reduced photosynthesis",
            "Early leaf senescence"
        ],

        "treatment": [
            "Use resistant hybrids.",
            "Apply fungicides if infection is severe."
        ],

        "prevention": [
            "Monitor fields regularly.",
            "Rotate crops.",
            "Maintain field hygiene."
        ]
    },

    "Corn_(maize)___Northern_Leaf_Blight": {

        "name": "Corn Northern Leaf Blight",

        "description":
            "Northern Leaf Blight is a fungal disease producing long cigar-shaped lesions on maize leaves.",

        "cause":
            "Caused by Exserohilum turcicum.",

        "symptoms": [
            "Long gray-green lesions",
            "Leaf drying",
            "Reduced grain production",
            "Premature leaf death"
        ],

        "treatment": [
            "Apply fungicides when appropriate.",
            "Plant resistant hybrids.",
            "Remove infected crop residue."
        ],

        "prevention": [
            "Rotate crops.",
            "Use disease-resistant varieties.",
            "Practice good field sanitation."
        ]
    },



    # --------------------------------------------------------
    # CORN
    # --------------------------------------------------------

    "Corn_(maize)___healthy": {

        "name": "Healthy Corn",

        "description":
            "The maize plant appears healthy with no visible signs of disease or nutrient deficiency.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Uniform green leaves",
            "Strong upright stalk",
            "Healthy ear development",
            "No lesions",
            "Normal growth"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Maintain balanced fertilization.",
            "Monitor fields regularly.",
            "Practice proper irrigation.",
            "Control weeds."
        ]
    },

    # --------------------------------------------------------
    # GRAPE
    # --------------------------------------------------------

    "Grape___Black_rot": {

        "name": "Grape Black Rot",

        "description":
            "Black Rot is a destructive fungal disease that affects grape leaves, shoots, and berries, reducing both fruit quality and yield.",

        "cause":
            "Caused by the fungus Guignardia bidwellii.",

        "symptoms": [
            "Brown circular leaf spots",
            "Black lesions on shoots",
            "Shriveled black berries",
            "Fruit mummification",
            "Premature leaf drop"
        ],

        "treatment": [
            "Remove infected fruit clusters.",
            "Prune infected vines.",
            "Apply recommended fungicides.",
            "Destroy infected plant debris."
        ],

        "prevention": [
            "Ensure good air circulation.",
            "Avoid excessive canopy density.",
            "Practice vineyard sanitation.",
            "Monitor vines regularly."
        ]
    },

    "Grape___Esca_(Black_Measles)": {

        "name": "Grape Esca (Black Measles)",

        "description":
            "Esca is a complex trunk disease that weakens grapevines and reduces productivity over time.",

        "cause":
            "Associated with several wood-decaying fungi including Phaeomoniella and Phaeoacremonium species.",

        "symptoms": [
            "Tiger-striped leaf patterns",
            "Dark spots on berries",
            "Branch dieback",
            "Reduced vine vigor",
            "Sudden vine collapse"
        ],

        "treatment": [
            "Prune infected wood.",
            "Remove severely infected vines.",
            "Protect pruning wounds.",
            "Maintain vine health."
        ],

        "prevention": [
            "Disinfect pruning tools.",
            "Avoid trunk injuries.",
            "Use healthy planting material.",
            "Inspect vineyards routinely."
        ]
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {

        "name": "Grape Leaf Blight",

        "description":
            "Leaf Blight causes extensive spotting and premature leaf loss, reducing photosynthesis and fruit production.",

        "cause":
            "Caused by Isariopsis species.",

        "symptoms": [
            "Brown irregular leaf spots",
            "Yellow leaf margins",
            "Leaf drying",
            "Premature defoliation",
            "Reduced vine vigor"
        ],

        "treatment": [
            "Apply approved fungicides.",
            "Remove infected leaves.",
            "Improve vineyard ventilation."
        ],

        "prevention": [
            "Avoid prolonged leaf wetness.",
            "Maintain good sanitation.",
            "Prune vines regularly."
        ]
    },

    "Grape___healthy": {

        "name": "Healthy Grape",

        "description":
            "The grapevine appears healthy with no visible signs of disease.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy green leaves",
            "Normal fruit clusters",
            "No spots",
            "No wilting",
            "Healthy vine growth"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Continue proper vineyard management.",
            "Monitor regularly.",
            "Maintain balanced nutrition."
        ]
    },

    # --------------------------------------------------------
    # ORANGE
    # --------------------------------------------------------

    "Orange___Haunglongbing_(Citrus_greening)": {

        "name": "Citrus Greening (Huanglongbing)",

        "description":
            "Citrus Greening is one of the most devastating citrus diseases worldwide. It severely reduces fruit quality and eventually kills infected trees.",

        "cause":
            "Caused by Candidatus Liberibacter bacteria and spread by the Asian citrus psyllid.",

        "symptoms": [
            "Yellow mottled leaves",
            "Misshapen fruits",
            "Green fruits that fail to ripen",
            "Twig dieback",
            "Poor tree growth"
        ],

        "treatment": [
            "There is currently no cure.",
            "Remove severely infected trees.",
            "Control psyllid populations.",
            "Maintain tree nutrition."
        ],

        "prevention": [
            "Use certified disease-free seedlings.",
            "Monitor citrus psyllids.",
            "Remove infected trees promptly.",
            "Inspect orchards frequently."
        ]
    },

    # --------------------------------------------------------
    # PEACH
    # --------------------------------------------------------

    "Peach___Bacterial_spot": {

        "name": "Peach Bacterial Spot",

        "description":
            "Bacterial Spot affects peach leaves and fruits, causing lesions that reduce fruit marketability.",

        "cause":
            "Caused by Xanthomonas arboricola pv. pruni.",

        "symptoms": [
            "Small dark leaf spots",
            "Fruit lesions",
            "Leaf yellowing",
            "Premature leaf drop",
            "Fruit cracking"
        ],

        "treatment": [
            "Apply copper-based sprays where recommended.",
            "Prune infected branches.",
            "Remove infected debris."
        ],

        "prevention": [
            "Plant resistant cultivars.",
            "Avoid overhead irrigation.",
            "Maintain orchard sanitation."
        ]
    },

    "Peach___healthy": {

        "name": "Healthy Peach",

        "description":
            "The peach tree appears healthy with no visible disease symptoms.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy foliage",
            "Normal fruit development",
            "No lesions",
            "No discoloration",
            "Healthy growth"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Continue routine orchard care.",
            "Inspect plants regularly.",
            "Maintain proper nutrition."
        ]
    },

    # --------------------------------------------------------
    # BELL PEPPER
    # --------------------------------------------------------

    "Pepper,_bell___Bacterial_spot": {

        "name": "Bell Pepper Bacterial Spot",

        "description":
            "Bacterial Spot causes lesions on leaves and fruits, reducing yield and market quality.",

        "cause":
            "Caused by Xanthomonas species.",

        "symptoms": [
            "Water-soaked leaf spots",
            "Dark fruit lesions",
            "Leaf yellowing",
            "Leaf drop",
            "Reduced fruit quality"
        ],

        "treatment": [
            "Apply copper-based bactericides where recommended.",
            "Remove infected plants.",
            "Avoid working with wet plants."
        ],

        "prevention": [
            "Use certified disease-free seed.",
            "Rotate crops.",
            "Avoid overhead watering.",
            "Maintain field sanitation."
        ]
    },

    "Pepper,_bell___healthy": {

        "name": "Healthy Bell Pepper",

        "description":
            "The bell pepper plant appears healthy with no visible signs of disease.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy leaves",
            "Healthy fruits",
            "No lesions",
            "Normal flowering",
            "Vigorous growth"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Maintain balanced fertilization.",
            "Water appropriately.",
            "Inspect plants routinely.",
            "Control weeds and pests."
        ]
    },

    # --------------------------------------------------------
    # POTATO
    # --------------------------------------------------------

    "Potato___Early_blight": {

        "name": "Potato Early Blight",

        "description":
            "Early Blight is a common fungal disease that affects potato leaves, stems, and tubers, reducing photosynthesis and crop yield.",

        "cause":
            "Caused by the fungus Alternaria solani.",

        "symptoms": [
            "Brown circular leaf spots with concentric rings",
            "Yellowing around lesions",
            "Premature leaf drop",
            "Stem lesions",
            "Reduced tuber yield"
        ],

        "treatment": [
            "Apply recommended fungicides.",
            "Remove infected leaves.",
            "Avoid overhead irrigation.",
            "Maintain adequate plant nutrition."
        ],

        "prevention": [
            "Rotate crops every 2–3 years.",
            "Use certified disease-free seed potatoes.",
            "Remove infected crop debris.",
            "Avoid excessive leaf wetness."
        ]
    },

    "Potato___Late_blight": {

        "name": "Potato Late Blight",

        "description":
            "Late Blight is one of the most destructive potato diseases and can rapidly destroy entire fields under cool and humid conditions.",

        "cause":
            "Caused by Phytophthora infestans.",

        "symptoms": [
            "Large water-soaked leaf lesions",
            "White fungal growth beneath leaves",
            "Dark brown stem lesions",
            "Rapid plant collapse",
            "Brown rotting tubers"
        ],

        "treatment": [
            "Apply appropriate fungicides immediately.",
            "Remove infected plants.",
            "Destroy infected tubers.",
            "Improve field drainage."
        ],

        "prevention": [
            "Use resistant potato varieties.",
            "Avoid overhead irrigation.",
            "Ensure proper field ventilation.",
            "Plant certified disease-free seed."
        ]
    },

    "Potato___healthy": {

        "name": "Healthy Potato",

        "description":
            "The potato plant appears healthy with no visible signs of disease.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy green foliage",
            "No lesions",
            "Normal tuber development",
            "Strong stems",
            "Uniform plant growth"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Maintain proper fertilization.",
            "Monitor for pests and diseases.",
            "Practice crop rotation.",
            "Use quality seed potatoes."
        ]
    },

    # --------------------------------------------------------
    # RASPBERRY
    # --------------------------------------------------------

    "Raspberry___healthy": {

        "name": "Healthy Raspberry",

        "description":
            "The raspberry plant appears healthy with no visible disease symptoms.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy green leaves",
            "Normal fruit production",
            "No discoloration",
            "Healthy canes",
            "Good plant vigor"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Prune regularly.",
            "Provide adequate irrigation.",
            "Monitor for insects.",
            "Maintain field sanitation."
        ]
    },

    # --------------------------------------------------------
    # SOYBEAN
    # --------------------------------------------------------

    "Soybean___healthy": {

        "name": "Healthy Soybean",

        "description":
            "The soybean plant appears healthy with no visible signs of disease.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy leaves",
            "Normal pod formation",
            "Uniform green color",
            "No spots",
            "Strong plant growth"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Continue proper crop management.",
            "Monitor fields regularly.",
            "Maintain balanced fertilization.",
            "Rotate crops."
        ]
    },

    # --------------------------------------------------------
    # SQUASH
    # --------------------------------------------------------

    "Squash___Powdery_mildew": {

        "name": "Squash Powdery Mildew",

        "description":
            "Powdery Mildew is a common fungal disease affecting squash leaves, reducing photosynthesis and overall yield.",

        "cause":
            "Caused by several powdery mildew fungi including Podosphaera xanthii.",

        "symptoms": [
            "White powdery patches on leaves",
            "Leaf yellowing",
            "Leaf curling",
            "Premature leaf death",
            "Reduced fruit production"
        ],

        "treatment": [
            "Apply sulfur or approved fungicides.",
            "Remove heavily infected leaves.",
            "Improve air circulation."
        ],

        "prevention": [
            "Avoid overcrowding.",
            "Plant resistant varieties.",
            "Monitor plants regularly.",
            "Avoid excessive nitrogen fertilizer."
        ]
    },

    # --------------------------------------------------------
    # STRAWBERRY
    # --------------------------------------------------------

    "Strawberry___Leaf_scorch": {

        "name": "Strawberry Leaf Scorch",

        "description":
            "Leaf Scorch is a fungal disease that causes purple spots which later merge and dry out, weakening strawberry plants.",

        "cause":
            "Caused by Diplocarpon earlianum.",

        "symptoms": [
            "Small purple leaf spots",
            "Brown scorched leaf margins",
            "Leaf drying",
            "Reduced plant vigor",
            "Lower fruit yield"
        ],

        "treatment": [
            "Remove infected leaves.",
            "Apply fungicides if necessary.",
            "Improve plant spacing."
        ],

        "prevention": [
            "Use disease-free planting material.",
            "Avoid overhead watering.",
            "Maintain field sanitation.",
            "Rotate planting areas."
        ]
    },

    "Strawberry___healthy": {

        "name": "Healthy Strawberry",

        "description":
            "The strawberry plant appears healthy with no visible signs of disease.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy green leaves",
            "Healthy fruits",
            "No lesions",
            "Normal flowering",
            "Strong plant growth"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Continue routine crop management.",
            "Maintain irrigation.",
            "Inspect plants regularly.",
            "Control weeds."
        ]
    },

    # --------------------------------------------------------
    # TOMATO
    # --------------------------------------------------------

    "Tomato___Bacterial_spot": {

        "name": "Tomato Bacterial Spot",

        "description":
            "Bacterial Spot affects tomato leaves, stems, and fruits, reducing both yield and fruit quality.",

        "cause":
            "Caused by Xanthomonas species.",

        "symptoms": [
            "Small dark leaf spots",
            "Yellow leaf halos",
            "Raised fruit lesions",
            "Leaf drop",
            "Reduced fruit quality"
        ],

        "treatment": [
            "Apply copper-based bactericides where recommended.",
            "Remove infected plants.",
            "Avoid handling wet plants.",
            "Use disease-free seedlings."
        ],

        "prevention": [
            "Rotate crops.",
            "Avoid overhead irrigation.",
            "Disinfect garden tools.",
            "Maintain good field hygiene."
        ]
    },

    "Tomato___Early_blight": {

        "name": "Tomato Early Blight",

        "description":
            "Early Blight is a fungal disease that causes characteristic concentric-ring lesions on tomato leaves and stems.",

        "cause":
            "Caused by Alternaria solani.",

        "symptoms": [
            "Brown circular leaf spots",
            "Yellowing around lesions",
            "Stem lesions",
            "Leaf drop",
            "Reduced fruit production"
        ],

        "treatment": [
            "Apply fungicides.",
            "Remove infected leaves.",
            "Mulch around plants.",
            "Improve air circulation."
        ],

        "prevention": [
            "Rotate crops.",
            "Avoid wetting foliage.",
            "Use disease-free seedlings.",
            "Practice good sanitation."
        ]
    },

    "Tomato___Late_blight": {

        "name": "Tomato Late Blight",

        "description":
            "Late Blight is one of the most destructive diseases of tomatoes. Under cool and humid conditions, it can spread rapidly and destroy entire crops within days.",

        "cause":
            "Caused by Phytophthora infestans.",

        "symptoms": [
            "Large water-soaked leaf lesions",
            "Brown or black leaf spots",
            "White fungal growth beneath leaves",
            "Dark stem lesions",
            "Brown rotting fruits"
        ],

        "treatment": [
            "Remove infected leaves and fruits immediately.",
            "Apply appropriate fungicides according to local recommendations.",
            "Improve air circulation around plants.",
            "Destroy severely infected plants."
        ],

        "prevention": [
            "Avoid overhead irrigation.",
            "Plant resistant varieties when available.",
            "Ensure proper spacing.",
            "Inspect plants regularly.",
            "Rotate crops annually."
        ]
    },

    "Tomato___Leaf_Mold": {

        "name": "Tomato Leaf Mold",

        "description":
            "Leaf Mold mainly affects greenhouse and humid-environment tomatoes, reducing photosynthesis and plant vigor.",

        "cause":
            "Caused by Passalora fulva (Fulvia fulva).",

        "symptoms": [
            "Yellow patches on upper leaf surfaces",
            "Olive-green mold underneath leaves",
            "Leaf curling",
            "Leaf drop",
            "Reduced fruit yield"
        ],

        "treatment": [
            "Remove infected leaves.",
            "Reduce humidity.",
            "Improve greenhouse ventilation.",
            "Apply recommended fungicides."
        ],

        "prevention": [
            "Maintain proper spacing.",
            "Avoid excessive humidity.",
            "Water at the base of plants.",
            "Sanitize greenhouse equipment."
        ]
    },

    "Tomato___Septoria_leaf_spot": {

        "name": "Tomato Septoria Leaf Spot",

        "description":
            "Septoria Leaf Spot is a fungal disease that primarily affects tomato foliage, leading to premature defoliation.",

        "cause":
            "Caused by Septoria lycopersici.",

        "symptoms": [
            "Small circular gray leaf spots",
            "Dark spot margins",
            "Yellow leaves",
            "Premature leaf drop",
            "Reduced fruit quality"
        ],

        "treatment": [
            "Remove infected leaves.",
            "Apply fungicides.",
            "Avoid overhead watering.",
            "Improve airflow around plants."
        ],

        "prevention": [
            "Rotate crops.",
            "Use disease-free seedlings.",
            "Maintain field sanitation.",
            "Mulch around plants."
        ]
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {

        "name": "Tomato Spider Mites",

        "description":
            "Spider mites are tiny sap-feeding pests that damage tomato leaves and reduce plant vigor, especially during hot and dry weather.",

        "cause":
            "Infestation by Two-spotted Spider Mites (Tetranychus urticae).",

        "symptoms": [
            "Tiny yellow speckles on leaves",
            "Fine webbing",
            "Leaf bronzing",
            "Leaf drying",
            "Reduced plant growth"
        ],

        "treatment": [
            "Spray affected plants with water to reduce mite populations.",
            "Apply insecticidal soap or horticultural oil.",
            "Use approved miticides if infestation is severe."
        ],

        "prevention": [
            "Maintain adequate humidity.",
            "Inspect plants regularly.",
            "Control weeds.",
            "Encourage beneficial predatory insects."
        ]
    },

    "Tomato___Target_Spot": {

        "name": "Tomato Target Spot",

        "description":
            "Target Spot is a fungal disease that causes circular lesions on tomato leaves and fruits, reducing crop yield.",

        "cause":
            "Caused by Corynespora cassiicola.",

        "symptoms": [
            "Circular brown lesions",
            "Concentric rings",
            "Leaf yellowing",
            "Fruit lesions",
            "Premature defoliation"
        ],

        "treatment": [
            "Apply fungicides.",
            "Remove infected plant material.",
            "Improve field ventilation.",
            "Reduce leaf wetness."
        ],

        "prevention": [
            "Practice crop rotation.",
            "Use healthy seedlings.",
            "Maintain proper spacing.",
            "Remove crop debris."
        ]
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {

        "name": "Tomato Yellow Leaf Curl Virus",

        "description":
            "Tomato Yellow Leaf Curl Virus is a serious viral disease that causes severe yield losses in tomato production.",

        "cause":
            "Caused by Tomato Yellow Leaf Curl Virus (TYLCV) and transmitted mainly by whiteflies.",

        "symptoms": [
            "Upward leaf curling",
            "Yellowing leaves",
            "Stunted plants",
            "Reduced flowering",
            "Poor fruit production"
        ],

        "treatment": [
            "There is no cure for infected plants.",
            "Remove infected plants.",
            "Control whitefly populations.",
            "Use resistant varieties."
        ],

        "prevention": [
            "Plant virus-resistant cultivars.",
            "Use insect-proof nets.",
            "Monitor and control whiteflies.",
            "Remove weeds that host the virus."
        ]
    },

    "Tomato___Tomato_mosaic_virus": {

        "name": "Tomato Mosaic Virus",

        "description":
            "Tomato Mosaic Virus is a highly contagious viral disease that reduces plant growth and fruit quality.",

        "cause":
            "Caused by Tomato Mosaic Virus (ToMV).",

        "symptoms": [
            "Mosaic light and dark green leaf patterns",
            "Leaf distortion",
            "Stunted growth",
            "Reduced fruit size",
            "Poor fruit quality"
        ],

        "treatment": [
            "There is no cure.",
            "Remove infected plants.",
            "Disinfect tools thoroughly.",
            "Avoid handling healthy plants after infected ones."
        ],

        "prevention": [
            "Use certified virus-free seed.",
            "Disinfect tools frequently.",
            "Avoid tobacco contamination.",
            "Plant resistant varieties."
        ]
    },

    "Tomato___healthy": {

        "name": "Healthy Tomato",

        "description":
            "The tomato plant appears healthy with no visible signs of disease or pest damage.",

        "cause":
            "No disease detected.",

        "symptoms": [
            "Healthy green leaves",
            "Normal flowering",
            "Healthy fruits",
            "Strong stems",
            "Normal plant growth"
        ],

        "treatment": [
            "No treatment required."
        ],

        "prevention": [
            "Continue regular monitoring.",
            "Maintain balanced fertilization.",
            "Water consistently.",
            "Control weeds and pests.",
            "Practice good garden sanitation."
        ]
    }

}
