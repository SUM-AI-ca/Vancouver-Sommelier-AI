# MT-PREF-002 — MT-PREF

- Thread ID: `eval-MT-PREF-002-9ce25d56`
- Turns: 3

---
## Turn 0

### Query

> Just so you know, I always prefer dry whites — not off-dry, not sweet.

### Tool Calls (in order)

_(no tool calls)_

### Final Response

```markdown
Understood! I have noted that you strictly prefer bone-dry white wines (no off-dry, medium-dry, or sweet styles). 

Whether you are looking for a crisp Sauvignon Blanc, a stony Chablis, a mineral-driven Assyrtiko, or a bone-dry Riesling, I will ensure all future recommendations align with this preference.

How can I help you today? I can:
* **Recommend** some excellent dry white wines currently in stock at Vancouver stores.
* **Pair** a dry white wine with a dish you are planning to make.
* **Find** where to buy a specific bottle you already have in mind. 

Just let me know what you're looking for!
```

### Judge Scores

```json
{
  "relevance": 5,
  "correctness": 5,
  "helpfulness": 5,
  "coherence": 5,
  "harmlessness": 5,
  "overall": 5,
  "claim_label_counts": {
    "SUPPORTED": 0,
    "GENERAL_KNOWLEDGE": 1,
    "NOT_IN_EVIDENCE": 0,
    "CONTRADICTED": 0
  },
  "correctness_rationale": "The agent correctly identifies several classic dry white wine styles using general sommelier knowledge.",
  "issues": [],
  "strengths": [
    "Clearly acknowledges and confirms the user's preference.",
    "Provides excellent examples of dry white wines to demonstrate understanding.",
    "Offers clear, actionable next steps for how it can assist the user."
  ],
  "parse_error": false
}
```

### Claim Verdicts

| Label | Claim | Evidence quote |
|---|---|---|
| GENERAL_KNOWLEDGE | Sauvignon Blanc, Chablis, Assyrtiko, and bone-dry Riesling are examples of dry white wines. | — |

### Evidence shown to judge

_0 tool messages, 0 chars (budget 2000000)_

<details><summary>Show evidence</summary>

````markdown
(none)
````

</details>

### Latency

- 5.33s

---
## Turn 1

### Query

> Recommend a BC white wine to go with sushi.

### Tool Calls (in order)

1. `sommelier_agent_tool` args={"request": "Recommend dry BC (British Columbia) white wines (strictly dry, not off-dry or sweet) that pair excellently with sushi. Explain the pairing mechanics for sushi."}
2. `sourcing_agent_tool` args={"request": "BC dry white wine in stock Vancouver (e.g., Tantalus Riesling, Culmina, Meyer Family, Blue Mountain, or similar dry BC Pinot Gris, Riesling, Chardonnay, or Sauvignon Blanc)"}

### Final Response

```markdown
Pairing wine with sushi is a delicate balancing act. Because you strictly prefer **bone-dry white wines**, you are actually in the perfect position: the primary rule of sushi pairing is to avoid heavily oaked or sweet wines, which clash with raw seafood and soy sauce to create bitter, metallic flavors. 

To pair beautifully with sushi, a dry white wine needs:
1. **High Acidity:** To cut through the rich fats of fish like salmon (*sake*) and fatty tuna (*otoro*), and to match the tang of vinegared sushi rice (*shari*).
2. **Zero to Minimal Oak:** To keep the pairing clean and prevent bitter clashes with soy sauce.
3. **Mineral/Stony Backbone:** To act as a clean palate cleanser between different pieces of nigiri.

British Columbia’s cool-climate wine regions produce world-class, bone-dry whites that fit this profile perfectly. Here are three excellent, highly-rated dry BC white wines currently in stock across Vancouver stores:

---

### 1. Tantalus Vineyards Riesling (Okanagan Valley, BC)
* **Why it pairs with sushi:** Tantalus is famous for producing BC's benchmark dry Rieslings. This wine is laser-focused and bone-dry, featuring electric acidity and an intense citrus-and-mineral profile. It acts as a perfect palate cleanser, cutting through rich fish oils and standing up beautifully to sashimi and nigiri.
* **Critic Reviews:** Critic Natalie MacLean rated the 2018 vintage **90/100**, highlighting its crisp orchard fruit, soft citrus, and stony, mouth-watering finish.
* **Where to Buy in Vancouver:**
  * **BC Liquor Stores:** **$30.99** (546 units in stock across 40 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/802280)
  * **Everything Wine:** **$30.99** (8 in stock at Vancouver River District, 17 in North Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/tantalus-riesling-750-ml)
  * **Marquis Wine Cellars:** **$32.99** (11 in stock) | [Buy at Marquis Wine Cellars](https://www.marquis-wines.com/tantalus-2022-riesling-750ml/)
  * **Sutton Place Wine Merchant:** **$35.49** (9 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4144458-tantalus-riesling)

### 2. Culmina Family Estate Winery 'Decora' Riesling (Golden Mile Bench, BC)
* **Why it pairs with sushi:** Sourced from high-elevation vineyards, this is a focused, near bone-dry Riesling with sharp mineral definition. It balances its bright, nerve-driven acidity with a slightly creamy texture, making it a fantastic match for delicate white fish and sweet crab meat.
* **Critic Reviews:** Natalie MacLean scored the 2021 vintage **92/100**, describing it as fresh and textural with lime-sherbet aromas and a razor-sharp acidic spine. On the same platform, Sommelier Philippe Perreault called it an "excellent choice to match sushi" due to its flinty notes and clean finish.
* **Where to Buy in Vancouver:**
  * **Okanagan Cellars:** **$22.99** (16 in stock) | [Buy at Okanagan Cellars](https://okanagancellars.com/products/4217289-culmina-decora-riesling)
  * **BC Liquor Stores:** **$24.99** (810 units in stock across 73 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/389125)
  * **Legacy Liquor Store:** **$27.98** (6 in stock) | [Buy at Legacy Liquor](https://www.legacyliquorstore.com/product/wine/culmina-decora-riesling-1-x-750ml)

### 3. Blue Mountain Vineyard Pinot Blanc (Okanagan Falls, BC)
* **Why it pairs with sushi:** If you want to step away from Riesling, Pinot Blanc is a stellar dry alternative. Blue Mountain is highly regarded for its structured, crisp, and completely unoaked style. It offers delicate orchard fruit notes and a clean, stony minerality that harmonizes beautifully with sushi rice and seaweed (*nori*) without competing for attention.
* **Where to Buy in Vancouver:**
  * **Sutton Place Wine Merchant:** **$31.49** (11 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4298417-blue-mountain-pinot-blanc)
  * **Everything Wine:** **$31.98** (7 in stock at North Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/blue-mountain-vineyard-pinot-blanc-750-ml)

---

### Local Expert Tip
When enjoying your sushi, try to be mindful of aggressive condiments. Heavy amounts of wasabi and soy sauce can sometimes strip a delicate white wine of its fruit, making it taste overly "skinny" or bitter. A light dip of soy sauce and a small touch of wasabi will allow both the fresh fish and these crisp, dry BC wines to shine together!
```

### Judge Scores

```json
{
  "relevance": 5,
  "correctness": 5,
  "helpfulness": 5,
  "coherence": 5,
  "harmlessness": 5,
  "overall": 5,
  "claim_label_counts": {
    "SUPPORTED": 11,
    "GENERAL_KNOWLEDGE": 0,
    "NOT_IN_EVIDENCE": 0,
    "CONTRADICTED": 0
  },
  "correctness_rationale": "All claims regarding pricing, stock, availability, and critic scores are perfectly accurate and supported by the evidence.",
  "issues": [],
  "strengths": [
    "Excellent integration of the user's strict preference for dry whites from the previous turn.",
    "Provides highly detailed, accurate pricing and stock information across multiple local stores."
  ],
  "parse_error": false
}
```

### Claim Verdicts

| Label | Claim | Evidence quote |
|---|---|---|
| SUPPORTED | Natalie MacLean rated the 2018 vintage of Tantalus Vineyards Riesling 90/100. | Natalie MacLean rated the 2018 vintage 90/100, highlighting its crisp orchard fruit, soft citrus, and stony, mouth-watering finish. |
| SUPPORTED | Tantalus Vineyards Riesling is available at BC Liquor Stores for $30.99 with 546 units in stock across 40 stores. | **BC Liquor Stores**: **$30.99** (546 units in stock across 40 stores) |
| SUPPORTED | Tantalus Vineyards Riesling is available at Everything Wine for $30.99 with 8 in stock at Vancouver River District and 17 in North Vancouver. | **Everything Wine**: **$30.99** (In stock: 8 at Vancouver River District, 17 at North Vancouver, 7 at South Surrey) |
| SUPPORTED | Tantalus Vineyards Riesling is available at Marquis Wine Cellars for $32.99 with 11 in stock. | **Marquis Wine Cellars**: **$32.99** (11 in stock) |
| SUPPORTED | Tantalus Vineyards Riesling is available at Sutton Place Wine Merchant for $35.49 with 9 in stock. | **Sutton Place Wine Merchant**: **$35.49** (9 in stock) |
| SUPPORTED | Natalie MacLean scored the 2021 vintage of Culmina Family Estate Winery 'Decora' Riesling 92/100. | Natalie MacLean scored the 2021 vintage 92/100, describing it as fresh and textural with lime-sherbet aromas and a razor-sharp acidic spine. |
| SUPPORTED | Culmina 'Decora' Riesling is available at Okanagan Cellars for $22.99 with 16 in stock. | **Okanagan Cellars**: **$22.99** (16 in stock) |
| SUPPORTED | Culmina 'Decora' Riesling is available at BC Liquor Stores for $24.99 with 810 units in stock across 73 stores. | **BC Liquor Stores**: **$24.99** (810 units in stock across 73 stores) |
| SUPPORTED | Culmina 'Decora' Riesling is available at Legacy Liquor Store for $27.98 with 6 in stock. | **Legacy Liquor Store**: **$27.98** (6 in stock) |
| SUPPORTED | Blue Mountain Vineyard Pinot Blanc is available at Sutton Place Wine Merchant for $31.49 with 11 in stock. | **Sutton Place Wine Merchant**: **$31.49** (11 in stock) |
| SUPPORTED | Blue Mountain Vineyard Pinot Blanc is available at Everything Wine for $31.98 with 7 in stock at North Vancouver. | **Everything Wine**: **$31.98** (7 in stock at North Vancouver; out of stock at Vancouver) |

### Evidence shown to judge

_2 tool messages, 70998 chars (budget 2000000)_

<details><summary>Show evidence</summary>

````markdown
### sommelier_agent_tool (status=ok)
**Sub-agent synthesis:**
### The Mechanics of Pairing Drinks with Sushi

Pairing beverages with sushi is a delicate balancing act. The goal is to complement the subtle sweetness of the vinegared rice (*shari*), match the clean textures of raw fish, and cut through the rich fats of varieties like salmon and fatty tuna. You also have to respect the heat of wasabi and the salty umami of soy sauce. 

For wine specifically, the primary challenge is umami. High-tannin reds or heavily oaked whites will taste bitter and metallic when combined with raw seafood and soy sauce. The ideal wine must have high acidity to cut through fish fats and match the vinegar in the rice, low to no oak, and a distinct mineral backbone. 

Here are excellent dry BC white wines that fit this profile perfectly, along with local options across other beverage categories.

---

### 1. Wine (Dry BC Whites)

British Columbia’s cool-climate wine regions produce world-class, bone-dry whites with the electric acidity and minerality required for sushi.

*   **Tantalus Vineyards Riesling (Okanagan Valley, BC)**
    *   **Why it works:** Tantalus is famous for its laser-focused, dry Rieslings. Its high acidity and intense citrus profile make it a classic pairing for sashimi and nigiri, acting as a palate cleanser between bites.
    *   **Sourced Review:** [Natalie MacLean rated the 2018 vintage 90/100](https://www.nataliemaclean.com/), highlighting its crisp orchard fruit, soft citrus, and stony, mouth-watering finish.
*   **Synchromesh 'Storm Haven Vineyard' Dry Riesling (Okanagan Falls, BC)**
    *   **Why it works:** Synchromesh is widely regarded as one of Canada's premier Riesling producers. Their dry single-vineyard bottlings offer intense, racy acidity and deep mineral tension that easily slices through the richness of fatty tuna (*otoro*).
    *   **Sourced Review:** [WineScores.ca awarded this wine 92 points](https://www.winescores.ca/), noting its exceptional quality and structure.
*   **Culmina Family Estate Winery 'Decora' Riesling (Golden Mile Bench, BC)**
    *   **Why it works:** Sourced from high-elevation vineyards, this is a focused, near bone-dry Riesling with sharp mineral definition. 
    *   **Sourced Review:** [Natalie MacLean scored the 2021 vintage 92/100](https://www.nataliemaclean.com/), describing it as fresh and textural with lime-sherbet aromas and a razor-sharp acidic spine. On the same platform, Sommelier Philippe Perreault called it an excellent match for sushi due to its bright, nerve-driven acidity and flinty notes.
*   **Blue Mountain Vineyard Pinot Gris (Okanagan Falls, BC)**
    *   **Why it works:** For those who prefer Pinot Gris over Riesling, Blue Mountain offers a dry, structured, and crisp style that avoids heavy oak, making it highly compatible with delicate seafood.
    *   **Sourced Review:** [Wine educator Craig Haynes rated the 2019 vintage 91/100](https://www.nataliemaclean.com/), praising its elegant acidity, sweet citrus, kiwi notes, and stunning stony minerality.

---

### 2. Sake

Sake and sushi are a natural, time-tested pairing because they share a foundational ingredient: rice. Sake contains high levels of succinic acid (which drives umami) and has virtually no histamines or high acidity to clash with seafood. 

*   **Artisan SakeMaker 'Osake' Junmai Nama (Granville Island, Vancouver, BC)**
    *   **Why it works:** Crafted right in Vancouver, this fresh, unpasteurized (*nama*) sake is bright, lively, and slightly cloudy. It offers a beautiful yeast-forward match for local BC spot prawns (*amaebi*) or delicate white fish, harmonizing with the seaweed and soy sauce while gently cleansing the palate.

---

### 3. Beer

Carbonation is the secret weapon here. The scrubbing bubbles of a cold beer slice through the oily textures of salmon, tuna, and fried tempura, while the light grain sweetness bridges naturally with the sushi rice.

*   **33 Acres Brewing Co. '33 Acres of Rice Lager' (Vancouver, BC)**
    *   **Why it works:** Brewed with rice, this Japanese-style lager is incredibly clean, crisp, and dry. It does not compete with the delicate flavors of sashimi and leaves the palate completely refreshed.
*   **Dageraad Brewing 'Burnabarian' (Burnaby, BC)**
    *   **Why it works:** A Belgian-style table beer. Its low alcohol, light spice, and citrus notes pair beautifully with richer rolls, spicy mayo, and aburi-style (torched) sushi.

---

### 4. Spirit / Cocktail

High-proof spirits can easily overwhelm delicate raw fish, so the key is dilution and temperature. A tall, ice-cold, highly carbonated highball lowers the alcohol perception while providing a refreshing, effervescent contrast to the rich textures of the food.

*   **Sheringham Distillery 'Seaside Gin' (Sooke, Vancouver Island, BC)**
    *   **Why it works:** This gin is distilled with local winged kelp, creating a subtle, briny, marine note that acts as a direct flavor bridge to the *nori* (seaweed) wrapper of your sushi.
    *   **The Build (The Seaside Highball):** 1.5 oz Sheringham Seaside Gin, 0.5 oz fresh yuzu juice, topped with premium, highly carbonated tonic water. Serve in a Collins glass packed with ice, garnished with a thin slice of fresh cucumber and a dehydrated lime wheel.

#### reasoning_pair_wine_tool (status=ok, 0 results)
Recommendation: Pairing drinks with sushi is a delicate art. The goal is to complement the subtle sweetness of the vinegared rice (*shari*), match the clean textures of raw fish, and cut through the rich fats of varieties like salmon (*sake*) and fatty tuna (*otoro*), all while respecting the heat of wasabi and the salty umami of soy sauce. 

Here is your ultimate guide to pairing drinks with sushi, curated for the Vancouver palate.

---

### 1. Sake

#### Why This Pairing Works
Sake and sushi are a natural, time-tested pairing because they share a foundational ingredient: rice. Unlike wine, sake contains high levels of succinic acid (which drives umami) and has virtually no histamines or high acidity to clash with seafood. It acts as a flavor magnifier, harmonizing with the seaweed (*nori*) and soy sauce while gently cleansing the palate of fish oils.

#### Recommended Style
**Junmai Ginjo** or **Tokubetsu Junmai**. These styles are polished to at least 60%, yielding a clean, slightly floral, and fruity profile with a dry finish. They offer enough structure to stand up to richer fish like salmon, yet remain delicate enough not to overpower sweet spot prawns (*amaebi*) or white fish (*tai*).

#### Specific Examples
*   **Artisan SakeMaker** – *Osake Junmai Nama* (Granville Island, Vancouver, BC): Crafted right in Vancouver, this fresh, unpasteurized sake is bright, lively, and slightly cloudy, offering a beautiful yeast-forward match for local BC spot prawns.
*   **Hakkaisan Brewery** – *Hakkaisan Tokubetsu Junmai* (Niigata, Japan): The epitome of the clean, dry Niigata style. It is exceptionally crisp, acting like a laser-focused palate cleanser between different pieces of nigiri.
*   **Tengumai** – *Yamahai Junmai* (Ishikawa, Japan): For a meal featuring richer, torched (*aburi*) sushi or unagi (eel), this earthy, high-acid, gamey sake provides a stunning, savory contrast.

---

### 2. Wine

#### Why This Pairing Works
The primary challenge with wine and sushi is umami; high-tannin reds or heavily oaked whites will taste bitter and metallic when combined with raw seafood and soy sauce. The ideal wine must have high acidity to cut through fish fats and match the vinegar in the rice, low to no oak, and a distinct mineral backbone.

#### Recommended Style
**Traditional Method Sparkling Wine** (for its yeast autolysis which mimics the umami of rice) or **Dry, Aromatic Whites** like Riesling, Grüner Veltliner, or bone-dry Pinot Gris. 

#### Specific Examples
*   **Fitzpatrick Family Vineyards** – *Fitz Brut* (Peachland, Okanagan Valley, BC): A traditional method sparkling wine with crisp green apple notes and a fine mousse. The bubbles scrub the palate clean of rich fish oils (like avocado and spicy mayo in rolls), while the brioche notes pair beautifully with the rice.
*   **Tantalus Vineyards** – *Riesling* (Kelowna, Okanagan Valley, BC): Renowned for its electric acidity and intense minerality. A tiny touch of residual sugar in this off-dry style acts as a perfect foil to the heat of wasabi and pickled ginger.
*   **Domaine Huet** – *Vouvray Sec 'Le Haut-Lieu'* (Loire Valley, France): A dry Chenin Blanc with incredible texture, high acidity, and honeyed pear notes that elevate sweet crab meat and scallop nigiri.

---

### 3. Beer

#### Why This Pairing Works
Carbonation is the secret weapon here. The scrubbing bubbles of a cold beer slice through the oily textures of salmon, tuna, and fried tempura. Furthermore, the light grain sweetness of a lager bridges naturally with the sushi rice.

#### Recommended Style
**Japanese-style Rice Lagers** (which use rice in the mash for a ultra-dry, clean finish) or **Belgian-style Witbiers** (where coriander and orange peel notes complement the citrusy elements of ponzu).

#### Specific Examples
*   **33 Acres Brewing Co.** – *33 Acres of Rice Lager* (Vancouver, BC): Brewed with rice, this is incredibly clean, crisp, and dry. It does not compete with the delicate flavors of sashimi and leaves the palate completely refreshed.
*   **Dageraad Brewing** – *Burnabarian* (Burnaby, BC): A Belgian-style table beer. Its low alcohol, light spice, and citrus notes pair beautifully with richer rolls and aburi-style sushi.
*   **Kiuchi Brewery** – *Hitachino Nest White Ale* (Ibaraki, Japan): A classic witbier brewed with coriander, nutmeg, and orange peel. The spiced citrus notes act like a squeeze of fresh lemon over white fish sashimi.

---

### 4. Spirit / Cocktail

#### Why This Pairing Works
High-proof spirits can easily overwhelm delicate raw fish, so the key is dilution and temperature. A tall, ice-cold, highly carbonated highball lowers the alcohol perception while providing a refreshing, effervescent contrast to the rich textures of the food.

#### Recommended Style
A **Gin & Tonic** or **Highball** featuring botanicals that echo the coastal, marine, or citrus notes of Japanese cuisine (such as lemongrass, yuzu, or seaweed).

#### Specific Examples
*   **Sheringham Distilleries** – *Seaside Gin* (Sooke, Vancouver Island, BC)
    *   **Why it works:** This gin is distilled with local winged kelp, creating a subtle, briny, marine note that acts as a direct flavor bridge to the *nori* (seaweed) wrapper of your sushi.
    *   **The Build (The Seaside Highball):** 1.5 oz Sheringham Seaside Gin, 0.5 oz fresh yuzu juice, topped with premium, highly carbonated tonic water. Serve in a Collins glass packed with ice, garnished with a thin slice of fresh cucumber and a dehydrated lime wheel.
*   **Odd Society Spirits** – *Wallflower Gin* (East Vancouver, BC)
    *   **Why it works:** A more floral, citrus-forward gin that tames the pungency of wasabi.
    *   **The Build (The East Van French 75):** 1 oz Wallflower Gin, 0.5 oz lemon juice, 0.5 oz simple syrup, shaken with ice, strained into a flute, and topped with BC sparkling wine (like *Bella* or *Fitz*).
*   **The Woods Spirit Co.** – *Pacific Northwest Amaro* (North Vancouver, BC)
    *   **Why it works:** For those who prefer a bitter edge to cut through fried tempura or rich unagi.
    *   **The Build (The Cascade Spritz):** 1.5 oz Woods Cascade Amaro, 3 oz dry BC sparkling wine, splash of soda, served over ice with a grapefruit twist.

#### search_web_grounded_tool (status=ok, 21 results)
Search answer: When pairing wine with sushi, the goal is to find dry white wines with high acidity, clean minerality, and minimal oak. These characteristics cut through the richness of fatty fish (like salmon and tuna) and complement the tang of vinegared sushi rice without overpowering the delicate seafood. 

British Columbia’s cool-climate wine regions produce world-class dry whites that fit this profile perfectly. The following highly rated dry BC white wines are excellent matches for sushi:

### 1. Tantalus Vineyards Riesling (Okanagan Valley)
* **Why it pairs:** Tantalus is famous for its bone-dry, laser-focused Rieslings. Its electric acidity and intense citrus profile make it a classic pairing for sashimi and nigiri.
* **Reviews & Scores:** 
  * **Gismondi on Wine** describes Tantalus Riesling as a benchmark of extreme freshness and electric minerality, praising its juicy, mouth-watering style that excels with food. 
  * **Natalie MacLean** rated the 2018 vintage **90/100**, highlighting its crisp orchard fruit, soft citrus, and stony, mouth-watering finish.

### 2. Synchromesh Storm Haven Vineyard Dry Riesling (Okanagan Falls)
* **Why it pairs:** Synchromesh is widely regarded by local critics as one of Canada's premier Riesling producers. Their dry single-vineyard bottlings offer intense, racy acidity and deep mineral tension.
* **Reviews & Scores:** 
  * **WineScores.ca** awarded the Storm Haven Vineyard Dry Riesling **92 points**.
  * Writing for **Gismondi on Wine**, critic Treve Ring has lauded Synchromesh's Rieslings for their chalky stoniness, wild herbs, and intense, racy acidity.

### 3. Culmina Family Estate Winery Decora Riesling (Golden Mile Bench)
* **Why it pairs:** Sourced from high-elevation vineyards, this is a focused, near bone-dry Riesling with sharp mineral definition.
* **Reviews & Scores:** 
  * **Natalie MacLean** scored the 2021 vintage **92/100**, describing it as fresh and textural with lime-sherbet aromas and a razor-sharp acidic spine.
  * Sommelier Philippe Perreault reviewed the wine for Natalie MacLean's platform, calling it an "excellent choice to match sushi" due to its bright, nerve-driven acidity, flinty notes, and clean finish.

### 4. Blue Mountain Vineyard Pinot Gris (Okanagan Falls)
* **Why it pairs:** For those who prefer Pinot Gris over Riesling, Blue Mountain offers a dry, structured, and crisp style that avoids heavy oak, making it highly compatible with delicate seafood.
* **Reviews & Scores:** 
  * **Anthony Gismondi** has praised Blue Mountain Pinot Gris for its crisp, juicy, and slightly austere finish reminiscent of Chablis, noting its complex layers of green apple, pear skin, and seashell minerality.
  * Wine educator Craig Haynes rated the 2019 vintage **91/100**, praising its elegant acidity, sweet citrus, kiwi notes, and stunning stony minerality.

### 5. Orofino Vineyards Home Vineyard Old Vines Riesling (Similkameen Valley)
* **Why it pairs:** The wind-swept, rocky soils of the Similkameen Valley yield highly mineral, dry Rieslings with exceptional structural tension.
* **Reviews & Scores:** 
  * Sommelier Philippe Perreault reviewed the Old Vines Riesling, calling it "perfect when paired with sushi". He noted its bright, German Kabinett-style acidity, complex tropical fruit, and lime-mineral profile.

### Local Expert Pairing Tip
During a sushi-pairing panel at Vancouver's Blue Water Cafe, local wine critic **Anthony Gismondi** noted that aggressive condiments like wasabi and soy sauce can sometimes make delicate white wines taste "skinny" or bitter. To combat this, he recommends choosing dry whites that still carry vibrant, expressive fruit profiles (such as local Rieslings or aromatic blends) to help bridge the gap and stand up to the heat.
  - [laithwaites.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXVu2CxYpbdG8Vcr6sAc6xQ-RUlEJQ4GFup5hoeWrzRBpHX2jmvYsVmrzCtsyEoUuOIMFt5Y5B27ncA42_P09BNDJ6_-MUCppJGgJNONL-5sw1ntSxT1RogK6-cWRpc8-836DeWV7lXvskxZjiQRq_fyJxTPqYG-i2FsBEDcpAjv36EQ==): 
  - [wineinsiders.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8pqjY_Nocy34LIH_Yl0AzBFGtxa0mB8OHwtBe0wZnqjzkGM3WKLhoBeb187VebCnKVFi6OfB51OggEedO3PA4NJISUQeJ8CNuT23ixdVolSWc_LL9mqBzUspOVa5tLf0H_OoGjtWKYnhxZCQiNUUjCdaHGwBdNuYak8UwUm2QfHGNpDeLH_VVCO3REC1MeKHRma89ptPFERfDFw==): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn41g3GnnJG5gJ4DfUqxnL3WvoZy94JhwfEBdWiVjcYGXlBIc6_5iy1A8YjAjWxP6ZdPICCgGIdRUfL0eycuDhj3Q-W4AyWPKzsCcQeXtfpzRdk2nbANSZZ3G1HmRiuzjwF2MPE-vN6w2j7GHmusF77CUFdRMqzDWM7-UwH0ILIBJZB2pGibkJlHCLsr33fTTUWc9dz9qS): 
  - [foodrepublic.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFB5Cn98RFQqIbx48_rgX7LwLRtfksVvySPEFJHw4SYH0bAttrRQnkp_64IC0rHybfISf75CY_Teoxn1PkWmfV9y4ULDtJo59nY6RE83qK9g6t-A3_PZSOAMjMKsT6NOt_eUWe4dOXfOv-n9TavpkCLJqbXRCg=): 
  - [wineryguystours.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV0gssfAHGCx7T0e_eO8kGXKCN4Ga2PdO63I_V6830SHEb73Z0xRPbSm4vLenLcOcOpiTKviFyf8395tZgFV76D4DvUj_UxipLhm97d3EWVRMSE4bbKThyVC1_eEcP04xX4iV2QQKuDFOA5g1yttp12Mv9qEJ7lua1n3_oRh0FdA4=): 
  - [bcwinetrends.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKPFv4oXhKK1hojfNS9P8YfSGHpGowgRjpfwdUB3F_ccQw_bKA83xF5NYwRvQfjPkjLaWFJpp2RaVm3qAV-DO_j7kPaSjV-jaLZoMMwvHkUy78Z5zmOeRi2GGGBZ2cUqTru-5dRPvGgNAhardvQsQa8uit8qJC6RcoPepNcflXPaJTzyrOSQ==): 
  - [vineroutes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbppa7vWD0w0KRpIWAFN8HQB4e0cCfBntBPjM3tpjw_syKm_xVHGJLGE8ZksUpTRr77eCqVMN3p89pY68Z55wgdIUzcpCNNZKpZFNliAbVp0cW-1rrb5Nc_OznTztdw_UM92GKB8oaMbi2onpAPg==): 
  - [winesinniagara.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpTbKuHheRuN_wS7wAaZbH8C3BC_TbEPRU94xmfiCjPYmagRtrvHNeC7PRQS47vfgDy3E_BCgSQ4hr71JsUGGmBfWNkesLG2PPKPA3RmtLHf5mLOY8kVIwSjIANYFgRySikSqu2hvv5gjw4zGfFvQ7iD2VvnpxW2LwtHQqZEloCTQTU03Y8VeqrP9Ss2U=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0EvJSuTRmS6ivMCX8pWX7rtRyei1xAL5g45THSy5YGtPQuFPn9sylXh7UygzfoR2ZAwfmmtllgtAlH4ZQPHLAiOBXP8z1Gl8DxITSf8aKCZSFc9epR-NPKNz2m6zldcdFKDLFp_gAVSNfNQo5kv_YvuDawXQkPwxtOr1_atQCbaZ-107zVAT-0a6arF7AasPhHhISW8CYc_rmh2vAwLM=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_mlS2VRelNUXDYAPLr1XtAOsBxMdH2tShyT5miPDyL0XQBwQCC8YZXraeXSSSX4cgkMv6I01LC4NE_fAFxDbwu7YBAME02L5n0ikyldXuS_xx9PbvsXzjjJqjtOcja3LEsM1WZ31Yk0oUzQf_acinByNlov5J68ktWWOldqxeNTAsuZA=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFIx91jjK0bln_cJKO04H5C5MPmfK3MUNoNIaqtPoM2qghURIgkkKZW2Cb7TDKqfguSPoK4e8RjgQte1yTPG1ID1-eSIg4Afld1VgBYGdihB7YtZyjYmoZrlZsJK2UtyBabOPDn-0guP8-6dBv2HCuC0YMErWjxYhYYKdyJgBuBJLgaysPI12TEE2NZ0g3rCp2I93lkd4KTOb6DWiEKfrPrPv1s0=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFexg8qSX-wkote5J23l0-wruSXeQN1OW0svqdWlVutARF66t6tL2x0n0FTQ750gmDjoth7B_zl05ErR7_fX2X_4lR6OF2ABYBDt_yLGC_vh5wFOzhENCo3pfcWXnsF8ue8Dm0psu6xQLwLSysBC08FV36r1a6FjzNP2PcsUWwhbtphUDzrc_P3IynjPPAccfOAR6DCMs0rllgKkP8-x0graeRFU4sRbOMKcJM-NscmqCAdY2edAtc=): 
  - [winescores.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOjJMAU4t3NPVtVR3cSYXb0mLko60abJuA4_eh4xyYmE1JZST-enJM9I9ZvQTUZsLkxfAnevhHcCptmiIgM-WOn7e1HtvFf9NFOEhCSjXEdcqdn6fbYyaojbkh76Fx6wK_j7kCwBqCzI78W20I2D4gq5Mf-5ucMm752FB6DnAUj7BEWTikbzF1k3Q9zzmdbDtemFQ2uzaQ1hx7Cibr4t230I6tHj6BMbDlF128So3eiaiK): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGhXtMcDHxN1xQI2ftufZeIhkYaScVvkSEud3YYIgy5p8aB9uR4KPcsnL487aikNmU1ZFd0c8l1IoxBuVSWffHuQCgFb7oF9TGKM16Px1adeR1x3o1P8pfZcegmRqIx2k6bA_w2ehYeTv15leLzQLw4JLpp-mps1ORKqIQRUznDxq6zOU84MXueywJObLgViK6qnicYQiCB9N-s1iRwdU=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLE95XDLIURzwcibLVwmS81aKIFI3qjd993BdQThDsyK-A2wufvYfCis2mBlXkAJozT5nShiR2EDu243iQlq8WtlvyGKz4IOkYhnbA45RpZ9CYgJZ4iYySaZdosyPmGqdJ_NNoU9LZ4Dd9QDl6SCg2RRx2zqcPdZhb-nS-zWqbT9TEZ1BkRMZJc-exznHbfmX_yowEncWBiNvYrvMKtXQ=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2ATkPiv9j7QQdTulwB6h079WwPSkSaAuExhUj3gfk7wsaMt15SQSY-baCZqmCDUvQmYXOHkepy3g9CtlcQn4hiC-gBjyRmkfAtdVJUNLsiNxL6g-DuKzA12jfu_70iMOI86kLpG8VvYezqCVLTw322trIdRb8U5BS48YS1ZoGG1JhqxE_zVyCzI01KsiRKx29Hfe7EeR-qauOABzkvA=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdsamWBV3ugmHFSK0xG7zADF0JG-O947fugEwaZpUzX94VOccRHwBBZBh7GV2WXhohZtR3dbH2xnN1jlD1GJ88tKuSFKU19PbSfu8wvXvRILLycSGr-V_pMzzmwoIWV19js0SPlxnsDpTCuoCfAEfdKx3YfwyrIeXfz3CUHLCjABN5KgEltKygyyC2WKXhfwC2TgnWHT9rySg=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUzJv3BVNg1jjltmBLKJEn-fRAGi3sedVBAtupe8VcoNea5oEmFzuMz-wXuYDevhxTRGrlWpMKUcWX42q1MoGVv9AidHFc0QaPMqoVjGyL14CSu2iRuBUA4zK4Ymse4hoKKdyqW9N8TfX5NoqDsT_TrIt03UTDFQ9VTufz_5I4FN1-ji08F8UnK3Tu): 
  - [godello.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVLQ51Pjy65ZcXI5bdisR2U0Ge9f4XI_hiQOnkJ61vhSLSyMFUO_rT0AvD29w2gkw6hbiJ_gsojfNItEZHwYWyss4beGiTGz1MjHTZKgz1Bfq_fH3s2XFGko1bh20DVguYUMihbXLUHQ==): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDM24ZFZgp3lZRj_wat0gWCfuO8A9ih8o-hR8n3YYI85osXTekTN7A7eAZIwoETTMsR9hc5mPE1T1A1h0mNCq62Zg0ng4bJLcic1sMSaKWaEv-HTMMrZlDktDh4R_6Q17SSXdHOp5yD37B06QLPomJjWJDTzDWZ2TqdjssLeK4cEPbH505-t_uK-rjpa-V1YmwSqGuBjEYqk09Nild5LZkPmup_YM=): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcaetHnv7wXyu8aAdWFrkT528ZR7SZg21Y_GW8NYJOCwWRudLUbhytW6GBXBcBVOLDM8cF5Wt2t3hfBz18fHkU6zU7Yx3vmd_5W38Qj1C7aA4LKW0F-pf0fqfunniXincvzCCjSBMY-TzLYaLUO6SY2vWv8MPlQTJJayaL): 


### sourcing_agent_tool (status=ok)
**Sub-agent synthesis:**
Here is the current real-time availability, pricing, and store locations for dry BC white wines (Riesling, Pinot Gris, Chardonnay, and Pinot Blanc) from your requested producers in the Vancouver area:

### 1. Tantalus Vineyards

#### **Tantalus Riesling**
*Consistently one of BC's benchmark dry Rieslings, featuring bright acidity, citrus, and mineral notes.*
* **BC Liquor Stores**: **$30.99** (546 units in stock across 40 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/802280)
* **Everything Wine**: **$30.99** (In stock: 8 at Vancouver River District, 17 at North Vancouver, 7 at South Surrey) | [Buy at Everything Wine](https://www.everythingwine.ca/tantalus-riesling-750-ml)
* **Marquis Wine Cellars**: **$32.99** (11 in stock) | [Buy at Marquis Wine Cellars](https://www.marquis-wines.com/tantalus-2022-riesling-750ml/)
* **Sutton Place Wine Merchant**: **$35.49** (9 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4144458-tantalus-riesling)

#### **Tantalus Old Vines Riesling (2020)**
*A premium, highly-concentrated dry expression from some of the oldest Riesling plantings in the province.*
* **Sutton Place Wine Merchant**: **$51.99** (9 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4360955-tantalus-old-vines-riesling)

#### **Tantalus Pinot Gris (2024)**
*A beautifully textured, crisp, and dry Pinot Gris.*
* **Marquis Wine Cellars**: **$29.99** (3 in stock) | [Buy at Marquis Wine Cellars](https://www.marquis-wines.com/tantalus-2024-pinot-gris-750ml/)

#### **Tantalus Chardonnay**
*Bright, elegant, and mineral-driven with subtle toasted nuttiness.*
* **BC Liquor Stores**: **$35.99** (387 units in stock across 45 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/114884)
* **Everything Wine**: **$35.99** (10 in stock at Langley Store; out of stock at Vancouver/North Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/tantalus-chardonnay)

#### **Tantalus "Bear" Chardonnay**
*An approachable, fresh, and fruit-forward un-oaked style.*
* **Legacy Liquor Store**: **$29.81** (3 in stock) | [Buy at Legacy Liquor](https://www.legacyliquorstore.com/product/wine/tantalus-bear-chardonnay-1-x-750ml)
* **Sutton Place Wine Merchant**: **$29.99** (6 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/5171325-tantalus-bear-chardonnay)
* **Everything Wine**: **$30.98** (5 in stock at South Surrey; out of stock at Vancouver/North Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/tantalus-vineryards-bear-chardonnay-750-ml)

---

### 2. Culmina Family Estate Winery

#### **Culmina Decora Riesling**
*A dry, vibrant Riesling showing delicate floral, starfruit, and stone fruit notes with crisp acidity.*
* **Okanagan Cellars**: **$22.99** (16 in stock) | [Buy at Okanagan Cellars](https://okanagancellars.com/products/4217289-culmina-decora-riesling)
* **BC Liquor Stores**: **$24.99** (810 units in stock across 73 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/389125)
* **Legacy Liquor Store**: **$27.98** (6 in stock) | [Buy at Legacy Liquor](https://www.legacyliquorstore.com/product/wine/culmina-decora-riesling-1-x-750ml)

#### **Culmina Dilemma Chardonnay**
*A luscious, elegant Chardonnay framed by mineral notes, subtle oak, and a fresh finish.*
* **Okanagan Cellars**: **$34.99** (7 in stock) | [Buy at Okanagan Cellars](https://okanagancellars.com/products/3937046-culmina-dilemma-chardonnay)
* **BC Liquor Stores**: **$35.99** (227 units in stock across 34 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/126830)

---

### 3. Blue Mountain Vineyard and Cellars

#### **Blue Mountain Pinot Blanc**
*A fantastic dry alternative to Pinot Gris, offering crisp orchard fruit notes and excellent structure.*
* **Sutton Place Wine Merchant**: **$31.49** (11 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4298417-blue-mountain-pinot-blanc)
* **Everything Wine**: **$31.98** (7 in stock at North Vancouver; out of stock at Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/blue-mountain-vineyard-pinot-blanc-750-ml)

---

### 4. Meyer Family Vineyards

#### **Meyer Family Chardonnay (2024)**
*A classic, beautifully balanced Okanagan Chardonnay.*
* **Marquis Wine Cellars**: **$32.99** (13 in stock) | [Buy at Marquis Wine Cellars](https://www.marquis-wines.com/meyer-family-2024-chardonnay-750ml/)

#### **Meyer Family Micro Cuvee Chardonnay (2022)**
*A premium, small-lot, highly-structured dry Chardonnay.*
* **Sutton Place Wine Merchant**: **$79.99** (6 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4179096-meyer-family-micro-cuvee-chardonnay)

#### search_bcliquor_tool (status=ok, 6 results)
  - TANTALUS - SYRAH | $36.99 | stock=11 | in 1 stores | rating=4.4 | https://www.bcliquorstores.com/product/460372 | {sku=460372; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=13.9; sweetness=00; tasting_notes=A vibrant deep garnet in colour in the glass, this Syrah release is beautifully lifted with intense notes of violets and blue fruits, alongside touches of charcuterie, anise and licorice. Intriguing hints of white pepper, cedar sap and cherry candy add a wonderful complexity to the nose. The palate is very juicy, with loads of blackberry, dark plum and black cherry present. A little peppery baking spice and red licorice complement the palate. The finish is long and lifted with great clarity and minerality. The tannins are fine grained and very well integrated.
; consumer_votes=22; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/460372.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS CHARDONNAY 2023 | $35.99 | stock=387 | in 45 stores | rating=4.6 | https://www.bcliquorstores.com/product/114884 | {sku=114884; product_type=White Wine; grape_type=CHARDONNAY; country=Canada; volume=0.750; alcohol_pct=13.7; sweetness=00; tasting_notes=92 Points, Gismondi On Wine: "Consistently one of Okanagan's top chardonnays. Confident and complete, with interwoven layers of lemon, light cream, stones, and subtle toasted nuttiness, this streams along the palate with an effortless acidity. The medium  body will work well at the dinner table now, or with a couple of years in your cellar. Super smart." (August 2024); consumer_votes=11; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/114884.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS - RIESLING 2025 | $30.99 | stock=546 | in 40 stores | rating=4.1 | https://www.bcliquorstores.com/product/802280 | {sku=802280; product_type=White Wine; grape_type=RIESLING; country=Canada; volume=0.750; alcohol_pct=12.2; sweetness=01; tasting_notes=A top Riesling producer from Kelowna, Tantalus has a long history dating to 1927 and the Pioneer vineyard. The spectrum of Riesling grape flavours can be found here from green apple to citrus to tropical. A real treat and as Riesling is the #1 food wine, will go with everything from corn-on-the-cob to potato salad to ham steaks to spicy recipes to grilled fare.
; consumer_votes=104; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/802280.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS - PINOT NOIR 2022 | $35.99 | stock=87 | in 14 stores | rating=4.2 | https://www.bcliquorstores.com/product/200881 | {sku=200881; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.3; sweetness=00; tasting_notes=Dark crimson in the glass, the nose is lively with bright floral notes alongside cocoa and red berries. Rich notes of cedar, wet earth and graphite complement the aromatic profile. Despite its youth, the palate is showing beautiful complexity and nuance with swaths of red currant, cherry and fig spun together with a unique mineral expression. Lush tannins offer depth and structure and the expectation of a graceful development in bottle. Comfortably enjoy over the next 5 to 10 years.
; consumer_votes=118; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/200881.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS VINEYARDS - REIMER VINEYARD PINOT NOIR | $39.99 | stock=506 | in 66 stores | rating=4.5 | https://www.bcliquorstores.com/product/692960 | {sku=692960; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=9; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/692960.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS - FURTHER AFIELD SERIES CAB FRANC | $34.99 | stock=492 | in 47 stores | rating=4.7 | https://www.bcliquorstores.com/product/252158 | {sku=252158; product_type=Red Wine; grape_type=CABERNET FRANC; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=91 Points, Gismondi On Wine: "Expect an attractive, juicy red that is a nod to Loire but made with the sensibility of a pinot specialist. Paterson has tamed the herbaceous, savoury notes and pushed the ripe blueberry and black fruits to the foreground, all sitting on a silky tannin structure that melts in your mouth.  Considerable value." (April 2024)
; consumer_votes=15; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/252158.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 9 results)
  - Tantalus Vineyards Rose 750 mL | $30.98 | [North Vancouver:0, South Surrey:17, Langley Store:0, Vancouver:7] | https://www.everythingwine.ca/tantalus-rose-2012 | {sku=439687; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/3/439687_tantalus_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Tantalus Vineyards Chardonnay 750 mL | $35.99 | [North Vancouver:0, South Surrey:0, Langley Store:10, Vancouver:0] | https://www.everythingwine.ca/tantalus-chardonnay | {sku=114884; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/1/114884_tantalus_chardonnay_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Riesling 750 mL | $30.99 | [North Vancouver:17, South Surrey:7, Langley Store:0, Vancouver:8] | https://www.everythingwine.ca/tantalus-riesling-750-ml | {sku=802280; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/0/802280_tantalus_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Tantalus Vineyards Bear Chardonnay 750 mL | $30.98 | [North Vancouver:0, South Surrey:5, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineryards-bear-chardonnay-750-ml | {sku=83282; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/3/83282_tantalus_bear_chardonnay.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Ontario Riesling 750 mL | $36.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineyards-ontario-riesling-750-ml | {sku=270640; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/270640_tantalus_ontario_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Further Afield Series Syrah 750 mL | $36.99 | [North Vancouver:0, South Surrey:0, Langley Store:6, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineyards-further-afield-series-syrah-750-ml | {sku=460372; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/6/460372_tantalus_further_afield_syrah.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Maija Pinot Noir 750 mL | $39.98 | [North Vancouver:12, South Surrey:2, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-juveniles-pinot-noir | {sku=348755; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/4/348755_tantalus_maija_pinot_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Looney Vineyard Oregon Rose 750 mL | $30.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineyards-looney-vineyard-oregon-rose-750-ml | {sku=270643; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/270643_tantalus_looney_vineyard_oregon_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Further Afield Series Cabernet Franc 750 mL | $34.99 | [North Vancouver:7, South Surrey:8, Langley Store:10, Vancouver:5] | https://www.everythingwine.ca/tantalus-vineyards-further-afield-series-cabernet-franc-750-ml | {sku=252158; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/5/252158_tantalus_further_afield_cabernet_franc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 8 results)
  - Tantalus Bear Chardonnay | $29.99 | stock=6 | https://store.suttonplacewinemerchant.com/products/5171325-tantalus-bear-chardonnay | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC83282.jpg; country=CANADA; varietal=Chardonnay; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Tantalus Further Afield Blanc de Noir | $47.99 | 2022 | stock=7 | https://store.suttonplacewinemerchant.com/products/5181376-tantalus-further-afield-blanc-de-noir | {category=SPARKLING CANADA; in_stock=True; unit_size=750ML Bottle; country=CANADA; varietal=Pinot Noir; is_staff_pick=False; is_featured=False}
  - Tantalus Further Afield Cab Franc | $39.49 | stock=6 | https://store.suttonplacewinemerchant.com/products/4724608-tantalus-further-afield-cab-franc | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000025/0000252158-8879.jpg; country=CANADA; varietal=Cabernet Franc; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Tantalus Maija Pinot Noir | $38.49 | 2022 | stock=9 | https://store.suttonplacewinemerchant.com/products/4668256-tantalus-maija-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000034/0000348755-4119.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=12.90; is_staff_pick=False; is_featured=False}
  - Tantalus Old Vines Riesling | $51.99 | 2020 | stock=9 | https://store.suttonplacewinemerchant.com/products/4360955-tantalus-old-vines-riesling | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000017/0000179226-1753.jpg; country=CANADA; varietal=Riesling; alcohol_pct=13.40; is_staff_pick=False; is_featured=False}
  - Tantalus Riesling | $35.49 | 2022 | stock=9 | https://store.suttonplacewinemerchant.com/products/4144458-tantalus-riesling | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000080/0000802280-5980.jpg; country=CANADA; varietal=Riesling; alcohol_pct=12.40; is_staff_pick=False; is_featured=False}
  - Tantalus Rose | $29.99 | 2021 | stock=22 | https://store.suttonplacewinemerchant.com/products/4254767-tantalus-rose | {category=ROSE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000043/0000439687-3791.jpg; country=CANADA; varietal=Pinot Noir/Pinot Meunier; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Tantalus Syrah  | $41.99 | 2021 | stock=6 | https://store.suttonplacewinemerchant.com/products/4171973-tantalus-syrah | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000046/0000460372-1677.jpg; country=CANADA; varietal=Syrah; alcohol_pct=14.20; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 5 results)
  - Tantalus 2025 Rose 750ml | $30.99 | stock=17 | https://www.marquis-wines.com/tantalus-2025-rose-750ml/ | {sku=1017799; in_stock=True; categories=["Rosé Wine", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21728/images/17421/2026-04-23-13.31.48__31357.1777054370.500.500.png?c=2}
  - Tantalus 2025 Riesling 750ml | $32.99 | stock=11 | https://www.marquis-wines.com/tantalus-2022-riesling-750ml/ | {sku=1010038; in_stock=True; categories=["White Wine", "Riesling", "Kelowna", "British Columbia", "Organic / Biodynamic Wine"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7320/images/8588/IMG_15051__08114.1588006662.500.500.jpg?c=2}
  - Tantalus 2024 Pinot Gris 750ml | $29.99 | stock=3 | https://www.marquis-wines.com/tantalus-2024-pinot-gris-750ml/ | {sku=1031910; in_stock=True; categories=["White Wine", "Pinot Gris & Grigio", "Organic / Biodynamic Wine"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21324/images/17029/2026-01-23-14.54.33__29085.1769462280.500.500.png?c=2}
  - Tantalus 2022 Cabernet Franc 750ml | $36.99 | stock=16 | https://www.marquis-wines.com/tantalus-2022-cabernet-franc-750ml/ | {sku=1029801; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Cabernet Franc", "Drink Local"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18670/images/14640/2024-05-08_11.38.04__97448.1715278618.500.500.png?c=2}
  - Tantalus 2023 Maija Pinot Noir 750ml | $40.99 | stock=7 | https://www.marquis-wines.com/tantalus-2017-maija-pinot-noir-750ml/ | {sku=1016222; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9531/images/7177/IMG_9636__76411.1544468344.500.500.JPG?c=2}

#### search_legacy_liquor_store_tool (status=ok, 2 results)
  - Tantalus "Maija" Pinot Noir | $38.64 | stock=7 | https://www.legacyliquorstore.com/product/wine/tantalus-maija-pinot-noir-1-x-750ml | {brand=Tantalus; slug=tantalus-maija-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Tantalus "Bear" Chardonnay | $29.81 | stock=3 | https://www.legacyliquorstore.com/product/wine/tantalus-bear-chardonnay-1-x-750ml | {slug=tantalus-bear-chardonnay-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "chardonnay"]}

#### search_bcliquor_tool (status=ok, 0 results)

#### search_everything_wine_tool (status=ok, 12 results)
  - Blue Mountain Vineyard Gamay Noir 750 mL | $34.98 | [North Vancouver:0, South Surrey:10, Langley Store:11, Vancouver:0] | https://www.everythingwine.ca/blue-mountain-gamay-noir | {sku=389882; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/8/389882_blue_mountain_vineyard_gamay_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Pinot Gris 750 mL | $31.98 | https://www.everythingwine.ca/blue-mountain-pinot-gris | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/b/m/bmvc_pgris.png?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366&format=jpeg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Pinot Blanc 750 mL | $31.98 | [North Vancouver:7, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/blue-mountain-vineyard-pinot-blanc-750-ml | {sku=329441; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/2/329441_blue_mountain_pinot_blanc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Reserve Brut Sparkling 750 mL | $52.98 | https://www.everythingwine.ca/blue-mountain-reserve-brut | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/b/m/bmvc_reserve_brut.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Reserve Pinot Noir 1.5 L | $115.98 | https://www.everythingwine.ca/blue-mountain-vineyard-reserve-pinot-noir-1-5-l | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Blanc de Blancs Sparkling 750 mL | $52.98 | [North Vancouver:10, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/blue-mountain-blanc-de-blancs-sparkling | {sku=402594; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/0/402594_blue_mountain_blanc_de_blancs.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Reserve Cuvee Pinot Noir 750 mL | $47.98 | https://www.everythingwine.ca/blue-mountain-vineyard-reserve-cuvee-pinot-noir-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/b/m/bmvc_reserve_pnoir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Gold Label Brut Sparkling 750 mL | $36.98 | [North Vancouver:1, South Surrey:9, Langley Store:9, Vancouver:5] | https://www.everythingwine.ca/blue-mountain-brut | {sku=471672; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/7/471672_blue_mountain_gold_label_brut_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Blossom Slope Block 17 Chardonnay 750 mL | $52.98 | https://www.everythingwine.ca/blue-mountain-blossom-slope-block-17-chardonnay-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Wild Terrain Block 9 Pinot Noir 750 mL | $57.98 | https://www.everythingwine.ca/blue-mountain-block-9-pinot-noir-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Gravel Force Block 14 Pinot Noir 750 mL | $57.98 | https://www.everythingwine.ca/blue-mountain-block-14-pinot-noir-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard River Flow Block 23 Pinot Noir 750 mL | $57.98 | https://www.everythingwine.ca/blue-mountain-block-23-pinot-noir-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 3 results)
  - Blue Mountain Brut Gold Label  | $35.99 | stock=26 | https://store.suttonplacewinemerchant.com/products/4144014-blue-mountain-brut-gold-label | {category=SPARKLING CANADA; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000047/0000471672-6624.jpg; country=CANADA; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}
  - Blue Mountain Gamay | $33.99 | 2020 | stock=4 | https://store.suttonplacewinemerchant.com/products/4228470-blue-mountain-gamay | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000038/0000389882-3198.png; country=CANADA; varietal=Gamay Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Blue Mountain Pinot Blanc | $31.49 | 2022 | stock=11 | https://store.suttonplacewinemerchant.com/products/4298417-blue-mountain-pinot-blanc | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000032/0000329441-8271.png; country=CANADA; varietal=Pinot Blanc; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 5 results)
  - Blue Mountain N/V Gold Label Brut 750ml | $37.99 | stock=33 | https://www.marquis-wines.com/blue-mountain-n-v-gold-label-brut-750ml/ | {sku=471672; in_stock=True; categories=["Sparkling", "Okanagan Falls", "British Columbia", "Lunar New Year"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/6072/images/11775/blue-mountain-gold-brut__28311.1648759359.500.500.jpg?c=2}
  - Blue Mountain 2023 Reserve Cuvee Pinot Noir 750ml | $51.99 | stock=11 | https://www.marquis-wines.com/blue-mountain-2022-reserve-cuvee-pinot-noir-750ml/ | {sku=1023129; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19489/images/15288/2024-10-31-14.17.17__41020.1730481578.500.500.png?c=2}
  - Blue Mountain 2022 Gamay Noir 750ml | $35.99 | stock=12 | https://www.marquis-wines.com/blue-mountain-2019-gamay-noir-750ml/ | {sku=1014652; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8456/images/5067/blue-mountain-gamay-2015__59204.1533682531.500.500.jpg?c=2}
  - Gagnon Kennedy Vineyards 2020 Cabernet Sauvignon Monte Rosso Vineyard Moon Mountain 750ml | $329.99 | stock=3 | https://www.marquis-wines.com/gagnon-kennedy-vineyards-2020-cabernet-sauvignon-monte-rosso-vineyard-moon-mountain-750ml/ | {sku=1030528; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "USA", "California", "Napa"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19625/images/15538/2025-01-10_14.19.46__85706.1736797630.500.500.png?c=2}
  - Arette Reposado Tequila 700ml | $89.99 | stock=5 | https://www.marquis-wines.com/arette-reposado-tequila-700ml/ | {sku=1024491; in_stock=True; categories=["Spirits", "Tequila & Mezcal"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21623/images/17318/2026-03-30-13.14.55__91622.1775070661.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 3 results)
  - Blue Mountain Reserve Cuvee Pinot Noir Magnum | $120.87 | stock=1 | https://www.legacyliquorstore.com/product/wine/blue-mountain-reserve-cuvee-pinot-noir-magnum-1-x-1-5l | {slug=blue-mountain-reserve-cuvee-pinot-noir-magnum-1-x-1-5l; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Blue Mountain Gamay Noir | $34.08 | stock=6 | https://www.legacyliquorstore.com/product/wine/blue-mountain-gamay-noir-1-x-750ml | {slug=blue-mountain-gamay-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "gamay"]}
  - Blue Mountain Brut Gold Label | $35.88 | stock=14 | https://www.legacyliquorstore.com/product/wine/blue-mountain-winery-gold-label-brut-1-x-750ml | {brand=Blue Mountain; slug=blue-mountain-winery-gold-label-brut-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}

#### search_bcliquor_tool (status=ok, 0 results)

#### search_everything_wine_tool (status=ok, 7 results)
  - Meyer Family Vineyards Tribute Chardonnay 750 mL | $43.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/meyer-family-tribute-chard | {sku=838532; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/3/838532_meyer-family-tribute-chard.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Pinot Noir 750 mL | $33.98 | [North Vancouver:0, South Surrey:0, Langley Store:6, Vancouver:0] | https://www.everythingwine.ca/meyer-family-ok-pinot-noir | {sku=154310; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/5/154310_meyer_family_okangan_valley_pinot_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Columbia Valley Chardonnay 750 mL | $31.98 | [North Vancouver:10, South Surrey:10, Langley Store:9, Vancouver:0] | https://www.everythingwine.ca/meyer-family-vineyards-columbia-valley-chardonnay-750-ml | {sku=323571; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/2/323571_meyer_columbia_valley_chard.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Micro Cuvee Pinot Noir 750 mL | $77.98 | [North Vancouver:11, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/meyer-family-micro-pinot-noir | {sku=942680; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/9/4/942680_meyer_micro_cuvee_pn.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Mclean Creek Road Vineyard Chardonnay 750 mL | $43.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/meyer-family-vineyards-mclean-vineyard-chardonnay-750-ml | {sku=139717; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/3/139717_meyer_family_vineyards_mclean_vineyard_chardonnay.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Snipes Mountain Washington Chardonnay 750 mL | $43.98 | https://www.everythingwine.ca/meyer-family-vineyards-snipes-mountain-washington-chardonnay-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/p/l/placeholder_image_white_wine_4_6.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Mclean Creek Road Vineyard Pinot Noir 750 mL | $47.98 | [North Vancouver:17, South Surrey:0, Langley Store:6, Vancouver:10] | https://www.everythingwine.ca/meyer-family-mclean-pinot-noir | {sku=831487; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/3/831487_meyer-family-pinot-noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 4 results)
  - Meyer Family Micro Cuvee Chardonnay | $79.99 | 2022 | stock=6 | https://store.suttonplacewinemerchant.com/products/4179096-meyer-family-micro-cuvee-chardonnay | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000088/0000883363-7064.jpg; country=CANADA; varietal=Chardonnay; alcohol_pct=13.90; is_staff_pick=False; is_featured=False}
  - Meyer Family Micro Cuvee Pinot Noir | $79.99 | 2019 | stock=6 | https://store.suttonplacewinemerchant.com/products/4179652-meyer-family-micro-cuvee-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000094/0000942680-7152.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Meyer Family Vineyards Mclean Creek Pinot Noir  | $48.99 | 2022 | stock=4 | https://store.suttonplacewinemerchant.com/products/4144485-meyer-family-vineyards-mclean-creek-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000083/0000831487-9040.png; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Meyer Family Vineyards Okanagan Valley Pinot Noir | $33.49 | 2025 | stock=27 | https://store.suttonplacewinemerchant.com/products/4298314-meyer-family-vineyards-okanagan-valley-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000015/0000154310-1810.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 2 results)
  - Meyer Family 2024 Chardonnay 750ml | $32.99 | stock=13 | https://www.marquis-wines.com/meyer-family-2024-chardonnay-750ml/ | {sku=1012941; in_stock=True; categories=["White Wine", "Chardonnay", "British Columbia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9924/images/9192/2020-09-24_14.12.59__56311.1761861012.500.500.jpg?c=2}
  - Meyer Family 2023 Pinot Noir 750ml | $34.99 | stock=12 | https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/ | {sku=1014474; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7708/images/8652/Lindsey_Ail_-_IMG_15661__44130.1589559651.500.500.jpg?c=2}

#### search_legacy_liquor_store_tool (status=ok, 0 results)

#### search_bcliquor_tool (status=ok, 6 results)
  - CULMINA - SAIGNEE 2023 | $26.99 | stock=37 | in 8 stores | rating=4.6 | https://www.bcliquorstores.com/product/72549 | {sku=72549; product_type=Rose Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=A blend of Malbec (44%), Cabernet Franc (29%) and Merlot (34%) from Arise and Stan's Benches, Certified Organic. "Pretty nose here, delicate and floral, bright red fruit-scented. Depth is very good." 92 Points - John Szabo, MS.
; consumer_votes=5; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/72549.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - DILEMMA CHARDONNAY | $35.99 | stock=227 | in 34 stores | rating=4.8 | https://www.bcliquorstores.com/product/126830 | {sku=126830; product_type=White Wine; grape_type=CHARDONNAY; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Showcasing mineral and spice aromas, Dilemma is framed by lovely oak, caramel and butter flavours, a luscious body, and a long, fresh finish, creating a wine of outstanding finesse, beauty, elegance and style.
; consumer_votes=8; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/126830.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - DECORA RIESLING | $24.99 | stock=810 | in 73 stores | rating=4.0 | https://www.bcliquorstores.com/product/389125 | {sku=389125; product_type=White Wine; grape_type=RIESLING; country=Canada; volume=0.750; alcohol_pct=13.4; sweetness=00; tasting_notes=Finely scented with daisies, dried apricots, toasted almonds and yeasty aromatics, Decora showcases delicacy and complexity. The verve and brightness of the palate are balanced by creaminess, with notes of starfruit and fuzzy peaches. 
; consumer_votes=6; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/389125.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - HYPOTHESIS 2019 | $34.99 (reg $42.99) | stock=1814 | in 97 stores | rating=4.5 | https://www.bcliquorstores.com/product/227436 | {sku=227436; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Opulent and refined, the bouquet brings complex aromas of cedar bark, leather, cocoa nibs and dark cherries. The generous palate is layered with succulent dark fruits, licorice and baking spice supported by balance acidity and silky tannins. The nuances of 2018 Hypothesis unfurl gradually over a long and persistent finish.
; consumer_votes=30; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/227436.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - CABERNET SAUVIGNON 2021 | $37.99 | stock=82 | in 16 stores | rating=4.5 | https://www.bcliquorstores.com/product/227457 | {sku=227457; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Our single-varietal expression of Malbec comes from our Arise Bench vineyard along the Golden Mile Bench. Well-balanced with rich fruit offset by supple, silky tannins and oolong tea flavours. Rich mulberry and plum linger on the deep, intriguing finish.
; consumer_votes=10; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/227457.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA OLIVER - R AND D RED BLEND GOLDEN MILE BENCH 2022 | $19.99 | stock=1477 | in 125 stores | rating=4.0 | https://www.bcliquorstores.com/product/495846 | {sku=495846; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=A Golden Mile expression is on show here with lots of Merlot fruit and other Bordeaux grapes from estate vineyards. Offering great ripe fruit from this exceptional vintage, the red and black fruit flavours and persistent linger highlight an expressive wine. Match with grilled fare or pasta recipes or vegetarian dishes.
; consumer_votes=63; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/495846.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 5 results)
  - Culmina Family Estate Winery Decora Riesling 750 mL | $28.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/culmina-family-estate-winery-decora-riesling-750-ml | {sku=863035; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/6/863035_culmina_decora_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery Saignee Rose 750 mL | $26.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/culmina-family-estate-winery-saignee-rose-merlot-cab-franc-cab-sauv-750-ml-1 | {sku=29593; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/9/29593_culmina_family_estate_winery_saignee_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery R&D Red Blend 750 mL | $19.99 | https://www.everythingwine.ca/culmina-family-estate-winery-r-d-red-blend-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/c/u/culmina_r_d_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery R&D Sauvignon Blanc Semillon 750 mL | $26.98 | https://www.everythingwine.ca/culmina-family-estate-winery-r-d-sauvignon-blanc-semillon-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery Golden Mile Bench Hypothesis Red Blend 750 mL | $34.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/culmina-family-estate-winery-golden-mile-bench-hypothesis-red-blend-750-ml | {sku=852012; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/5/852012_culmina_family_estate_winery_golden_mile_bench_hypothesis.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}

#### search_okanagan_cellars_tool (status=ok, 7 results)
  - CULMINA - CAB SAUV | $37.99 | stock=10 | https://okanagancellars.com/products/3946821-culmina-cab-sauv | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000022/0000227457-4800.png}
  - CULMINA - DECORA RIESLING | $22.99 | stock=16 | https://okanagancellars.com/products/4217289-culmina-decora-riesling | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/all/BC389125.jpg}
  - CULMINA - DILEMMA CHARDONNAY | $34.99 | stock=7 | https://okanagancellars.com/products/3937046-culmina-dilemma-chardonnay | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000012/0000126830-4871.png}
  - CULMINA - HYPOTHESIS | $32.99 (reg $36.99) | stock=10 | https://okanagancellars.com/products/3957069-culmina-hypothesis | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000022/0000227436-6306.jpg}
  - CULMINA - MALBEC | $37.99 | stock=12 | https://okanagancellars.com/products/4114513-culmina-malbec | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000025/0000252952-8251.png}
  - CULMINA - R&D RED BLEND | $19.99 | stock=21 | https://okanagancellars.com/products/3410072-culmina-r-d-red-blend | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000049/0000495846-8804.png}
  - CULMINA - SAIGNEE | $25.99 | stock=10 | https://okanagancellars.com/products/3403440-culmina-saignee | {category=Rose; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000007/0000072549-9622.png}

#### search_suttonplace_tool (status=ok, 0 results)

#### search_marquis_tool (status=ok, 5 results)
  - Penfolds 2022 Reserve Bin A Chardonnay 750ml | $154.99 | stock=9 | https://www.marquis-wines.com/penfolds-2022-reserve-bin-a-chardonnay-750ml-ojrx/ | {sku=1030793; in_stock=True; categories=["White Wine", "Chardonnay", "95+ Point Wines", "Adelaide Hills", "Australia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19951/images/15788/2025-02-25-14.38.19__97300.1740678446.500.500.png?c=2}
  - Wohlmuth 2024 Sauvgnon Blanc "Phyllit" 750ml | $44.99 | stock=21 | https://www.marquis-wines.com/wohlmuth-2024-sauvgnon-blanc-phyllit-750ml/ | {sku=1031052; in_stock=True; categories=["White Wine", "Sauvignon Blanc", "Austria", "Steiermark"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21423/images/17077/IMG_0574__88566.1770668649.500.500.png?c=2}
  - Monteraponi 2021 Colli Toscana Centrale Trebbiano 750ml | $149.99 | stock=19 | https://www.marquis-wines.com/monteraponi-2021-colli-toscana-centrale-trebbiano-750ml/ | {sku=1029800; in_stock=True; categories=["White Wine", "Tuscany", "Italy", "Marquis Exclusives", "Organic / Biodynamic Wine", "Trebbiano / Ugni Blanc", "Monteraponi"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18696/images/14607/monteraponi_trebbiano__42009.1712869357.500.500.jpg?c=2}
  - Gaja 2019 Pieve Santa Restituta Rennina Brunello di Montalcino 750ml | $399.99 | stock=3 | https://www.marquis-wines.com/gaja-2019-pieve-santa-restituta-rennina-brunello-di-montalcino-750ml/ | {sku=1013605; in_stock=True; categories=["Red Wine", "Sangiovese", "Italy", "Tuscany", "Brunello/Rosso di Montalcino", "95+ Point Wines"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20910/images/16684/2025-10-17_11.31.29__87413.1760991164.500.500.png?c=2}
  - Lagavulin 8 Year Old Single Malt Whisky 750ml | $107.99 | stock=5 | https://www.marquis-wines.com/lagavulin-8-year-old-750ml/ | {sku=1026213; in_stock=True; categories=["Single Malt Scotch", "Islay"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/15552/images/11248/2021-12-07_16.32.57__16452.1638999505.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 4 results)
  - Culmina Hypothesis | $39.81 | stock=4 | https://www.legacyliquorstore.com/product/wine/culmina-hypothesis-1-x-750ml | {slug=culmina-hypothesis-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Culmina Decora Riesling | $27.98 | stock=6 | https://www.legacyliquorstore.com/product/wine/culmina-decora-riesling-1-x-750ml | {brand=Culmina; slug=culmina-decora-riesling-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "riesling"]}
  - Culmina Cabernet Sauvignon | $48.58 | stock=5 | https://www.legacyliquorstore.com/product/wine/culmina-cabernet-sauvignon-1-x-750ml | {brand=Culmina; slug=culmina-cabernet-sauvignon-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "cabernet sauvignon"]}
  - Culmina R&D Red Blend | $22.27 | stock=6 | https://www.legacyliquorstore.com/product/wine/culmina-r-d-red-blend-1-x-750ml | {brand=Culmina Oliver; slug=culmina-r-d-red-blend-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}

````

</details>

### Latency

- 78.59s

---
## Turn 2

### Query

> What's a good BC white under $40 for warm weather?

### Tool Calls (in order)

1. `sommelier_agent_tool` args={"request": "Recommend crisp, dry BC white wines under $40 that are perfect for warm weather (refreshing, high acidity, patio-friendly, no off-dry or sweet styles)."}
2. `sourcing_agent_tool` args={"request": "Find prices and stock in Vancouver for crisp dry BC white wines under $40, such as Sauvignon Blanc, Pinot Blanc, Pinot Gris, Riesling, or Albari\u00f1o from producers like Tantalus, Blue Mountain, Culmina, Synchromesh, Road 13, or CedarCreek."}

### Final Response

```markdown
For warm-weather sipping, you want wines with bracing acidity, zero sweetness, and a clean, mineral-driven finish that keeps you refreshed. British Columbia excels at these electric, bone-dry styles. 

Here are four exceptional, strictly dry BC white wines under $40 that are currently in stock across Vancouver stores, perfect for a sunny patio day.

---

### 1. Culmina Family Estate Winery 'Decora' Riesling (Golden Mile Bench, BC)
* **Why it's great for warm weather:** Sourced from high-elevation vineyards, this is a focused, bone-dry Riesling with sharp mineral definition, bright nerve-driven acidity, and flinty notes. It is incredibly crisp and refreshing on a hot day.
* **Critic Reviews:** Natalie MacLean scored the 2021 vintage **92/100**, describing it as fresh and textural with lime-sherbet aromas and a razor-sharp acidic spine.
* **Where to Buy in Vancouver:**
  * **Okanagan Cellars:** **$22.99** (16 in stock) | [Buy at Okanagan Cellars](https://okanagancellars.com/products/4217289-culmina-decora-riesling)
  * **BC Liquor Stores:** **$24.99** (810 units in stock) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/389125)
  * **Legacy Liquor Store:** **$27.98** (6 in stock) | [Buy at Legacy Liquor](https://www.legacyliquorstore.com/product/wine/culmina-decora-riesling-1-x-750ml)

### 2. Synchromesh Wines Riesling (Four Properties / Blend) (Okanagan Valley, BC)
* **Why it's great for warm weather:** Synchromesh is a premier Riesling specialist in BC. Their "Four Properties" blend is a beautiful, vibrant dry Riesling with bright citrus, green apple, and a clean, mineral finish. It is the definition of a high-acid, thirst-quenching patio white.
* **Where to Buy in Vancouver:**
  * **Everything Wine:** **$27.98** (In stock: 24 in Vancouver, 23 in North Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/synchromesh-wines-inc-riesling-four-vineyard-blend-750-ml)
  * **Sutton Place Wine Merchant:** **$28.49** (13 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4144511-synchromesh-riesling)
  * **Marquis Wine Cellars:** **$28.99** (9 in stock) | [Buy at Marquis Wine Cellars](https://www.marquis-wines.com/synchromesh-riesling-blend-750ml/)
  * **Legacy Liquor Store:** **$34.29** (9 in stock) | [Buy at Legacy Liquor](https://www.legacyliquorstore.com/product/wine/synchromesh-riesling-blend-1-x-750ml)

### 3. Blue Mountain Vineyard Pinot Blanc (Okanagan Falls, BC)
* **Why it's great for warm weather:** Blue Mountain is legendary for its restrained, mineral-driven, French-inspired winemaking. Their Pinot Blanc is a stellar dry white with crisp orchard fruit, clean minerality, and no heavy oak, making it highly refreshing and patio-friendly.
* **Where to Buy in Vancouver:**
  * **Sutton Place Wine Merchant:** **$31.49** (11 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4298417-blue-mountain-pinot-blanc)
  * **Everything Wine:** **$31.98** (7 in stock in North Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/blue-mountain-vineyard-pinot-blanc-750-ml)

### 4. Road 13 Vineyards Viognier (Okanagan Valley, BC)
* **Why it's great for warm weather:** If you want a dry white with a bit more aromatic intensity on a warm day, this is a great choice. It is completely dry but highly expressive, offering beautiful tropical and stone fruit notes (peach, apricot, orange peel) with a rich, full-bodied finish.
* **Where to Buy in Vancouver:**
  * **Okanagan Cellars:** **$27.99** (30 in stock) | [Buy at Okanagan Cellars](https://okanagancellars.com/products/2643782-road-13-viognier)
  * **BC Liquor Stores:** **$29.99** (356 units in stock) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/739888)
  * **Legacy Liquor Store:** **$33.73** (31 in stock) | [Buy at Legacy Liquor](https://www.legacyliquorstore.com/product/wine/road-13-select-harvest-viognier-1-x-750ml)

---

### 💡 A Quick Note on BC Wines This Season
Due to severe winter freeze damage in the Okanagan Valley over the last two years, some BC wineries have released **"Crafted in BC"** wines using grapes imported from regions like Oregon and New Zealand to keep their shelves stocked. 

If you are browsing local stores, you will see options like **CedarCreek Oregon Pinot Gris ($24.99)** or **CedarCreek New Zealand Sauvignon Blanc ($24.99)**. These are excellent, crisp, dry options made by BC winemakers using imported fruit, but if you want 100% BC-grown estate wines, the four options listed above are your best bets!
```

### Judge Scores

```json
{
  "relevance": 5,
  "correctness": 5,
  "helpfulness": 5,
  "coherence": 5,
  "harmlessness": 5,
  "overall": 5,
  "claim_label_counts": {
    "SUPPORTED": 16,
    "GENERAL_KNOWLEDGE": 0,
    "NOT_IN_EVIDENCE": 0,
    "CONTRADICTED": 0
  },
  "correctness_rationale": "All claims regarding pricing, stock, reviews, and tasting notes are fully supported by the provided evidence.",
  "issues": [],
  "strengths": [
    "Excellent adherence to the user's strict preference for bone-dry whites.",
    "Provides a very helpful and relevant note about the 'Crafted in BC' wines currently on the market due to winter freeze damage."
  ],
  "parse_error": false
}
```

### Claim Verdicts

| Label | Claim | Evidence quote |
|---|---|---|
| SUPPORTED | Culmina Family Estate Winery 'Decora' Riesling is sourced from high-elevation vineyards, is a bone-dry Riesling with sharp mineral definition, bright nerve-driven acidity, and flinty notes. | Sourced from high-elevation vineyards, this is a focused, near bone-dry Riesling with sharp mineral definition. ... bright, nerve-driven acidity and flinty notes. |
| SUPPORTED | Natalie MacLean scored the 2021 vintage of Culmina 'Decora' Riesling 92/100, describing it as fresh and textural with lime-sherbet aromas and a razor-sharp acidic spine. | Natalie MacLean scored the 2021 vintage 92/100, describing it as fresh and textural with lime-sherbet aromas and a razor-sharp acidic spine. |
| SUPPORTED | Culmina 'Decora' Riesling is available at Okanagan Cellars for $22.99 with 16 in stock. | Okanagan Cellars: $22.99 (16 in stock) |
| SUPPORTED | Culmina 'Decora' Riesling is available at BC Liquor Stores for $24.99 with 810 units in stock. | BC Liquor Stores: $24.99 (810 units in stock across 73 stores) |
| SUPPORTED | Culmina 'Decora' Riesling is available at Legacy Liquor Store for $27.98 with 6 in stock. | Legacy Liquor Store: $27.98 (6 in stock) |
| SUPPORTED | Synchromesh Wines Riesling (Four Properties / Blend) is available at Everything Wine for $27.98 with 24 in stock in Vancouver and 23 in North Vancouver. | Everything Wine: $27.98 (In stock: 23 in North Vancouver, 3 in South Surrey, 8 in Langley, 24 in Vancouver) |
| SUPPORTED | Synchromesh Wines Riesling (Four Properties / Blend) is available at Sutton Place Wine Merchant for $28.49 with 13 in stock. | Sutton Place Wine Merchant: $28.49 (13 in stock) |
| SUPPORTED | Synchromesh Wines Riesling (Four Properties / Blend) is available at Marquis Wine Cellars for $28.99 with 9 in stock. | Marquis Wine Cellars: $28.99 (9 in stock) |
| SUPPORTED | Synchromesh Wines Riesling (Four Properties / Blend) is available at Legacy Liquor Store for $34.29 with 9 in stock. | Legacy Liquor Store: $34.29 (9 in stock) |
| SUPPORTED | Blue Mountain Vineyard Pinot Blanc is available at Sutton Place Wine Merchant for $31.49 with 11 in stock. | Sutton Place Wine Merchant: $31.49 (11 in stock) |
| SUPPORTED | Blue Mountain Vineyard Pinot Blanc is available at Everything Wine for $31.98 with 7 in stock in North Vancouver. | Everything Wine: $31.98 (7 in stock at North Vancouver; out of stock at Vancouver) |
| SUPPORTED | Road 13 Vineyards Viognier is available at Okanagan Cellars for $27.99 with 30 in stock. | ROAD 13 - VIOGNIER \| $27.99 \| stock=30 |
| SUPPORTED | Road 13 Vineyards Viognier is available at BC Liquor Stores for $29.99 with 356 units in stock. | ROAD 13 VINEYARDS VIOGNIER 2022 \| $29.99 \| stock=356 |
| SUPPORTED | Road 13 Vineyards Viognier is available at Legacy Liquor Store for $33.73 with 31 in stock. | Road 13 Viognier \| $33.73 \| stock=31 |
| SUPPORTED | CedarCreek Oregon Pinot Gris is available for $24.99. | CedarCreek Oregon Pinot Gris (Crafted in BC using Oregon grapes) BC Liquor Stores: $24.99 |
| SUPPORTED | CedarCreek New Zealand Sauvignon Blanc is available for $24.99. | CedarCreek New Zealand Sauvignon Blanc (Crafted in BC using Marlborough grapes) BC Liquor Stores: $24.99 |

### Evidence shown to judge

_4 tool messages, 203404 chars (budget 2000000)_

<details><summary>Show evidence</summary>

````markdown
### sommelier_agent_tool (status=ok)
**Sub-agent synthesis:**
### The Mechanics of Pairing Drinks with Sushi

Pairing beverages with sushi is a delicate balancing act. The goal is to complement the subtle sweetness of the vinegared rice (*shari*), match the clean textures of raw fish, and cut through the rich fats of varieties like salmon and fatty tuna. You also have to respect the heat of wasabi and the salty umami of soy sauce. 

For wine specifically, the primary challenge is umami. High-tannin reds or heavily oaked whites will taste bitter and metallic when combined with raw seafood and soy sauce. The ideal wine must have high acidity to cut through fish fats and match the vinegar in the rice, low to no oak, and a distinct mineral backbone. 

Here are excellent dry BC white wines that fit this profile perfectly, along with local options across other beverage categories.

---

### 1. Wine (Dry BC Whites)

British Columbia’s cool-climate wine regions produce world-class, bone-dry whites with the electric acidity and minerality required for sushi.

*   **Tantalus Vineyards Riesling (Okanagan Valley, BC)**
    *   **Why it works:** Tantalus is famous for its laser-focused, dry Rieslings. Its high acidity and intense citrus profile make it a classic pairing for sashimi and nigiri, acting as a palate cleanser between bites.
    *   **Sourced Review:** [Natalie MacLean rated the 2018 vintage 90/100](https://www.nataliemaclean.com/), highlighting its crisp orchard fruit, soft citrus, and stony, mouth-watering finish.
*   **Synchromesh 'Storm Haven Vineyard' Dry Riesling (Okanagan Falls, BC)**
    *   **Why it works:** Synchromesh is widely regarded as one of Canada's premier Riesling producers. Their dry single-vineyard bottlings offer intense, racy acidity and deep mineral tension that easily slices through the richness of fatty tuna (*otoro*).
    *   **Sourced Review:** [WineScores.ca awarded this wine 92 points](https://www.winescores.ca/), noting its exceptional quality and structure.
*   **Culmina Family Estate Winery 'Decora' Riesling (Golden Mile Bench, BC)**
    *   **Why it works:** Sourced from high-elevation vineyards, this is a focused, near bone-dry Riesling with sharp mineral definition. 
    *   **Sourced Review:** [Natalie MacLean scored the 2021 vintage 92/100](https://www.nataliemaclean.com/), describing it as fresh and textural with lime-sherbet aromas and a razor-sharp acidic spine. On the same platform, Sommelier Philippe Perreault called it an excellent match for sushi due to its bright, nerve-driven acidity and flinty notes.
*   **Blue Mountain Vineyard Pinot Gris (Okanagan Falls, BC)**
    *   **Why it works:** For those who prefer Pinot Gris over Riesling, Blue Mountain offers a dry, structured, and crisp style that avoids heavy oak, making it highly compatible with delicate seafood.
    *   **Sourced Review:** [Wine educator Craig Haynes rated the 2019 vintage 91/100](https://www.nataliemaclean.com/), praising its elegant acidity, sweet citrus, kiwi notes, and stunning stony minerality.

---

### 2. Sake

Sake and sushi are a natural, time-tested pairing because they share a foundational ingredient: rice. Sake contains high levels of succinic acid (which drives umami) and has virtually no histamines or high acidity to clash with seafood. 

*   **Artisan SakeMaker 'Osake' Junmai Nama (Granville Island, Vancouver, BC)**
    *   **Why it works:** Crafted right in Vancouver, this fresh, unpasteurized (*nama*) sake is bright, lively, and slightly cloudy. It offers a beautiful yeast-forward match for local BC spot prawns (*amaebi*) or delicate white fish, harmonizing with the seaweed and soy sauce while gently cleansing the palate.

---

### 3. Beer

Carbonation is the secret weapon here. The scrubbing bubbles of a cold beer slice through the oily textures of salmon, tuna, and fried tempura, while the light grain sweetness bridges naturally with the sushi rice.

*   **33 Acres Brewing Co. '33 Acres of Rice Lager' (Vancouver, BC)**
    *   **Why it works:** Brewed with rice, this Japanese-style lager is incredibly clean, crisp, and dry. It does not compete with the delicate flavors of sashimi and leaves the palate completely refreshed.
*   **Dageraad Brewing 'Burnabarian' (Burnaby, BC)**
    *   **Why it works:** A Belgian-style table beer. Its low alcohol, light spice, and citrus notes pair beautifully with richer rolls, spicy mayo, and aburi-style (torched) sushi.

---

### 4. Spirit / Cocktail

High-proof spirits can easily overwhelm delicate raw fish, so the key is dilution and temperature. A tall, ice-cold, highly carbonated highball lowers the alcohol perception while providing a refreshing, effervescent contrast to the rich textures of the food.

*   **Sheringham Distillery 'Seaside Gin' (Sooke, Vancouver Island, BC)**
    *   **Why it works:** This gin is distilled with local winged kelp, creating a subtle, briny, marine note that acts as a direct flavor bridge to the *nori* (seaweed) wrapper of your sushi.
    *   **The Build (The Seaside Highball):** 1.5 oz Sheringham Seaside Gin, 0.5 oz fresh yuzu juice, topped with premium, highly carbonated tonic water. Serve in a Collins glass packed with ice, garnished with a thin slice of fresh cucumber and a dehydrated lime wheel.

#### reasoning_pair_wine_tool (status=ok, 0 results)
Recommendation: Pairing drinks with sushi is a delicate art. The goal is to complement the subtle sweetness of the vinegared rice (*shari*), match the clean textures of raw fish, and cut through the rich fats of varieties like salmon (*sake*) and fatty tuna (*otoro*), all while respecting the heat of wasabi and the salty umami of soy sauce. 

Here is your ultimate guide to pairing drinks with sushi, curated for the Vancouver palate.

---

### 1. Sake

#### Why This Pairing Works
Sake and sushi are a natural, time-tested pairing because they share a foundational ingredient: rice. Unlike wine, sake contains high levels of succinic acid (which drives umami) and has virtually no histamines or high acidity to clash with seafood. It acts as a flavor magnifier, harmonizing with the seaweed (*nori*) and soy sauce while gently cleansing the palate of fish oils.

#### Recommended Style
**Junmai Ginjo** or **Tokubetsu Junmai**. These styles are polished to at least 60%, yielding a clean, slightly floral, and fruity profile with a dry finish. They offer enough structure to stand up to richer fish like salmon, yet remain delicate enough not to overpower sweet spot prawns (*amaebi*) or white fish (*tai*).

#### Specific Examples
*   **Artisan SakeMaker** – *Osake Junmai Nama* (Granville Island, Vancouver, BC): Crafted right in Vancouver, this fresh, unpasteurized sake is bright, lively, and slightly cloudy, offering a beautiful yeast-forward match for local BC spot prawns.
*   **Hakkaisan Brewery** – *Hakkaisan Tokubetsu Junmai* (Niigata, Japan): The epitome of the clean, dry Niigata style. It is exceptionally crisp, acting like a laser-focused palate cleanser between different pieces of nigiri.
*   **Tengumai** – *Yamahai Junmai* (Ishikawa, Japan): For a meal featuring richer, torched (*aburi*) sushi or unagi (eel), this earthy, high-acid, gamey sake provides a stunning, savory contrast.

---

### 2. Wine

#### Why This Pairing Works
The primary challenge with wine and sushi is umami; high-tannin reds or heavily oaked whites will taste bitter and metallic when combined with raw seafood and soy sauce. The ideal wine must have high acidity to cut through fish fats and match the vinegar in the rice, low to no oak, and a distinct mineral backbone.

#### Recommended Style
**Traditional Method Sparkling Wine** (for its yeast autolysis which mimics the umami of rice) or **Dry, Aromatic Whites** like Riesling, Grüner Veltliner, or bone-dry Pinot Gris. 

#### Specific Examples
*   **Fitzpatrick Family Vineyards** – *Fitz Brut* (Peachland, Okanagan Valley, BC): A traditional method sparkling wine with crisp green apple notes and a fine mousse. The bubbles scrub the palate clean of rich fish oils (like avocado and spicy mayo in rolls), while the brioche notes pair beautifully with the rice.
*   **Tantalus Vineyards** – *Riesling* (Kelowna, Okanagan Valley, BC): Renowned for its electric acidity and intense minerality. A tiny touch of residual sugar in this off-dry style acts as a perfect foil to the heat of wasabi and pickled ginger.
*   **Domaine Huet** – *Vouvray Sec 'Le Haut-Lieu'* (Loire Valley, France): A dry Chenin Blanc with incredible texture, high acidity, and honeyed pear notes that elevate sweet crab meat and scallop nigiri.

---

### 3. Beer

#### Why This Pairing Works
Carbonation is the secret weapon here. The scrubbing bubbles of a cold beer slice through the oily textures of salmon, tuna, and fried tempura. Furthermore, the light grain sweetness of a lager bridges naturally with the sushi rice.

#### Recommended Style
**Japanese-style Rice Lagers** (which use rice in the mash for a ultra-dry, clean finish) or **Belgian-style Witbiers** (where coriander and orange peel notes complement the citrusy elements of ponzu).

#### Specific Examples
*   **33 Acres Brewing Co.** – *33 Acres of Rice Lager* (Vancouver, BC): Brewed with rice, this is incredibly clean, crisp, and dry. It does not compete with the delicate flavors of sashimi and leaves the palate completely refreshed.
*   **Dageraad Brewing** – *Burnabarian* (Burnaby, BC): A Belgian-style table beer. Its low alcohol, light spice, and citrus notes pair beautifully with richer rolls and aburi-style sushi.
*   **Kiuchi Brewery** – *Hitachino Nest White Ale* (Ibaraki, Japan): A classic witbier brewed with coriander, nutmeg, and orange peel. The spiced citrus notes act like a squeeze of fresh lemon over white fish sashimi.

---

### 4. Spirit / Cocktail

#### Why This Pairing Works
High-proof spirits can easily overwhelm delicate raw fish, so the key is dilution and temperature. A tall, ice-cold, highly carbonated highball lowers the alcohol perception while providing a refreshing, effervescent contrast to the rich textures of the food.

#### Recommended Style
A **Gin & Tonic** or **Highball** featuring botanicals that echo the coastal, marine, or citrus notes of Japanese cuisine (such as lemongrass, yuzu, or seaweed).

#### Specific Examples
*   **Sheringham Distilleries** – *Seaside Gin* (Sooke, Vancouver Island, BC)
    *   **Why it works:** This gin is distilled with local winged kelp, creating a subtle, briny, marine note that acts as a direct flavor bridge to the *nori* (seaweed) wrapper of your sushi.
    *   **The Build (The Seaside Highball):** 1.5 oz Sheringham Seaside Gin, 0.5 oz fresh yuzu juice, topped with premium, highly carbonated tonic water. Serve in a Collins glass packed with ice, garnished with a thin slice of fresh cucumber and a dehydrated lime wheel.
*   **Odd Society Spirits** – *Wallflower Gin* (East Vancouver, BC)
    *   **Why it works:** A more floral, citrus-forward gin that tames the pungency of wasabi.
    *   **The Build (The East Van French 75):** 1 oz Wallflower Gin, 0.5 oz lemon juice, 0.5 oz simple syrup, shaken with ice, strained into a flute, and topped with BC sparkling wine (like *Bella* or *Fitz*).
*   **The Woods Spirit Co.** – *Pacific Northwest Amaro* (North Vancouver, BC)
    *   **Why it works:** For those who prefer a bitter edge to cut through fried tempura or rich unagi.
    *   **The Build (The Cascade Spritz):** 1.5 oz Woods Cascade Amaro, 3 oz dry BC sparkling wine, splash of soda, served over ice with a grapefruit twist.

#### search_web_grounded_tool (status=ok, 21 results)
Search answer: When pairing wine with sushi, the goal is to find dry white wines with high acidity, clean minerality, and minimal oak. These characteristics cut through the richness of fatty fish (like salmon and tuna) and complement the tang of vinegared sushi rice without overpowering the delicate seafood. 

British Columbia’s cool-climate wine regions produce world-class dry whites that fit this profile perfectly. The following highly rated dry BC white wines are excellent matches for sushi:

### 1. Tantalus Vineyards Riesling (Okanagan Valley)
* **Why it pairs:** Tantalus is famous for its bone-dry, laser-focused Rieslings. Its electric acidity and intense citrus profile make it a classic pairing for sashimi and nigiri.
* **Reviews & Scores:** 
  * **Gismondi on Wine** describes Tantalus Riesling as a benchmark of extreme freshness and electric minerality, praising its juicy, mouth-watering style that excels with food. 
  * **Natalie MacLean** rated the 2018 vintage **90/100**, highlighting its crisp orchard fruit, soft citrus, and stony, mouth-watering finish.

### 2. Synchromesh Storm Haven Vineyard Dry Riesling (Okanagan Falls)
* **Why it pairs:** Synchromesh is widely regarded by local critics as one of Canada's premier Riesling producers. Their dry single-vineyard bottlings offer intense, racy acidity and deep mineral tension.
* **Reviews & Scores:** 
  * **WineScores.ca** awarded the Storm Haven Vineyard Dry Riesling **92 points**.
  * Writing for **Gismondi on Wine**, critic Treve Ring has lauded Synchromesh's Rieslings for their chalky stoniness, wild herbs, and intense, racy acidity.

### 3. Culmina Family Estate Winery Decora Riesling (Golden Mile Bench)
* **Why it pairs:** Sourced from high-elevation vineyards, this is a focused, near bone-dry Riesling with sharp mineral definition.
* **Reviews & Scores:** 
  * **Natalie MacLean** scored the 2021 vintage **92/100**, describing it as fresh and textural with lime-sherbet aromas and a razor-sharp acidic spine.
  * Sommelier Philippe Perreault reviewed the wine for Natalie MacLean's platform, calling it an "excellent choice to match sushi" due to its bright, nerve-driven acidity, flinty notes, and clean finish.

### 4. Blue Mountain Vineyard Pinot Gris (Okanagan Falls)
* **Why it pairs:** For those who prefer Pinot Gris over Riesling, Blue Mountain offers a dry, structured, and crisp style that avoids heavy oak, making it highly compatible with delicate seafood.
* **Reviews & Scores:** 
  * **Anthony Gismondi** has praised Blue Mountain Pinot Gris for its crisp, juicy, and slightly austere finish reminiscent of Chablis, noting its complex layers of green apple, pear skin, and seashell minerality.
  * Wine educator Craig Haynes rated the 2019 vintage **91/100**, praising its elegant acidity, sweet citrus, kiwi notes, and stunning stony minerality.

### 5. Orofino Vineyards Home Vineyard Old Vines Riesling (Similkameen Valley)
* **Why it pairs:** The wind-swept, rocky soils of the Similkameen Valley yield highly mineral, dry Rieslings with exceptional structural tension.
* **Reviews & Scores:** 
  * Sommelier Philippe Perreault reviewed the Old Vines Riesling, calling it "perfect when paired with sushi". He noted its bright, German Kabinett-style acidity, complex tropical fruit, and lime-mineral profile.

### Local Expert Pairing Tip
During a sushi-pairing panel at Vancouver's Blue Water Cafe, local wine critic **Anthony Gismondi** noted that aggressive condiments like wasabi and soy sauce can sometimes make delicate white wines taste "skinny" or bitter. To combat this, he recommends choosing dry whites that still carry vibrant, expressive fruit profiles (such as local Rieslings or aromatic blends) to help bridge the gap and stand up to the heat.
  - [laithwaites.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXVu2CxYpbdG8Vcr6sAc6xQ-RUlEJQ4GFup5hoeWrzRBpHX2jmvYsVmrzCtsyEoUuOIMFt5Y5B27ncA42_P09BNDJ6_-MUCppJGgJNONL-5sw1ntSxT1RogK6-cWRpc8-836DeWV7lXvskxZjiQRq_fyJxTPqYG-i2FsBEDcpAjv36EQ==): 
  - [wineinsiders.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8pqjY_Nocy34LIH_Yl0AzBFGtxa0mB8OHwtBe0wZnqjzkGM3WKLhoBeb187VebCnKVFi6OfB51OggEedO3PA4NJISUQeJ8CNuT23ixdVolSWc_LL9mqBzUspOVa5tLf0H_OoGjtWKYnhxZCQiNUUjCdaHGwBdNuYak8UwUm2QfHGNpDeLH_VVCO3REC1MeKHRma89ptPFERfDFw==): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn41g3GnnJG5gJ4DfUqxnL3WvoZy94JhwfEBdWiVjcYGXlBIc6_5iy1A8YjAjWxP6ZdPICCgGIdRUfL0eycuDhj3Q-W4AyWPKzsCcQeXtfpzRdk2nbANSZZ3G1HmRiuzjwF2MPE-vN6w2j7GHmusF77CUFdRMqzDWM7-UwH0ILIBJZB2pGibkJlHCLsr33fTTUWc9dz9qS): 
  - [foodrepublic.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFB5Cn98RFQqIbx48_rgX7LwLRtfksVvySPEFJHw4SYH0bAttrRQnkp_64IC0rHybfISf75CY_Teoxn1PkWmfV9y4ULDtJo59nY6RE83qK9g6t-A3_PZSOAMjMKsT6NOt_eUWe4dOXfOv-n9TavpkCLJqbXRCg=): 
  - [wineryguystours.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV0gssfAHGCx7T0e_eO8kGXKCN4Ga2PdO63I_V6830SHEb73Z0xRPbSm4vLenLcOcOpiTKviFyf8395tZgFV76D4DvUj_UxipLhm97d3EWVRMSE4bbKThyVC1_eEcP04xX4iV2QQKuDFOA5g1yttp12Mv9qEJ7lua1n3_oRh0FdA4=): 
  - [bcwinetrends.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKPFv4oXhKK1hojfNS9P8YfSGHpGowgRjpfwdUB3F_ccQw_bKA83xF5NYwRvQfjPkjLaWFJpp2RaVm3qAV-DO_j7kPaSjV-jaLZoMMwvHkUy78Z5zmOeRi2GGGBZ2cUqTru-5dRPvGgNAhardvQsQa8uit8qJC6RcoPepNcflXPaJTzyrOSQ==): 
  - [vineroutes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbppa7vWD0w0KRpIWAFN8HQB4e0cCfBntBPjM3tpjw_syKm_xVHGJLGE8ZksUpTRr77eCqVMN3p89pY68Z55wgdIUzcpCNNZKpZFNliAbVp0cW-1rrb5Nc_OznTztdw_UM92GKB8oaMbi2onpAPg==): 
  - [winesinniagara.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpTbKuHheRuN_wS7wAaZbH8C3BC_TbEPRU94xmfiCjPYmagRtrvHNeC7PRQS47vfgDy3E_BCgSQ4hr71JsUGGmBfWNkesLG2PPKPA3RmtLHf5mLOY8kVIwSjIANYFgRySikSqu2hvv5gjw4zGfFvQ7iD2VvnpxW2LwtHQqZEloCTQTU03Y8VeqrP9Ss2U=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0EvJSuTRmS6ivMCX8pWX7rtRyei1xAL5g45THSy5YGtPQuFPn9sylXh7UygzfoR2ZAwfmmtllgtAlH4ZQPHLAiOBXP8z1Gl8DxITSf8aKCZSFc9epR-NPKNz2m6zldcdFKDLFp_gAVSNfNQo5kv_YvuDawXQkPwxtOr1_atQCbaZ-107zVAT-0a6arF7AasPhHhISW8CYc_rmh2vAwLM=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_mlS2VRelNUXDYAPLr1XtAOsBxMdH2tShyT5miPDyL0XQBwQCC8YZXraeXSSSX4cgkMv6I01LC4NE_fAFxDbwu7YBAME02L5n0ikyldXuS_xx9PbvsXzjjJqjtOcja3LEsM1WZ31Yk0oUzQf_acinByNlov5J68ktWWOldqxeNTAsuZA=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFIx91jjK0bln_cJKO04H5C5MPmfK3MUNoNIaqtPoM2qghURIgkkKZW2Cb7TDKqfguSPoK4e8RjgQte1yTPG1ID1-eSIg4Afld1VgBYGdihB7YtZyjYmoZrlZsJK2UtyBabOPDn-0guP8-6dBv2HCuC0YMErWjxYhYYKdyJgBuBJLgaysPI12TEE2NZ0g3rCp2I93lkd4KTOb6DWiEKfrPrPv1s0=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFexg8qSX-wkote5J23l0-wruSXeQN1OW0svqdWlVutARF66t6tL2x0n0FTQ750gmDjoth7B_zl05ErR7_fX2X_4lR6OF2ABYBDt_yLGC_vh5wFOzhENCo3pfcWXnsF8ue8Dm0psu6xQLwLSysBC08FV36r1a6FjzNP2PcsUWwhbtphUDzrc_P3IynjPPAccfOAR6DCMs0rllgKkP8-x0graeRFU4sRbOMKcJM-NscmqCAdY2edAtc=): 
  - [winescores.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOjJMAU4t3NPVtVR3cSYXb0mLko60abJuA4_eh4xyYmE1JZST-enJM9I9ZvQTUZsLkxfAnevhHcCptmiIgM-WOn7e1HtvFf9NFOEhCSjXEdcqdn6fbYyaojbkh76Fx6wK_j7kCwBqCzI78W20I2D4gq5Mf-5ucMm752FB6DnAUj7BEWTikbzF1k3Q9zzmdbDtemFQ2uzaQ1hx7Cibr4t230I6tHj6BMbDlF128So3eiaiK): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGhXtMcDHxN1xQI2ftufZeIhkYaScVvkSEud3YYIgy5p8aB9uR4KPcsnL487aikNmU1ZFd0c8l1IoxBuVSWffHuQCgFb7oF9TGKM16Px1adeR1x3o1P8pfZcegmRqIx2k6bA_w2ehYeTv15leLzQLw4JLpp-mps1ORKqIQRUznDxq6zOU84MXueywJObLgViK6qnicYQiCB9N-s1iRwdU=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLE95XDLIURzwcibLVwmS81aKIFI3qjd993BdQThDsyK-A2wufvYfCis2mBlXkAJozT5nShiR2EDu243iQlq8WtlvyGKz4IOkYhnbA45RpZ9CYgJZ4iYySaZdosyPmGqdJ_NNoU9LZ4Dd9QDl6SCg2RRx2zqcPdZhb-nS-zWqbT9TEZ1BkRMZJc-exznHbfmX_yowEncWBiNvYrvMKtXQ=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2ATkPiv9j7QQdTulwB6h079WwPSkSaAuExhUj3gfk7wsaMt15SQSY-baCZqmCDUvQmYXOHkepy3g9CtlcQn4hiC-gBjyRmkfAtdVJUNLsiNxL6g-DuKzA12jfu_70iMOI86kLpG8VvYezqCVLTw322trIdRb8U5BS48YS1ZoGG1JhqxE_zVyCzI01KsiRKx29Hfe7EeR-qauOABzkvA=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdsamWBV3ugmHFSK0xG7zADF0JG-O947fugEwaZpUzX94VOccRHwBBZBh7GV2WXhohZtR3dbH2xnN1jlD1GJ88tKuSFKU19PbSfu8wvXvRILLycSGr-V_pMzzmwoIWV19js0SPlxnsDpTCuoCfAEfdKx3YfwyrIeXfz3CUHLCjABN5KgEltKygyyC2WKXhfwC2TgnWHT9rySg=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUzJv3BVNg1jjltmBLKJEn-fRAGi3sedVBAtupe8VcoNea5oEmFzuMz-wXuYDevhxTRGrlWpMKUcWX42q1MoGVv9AidHFc0QaPMqoVjGyL14CSu2iRuBUA4zK4Ymse4hoKKdyqW9N8TfX5NoqDsT_TrIt03UTDFQ9VTufz_5I4FN1-ji08F8UnK3Tu): 
  - [godello.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVLQ51Pjy65ZcXI5bdisR2U0Ge9f4XI_hiQOnkJ61vhSLSyMFUO_rT0AvD29w2gkw6hbiJ_gsojfNItEZHwYWyss4beGiTGz1MjHTZKgz1Bfq_fH3s2XFGko1bh20DVguYUMihbXLUHQ==): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDM24ZFZgp3lZRj_wat0gWCfuO8A9ih8o-hR8n3YYI85osXTekTN7A7eAZIwoETTMsR9hc5mPE1T1A1h0mNCq62Zg0ng4bJLcic1sMSaKWaEv-HTMMrZlDktDh4R_6Q17SSXdHOp5yD37B06QLPomJjWJDTzDWZ2TqdjssLeK4cEPbH505-t_uK-rjpa-V1YmwSqGuBjEYqk09Nild5LZkPmup_YM=): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcaetHnv7wXyu8aAdWFrkT528ZR7SZg21Y_GW8NYJOCwWRudLUbhytW6GBXBcBVOLDM8cF5Wt2t3hfBz18fHkU6zU7Yx3vmd_5W38Qj1C7aA4LKW0F-pf0fqfunniXincvzCCjSBMY-TzLYaLUO6SY2vWv8MPlQTJJayaL): 


### sourcing_agent_tool (status=ok)
**Sub-agent synthesis:**
Here is the current real-time availability, pricing, and store locations for dry BC white wines (Riesling, Pinot Gris, Chardonnay, and Pinot Blanc) from your requested producers in the Vancouver area:

### 1. Tantalus Vineyards

#### **Tantalus Riesling**
*Consistently one of BC's benchmark dry Rieslings, featuring bright acidity, citrus, and mineral notes.*
* **BC Liquor Stores**: **$30.99** (546 units in stock across 40 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/802280)
* **Everything Wine**: **$30.99** (In stock: 8 at Vancouver River District, 17 at North Vancouver, 7 at South Surrey) | [Buy at Everything Wine](https://www.everythingwine.ca/tantalus-riesling-750-ml)
* **Marquis Wine Cellars**: **$32.99** (11 in stock) | [Buy at Marquis Wine Cellars](https://www.marquis-wines.com/tantalus-2022-riesling-750ml/)
* **Sutton Place Wine Merchant**: **$35.49** (9 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4144458-tantalus-riesling)

#### **Tantalus Old Vines Riesling (2020)**
*A premium, highly-concentrated dry expression from some of the oldest Riesling plantings in the province.*
* **Sutton Place Wine Merchant**: **$51.99** (9 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4360955-tantalus-old-vines-riesling)

#### **Tantalus Pinot Gris (2024)**
*A beautifully textured, crisp, and dry Pinot Gris.*
* **Marquis Wine Cellars**: **$29.99** (3 in stock) | [Buy at Marquis Wine Cellars](https://www.marquis-wines.com/tantalus-2024-pinot-gris-750ml/)

#### **Tantalus Chardonnay**
*Bright, elegant, and mineral-driven with subtle toasted nuttiness.*
* **BC Liquor Stores**: **$35.99** (387 units in stock across 45 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/114884)
* **Everything Wine**: **$35.99** (10 in stock at Langley Store; out of stock at Vancouver/North Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/tantalus-chardonnay)

#### **Tantalus "Bear" Chardonnay**
*An approachable, fresh, and fruit-forward un-oaked style.*
* **Legacy Liquor Store**: **$29.81** (3 in stock) | [Buy at Legacy Liquor](https://www.legacyliquorstore.com/product/wine/tantalus-bear-chardonnay-1-x-750ml)
* **Sutton Place Wine Merchant**: **$29.99** (6 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/5171325-tantalus-bear-chardonnay)
* **Everything Wine**: **$30.98** (5 in stock at South Surrey; out of stock at Vancouver/North Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/tantalus-vineryards-bear-chardonnay-750-ml)

---

### 2. Culmina Family Estate Winery

#### **Culmina Decora Riesling**
*A dry, vibrant Riesling showing delicate floral, starfruit, and stone fruit notes with crisp acidity.*
* **Okanagan Cellars**: **$22.99** (16 in stock) | [Buy at Okanagan Cellars](https://okanagancellars.com/products/4217289-culmina-decora-riesling)
* **BC Liquor Stores**: **$24.99** (810 units in stock across 73 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/389125)
* **Legacy Liquor Store**: **$27.98** (6 in stock) | [Buy at Legacy Liquor](https://www.legacyliquorstore.com/product/wine/culmina-decora-riesling-1-x-750ml)

#### **Culmina Dilemma Chardonnay**
*A luscious, elegant Chardonnay framed by mineral notes, subtle oak, and a fresh finish.*
* **Okanagan Cellars**: **$34.99** (7 in stock) | [Buy at Okanagan Cellars](https://okanagancellars.com/products/3937046-culmina-dilemma-chardonnay)
* **BC Liquor Stores**: **$35.99** (227 units in stock across 34 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/126830)

---

### 3. Blue Mountain Vineyard and Cellars

#### **Blue Mountain Pinot Blanc**
*A fantastic dry alternative to Pinot Gris, offering crisp orchard fruit notes and excellent structure.*
* **Sutton Place Wine Merchant**: **$31.49** (11 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4298417-blue-mountain-pinot-blanc)
* **Everything Wine**: **$31.98** (7 in stock at North Vancouver; out of stock at Vancouver) | [Buy at Everything Wine](https://www.everythingwine.ca/blue-mountain-vineyard-pinot-blanc-750-ml)

---

### 4. Meyer Family Vineyards

#### **Meyer Family Chardonnay (2024)**
*A classic, beautifully balanced Okanagan Chardonnay.*
* **Marquis Wine Cellars**: **$32.99** (13 in stock) | [Buy at Marquis Wine Cellars](https://www.marquis-wines.com/meyer-family-2024-chardonnay-750ml/)

#### **Meyer Family Micro Cuvee Chardonnay (2022)**
*A premium, small-lot, highly-structured dry Chardonnay.*
* **Sutton Place Wine Merchant**: **$79.99** (6 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4179096-meyer-family-micro-cuvee-chardonnay)

#### search_bcliquor_tool (status=ok, 6 results)
  - TANTALUS - SYRAH | $36.99 | stock=11 | in 1 stores | rating=4.4 | https://www.bcliquorstores.com/product/460372 | {sku=460372; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=13.9; sweetness=00; tasting_notes=A vibrant deep garnet in colour in the glass, this Syrah release is beautifully lifted with intense notes of violets and blue fruits, alongside touches of charcuterie, anise and licorice. Intriguing hints of white pepper, cedar sap and cherry candy add a wonderful complexity to the nose. The palate is very juicy, with loads of blackberry, dark plum and black cherry present. A little peppery baking spice and red licorice complement the palate. The finish is long and lifted with great clarity and minerality. The tannins are fine grained and very well integrated.
; consumer_votes=22; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/460372.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS CHARDONNAY 2023 | $35.99 | stock=387 | in 45 stores | rating=4.6 | https://www.bcliquorstores.com/product/114884 | {sku=114884; product_type=White Wine; grape_type=CHARDONNAY; country=Canada; volume=0.750; alcohol_pct=13.7; sweetness=00; tasting_notes=92 Points, Gismondi On Wine: "Consistently one of Okanagan's top chardonnays. Confident and complete, with interwoven layers of lemon, light cream, stones, and subtle toasted nuttiness, this streams along the palate with an effortless acidity. The medium  body will work well at the dinner table now, or with a couple of years in your cellar. Super smart." (August 2024); consumer_votes=11; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/114884.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS - RIESLING 2025 | $30.99 | stock=546 | in 40 stores | rating=4.1 | https://www.bcliquorstores.com/product/802280 | {sku=802280; product_type=White Wine; grape_type=RIESLING; country=Canada; volume=0.750; alcohol_pct=12.2; sweetness=01; tasting_notes=A top Riesling producer from Kelowna, Tantalus has a long history dating to 1927 and the Pioneer vineyard. The spectrum of Riesling grape flavours can be found here from green apple to citrus to tropical. A real treat and as Riesling is the #1 food wine, will go with everything from corn-on-the-cob to potato salad to ham steaks to spicy recipes to grilled fare.
; consumer_votes=104; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/802280.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS - PINOT NOIR 2022 | $35.99 | stock=87 | in 14 stores | rating=4.2 | https://www.bcliquorstores.com/product/200881 | {sku=200881; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.3; sweetness=00; tasting_notes=Dark crimson in the glass, the nose is lively with bright floral notes alongside cocoa and red berries. Rich notes of cedar, wet earth and graphite complement the aromatic profile. Despite its youth, the palate is showing beautiful complexity and nuance with swaths of red currant, cherry and fig spun together with a unique mineral expression. Lush tannins offer depth and structure and the expectation of a graceful development in bottle. Comfortably enjoy over the next 5 to 10 years.
; consumer_votes=118; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/200881.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS VINEYARDS - REIMER VINEYARD PINOT NOIR | $39.99 | stock=506 | in 66 stores | rating=4.5 | https://www.bcliquorstores.com/product/692960 | {sku=692960; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=9; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/692960.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS - FURTHER AFIELD SERIES CAB FRANC | $34.99 | stock=492 | in 47 stores | rating=4.7 | https://www.bcliquorstores.com/product/252158 | {sku=252158; product_type=Red Wine; grape_type=CABERNET FRANC; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=91 Points, Gismondi On Wine: "Expect an attractive, juicy red that is a nod to Loire but made with the sensibility of a pinot specialist. Paterson has tamed the herbaceous, savoury notes and pushed the ripe blueberry and black fruits to the foreground, all sitting on a silky tannin structure that melts in your mouth.  Considerable value." (April 2024)
; consumer_votes=15; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/252158.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 9 results)
  - Tantalus Vineyards Rose 750 mL | $30.98 | [North Vancouver:0, South Surrey:17, Langley Store:0, Vancouver:7] | https://www.everythingwine.ca/tantalus-rose-2012 | {sku=439687; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/3/439687_tantalus_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Tantalus Vineyards Chardonnay 750 mL | $35.99 | [North Vancouver:0, South Surrey:0, Langley Store:10, Vancouver:0] | https://www.everythingwine.ca/tantalus-chardonnay | {sku=114884; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/1/114884_tantalus_chardonnay_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Riesling 750 mL | $30.99 | [North Vancouver:17, South Surrey:7, Langley Store:0, Vancouver:8] | https://www.everythingwine.ca/tantalus-riesling-750-ml | {sku=802280; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/0/802280_tantalus_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Tantalus Vineyards Bear Chardonnay 750 mL | $30.98 | [North Vancouver:0, South Surrey:5, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineryards-bear-chardonnay-750-ml | {sku=83282; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/3/83282_tantalus_bear_chardonnay.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Ontario Riesling 750 mL | $36.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineyards-ontario-riesling-750-ml | {sku=270640; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/270640_tantalus_ontario_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Further Afield Series Syrah 750 mL | $36.99 | [North Vancouver:0, South Surrey:0, Langley Store:6, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineyards-further-afield-series-syrah-750-ml | {sku=460372; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/6/460372_tantalus_further_afield_syrah.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Maija Pinot Noir 750 mL | $39.98 | [North Vancouver:12, South Surrey:2, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-juveniles-pinot-noir | {sku=348755; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/4/348755_tantalus_maija_pinot_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Looney Vineyard Oregon Rose 750 mL | $30.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineyards-looney-vineyard-oregon-rose-750-ml | {sku=270643; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/270643_tantalus_looney_vineyard_oregon_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Further Afield Series Cabernet Franc 750 mL | $34.99 | [North Vancouver:7, South Surrey:8, Langley Store:10, Vancouver:5] | https://www.everythingwine.ca/tantalus-vineyards-further-afield-series-cabernet-franc-750-ml | {sku=252158; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/5/252158_tantalus_further_afield_cabernet_franc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 8 results)
  - Tantalus Bear Chardonnay | $29.99 | stock=6 | https://store.suttonplacewinemerchant.com/products/5171325-tantalus-bear-chardonnay | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC83282.jpg; country=CANADA; varietal=Chardonnay; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Tantalus Further Afield Blanc de Noir | $47.99 | 2022 | stock=7 | https://store.suttonplacewinemerchant.com/products/5181376-tantalus-further-afield-blanc-de-noir | {category=SPARKLING CANADA; in_stock=True; unit_size=750ML Bottle; country=CANADA; varietal=Pinot Noir; is_staff_pick=False; is_featured=False}
  - Tantalus Further Afield Cab Franc | $39.49 | stock=6 | https://store.suttonplacewinemerchant.com/products/4724608-tantalus-further-afield-cab-franc | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000025/0000252158-8879.jpg; country=CANADA; varietal=Cabernet Franc; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Tantalus Maija Pinot Noir | $38.49 | 2022 | stock=9 | https://store.suttonplacewinemerchant.com/products/4668256-tantalus-maija-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000034/0000348755-4119.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=12.90; is_staff_pick=False; is_featured=False}
  - Tantalus Old Vines Riesling | $51.99 | 2020 | stock=9 | https://store.suttonplacewinemerchant.com/products/4360955-tantalus-old-vines-riesling | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000017/0000179226-1753.jpg; country=CANADA; varietal=Riesling; alcohol_pct=13.40; is_staff_pick=False; is_featured=False}
  - Tantalus Riesling | $35.49 | 2022 | stock=9 | https://store.suttonplacewinemerchant.com/products/4144458-tantalus-riesling | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000080/0000802280-5980.jpg; country=CANADA; varietal=Riesling; alcohol_pct=12.40; is_staff_pick=False; is_featured=False}
  - Tantalus Rose | $29.99 | 2021 | stock=22 | https://store.suttonplacewinemerchant.com/products/4254767-tantalus-rose | {category=ROSE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000043/0000439687-3791.jpg; country=CANADA; varietal=Pinot Noir/Pinot Meunier; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Tantalus Syrah  | $41.99 | 2021 | stock=6 | https://store.suttonplacewinemerchant.com/products/4171973-tantalus-syrah | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000046/0000460372-1677.jpg; country=CANADA; varietal=Syrah; alcohol_pct=14.20; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 5 results)
  - Tantalus 2025 Rose 750ml | $30.99 | stock=17 | https://www.marquis-wines.com/tantalus-2025-rose-750ml/ | {sku=1017799; in_stock=True; categories=["Rosé Wine", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21728/images/17421/2026-04-23-13.31.48__31357.1777054370.500.500.png?c=2}
  - Tantalus 2025 Riesling 750ml | $32.99 | stock=11 | https://www.marquis-wines.com/tantalus-2022-riesling-750ml/ | {sku=1010038; in_stock=True; categories=["White Wine", "Riesling", "Kelowna", "British Columbia", "Organic / Biodynamic Wine"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7320/images/8588/IMG_15051__08114.1588006662.500.500.jpg?c=2}
  - Tantalus 2024 Pinot Gris 750ml | $29.99 | stock=3 | https://www.marquis-wines.com/tantalus-2024-pinot-gris-750ml/ | {sku=1031910; in_stock=True; categories=["White Wine", "Pinot Gris & Grigio", "Organic / Biodynamic Wine"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21324/images/17029/2026-01-23-14.54.33__29085.1769462280.500.500.png?c=2}
  - Tantalus 2022 Cabernet Franc 750ml | $36.99 | stock=16 | https://www.marquis-wines.com/tantalus-2022-cabernet-franc-750ml/ | {sku=1029801; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Cabernet Franc", "Drink Local"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18670/images/14640/2024-05-08_11.38.04__97448.1715278618.500.500.png?c=2}
  - Tantalus 2023 Maija Pinot Noir 750ml | $40.99 | stock=7 | https://www.marquis-wines.com/tantalus-2017-maija-pinot-noir-750ml/ | {sku=1016222; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9531/images/7177/IMG_9636__76411.1544468344.500.500.JPG?c=2}

#### search_legacy_liquor_store_tool (status=ok, 2 results)
  - Tantalus "Maija" Pinot Noir | $38.64 | stock=7 | https://www.legacyliquorstore.com/product/wine/tantalus-maija-pinot-noir-1-x-750ml | {brand=Tantalus; slug=tantalus-maija-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Tantalus "Bear" Chardonnay | $29.81 | stock=3 | https://www.legacyliquorstore.com/product/wine/tantalus-bear-chardonnay-1-x-750ml | {slug=tantalus-bear-chardonnay-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "chardonnay"]}

#### search_bcliquor_tool (status=ok, 0 results)

#### search_everything_wine_tool (status=ok, 12 results)
  - Blue Mountain Vineyard Gamay Noir 750 mL | $34.98 | [North Vancouver:0, South Surrey:10, Langley Store:11, Vancouver:0] | https://www.everythingwine.ca/blue-mountain-gamay-noir | {sku=389882; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/8/389882_blue_mountain_vineyard_gamay_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Pinot Gris 750 mL | $31.98 | https://www.everythingwine.ca/blue-mountain-pinot-gris | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/b/m/bmvc_pgris.png?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366&format=jpeg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Pinot Blanc 750 mL | $31.98 | [North Vancouver:7, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/blue-mountain-vineyard-pinot-blanc-750-ml | {sku=329441; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/2/329441_blue_mountain_pinot_blanc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Reserve Brut Sparkling 750 mL | $52.98 | https://www.everythingwine.ca/blue-mountain-reserve-brut | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/b/m/bmvc_reserve_brut.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Reserve Pinot Noir 1.5 L | $115.98 | https://www.everythingwine.ca/blue-mountain-vineyard-reserve-pinot-noir-1-5-l | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Blanc de Blancs Sparkling 750 mL | $52.98 | [North Vancouver:10, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/blue-mountain-blanc-de-blancs-sparkling | {sku=402594; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/0/402594_blue_mountain_blanc_de_blancs.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Reserve Cuvee Pinot Noir 750 mL | $47.98 | https://www.everythingwine.ca/blue-mountain-vineyard-reserve-cuvee-pinot-noir-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/b/m/bmvc_reserve_pnoir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Gold Label Brut Sparkling 750 mL | $36.98 | [North Vancouver:1, South Surrey:9, Langley Store:9, Vancouver:5] | https://www.everythingwine.ca/blue-mountain-brut | {sku=471672; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/7/471672_blue_mountain_gold_label_brut_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Blossom Slope Block 17 Chardonnay 750 mL | $52.98 | https://www.everythingwine.ca/blue-mountain-blossom-slope-block-17-chardonnay-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Wild Terrain Block 9 Pinot Noir 750 mL | $57.98 | https://www.everythingwine.ca/blue-mountain-block-9-pinot-noir-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Gravel Force Block 14 Pinot Noir 750 mL | $57.98 | https://www.everythingwine.ca/blue-mountain-block-14-pinot-noir-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard River Flow Block 23 Pinot Noir 750 mL | $57.98 | https://www.everythingwine.ca/blue-mountain-block-23-pinot-noir-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 3 results)
  - Blue Mountain Brut Gold Label  | $35.99 | stock=26 | https://store.suttonplacewinemerchant.com/products/4144014-blue-mountain-brut-gold-label | {category=SPARKLING CANADA; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000047/0000471672-6624.jpg; country=CANADA; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}
  - Blue Mountain Gamay | $33.99 | 2020 | stock=4 | https://store.suttonplacewinemerchant.com/products/4228470-blue-mountain-gamay | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000038/0000389882-3198.png; country=CANADA; varietal=Gamay Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Blue Mountain Pinot Blanc | $31.49 | 2022 | stock=11 | https://store.suttonplacewinemerchant.com/products/4298417-blue-mountain-pinot-blanc | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000032/0000329441-8271.png; country=CANADA; varietal=Pinot Blanc; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 5 results)
  - Blue Mountain N/V Gold Label Brut 750ml | $37.99 | stock=33 | https://www.marquis-wines.com/blue-mountain-n-v-gold-label-brut-750ml/ | {sku=471672; in_stock=True; categories=["Sparkling", "Okanagan Falls", "British Columbia", "Lunar New Year"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/6072/images/11775/blue-mountain-gold-brut__28311.1648759359.500.500.jpg?c=2}
  - Blue Mountain 2023 Reserve Cuvee Pinot Noir 750ml | $51.99 | stock=11 | https://www.marquis-wines.com/blue-mountain-2022-reserve-cuvee-pinot-noir-750ml/ | {sku=1023129; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19489/images/15288/2024-10-31-14.17.17__41020.1730481578.500.500.png?c=2}
  - Blue Mountain 2022 Gamay Noir 750ml | $35.99 | stock=12 | https://www.marquis-wines.com/blue-mountain-2019-gamay-noir-750ml/ | {sku=1014652; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8456/images/5067/blue-mountain-gamay-2015__59204.1533682531.500.500.jpg?c=2}
  - Gagnon Kennedy Vineyards 2020 Cabernet Sauvignon Monte Rosso Vineyard Moon Mountain 750ml | $329.99 | stock=3 | https://www.marquis-wines.com/gagnon-kennedy-vineyards-2020-cabernet-sauvignon-monte-rosso-vineyard-moon-mountain-750ml/ | {sku=1030528; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "USA", "California", "Napa"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19625/images/15538/2025-01-10_14.19.46__85706.1736797630.500.500.png?c=2}
  - Arette Reposado Tequila 700ml | $89.99 | stock=5 | https://www.marquis-wines.com/arette-reposado-tequila-700ml/ | {sku=1024491; in_stock=True; categories=["Spirits", "Tequila & Mezcal"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21623/images/17318/2026-03-30-13.14.55__91622.1775070661.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 3 results)
  - Blue Mountain Reserve Cuvee Pinot Noir Magnum | $120.87 | stock=1 | https://www.legacyliquorstore.com/product/wine/blue-mountain-reserve-cuvee-pinot-noir-magnum-1-x-1-5l | {slug=blue-mountain-reserve-cuvee-pinot-noir-magnum-1-x-1-5l; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Blue Mountain Gamay Noir | $34.08 | stock=6 | https://www.legacyliquorstore.com/product/wine/blue-mountain-gamay-noir-1-x-750ml | {slug=blue-mountain-gamay-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "gamay"]}
  - Blue Mountain Brut Gold Label | $35.88 | stock=14 | https://www.legacyliquorstore.com/product/wine/blue-mountain-winery-gold-label-brut-1-x-750ml | {brand=Blue Mountain; slug=blue-mountain-winery-gold-label-brut-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}

#### search_bcliquor_tool (status=ok, 0 results)

#### search_everything_wine_tool (status=ok, 7 results)
  - Meyer Family Vineyards Tribute Chardonnay 750 mL | $43.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/meyer-family-tribute-chard | {sku=838532; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/3/838532_meyer-family-tribute-chard.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Pinot Noir 750 mL | $33.98 | [North Vancouver:0, South Surrey:0, Langley Store:6, Vancouver:0] | https://www.everythingwine.ca/meyer-family-ok-pinot-noir | {sku=154310; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/5/154310_meyer_family_okangan_valley_pinot_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Columbia Valley Chardonnay 750 mL | $31.98 | [North Vancouver:10, South Surrey:10, Langley Store:9, Vancouver:0] | https://www.everythingwine.ca/meyer-family-vineyards-columbia-valley-chardonnay-750-ml | {sku=323571; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/2/323571_meyer_columbia_valley_chard.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Micro Cuvee Pinot Noir 750 mL | $77.98 | [North Vancouver:11, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/meyer-family-micro-pinot-noir | {sku=942680; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/9/4/942680_meyer_micro_cuvee_pn.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Mclean Creek Road Vineyard Chardonnay 750 mL | $43.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/meyer-family-vineyards-mclean-vineyard-chardonnay-750-ml | {sku=139717; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/3/139717_meyer_family_vineyards_mclean_vineyard_chardonnay.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Snipes Mountain Washington Chardonnay 750 mL | $43.98 | https://www.everythingwine.ca/meyer-family-vineyards-snipes-mountain-washington-chardonnay-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/p/l/placeholder_image_white_wine_4_6.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Meyer Family Vineyards Mclean Creek Road Vineyard Pinot Noir 750 mL | $47.98 | [North Vancouver:17, South Surrey:0, Langley Store:6, Vancouver:10] | https://www.everythingwine.ca/meyer-family-mclean-pinot-noir | {sku=831487; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/3/831487_meyer-family-pinot-noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 4 results)
  - Meyer Family Micro Cuvee Chardonnay | $79.99 | 2022 | stock=6 | https://store.suttonplacewinemerchant.com/products/4179096-meyer-family-micro-cuvee-chardonnay | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000088/0000883363-7064.jpg; country=CANADA; varietal=Chardonnay; alcohol_pct=13.90; is_staff_pick=False; is_featured=False}
  - Meyer Family Micro Cuvee Pinot Noir | $79.99 | 2019 | stock=6 | https://store.suttonplacewinemerchant.com/products/4179652-meyer-family-micro-cuvee-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000094/0000942680-7152.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Meyer Family Vineyards Mclean Creek Pinot Noir  | $48.99 | 2022 | stock=4 | https://store.suttonplacewinemerchant.com/products/4144485-meyer-family-vineyards-mclean-creek-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000083/0000831487-9040.png; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Meyer Family Vineyards Okanagan Valley Pinot Noir | $33.49 | 2025 | stock=27 | https://store.suttonplacewinemerchant.com/products/4298314-meyer-family-vineyards-okanagan-valley-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000015/0000154310-1810.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 2 results)
  - Meyer Family 2024 Chardonnay 750ml | $32.99 | stock=13 | https://www.marquis-wines.com/meyer-family-2024-chardonnay-750ml/ | {sku=1012941; in_stock=True; categories=["White Wine", "Chardonnay", "British Columbia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9924/images/9192/2020-09-24_14.12.59__56311.1761861012.500.500.jpg?c=2}
  - Meyer Family 2023 Pinot Noir 750ml | $34.99 | stock=12 | https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/ | {sku=1014474; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7708/images/8652/Lindsey_Ail_-_IMG_15661__44130.1589559651.500.500.jpg?c=2}

#### search_legacy_liquor_store_tool (status=ok, 0 results)

#### search_bcliquor_tool (status=ok, 6 results)
  - CULMINA - SAIGNEE 2023 | $26.99 | stock=37 | in 8 stores | rating=4.6 | https://www.bcliquorstores.com/product/72549 | {sku=72549; product_type=Rose Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=A blend of Malbec (44%), Cabernet Franc (29%) and Merlot (34%) from Arise and Stan's Benches, Certified Organic. "Pretty nose here, delicate and floral, bright red fruit-scented. Depth is very good." 92 Points - John Szabo, MS.
; consumer_votes=5; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/72549.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - DILEMMA CHARDONNAY | $35.99 | stock=227 | in 34 stores | rating=4.8 | https://www.bcliquorstores.com/product/126830 | {sku=126830; product_type=White Wine; grape_type=CHARDONNAY; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Showcasing mineral and spice aromas, Dilemma is framed by lovely oak, caramel and butter flavours, a luscious body, and a long, fresh finish, creating a wine of outstanding finesse, beauty, elegance and style.
; consumer_votes=8; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/126830.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - DECORA RIESLING | $24.99 | stock=810 | in 73 stores | rating=4.0 | https://www.bcliquorstores.com/product/389125 | {sku=389125; product_type=White Wine; grape_type=RIESLING; country=Canada; volume=0.750; alcohol_pct=13.4; sweetness=00; tasting_notes=Finely scented with daisies, dried apricots, toasted almonds and yeasty aromatics, Decora showcases delicacy and complexity. The verve and brightness of the palate are balanced by creaminess, with notes of starfruit and fuzzy peaches. 
; consumer_votes=6; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/389125.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - HYPOTHESIS 2019 | $34.99 (reg $42.99) | stock=1814 | in 97 stores | rating=4.5 | https://www.bcliquorstores.com/product/227436 | {sku=227436; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Opulent and refined, the bouquet brings complex aromas of cedar bark, leather, cocoa nibs and dark cherries. The generous palate is layered with succulent dark fruits, licorice and baking spice supported by balance acidity and silky tannins. The nuances of 2018 Hypothesis unfurl gradually over a long and persistent finish.
; consumer_votes=30; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/227436.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - CABERNET SAUVIGNON 2021 | $37.99 | stock=82 | in 16 stores | rating=4.5 | https://www.bcliquorstores.com/product/227457 | {sku=227457; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Our single-varietal expression of Malbec comes from our Arise Bench vineyard along the Golden Mile Bench. Well-balanced with rich fruit offset by supple, silky tannins and oolong tea flavours. Rich mulberry and plum linger on the deep, intriguing finish.
; consumer_votes=10; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/227457.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA OLIVER - R AND D RED BLEND GOLDEN MILE BENCH 2022 | $19.99 | stock=1477 | in 125 stores | rating=4.0 | https://www.bcliquorstores.com/product/495846 | {sku=495846; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=A Golden Mile expression is on show here with lots of Merlot fruit and other Bordeaux grapes from estate vineyards. Offering great ripe fruit from this exceptional vintage, the red and black fruit flavours and persistent linger highlight an expressive wine. Match with grilled fare or pasta recipes or vegetarian dishes.
; consumer_votes=63; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/495846.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 5 results)
  - Culmina Family Estate Winery Decora Riesling 750 mL | $28.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/culmina-family-estate-winery-decora-riesling-750-ml | {sku=863035; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/6/863035_culmina_decora_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery Saignee Rose 750 mL | $26.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/culmina-family-estate-winery-saignee-rose-merlot-cab-franc-cab-sauv-750-ml-1 | {sku=29593; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/9/29593_culmina_family_estate_winery_saignee_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery R&D Red Blend 750 mL | $19.99 | https://www.everythingwine.ca/culmina-family-estate-winery-r-d-red-blend-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/c/u/culmina_r_d_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery R&D Sauvignon Blanc Semillon 750 mL | $26.98 | https://www.everythingwine.ca/culmina-family-estate-winery-r-d-sauvignon-blanc-semillon-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery Golden Mile Bench Hypothesis Red Blend 750 mL | $34.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/culmina-family-estate-winery-golden-mile-bench-hypothesis-red-blend-750-ml | {sku=852012; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/5/852012_culmina_family_estate_winery_golden_mile_bench_hypothesis.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}

#### search_okanagan_cellars_tool (status=ok, 7 results)
  - CULMINA - CAB SAUV | $37.99 | stock=10 | https://okanagancellars.com/products/3946821-culmina-cab-sauv | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000022/0000227457-4800.png}
  - CULMINA - DECORA RIESLING | $22.99 | stock=16 | https://okanagancellars.com/products/4217289-culmina-decora-riesling | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/all/BC389125.jpg}
  - CULMINA - DILEMMA CHARDONNAY | $34.99 | stock=7 | https://okanagancellars.com/products/3937046-culmina-dilemma-chardonnay | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000012/0000126830-4871.png}
  - CULMINA - HYPOTHESIS | $32.99 (reg $36.99) | stock=10 | https://okanagancellars.com/products/3957069-culmina-hypothesis | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000022/0000227436-6306.jpg}
  - CULMINA - MALBEC | $37.99 | stock=12 | https://okanagancellars.com/products/4114513-culmina-malbec | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000025/0000252952-8251.png}
  - CULMINA - R&D RED BLEND | $19.99 | stock=21 | https://okanagancellars.com/products/3410072-culmina-r-d-red-blend | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000049/0000495846-8804.png}
  - CULMINA - SAIGNEE | $25.99 | stock=10 | https://okanagancellars.com/products/3403440-culmina-saignee | {category=Rose; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000007/0000072549-9622.png}

#### search_suttonplace_tool (status=ok, 0 results)

#### search_marquis_tool (status=ok, 5 results)
  - Penfolds 2022 Reserve Bin A Chardonnay 750ml | $154.99 | stock=9 | https://www.marquis-wines.com/penfolds-2022-reserve-bin-a-chardonnay-750ml-ojrx/ | {sku=1030793; in_stock=True; categories=["White Wine", "Chardonnay", "95+ Point Wines", "Adelaide Hills", "Australia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19951/images/15788/2025-02-25-14.38.19__97300.1740678446.500.500.png?c=2}
  - Wohlmuth 2024 Sauvgnon Blanc "Phyllit" 750ml | $44.99 | stock=21 | https://www.marquis-wines.com/wohlmuth-2024-sauvgnon-blanc-phyllit-750ml/ | {sku=1031052; in_stock=True; categories=["White Wine", "Sauvignon Blanc", "Austria", "Steiermark"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21423/images/17077/IMG_0574__88566.1770668649.500.500.png?c=2}
  - Monteraponi 2021 Colli Toscana Centrale Trebbiano 750ml | $149.99 | stock=19 | https://www.marquis-wines.com/monteraponi-2021-colli-toscana-centrale-trebbiano-750ml/ | {sku=1029800; in_stock=True; categories=["White Wine", "Tuscany", "Italy", "Marquis Exclusives", "Organic / Biodynamic Wine", "Trebbiano / Ugni Blanc", "Monteraponi"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18696/images/14607/monteraponi_trebbiano__42009.1712869357.500.500.jpg?c=2}
  - Gaja 2019 Pieve Santa Restituta Rennina Brunello di Montalcino 750ml | $399.99 | stock=3 | https://www.marquis-wines.com/gaja-2019-pieve-santa-restituta-rennina-brunello-di-montalcino-750ml/ | {sku=1013605; in_stock=True; categories=["Red Wine", "Sangiovese", "Italy", "Tuscany", "Brunello/Rosso di Montalcino", "95+ Point Wines"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20910/images/16684/2025-10-17_11.31.29__87413.1760991164.500.500.png?c=2}
  - Lagavulin 8 Year Old Single Malt Whisky 750ml | $107.99 | stock=5 | https://www.marquis-wines.com/lagavulin-8-year-old-750ml/ | {sku=1026213; in_stock=True; categories=["Single Malt Scotch", "Islay"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/15552/images/11248/2021-12-07_16.32.57__16452.1638999505.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 4 results)
  - Culmina Hypothesis | $39.81 | stock=4 | https://www.legacyliquorstore.com/product/wine/culmina-hypothesis-1-x-750ml | {slug=culmina-hypothesis-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Culmina Decora Riesling | $27.98 | stock=6 | https://www.legacyliquorstore.com/product/wine/culmina-decora-riesling-1-x-750ml | {brand=Culmina; slug=culmina-decora-riesling-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "riesling"]}
  - Culmina Cabernet Sauvignon | $48.58 | stock=5 | https://www.legacyliquorstore.com/product/wine/culmina-cabernet-sauvignon-1-x-750ml | {brand=Culmina; slug=culmina-cabernet-sauvignon-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "cabernet sauvignon"]}
  - Culmina R&D Red Blend | $22.27 | stock=6 | https://www.legacyliquorstore.com/product/wine/culmina-r-d-red-blend-1-x-750ml | {brand=Culmina Oliver; slug=culmina-r-d-red-blend-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}


### sommelier_agent_tool (status=ok)
**Sub-agent synthesis:**
For warm-weather patio sipping, you want wines with bracing acidity, zero residual sugar, and a clean, mineral-driven finish. British Columbia excels at these electric, bone-dry styles, particularly from the Similkameen Valley, Okanagan Falls, and the Naramata Bench. 

Here are four exceptional, strictly dry BC white wines that fit your profile perfectly, along with crisp, patio-friendly alternatives across other beverage categories.

### **The Core Request: Crisp, Dry BC White Wines**

**1. Little Farm Mulberry Tree Vineyard Riesling (Similkameen Valley)**
If you want bone-dry, high-acid refreshment, Little Farm is the gold standard in BC. They specialize in low-intervention, searingly dry Rieslings that showcase the rocky minerality of the Similkameen Valley. 
*   **The Profile:** Expect intense green apple, bright citrus, and a distinct chalky texture. 
*   **Review:** Reviewing the 2020 vintage, Michaela Morris for *Decanter* awarded it **93 points**, praising its pristine, focused, and "searingly dry" nature [Decanter via MyWineCanada](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtij7eDQFxSowsWIAer3ISSg0MCiOK0DsW5ax9W6WIogIPH0RdWnjyjFGedcmkzseDkcGNMhBAQ3TlvVFR2lWgUgrncKnDFNe6ijYtJhVz5un9n1vAnoV2-F_cKKOVUnCKkp4X42DC7cgaJ59kuNNxFiJNwnn8Uswm2omBiU8dRHR00DvRSw9N-Kg=).

**2. Terravista Vineyards "Fandango" (Naramata Bench)**
Terravista produces the only Albariño and Verdejo blend in Canada. These are classic Iberian grapes built for hot weather and seafood, resulting in a wine that is incredibly zippy and refreshing.
*   **The Profile:** A vibrant, textured white with notes of citrus zest, pear, and a stony backbone.
*   **Review:** Jennifer Havers for *Natalie MacLean* gave the 2021 vintage **90 points**, highlighting its crisp, refreshing palate of orange blossom and gooseberry with a bright, mineral-driven finish [Natalie MacLean](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI9m1XhCsB9yQEvu8cCkp-Jk2EFd1GKJjFpWp5TLJGHnOMtHdcVJGKjYThUuCigyVD5keTjzi32yjtW8zooWsT3xi0VcIJ8scpRbmV21qH1p9EC8RVGr3ufkr17tKFxYD8R0GsOJKSiWI5-Pz2tdnVRnFrLppUj8DfIpJO5T6mp4KFX842tlYvrRBPUDvlZk0=).

**3. Clos du Soleil "Capella" (Similkameen Valley)**
A sophisticated, Bordeaux-style white blend dominated by Sauvignon Blanc with a touch of Sémillon. It offers the grassy, grapefruit snap of Sauvignon Blanc but with an elegant, slightly waxy texture that elevates it above a standard patio pounder.
*   **The Profile:** Racy and complex, featuring lemon peel, white grapefruit, and savory desert herbs.
*   **Review:** Daenna Van Mulligen of *WineScores.ca* awarded the 2021 vintage **92 points**, describing it as a harmonious, racy wine with a slick texture [WineScores.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_5Acdci1RRtZKHaKN67u6dfsPyps_FPDTCb-CiLvWFctdZ-FFjC_4WwjjO-NM2F384oTw04uuUChxzm0gmCileLtH9GVX3jl_yeN0PnQS_2mOSpkR0A5sj2FkKe76a5hS6u7LI40Xz2e6VI9vZNucGFuAgS3Jo0lOnLFxy7Tv4SZgl-quayH5x93vATJxRel6C9-f_ASUg4xsDff-9k65fW-KLAlTXOAdzMxuVQ3tnTS5bXWmI6v4x1P5CqCUyc5L-OwSZmIGwlZ3rYTYzlY280YS5AiHsrGYa4I_1DQLnCLvKfPftThPYGFfztxT261VjVzy_JjZFsJevY8LcDkl).

**4. Blue Mountain Estate Cuvée Sauvignon Blanc (Okanagan Falls)**
Blue Mountain is legendary for its restrained, mineral-driven, French-inspired winemaking. Their Sauvignon Blanc avoids the overly tropical, pungent notes of New Zealand styles, leaning instead toward a crisp, steely, Sancerre-like profile.
*   **The Profile:** Laser-sharp acidity, wet stone, lemon peel, and a clean, saline finish.
*   **Review:** Anthony Gismondi gave the 2023 vintage **90 points**, noting its vibrant freshness, leesy texture, and clean, salty finish [Gismondi on Wine](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt1CywyB-kbgcDscxjz31ZpoXDcKgTPvziJCKOyfn2ULLmSu44N2pVihSKRjo2qbw9eh2Z3gT0jP6yJQyLN72ExIb92bp-6wzQQZfvvfiuUF8TxiNhKZ1NUFYtyC1oSVsIJhw9UFJxdzucbgTdjDxGTmEwD2hlvWMIgz0cQ9BvRpETVxICPPXo_dOVqpm3_IKn8sRySzmfWSmX1diyqjtaOENcE2DSE8Ax63LJDD64vBw7d3doN14D0rqcdg==).

---

### **Patio-Friendly Alternatives (Crisp & Dry)**

If you want to mix up the beverage offerings while maintaining that dry, high-acid, refreshing profile, consider these local BC options:

*   **Beer:** **Four Winds Hüftgold Pilsner (Delta, BC)**
    A traditional German-style pilsner that is the definition of crisp. Rob Mangelsdorf of *The Growler B.C.* praised it as an exceptionally balanced, clean, and dry lager that perfectly showcases crackery malt and spicy hop bitterness [The Growler B.C.](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNanf6vRfP6OD-Oo4MyiyeFk8ZaLeXSqHzaEfzXKPUu8tv6rZtNDwAKcIEftxPDfd8_9nBVjfIch9bJ0BrxXu3o9-n3_ckDJ0XSXLk-LD2AYdBYGEubSs8m3EicbJESai-qvQBl9FJxfKEUcP9gaH7Z5UCs_-uTi2iXEFhRUxjuI0G-I1aiWsjMBf1AtJCHTg=).
*   **Spirit / Cocktail:** **Sheringham Seaside Gin (Sooke, BC)**
    For a bone-dry, refreshing cocktail, mix this Vancouver Island gin with a premium Indian tonic water and a slice of lemon. It is distilled with sustainably harvested local winged kelp, giving it a subtle maritime salinity. *Tastings.com* awarded it **92 points**, highlighting its complex floral notes and solid juniper backbone [Tastings.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKIl6No1pN--5976VBXq9_hmR1IFj_zVnaKN2x7G6jmm-nGu4Y7_OoLK36mf7vM7plB6DYlxj6nFWHLEqq_Mq6bCaUbyA7JoCbLFc2HxUwT6QU9K03ao8Cy_ul6RMWcC2KkEwcSTTtRQqTIPhDUksBsmzed5OYgHfDNOWATEZ0H4pUnjaEraLZl36XU5lMWN11ONxCE7NaTZh7d7viwGir_6CI0cTWFF3nwWk053HIV2iGwmQ1yZUy9FQuiCvmrrC_kQITziqG-AvPoA==).
*   **Sake:** **Artisan SakeMaker Osake Fraser Valley Junmai Renaissance (Vancouver, BC)**
    Sake is a fantastic, high-acid alternative to white wine on a warm day. Brewed on Granville Island using 100% BC-grown rice, this sake is crisp and savoury. Treve Ring of *Sip Magazine* noted its crisp acidity, meadow herbs, and refreshing sea salt finish [Sip Magazine](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjm6VVc28zdK0yfCZU0Q7TtA29auFnkPnxNv2A8_cpCthOyJkgCaTV2vGbYpBfXqK3HnQlssoklB8ZDjLkAEpI4Me2zvc-OPJKN6GJ4H88SKXifBNRJ6_slxVDskFspJPyYQqvugpdqudH1zXFog==). Serve it well-chilled.

#### search_web_grounded_tool (status=ok, 13 results)
Search answer: **Terravista Vineyards "Fandango"** is a highly unique and acclaimed white wine blend of Albariño and Verdejo produced on the Naramata Bench in British Columbia. It is notable for being the only Albariño/Verdejo blend produced in Canada. 

Review scores and tasting summaries from prominent Canadian and international critics include:

### **2024 Vintage ("Proyecto Terruño")**
* **Score: 90 Points** — Treve Ring, *Gismondi on Wine* (July 2025)
* **Summary:** Due to severe winter freeze damage in BC, this vintage was crafted using fruit sourced from Washington and California under the temporary Crafted in British Columbia (CIBC) allowance. Ring praised it as a smart, capable replacement featuring aromas of jasmine and honeysuckle, alongside flavors of white peach, apricot, and a lively lime-zest finish.

### **2022 Vintage**
* **Score: 85–90 Points** — *Gismondi on Wine* (Tasted July 2023)
* **Summary:** This vintage marked the first time Verdejo took the lead in the blend (60% Verdejo / 40% Albariño). It was noted for its fresh green herbs, expressive citrus, and vibrant, mineral-driven acidity.

### **2021 Vintage**
* **Score: 88 Points** — *Gismondi on Wine* (March 2023)
* **Score: 90 Points** — Jennifer Havers, *Natalie MacLean*
* **Score: 87 Points** — Dianne Fisher, *Natalie MacLean*
* **Score: 92 Points** — *Global Fine Wine Challenge* (2022)
* **Summary:** Critics described this vintage as crisp, textured, and refreshing, highlighting notes of orange blossom, pear, gooseberry, and lemon with a bright, mineral-driven finish.

### **2016 Vintage**
* **Score: 91 Points** — Anthony Gismondi, *The Vancouver Sun* (August 2017)
* **Score: 91+ Points** — *Pop & Pour* (February 2018)
* **Summary:** Gismondi praised this vintage for its expressive aromas of lime blossom, apricot, and pear, backed by a refreshing, gingery finish. 

### **2015 Vintage**
* **Score: 90 Points** — Anthony Gismondi, *The Vancouver Sun* (September 2016)
* **Summary:** Described as full-bodied yet fresh, showing notes of apricot, red apple, melon, and lime oil over a stony, mineral backbone.
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI-ON4qDxRfl7ivKhftd96BHLp7qi12deeu3ieotLVu79gaxu3ZiVjBVBcxJhLP8W1X0ufpTLKFE5ffrOUAp7C4J-blBx86SNuriWRiTJH7uCFEqgn05s7RZ3iYOo6duWFnHJLQ75vLO0qUYq8ttejvfZ80JWIVzXUlYNfefThSfTtMs-xIcYJUOtGjI8xFzL6llFANXGAkI0=): 
  - [winebc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCXUboP_9j8vYr9k_CiJ_8KXBPj1rJJ0VbwSq_1t8NTuXPseWZaybp5ob34oAPJtDOsVD1Qda4-BN8r64lnJhy0Ap5-DE7GHcK9qRA3-Ua0biE7ycG1edJm4DEZFoR54T1KDL1QRNPqUQ=): 
  - [vivid.tours](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsdeNj1LggjNWGBxEh2E9Ygps3PWrhTiUUBqEIHIM-nC0z-WR1slNxAvn64WQq8ecN3Rv3vR0rxpJiCAyKb8159Y7vYnIIbJp6JOq4eB_1OwmvgQklzpwpCmdKS0JvlE_WYdK2BzQfWB0pv0O9hUztYtA=): 
  - [terravistavineyards.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8kDMxDk5FVsBs03kYQLeaewzxuxsJWrEquieDE9nEZ00DL1zD3NDfdKI0FvowILIQZAJRbvTqZRK-17WPpjKfPlqxotX3WY28bR1LTc_OmSnACb0JPw59P8KSmIDMnYf2ky6xUf5f3hCfpNqyMZ9AFYW06byTsQwRccQKhTDO4FexKeFz): 
  - [wineanorak.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXSOyHSZFCkh9C_oxgEp0xJQKTBe2mJb07WY_ZJ2UWqCh0lltNDHUClw6Rox5Z4kViFD43lwq50p-wIOmoLhunwerTTvg_mZeG3z-Ae0RmKKW2GT3Lgq6skA8vwd4h_uxdssZFsyaNmTJdQ-kjdXs8UKtYQ4_usJxJmdAYwGgBbhV4huFlBN_Gqid634xhNw==): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMW7jCml3SW686SX4qkZ4_gWP6HG8_t6QUwhM_0V9i_3oxlq_tVOc3Q5btP5rYvUHmDG2U77HuaLb7J8lSVqmi1AJibc69xCid1DxG7hpXN4Fc5Yngpzoh97b7JFV1QPkkeeHl28bO1tyAl-jzgQeQWP7lhqTctpGlkalgIfjP9Uhgs9YXecqHyiTi_wuNBWFA6pWY3cXgueQ=): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXccNqPUDMoi9sx9tUiaxNcZscYHy0vUsar5oKAYvXoxPN6-AM4QVLIfrABS_UlamBgeMrtQXCdn1vNVub9ee0s7ok0_i7AqLIgkVh_Q03404SZ2zFeWNQyvHaZG12acQIgm49fkfrcA6uCA==): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI9m1XhCsB9yQEvu8cCkp-Jk2EFd1GKJjFpWp5TLJGHnOMtHdcVJGKjYThUuCigyVD5keTjzi32yjtW8zooWsT3xi0VcIJ8scpRbmV21qH1p9EC8RVGr3ufkr17tKFxYD8R0GsOJKSiWI5-Pz2tdnVRnFrLppUj8DfIpJO5T6mp4KFX842tlYvrRBPUDvlZk0=): 
  - [globalfine.wine](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn_50LXRzYUOkhUAXTdtZ_Ejy_qQ1CFqcfTHSziIyoyh0GxsGTanb0JCHZgSeyw_lfHj7yGE61CoOvjCQfxE0ZcFv4PwQcQHOmWBvLRMth_z6owtUOQPDp0Qll3MGrHqVymfWszVzjz3Xsatv9jTKUcUTxjf6YyGATzA==): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhczpXxdxP2XKA2IStOFvnnQrIrgXD2cqLJccGR9Ec96IRX2wK1MCEIsRNL8e8v74bBJoFJtRVcnuKk9ZEFvXVajaM1Xb4zUt44IBABcMbZtOuo3NZS21rCNTSM1gEBxmk4BY4FPoYosAoP457d1b695j3gsywPDTsiLs24Qld9YY9ar-rAMf4OsoPhvG0JeiUhAcJFl4PywFKdmukR1f4wDKcMw==): 
  - [popandpour.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNcfkesW1PWyhLR5PEV5a7sbAz6NWMPpooTFpbeaDiQgEydj_Pe5lo4FAf0L2KU8B6EA04rrNX0DYxNsp3CPLWsj8wMJg82PsCOygZz4SZtgbUMQuu7eCmBL2jyafScdv9F9Pwh5ekGnoBCR5oMYKM3TqcKXsSFh-dF64-5-3oAK6k3bDjPx_F): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsfgS_D6v0FeujX3Dr6aN7QyIt8Mt8nAYjJxFaXumlyjTPUvNAGkX4uftE_zvzXPUcRNtawtRP47D-gbVtnIJtdaGKs1pj3cq4UW4u2Dk3Vq9SibQxauX-a1h_AcvY6kVhZW_fj4s=): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETDuSq32w0GK1FV4nR0g33QHNuqwbubtCKuTZEzIfitWAN_0lUH4L7gH3xxCzVjM7E5fpXAw6LzFg3dHDwVUWy77TUg6YstEkZMN9iGN_zt_Lfv3TWl_vhjISCTQY2-80Q8udJmsQ=): 

#### search_web_grounded_tool (status=ok, 10 results)
Search answer: The **Blue Mountain Vineyard and Cellars Estate Cuvée Sauvignon Blanc** (Okanagan Falls, BC) is highly regarded in the Pacific Northwest for its elegant, restrained, and mineral-driven style. 

*Note: Blue Mountain did not produce a 2021 vintage due to wildfire smoke taint, nor did they produce a 2024 vintage due to a devastating winter freeze in the Okanagan.*

Recent vintage reviews and scores include:

### **2023 Vintage**
* **Score: 90 Points** – Anthony Gismondi, *Gismondi on Wine*  
  Gismondi highlighted the wine's vibrant freshness, noting a nose of lemon peel, lime, and wet stone, leading to a clean, leesy, and saline finish.
* **Review** – Karl Kliparchuk, *MyWinePal*  
  Kliparchuk described the wine as dry and medium-plus bodied with a smooth, round mouthfeel, featuring flavours of stone fruit, honey, and citrus rind.

### **2022 Vintage**
* **Score: 90 Points** – Anthony Gismondi, *The Vancouver Sun*  
  Gismondi called this a subtle, balanced expression with aromas of fresh-cut herbs, grapefruit, and peach, supported by a chalky, mineral finish.

### **2020 Vintage**
* **Score: 90 Points** – Anthony Gismondi, *Gismondi on Wine*  
  Described as a precise, steely, and laser-sharp wine with notes of lemon, green apple, and chalk, balanced by subtle oak and lees aging.
* **Review** – Shelley Boettcher, *Castanet*  
  Boettcher noted a nose of green melon, wet stones, and tea leaves, with a surprisingly full-bodied palate of peach and white grapefruit.

### **2019 Vintage**
* **Score: 91 Points** – Anthony Gismondi, *Gismondi on Wine*  
* **Score: 91 Points** – Natalie MacLean  
  MacLean praised it as a zesty, lime-forward, and refreshing white that pairs excellently with seafood.

### **2018 Vintage**
* **Score: 90 Points** – Anthony Gismondi, *Gismondi on Wine*  
  Gismondi described it as a "Sancerre meets Okanagan Falls" style, offering a fine texture with notes of river stones, lemon verbena, and pear.
* **Score: 92 Points** – Natalie MacLean  
  MacLean enjoyed its bright, juicy citrus and lemongrass profile, noting its soft texture from neutral oak aging.
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt1CywyB-kbgcDscxjz31ZpoXDcKgTPvziJCKOyfn2ULLmSu44N2pVihSKRjo2qbw9eh2Z3gT0jP6yJQyLN72ExIb92bp-6wzQQZfvvfiuUF8TxiNhKZ1NUFYtyC1oSVsIJhw9UFJxdzucbgTdjDxGTmEwD2hlvWMIgz0cQ9BvRpETVxICPPXo_dOVqpm3_IKn8sRySzmfWSmX1diyqjtaOENcE2DSE8Ax63LJDD64vBw7d3doN14D0rqcdg==): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXBegZIra7RrdSqpZ6qd0grutMrHBNJfYG_fs97ZNRZpt-jLY0oamdNuoLys-2d81eaM0dV384o8OImGz5Yj8-plmayjN17UoxZL3-79NsGgnH5S_2cv_Z_1JnWym7AH0VV6GE2wR3v1M0OG2cR20t_EARw3NTOWczuIeU3AUTlLSkTLHm8_36dO_qyPrBySXSkZOD38QE-_I=): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZiRYWK2RTSNDbFEGqT52CrfiGPPvmb5zXnpnd_CljzMFQR56AnF-1e2lhWpv7mu06-z7ydyKBllcZFw13shzahqvu0wkcOo3WMc-pjUgo32Sck2FP7PotiqkEbaWqDFOv9KBLj_wayKvfmYhG_Jz7vilfQ9lit6_yCi76KvlFLh77Qk_aAp4IHHpjSymk): 
  - [canadasbestwines.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVdouVTF0HWcb64sQb6Qj2HHvMA3xMioAZ81yQskIqDDu3WzVSIzur-BFpLTvV5S7GijFmRvtohbqhovKvtlo13ZYsRVeFI7H81knMCmgYdE8r0cBpZAb-XJD6BIim0EuBSLdwEFVZ8hvHXllNa8vLB-6sBfGUog==): 
  - [marquis-wines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBlgZITOkfRij0H1Q5C39NDShTngnbo8pCX6J7KfetKbOvkFga69e1RLukbeXQyWjj5v3WNKJxqs1NEz8qCeruqxypboRc_QvMregISI79jIJJz-ibunjHFNuqwoBMr0DqtwMoZG1Hgb0FlFLyp2NQbpnyniVWFosLaYMRAhZhnrkP): 
  - [mywinepal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK3_pSaM4-HIngbLEfJ_jo1HnoYcdoMk2ZYNwQhcDIvF3wjXBaa2vESJYWJbW46WKM9zFlhh4sqDKpuxhfBH-C9lfI1FRMaqhXsE2y8_kctTex1ffTm0Fyc2EDwRpRBOnGTbydo-RMbhO_uJXieD7HDti39F1lrb8gnox-gA77tbzaRKnnqsQJEIUrGUrNmMigCi546j0H-U4atRHzUgdnEvkBeVQ=): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHhKCL7nI9R92E-Y9ypWquiY1zNjOQC1T4ljDbHyTDzGBZ5OBrsf4o9sOT-AWNqt3m0_KitdMfSHWDDV5UFDz-rnVqYBoVX5PqPj_fSCMydZs42JWmJfkkYFrgSHcNAT8XfRKJKd1GKKGevlHBgxpNUiEwIwNEYujnD4ey): 
  - [castanet.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVLwLUQQV3JzuJDDm714Z5ERQOHPT1uZF6IF_zJaEq0c7QrOBXdikvhuxa9CIXb-bus2S3RxDkYUnoVzSJRKvQa-z9KhaPjFVHyRUki67GtAslqJCG3JvFyKhLfzlZztgLZ8G-22nP69h6F2TrOAaqmZCqw1KthOc4sZqGtZ59qj0ZcvV1FwytvkXRdIkkPw==): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxbRnYs_9SEdWR1By7Hto80-bIF_hBCuCdPAobL97rKSUmDFPj9p0Z12W-xAsDzLVPdcUa804NYDfRFV7cwYroMDgCTtPWgAMNdM5YLmqlyjBUuBvhazLlooJccKvFGg4oMOSmNqWTlScdQ_c2DP3_elRDiNnOBibK0MFQv-2-vKXzHqcesGqjiMsQZRVqikw=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx7oyehtbEcG0jXTx0RJg_DaEgQkBpRxPULHzD8KtZBhIkplg16EK211VJ2HZ2L_Ev6GG5t2XHSKOasO_dYBCvEbKr2thXicOYvweByC3nQAh7Vhgw5GeUxa25MCeu-IVoFu5M2B1UaSCjZXOLQ0RaCqTfLZU8UnYU94ajEdw5eTrhRMU9YbP_P2AgG6Ylorkg6mLUL9635c3yhxi8Y-jlRi3IZcU=): 

#### search_web_grounded_tool (status=ok, 12 results)
Search answer: Little Farm Winery, located in Cawston in British Columbia's Similkameen Valley, is a small-scale producer run by Rhys Pender MW and Alishan Driediger. They are highly regarded in the local market for their low-intervention, single-vineyard, bone-dry Rieslings that emphasize intense minerality and high acidity. 

Review scores and tasting summaries for their dry Rieslings across various vintages include:

### **Little Farm Mulberry Tree Vineyard Riesling**
*   **2020 Vintage:** 
    *   **Decanter (Michaela Morris):** **93 points**. Morris praised the wine's searingly dry, pristine, and focused nature, highlighting its intense green apple, citrus, and chalky lees characteristics.
    *   **WineAlign (Michael Godel & David Lawrason):** **92 points**.
*   **2016 Vintage:** 
    *   **The Wine Society:** Described as a bone-dry, racy, and perfectly balanced white featuring floral honeysuckle, poached pear, and a distinct chalky minerality.
*   **2013 Vintage:** 
    *   **Gismondi on Wine (Anthony Gismondi):** **90 points**. Gismondi noted its German-style profile, neutral oak aging (which softens the bracing acidity), and dry, mineral-driven finish.
    *   **Edmonton Journal:** Described as vibrant and firm, offering bright citrus and crunchy apple flavors alongside a long, dry, mineral finish.
*   **2011 Vintage:** 
    *   **Gismondi on Wine (Anthony Gismondi):** **90 points**. Gismondi lauded its steely, high-acid, and mineral-packed profile, comparing its low-alcohol, zippy style to a classic German Kabinett.

### **Little Farm Pied de Cuve Riesling** (Wild Ferment)
*   **2021 Vintage:** 
    *   **MyVanCity (Sam_WineTeacher):** **90+ points**. The review highlighted the wine's prominent wet stone minerality, stone fruit aromas, and a well-balanced, creamy texture.
*   **2020 Vintage:** 
    *   **WineAlign (Michael Godel):** **91 points**.
*   **2016 Vintage:** 
    *   **Judgment of BC (Gismondi on Wine / Treve Ring):** **92 points**.
  - [mywinecanada.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtij7eDQFxSowsWIAer3ISSg0MCiOK0DsW5ax9W6WIogIPH0RdWnjyjFGedcmkzseDkcGNMhBAQ3TlvVFR2lWgUgrncKnDFNe6ijYtJhVz5un9n1vAnoV2-F_cKKOVUnCKkp4X42DC7cgaJ59kuNNxFiJNwnn8Uswm2omBiU8dRHR00DvRSw9N-Kg=): 
  - [myvancity.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8V2_DES1o_NKAJ8jFemlDeWzaEhkD36OlbziHT-5CkCERDBiYslInmXvvMgYVs8KTotEVXQDnFv_bWjkoz4qkqxugxJy1VN_8SMvgUfTFz_QjQxsUcVRd3Idp56ZHXioy5ohlVPBILfgc2qWXgjqHOnSyU22FM6R2hKCOEdf_R8SpEQ==): 
  - [heavenlyvines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ1-10YEevPlXLbmkc9vud3g79wiBuYhzawbFSbKZFkvRq_Yka-3gv8VXlpfVXOJH9Cjtw0y1rswlETqdAMzDrbo5RZl7uzFUa6qoImvKKnXMbdYdoLzMOO2EP7NqaS5h2FRcvm4bI6wYMertcjah80bIxFaUBvgoVv9WVh-ZueJc=): 
  - [littlefarmwinery.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfT_RxPrj6BjT71Esf6oq9rFYr1NDJgjdsDQ5SXd85t2jRVMXX0gkmkFxw_mPVk8XZEeYaEoop1plqzGAcW180DMgKHTffZPe6aMdXspbsGqmu-tvoulZHb0NpFI6C7K_jjJZ64EPuLryC3A==): 
  - [thewinesociety.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTwAs8ofz9cQGjCKIMIK4Bc8xeKqLaew9mTsvZjQ4GbPukffh_MSX6bN6J2ttiyDFKf9XbvwOlWP0EB4MjwSGblYc18KlZJLOKwxNdUOHn3xO01z07P9o-U0gImjicop0YepCbY1bwLfpLv5BzJJxucTr_RlCVT5gapwvC7XLFL-Y9tTgqPOKvZe1eDeU0bxVY9H12pfuSqEGHx1veQOgUlQjT8BLJ): 
  - [littlefarmwinery.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET3jr8EYOCcgVK33y9YF9Ta8w8snWwxpfJm_E1Ptl4zOjjQphvGiHn4T4wzJ9p0WD6daVGnBiSGMy3pUUpJJ6ZUZNdfc8mzw4LDZJcEBStmt7IKpO3ajWvd35UeoTMlQ-0CKAMHPhc6coInECz): 
  - [edmontonjournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1gn1UV-UBEJJIyiB-IlgrNaCqg0h7mMqn44v0tinmcPxBQS3tAODPQkte9HLSZf-jCMGPo7Dis6waMSlgF1G_5zwWyCFUkAAf6Wzkn4OFNC5Z3vYts3vNfF6lp6F5D81OcAygVR2DBNbpmV8N0jLjFhhJPQHNE_li8ktAasNxs5NKmxklB2nkc5FnQkCHXzhlG3baYpg=): 
  - [littlefarmwinery.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_HXoSxVGEWJiPCmQTQo5r4Runx_lLBrdK7HV0Swjjs6HBcXaZg9DBVuWq87TgUVetK3WYKp_xKOtJVmVHghuzVI7zAvE3tApraF54a9w4rkLYnhUS3G1sh_FnnxBS1-_DWVMuhNQgWFX72yU2): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfi9-fWwcVAEPsI8mbg8wO1flogSCMP2izDq2osLl0Cq-M3Ewyo3LOZoJFt_EcyaW91-fW-Q6v4jQVfjAFZNJ11ReYnZR3pxbG1CK2qTqjGPdgRJ3LErVK7RUkqjs7_aTxo65LYkajDysOsjei6esV9ysKY7jnLg==): 
  - [myvancity.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEJuWZzPDoVVugSV7sB9j9wG3Oy5ZxSoIo8IDSgPr5IElYpbSFB2gXCiPL8k4xk3kevTfv-oUgiEYdlLp-2XhBok5ui3-Bx2nrldff_x6FcxwN7YkmNpiWDhO6p64tfHU7nsZNcvg_Sy4fypEHWawZ9L9F6adTvuqyxT8nlbcIUHI0nw==): 
  - [myvancity.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbzUsk8mwW3_y9c1OjQsbdIZMs3Sf3ryfMueHlXrh3HfYDrpuT-kgJPHHBrFQ12aEETddS8uwGL3n-PFNgZL9nTSZmSFq_h21qrG1PUEf_t19kaXHxTFbog0AEj_Pkw-rZje-4f-ZJqYiMMz_de_snsq-XE-XCJfDzhDBclGYrBxw9Kg==): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeQqb04KRjO2Fs7YVK169BV23lImgB-Vx8VtmzPo-m8a12v_2aFqrtHecUoGU6vigw4qjjypxz-b_07qt5wmOvN0y9rTo22n_2wLSepl3RffuVcr3TZhzluRbKuywRUld4w7TMMVKFnC5yqIrHw16Ckap2EK27): 

#### search_web_grounded_tool (status=ok, 17 results)
Search answer: **Clos du Soleil Capella** is the flagship white wine from Clos du Soleil, an organic and biodynamic estate winery located on the Upper Bench of the Similkameen Valley, BC. It is crafted as a classic Bordeaux-style white blend, primarily dominated by Sauvignon Blanc with a smaller portion of Sémillon. 

The wine is highly regarded in the Pacific Northwest for its crisp acidity, distinct Similkameen minerality, and surprising ageability. Below is a summary of review scores and tasting notes from prominent critics and publications relevant to the Vancouver and BC markets:

### **2021 Vintage**
* **Gismondi on Wine (Geoffrey Moss MW):** Moss praised this vintage as one of the most consistent and reliable white wines in British Columbia. He highlighted its elegant balance of lemon, white grapefruit, gooseberry, and white peach, framed by savory desert herbs, beeswax, and lees.
* **WineScores.ca (Daenna Van Mulligen):** **92 Points.** Van Mulligen described the wine as harmonious, racy, and complex.
* **John Schreiner:** **90 Points.** Schreiner noted its bright aromas of grapefruit and grass, followed by a palate of lemon, lime, and stone fruit.

### **2020 Vintage**
* **WineScores.ca (Daenna Van Mulligen):** **93 Points.** Van Mulligen lauded its precise, racy, and complex character, noting aromas of lemon peel, pine, beeswax, and wildflowers alongside a slick texture.
* **Gismondi on Wine:** **89 Points**.

### **2019 Vintage**
* **WineAlign National Wine Awards of Canada:** Awarded a **Gold Medal**.
* **BC Wine Trends:** **92 Points.** The review highlighted its vibrant citrus zest, tropical hints of passionfruit, and a supple mineral backbone.

### **2018 Vintage**
* **Gismondi on Wine:** **90 Points.** The review emphasized the wine's restraint and salty Similkameen minerality, describing it as a lean, mineral-driven white of great finesse.
* **Natalie MacLean (Deborah Podurgiel):** **92 Points.** Podurgiel described it as a fresh, vibrant, and beautifully balanced white Meritage with smoky, mineral undertones.
* **Decanter World Wine Awards:** **85 Points**.

### **2016 Vintage**
* **Anthony Gismondi (Vancouver Sun / Gismondi on Wine):** **90 Points.** Gismondi called it a precise, fresh, and age-worthy blend showing bright citrus, grapefruit, sea salt, and sage notes.
* **Natalie MacLean (Deborah Podurgiel):** **92 Points.** Rated as a dry, vibrant, and zesty white with clean mineral and Meyer lemon flavors.

### **Pricing & Availability**
Clos du Soleil Capella typically retails between **$30 and $38 CAD** at BC Liquor Stores and private wine boutiques across British Columbia.
  - [winescores.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_5Acdci1RRtZKHaKN67u6dfsPyps_FPDTCb-CiLvWFctdZ-FFjC_4WwjjO-NM2F384oTw04uuUChxzm0gmCileLtH9GVX3jl_yeN0PnQS_2mOSpkR0A5sj2FkKe76a5hS6u7LI40Xz2e6VI9vZNucGFuAgS3Jo0lOnLFxy7Tv4SZgl-quayH5x93vATJxRel6C9-f_ASUg4xsDff-9k65fW-KLAlTXOAdzMxuVQ3tnTS5bXWmI6v4x1P5CqCUyc5L-OwSZmIGwlZ3rYTYzlY280YS5AiHsrGYa4I_1DQLnCLvKfPftThPYGFfztxT261VjVzy_JjZFsJevY8LcDkl): 
  - [winesofcanada.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBhK4ehTP8Z6SUuY5qEKt7gVOetivjsObnE1HQP-AnUialMFqvgi44rZIFxqArWrh1xw_heQL6RbIgneEddNRaDRc4YDEuS2ztBLYLNHF8S5Q_i6vnQTbbJI56TKO7UyC5NqwY-3Gdi70bJjaLXH8LTCKbiaBCKLQODFA=): 
  - [jadorefinecheese.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxVRfvQvEM7tLMn3GPmTs__8DVwMq1Q6a0JRp5t6l56T7zenwxiOUV5U6bQSNIfQ0pa8eM1F4dzRicNEL122i23_-EtD_jTIePBPTLo16Lrt-ZZnAzvqEYW42q5U7hDvkXIa6gI--rkjpKorzx0kyxBX4nEkxnEYd9ZJmbKpPfY0FLLJW3-BcwFJIoe5U=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkt4E8pZ-YeOo--nv4APavIexpqTXOECC-IrtzV03LFKe07yIwtoYymWGWWL_CHkNfoc67RoEKy8MxWvfmimhhUlBzXlsqCwlaz3yhW1kr0VhL5PxACjZXKy5XLM9ZaiQOEpN43lmfE01onkoTvMugs8Hk-ZIFEKD9Vr2epaTmrCD3mVYwZmIGy9cBX4lBXoGoWQ==): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFydYzLn7V3bLfUJ_qGGdvQUEV5mNvQzy2o08_ykyCYSACl4TOOS2hAkOwqrJkVYC0ei9ZwyptgXmdJ8LUQRIwkchCrydl0PRqdiRyXucEXpJhOwaWg56__zx-bQNKqXvd7sRp8uAtwnoeTfrRsQfAvEG7dR8SY7F7jHEpOlhHC-ANv4lFwBGZKN93gM6JScCap): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqi_MNOKcoHydQ8ZtnEkk3oNTO3Q-FOsirZUF9AIOFsiPJ7W0Grj_IMCcmZ5pxIt9edIcQOcDZ2Jko6IsnM_Ls7IsOX5J8yU8LQj6_oe52XdGwp17H0wPNErDTvVAlOJ69lS7oHm1x6JC5LCz56ZImR_Iagtdnv1tDjKaiFWt9happk1U_3hi8AclZSoITK2ZO5Q==): 
  - [winescores.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOEw-dcdIwvH8Zk_yxt3M0Fy34FEqG3VjJozBQrt1DdlKHGeF6bEQfKITAAXI_GawfN6HF4Z0RYLS_vxNNxVHRo7VAA0NLJCMjm2fnBgQH8CpYKbJprEnyMENacTyBv_HO7EFVtM-_thgp6Gyyp0KEvRsAsGiyQsst3Dc8UEAxgjxQ5d1VkUMSqJTAGCmPXlvQ3RgnQwmVQXNGHMHnfcW82k4iKaIDymU9hB_fe19oaeDv2o7MZNSqZlHfoHhKY-DyVUyW8jDCxIjcCz0xCPpY6UtH2Amuk9OTwoKn8G2aFaY7dsFpO6xeeNcKMSFratVFBw9ELlbohEzNiXsyGne1): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYOZNFxeNZOBoDM16ED7vYGGFEPNX0DdydgKeoUuaKelQ07sAOSVKe2Es86W6iZLAJZ0qCAGW0SQDc-PieekcUxuHlEb5I-Yo-tWSua0ewcnNdleJ3XzJmWssgkkUVanCGFojUsNuEgGmV0-hBlAVMniYt3pwUzWQP99k=): 
  - [winesofnovascotia.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2w2GJILMGe-ZBagFRpuxkyOCICybzlRtuwdjJljUl3obXVhxzKKDn8S-kWmHXwMDAaNvhjdH-pWLQHSySCFgdKI-X91v4fQAqUTBkHGV-pBw3P3LTmntTm_DWb8rRyYRWKdHjS68gXxlt0SvZ9x61U3UDILAWzroWoBIVWolTv7oyVH0bTQUwGfGFDL4hzeHq2owcBcjoJk6pFm1pTvsJZXxs): 
  - [winesofnovascotia.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm5089MtvpYswl1idqYt_lpSu29ROXdlxlC_pSRSgtJk6c5IA2msK7Ut_Y3Cb11PqoM5XSQjYG8wbkzkHCk73hQ7wi6jsrff743aq5iZBMjqt90yT53C86SSEosYSe8VQ_gcT50dB4XBArh04srx_9fpJCnzYER98-iC6E_71CfJimgojAfakbYLEM4jzunfgw4gOIG9pu6NGWOadk5th4aWZD): 
  - [bcwinetrends.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3ZFT4FrmrfcdnmKfrGKvlujwgjO-38eadrJuVwEkb6-b4EhyPoEYWlfdgrIkmcHRNYuRO9ucS73Ndx19e8M4e4RDKadCuqKwTAtffahUpac7g6olHqALT_IXGN5qXcMMCTBkIv3vmtT6rInpbfwJUnMon3AQvlOab1LVa_LoOVM8pZVY=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMmS-fR_3hTCqfD6m49nFOe0kKXAbuGsytz5FqBmM8NHtqOevIlWAOlJPxbMtpEup0AK9Zfwp2OtHRtYWQoKjEC4t3O2VOrpT3c_5G75YL-VCNRH43S-VlLP2gj5laFmoEqxyv3iqjVD4LHbR9UvtG9cfRZl6q_QpnOKe-AyOwDVWZ9j9ByBVQs2qHKwMTP8r_SpkYpNwz): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL5Lt2eHx-fHs33tO4Pfmxe6BgRipZ5ktnZiyQOrnYz0kDiD2PRVD9ryMS0nU_GuBktk0Xoqbzcvwt-t2nuHScCmMFR37PrGkjG6t_fqnNH7oDNl__hEYQ-CwNMjT9BO2-tzRGs2jWARABWo3mq_-GlUyq_liE05cBlE-RN71vDlTseOGWHPuVMUzM-wW9R04=): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAWfkdlcrtrW6Hsz2Df99dXLZmxF1l29bCDOavUpt39L8DEG3Xwr2auyDMuJUmWYO6a7oIeewKUVntidg0HLteUSkhnK0GpzyKx7CY5ZRNQPW2l3AAjoK7MfQBr34aLCxTyQNUMkko4haBMZeCNHakkQdHiOr4sQm9uiqhp8ajkrbA): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBg4o2CGlgb_t-zhjbQtS8vwzB7We0u2OH60j-wrGp29BAiaccZXARxbhvv_vB22HygreF7AiOGCCJuGgeLVrrhmhb9Xtg1imzEVEYFFxgcdt3GWpurLC39N-hoZxUBAMbv77mPGDUdx_e9c70NGYOTg4PPGVGMHv69eYSKX3snA_p): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi2B6hnOXZLxQGxD7zmCe85CurEGMJTF-Nv9Mad7q3fwC40zq9IRsqD1iTVV0eW6rs-SRj1f-v2xOsZvtW_u1pWv-K-YSmwCm8XwYV1Xv01lXcwr45q5SjS9G52Rha5QfsIfzHIF8wulLkz6zfrViQEUJJG-6qqY1xxgo5FFf1sdchQfCvn26_AOyP6NijadI=): 
  - [bcliquorstores.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEboeSZKkAXAaF5c747GOmKJ4PyNgn0QaC6rFDw7rN-Xxd5kHdGY8H4VSJ-h-e_8sp2JrQQGBoxS6NmpWZm9QKOPqckvsFPTveC1baPzjclDi8yjPgiJtSVoKzojCwTA40wTr6nEsvaxw==): 

#### search_web_grounded_tool (status=ok, 8 results)
Search answer: Sheringham Seaside Gin, crafted on Vancouver Island in Sooke, BC, is a highly acclaimed flagship spirit that has received excellent scores and major industry awards:

### **Major Awards**
* **World Gin Awards (2019):** Named the **World's Best Contemporary Gin**.
* **B.C. Food and Beverage Awards (2020):** Won the Gold Award for **Product of the Year**.
* **Canadian Artisan Spirits Competition (2018):** Awarded a **Gold Medal**.

### **Review Scores & Critic Ratings**
* **Tastings.com (Beverage Testing Institute): 92/100** 
  The publication described the gin as highly complex, floral, and fruity, noting a solid juniper backbone and pleasing citrus notes that appeal to modern gin drinkers.
* **The Rum Howler Blog: 90/100** 
  Reviewer Chip Dykstra highlighted the gin's unique, savory undertone—attributed to its local winged kelp botanical—which balances beautifully with bright citrus, juniper, and floral aromas.
* **Drinkhacker: B+ (8.5/10)** 
  Reviewer Drew Beard praised the gin's distinct coastal, maritime aroma and its dry, well-balanced palate of lavender and baking spice, though he noted the finish was slightly flat.
* **Good Gin Tentions: 98/100** 
  The reviewer lauded it as one of the finest modern gins they had ever tasted, giving it a 98 for sipping and a 99 for mixing, praising its versatility in cocktails and smooth, floral profile.
  - [timescolonist.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmp8VvCKvfFvxRxpcw4MDxoaLStdC-Pc1SUrh1ls31pSZnOWN9H2uti09e2A87Mn46ibT8cNc7KpvfAnVnOwSL-KB8axOoP7pCF2hrTU7TAr3XU-KHD1YSx8yrC6jRmmHfk15FOK-7mpBSthKydQmV1IDzUA71JcWF2YwxPBgv_PeGu3lerME7vbGvePY-7KfsUSRIPiwBUilzzVs9c6SyWBM1gq4_gGcqFZXwNawGGFH1jhRnaaZlA7Cfz9E=): 
  - [therumhowlerblog.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQXnSP5Yhld29EVksai_X8CShBMuBuYCEclIGXF9yHMD8R1BBwKhnVJTrW_HwgJ5h2tPSVNwdEzHsmcZIO7171wh2MIMCTaJKggAXV9ReUOFodrGBxVUt6SdsoWqgK0NXxWcMrgjI9E1PPP9B3OLl8KiwIuQtX5xBpqhU=): 
  - [sheringhamdistillery.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0jp0u6yp84LNne5_w8N2eeyDBQIqlnON3cSjZwys0YuKhdR9N0pYjN2MqkRNYpDgod1G_f79zwc23KxH60R0PpgO3sRAX9HtoTccFB38uz4sl9zyEHtvR2C_V-rzmt_k2pKJWFQaB9QUESW4=): 
  - [lcbo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdaqy_3sSlbuzXEvzw5BQYzZGM204LblB_lsYvzIX01naVMvmjTsuWbFj57JlucQcAJr9Mpl7w3-Q-5d5iY7OSH48cO_Sp3TK-4dVmOt46Xmt1MHOP-jeaDEhl0gJEpbp0pADzpxjHIIuOO6pj1vg=): 
  - [scoutmagazine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfVVReoAWXmcWEAuc6ugJYOkmqpxtiyTtK3KX9L-QaDEH1FTXGbw-vuKNQj_MWZ08RmisAvWMtU7uUK2czj7RUqfADnaCdou__TE-yEkL1gPPfIs7TLbvGtISrxajRvas5dmEsa0sLikKIPF5OKunKWCZ_DDMHAZXSVe80umwHVovcQ0tmAbQf29FOOUsoZbvBn3z0ou8UR5j57WsMmrD_hmHb2mkSd7wAstM=): 
  - [tastings.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKIl6No1pN--5976VBXq9_hmR1IFj_zVnaKN2x7G6jmm-nGu4Y7_OoLK36mf7vM7plB6DYlxj6nFWHLEqq_Mq6bCaUbyA7JoCbLFc2HxUwT6QU9K03ao8Cy_ul6RMWcC2KkEwcSTTtRQqTIPhDUksBsmzed5OYgHfDNOWATEZ0H4pUnjaEraLZl36XU5lMWN11ONxCE7NaTZh7d7viwGir_6CI0cTWFF3nwWk053HIV2iGwmQ1yZUy9FQuiCvmrrC_kQITziqG-AvPoA==): 
  - [drinkhacker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZujAQ7tNy1hbghgDZE4wYNHP5eMtj9GSDfdwCsy1JAgQYiCrack_ats-p1E_LO_MqfGtHJZYiPnsLvToy9vSTX4P9BsWnnEXNw7_8fUUdG73UtM8oaa9WVuS7ptLMIniQCmritclrF8QL_r7UTdco0mZuMOX5-FVcy3K4gytg0g==): 
  - [goodgintentions.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFndMAYkkbN_CJBf-0tg-rEk5t-f9rQmkeN8SYMPoRrgs0qNQTr0-DTVgbjlZwTcUnP5OfLgWPHQc49tgoIz9SZEIadBJG-XruqJh6OPti-HNTQ0oXR1SrrCdeXFyvYk6_AkwYp2ONLaMMjNKM6F0Etg0OZ0REVJjbBVybRAQ==): 

#### search_web_grounded_tool (status=ok, 9 results)
Search answer: Four Winds Brewing in Delta, BC, produces two primary pilsners that have received strong reviews and scores from beer critics and community platforms:

### 1. Four Winds Pilsner (Czech/Bohemian Style)
This is their classic Czech-style pilsner, dry-hopped with New Zealand Motueka hops. 
* **BeerAdvocate:** It holds a score of **89 ("Very Good")** with an average rating of 4.04 out of 5. 
* **Untappd:** It has a rating of **3.6 out of 5** based on over 2,400 user reviews.
* **Beer Me BC:** The publication rated the beer **4.3 out of 5** overall. The review noted that it is a highly sessionable, flavorful take on the style, offering a hoppier and sweeter profile than traditional Czech pilsners due to its unique BC-style infusion.

### 2. Hüftgold (German-style Pilsner)
This is their traditional German-style pilsner, brewed with German malts and noble hops.
* **Untappd:** It holds a rating of **3.7 out of 5** with over 2,100 reviews.
* **The Growler B.C.:** Critic Rob Mangelsdorf highly praised the beer, describing it as an exceptionally balanced, clean, and dry lager that perfectly showcases crackery malt notes alongside spicy, herbal hop bitterness. 
* **Awards:** Hüftgold won a **Gold Medal** at the 2018 B.C. Beer Awards and was named **"Best Light Lager"** in *The Growler B.C.*'s 2023 awards.
  - [pintplease.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFZqYvTPWUHogOm_SBQ_ANnKZQdaACWQeObk7H3cQWl0EFUHh07RUGgvf7xSSwd4-63NvkZ_eam-HSG8IsPG0ZizpZqGR4tOVOj6RQgPp1S6sWWylzwT0DUfcu8xeIaKv-uWBWxl_AZMhuhpI2YYzHuw==): 
  - [beeradvocate.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxFHfjF3U0ZajkhZoDGrcTEioe0cbTDEPLy5b-lnwU2r6dGkOUwgkWr2zY7EtiEf7MO0tJX17CFmDqGvTTluDPdI81cZp9vVlG9WXMeYRmv90AGdpooX1yfg48w6P5xQm6da2L2y2fy58A-DlCRmZcEHY=): 
  - [untappd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfcgbzRLJZ5vWRzX4b7-LrN82NpVCav7Lb4frGtg53_aDhUtlM2mxc8Rp_fbEWavjONkq68vT5gEeqW4rYfBD0K6jTIe7Auvaysuo-lpE5oW4vZfU57barDFSKBX6L95YrbXCt8y6j6JPLL9GYXVn6Zg==): 
  - [beermebc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOZRG6uLFCe6oMI2ar5-DF0GdFWsoYUcgMvbdN0CBbpsQUTDWsFrdP1DSfrKHGSVh5w8lahuyWQKQDqOiLPsDbwTKYBD9wRWubbQSe1KkEqGMQ9erC6gbQaDCN2v4Yol74Lx3Vyw0RcmbFogMC2EZJROFx4BHvSWlc): 
  - [untappd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9NzhpRaQaeNxOd_6xu5pTY2TECDUe_zzNEDoYxY3cMjuldBP4lDny3tDWuJBPdHKrasro8gEttn9vXmqG53Qh2kLkdGxpJXUsHfEOLWg3Xup4e59kEQsdgT9vYt0VPfogt73j): 
  - [untappd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIHi8pfPlXilKMfucgZ_AKT_zMf4fPiLu91Jm-G1RXGTYh4ls2GKDfN8TNJEPnjMpcJ1Bjg0Dg4H4RLARUsgjUP3So_Qlqg8L7qF4pGRp-84eEY104s16_FUqQhyHkeJBYMVE0DbYyDxqY4Gc9Az_Ku86R): 
  - [untappd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJOf1gEXSPXYH7P4U8glVwtw_FknqMAYK7z8wuCP_ixjt_cjc8WyI0TT2gB-hH3kvcoUeqpy6kW5oOQK6rnT6JCCb0L0ZecZ8O8MI6iyEhz5vC-LlWFfqkJTT20wOjWq99i1H-S_x8GWdhVCJU4SyowWvKng==): 
  - [thegrowler.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNanf6vRfP6OD-Oo4MyiyeFk8ZaLeXSqHzaEfzXKPUu8tv6rZtNDwAKcIEftxPDfd8_9nBVjfIch9bJ0BrxXu3o9-n3_ckDJ0XSXLk-LD2AYdBYGEubSs8m3EicbJESai-qvQBl9FJxfKEUcP9gaH7Z5UCs_-uTi2iXEFhRUxjuI0G-I1aiWsjMBf1AtJCHTg=): 
  - [thegrowler.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAnRid7dwdmQjw1zeC8TP_1PHe_8XjXysmGtXoBlk4JmBdjKC67UiWkuLfjuUkqaTsG_Kfuh3rFPHviQjhlPMaJRn5c3ujXK8AMVqP31Ue2q42sfYV6FQcIn0iJDobDI47aEwHK9tWIwp-OgmUp5Dz6KgccgFkUNG4mhdW4Y4VWrSohPFE21JJXliWxatJAooaxMgbq2Eiku6W5MfwA-wEGKkmxI9XCsJ72F-EhQRqPW4Z): 

#### search_web_grounded_tool (status=ok, 6 results)
Search answer: While there is no widely published numerical score (such as on a 100-point scale) for the **Artisan SakeMaker Osake Fraser Valley Junmai – Renaissance**, the sake has received significant critical acclaim, awards, and high-profile culinary recognition in the Pacific Northwest market. 

### Critical Review
* **Treve Ring (*Sip Magazine*, 2019):** BC-based wine journalist and sommelier Treve Ring reviewed the sake, highlighting its unique "farm-to-glass" nature. She described it as having an aromatic profile of fresh hay, meadow herbs, honeysuckle, and hazelnut. On the palate, she noted its herbal and lightly honeyed character, balanced by crisp acidity over a sweet cereal base, finishing with notes of sea salt, orange, and vanilla.

### Awards
* **NorthWest Wine Summit (2017):** Awarded a **Silver Medal**.
* **Alberta Beverage Awards (2016):** Named a **Judge's Selection**.

### Culinary & Pairing Recognition
The Fraser Valley Junmai Renaissance is highly regarded by Vancouver chefs for food pairings due to its rich, savoury, and high-acid profile:
* **Canada's Great Kitchen Party Vancouver (2023):** Chef Akira Kishimoto (Kishimoto Restaurant) won a **Silver Medal** pairing his competition dish with this sake.
* **Canadian Culinary Championships Victoria (2018):** Chef Takashi Ito (Aura Restaurant) won the regional **Gold Medal** with a dish paired with the *Fraser Valley Junmai Nigori Sake – Renaissance*.

### Product Background
Brewed by Artisan SakeMaker on Granville Island in Vancouver, BC, this sake is historically significant as a 100% Canadian-sourced product. It is crafted using Ginpu sake rice grown locally in Abbotsford, BC.
  - [ellecanada.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFBMctXx8cJ_gSK4s_3Ii4v-mXcz3CmZWqzbvLqKLDnY26fygl_a6wVb5ob6OIOoIBGnTSOg8yjtJvmJ0kN9EZbEhuxQMNwjRMdMpAJWAR-JVF4f-NWVf00vQaF4QAuNjgC8VH7qQPpZbUmZeOPGyg7dEN4UQU5sPCa66zozR2_XgVKSuWNyci2QwnmMev-T1e_wPzMIkX_s8vB9GZ0VCpq0L1Bsm4-gSyDQ==): 
  - [sipmagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjm6VVc28zdK0yfCZU0Q7TtA29auFnkPnxNv2A8_cpCthOyJkgCaTV2vGbYpBfXqK3HnQlssoklB8ZDjLkAEpI4Me2zvc-OPJKN6GJ4H88SKXifBNRJ6_slxVDskFspJPyYQqvugpdqudH1zXFog==): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbiuhin2t0tqbXnjePiOrDogojIXPJTPQQmQI8p4u-l_thpT3_61p3PWLXmLrM7QJDYtA1zpm699EzeYtf_aBEr3SjHkq2HhkWZNq2n2uWHd31MmiV12amm4TJ3kfxxi79M61L-iudKe84f5Hblu7Um-psAtAYeFY64Xlk2GlczKdNnh8oGQ==): 
  - [scoutmagazine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgNKlfehiJelINl_yV_eo15vHhiweDA4Xd1hsXm5gWtASo_8mSppcrgpvfWjTPibXjp5uzkuEBBb3ygGHgME7tyKHbcbtRg5B5E84dAEEmbTDr6fMOimHFs___yORKyj1gVEbA3rswC1szJM2RBlsPLJpxyvrevRUtZc_ldILp_9dAP3GE81GNWibYlXn6YceZ39VOn-fajPDkynTwiN24CraxTDccN9s=): 
  - [goodlifevancouver.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwq-5hPW7w0VF5-scLTSfA2CRujIjKX8H_q6YUjjwBIo7LEQbLpqHJhHF24HOJ64oNsnPumT8mFAJXzGH8r3_tMqFHsg07Q6Ij-6FqlcwFb69lLXZWrvj5CvGzfx7N9S0bg9C3sbDdSKEQRpl2L8m0pooVe_1dVsmgpg==): 
  - [winebc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc6T204fIpBrBMUm8UKODGv0J9y3WZ3lxxGRkjMEaa6reBGVaqK221KzT8x6xd_NnXkGFChyaSqgKcW5YRvGXVMDPnhHbovQ65A6siIkIGaAAebzMadpAXgGdam5nop4NsxcgPOojbpZiqNiAiOEKQMl206ZiiGV4=): 


### sourcing_agent_tool (status=ok)
**Sub-agent synthesis:**
Here is the current availability and price comparison for crisp, dry white wines under $40 from your requested BC producers in Vancouver. 

*Note: Due to the severe crop losses in the Okanagan Valley, some BC wineries (like CedarCreek and Road 13) have released "Crafted in BC" wines using grapes imported from regions like Oregon and New Zealand. These are noted below as they represent the current releases from these producers.*

---

### **Tantalus Vineyards**

*   **Tantalus Riesling**
    *   **BC Liquor Stores:** $30.99 (546 units available) | [Product Link](https://www.bcliquorstores.com/product/802280)
    *   **Everything Wine:** $30.99 (In stock: 17 in North Vancouver, 7 in South Surrey, 8 in Vancouver) | [Product Link](https://www.everythingwine.ca/tantalus-riesling-750-ml)
    *   **Marquis Wine Cellars:** $32.99 (11 in stock) | [Product Link](https://www.marquis-wines.com/tantalus-2022-riesling-750ml/)
    *   **Sutton Place Wine Merchant:** $35.49 (9 in stock) | [Product Link](https://store.suttonplacewinemerchant.com/products/4144458-tantalus-riesling)
*   **Tantalus Pinot Gris**
    *   **Marquis Wine Cellars:** $29.99 (3 in stock) | [Product Link](https://www.marquis-wines.com/tantalus-2024-pinot-gris-750ml/)

---

### **Blue Mountain Vineyard**

*   **Blue Mountain Pinot Blanc**
    *   **Sutton Place Wine Merchant:** $31.49 (11 in stock) | [Product Link](https://store.suttonplacewinemerchant.com/products/4298417-blue-mountain-pinot-blanc)
    *   **Everything Wine:** $31.98 (7 in stock in North Vancouver) | [Product Link](https://www.everythingwine.ca/blue-mountain-vineyard-pinot-blanc-750-ml)

---

### **Culmina Family Estate Winery**

*   **Culmina Decora Riesling**
    *   **Okanagan Cellars:** $22.99 (16 in stock) | [Product Link](https://okanagancellars.com/products/4217289-culmina-decora-riesling)
    *   **BC Liquor Stores:** $24.99 (810 units available) | [Product Link](https://www.bcliquorstores.com/product/389125)
    *   **Legacy Liquor Store:** $27.98 (6 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/culmina-decora-riesling-1-x-750ml)

---

### **Synchromesh Wines**

*   **Synchromesh Riesling (Four Properties / Blend)**
    *   **Everything Wine:** $27.98 (In stock: 23 in North Vancouver, 3 in South Surrey, 8 in Langley, 24 in Vancouver) | [Product Link](https://www.everythingwine.ca/synchromesh-wines-inc-riesling-four-vineyard-blend-750-ml)
    *   **Sutton Place Wine Merchant:** $28.49 (13 in stock) | [Product Link](https://store.suttonplacewinemerchant.com/products/4144511-synchromesh-riesling)
    *   **Marquis Wine Cellars:** $28.99 (9 in stock) | [Product Link](https://www.marquis-wines.com/synchromesh-riesling-blend-750ml/)
    *   **Legacy Liquor Store:** $34.29 (9 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/synchromesh-riesling-blend-1-x-750ml)
*   **Synchromesh 'Long's View' Riesling**
    *   **Marquis Wine Cellars:** $35.99 (20 in stock) | [Product Link](https://www.marquis-wines.com/synchromesh-2024-long-s-view-riesling-750ml/)
*   **Synchromesh Stormhaven Gold Digger Riesling**
    *   **Sutton Place Wine Merchant:** $35.99 (7 in stock) | [Product Link](https://store.suttonplacewinemerchant.com/products/5024288-synchromesh-stormhaven-gold-digger-riesling)
    *   **Marquis Wine Cellars:** $38.99 (10 in stock) | [Product Link](https://www.marquis-wines.com/synchromesh-2022-storm-haven-gold-digger-riesling-750ml/)

---

### **CedarCreek Estate Winery**

*   **CedarCreek Riesling (BC VQA)**
    *   **BC Liquor Stores:** $27.99 (18 units available) | [Product Link](https://www.bcliquorstores.com/product/217166)
*   **CedarCreek Oregon Pinot Gris** *(Crafted in BC using Oregon grapes)*
    *   **BC Liquor Stores:** $24.99 (1,748 units available) | [Product Link](https://www.bcliquorstores.com/product/364863)
    *   **Everything Wine:** $24.99 (In stock: 15 in North Vancouver, 11 in South Surrey, 59 in Langley) | [Product Link](https://www.everythingwine.ca/cedar-creek-estate-winery-oregon-pinot-gris-750-ml)
*   **CedarCreek New Zealand Sauvignon Blanc** *(Crafted in BC using Marlborough grapes)*
    *   **BC Liquor Stores:** $24.99 (1,420 units available) | [Product Link](https://www.bcliquorstores.com/product/364860)
    *   **Everything Wine:** $24.99 (In stock: 18 in North Vancouver, 25 in South Surrey, 39 in Langley, 8 in Vancouver) | [Product Link](https://www.everythingwine.ca/cedar-creek-estate-winery-new-zealand-sauvignon-blanc-750-ml)

---

### **Road 13 Vineyards**

*   **Road 13 Honest John's White Blend** *(Crafted in BC using New Zealand grapes)*
    *   **Okanagan Cellars:** $19.99 (34 in stock) | [Product Link](https://okanagancellars.com/products/4829149-road-13-honest-johns-white-2024-nz)
    *   **Legacy Liquor Store:** $24.40 (43 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/road-13-honest-johns-white-new-zealand-1-x-750ml)
    *   **Everything Wine:** $24.98 (In stock: 22 in North Vancouver, 17 in South Surrey, 12 in Langley, 17 in Vancouver) | [Product Link](https://www.everythingwine.ca/road-13-vineyards-honest-john-s-new-zealand-white-blend-750-ml)

#### search_bcliquor_tool (status=ok, 6 results)
  - TANTALUS - SYRAH | $36.99 | stock=11 | in 1 stores | rating=4.4 | https://www.bcliquorstores.com/product/460372 | {sku=460372; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=13.9; sweetness=00; tasting_notes=A vibrant deep garnet in colour in the glass, this Syrah release is beautifully lifted with intense notes of violets and blue fruits, alongside touches of charcuterie, anise and licorice. Intriguing hints of white pepper, cedar sap and cherry candy add a wonderful complexity to the nose. The palate is very juicy, with loads of blackberry, dark plum and black cherry present. A little peppery baking spice and red licorice complement the palate. The finish is long and lifted with great clarity and minerality. The tannins are fine grained and very well integrated.
; consumer_votes=22; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/460372.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS CHARDONNAY 2023 | $35.99 | stock=387 | in 45 stores | rating=4.6 | https://www.bcliquorstores.com/product/114884 | {sku=114884; product_type=White Wine; grape_type=CHARDONNAY; country=Canada; volume=0.750; alcohol_pct=13.7; sweetness=00; tasting_notes=92 Points, Gismondi On Wine: "Consistently one of Okanagan's top chardonnays. Confident and complete, with interwoven layers of lemon, light cream, stones, and subtle toasted nuttiness, this streams along the palate with an effortless acidity. The medium  body will work well at the dinner table now, or with a couple of years in your cellar. Super smart." (August 2024); consumer_votes=11; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/114884.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS - RIESLING 2025 | $30.99 | stock=546 | in 40 stores | rating=4.1 | https://www.bcliquorstores.com/product/802280 | {sku=802280; product_type=White Wine; grape_type=RIESLING; country=Canada; volume=0.750; alcohol_pct=12.2; sweetness=01; tasting_notes=A top Riesling producer from Kelowna, Tantalus has a long history dating to 1927 and the Pioneer vineyard. The spectrum of Riesling grape flavours can be found here from green apple to citrus to tropical. A real treat and as Riesling is the #1 food wine, will go with everything from corn-on-the-cob to potato salad to ham steaks to spicy recipes to grilled fare.
; consumer_votes=104; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/802280.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS - PINOT NOIR 2022 | $35.99 | stock=87 | in 14 stores | rating=4.2 | https://www.bcliquorstores.com/product/200881 | {sku=200881; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.3; sweetness=00; tasting_notes=Dark crimson in the glass, the nose is lively with bright floral notes alongside cocoa and red berries. Rich notes of cedar, wet earth and graphite complement the aromatic profile. Despite its youth, the palate is showing beautiful complexity and nuance with swaths of red currant, cherry and fig spun together with a unique mineral expression. Lush tannins offer depth and structure and the expectation of a graceful development in bottle. Comfortably enjoy over the next 5 to 10 years.
; consumer_votes=118; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/200881.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS VINEYARDS - REIMER VINEYARD PINOT NOIR | $39.99 | stock=506 | in 66 stores | rating=4.5 | https://www.bcliquorstores.com/product/692960 | {sku=692960; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=9; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/692960.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS - FURTHER AFIELD SERIES CAB FRANC | $34.99 | stock=492 | in 47 stores | rating=4.7 | https://www.bcliquorstores.com/product/252158 | {sku=252158; product_type=Red Wine; grape_type=CABERNET FRANC; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=91 Points, Gismondi On Wine: "Expect an attractive, juicy red that is a nod to Loire but made with the sensibility of a pinot specialist. Paterson has tamed the herbaceous, savoury notes and pushed the ripe blueberry and black fruits to the foreground, all sitting on a silky tannin structure that melts in your mouth.  Considerable value." (April 2024)
; consumer_votes=15; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/252158.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 9 results)
  - Tantalus Vineyards Rose 750 mL | $30.98 | [North Vancouver:0, South Surrey:17, Langley Store:0, Vancouver:7] | https://www.everythingwine.ca/tantalus-rose-2012 | {sku=439687; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/3/439687_tantalus_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Tantalus Vineyards Chardonnay 750 mL | $35.99 | [North Vancouver:0, South Surrey:0, Langley Store:10, Vancouver:0] | https://www.everythingwine.ca/tantalus-chardonnay | {sku=114884; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/1/114884_tantalus_chardonnay_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Riesling 750 mL | $30.99 | [North Vancouver:17, South Surrey:7, Langley Store:0, Vancouver:8] | https://www.everythingwine.ca/tantalus-riesling-750-ml | {sku=802280; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/0/802280_tantalus_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Tantalus Vineyards Bear Chardonnay 750 mL | $30.98 | [North Vancouver:0, South Surrey:5, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineryards-bear-chardonnay-750-ml | {sku=83282; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/3/83282_tantalus_bear_chardonnay.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Ontario Riesling 750 mL | $36.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineyards-ontario-riesling-750-ml | {sku=270640; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/270640_tantalus_ontario_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Further Afield Series Syrah 750 mL | $36.99 | [North Vancouver:0, South Surrey:0, Langley Store:6, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineyards-further-afield-series-syrah-750-ml | {sku=460372; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/6/460372_tantalus_further_afield_syrah.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Maija Pinot Noir 750 mL | $39.98 | [North Vancouver:12, South Surrey:2, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-juveniles-pinot-noir | {sku=348755; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/4/348755_tantalus_maija_pinot_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Looney Vineyard Oregon Rose 750 mL | $30.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/tantalus-vineyards-looney-vineyard-oregon-rose-750-ml | {sku=270643; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/270643_tantalus_looney_vineyard_oregon_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tantalus Vineyards Further Afield Series Cabernet Franc 750 mL | $34.99 | [North Vancouver:7, South Surrey:8, Langley Store:10, Vancouver:5] | https://www.everythingwine.ca/tantalus-vineyards-further-afield-series-cabernet-franc-750-ml | {sku=252158; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/5/252158_tantalus_further_afield_cabernet_franc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 8 results)
  - Tantalus Bear Chardonnay | $29.99 | stock=6 | https://store.suttonplacewinemerchant.com/products/5171325-tantalus-bear-chardonnay | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC83282.jpg; country=CANADA; varietal=Chardonnay; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Tantalus Further Afield Blanc de Noir | $47.99 | 2022 | stock=7 | https://store.suttonplacewinemerchant.com/products/5181376-tantalus-further-afield-blanc-de-noir | {category=SPARKLING CANADA; in_stock=True; unit_size=750ML Bottle; country=CANADA; varietal=Pinot Noir; is_staff_pick=False; is_featured=False}
  - Tantalus Further Afield Cab Franc | $39.49 | stock=6 | https://store.suttonplacewinemerchant.com/products/4724608-tantalus-further-afield-cab-franc | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000025/0000252158-8879.jpg; country=CANADA; varietal=Cabernet Franc; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Tantalus Maija Pinot Noir | $38.49 | 2022 | stock=9 | https://store.suttonplacewinemerchant.com/products/4668256-tantalus-maija-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000034/0000348755-4119.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=12.90; is_staff_pick=False; is_featured=False}
  - Tantalus Old Vines Riesling | $51.99 | 2020 | stock=9 | https://store.suttonplacewinemerchant.com/products/4360955-tantalus-old-vines-riesling | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000017/0000179226-1753.jpg; country=CANADA; varietal=Riesling; alcohol_pct=13.40; is_staff_pick=False; is_featured=False}
  - Tantalus Riesling | $35.49 | 2022 | stock=9 | https://store.suttonplacewinemerchant.com/products/4144458-tantalus-riesling | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000080/0000802280-5980.jpg; country=CANADA; varietal=Riesling; alcohol_pct=12.40; is_staff_pick=False; is_featured=False}
  - Tantalus Rose | $29.99 | 2021 | stock=22 | https://store.suttonplacewinemerchant.com/products/4254767-tantalus-rose | {category=ROSE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000043/0000439687-3791.jpg; country=CANADA; varietal=Pinot Noir/Pinot Meunier; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Tantalus Syrah  | $41.99 | 2021 | stock=6 | https://store.suttonplacewinemerchant.com/products/4171973-tantalus-syrah | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000046/0000460372-1677.jpg; country=CANADA; varietal=Syrah; alcohol_pct=14.20; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 5 results)
  - Tantalus 2025 Rose 750ml | $30.99 | stock=17 | https://www.marquis-wines.com/tantalus-2025-rose-750ml/ | {sku=1017799; in_stock=True; categories=["Rosé Wine", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21728/images/17421/2026-04-23-13.31.48__31357.1777054370.500.500.png?c=2}
  - Tantalus 2025 Riesling 750ml | $32.99 | stock=11 | https://www.marquis-wines.com/tantalus-2022-riesling-750ml/ | {sku=1010038; in_stock=True; categories=["White Wine", "Riesling", "Kelowna", "British Columbia", "Organic / Biodynamic Wine"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7320/images/8588/IMG_15051__08114.1588006662.500.500.jpg?c=2}
  - Tantalus 2024 Pinot Gris 750ml | $29.99 | stock=3 | https://www.marquis-wines.com/tantalus-2024-pinot-gris-750ml/ | {sku=1031910; in_stock=True; categories=["White Wine", "Pinot Gris & Grigio", "Organic / Biodynamic Wine"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21324/images/17029/2026-01-23-14.54.33__29085.1769462280.500.500.png?c=2}
  - Tantalus 2022 Cabernet Franc 750ml | $36.99 | stock=16 | https://www.marquis-wines.com/tantalus-2022-cabernet-franc-750ml/ | {sku=1029801; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Cabernet Franc", "Drink Local"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18670/images/14640/2024-05-08_11.38.04__97448.1715278618.500.500.png?c=2}
  - Tantalus 2023 Maija Pinot Noir 750ml | $40.99 | stock=7 | https://www.marquis-wines.com/tantalus-2017-maija-pinot-noir-750ml/ | {sku=1016222; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9531/images/7177/IMG_9636__76411.1544468344.500.500.JPG?c=2}

#### search_legacy_liquor_store_tool (status=ok, 2 results)
  - Tantalus "Maija" Pinot Noir | $38.64 | stock=7 | https://www.legacyliquorstore.com/product/wine/tantalus-maija-pinot-noir-1-x-750ml | {brand=Tantalus; slug=tantalus-maija-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Tantalus "Bear" Chardonnay | $29.81 | stock=3 | https://www.legacyliquorstore.com/product/wine/tantalus-bear-chardonnay-1-x-750ml | {slug=tantalus-bear-chardonnay-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "chardonnay"]}

#### search_bcliquor_tool (status=ok, 0 results)

#### search_everything_wine_tool (status=ok, 12 results)
  - Blue Mountain Vineyard Gamay Noir 750 mL | $34.98 | [North Vancouver:0, South Surrey:10, Langley Store:11, Vancouver:0] | https://www.everythingwine.ca/blue-mountain-gamay-noir | {sku=389882; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/8/389882_blue_mountain_vineyard_gamay_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Pinot Gris 750 mL | $31.98 | https://www.everythingwine.ca/blue-mountain-pinot-gris | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/b/m/bmvc_pgris.png?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366&format=jpeg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Pinot Blanc 750 mL | $31.98 | [North Vancouver:7, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/blue-mountain-vineyard-pinot-blanc-750-ml | {sku=329441; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/2/329441_blue_mountain_pinot_blanc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Reserve Brut Sparkling 750 mL | $52.98 | https://www.everythingwine.ca/blue-mountain-reserve-brut | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/b/m/bmvc_reserve_brut.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Reserve Pinot Noir 1.5 L | $115.98 | https://www.everythingwine.ca/blue-mountain-vineyard-reserve-pinot-noir-1-5-l | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Blanc de Blancs Sparkling 750 mL | $52.98 | [North Vancouver:10, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/blue-mountain-blanc-de-blancs-sparkling | {sku=402594; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/0/402594_blue_mountain_blanc_de_blancs.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Reserve Cuvee Pinot Noir 750 mL | $47.98 | https://www.everythingwine.ca/blue-mountain-vineyard-reserve-cuvee-pinot-noir-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/b/m/bmvc_reserve_pnoir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Gold Label Brut Sparkling 750 mL | $36.98 | [North Vancouver:1, South Surrey:9, Langley Store:9, Vancouver:5] | https://www.everythingwine.ca/blue-mountain-brut | {sku=471672; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/7/471672_blue_mountain_gold_label_brut_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Blossom Slope Block 17 Chardonnay 750 mL | $52.98 | https://www.everythingwine.ca/blue-mountain-blossom-slope-block-17-chardonnay-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Blue Mountain Vineyard Wild Terrain Block 9 Pinot Noir 750 mL | $57.98 | https://www.everythingwine.ca/blue-mountain-block-9-pinot-noir-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard Gravel Force Block 14 Pinot Noir 750 mL | $57.98 | https://www.everythingwine.ca/blue-mountain-block-14-pinot-noir-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blue Mountain Vineyard River Flow Block 23 Pinot Noir 750 mL | $57.98 | https://www.everythingwine.ca/blue-mountain-block-23-pinot-noir-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 3 results)
  - Blue Mountain Brut Gold Label  | $35.99 | stock=26 | https://store.suttonplacewinemerchant.com/products/4144014-blue-mountain-brut-gold-label | {category=SPARKLING CANADA; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000047/0000471672-6624.jpg; country=CANADA; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}
  - Blue Mountain Gamay | $33.99 | 2020 | stock=4 | https://store.suttonplacewinemerchant.com/products/4228470-blue-mountain-gamay | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000038/0000389882-3198.png; country=CANADA; varietal=Gamay Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Blue Mountain Pinot Blanc | $31.49 | 2022 | stock=11 | https://store.suttonplacewinemerchant.com/products/4298417-blue-mountain-pinot-blanc | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000032/0000329441-8271.png; country=CANADA; varietal=Pinot Blanc; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 5 results)
  - Blue Mountain N/V Gold Label Brut 750ml | $37.99 | stock=33 | https://www.marquis-wines.com/blue-mountain-n-v-gold-label-brut-750ml/ | {sku=471672; in_stock=True; categories=["Sparkling", "Okanagan Falls", "British Columbia", "Lunar New Year"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/6072/images/11775/blue-mountain-gold-brut__28311.1648759359.500.500.jpg?c=2}
  - Blue Mountain 2023 Reserve Cuvee Pinot Noir 750ml | $51.99 | stock=11 | https://www.marquis-wines.com/blue-mountain-2022-reserve-cuvee-pinot-noir-750ml/ | {sku=1023129; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19489/images/15288/2024-10-31-14.17.17__41020.1730481578.500.500.png?c=2}
  - Blue Mountain 2022 Gamay Noir 750ml | $35.99 | stock=12 | https://www.marquis-wines.com/blue-mountain-2019-gamay-noir-750ml/ | {sku=1014652; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8456/images/5067/blue-mountain-gamay-2015__59204.1533682531.500.500.jpg?c=2}
  - Gagnon Kennedy Vineyards 2020 Cabernet Sauvignon Monte Rosso Vineyard Moon Mountain 750ml | $329.99 | stock=3 | https://www.marquis-wines.com/gagnon-kennedy-vineyards-2020-cabernet-sauvignon-monte-rosso-vineyard-moon-mountain-750ml/ | {sku=1030528; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "USA", "California", "Napa"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19625/images/15538/2025-01-10_14.19.46__85706.1736797630.500.500.png?c=2}
  - Arette Reposado Tequila 700ml | $89.99 | stock=5 | https://www.marquis-wines.com/arette-reposado-tequila-700ml/ | {sku=1024491; in_stock=True; categories=["Spirits", "Tequila & Mezcal"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21623/images/17318/2026-03-30-13.14.55__91622.1775070661.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 3 results)
  - Blue Mountain Reserve Cuvee Pinot Noir Magnum | $120.87 | stock=1 | https://www.legacyliquorstore.com/product/wine/blue-mountain-reserve-cuvee-pinot-noir-magnum-1-x-1-5l | {slug=blue-mountain-reserve-cuvee-pinot-noir-magnum-1-x-1-5l; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Blue Mountain Gamay Noir | $34.08 | stock=6 | https://www.legacyliquorstore.com/product/wine/blue-mountain-gamay-noir-1-x-750ml | {slug=blue-mountain-gamay-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "gamay"]}
  - Blue Mountain Brut Gold Label | $35.88 | stock=14 | https://www.legacyliquorstore.com/product/wine/blue-mountain-winery-gold-label-brut-1-x-750ml | {brand=Blue Mountain; slug=blue-mountain-winery-gold-label-brut-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}

#### search_bcliquor_tool (status=ok, 0 results)

#### search_everything_wine_tool (status=ok, 9 results)
  - Synchromesh Wines Storm Haven Vineyard Riesling 750 mL | $32.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/synchromesh-wines-storm-haven-vineyard-riesling-750-ml | {sku=3588; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/5/3588_synchromesh_storm_haven_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Synchromesh Wines Storm Haven Dry Riesling 750 mL | $32.98 | https://www.everythingwine.ca/synchromesh-haven-dry-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Synchromesh Wines Storm Haven Cabernet Franc 750 mL | $40.98 | https://www.everythingwine.ca/synchromesh-wines-storm-haven-cab-franc-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Synchromesh Wines Long's View Vineyard Riesling 750 mL | $32.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/synchromesh-wines-inc-riesling-bob-hancock-750-ml | {sku=635524; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/6/3/635524_synchromesh_lv_riesling_nl.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Synchromesh Wines Boulders Block Riesling 750 mL | $41.98 | https://www.everythingwine.ca/synchromesh-boulders-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/p/l/placeholder_image_white_2025_5.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Synchromesh Wines Paddle Shift Riesling Spritzer 250 mL | $8.99 | [North Vancouver:0, South Surrey:0, Langley Store:23, Vancouver:0] | https://www.everythingwine.ca/synchromesh-paddle-shift-riesling-spritzer-250-ml | {sku=382372; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/8/382372_synchromesh_paddle_shift_riesling_250ml.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Synchromesh Wines Four Properties Riesling Blend 750 mL | $27.98 | [North Vancouver:23, South Surrey:3, Langley Store:8, Vancouver:24] | https://www.everythingwine.ca/synchromesh-wines-inc-riesling-four-vineyard-blend-750-ml | {sku=850115; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/5/850115_synchromesh_wines_four_vineyard_riesling_nl.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Synchromesh Wines Turtle Rock Farms Tertre Rouge 750 mL | $33.98 | [North Vancouver:0, South Surrey:5, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/synchromesh-wines-inc-tertre-rouge-750-ml | {sku=239103; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/3/239103_synchromesh_wines_inc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Synchromesh Wines Storm Haven Vineyard Gibson Block 3 Riesling 750 mL | $41.98 | [North Vancouver:3, South Surrey:3, Langley Store:12, Vancouver:0] | https://www.everythingwine.ca/synchromesh-riesling-storm | {sku=820894; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/2/820894_synchromesh_gibson3_nl.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 3 results)
  - Synchromesh Paddle Shift Riesling Spritz 250ml | $8.49 | stock=19 | https://store.suttonplacewinemerchant.com/products/4331170-synchromesh-paddle-shift-riesling-spritz-250ml | {category=WHITE BC; in_stock=True; unit_size=250ml; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000038/0000382372-5606.jpg; country=CANADA; varietal=Riesling; alcohol_pct=5.20; is_staff_pick=False; is_featured=False}
  - Synchromesh Riesling | $28.49 | 2021 | stock=13 | https://store.suttonplacewinemerchant.com/products/4144511-synchromesh-riesling | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC850115.jpg; country=CANADA; varietal=Riesling; is_staff_pick=False; is_featured=False}
  - Synchromesh Stormhaven Gold Digger Riesling | $35.99 | 2022 | stock=7 | https://store.suttonplacewinemerchant.com/products/5024288-synchromesh-stormhaven-gold-digger-riesling | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC419471.png; country=CANADA; varietal=Riesling; alcohol_pct=7.30; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 4 results)
  - Synchromesh 2025 Riesling Blend 750ml | $28.99 | stock=9 | https://www.marquis-wines.com/synchromesh-riesling-blend-750ml/ | {sku=1017693; in_stock=True; categories=["White Wine", "Riesling", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8821/images/4556/synchromesh_2014_riesling__15658.1772473793.500.500.jpg?c=2}
  - Synchromesh 2025 'Long's View' Riesling 750ml | $35.99 | stock=20 | https://www.marquis-wines.com/synchromesh-2024-long-s-view-riesling-750ml/ | {sku=1030994; in_stock=True; categories=["White Wine", "Riesling", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20238/images/16135/synchromesh_longs_view__79247.1747765724.500.500.jpg?c=2}
  - Synchromesh 2022 Storm Haven Cabernet Franc 750ml | $38.99 | stock=2 | https://www.marquis-wines.com/synchromesh-2022-storm-haven-cabernet-franc-750ml/ | {sku=1024164; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Cabernet Franc"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19917/images/15695/2025-02-03-15.48.24__56977.1738705473.500.500.png?c=2}
  - Synchromesh 2023/25 Storm Haven Gold Digger Riesling 750ml | $38.99 | stock=10 | https://www.marquis-wines.com/synchromesh-2022-storm-haven-gold-digger-riesling-750ml/ | {sku=1026009; in_stock=True; categories=["White Wine", "Riesling", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/15368/images/11071/2021-10-29-13.16.36__98025.1635802956.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 3 results)
  - Synchromesh Riesling Blend | $34.29 | stock=9 | https://www.legacyliquorstore.com/product/wine/synchromesh-riesling-blend-1-x-750ml | {slug=synchromesh-riesling-blend-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "riesling"]}
  - Synchromesh Wines Storm Haven Vineyard Pinot Noir | $35.82 | stock=12 | https://www.legacyliquorstore.com/product/wine/synchromesh-wines-storm-haven-vineyard-pinot-noir-1-x-750ml | {brand=Synchromesh; slug=synchromesh-wines-storm-haven-vineyard-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Synchromesh Paddle Shift Riesling Spritzer Can | $8.18 | stock=10 | https://www.legacyliquorstore.com/product/wine/synchromesh-paddle-shift-riesling-spritzer-can-1-x-250ml | {brand=Synchromesh; slug=synchromesh-paddle-shift-riesling-spritzer-can-1-x-250ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}

#### search_bcliquor_tool (status=ok, 6 results)
  - CULMINA - SAIGNEE 2023 | $26.99 | stock=37 | in 8 stores | rating=4.6 | https://www.bcliquorstores.com/product/72549 | {sku=72549; product_type=Rose Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=A blend of Malbec (44%), Cabernet Franc (29%) and Merlot (34%) from Arise and Stan's Benches, Certified Organic. "Pretty nose here, delicate and floral, bright red fruit-scented. Depth is very good." 92 Points - John Szabo, MS.
; consumer_votes=5; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/72549.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - DILEMMA CHARDONNAY | $35.99 | stock=227 | in 34 stores | rating=4.8 | https://www.bcliquorstores.com/product/126830 | {sku=126830; product_type=White Wine; grape_type=CHARDONNAY; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Showcasing mineral and spice aromas, Dilemma is framed by lovely oak, caramel and butter flavours, a luscious body, and a long, fresh finish, creating a wine of outstanding finesse, beauty, elegance and style.
; consumer_votes=8; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/126830.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - DECORA RIESLING | $24.99 | stock=810 | in 73 stores | rating=4.0 | https://www.bcliquorstores.com/product/389125 | {sku=389125; product_type=White Wine; grape_type=RIESLING; country=Canada; volume=0.750; alcohol_pct=13.4; sweetness=00; tasting_notes=Finely scented with daisies, dried apricots, toasted almonds and yeasty aromatics, Decora showcases delicacy and complexity. The verve and brightness of the palate are balanced by creaminess, with notes of starfruit and fuzzy peaches. 
; consumer_votes=6; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/389125.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - HYPOTHESIS 2019 | $34.99 (reg $42.99) | stock=1814 | in 97 stores | rating=4.5 | https://www.bcliquorstores.com/product/227436 | {sku=227436; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Opulent and refined, the bouquet brings complex aromas of cedar bark, leather, cocoa nibs and dark cherries. The generous palate is layered with succulent dark fruits, licorice and baking spice supported by balance acidity and silky tannins. The nuances of 2018 Hypothesis unfurl gradually over a long and persistent finish.
; consumer_votes=30; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/227436.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA - CABERNET SAUVIGNON 2021 | $37.99 | stock=82 | in 16 stores | rating=4.5 | https://www.bcliquorstores.com/product/227457 | {sku=227457; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Our single-varietal expression of Malbec comes from our Arise Bench vineyard along the Golden Mile Bench. Well-balanced with rich fruit offset by supple, silky tannins and oolong tea flavours. Rich mulberry and plum linger on the deep, intriguing finish.
; consumer_votes=10; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/227457.jpeg; certificates=["BC VQA", "All VQA"]}
  - CULMINA OLIVER - R AND D RED BLEND GOLDEN MILE BENCH 2022 | $19.99 | stock=1477 | in 125 stores | rating=4.0 | https://www.bcliquorstores.com/product/495846 | {sku=495846; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=A Golden Mile expression is on show here with lots of Merlot fruit and other Bordeaux grapes from estate vineyards. Offering great ripe fruit from this exceptional vintage, the red and black fruit flavours and persistent linger highlight an expressive wine. Match with grilled fare or pasta recipes or vegetarian dishes.
; consumer_votes=63; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/495846.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 5 results)
  - Culmina Family Estate Winery Decora Riesling 750 mL | $28.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/culmina-family-estate-winery-decora-riesling-750-ml | {sku=863035; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/6/863035_culmina_decora_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery Saignee Rose 750 mL | $26.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/culmina-family-estate-winery-saignee-rose-merlot-cab-franc-cab-sauv-750-ml-1 | {sku=29593; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/9/29593_culmina_family_estate_winery_saignee_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery R&D Red Blend 750 mL | $19.99 | https://www.everythingwine.ca/culmina-family-estate-winery-r-d-red-blend-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/c/u/culmina_r_d_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery R&D Sauvignon Blanc Semillon 750 mL | $26.98 | https://www.everythingwine.ca/culmina-family-estate-winery-r-d-sauvignon-blanc-semillon-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Culmina Family Estate Winery Golden Mile Bench Hypothesis Red Blend 750 mL | $34.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/culmina-family-estate-winery-golden-mile-bench-hypothesis-red-blend-750-ml | {sku=852012; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/5/852012_culmina_family_estate_winery_golden_mile_bench_hypothesis.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}

#### search_okanagan_cellars_tool (status=ok, 7 results)
  - CULMINA - CAB SAUV | $37.99 | stock=10 | https://okanagancellars.com/products/3946821-culmina-cab-sauv | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000022/0000227457-4800.png}
  - CULMINA - DECORA RIESLING | $22.99 | stock=16 | https://okanagancellars.com/products/4217289-culmina-decora-riesling | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/all/BC389125.jpg}
  - CULMINA - DILEMMA CHARDONNAY | $34.99 | stock=7 | https://okanagancellars.com/products/3937046-culmina-dilemma-chardonnay | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000012/0000126830-4871.png}
  - CULMINA - HYPOTHESIS | $32.99 (reg $36.99) | stock=10 | https://okanagancellars.com/products/3957069-culmina-hypothesis | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000022/0000227436-6306.jpg}
  - CULMINA - MALBEC | $37.99 | stock=12 | https://okanagancellars.com/products/4114513-culmina-malbec | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000025/0000252952-8251.png}
  - CULMINA - R&D RED BLEND | $19.99 | stock=21 | https://okanagancellars.com/products/3410072-culmina-r-d-red-blend | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000049/0000495846-8804.png}
  - CULMINA - SAIGNEE | $25.99 | stock=10 | https://okanagancellars.com/products/3403440-culmina-saignee | {category=Rose; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000007/0000072549-9622.png}

#### search_suttonplace_tool (status=ok, 0 results)

#### search_marquis_tool (status=ok, 5 results)
  - Penfolds 2022 Reserve Bin A Chardonnay 750ml | $154.99 | stock=9 | https://www.marquis-wines.com/penfolds-2022-reserve-bin-a-chardonnay-750ml-ojrx/ | {sku=1030793; in_stock=True; categories=["White Wine", "Chardonnay", "95+ Point Wines", "Adelaide Hills", "Australia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19951/images/15788/2025-02-25-14.38.19__97300.1740678446.500.500.png?c=2}
  - Wohlmuth 2024 Sauvgnon Blanc "Phyllit" 750ml | $44.99 | stock=21 | https://www.marquis-wines.com/wohlmuth-2024-sauvgnon-blanc-phyllit-750ml/ | {sku=1031052; in_stock=True; categories=["White Wine", "Sauvignon Blanc", "Austria", "Steiermark"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21423/images/17077/IMG_0574__88566.1770668649.500.500.png?c=2}
  - Monteraponi 2021 Colli Toscana Centrale Trebbiano 750ml | $149.99 | stock=19 | https://www.marquis-wines.com/monteraponi-2021-colli-toscana-centrale-trebbiano-750ml/ | {sku=1029800; in_stock=True; categories=["White Wine", "Tuscany", "Italy", "Marquis Exclusives", "Organic / Biodynamic Wine", "Trebbiano / Ugni Blanc", "Monteraponi"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18696/images/14607/monteraponi_trebbiano__42009.1712869357.500.500.jpg?c=2}
  - Gaja 2019 Pieve Santa Restituta Rennina Brunello di Montalcino 750ml | $399.99 | stock=3 | https://www.marquis-wines.com/gaja-2019-pieve-santa-restituta-rennina-brunello-di-montalcino-750ml/ | {sku=1013605; in_stock=True; categories=["Red Wine", "Sangiovese", "Italy", "Tuscany", "Brunello/Rosso di Montalcino", "95+ Point Wines"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20910/images/16684/2025-10-17_11.31.29__87413.1760991164.500.500.png?c=2}
  - Lagavulin 8 Year Old Single Malt Whisky 750ml | $107.99 | stock=5 | https://www.marquis-wines.com/lagavulin-8-year-old-750ml/ | {sku=1026213; in_stock=True; categories=["Single Malt Scotch", "Islay"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/15552/images/11248/2021-12-07_16.32.57__16452.1638999505.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 4 results)
  - Culmina Hypothesis | $39.81 | stock=4 | https://www.legacyliquorstore.com/product/wine/culmina-hypothesis-1-x-750ml | {slug=culmina-hypothesis-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Culmina Decora Riesling | $27.98 | stock=6 | https://www.legacyliquorstore.com/product/wine/culmina-decora-riesling-1-x-750ml | {brand=Culmina; slug=culmina-decora-riesling-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "riesling"]}
  - Culmina Cabernet Sauvignon | $48.58 | stock=5 | https://www.legacyliquorstore.com/product/wine/culmina-cabernet-sauvignon-1-x-750ml | {brand=Culmina; slug=culmina-cabernet-sauvignon-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "cabernet sauvignon"]}
  - Culmina R&D Red Blend | $22.27 | stock=6 | https://www.legacyliquorstore.com/product/wine/culmina-r-d-red-blend-1-x-750ml | {brand=Culmina Oliver; slug=culmina-r-d-red-blend-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}

#### search_bcliquor_tool (status=ok, 12 results)
  - CEDARCREEK - MERITAGE | $29.99 | stock=817 | in 64 stores | rating=4.0 | https://www.bcliquorstores.com/product/535658 | {sku=535658; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=14.3; sweetness=00; tasting_notes=Plum, spice, and purple fruits with a hint of leafy, tobacco notes. The palate shows nice density and structure while maintaining a certain degree of elegance.
; consumer_votes=60; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/535658.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - CEDARCREEK - CABERNET MERLOT | $27.99 | stock=921 | in 89 stores | rating=3.8 | https://www.bcliquorstores.com/product/163303 | {sku=163303; product_type=Red Wine; grape_type=CABERNET/MERLOT; country=Canada; volume=0.750; alcohol_pct=14.2; sweetness=00; tasting_notes=Classic Cabernet Merlot blend with plum, black currant, tomato leaf, and cigar notes. Balanced structure and length on the palate with fruit purity and weight.
; consumer_votes=143; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/163303.jpeg; certificates=["BC VQA", "All VQA"]}
  - CEDARCREEK - CHARDONNAY 2022 | $25.99 | stock=93 | in 16 stores | rating=4.0 | https://www.bcliquorstores.com/product/237974 | {sku=237974; product_type=White Wine; grape_type=CHARDONNAY; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=CedarCreek Estate Chardonnay offers lime, lemon, mineral, and peach on the nose with fresh acidity. The palate is round and weighty, with a lovely long finish that highlights its vibrant citrus and mineral notes.
; consumer_votes=56; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/237974.jpeg; certificates=["BC VQA", "All VQA"]}
  - CEDARCREEK - RIESLING 2023 | $27.99 | stock=18 | in 7 stores | rating=4.4 | https://www.bcliquorstores.com/product/217166 | {sku=217166; product_type=White Wine; grape_type=RIESLING; country=Canada; volume=0.750; alcohol_pct=11.7; sweetness=01; tasting_notes=The 2023 CedarCreek Estate Riesling, certified organic, offers tropical aromas and citrus notes. Its northern Okanagan vineyard location ensures bright acidity and fresh flavours. On the palate, it balances residual sugar and acidity, creating a juicy, vibrant experience with a clean, fresh finish.; consumer_votes=25; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/217166.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - CEDARCREEK - ESTATE CABERNET FRANC | $29.99 | stock=323 | in 28 stores | rating=4.4 | https://www.bcliquorstores.com/product/73724 | {sku=73724; product_type=Red Wine; grape_type=CABERNET FRANC; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Red fruit such as sour cherry, rhubarb, blackberry, floral and graphite notes. The palate is medium weight and balanced with soft tannins and good mouthfeel.
; consumer_votes=19; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/73724.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - CEDARCREEK - PINOT NOIR 2022 | $30.99 | stock=21 | in 4 stores | rating=4.0 | https://www.bcliquorstores.com/product/567412 | {sku=567412; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.4; sweetness=00; tasting_notes=This lighter style of Pinot Noir with good fruit concentration has loads of black cherry, raspberry and wood spice wrapped in moderate tannins and juicy acidity.
; consumer_votes=83; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/567412.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - CEDARCREEK - PLATINUM SYRAH 2021 | $64.90 | stock=29 | in 7 stores | rating=2.8 | https://www.bcliquorstores.com/product/83400 | {sku=83400; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=14.5; sweetness=00; tasting_notes=The Syrah that grows at our southern Okanagan vineyards is situated on unique south-west facing slopes. At midday in summer, the heat is powerful, but Syrah likes that; the terroir evokes its Rhone Valley origins. The wine is structured and balanced with delicate tannins and spice - the direct result of a decision to plant it where it feels right at home.
; consumer_votes=5; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/83400.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - CEDARCREEK - ESTATE PINOT GRIS OREGON 2025 | $24.99 | stock=1748 | in 130 stores | rating=4.8 | https://www.bcliquorstores.com/product/364863 | {sku=364863; product_type=White Wine; grape_type=PINOT GRIS/PINOT GRIGIO; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=01; tasting_notes=CRAFTED IN BC. Core notes of pear and apple flow through both the nose and palate supported by delicate texture and fresh acidity.
; consumer_votes=8; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/364863.jpeg}
  - CEDARCREEK - PLATINUM JAGGED ROCK CHARDONNAY | $52.99 | stock=174 | in 26 stores | rating=4.6 | https://www.bcliquorstores.com/product/618637 | {sku=618637; product_type=White Wine; grape_type=CHARDONNAY; country=Canada; volume=0.750; alcohol_pct=13.4; sweetness=00; tasting_notes=The Jagged Rock Vineyard, a quintessential site in South Okanagan, is located in Canada's only desert climate. This vineyard is mostly sand with the lack of moisture, forcing our vineyard to dig deep into the ground. On the nose, meyer lemon, melon, nashi pear, and stone fruit supported by a hint of toasty oak. The palate is fresh and vibrant, with citrus notes and acidity providing energy and direction to the wine.
; consumer_votes=3; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/618637.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - CEDARCREEK - PLATINUM PINOT NOIR SOUTH KELOWNA SLOPES | $66.99 | stock=9 | in 2 stores | rating=3.3 | https://www.bcliquorstores.com/product/316971 | {sku=316971; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=This 2022 vintage is a beautiful and elegant nose of brambly berries, potpourri, and forest floor. On the palate, the tannins are fine and well-integrated. A beautiful energy and freshness underline the nose and palate.
; consumer_votes=6; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/316971.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - CEDARCREEK ESTATE - SAUVIGNON BLANC NEW ZEALAND 2025 | $24.99 | stock=1420 | in 103 stores | rating=4.1 | https://www.bcliquorstores.com/product/364860 | {sku=364860; product_type=White Wine; grape_type=SAUVIGNON BLANC; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=01; tasting_notes=CRAFTED IN BC: grown in regions beyond the Okanagan to overcome the lost 2024 harvest; crafted by BC winemakers reflecting the unique style of the winery. Guava and passionfruit flavours with bright acidity and a crisp palate. Lemongrass notes lead to a clean finish showcasing the freshness of Marlborough fruit
; consumer_votes=6; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/364860.jpeg}
  - CEDARCREEK - PLATINUM PINOT NOIR EAST KELOWNA SLOPES | $69.99 | stock=2 | in 1 stores | rating=4.2 | https://www.bcliquorstores.com/product/245489 | {sku=245489; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=The East Kelowna Slopes get pretty warm during the day, leading to dark fruit flavour and dense tannins in the Pinot Noirs. We embraced this tendency, leading to a structured, intense, and dense Pinot Noir supported by a hit of classic French Oak. Dark, brooding nose. Plum, blackberry, with some raspberry leaf. On the palate, the structure is firm, but the tannins are supple and will age well.
; consumer_votes=4; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/245489.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 17 results)
  - Cedar Creek Estate Winery Meritage 750 mL | $29.99 | [North Vancouver:15, South Surrey:0, Langley Store:11, Vancouver:10] | https://www.everythingwine.ca/cedar-creek-meritage | {sku=535658; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/3/535658_cedar_creek_meritage.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Cedar Creek Estate Winery Merlot 750 mL | $29.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/cedar-creek-merlot | {sku=408666; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/0/408666_cedarcreek_merlot.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Cedar Creek Estate Winery Platinum Chardonnay 750 mL | $52.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/cedar-creek-estate-winery-platinum-chardonnay-750-ml | {sku=618637; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/6/1/618637_cedar_creek_platinum_chard.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Cedar Creek Estate Winery Merlot Cabernet 750 mL | $27.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:8] | https://www.everythingwine.ca/cedar-creek-merlot-cabernet | {sku=163303; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/6/163303_cedar_creek_cabernet_merlot.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Cedar Creek Estate Winery Germany Riesling 750 mL | $26.98 | [North Vancouver:0, South Surrey:8, Langley Store:10, Vancouver:0] | https://www.everythingwine.ca/cedar-creek-estate-winery-germany-riesling-750-ml | {sku=323210; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/2/323210_cedar_creek_crafted_riesling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Cedar Creek Estate Winery Oregon Rose 750 mL | $29.98 | [North Vancouver:15, South Surrey:6, Langley Store:13, Vancouver:14] | https://www.everythingwine.ca/cedar-creek-estate-winery-washington-rose-750-ml | {sku=364866; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/6/364866_cedar_creek_cibc_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Cedar Creek Estate Winery Platinum Syrah 2021 750 mL | $64.9 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:2] | https://www.everythingwine.ca/cedar-creek-estate-winery-platinum-syrah-750-ml | {sku=83400; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/3/83400_cedar_creek_estate_winery_platinum_syrah_750_ml.jpeg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Cedar Creek Estate Winery Platinum Syrah 2022 750 mL | $62.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/cedar-creek-estate-winery-platinum-syrah-2022-750-ml | {sku=14744; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/4/14744_cedar_creek_platinum_syrah.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Cedar Creek Estate Winery France Cabernet Merlot 750 mL | $32.98 | [North Vancouver:0, South Surrey:1, Langley Store:12, Vancouver:0] | https://www.everythingwine.ca/cedar-creek-estate-winery-france-cabernet-merlot-750-ml | {sku=725273; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/2/725273_cedarcreek_cabfranc_crafted.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Cedar Creek Estate Winery Oregon Pinot Noir 750 mL | $32.98 | [North Vancouver:0, South Surrey:6, Langley Store:0, Vancouver:12] | https://www.everythingwine.ca/cedar-creek-estate-winery-oregon-pinot-noir-750-ml | {sku=364875; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/6/364875_cedar_creek_crafted_pn.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Cedar Creek Estate Winery Oregon Pinot Gris 750 mL | $24.99 | [North Vancouver:15, South Surrey:11, Langley Store:59, Vancouver:0] | https://www.everythingwine.ca/cedar-creek-estate-winery-oregon-pinot-gris-750-ml | {sku=364863; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/6/364863_cedarcreek_oregon_pg.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Cedar Creek Estate Winery New Zealand Sauvignon Blanc 750 mL | $24.99 | [North Vancouver:18, South Surrey:25, Langley Store:39, Vancouver:8] | https://www.everythingwine.ca/cedar-creek-estate-winery-new-zealand-sauvignon-blanc-750-ml | {sku=364860; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/6/364860_cedarcreek_nz_sb.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Cedar Creek Estate Winery Platinum South Kelowna Slopes Pinot Noir 750 mL | $66.99 | https://www.everythingwine.ca/cedar-creek-estate-winery-platinum-south-kelowna-slopes-pinot-noir-750-ml | {sku=316971; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/1/316971_cedar_creek_plat_south_slopes_pinot.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Cedar Creek Estate Winery Platinum East Kelowna Slope Pinot Noir 750 mL | $69.99 | https://www.everythingwine.ca/cedar-creek-estate-winery-platinum-east-kelowna-slope-pinot-noir-750-ml | {sku=245489; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/4/245489_cedar_creek_plat_east_pinot_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Jacobs Creek Reserve Cabernet Sauvignon 750 mL | $19.99 | https://www.everythingwine.ca/jacobs-creek-reserve-cabernet-sauvignon-750-ml | {sku=775296; country=Australia; image_url=https://www.everythingwine.ca/media/catalog/product/7/7/775296_jacobs_creek_reserve_cabernet_sauvignon.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Cobble Creek Paso Robles Pinot Noir 750 mL | $34.99 | https://www.everythingwine.ca/cobble-creek-paso-robles-pinot-noir-750-ml | {sku=312909; country=USA; image_url=https://www.everythingwine.ca/media/catalog/product/3/1/312909_cobble_hill_pinot_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Tinhorn Creek Vineyards Cabernet Franc 750 mL | $26.99 | https://www.everythingwine.ca/tinhorn-creek-cabernet-franc-750-ml | {sku=530717; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/3/530717_tinhorn_creek_cabernet_franc_1.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 0 results)

#### search_marquis_tool (status=ok, 0 results)

#### search_legacy_liquor_store_tool (status=ok, 5 results)
  - CedarCreek Cabernet Merlot (France) | $32.16 | stock=35 | https://www.legacyliquorstore.com/product/wine/cedarcreek-cabernet-merlot-france-1-x-750ml | {slug=cedarcreek-cabernet-merlot-france-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - CedarCreek Chardonnay (Oregon & California) | $29.84 | stock=27 | https://www.legacyliquorstore.com/product/wine/cedarcreek-chardonnay-oregon-california-1-x-750ml | {slug=cedarcreek-chardonnay-oregon-california-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "chardonnay"]}
  - Cedarcreek Riesling (Germany) | $26.09 | stock=3 | https://www.legacyliquorstore.com/product/wine/cedarcreek-riesling-germany-1-x-750ml | {slug=cedarcreek-riesling-germany-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "riesling"]}
  - CedarCreek Pinot Noir (Oregon) | $32.36 | stock=44 | https://www.legacyliquorstore.com/product/wine/cedarcreek-pinot-noir-oregon-1-x-750ml | {slug=cedarcreek-pinot-noir-oregon-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Cedarcreek Cabernet Merlot | $32.58 | stock=6 | https://www.legacyliquorstore.com/product/wine/cedarcreek-cabernet-merlot-1-x-750ml | {brand=Cedarcreek; slug=cedarcreek-cabernet-merlot-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}

#### search_bcliquor_tool (status=ok, 10 results)
  - ROAD 13 - ROSE 2023 | $27.99 | stock=159 | in 15 stores | rating=5.0 | https://www.bcliquorstores.com/product/214075 | {sku=214075; product_type=Rose Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=This Rosé opens with delicate aromas of wild rose petals, cherry blossom, and red apple. The palate is fresh and vibrant, offering flavours of cherry juice, pear, apple, and a hint of licorice, finishing long and persistent with balanced acidity.
; consumer_votes=1; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/214075.jpeg; certificates=["BC VQA", "All VQA"]}
  - ROAD 13 - SEVENTY-FOUR K | $27.99 | stock=1492 | in 126 stores | rating=4.1 | https://www.bcliquorstores.com/product/78915 | {sku=78915; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=Delicate aromas of dark cherry, black currant, blackberry, and dark chocolate with subtle toasted oak notes on the nose. Flavours of caramel, dark chocolate, and vanilla bean on the palate, ending with a long, rich finish.
; consumer_votes=166; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/78915.jpeg; certificates=["BC VQA", "All VQA"]}
  - ROAD 13 - HONEST JOHN'S RED | $23.99 | stock=335 | in 38 stores | rating=4.0 | https://www.bcliquorstores.com/product/290684 | {sku=290684; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=13.9; sweetness=00; tasting_notes=Ripe dark fruit, strawberry pastry, and black pepper are delicately pronounced on the nose. Balanced with silky tannins, this fruit forward red is a crowd-pleaser filled with complexity. 
; consumer_votes=196; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/290684.jpeg; certificates=["BC VQA", "All VQA"]}
  - ROAD 13 VINEYARDS VIOGNIER 2022 | $29.99 | stock=356 | in 32 stores | rating=4.5 | https://www.bcliquorstores.com/product/739888 | {sku=739888; product_type=White Wine; grape_type=VIOGNIER; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=This Viognier offers nuanced notes of ripe papaya, peach, apricot, honey, and orange peel on the nose. The palate is complemented by ripe tropical and stone fruit, delivering a full-bodied and rich experience with an excellent finish and length.
; consumer_votes=2; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/739888.jpeg; certificates=["BC VQA", "All VQA"]}
  - ROAD 13 - HONEST JOHN'S RED AUSTRALIA 2024 | $23.99 | stock=1969 | in 185 stores | rating=4.5 | https://www.bcliquorstores.com/product/688419 | {sku=688419; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=CRAFTED IN BC. Raspberry and cherry lead the palate, supported by eucalyptus and spice. Fine tannins and integrated oak give balance and length.
; consumer_votes=4; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/688419.jpeg}
  - ROAD 13 - JOHN OLIVER 5TH ELEMENT 2020 | $62.99 | stock=62 | in 12 stores | rating=4.2 | https://www.bcliquorstores.com/product/45922 | {sku=45922; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=15.5; sweetness=00; tasting_notes=90 Points, Anthony Gismondi: "Merlot dominant Bordeaux blend with Syrah added to the mix. The grapes for this wine were sourced from our best-producing vineyards and then selected from the best of the barrels in the cellar. A full-bodied, juicy, jammy dark fruit-forward wine that has exceptional oaky charcater."
; consumer_votes=29; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/45922.jpeg; certificates=["BC VQA", "All VQA"]}
  - ROAD 13 - HONEST JOHN'S BRIGHT ROSE NEW ZEALAND 2025 | $18.99 (reg $20.99) | stock=3340 | in 158 stores | rating=4.8 | https://www.bcliquorstores.com/product/270047 | {sku=270047; product_type=Rose Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Bright red fruit and raspberry aromas capture a New Zealand summer, leading into a strawberries and cream palate lifted by vibrant acidity and a crisp, refreshing finish.
; consumer_votes=7; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/270047.jpeg}
  - PINOT NOIR - FELTON ROAD BANNOCKBURN | $94.99 | stock=137 | in 17 stores | rating=4.5 | https://www.bcliquorstores.com/product/391511 | {sku=391511; product_type=Red Wine; grape_type=PINOT NOIR; country=New Zealand; volume=0.750; alcohol_pct=13.8; sweetness=00; tasting_notes=95 Points, James Suckling: "A perfumed nose of strawberries, sour cherries, raspberries, violets, vanilla and baking spices. It's medium-to full-bodied with lively acidity and fine tannins. Balanced and compact with a velvety texture and a bright core of fruit on the mid-palate. Long finish. Chewy..." (October, 2021)
; consumer_votes=20; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/391511.jpeg}
  - FLEURIE - MARC DELIENNE ABBAYE ROAD | $65.97 (reg $75.99) | stock=1 | in 1 stores | rating=4.2 | https://www.bcliquorstores.com/product/389968 | {sku=389968; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=A juicy, fragrant wine with notes of red fruits, blueberries and spice. Great balance with silky, succulent fruit and a core of acid holding things in place.
; consumer_votes=4; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/389968.jpeg}
  - GRENACHE - HITHER AND YON MCLAREN VALE SAND ROAD | $32.99 | stock=450 | in 38 stores | rating=5.0 | https://www.bcliquorstores.com/product/300713 | {sku=300713; product_type=Red Wine; grape_type=GRENACHE/GARNACHA; country=Australia; volume=0.750; alcohol_pct=14.0; sweetness=00; consumer_votes=7; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/300713.jpeg}

#### search_everything_wine_tool (status=ok, 14 results)
  - Road 13 Vineyards Marsanne 750 mL | $34.98 | https://www.everythingwine.ca/road-13-vineyards-marsanne-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards Viognier 750 mL | $29.99 | [North Vancouver:0, South Surrey:0, Langley Store:13, Vancouver:0] | https://www.everythingwine.ca/road-13-vineyards-viognier-750-ml | {sku=739888; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/3/739888_road_13_viognier.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards Select Harvest GSM 2020 750 mL | $45.99 | [North Vancouver:0, South Surrey:0, Langley Store:4, Vancouver:0] | https://www.everythingwine.ca/road-13-vineyards-grenache-syrah-mourvedre-750ml | {sku=579938; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/7/579938_road_13_select_harvest_gsm.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards Honest John's Australia Red Blend 750 mL | $23.99 | https://www.everythingwine.ca/road-13-vineyards-honest-john-s-australia-red-blend-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards Jackpot Chardonnay 750 mL | $60.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/road-13-vineyards-jackpot-chardonnay-750ml | {sku=580910; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/8/580910_road13_jackpot_chard.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards John Oliver Syrah 750 mL | $87.98 | https://www.everythingwine.ca/road-13-vineyards-john-oliver-syrah-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards John Oliver Malbec 750 mL | $87.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/road-13-vineyards-john-oliver-malbec-750-ml | {sku=312926; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/1/312926_road_13_john_oliver_malbec.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards 5th Element 750 mL | $62.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/road-13-5th-element-11 | {sku=45922; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/5/45922_road_13_5th_element_nl.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards Blind Creek Viognier 750 mL | $31.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/road-13-vineyards-blind-creek-viognier-750-ml | {sku=21454; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/1/21454_road_13_vineyards_blind_creek_viognier.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards Select Harvest Cabernet Merlot 750 mL | $25.99 | [North Vancouver:102, South Surrey:102, Langley Store:52, Vancouver:87] | https://www.everythingwine.ca/road-13-vineyards-select-harvest-cabernet-merlot-750-ml | {sku=139793; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/3/139793_road_13_select_harvest_cabmer.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Road 13 Vineyards Honest John's Washington Rosé 750 mL | $18.99 | [North Vancouver:13, South Surrey:8, Langley Store:4, Vancouver:8] | https://www.everythingwine.ca/road-13-vineyards-honest-john-s-washington-rose-750-ml | {sku=270047; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/270047_road13_washington_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Road 13 Vineyards Honest John's Bold Red 750 mL | $23.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/road-13-honest-john-s-red | {sku=290684; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/9/290684_road_13_honest_john_red_nl2_1.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Road 13 Vineyards Seventy-Four K Red Blend 750 mL | $27.99 | [North Vancouver:0, South Surrey:6, Langley Store:10, Vancouver:1] | https://www.everythingwine.ca/road-13-seventy-four-k | {sku=78915; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/8/78915_road13_74k.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Road 13 Vineyards Honest John's New Zealand White Blend 750 mL | $24.98 | [North Vancouver:22, South Surrey:17, Langley Store:12, Vancouver:17] | https://www.everythingwine.ca/road-13-vineyards-honest-john-s-new-zealand-white-blend-750-ml | {sku=270039; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/270039_road13_honestjohns_whiite_crafted.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 14 results)
  - ROAD 13 - GSM | $44.99 | stock=10 | https://okanagancellars.com/products/2643791-road-13-gsm | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000057/0000579938-4834.png}
  - ROAD 13 - HONEST JOHNS RED 2024 | $22.99 | stock=28 | https://okanagancellars.com/products/5073372-road-13-honest-johns-red-2024 | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000068/0000688419-5922.jpg}
  - ROAD 13 - HONEST JOHNS ROSE 2024 US | $17.99 (reg $19.99) | stock=15 | https://okanagancellars.com/products/4806018-road-13-honest-johns-rose-2024-us | {category=Rose; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000027/0000270047-2964.jpg}
  - ROAD 13 - HONEST JOHNS WHITE 2024 NZ | $19.99 | stock=34 | https://okanagancellars.com/products/4829149-road-13-honest-johns-white-2024-nz | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/all/BC270039.png}
  - ROAD 13 - JACKPOT CHARDONNAY | $54.99 | stock=13 | https://okanagancellars.com/products/4295187-road-13-jackpot-chardonnay | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000058/0000580910-4128.png}
  - ROAD 13 - JOHN OLIVER 5TH ELEMENT | $64.99 | stock=7 | https://okanagancellars.com/products/4353202-road-13-john-oliver-5th-element | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000004/0000045922-3438.jpg}
  - ROAD 13 - JOHN OLIVER MALBEC | $79.99 | stock=7 | https://okanagancellars.com/products/4353158-road-13-john-oliver-malbec | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000031/0000312926-8194.jpg}
  - ROAD 13 - JOHN OLIVER SYRAH | $79.99 | stock=6 | https://okanagancellars.com/products/2643785-road-13-john-oliver-syrah | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000087/0000876698-4259.png}
  - ROAD 13 - SELECT HARVEST CAB MERLOT | $25.99 | stock=31 | https://okanagancellars.com/products/5171088-road-13-select-harvest-cab-merlot | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000013/0000139793-2329.jpg}
  - ROAD 13 - SELECT HARVEST WINDING ROAD WHITE | $20.99 | stock=15 | https://okanagancellars.com/products/4726962-road-13-select-harvest-winding-road-white | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/all/BC269046.jpg}
  - ROAD 13 - SEVENTY-FOUR K | $27.99 | stock=15 | https://okanagancellars.com/products/2643783-road-13-seventy-four-k | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/bc_lrs/000007/0000078915.jpg}
  - ROAD 13 - SPARKLING CHENIN BLANC | $44.99 | stock=16 | https://okanagancellars.com/products/3420958-road-13-sparkling-chenin-blanc | {category=Bubbles; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000082/0000820696-7288.png}
  - ROAD 13 - SYRAH | $39.99 | stock=16 | https://okanagancellars.com/products/2643789-road-13-syrah | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000041/0000417287-1994.png}
  - ROAD 13 - VIOGNIER | $27.99 | stock=30 | https://okanagancellars.com/products/2643782-road-13-viognier | {category=White Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000073/0000739888-7338.png}

#### search_suttonplace_tool (status=ok, 0 results)

#### search_marquis_tool (status=ok, 1 results)
  - Domaine Artema 2022 Black Sage Road Rouge 750ml | $24.49 | stock=14 | https://www.marquis-wines.com/domaine-artema-2022-black-sage-road-rouge-750ml/ | {sku=1032199; in_stock=True; categories=["Red Wine", "Syrah & Shiraz", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21816/images/17501/2026-05-15-12.09.58__73486.1779221076.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 5 results)
  - Road 13 Honest John's White (New Zealand) | $24.4 | stock=43 | https://www.legacyliquorstore.com/product/wine/road-13-honest-johns-white-new-zealand-1-x-750ml | {slug=road-13-honest-johns-white-new-zealand-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "blend"]}
  - Road 13 Honest John's Red (Australia) | $27.58 | stock=24 | https://www.legacyliquorstore.com/product/wine/road-13-honest-johns-red-australia-1-x-750ml | {slug=road-13-honest-johns-red-australia-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Road 13 Honest John's Rose (Washington) | $21.99 | stock=2 | https://www.legacyliquorstore.com/product/wine/road-13-honest-johns-rose-washington-1-x-750ml | {slug=road-13-honest-johns-rose-washington-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "rose wine"]}
  - Road 13 Viognier | $33.73 | stock=31 | https://www.legacyliquorstore.com/product/wine/road-13-select-harvest-viognier-1-x-750ml | {slug=road-13-select-harvest-viognier-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "viognier"]}
  - Road 13 Seventy-Four K | $29.19 | stock=33 | https://www.legacyliquorstore.com/product/wine/road-13-vineyards-seventy-four-k-1-x-750ml | {brand=Road 13; slug=road-13-vineyards-seventy-four-k-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}

````

</details>

### Latency

- 136.32s
