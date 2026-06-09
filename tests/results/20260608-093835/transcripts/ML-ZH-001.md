# ML-ZH-001 — ML

_Notes:_ Chinese query (red wine for Peking duck, buyable in Vancouver) — must answer in Chinese

- Thread ID: `eval-ML-ZH-001-e7cef2f2`
- Turns: 1

---
## Turn 0

### Query

> 推荐一款适合北京烤鸭的红葡萄酒，最好在温哥华能买到。

### Tool Calls (in order)

1. `sommelier_agent_tool` args={"request": "What are some excellent red wine pairings for Peking Duck (\u5317\u4eac\u70e4\u9e2d)? Please recommend specific styles (such as Pinot Noir or Cru Beaujolais) and specific producers or bottles that would pair beautifully with the rich, savory, and slightly sweet profile of the duck and hoisin sauce."}
2. `sourcing_agent_tool` args={"request": "Pinot Noir and Cru Beaujolais red wines available in Vancouver liquor stores with prices and stock."}

### Final Response

```markdown
为您推荐两款在温哥华本地非常容易买到、且堪称**北京烤鸭（Peking Duck）绝配**的红葡萄酒。

北京烤鸭皮脆肉嫩、油脂丰厚，且伴有甜面酱的甜咸风味。搭配红葡萄酒时，**必须避免高单宁的重酒体红酒**（如赤霞珠 Cabernet Sauvignon），因为重单宁会与甜面酱的甜味冲突，产生不愉悦的苦涩感。因此，**高酸度、低单宁、果香充沛的红葡萄酒**（如黑皮诺 Pinot Noir 或博若莱佳美 Gamay）是最佳选择，它们能像高档樱桃酱或梅子酱一样，既能化解鸭肉的油腻，又能衬托出鸭肉的鲜美。

---

### 推荐一：法国博若莱特级村庄名庄酒（Cru Beaujolais）
#### **Marcel Lapierre Morgon (马塞尔·拉皮埃尔 摩根红葡萄酒)**
*   **推荐理由**：这是自然酒先驱 Lapierre 的旗舰酒款，也是侍酒师界公认的“北京烤鸭终极绝配”。它由 100% 佳美（Gamay）葡萄酿造，单宁极低，质地如丝般顺滑。酒中带有明亮的甜樱桃、覆盆子、甘草和轻微的香料气息，活泼的酸度能瞬间带走鸭皮的油腻感，而其多汁的红果风味与甜面酱的甜咸味完美融合。
*   **专业评分**：其 **2023 年份** 荣获《Decanter》**92 分**，罗伯特·帕克《葡萄酒倡导家》（Wine Advocate）**90 分**。
*   **温哥华本地购买渠道**：
    *   **BC Liquor Stores**：售价 **$56.99** | 现货充足（系统登记名称为 *Morgon - Mathieu & Camille Lapierre*）| [BC Liquor 购买链接](https://www.bcliquorstores.com/product/141366)
    *   **Everything Wine (Vancouver)**：售价 **$56.99** | 少量现货 | [Everything Wine 购买链接](https://www.everythingwine.ca/marcel-lapierre-morgon)

---

### 推荐二：本地 BC 省顶级黑皮诺（BC VQA Pinot Noir）
#### **Meyer Family Vineyards Pinot Noir (迈耶家族黑皮诺红葡萄酒)**
*   **推荐理由**：黑皮诺是烤鸭的经典传统搭配。位于 BC 省 Okanagan Falls 的 Meyer Family Vineyards 被誉为加拿大酿造“勃艮第风格”黑皮诺的标杆酒庄。这款黑皮诺充满新鲜的红樱桃、野草莓和微妙的泥土、香料气息，口感优雅，酸度清爽，能完美衬托烤鸭的细腻肉质。
*   **专业评分**：迈耶家族的黑皮诺品质极高，其高端单园系列（如 Old Block 2022）曾斩获加拿大国家葡萄酒奖 **93 分**白金奖及 Decanter **94 分**。这款庄园级黑皮诺同样继承了其优雅细腻的骨架，性价比极高。
*   **温哥华本地购买渠道**：
    *   **Marquis Wine Cellars**：售价 **$34.99** | 现货 12 瓶 | [Marquis Wine 购买链接](https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/)
    *   **Legacy Liquor Store**：售价 **$33.30** | 现货 6 瓶 | [Legacy Liquor 购买链接](https://www.legacyliquorstore.com/product/wine/meyer-pinot-noir-1-x-750ml)

---

### 备选推荐：高性价比本地名庄黑皮诺
#### **Tantalus Pinot Noir 2022 (坦塔罗斯黑皮诺红葡萄酒)**
*   **推荐理由**：Tantalus 是 BC 省最著名的精品酒庄之一。这款 2022 年份黑皮诺带有红醋栗、樱桃、无花果的香气，并伴有独特的矿物质感和雪松、湿泥土的复杂层次。单宁柔和，结构优雅，非常适合搭配烤鸭。
*   **温哥华本地购买渠道**：
    *   **BC Liquor Stores**：售价 **$35.99** | 现货 87 瓶 | [BC Liquor 购买链接](https://www.bcliquorstores.com/product/200881)

**侍酒师贴士**：在享用北京烤鸭前，建议将上述红葡萄酒稍微冰镇至 **14°C - 16°C** 饮用，此时酒中的红果香气最清爽，酸度也最活泼，解腻效果更佳！
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
    "SUPPORTED": 13,
    "GENERAL_KNOWLEDGE": 2,
    "NOT_IN_EVIDENCE": 0,
    "CONTRADICTED": 0
  },
  "correctness_rationale": "The agent perfectly extracted the pairing rationale, specific wine recommendations, accurate pricing, stock levels, and purchase links from the evidence.",
  "issues": [],
  "strengths": [
    "Excellent explanation of the pairing rationale for Peking Duck.",
    "Provides highly specific, actionable purchasing information for the Vancouver market, including prices, stock levels, and links.",
    "Well-structured and easy to read, with a helpful sommelier tip at the end."
  ],
  "parse_error": false
}
```

### Claim Verdicts

| Label | Claim | Evidence quote |
|---|---|---|
| SUPPORTED | Cabernet Sauvignon is a high-tannin red wine that clashes with sweet hoisin sauce. | Crucially, for red wine, we must avoid high-tannin bottles (like Cabernet Sauvignon), as heavy tannins will clash with the sweet hoisin and taste bitter and astringent. |
| SUPPORTED | Pinot Noir and Gamay are high-acid, low-tannin red wines. | Recommended Style *   **Red:** Cool-climate, high-acid, low-tannin reds (Pinot Noir, Gamay Noir). |
| GENERAL_KNOWLEDGE | Marcel Lapierre Morgon is made from 100% Gamay grapes. | — |
| SUPPORTED | The 2023 vintage of Marcel Lapierre Morgon scored 92 points from Decanter. | **Decanter: 92 Points**     *   *Review Summary:* Decanter highlights this flagship bottling for its luminous, bright profile |
| SUPPORTED | The 2023 vintage of Marcel Lapierre Morgon scored 90 points from Robert Parker's Wine Advocate. | **Robert Parker’s Wine Advocate: 90 Points** (Reviewed by Kenna Wells, March 2025) |
| SUPPORTED | Marcel Lapierre Morgon is available at BC Liquor Stores for $56.99. | **Marcel Lapierre Morgon Beaujolais (750 mL)**     *   **BC Liquor:** $56.99 \| Stock: 42 units |
| SUPPORTED | Marcel Lapierre Morgon is available at Everything Wine in Vancouver for $56.99. | **Everything Wine (Vancouver):** $56.99 \| Stock: 2 units |
| SUPPORTED | Meyer Family Vineyards is located in Okanagan Falls, BC. | Meyer Family Vineyards in Okanagan Falls, BC, is highly regarded for its Burgundian-style Pinot Noirs. |
| SUPPORTED | Meyer Family Vineyards 'Old Block' Pinot Noir 2022 scored 93 points and won a Platinum Medal at the National Wine Awards of Canada. | **2022 Old Block Pinot Noir:** Awarded a Platinum Medal and **93 points** at the 2025 National Wine Awards of Canada. |
| SUPPORTED | Meyer Family Vineyards 'Old Block' Pinot Noir 2022 scored 94 points from Decanter. | **2022 Old Block Pinot Noir:** Awarded a Silver Medal and **94 points** at the 2024 Decanter World Wine Awards. |
| SUPPORTED | Meyer Family Pinot Noir is available at Marquis Wine Cellars for $34.99 with 12 bottles in stock. | **Marquis Wine Cellars (2023):** $34.99 \| Stock: 12 units |
| SUPPORTED | Meyer Family Pinot Noir is available at Legacy Liquor Store for $33.30 with 6 bottles in stock. | **Legacy Liquor Store:** $33.30 \| Stock: 6 units |
| SUPPORTED | Tantalus Pinot Noir 2022 features notes of red currant, cherry, fig, mineral, cedar, and wet earth. | Rich notes of cedar, wet earth and graphite complement the aromatic profile. Despite its youth, the palate is showing beautiful complexity and nuance with swaths of red currant, cherry and fig spun to |
| SUPPORTED | Tantalus Pinot Noir 2022 is available at BC Liquor Stores for $35.99 with 87 bottles in stock. | **Tantalus Pinot Noir 2022 (750 mL)**     *   **BC Liquor:** $35.99 \| Stock: 87 units |
| GENERAL_KNOWLEDGE | Light red wines like Pinot Noir and Gamay are best served slightly chilled at 14°C - 16°C. | — |

### Evidence shown to judge

_2 tool messages, 149768 chars (budget 2000000)_

<details><summary>Show evidence</summary>

````markdown
### sommelier_agent_tool (status=ok)
**Sub-agent synthesis:**
As the beverage director for your Vancouver drinks concierge, I can tell you that pairing beverages with Peking Duck (北京烤鸭) is one of the most exciting challenges in the culinary world. The dish is a masterclass in contrasting textures and flavors: ultra-crispy, fatty skin; rich, tender meat; sweet, earthy hoisin or sweet bean sauce; and the sharp, fresh bite of scallions and cucumber wrapped in a delicate pancake. 

To pair successfully, we need beverages that can **cut through the rich duck fat** (via high acidity or carbonation) and **complement the sweet/savory hoisin sauce** (via ripe fruit, spice, or umami). Crucially, for red wine, we must avoid high-tannin bottles (like Cabernet Sauvignon), as heavy tannins will clash with the sweet hoisin and taste bitter and astringent. 

Here are my top recommendations across all categories, with a special focus on the excellent red wines you requested.

---

### 1. Wine (Focus on Red Wine)
Cool-climate, fruit-forward reds with low-to-moderate tannins and high acidity act almost like a gourmet cherry or plum sauce accompaniment to the duck. 

**BC VQA Pinot Noir**
*   **Meyer Family Vineyards 'Old Block' Pinot Noir (Okanagan Falls, BC):** Meyer is renowned for its Burgundian-style Pinot Noirs. The **2022 vintage** was awarded a Platinum Medal and **93 points** at the National Wine Awards of Canada ([WineAlign](https://mfvwines.com)), as well as **94 points** at the Decanter World Wine Awards ([Decanter](https://www.decanter.com)). It offers elegant, bright acidity that slices through the duck fat, with a sour cherry profile and fine spice integration that perfectly matches the hoisin.
*   **Martin's Lane 'Naramata Ranch Vineyard' Pinot Noir (Naramata Bench, BC):** For a premium, structured local option, the **2020 vintage** scored **96 points** from critic Anthony Gismondi ([WineAlign / Godello](https://godello.ca)). Gismondi celebrated it as a textbook expression of Naramata Bench Pinot, showing great depth, polished tannins, and a stony minerality that provides a beautiful, earthy counterpoint to the savory duck meat.

**Cru Beaujolais (Gamay Noir)**
*   **Domaine Marcel Lapierre Morgon (Beaujolais, France):** This is a legendary pairing for Peking Duck. The **2023 vintage** scored **92 points** from [Decanter](https://www.vinetrail.co.uk), which highlighted its luminous, bright profile of sweet cherry, raspberry, licorice, and clove. Robert Parker’s Wine Advocate awarded it **90 points**, praising its floral aromas of lavender and crushed petals alongside a lush, dense palate with bright acidity. The juicy blue and red fruit core bridges flawlessly with the sweet bean sauce, while the vibrant acidity cleanses the palate.

---

### 2. Beer
Carbonation is a sommelier’s secret weapon against fat, acting as a scrubbing brush on the tongue to clear away rich duck oils. 

*   **BC Craft - Sour Ale:** **Strange Fellows Brewing 'Reynard' Oud Bruin (Vancouver, BC).** This is a Flanders-style sour brown ale aged in French oak. Reviewers at [*Mike's Craft Beer* / *Beer Me BC*](https://beermebc.com) note its complex layers of oak, cherry, dark fruits, and caramel, balanced by a tart, vinegar-like sourness. The lactic acidity cuts the fat like a knife, while the sour cherry notes act as a brilliant condiment to the duck.
*   **BC Craft - Belgian Dubbel:** **Dageraad Brewing 'Brune' (Burnaby, BC).** If you prefer something without sourness, this Belgian-style Dubbel is perfect. Reviewed by [*BeerCrank.ca*](https://beercrank.ca), it features prominent caramel sweetness, nuttiness, and deep dark fruit notes of raisin, plum, and fig. The caramelized sugars in the roasted duck skin and the hoisin sauce find a perfect flavor bridge in this malt-forward beer.

---

### 3. Spirit / Cocktail
A cocktail for Peking Duck needs to balance sweetness, acidity, and spice, echoing the Chinese five-spice and scallion components of the dish.

*   **The Spirit:** **Sheringham Distilling 'Beacon Gin' (formerly Kazuki Gin) (Langford, BC).** This unique Vancouver Island gin is distilled with Japanese cherry blossoms, yuzu peel, and local Westholme green tea. [*The Rum Howler Blog*](https://therumhowlerblog.com) awarded it **89/100**, praising its exotic character and spicy coriander/citrus finish. 
*   **The Cocktail Build: "The Orchard Highball"**
    *   1.5 oz Sheringham Beacon Gin
    *   0.75 oz Fresh Lime Juice
    *   0.75 oz House-made Five-Spice Plum Syrup (plum juice simmered with star anise, cinnamon, and clove)
    *   Top with soda water (or Lapsang Souchong smoked tea-infused soda for a roasted note).
    *   *Garnish:* A long cucumber ribbon (matching the cucumber in the duck pancake).
    *   *Why it works:* The plum and five-spice echo the hoisin, the citrus cuts the fat, and the gin's green tea botanicals refresh the palate without overwhelming the delicate pancake.

---

### 4. Sake
Sake is naturally high in succinic acid (umami), which acts as a flavor magnifier for savory, roasted meats. 

*   **Traditional Import:** **Tengumai 'Yamahai Junmai' (Ishikawa, Japan).** Brewed using the traditional, slow Yamahai method. Sake specialist Mariko Tajiri and sommelier Iori Kataoka (via [*Business in Vancouver*](https://biv.com)) note its funky, yogurt-and-mushroom complexity, likening it to natural wine. It has rich flavors of butterscotch and walnut with robust acidity. Served warm, its intense umami acts as a luxurious, savory blanket to the rich duck meat and fermented soybean paste.
*   **BC Local:** **Artisan SakeMaker 'Osake' Junmai Nama (Granville Island, Vancouver, BC).** From Canada's first local sake winery, this unpasteurized (*nama*) sake is light, crisp, and off-dry with notes of pear and melon ([Artisan SakeMaker](https://artisansakemaker.com)). Its bright, clean profile offers a refreshing, palate-cleansing contrast to the rich, fatty duck skin, making it highly approachable for white wine drinkers. 

*Our Sourcing specialist will follow up shortly with verified pricing and availability for these recommendations in the Vancouver market.*

#### reasoning_pair_wine_tool (status=ok, 0 results)
Recommendation: As an expert sommelier and beverage director in the Vancouver market, pairing with Peking Duck is one of the most exciting challenges. This iconic dish is a masterclass in textures and flavors: the ultra-crispy, fatty skin; the rich, tender meat; the sweet, savory, and slightly earthy hoisin or sweet bean sauce; and the sharp, fresh bite of scallions and cucumber wrapped in a delicate pancake. 

To pair successfully, we need beverages that can **cut through the rich duck fat** (via high acidity, carbonation, or alcohol), **complement the sweet/savory hoisin sauce** (via ripe fruit or spice notes), and **not overwhelm the delicate pancake and cucumber**.

Here are my top recommendations across all categories for the ultimate Peking Duck pairing experience.

---

### 1. Wine

#### Why This Pairing Works
Peking Duck demands a wine with high acidity to slice through the rich layer of fat under the crispy skin. However, because hoisin sauce is sweet and savory, we must avoid high-tannin red wines, which will taste bitter and astringent when clashing with the sauce. 

A cool-climate, fruit-forward red with low-to-moderate tannins (like Pinot Noir or Gamay) acts like a classic cherry or plum sauce accompaniment to the duck. Alternatively, a traditional-method sparkling wine provides the ultimate textural contrast, using effervescence to scrub the palate clean after each rich bite.

#### Recommended Style
*   **Red:** Cool-climate, high-acid, low-tannin reds (Pinot Noir, Gamay Noir).
*   **Sparkling:** Brut or Rosé traditional-method sparkling wine with bright acidity and yeast autolysis (brioche notes) to match the pancake.

#### Specific Examples
*   **BC VQA:** *Meyer Family Vineyards 'McLean Creek Road' Pinot Noir* (Okanagan Falls, BC) – Elegant, bright acidity, bursting with sour cherry and wild strawberry that cuts the fat, with a subtle earthy undertone that matches the hoisin.
*   **BC VQA:** *Haywire 'Gamay' Gamay Noir* (Summerland, BC) – Juicy, vibrant, and fermented in concrete, offering pure red berry fruit and a mineral finish that keeps the palate refreshed.
*   **International:** *Domaine de Colette Morgon* (Beaujolais, France) – A Gamay with a bit more structure, offering dark cherry, black pepper, and a stony minerality that stands up beautifully to the rich meat.
*   **International:** *Schramsberg 'Mirabelle' Brut Rosé* (North Coast, California, USA) – A Pinot Noir-dominant sparkling wine with vibrant acidity, creamy mousse, and red fruit notes that dance with the crispy duck skin.

---

### 2. Beer

#### Why This Pairing Works
Carbonation is a sommelier’s secret weapon against fat. The bubbles in beer act as a scrubbing brush on the tongue, clearing away the rich duck oils. Furthermore, the caramelized sugars in roasted duck skin and the sweet hoisin sauce find a perfect flavor bridge in beers that feature toasted malt profiles or dark fruit esters.

#### Recommended Style
*   **Belgian Dubbel:** Rich, yeasty, with dark fruit (fig, plum) and clove notes that mimic five-spice.
*   **Flanders Red Ale:** A sour, oak-aged ale. The lactic acidity cuts the fat like a knife, while the sour cherry profile acts as a gourmet condiment to the duck.

#### Specific Examples
*   **BC Craft:** *Dageraad Brewing 'Dubbel'* (Burnaby, BC) – A world-class, Belgian-style dubbel. Its notes of dried plum, brown sugar, and high carbonation are a sublime match for the hoisin and crispy skin.
*   **BC Craft:** *Strange Fellows Brewing 'Reynard' Oud Bruin* (Vancouver, BC) – A sour brown ale with cherry notes and a dry, tart finish that slices through the duck's richness.
*   **Import:** *Duchesse de Bourgogne* (West Flanders, Belgium) – The quintessential Flanders Red Ale. Its sweet-and-sour, balsamic-like complexity is arguably the single best beer pairing for Peking Duck on earth.
*   **Import:** *Chimay Première (Red)* (Scourmont Abbey, Belgium) – A classic Trappist Dubbel with a velvety body, light hop bitterness, and rich dark fruit notes.

---

### 3. Spirit / Cocktail

#### Why This Pairing Works
A cocktail for Peking Duck needs to balance sweetness, acidity, and spice. We want to avoid overly sweet drinks, instead opting for something refreshing, slightly tart, and infused with botanicals or tea that echo the Chinese five-spice and scallion components of the dish. 

#### Recommended Style
A highball or sour featuring local BC gin (which offers herbal complexity) or vodka, infused with smoky tea (like Lapsang Souchong) or stone fruit (plum/apricot) to bridge with the hoisin.

#### Specific Cocktail Build: **"The Forbidden Orchard Highball"**
This drink uses smoky tea to echo the roasted nature of the duck, while the plum and citrus cut the fat and match the hoisin.
*   **1.5 oz** *Sheringham Distilling 'Kazuki' Gin* (Sooke, BC) – chosen for its cherry blossom and green tea botanicals.
*   **0.75 oz** Fresh Lime Juice
*   **0.75 oz** House-made Five-Spice Plum Syrup (Plum juice simmered with star anise, fennel, cinnamon, clove, and Sichuan pepper).
*   **Top with:** Lapsang Souchong smoked black tea-infused soda water.
*   **Garnish:** A long, thin cucumber ribbon (matching the cucumber in the duck pancake).

#### Specific Spirit Examples (for the base)
*   **BC Distillery:** *Sheringham Distilling 'Kazuki' Gin* (Sooke, Vancouver Island, BC) – Its green tea and yuzu notes are incredibly food-friendly.
*   **BC Distillery:** *Odd Society Spirits 'East Van Vodka'* (Vancouver, BC) – A smooth, lightly sweet malted-barley vodka that takes infusions beautifully.
*   **BC Distillery:** *Resurrection Spirits 'White Rye'* (Vancouver, BC) – Offers a spicy, grain-forward kick that stands up to the pungent scallions.

---

### 4. Sake

#### Why This Pairing Works
Sake is naturally high in succinic acid (umami), which acts as a flavor magnifier for savory, roasted meats. Unlike wine, sake has very low acidity but makes up for it with body and amino acids. A richer, slightly earthy sake style will wrap around the savory duck meat and fermented soybean paste in the hoisin, creating a luxurious, savory harmony.

#### Recommended Style
*   **Yamahai or Kimoto Junmai:** These traditional brewing methods yield sakes with higher natural acidity, earthy/gamey notes, and intense umami that pair perfectly with roasted game.

#### Specific Examples
*   **BC/Local:** *Artisan SakeMaker 'Osake' Junmai Nama* (Granville Island, Vancouver, BC) – Fresh, unpasteurized, and lively. It has a bright, green-apple acidity and yeastiness that cuts the fat while respecting the delicate pancake.
*   **Import:** *Tengumai 'Yamahai Junmai'* (Ishikawa, Japan) – A legendary sake with a pale golden color, earthy, mushroomy aromas, and a rich, acidic backbone that loves roasted duck.
*   **Import:** *Sohomare 'Heart and Soul' Tokubetsu Kimoto Junmai* (Tochigi, Japan) – Deeply flavorful, structured, and brimming with umami. It acts as a savory blanket to the rich duck meat.

#### search_web_grounded_tool (status=ok, 10 results)
Search answer: Meyer Family Vineyards in Okanagan Falls, BC, is highly regarded for its Burgundian-style Pinot Noirs. Reviews and scores from **WineAlign** (including the National Wine Awards of Canada) and **Decanter** (including the Decanter World Wine Awards) highlight several key vintages:

### **WineAlign & National Wine Awards of Canada (NWAC)**
*   **2022 Old Block Pinot Noir:** Awarded a Platinum Medal and **93 points** at the 2025 National Wine Awards of Canada.
*   **2020 Old Block Pinot Noir:** Awarded a Platinum Medal and **94 points** at the 2022 National Wine Awards of Canada.
*   **2020 Micro Cuvée Pinot Noir:** Awarded a Gold Medal and **92 points** at the 2022 National Wine Awards of Canada.
*   **2014 Reimer Vineyard Pinot Noir:** Scored **92 points** by WineAlign critic David Lawrason, who praised its refined floral and red fruit aromatics, mid-weight silkiness, and intense finish.
*   **2014 McLean Creek Road Vineyard Pinot Noir:** Scored **90 points** by David Lawrason, who noted its ripe sour cherry profile, fine spice integration, and energetic, tannic structure.
*   **2010 Reimer Vineyard Pinot Noir:** Scored **92 points** by David Lawrason, who called it a "modern B.C. classic".
*   **2010 McLean Creek Road Vineyard Pinot Noir:** Scored **92 points** by David Lawrason, who described it as a vibrant, solid Pinot with ripe raspberry-cherry fruit and well-integrated oak spice.

### **Decanter & Decanter World Wine Awards (DWWA)**
*   **2022 Old Block Pinot Noir:** Awarded a Silver Medal and **94 points** at the 2024 Decanter World Wine Awards.
*   **2022 McLean Creek Road Pinot Noir:** Awarded a Silver Medal and **91 points** at the 2024 Decanter World Wine Awards.
*   **2013 McLean Creek Road Pinot Noir:** Featured in *Decanter* magazine as "highly recommended" and named a top-value Pinot Noir from outside of Burgundy.
*   **2012 McLean Creek Road Pinot Noir:** Scored **91 points** by *Decanter* critic Steven Spurrier, who lauded its Burgundian profile, smooth texture, and vibrant energy.
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9q4BP_xDI58YqOj8sAsp1CFSIM3aLdMaGBcSlUaI_JB0px-BfnopAAX8wSmJ9ZeKQv_mk99sxaAskSh9-rcRroeLCgcoGAAeWcvPhT0wj): 
  - [scoutmagazine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3wdLcJlGGQxKD6YQqNdBHq43VY0n5wzly0zHyaipu6_CBxxlRzosiOWRymMYhCtmSPm4sRCf44ataiUcufLSxqlwJz5z1jD8vMZe59hWZFS7tv1lXCeEKE7TjZp320Nz4zSTi3VSn11g3qdhVIa0VSA==): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUgJDXSF_AKOtyp9hyA0QT19_Vej2xQ5sx23AhfOziwoKP8So_XwafkBAXQM5doiYGjESlDgmHBnBKQpLSXG1txCSt_vXlMltIKdtgf_ZA): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuGNZNT9MxUTNre7NsphqwWzoTCxei8S850tplWCv8FJFJg4Z3fYMhMTseijRJ0DqF56P6jPEU-QAbNEcWFEfZ1AnhDQbPGHYMAym93RxCUCoP8JBbhxm7qlAeL_fDzuXgrgDVLprCY8hRXTaQ3aEpTTI0Y_QhSf_HsdDjGlYLjw==): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzypE_oOi6iL8FZI4pBLL2HgJ1dVMnUsZwXyNHrCMga8kdpc602Q-6MHIBC0K5bD_mJyL86jrw0LtuhUJQFHPeXoSdewlKsuaMPg2kan1gv5nxONO9a7jXBQi2dkFJ5nV10GNQgY4PMJbJKPErxO6l-JhPr95CDyW6lxRc): 
  - [scoutmagazine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkBYLTXyr5KDqA7BJfBUiAYHf2F2CUpucopoSlVx4XbpuS2pBIdKzlsyRlNysbPu0T8obmCn07JQBlG-xfyt_7KnISzzUY-MPlEijuTUvHcMgbzzCdQXWojhxQ_g9cXRXs3d2_9ahesj4vg3oNEW7976y29GncyKC2YsUqS45OndHzls8pKshvd1V9xtigf02Z2Q5D53Wgp5ivjUHmKvblSRvoCig=): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGKG6ipk3nRDhCdrOs0VVX81O-IGN5f88lF-Dn6Gg4Qw7XIUqP6dPQws2gKxyTqta8IOw3lelqEi2VK8dXuZPZ1aZoGzlCKVVl_cmY0dKRGGzjoptRE6igxR_rlKZMe_ZpxZqJsPrj-45fP5k8o8jm76385J61jkeCisM=): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJTAI-MBzpu3yRhCbYeAwjzmL4IUzvmP1GLyptfQ6dqzYR-6Mq-8hfPCymDNyLVrJS1AoiG54AgUrlHKeqoNsRj5GsMpVgFuyCwPd9jFjC1hkB1i5neDKeFohIjx9w6jekEjhhKXn4aWiD3092Mw==): 
  - [mywinecanada.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGddRpRTd3jO_ow9c2UF_bzmnsyEtFFLqzafLudHZcY2qbDrvcvIyhKI9c8YjosZNe_mQCIjPcgnrK1_M4f81K_1I9eYA3pCqrRSTFBgPCRgsn6G2x8hzhEMEN0NKSKsIknudOcJRbG1XpJ-C0_3bOdMQ=): 
  - [decanter.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC1mKm3H9QoUVLC1i3PEt3X_1W2OJmZ2mWyxFSNOQbyN1Cfs1C0IiQriv6ICJYfiV1VjHqd0qonesRm7syj1f4JQ2LoSoCwQDw9FoAjk3aPHlQId1c_2j4aB_W3r-mF5kQwmdGisNhE3OgGjkipR_pNx1iPkojM0-vD5aM9B7UK1YHhud20e_HLgDJqfVoba1H12nhNXUbFA==): 

#### search_web_grounded_tool (status=ok, 12 results)
Search answer: Reviews and scores from **Decanter** and **Robert Parker’s Wine Advocate** for recent vintages of the iconic natural Beaujolais, **Domaine Marcel Lapierre Morgon**, include:

### **2023 Vintage**
*   **Decanter: 92 Points**
    *   *Review Summary:* Decanter highlights this flagship bottling for its luminous, bright profile of sweet cherry and raspberry, accented by licorice and clove. They note that despite its immediate appeal, it is a serious wine with the structure to age well.
*   **Robert Parker’s Wine Advocate: 90 Points** (Reviewed by Kenna Wells, March 2025)
    *   *Review Summary:* The Wine Advocate praises the wine's signature vibrancy, noting floral aromas of lavender and crushed petals alongside ripe red and blue fruits. The palate is described as medium-to-full-bodied, lush, and dense, supported by integrated tannins and bright acidity.

### **2022 Vintage**
*   **Morgon Cuvée Marcel Lapierre** *(sourced from old vines)*:
    *   **Decanter: 95 Points**
    *   **Wine Advocate: 91 Points** (Reviewed by Kenna Wells, 2024)
        *   *Review Summary:* The Wine Advocate describes a lush, blue-fruit-driven nose of blueberries, lilac, licorice, and herbs. It is medium-to-full-bodied with excellent concentration, freshness, and a juicy core.
*   **Morgon (Regular Bottling)**:
    *   **Wine Advocate: 88 Points**
        *   *Review Summary:* The review notes a classic nose of baking spices, plums, and cherries, leading to a velvety, succulent palate with rounded tannins.

### **Older Vintages**
*   **2020 Morgon — Wine Advocate: 91 Points** (Reviewed by William Kelley, August 2021)
    *   *Review Summary:* Kelley describes the wine as satiny and enveloping, showcasing pure, precise plum and raspberry fruit framed by melting tannins.
*   **2015 Morgon — Wine Advocate: 93 Points**
    *   *Review Summary:* The review highlights a vibrant bouquet of dark cherries, redcurrant, and rose petals, with a structured, energetic, and beautifully balanced palate.

### **Vancouver, BC Market Availability**
Marcel Lapierre's Morgon is highly sought after by natural wine enthusiasts in British Columbia. It is regularly imported in limited quantities and can be found at premium private wine retailers in Vancouver, such as **Marquis Wine Cellars**.
  - [pluckywines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-74G9uomELCVwBljjxV9Y0QhyVRyBLwC2a7jslB3BI8KxGPVuCS1-H4AE3GLcXhy4EPukUbTRbqds5UHw5iziiH7aCOrSlxd65hmp_ptKhbiUgxXqf_jlv9-TKgietEjvlyQg47C46irbI1t0kJ2hhhQ77HXsdyx43PrRVm4OVWLIbZryNkQ9GF1_9SjLJ9mTkg==): 
  - [wine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxAabGJUw0E2cIaJPJu-8-zwkGGdk-olD34Sk-qeUFgBT0sE6nmifA586Txj7gRtVc2qvS1b-35M0ILbZOE9C2Ko6glkm_PWkjnnYIQgsBIJZm4wX6HvW8rBBREXzGWENYzh2aKQU5K-J-8NGff7SfwijcOYbNL1QDO_l-): 
  - [jjbuckley.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENEQ2LWx-nd_rnw7yaKcyPwWwwiR7ZHpdKZIZ5y44-GCeVtj65KAUsk8Ft-u2K7kO6ny-od0bi0-XniszZlBQ2_gZ1MkH6NrbXnnVBORvaNf4PMHZFcYuNJjrSF0EzFhb6uMPFKYiwMDy_mrU_he-sftkoMlg6Krf-7IO9Mzb1nDnNiWqnEA==): 
  - [vinetrail.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtJ1i6mkHSOWZQnLwMJcx8mqDRg64uQdd0eW_KGThVZxoxegNH59xc3Mc3t-osVcfTmhv-W2mkOOvJrHqWSiE73STCBwNJNYEN-Wyz9lqN0xuIsC5H_lDDN9ssSzkGXHxOb1FNxmjYiHSQet7Izap9HOTOKuztWsNq2BwZhHp-X2wF8Aci): 
  - [marquis-wines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn74OEslZAoZVzIZkmGTD3dT2v4eCLGMOVYMPFx6U0ZobjLTezXRMBaxHZ8F3mmXn0a8OXJdHUkGNTxjFYTd_rStVOmUdmocS3N43FDBL1a00eun-8up7h0hTYOHerfcjkkKQKPuc1OD9HfTU0sgxMZHvXa1O-bEM8Uo4R1alCj29mng==): 
  - [kork.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVQXIsxOS3TX8eZo3AWYjz7TuGakkNsdqyEwulOI4LJN-ovqkI_OGPeUZ2eUnRG7Pt6csaLBLPJohdXAh_VURB3x7M-Se24r4HdXbUfPCeiuM1jufXmqHth10arwA6akqMG9EiHahPmclGktNd_Wi-gJ4vSPN4F3O1k7SZ1Nl--LWpFW6wH5uuXTrjBmP30ZidD6Ev6yWXdVLd_x_Box5805GKjbcsSTohw4TwGEQ=): 
  - [kork.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhOiR5Nrc9EhhF2jWWEXQfLqMrLDBr0qaKl2E34fe0cxG1dGaTaRJ1aoa7bTbL9QE2yWNHKXxmHSk-651Lqz3o-ifhAIhSxYXaYVgLJvjD5BSnuPCYRZNo8z5NzF1fboCHtGEoYGoC-dXEZnnYn5U4vBFvTxva8PsER1DjhV0uKsBKY8fpPVitcdzKoD2UfWjFkzHV6FPVZQ==): 
  - [marquis-wines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED7HvuOVZLnrvp7iQHYs94gzs-RtMS-ynYw_EaaczxRelsh9Ag4SC_YtnaK1XXn6iyb0mPWxLekENzm9DVpjP28t9QxgS8bB2yzq8q5WAKYkEk9kDtLA-1F4SD48vAtwjrQOUG7hKIYP9kr2PbxiGzj1Qaz9dPusHXtcl_GYzZl6a1mOw=): 
  - [gourmethunters.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeloXhoKo8PqxWZrnpTwrvDwTrTrVqy-ms23iG0ti_Q1s4tlhD1C1S80T-ibpubGTu83AVDoFUnIv8wHPNS9KOr89jDp3DHp9qq5yXodnmMVwTST2SCBhchP1-OBI_hFU0BQj8o3X6o2FxXxX8HtTKbHHRQK0gFA==): 
  - [zachys.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEYeyzFCcYvCCyGpxcFi8SAUc7XcwZ8Np4NvqvT4wdVsFar3Mf0UFm-yB6Q9SFS7FdX8q-A_MSYEapib12thC1-9WCvtW5tJizwLZ5-2R0Es4punyw702FZtRel1DqVDo_bcokhypLERfz69Ni3i6y6AE6NF87vlE1gpiG): 
  - [hmbwineandcheese.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzWnWXfwH7QseKhWBKaFBU18ZIz4Kqcpn7bmE0dJL4fud0QrZ0HK2X2rlrqwvsMqNCsQVQNgcwJoWldw6n3xQmmAq91fbdElbKcQMweRlvG2Bz0oTO0dcAwGwYHWYvVZgLhK1u7mgaaWjPwM4n40bUbH_HQ_Ld_PFxs1w91RCJjBYF4nYEgwILmXK6Uw==): 
  - [hmbwineandcheese.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXgB4pj1hXpih2TPEhCXQvRlDLBf9IauicODfMq0cPGf0jjNOOGUCUlzPXY3qCWpAvbX8OkGt4HF3xIW7CyL71u4KpwJmGqO5mohQlKWO-jEUrVF_NCCnxkGFzKV_eo9Q5m8Zmi7QftsZ0l3ZcihSXoiri0aqsZbrPRRuxDO_R05U5hYv3MhKByUM7): 

#### search_web_grounded_tool (status=ok, 13 results)
Search answer: Martin’s Lane Winery in East Kelowna, BC, is highly regarded for its premium, single-vineyard Pinot Noirs. On **WineAlign**, Canada's premier wine review platform, the winery's portfolio is regularly evaluated by top Canadian critics, including Anthony Gismondi, David Lawrason, John Szabo, MS, and Michael Godel (Godello). 

Key WineAlign review scores and summaries for Martin's Lane Pinot Noirs include:

### **Martin's Lane Naramata Ranch Vineyard Pinot Noir**
* **2020 Vintage:** Scored **96 points** by WineAlign co-founder and critic Anthony Gismondi. The wine is celebrated as a textbook expression of premium Naramata Bench Pinot, showing great structure, depth, and polished tannins.
* **2017 Vintage:** Reviewed by Michael Godel on December 10, 2021.
* **2014 Vintage:** Reviewed by John Szabo, MS (May 23, 2018) and David Lawrason (February 11, 2018). Critics noted its floral nose, ripe red cherry fruit, firm tannins, and excellent structure.

### **Martin's Lane Hieroglyph Pinot Noir (Naramata Ranch)**
* **2020 Vintage:** Reviewed by Michael Godel. He described this single-block, south-facing Naramata Bench Pinot as exceptionally stony and phenolic, highlighting its spontaneous fermentation and 80% whole cluster maceration.

### **Martin's Lane Fritzi's Vineyard "Missing Ear" Pinot Noir**
* **2018 Vintage:** Reviewed by Michael Godel. He highlighted the wine's 70% whole bunch natural fermentation and "semi-délestage" technique (fanning over the cap to polymerize tannins), calling it a testament to winemaker Shane Munn's meticulous style.
* **2017 Vintage:** Reviewed on WineAlign by David Lawrason (December 8, 2021) and John Szabo, MS (December 6, 2021).

### **Martin's Lane Simes Vineyard Pinot Noir**
* **2018 Vintage:** Reviewed by David Lawrason on August 25, 2022. This cool-climate, north-facing South Kelowna Slopes Pinot is typically noted for its fresh, elegant, and savory profile.
* **2014 Vintage:** Reviewed by David Lawrason on February 11, 2018.
  - [dreyfusashby.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgSVbXFXa7JxWCJfbr3eC6Y9X1wcDakb5OXOI_w3pxywt-Vv42hMOYXBog6SA9o82tMSaGkEMNzZO3EOJSR0Mik70--B0UtiCxAsZie8PBt9bIJC8r3bL2W6nEPco-ev0Y): 
  - [martinslanewinery.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3OjXG90F_tYu59GNVpXP7JhNHP4GFrOjEAiJlbRCsnVKOVcXyWlxZUX-adRx9z4580INTh3XYJxWBDeFGmoE5cm7_6w7LJgMaoTKdhSyOH-o7zI_CLEfBjfPU0W8=): 
  - [markanthony.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2OSI66m-VElXq3JIT0CdasaXI-2vYpOyz85qkY-W8QCWleGfaERmqyYL6ZZDHtREr_teCeYZbjwaHqvfozY9Wt4uGochGrF4apQalLH-qEwo_cD8Aj4rxaPrakCwNcrCiPi0=): 
  - [cellartracker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtdqnbDH7p8cPrho8vLkS_lDadgwMEXEXRNia9Q-mLedYfGsFSFDmXxC4psG-174ttMvYv-rmuzWEaKcgkKrL7Y4CLuswVQ_TV-mcKZtChaggl-AFJlgStuT_Vb283VmohnZTcDQmZKk5Pdal1-w==): 
  - [cellartracker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSokrIDNRzJJJgdewCHyp7X79z0faT8dHNq2DWeMU2XxGOqyxa9hdRCpNLPobD759WdzYunzf4QwDYx4lEWv46e3yRZgZo9ogAmVox4Cey9GCgpYQydKvM78DpYfaneNB8-PKidK2X-DdbdCBsVA==): 
  - [greatkitchenparty.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqvTABkhm8Pd27TiqDJHlkwHOrm8sqSl7QrbAw6Ia3SKMFr4uZShQ7xdzscPQ9OqxFaZbYUgJU5-ugCscvXBnv5HaBrQQfKIN4n0wZ9TSA37hdT96-Vr5_QQyXNnbi-G9Mhq-vg_lPGJTcRjAaQYwLvl51do6zsWVIbtMfj_QOmBmu): 
  - [quercusvino.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6RCyWoDX45VMyd6QgHwGipYl4teDiv9OrJsRdneK_Ipz7chEb-cBjLITBYM-lBU9fHZa7rwjFiM24jP7C2UnQEcf7JHMtygwgoSOe3fl5wiFTekUJv1GtMGMn_RJT83fYsAfDyiQDUQax1dcRzBTSeHIR_eGPf8X-KScUtRqThhSEYCzCMg==): 
  - [cellartracker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG80ES5RFiYkL2PwK3-T3G6fAUvZ_HG87pc0KjCjCjkYmlFwj-zat04NUYxsPsMf_69oIOG-77zPw2wQp_yXL-dKuc2NnhpdnIeA7ldZhlDEkpar9_vESSPc-6JBuUepiq877i2ijCXxqikDSsWtQ==): 
  - [godello.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIDJaiKcRGjTn9g7dyDZCCqgs3k6d3iesq9IXcEIfgnxcN6Tz65QaTsaqcbzY_Zvcy3fx_nBTUB28FUuSeW7ZR-mPu0ooqmdW3A9Q73hKP4EtQFH8ejGMH6ObYr24Q1SJUVJaSd2C6GNQA_kcqnvH7VUtUYQd1EfQlTPgNzP4i): 
  - [godello.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg8yVsStonv6ZH6F78ss4QLnUHz3NST1zNmqO-tNeNVQAwVaQxjWvmJWHWxkmrZhPGYXMIVtRQ6nuvJ6_9bYseB45xOSAVuvDzd6dx_a2LEpRhi60CbriT9o-TRf-ejX2rk-39As_0nLRuZrlj62BQQJKwTp7B8QdSy6rEdp3ahVIALIqFivYIkC_ASA==): 
  - [cellartracker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqv7DjlufX0jJsNhLbzhoaW3lsSMfH3GPFuSh1YmT-DYedLnKT2Ed_q7RLJcQpqKMsfy8bXRWR-DzFpWJc02bAQib6UzVf-FHpszyylTHkfGvim1btridihMI_hUcn0eAsr2vXvwck6uuXBzt2rA==): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKiYBjgR148nPWhjDNYt1kspACC-xmksbdhg-QOZGllIWqzghYwMkWmiD42X9-cCXEwvEgVxc0Qt8sMTSnF-MjLZuQ5-wNAjt0HphUQahwN5pgHgabjSzwziHoQhBj0C4JObqb05tuLL54WRiIuLVLdaM4FMYF0rIyB852iX7VlSuwX2zGgnCXdsmdlZMsYpfnrjgJ8L1ty6LfngVDwP0LGenZ): 
  - [cellartracker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSsY6EfSY5L7pP6LMOvMKfVIWwP-IpeVAX-24-P3iKt7CCqNGiYMUy3rEx5dI7-Jqw7gLiRVDWe0a73OjhJXe9fNk1UxdNHeUxx245udPyrN2IXMwmZrTKFP9gc9Ssuv-2g4R-BmxdwhK6giQOTA==): 

#### search_web_grounded_tool (status=ok, 10 results)
Search answer: While there is no specific beer named "Burnaby Dubbel," **Dageraad Brewing** (located in Burnaby, BC) is famous for its Belgian-style dubbels. 

Depending on whether you are looking for a classic, malty Belgian abbey ale or a complex, barrel-aged sour, here is how the flagship dubbel from **Dageraad** compares to **Strange Fellows' Reynard Oud Bruin**:

---

### 1. Dageraad Brewing – Brune (Belgian Abbey-Style Dubbel)
* **Style:** Belgian Abbey-style Dubbel
* **ABV:** 7.5%
* **The Beer:** Dageraad’s flagship dubbel, **Brune**, is brewed with Mission figs and fermented with European Trappist yeast. It is bottle-conditioned, meaning it undergoes a secondary fermentation in the bottle for natural carbonation and added complexity. 
* **Flavor Profile:** Rich, sweet, and warming. Cody Lobreau of *BeerCrank.ca* reviewed the beer, highlighting its prominent caramel sweetness, nuttiness, and deep dark fruit notes of raisin, plum, and fig. 
* **Accolades:** Highly decorated in the Canadian beer scene, it won **Gold** at the 2024 Canadian Brewing Awards (Belgian-Style Dubbel or Quadrupel), **Bronze** at the 2023 BC Beer Awards, and **Bronze** at the 2022 Canada Beer Cup.
* *Note: Dageraad also brews a seasonal dubbel called **Sri Lanka** (7.5% ABV) made with tamarind and Sri Lankan kithul treacle, which offers a more exotic, sweet-and-tangy profile.*

---

### 2. Strange Fellows Brewing – Reynard Oud Bruin
* **Style:** Flanders Oud Bruin (Flemish-style Sour Brown Ale)
* **ABV:** 6.5%
* **The Beer:** Brewed in Vancouver, **Reynard** is a sour brown ale blended from several vintages aged in French oak barrels for up to three years. It is typically released as a limited-edition vintage.
* **Flavor Profile:** Sweet, tart, and highly complex. *Mike's Craft Beer* reviewed the release, praising its intricate layers of oak, cherry, dark fruits, and caramel, balanced by a distinct, vinegar-like sourness and earthy undertones. The brewery notes that the extended oak aging contributes subtle vanilla and leather aromas.

---

### Summary Recommendation
* **Choose Dageraad Brune** if you prefer a traditional, comforting, and malt-forward Belgian ale with rich dark fruit sweetness and no sourness. 
* **Choose Strange Fellows Reynard** if you are looking for a tart, acidic, and complex wild ale with deep oak-aged character and cherry-like sourness.
  - [beeradvocate.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0RIsCXaXVwq_pseieyP6un-etkH4d3c_48Fau5fmPo3DRICHkHFgT5XUdRCRhaI5X7ItUxXaCdYKSkVOx4vpxkzUHE6NQ0OnJ_4RXm2i3k5cXVINpOmD-1hSUwMflcsrFrTi-A94-kXuA6g==): 
  - [bcaletrail.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuozIKBCWneejjY8yKhuOBfcTHLXSD9q30_8t8A6ZU6h9Hn6DSFtGlFxZg4Vd8GsPRQQP4g6oy5WRVVLhNjlo0RbbgP7LjwlX6JAz9_S83ue2c9Sea3dK8plEuk6I0L-8ZW6xr4pB8suswQx0=): 
  - [dageraadbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDX8JR_pHRag73ndjJASlHat4MNHauf_WbJtzFB0Azq6Tod0sXhgnSPXzfMYjhp5obOTCWWH58qzmB-mUp_NaYrmDU8Q_CoKNMNX3UHtI6QN3LO89JZXltiVQMRT1EfOoXRw==): 
  - [dageraadbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVsc3V7J9b8uTNtU2xPgA5Dkiw-4Ty9bRl6hJNBmHWPuGFhGvtU8qUg2NB_4U2IfCck-ZHbe7au_pb5xLRxiPPTGtvwDld17uHmFmNDAJ2oJv6yRC4BQ1vUFHUbsbncJE01hBk91CzWRc=): 
  - [beercrank.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH024TrpOfGtUV10I8X_0aebyWviIu2pzoDPsG2eJAVhxbiiN4Ty9-KHLf6j_BEdRO9lR4aebzYriAoBYplbiLpfwPwjmmvdr_7lA7ORLvik1bSiNe4aC9V0Jmb6_j5OA1FmnPVR7RWNdd9XNaMZMDfRRhDeT-CoRBIQe_l9tjsoecRWud6iD_OqQ==): 
  - [dageraadbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtKElj-PaPXSyu42ZWBaO8yjHyGu-KQ0crwWyOTjD0RGPAWKCyHM8XplIiPQ9Ro-Fa8XW1wgPkKQkQanGQfpdH0i0R8jJHtgFCpEUxAHX7ewXwOMdnSFJXDXKaJ1pojyfM7PxS_ro=): 
  - [strangefellowsbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPRk00wffAkfNEVhuKJC2GZ4MRWooIRaEp__L_uFU3qg5dV5E0oYeR0i4fNBIQHx4LI4lt-6OvsRyha8un6FhnRMdnuQPAURzvySpbonaVpPDL2vHi8uWJcf6lp28aGOhYLBPQc81Wc5eVXwM2FkO4XH6-e__GJrJM-A==): 
  - [untappd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG24o_BXjvKsU93QfnrHXJeERcKush9cAVyWg3ZXc7b2Es5hK50PaCUfCnxJPMWfL3oxTpSXnDhqRqUOAhLT-2PPvcakFYb6JLR73-8Urk0AOZA01AgHfhddelTZlw4vtgfmjd1yKcGcFCMtRjxqrnT0w_Ex_qklsw=): 
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExnzJR5hQ7jXwCkkZFuPW9CYr9PaHVp6EpOJQfkRgUkBHMXMZAHKHAhDW81k2811Y9t-hPBEUDxoEANl-6wkvkaNtbxvcVml86rWJGFFdf7MWpJVu-d5PgPCA1aicjLYomoHQ0yB4DNTgM1xKyDdjBqASi-4qrrnxZsd57_Unh1QFkyayC6fp6YnUvvjeA8NWaF21-JA==): 
  - [beermebc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERp4yiJK0MMnGDVZhLIhxTCJH-7dz_lDv8m3ayjyHcQv-hjGH4dVty74If_J6wKjyPakrT5_5vWUkXmo3_kBo_XPR1O-jM78pj25rXdGA-JsvvvjexIFRrubju4W-c7pI4laIpXt1TTebBaUiX1B0Gq6K_NM2bp0A5HB8UiOj9KXQ=): 

#### search_web_grounded_tool (status=ok, 13 results)
Search answer: **Sheringham Distilling's Kazuki Gin** (now rebranded as **Beacon Gin**) is an artisanal, "East meets West" style gin crafted on Vancouver Island, British Columbia. 

### Rebranding & Distillery History
* **The Name Change:** Originally released as **Kazuki Gin**, the spirit has since been rebranded as **Beacon Gin**. The name pays tribute to two Vancouver Island landmarks: the Sheringham Point Lighthouse beacon (near the distillery's original home) and the cherry blossom-lined paths of Beacon Hill Park.
* **The Sooke Connection:** Sheringham Distillery was founded in 2015 in Shirley, BC (just north of Sooke). It moved to Sooke in 2017/2018 to expand production, and later relocated to a larger, 10,000-square-foot facility in Langford, BC, in April 2023. 

### Botanicals & Flavor Profile
* **Base Spirit:** Distilled from British Columbia-grown white wheat and malted barley.
* **Key Botanicals:** Bottled at 43% ABV, the gin blends traditional botanicals with Japanese-influenced ingredients. It features salted cherry blossoms and yuzu peel imported from Japan, alongside green tea leaves and flowers sourced locally from Westholme Tea Farm in BC's Cowichan Valley.
* **Taste:** The combination yields a delicate, aromatic profile with bright floral notes, soft citrus (yuzu and grapefruit), and a subtle, herbaceous green tea finish.

### Critical Acclaim
* **The Rum Howler Blog:** Spirit critic Chip Dykstra reviewed the gin (under its Kazuki label) in 2020, awarding it a score of **89/100**. He praised its unique, exotic character, highlighting a spicy finish of coriander and citrus, and noted that while it departs from a traditional London Dry style, it is highly enjoyable and shines when paired with the right cocktail.

### BC Market Availability
* The gin is widely distributed across British Columbia and can be found at private liquor retailers in the Vancouver area (such as Gull Liquor Store). It typically retails for approximately $54 CAD for a 750ml bottle.
  - [liquorexpress.us](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEUz1SakpJhwScDmsqr4OvEt4_7B_SvdqNcdRO-l7m_wrnqjYJLooI5cqv8c0ZYxcyDX4N1fHKSVwThGqxUngi1954KNKqRtmAZ4OcnuiFisQvrDAa0nk8nJpp-XqMo0vcqZPZ1cOLrQ-JHjyC21BIEsG7zAff): 
  - [bswliquor.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdgI3hpcSijyJ2Euk5NCNdEadvTA3ec0YC7XDOfX1h99tSmG6NadCpWhf6LqeH2rSzCkvO6QQkcQj4376KwLuze7KAtHyxe0EdcCIWQFm3DNYYxYSNAWqR_7xmKMVF0nMwjQxNkGSm9TTdk-7KFZwz1E1r): 
  - [missionliquor.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPNyfvi_ewyWc_2G2wUHR_P3IUtFes786b7oMHbAC3KCOLsuyWiWVIJIFqyGBhs5D2_z_9P0F4S0oacFlEpt4qxyjYU6L9zeu6GbqEffpnU9pe8aom0RXxxOTVqbQYSkKhaNtTScKSfr9YguD0S9lu2O8aFLluoaD4G6-9Ew==): 
  - [therumhowlerblog.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGwCg0rp_CwjBk8LlAduuXnsjSxaYWKSaI0UyOrTifetD34KHGb-GfFBN516FPo25O4p3YjWE_TmbVNE2bImKvGCfzfw0rKGFm8BNRLbAg1tVJVvY58o65Ta1oiE1Xx9aTh7VknoIPmGzNOVDiuhwmSL5Ez9Oqp7eSEg==): 
  - [scoutmagazine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6PxuIWTpXJ72YGs5otHkWRFeTuljGAN7F46qbzU3vymW42YEk-3biVrrwa_QrlEgGQ7g71X6xRTU1oXzYZQ9zSl6CBe7hHgtAs-IMcE9LWvD6vMD8qyzbVHM4egjj_9FE1P2yP29qRyhVhRrpRQCwqg==): 
  - [timescolonist.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsgsDgHrcq0Y7h_XiQQyG51YD3SuJwzMEUXmlDsxvJDtjZe_YenQYR85B9lO7a9Vx-05ebyFFp670bJIySkCZRFJeMubg_0tnWDnrrgHRsCFiANiuMbOXCmNKUpcgPGNoarQ_Aob3IwQACKOvqxD0FCi60Sl4dmZBA7bfybZ8DT1E9v8RiTD-RIcQ=): 
  - [vicnews.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQFP2ihtf-TfrZxfIrSE-DF3gL8c9wOk6RTnabYyqbMlwaHN-ES5_EnUZdRIo2Df317xQYrxUA_Nu6HISi_j2zDvjuww7b076fFB_xMo3Y_eT5tj89ruEqdJjpcE8JjwhhUHovA11C9eZWsoCxGlpJinraqAsoOVe19_5v_bLLpPWEYWRSpnz57OC3weDwNAEYOlfW7I4fqisx52kLzw==): 
  - [biv.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEji-njUbZMU1KITK1QGInJ_vkTMZ_uwKu6H8iwFSuxaRoZn_bABWK6120DEaRSVNpJXbSNFdgWny7i70Gjx51mxCpq0XXWLuDyQ46JBVSd4TaVAs1fbHGbjfPHeAzqkcF_P3SFq8b_M5o1yq60K3Nnigdmen8cU3wyiIltbBeDScpdVdrTgbVAmY5cfcqPafBsuMwvxunR2x0k82nZbj98hP0q4KS7UH0k8Ur9x5ushpRFl2aJcnzLPhcQAg==): 
  - [langford.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWRT4RwbkpqEBUWUDOyIEpyEzzPIVSkFuptg3pYKbL0R-s531-Y88AxadQG5Jfxn5TcxUu6cODIXsEuUG6eIRzPUBDOWifBt4v9XT5crkGGENGFBuV4b9BpVw_Wlihx6qui6xIevNRpdBgnCMxvCgAltoRtBPylzUQU3Gs4yk7HSfFLjKmkSYlZTVFyrh1t4-LRhHq3vtc3lo-AbnoKtCTYs0=): 
  - [therumhowlerblog.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsoImy64yUpBpz4FACbv8Pxm52AJfLGblc8FAzWy7MNfcB3PJ3Wpu9koVMmamk_yXswQNgMULuSz8Y3TYe2jVoLpDVTD0Im6IMLUm93FWdZA7ViHLQZ3pjFErQ3CujFefaYUX8iGEkeojcJjxJavzWX3H-nla9ATt3fdz-rjlBeQ==): 
  - [kensingtonwinemarket.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp8F3vPVYYxzUU10Wlz3kiZ7h5xgWs3e-qY7-cFLNQwrcw4k8zTN5Sb-EXcmtXEudjhRQ4Xwr9HEj_-B1hBlYZPuuxGWbgDtBoJO1XZyMvU-3bj30zYPbxBXaR0U_pyRbyanTg2pHT5FhdbekYuZmQOYZ5U973rhZBDbP1DwgRsv6RiR4=): 
  - [sheringhamdistillery.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN8owC5SMuaRmG7A4Wy3q9Zz5jHFv4QaiFmIfq9iRVvG80jSElFYUQjCNJl5sqIlDKlmtyOztMOBRs0ZWgQV8a2w82nhRJMqQW2vXuBW9veZrCHPBPzJLPhm8Kr2OZVwf0I6KxdMvISOh9iPH9e4VghQkZrVliYBfmAFGevtdssa14PfTSH6f5DhfUtA==): 
  - [gullliquorstore.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnJx-MsIH9gnXKevaHpQWHhjB_pR4_OrnjCtpwMni_n3BjrFI3UJP5xIDxNA2OiKoQBvMdhw2sHMTMiz3ainUCtCHH59rfp5NIzkr1X-oIO8cnv28nDm44PYSeE3CAiWvlCDaaTHYNFSHQ1bkB6AZgDziNv7mlLA6D): 

#### search_web_grounded_tool (status=ok, 16 results)
Search answer: These two sakes represent completely different styles, origins, and flavor profiles. Here is a comparison of the local Vancouver craft pioneer and the traditional Japanese classic:

### **1. Artisan SakeMaker "OSAKE" Junmai (Granville Island, Vancouver)**
* **The Story:** Founded in 2007 by Masa Shiroki on Granville Island, Artisan SakeMaker is Canada’s first local sake winery. They produce small-batch, unpasteurized (*namazake*) sakes using 100% Canadian ingredients, including sake rice grown in BC's Fraser Valley. 
* **The Style:** Fresh, lively, and unpasteurized (*Nama*). 
* **Tasting Profile:** Light, crisp, and off-dry. It features bright, clean notes of pear, melon, and citrus. It is crafted to be softer and less alcohol-forward than traditional imports, making it highly approachable for white wine drinkers.
* **Best Pairings:** Delicate West Coast fare, such as fresh oysters, sushi, and local seafood. 
* **Price & Availability:** Typically around $16 for 375ml or $27 for 750ml, available directly from their Granville Island kura or select local BC private retailers.

---

### **2. "Tengumai" Yamahai Junmai (Shata Shuzo, Ishikawa, Japan)**
* **The Story:** Brewed by Shata Shuzo (established in 1823) in Ishikawa Prefecture, Japan. Tengumai is world-renowned for its mastery of the *Yamahai* method—a traditional, slow-brewing technique that allows wild lactic acid bacteria to develop naturally.
* **The Style:** Earthy, rich, and deeply complex. 
* **Tasting Profile:** A pale amber pour with a distinctively funky, mushroom-like nose. It is full-bodied and savory, offering rich flavors of butterscotch, walnuts, and honeyed mead, balanced by a robust, mouth-watering acidity. 
* **Expert Review:** Writing for *Business in Vancouver*, sake specialist Mariko Tajiri and local sommelier Iori Kataoka (of Vancouver's Yuwa restaurant) likened Tengumai's funky, yogurt-and-mushroom complexity to natural wine. They recommended serving it warm (around 40–45°C) to complement rich dishes like truffled pasta or aged cheeses.
* **Best Pairings:** Rich, savory dishes, including grilled meats, yakitori, mushrooms, and hot pot.
* **Price & Availability:** Imported to BC by *That's Life Gourmet*. It is a staple on local lists (like Dachi and Zakkushi) and can be found at private retailers (such as JAK's and Everything Wine) for approximately $44 to $59 depending on the specific bottling.

---

### **Summary Recommendation**
* **Choose the Osake Junmai** if you want a fresh, local, easy-drinking sake with clean fruit notes to enjoy chilled on a warm day or alongside fresh seafood.
* **Choose the Tengumai Yamahai** if you want a bold, traditional, and savory sake experience with plenty of umami, especially if you plan to serve it warm alongside a hearty dinner.
  - [urbansake.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyvTGGVPYJIauGFsx-0MkWDpoGjzp83GcLq0kFwD2JHGW4C2fpJUspS7gHYEV4IIN6_g6WAjdyD9JYqZlkIzNUhs9xRuan5ToCp_ygKZeUdMgSiykYMjYzh-rdix_ZIyIQ03Xw7l13WPKc0xh8ewF7wjFx): 
  - [winebc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyFfVuN15FDUKAq4pSKYmIlPnaGKzWxGIKKEevDxtn4T2ZBNOtZOAXJ4vtVHEfCzIM2AyUhfdPAYZJGrhLr0HkXvQvi6hCtSf6fIssXo34WVsSnvCZs4Ca_ayvViY1qyemLSSODJ9tOrGGyrl63gNTwhCqax2LDs4=): 
  - [eatnorth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaovfoBddXNdetWAm_5c9YTlnbEfgB4n6QVhtJPbAcQPkSJgwIfPp6GeusUNE0vggbuuNso0CFwP0GoWRF5LkyTQuZcW8xsY0CmptG0_72KwqxmyLM-sNnINEImLkXF1TF3Nk7I0Ihk6vi8PoKEQDHAXOT1VPXaC-Ke0hqZKLBiSE3a1mn0ZCfsQ==): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5PGzl_ue_wFIUE9a6l9AQ9LoTvVV6XJVroIgaiJR7xH52qOjSUwxrbqgDrzg3X0p6fSsLdEvU_TgydpRd-TBc3Ad2JhGd4tTQWXuWuxhoGxwc9KMwZ9Mi9hOg5SthI2T-PKgp8RD3vKCS): 
  - [myviewfromthemiddleseat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhTpkC2YZpIlTcwaCnp8EM4PI3INrkwJlb0aR01VpdZG_h2YjXtIvzh3jB4PZsdBiaZFDjvCQ9MOiduUneYkvgGT8q_Y9jaX4Li6K3sOaixGaBDPR0cekq8Y65NrXaFvnLJiIGhNhFpz116u-ZNNoVbA1cAEbT): 
  - [wixsite.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPa3qb8FT6VukLjVEbzqyNIm4x728Jq9venMZfoXVI9AcvD6n1exaRl78Z_HsbTuXQdBqDcBY9cS2OJo77JbJMTpzKY9wjSNyKmvXjJzzUWBABWjC94xOV4Z74HPH66iqfVpHC30fPKf4=): 
  - [mmsake.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmixAJ-N75Ouc7WvGPbeihs0ROfg7v-PWjhrzMPbSn53STrYmrmbFS7-QfZHoG_ZyiJ-vk8PektRr7SbZ1potiiq3wkPNoDkzThl6d6t1OJC__U6LP_pd23lRCOJlfGY0JGhgD769yL6cTMeznUgAtTS_yeNwy4HmYw5UBU7DFKVDGvQ==): 
  - [dejavusake.com.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEztdSFmwpGaRPXc1lC7cUovqOT9YLJMQHG3dp7zqJDzKRpRDdaIv6wUkRwFBNLPB4mVdqxHNM7j7ICgLnFskQZK3NKjY6JnLYdIgHvMfaVUPs3kGCwc7QtClVuAdro): 
  - [theartofsake.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJptevuLUc0EG7f9kFyJC95IxYUOJwXuaeMeJFm-cdFbMQP6N8FKkDzdA41PayV64Vl1uTdXOTCfEKCZdfxtdcSdSKNH7BsKcW4HrYEjpViiz8lvDNKOuMZ8w6JVPLRAgh49VvVPeVTw==): 
  - [biv.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwWDohjN1ByVDQ5L9YAIDR6V5NLnYxpZPrg6x0LqMQBodcyy3Aimh7g0Kv8dheDEAP_FH5agb4hnu9PN5PjZqiryTVWCp-5gb0V3JmmdA_ujka_aZslQ1xFQmrBfAzeIB0MzAkHwQpcB6zBea6Qalw9ZZxvaFisf2sJC2Rtw66floJKFAp89P--c=): 
  - [kenshinsake.us](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpeimJmj6VlvF5tWeMA4bcfRfbNbBcKkfzRjv2CMy0tNKsS739VUTcU1BJqL3g_RcZBr_5U16JS9K8sNepRMuiJ9HrkgkP0xWyVdh3yQq7-bljB4nxQjvI7zY2vnjtLIN98PWP): 
  - [truesake.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv5_Ur_10LsgwbcP_ZGD4DytToWOjqKXl233vsfwOuerX_T4RPhEwZspc42bC8_FRqp67unbe22IviCvDGXenzqIZSzCtMiz4ro-WCc8_3XyD698i6-APZ32gqVv6geOuBwpyn6w==): 
  - [zakkushi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZY6pGPehR1xMQUlj_qXIaFuyvaqfUouwW-pXmuPEKhfo_lbi1nEVz8vqz3oKWArG-ld7E0QBtHBglGKgEZVOdEHymRb4VF0lip8hrS3hQHzb9GktBvzf_vtuMn5UDQTA0dECdL5lNhw1je5sP): 
  - [montecristomagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJRyap75_of8XRBcDTtYjpsKHp9DPxiK43AyEG0oqX1tyg2PpYO7ojWamewsjZtUXSmYDMBBE8BXi4NCDQw6WU8f0JQDcLl67q2NelLB7IRYvOQXtOOS3ackqZEOT-OvdViK4rl8N20xty0GDgSrteoVxiaIgYqTIGr1L3NVJOlXweLfKiituNCeP0qhk=): 
  - [everythingwine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiiwllzuTtsGK8FbD94dv2zFqXZEKTTeCyCmMNBHR0X8n2KlWBYXDzj9xxc99Bs2ztwO9_qZ-RCIJr2IvIOobfhhHkxyCPjcKg7lOzzW5ufr6noZkdbV9J6S2uC6Nu1KAg98DXyiVGmEMJFEt6lYIREiPNzNjPCdFcLxMNqMflRV3NcQcUyWkm): 
  - [maff.go.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbAmKKC_KbYVU6zm5ny-T_uaq8nqauWsEnMpQTiss6PHgZTBljtNUSGpqPVcbYOs_lie0oTmA2DIgYQy3hA4_ur8qmzdORj-Mtaj7CmRT9ApHP-qLDEtFctvgkhxLa6h5LgtSRy5rdGgGJQne6Tf3DBCTZv1OGAF0j9dfJ1S5x35DFBUjS): 


### sourcing_agent_tool (status=ok)
**Sub-agent synthesis:**
Here is a curated selection of **Cru Beaujolais** and **Pinot Noir** red wines currently in stock across Vancouver liquor stores, complete with exact pricing, stock levels, and direct product links for easy comparison.

---

### Part 1: Cru Beaujolais Red Wines (Gamay)
Cru Beaujolais wines represent the highest quality tier of the Beaujolais region, coming from 10 designated hillside crus. 

#### **Morgon** (Known for robust, structured, and age-worthy profiles)
*   **Marcel Lapierre Morgon Beaujolais (750 mL)**
    *   **BC Liquor:** $56.99 | Stock: 42 units | [Product Link](https://www.bcliquorstores.com/product/141366)
    *   **Everything Wine (Vancouver):** $56.99 | Stock: 2 units | [Product Link](https://www.everythingwine.ca/marcel-lapierre-morgon)
*   **Michel Guignier Morgon Canon 2023 (750 mL)**
    *   **BC Liquor:** $46.99 | Stock: 268 units | [Product Link](https://www.bcliquorstores.com/product/210506)
*   **Lapierre 2023 Morgon "Cuvée Camille" (750 mL)**
    *   **Marquis Wine Cellars:** $102.99 | Stock: 2 units | [Product Link](https://www.marquis-wines.com/lapierre-2022-morgon-cuvee-camille-750ml/)
*   **Louis Claude Desvignes 2023 Morgon "Chateau Gaillard" (750 mL)**
    *   **Marquis Wine Cellars:** $51.99 | Stock: 1 unit | [Product Link](https://www.marquis-wines.com/louis-claude-desvignes-2023-morgon-chateau-gaillard-750ml/)
*   **Louis Claude Desvignes 2023 Morgon Côte de Py "Javernières" (750 mL)**
    *   **Marquis Wine Cellars:** $63.99 | Stock: 146 units | [Product Link](https://www.marquis-wines.com/louis-claude-desvignes-2023-morgon-cote-de-py-javernieres-750ml/)
*   **Clos de Mez 2018 Morgon "Chateau Gaillard" (750 mL)**
    *   **Marquis Wine Cellars:** $55.99 | Stock: 40 units | [Product Link](https://www.marquis-wines.com/clos-de-mez-2018-morgon-chateau-gaillard-750ml/)
*   **J Drouhin Morgon Gamay (750 mL)**
    *   **Everything Wine (Vancouver):** $49.98 | Stock: 4 units | [Product Link](https://www.everythingwine.ca/j-drouhin-morgon)

#### **Fleurie** (Known for elegant, floral, and aromatic profiles)
*   **Fleurie - Burrier (750 mL)**
    *   **BC Liquor:** $54.99 | Stock: 49 units | [Product Link](https://www.bcliquorstores.com/product/177402)
*   **Fleurie - Domaine des Marrans Clos du Pavillon 2021 (750 mL)**
    *   **BC Liquor:** $41.99 | Stock: 117 units | [Product Link](https://www.bcliquorstores.com/product/210509)
*   **Jean Louis Dutraive 2023 Fleurie Grand Cour (750 mL)**
    *   **Marquis Wine Cellars:** $75.99 | Stock: 10 units | [Product Link](https://www.marquis-wines.com/jean-louis-dutraive-2022-fleurie-grand-cour-750ml/)
*   **Domaine Gregoire Hoppenot 2022 Fleurie "Les Moriers" (750 mL)**
    *   **Marquis Wine Cellars:** $61.99 | Stock: 22 units | [Product Link](https://www.marquis-wines.com/domaine-gregoire-hoppenot-2022-fleurie-les-moriers-750ml/)
*   **Clos de Mez 2022 Fleurie "Mademoiselle M" (750 mL)**
    *   **Marquis Wine Cellars:** $49.99 | Stock: 54 units | [Product Link](https://www.marquis-wines.com/clos-de-mez-2022-fleurie-mademoiselle-m-750ml/)

#### **Moulin-à-Vent** (Known for powerful, tannic, and complex profiles)
*   **Moulin à Vent - Domaine Anita Coeur de Vigneronne 2023 (750 mL)**
    *   **BC Liquor:** $49.99 | Stock: 65 units | [Product Link](https://www.bcliquorstores.com/product/303969)
*   **Louis Boillot 2022 Moulin à Vent "Vieilles Vignes" (750 mL)**
    *   **Marquis Wine Cellars:** $51.99 | Stock: 33 units | [Product Link](https://www.marquis-wines.com/louis-boillot-2022-moulin-a-vent-vieilles-vignes-750ml/)
*   **Jean-Etienne Chermette Moulin-à-Vent Rochegrès (750 mL)**
    *   **Everything Wine (Vancouver):** $55.98 | Stock: 5 units | [Product Link](https://www.everythingwine.ca/jean-etienne-chermette-moulin-a-vent-rochegres)
*   **Domaine Jean Loron Champ de Cour Moulin-à-Vent 2019 (750 mL)**
    *   **Legacy Liquor Store:** $55.28 | Stock: 2 units | [Product Link](https://www.legacyliquorstore.com/product/wine/domaine-jean-loron-champ-de-cour-moulin-vent-2019-1-x-750ml)

#### **Other Crus (Brouilly, Côte de Brouilly, Chénas, Saint-Amour, Régnié, Chiroubles)**
*   **Dominique Piron Domaine De La Combiaty Brouilly (750 mL)**
    *   **Everything Wine (Vancouver):** $32.98 | Stock: 6 units | [Product Link](https://www.everythingwine.ca/dominique-piron-brouilly)
*   **Côte de Brouilly - Domaine Baron de l'Ecluse Les Garances 2020 (750 mL)**
    *   **BC Liquor:** $42.99 | Stock: 201 units | [Product Link](https://www.bcliquorstores.com/product/165636)
*   **Chénas - Pascal Aufranc Naturellement (750 mL)**
    *   **BC Liquor:** $36.99 | Stock: 318 units | [Product Link](https://www.bcliquorstores.com/product/287514)
*   **Saint Amour - Domaine Chardigny Clos du Chapitre Organic (750 mL)**
    *   **BC Liquor:** $55.99 | Stock: 5 units | [Product Link](https://www.bcliquorstores.com/product/283320)
*   **Régnié - Domaine Les Capreoles Diaclase (750 mL)**
    *   **BC Liquor:** $44.99 | Stock: 288 units | [Product Link](https://www.bcliquorstores.com/product/267201)
*   **Chiroubles - Steeve Charvet 2019 (750 mL)**
    *   **BC Liquor:** $26.97 *(On Sale, Reg. $30.99)* | Stock: 35 units | [Product Link](https://www.bcliquorstores.com/product/121135)

---

### Part 2: Pinot Noir Red Wines

#### **British Columbia (Local VQA & Island Pinot Noirs)**
*   **Liquidity Pinot Noir Estate 2023 (750 mL)**
    *   **Okanagan Cellars:** $34.99 | Stock: 28 units | [Product Link](https://okanagancellars.com/products/3272606-liquidity-pinot-noir)
    *   **BC Liquor:** $36.99 | Stock: 57 units | [Product Link](https://www.bcliquorstores.com/product/72570)
*   **Gray Monk Pinot Noir (750 mL)**
    *   **BC Liquor (2024 LE):** $20.99 *(On Sale, Reg. $23.99)* | Stock: 2,239 units | [Product Link](https://www.bcliquorstores.com/product/650385)
    *   **Okanagan Cellars (2024):** $20.99 *(On Sale, Reg. $23.99)* | Stock: 11 units | [Product Link](https://okanagancellars.com/products/5074445-gray-monk-pinot-noir-2024)
    *   **Marquis Wine Cellars (2021/24):** $24.99 | Stock: 18 units | [Product Link](https://www.marquis-wines.com/gray-monk-2019-pinot-noir-750ml/)
*   **CedarCreek Pinot Noir (750 mL)**
    *   **Okanagan Cellars (2024):** $30.99 | Stock: 16 units | [Product Link](https://okanagancellars.com/products/5057889-cedar-creek-pinot-noir-2024)
    *   **BC Liquor (2022):** $30.99 | Stock: 21 units | [Product Link](https://www.bcliquorstores.com/product/567412)
*   **Meyer Family Pinot Noir (750 mL)**
    *   **Legacy Liquor Store:** $33.30 | Stock: 6 units | [Product Link](https://www.legacyliquorstore.com/product/wine/meyer-pinot-noir-1-x-750ml)
    *   **Marquis Wine Cellars (2023):** $34.99 | Stock: 12 units | [Product Link](https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/)
*   **Averill Creek Pinot Noir 2021 (750 mL) — Vancouver Island**
    *   **Sutton Place Wine Merchant:** $35.99 | Stock: 5 units | [Product Link](https://store.suttonplacewinemerchant.com/products/4144447-averill-creek-pinot-noir)
*   **La Frenz Desperation Hill Pinot Noir 2022 (750 mL)**
    *   **Sutton Place Wine Merchant:** $42.99 | Stock: 18 units | [Product Link](https://store.suttonplacewinemerchant.com/products/5101285-la-frenz-desperation-hill-pinot-noir)
*   **Unsworth Vineyards Pinot Noir Saison 2022 (750 mL) — Vancouver Island**
    *   **BC Liquor:** $74.99 | Stock: 141 units | [Product Link](https://www.bcliquorstores.com/product/148952)
*   **Solvero Garnet Valley Pinot Noir (750 mL)**
    *   **BC Liquor:** $34.99 | Stock: 158 units | [Product Link](https://www.bcliquorstores.com/product/415565)
*   **Tantalus Pinot Noir 2022 (750 mL)**
    *   **BC Liquor:** $35.99 | Stock: 87 units | [Product Link](https://www.bcliquorstores.com/product/200881)

#### **International Pinot Noirs (Burgundy, Oregon, New Zealand)**
*   **Felton Road Bannockburn Pinot Noir (750 mL) — Central Otago, NZ**
    *   **BC Liquor:** $94.99 | Stock: 137 units | [Product Link](https://www.bcliquorstores.com/product/391511)
    *   **Marquis Wine Cellars (2023):** $94.99 | Stock: 9 units | [Product Link](https://www.marquis-wines.com/felton-road-2022-bannockburn-pinot-noir-750ml/)
*   **Bourgogne Pinot Noir - Louis Latour 2023 (750 mL) — Burgundy, France**
    *   **BC Liquor:** $39.99 | Stock: 1,612 units | [Product Link](https://www.bcliquorstores.com/product/69914)
*   **Bourgogne Pinot Noir - Joseph Drouhin 2022 (750 mL) — Burgundy, France**
    *   **BC Liquor:** $39.99 | Stock: 469 units | [Product Link](https://www.bcliquorstores.com/product/286682)
*   **Domaine Drouhin Dundee Hills Pinot Noir (750 mL) — Oregon, USA**
    *   **Legacy Liquor Store:** $68.99 | Stock: 6 units | [Product Link](https://www.legacyliquorstore.com/product/wine/domaine-drouhin-dundee-hills-pinot-noir-1-x-750ml)
*   **Clos Henri Estate Pinot Noir (750 mL) — Marlborough, NZ**
    *   **Legacy Liquor Store:** $41.75 | Stock: 16 units | [Product Link](https://www.legacyliquorstore.com/product/wine/clos-henri-pinot-noir-1-x-750ml)
    *   **Marquis Wine Cellars (2024):** $44.99 | Stock: 44 units | [Product Link](https://www.marquis-wines.com/clos-henri-2024-estate-pinot-noir-750ml/)
*   **Cuvée Dissenay Pinot Noir 2024 (750 mL) — France**
    *   **Sutton Place Wine Merchant:** $20.99 | Stock: 21 units | [Product Link](https://store.suttonplacewinemerchant.com/products/4680962-cuvee-dissenay-pinot-noir)

#### search_bcliquor_tool (status=ok, 48 results)
  - PRIVATO - PINOT NOIR | $30.99 | stock=41 | in 2 stores | https://www.bcliquorstores.com/product/96022 | {sku=96022; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=The nose is characterized by a ripe profile of sun-warmed black and ruby plums, black cherry jam, and subtle hints of tobacco. Its lingering soft palate, coupled with approachable tannins, enhance the elegance of the mouthfeel. 
; consumer_votes=0; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/96022.jpeg; certificates=["BC VQA", "All VQA"]}
  - BASK - PINOT NOIR | $12.99 | stock=2421 | in 167 stores | rating=3.3 | https://www.bcliquorstores.com/product/9330 | {sku=9330; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=Just BASK in 0g sugar per serving. That's one less thing to worry about, so you can zero in on the moment and savour every second. BASK Pinot Noir has aromas of dark cherry and subtle notes of spice. Well-balanced and perfect on its own or with a meal.
; consumer_votes=353; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/9330.jpeg}
  - PINOT NOIR - ECCENTRIC | $12.99 (reg $18.99) | stock=10893 | in 194 stores | rating=4.1 | https://www.bcliquorstores.com/product/335500 | {sku=335500; product_type=Red Wine; grape_type=PINOT NOIR; country=Argentina; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=A wine of an intensely red color, with aromas of ripe plums and violets, a medium body and round tannins. It offers a very light and fruity finish with good persistence.​
; consumer_votes=44; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/335500.jpeg}
  - PINOT NOIR -  ARE YOU GAME | $29.99 | stock=836 | in 65 stores | rating=4.3 | https://www.bcliquorstores.com/product/717465 | {sku=717465; product_type=Red Wine; grape_type=PINOT NOIR; country=Australia; volume=0.750; alcohol_pct=13.7; sweetness=00; tasting_notes=Aromas of ripe strawberry and forest berries back by a hint of subtle spice, with an earthy touch of rhubarb. Bright strawberries and red plum, followed by tart cherry and rhubarb, with a subtle hint of cardamom. Soft, silky tannins provide a smooth, elegant texture.
; consumer_votes=6; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/717465.jpeg}
  - XOXO - PINOT NOIR | $9.47 (reg $10.97) | stock=1190 | in 101 stores | rating=3.4 | https://www.bcliquorstores.com/product/47988 | {sku=47988; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=01; tasting_notes=Off-dry and medium-bodied, with notes of bright red fruit along with vanilla and a slight hint of cloves.
; consumer_votes=109; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/47988.jpeg}
  - QUAILS GATE - PINOT NOIR | $34.99 | rating=3.8 | https://www.bcliquorstores.com/product/585760 | {sku=585760; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=Expect inviting notes of cherry, wild strawberry, sage, and black tea. On the palate, this medium-bodied wine is well structured with a rich tannin profile presenting flavours of cherry and cocoa. An ideal match for late-season mushrooms or squash risotto, seared game meats or creamy wild mushroom pork chops.
; consumer_votes=153; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/585760.jpeg; certificates=["BC VQA", "All VQA"]}
  - PINOT NOIR BORTHWICK VINEYARD | $44.99 | stock=10 | in 1 stores | rating=3.7 | https://www.bcliquorstores.com/product/613299 | {sku=613299; product_type=Red Wine; grape_type=PINOT NOIR; country=New Zealand; volume=0.750; alcohol_pct=14.1; sweetness=00; consumer_votes=7; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/613299.jpeg}
  - BOURGOGNE - ROBLOT MARCHAND PINOT NOIR 2021 | $45.99 | stock=34 | in 6 stores | rating=3.0 | https://www.bcliquorstores.com/product/486566 | {sku=486566; product_type=Red Wine; grape_type=PINOT NOIR; country=France; volume=0.750; alcohol_pct=13.0; sweetness=NA; consumer_votes=2; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/486566.jpeg}
  - LIQUIDITY - PINOT NOIR ESTATE 2023 | $36.99 | stock=57 | in 8 stores | rating=5.0 | https://www.bcliquorstores.com/product/72570 | {sku=72570; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=Ripe red fruits shine through with a bright  freshness to the wine. Woody and spicy notes lend structure and round out the body 
; consumer_votes=1; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/72570.jpeg; certificates=["BC VQA", "All VQA"]}
  - UNSWORTH VINEYARDS - PINOT NOIR SAISON 2022 | $74.99 | stock=141 | in 9 stores | rating=5.0 | https://www.bcliquorstores.com/product/148952 | {sku=148952; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.1; sweetness=00; tasting_notes=93 Points, Gismondi On Wine: "Saison has a fragrant nose with local wild strawberry, some florals, and deeper dark fruit, that in Island speak, are always subtle. The finish is filled with spice and complex joy." (January 2025)
; consumer_votes=3; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/148952.jpeg; certificates=["BC VQA", "All VQA"]}
  - SANCERRE PINOT NOIR - PIERRE MARTIN | $59.99 | stock=65 | in 9 stores | rating=4.7 | https://www.bcliquorstores.com/product/311046 | {sku=311046; product_type=Red Wine; grape_type=PINOT NOIR; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=Delicate nose with an expressive, tangy red-fruit bouquet of cherry and raspberry. Medium-bodied, dry, and beautifully precise, the palate reveals mouthwatering acidity, subtle earthy spice, and well-integrated tannins. Sappy persistence carries the finish, giving it lift and refinement. It pairs perfectly with grilled or seared salmon.
; consumer_votes=14; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/311046.jpeg}
  - MERCUREY PINOT NOIR - MICHEL JUILLOT 2019 | $59.99 | stock=37 | in 4 stores | rating=4.8 | https://www.bcliquorstores.com/product/391373 | {sku=391373; product_type=Red Wine; grape_type=PINOT NOIR; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=Fresh nose tinged with fruit aromas generously sprinkled with hints of warm earth. It has flavours of generous proportions, rich and striking with ripe tannins that make this wine a very solid village.
; consumer_votes=58; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/391373.jpeg}
  - SOLVERO - GARNET VALLEY PINOT NOIR | $34.99 | stock=158 | in 16 stores | rating=3.6 | https://www.bcliquorstores.com/product/415565 | {sku=415565; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=12.2; sweetness=00; tasting_notes=90 Points, Gismondi On Wine: "This opens with herbal ripe cherry, baking spice, lilac, bramble, dried leaves, and tobacco before following through with autumn leaves, mulberry, and leaf smoke. Overall very savoury, quite long, and balanced, with an airy finish that lingers." (January 2026)
; consumer_votes=3; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/415565.jpeg; certificates=["BC VQA", "All VQA"]}
  - GEHRINGER - PRIVATE RESERVE PINOT NOIR 2019 | $17.97 (reg $19.49) | stock=83 | in 10 stores | rating=2.9 | https://www.bcliquorstores.com/product/430306 | {sku=430306; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=12.0; sweetness=00; consumer_votes=18; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/430306.jpeg; certificates=["BC VQA", "All VQA"]}
  - PINOT NOIR - INVIVO CENTRAL OTAGO | $29.99 | stock=322 | in 41 stores | rating=4.5 | https://www.bcliquorstores.com/product/531723 | {sku=531723; product_type=Red Wine; grape_type=PINOT NOIR; country=New Zealand; volume=0.750; alcohol_pct=12.0; sweetness=00; tasting_notes=91 Points, James Suckling: "Linear and predictable with dark cherries, warm spices and some dark chocolate on the nose. Medium-bodied with chewy tannins. Soft finish. Drink now. Screw cap." (October 2025)
; consumer_votes=6; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/531723.jpeg}
  - PINOT NOIR - STONELEIGH MARLBOROUGH 2018 | $21.99 | stock=1116 | in 87 stores | rating=3.3 | https://www.bcliquorstores.com/product/610857 | {sku=610857; product_type=Red Wine; grape_type=PINOT NOIR; country=New Zealand; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Immediately approachable. This wine has a deep, ruby red hue and a fragrant bouquet of blackberry, and dark cherry overlaid with integrated oak spice.
; consumer_votes=107; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/610857.jpeg}
  - PINOT NOIR - CONO SUR OCIO | $79.99 | stock=338 | in 31 stores | rating=4.6 | https://www.bcliquorstores.com/product/835470 | {sku=835470; product_type=Red Wine; grape_type=PINOT NOIR; country=Chile; volume=0.750; alcohol_pct=13.9; sweetness=00; tasting_notes=Bursting with expressive aromas of ripe cherry, wild raspberry, and juicy blackberry, this wine is layered with hints of warm spice and a delicate touch of tobacco. The palate is luxuriously silky yet vibrant, delivering impressive depth, fresh acidity, and beautifully balanced structure. Elegant and refined, it lingers effortlessly on the finish with remarkable length and finesse.
; consumer_votes=64; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/835470.jpeg}
  - BASK - PINOT NOIR | $36.99 (reg $39.99) | stock=1269 | in 137 stores | rating=3.4 | https://www.bcliquorstores.com/product/451790 | {sku=451790; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=3.000; alcohol_pct=12.5; sweetness=00; tasting_notes=Just BASK in 0g sugar per serving. That's one less thing to worry about, so you can zero in on the moment and savour every second. BASK Pinot Noir has aromas of dark cherry and subtle notes of spice. Well-balanced and perfect on its own or with a meal.
; consumer_votes=57; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/451790.jpeg}
  - PRIVATO - TESORO PINOT NOIR | $46.99 | stock=22 | in 1 stores | https://www.bcliquorstores.com/product/96027 | {sku=96027; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=This ruby red wine exhibits aromas of lavender and black cherries intertwined with toasty oak. The palate shows lovely acid and tannin balance which lingers with a soft, silky mouth feel.   Enjoy this wine now or age for a good 7 years.
; consumer_votes=0; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/96027.jpeg; certificates=["BC VQA", "All VQA"]}
  - PINOT NOIR - PEGASUS BAY | $60.99 | stock=22 | in 5 stores | rating=5.0 | https://www.bcliquorstores.com/product/607622 | {sku=607622; product_type=Red Wine; grape_type=PINOT NOIR; country=New Zealand; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=94 Points, James Suckling: "Dried strawberries, cedar and fresh rose petals come through clearly. Some citrus. Medium-bodied with firm, creamy tannins and a juicy finish. Lovely texture and fruit to this. Really nice to drink now but better in three or four years. Screw cap." (March 2024)
; consumer_votes=4; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/607622.jpeg}
  - PINOT NOIR - PURE COASTAL | $21.99 | stock=2144 | in 168 stores | rating=4.6 | https://www.bcliquorstores.com/product/708423 | {sku=708423; product_type=Red Wine; grape_type=PINOT NOIR; country=Australia; volume=0.750; alcohol_pct=13.7; sweetness=00; tasting_notes=Deep and dark purple colour with bright hues. Aromas of raspberries and plums coupled with baking spice and a hint of earthiness. The palate displays fruits of the forest flavours with fine grain tannins and silk texture. Smooth drinking.; consumer_votes=6; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/708423.jpeg}
  - PINOT NOIR - MARANTIQUA | $19.99 (reg $22.99) | stock=1389 | in 93 stores | rating=4.4 | https://www.bcliquorstores.com/product/275779 | {sku=275779; product_type=Red Wine; grape_type=PINOT NOIR; country=Argentina; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Marantiqua Pinot Noir showcases an emblematic characteristic of the wines from this region: a deeper color intensity than that found in other Pinot Noirs from around the globe. Aromas of red fruit, mostly strawberry and some cherry, stand out on the nose, as well as notes of red flowers.; consumer_votes=16; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/275779.jpeg}
  - BOURGOGNE PINOT NOIR - LOUIS LATOUR 2023 | $39.99 | stock=1612 | in 135 stores | rating=3.3 | https://www.bcliquorstores.com/product/69914 | {sku=69914; product_type=Red Wine; grape_type=PINOT NOIR; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=This is a classic, reliable, well-made Burgundian Pinot Noir at a good price. Raspberry and strawberry aromas and flavours complement a savoury earthiness reminiscent of beetroot. A clean, balanced and supremely drinkable wine, try it with barbecued planked salmon, roasted duck or wild mushroom risotto.
; consumer_votes=197; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/69914.jpeg}
  - BOURGOGNE PINOT NOIR - DOMAINE DE ROMY | $44.99 | stock=12 | in 2 stores | rating=4.0 | https://www.bcliquorstores.com/product/197451 | {sku=197451; product_type=Red Wine; grape_type=PINOT NOIR; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=This long-established family estate has produced a richly textured Pinot Noir. It is full of blackcherry and red-berry fruits while also having a good tannic structure that will soften and give shape to the wine. It has a refreshing finish with a delicate touch of pepper.
; consumer_votes=5; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/197451.jpeg}
  - ROCHE - VIG PINOT NOIR CLONE 777 | $27.99 | stock=1873 | in 110 stores | rating=4.0 | https://www.bcliquorstores.com/product/278372 | {sku=278372; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.1; sweetness=00; tasting_notes=88 Points, John Schreiner: "This Pinot Noir is beautiful, light red in colour. Morello cherry, cola, and five-spice on the nose. The palate boasts sweet pipe tobacco and an herbal freshness. The tannins are soft and dusty. Drink now or hold." (June 2024)
; consumer_votes=4; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/278372.jpeg; certificates=["BC VQA", "All VQA"]}
  - TANTALUS VINEYARDS - REIMER VINEYARD PINOT NOIR | $39.99 | stock=506 | in 66 stores | rating=4.5 | https://www.bcliquorstores.com/product/692960 | {sku=692960; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=9; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/692960.jpeg; certificates=["BC VQA", "All VQA"]}
  - WHISTLER - PINOT NOIR ICEWINE 2019 | $29.99 | stock=89 | in 13 stores | rating=4.0 | https://www.bcliquorstores.com/product/817841 | {sku=817841; product_type=Ice Wine; grape_type=PINOT NOIR; country=Canada; volume=0.200; alcohol_pct=13.7; sweetness=10; consumer_votes=86; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/817841.jpeg; certificates=["BC VQA", "All VQA"]}
  - CEDARCREEK - PINOT NOIR 2022 | $30.99 | stock=21 | in 4 stores | rating=4.0 | https://www.bcliquorstores.com/product/567412 | {sku=567412; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.4; sweetness=00; tasting_notes=This lighter style of Pinot Noir with good fruit concentration has loads of black cherry, raspberry and wood spice wrapped in moderate tannins and juicy acidity.
; consumer_votes=83; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/567412.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - PINOT NOIR - WHITEHAVEN MARLBOROUGH 2018 | $26.99 | stock=1062 | in 82 stores | rating=3.9 | https://www.bcliquorstores.com/product/161703 | {sku=161703; product_type=Red Wine; grape_type=PINOT NOIR; country=New Zealand; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=92 Points, James Suckling: "A linear pinot noir with fine tannins, sliced strawberries and hints of cedar. It's fresh and medium-bodied with integration and length. This is a fine example of subtle pinot at an excellent price. Drink now. Screw cap." (June 2024)
; consumer_votes=84; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/161703.jpeg}
  - PINOT NOIR - GIANT STEPS YARRA VALLEY | $39.99 (reg $44.99) | stock=537 | in 55 stores | rating=4.0 | https://www.bcliquorstores.com/product/89613 | {sku=89613; product_type=Red Wine; grape_type=PINOT NOIR; country=Australia; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=96 Points, James Halliday 'A 50/50 mix of upper and lower Yarra fruit; 35% whole bunches and matured in French oak (10% new). Bright crimson red with aromas of ripe raspberries, black cherries, wild herbs, and crushed violets. Silken and sappy with excellent depth and persistence.' (April 2024)
; consumer_votes=30; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/89613.jpeg}
  - PINOT NOIR LOVELY LILLY - SHELTER WINERY | $30.99 | stock=349 | in 29 stores | rating=4.6 | https://www.bcliquorstores.com/product/121564 | {sku=121564; product_type=Red Wine; grape_type=PINOT NOIR; country=Germany; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=90 points, Winescores.ca: "...It's a fragrant one--cherry and raspberry, cedar and dried flowers, cranberry and sweet spice aromas dominate the nose. It's dry and juicy with high-toned red berry flavours woven with tealeaf and spice. It's an engaging wine with good classic pinosity." (Daenna Van Mulligen, February 2023)
; consumer_votes=18; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/121564.jpeg}
  - PAYS D'OC PINOT NOIR - BOUCHARD AINE | $17.99 (reg $19.99) | stock=1017 | in 76 stores | rating=3.7 | https://www.bcliquorstores.com/product/143420 | {sku=143420; product_type=Red Wine; grape_type=PINOT NOIR; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Hearty and intense with notes of jammy fruits, spices and herbs. Friendly, harmonious and structured with round tannins. Black currant, licorice and black cherry flavors followed by a long lasting vanilla finish. A wonderful companion for the entire meal.
; consumer_votes=99; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/143420.jpeg}
  - PINOT NOIR - MONTGRAS RESERVA 2023 | $12.97 (reg $16.99) | stock=2063 | in 53 stores | rating=3.8 | https://www.bcliquorstores.com/product/391450 | {sku=391450; product_type=Red Wine; grape_type=PINOT NOIR; country=Chile; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Lively red with a medium intensity. The nose is dominated by notes of cassis and cherries followed by subtle hints of fresh grass. Agile on the palate with young, elegant tannins. The acidity is very fresh and can pair with seafood or vegetable dishes.; consumer_votes=55; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/391450.jpeg}
  - RED ROOSTER PINOT NOIR 2022 | $24.99 | stock=1408 | in 92 stores | rating=4.0 | https://www.bcliquorstores.com/product/533190 | {sku=533190; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Bold ruby-red colour, alluring fragrances of ripe red cherries and currants, harmoniously complemented by subtle notes of forest floor and clove. On the palate, a velvety texture and fine, well-defined tannins. Flavours of cherry, red berries, cola and hibiscus tea culminate in a dry finish.
; consumer_votes=29; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/533190.jpeg; certificates=["BC VQA", "All VQA"]}
  - GRAY MONK - PINOT NOIR LE 2024 | $20.99 (reg $23.99) | stock=2239 | in 178 stores | rating=4.5 | https://www.bcliquorstores.com/product/650385 | {sku=650385; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=12.4; sweetness=00; tasting_notes=CRAFTED IN BC. Aromas of juicy cherry, sun-ripened strawberry and a hint of earthiness. The palate is elegant, medium-bodied, offering layers of cranberry, raspberry compote, and a delicate hint of steeped tea. Well-integrated tannins. Refined finish with lingering notes of red currant and a trace of vanilla bean
; consumer_votes=6; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/650385.jpeg}
  - PINOT NOIR - SMALL WONDER BLOCK 3 | $47.99 (reg $52.99) | stock=739 | in 71 stores | rating=5.0 | https://www.bcliquorstores.com/product/677065 | {sku=677065; product_type=Red Wine; grape_type=PINOT NOIR; country=Australia; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=96 Points, Wine Orbit: "Immensely complex and alluring, the bouquet shows dark berry, cured meat, bouquet garni, assorted nut, and potpourri aromas. The palate exhibits outstanding concentration and depth, together with plush texture and compact tannins, making it opulent and robust simultaneously with a persistent, seductive finish." (December 2025); consumer_votes=6; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/677065.jpeg}
  - TANTALUS - PINOT NOIR 2022 | $35.99 | stock=87 | in 14 stores | rating=4.2 | https://www.bcliquorstores.com/product/200881 | {sku=200881; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.3; sweetness=00; tasting_notes=Dark crimson in the glass, the nose is lively with bright floral notes alongside cocoa and red berries. Rich notes of cedar, wet earth and graphite complement the aromatic profile. Despite its youth, the palate is showing beautiful complexity and nuance with swaths of red currant, cherry and fig spun together with a unique mineral expression. Lush tannins offer depth and structure and the expectation of a graceful development in bottle. Comfortably enjoy over the next 5 to 10 years.
; consumer_votes=118; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/200881.jpeg; certificates=["BC VQA", "All VQA"]}
  - PINOT NOIR - VINA LEYDA RESERVA | $13.99 (reg $17.99) | stock=1799 | in 93 stores | rating=4.1 | https://www.bcliquorstores.com/product/138982 | {sku=138982; product_type=Red Wine; grape_type=PINOT NOIR; country=Chile; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=A ripe and fruity pinot with a touch of fresh herbs to the ripe-strawberry aromas. Pretty round and straightforward on the palate, with a fleshy core of red fruit and a succinct, fresh finish.
; consumer_votes=25; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/138982.jpeg}
  - BOURGOGNE PINOT NOIR - JOSEPH DROUHIN 2022 | $39.99 | stock=469 | in 36 stores | rating=4.3 | https://www.bcliquorstores.com/product/286682 | {sku=286682; product_type=Red Wine; grape_type=PINOT NOIR; country=France; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=90 Points, Natalie MacLean: "A juicy, mouth-watering Old World Burgundian Pinot Noir from one of the most respected names in the region, Joseph Drouhin. Aromas of tart cherry, cranberry and smoke. Medium-bodied and smooth." (July 2019)
; consumer_votes=245; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/286682.jpeg}
  - QUAILS' GATE - FIELD AND FLIGHT PINOT NOIR | $20.99 (reg $22.99) | stock=2024 | in 103 stores | rating=4.3 | https://www.bcliquorstores.com/product/668257 | {sku=668257; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Lush aromatics & complex palate. This Pinot Noir has it all! Crunchy red fruit, cool florality, and the kind of savoury finish that only Oregon dirt can deliver. This is a wine you bring home to meet your mother. Pair with a bowl of cherries. A pot of Risotto. 
; consumer_votes=18; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/668257.jpeg}
  - PINOT NOIR - ALLAN SCOTT AROHA BAY | $19.99 | stock=1606 | in 112 stores | rating=4.4 | https://www.bcliquorstores.com/product/673693 | {sku=673693; product_type=Red Wine; grape_type=PINOT NOIR; country=New Zealand; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=Marlborough Pinot Noir, light in tannin full of flavor. Vibrant fruit drives a bright, fruit-forward style, with cherry, strawberry, boysenberry, raspberry, and ripe plum notes. Soft and supple on the palate. Serve chilled with tapas or cheeses, or at room temperature with charcuterie, duck, pork, or creamy pasta.
; consumer_votes=13; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/673693.jpeg}
  - CEDARCREEK - PLATINUM PINOT NOIR SOUTH KELOWNA SLOPES | $66.99 | stock=9 | in 2 stores | rating=3.3 | https://www.bcliquorstores.com/product/316971 | {sku=316971; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=This 2022 vintage is a beautiful and elegant nose of brambly berries, potpourri, and forest floor. On the palate, the tannins are fine and well-integrated. A beautiful energy and freshness underline the nose and palate.
; consumer_votes=6; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/316971.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - VIN DE FRANCE PINOT NOIR - BARTON AND GUESTIER BISTRO | $41.99 | stock=2 | in 1 stores | rating=4.0 | https://www.bcliquorstores.com/product/390391 | {sku=390391; product_type=Red Wine; grape_type=PINOT NOIR; country=France; volume=3.000; alcohol_pct=13.5; sweetness=00; tasting_notes=Purple red colour. Intense aromas of fresh red cherry fruits with spicy hints, tobacco and coffee notes. Long cherry pie and vanilla flavours magnified by hint of spices (curry). Rich and full bodied with supple tannins and a long silky aftertaste.
; consumer_votes=56; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/390391.jpeg}
  - PINOT NOIR - TERRANOBLE RESERVA VEGAN CASABLANCA 22 | $21.99 | stock=370 | in 34 stores | rating=3.9 | https://www.bcliquorstores.com/product/495595 | {sku=495595; product_type=Red Wine; grape_type=PINOT NOIR; country=Chile; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=From grapes harvested in our vineyard in the Las Dichas sector of the Casablanca Valley, its soft and bright ruby red colour stands out. With pleasant notes of fresh red fruits, the palate is fresh, fruity, with soft tannins and vibrant acidity.
; consumer_votes=45; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/495595.jpeg}
  - PINOT NOIR - CIGAR BOX | $14.99 (reg $16.99) | stock=5538 | in 173 stores | rating=3.8 | https://www.bcliquorstores.com/product/234901 | {sku=234901; product_type=Red Wine; grape_type=PINOT NOIR; country=Chile; volume=0.750; alcohol_pct=13.5; sweetness=01; tasting_notes=This Pinot Noir has a medium intensity purplish red colour, with notes of raspberry, cherry and flowers, combined with the sweetness of vanilla and caramel provided by the French oak. It is a silky and very balanced with a fresh acidity and juciness that make it very easy to drink.
; consumer_votes=169; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/234901.jpeg}
  - POPLAR GROVE - PINOT NOIR 2023 | $38.99 | stock=355 | in 47 stores | rating=4.5 | https://www.bcliquorstores.com/product/261691 | {sku=261691; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=Aromas of cherry marzipan, fresh raspberry, vanilla, and a hint of light toast. Bing cherries shine through on the nose, setting the stage for a palate layered with fine tannins, raspberry, subtle licorice, and a touch of minerality. A medium-long finish that is both elegant and expressive.
; consumer_votes=17; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/261691.jpeg; certificates=["BC VQA", "All VQA"]}
  - PINOT NOIR - FELTON ROAD BANNOCKBURN | $94.99 | stock=137 | in 17 stores | rating=4.5 | https://www.bcliquorstores.com/product/391511 | {sku=391511; product_type=Red Wine; grape_type=PINOT NOIR; country=New Zealand; volume=0.750; alcohol_pct=13.8; sweetness=00; tasting_notes=95 Points, James Suckling: "A perfumed nose of strawberries, sour cherries, raspberries, violets, vanilla and baking spices. It's medium-to full-bodied with lively acidity and fine tannins. Balanced and compact with a velvety texture and a bright core of fruit on the mid-palate. Long finish. Chewy..." (October, 2021)
; consumer_votes=20; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/391511.jpeg}
  - PINOT NOIR - YERING STATION LITTLE YERING | $23.49 (reg $24.99) | stock=744 | in 74 stores | rating=3.9 | https://www.bcliquorstores.com/product/616110 | {sku=616110; product_type=Red Wine; grape_type=PINOT NOIR; country=Australia; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=27; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/616110.jpeg}

#### search_everything_wine_tool (status=ok, 0 results)

#### search_okanagan_cellars_tool (status=ok, 15 results)
  - BASK - 3L PINOT NOIR | $36.99 (reg $39.99) | stock=9 | https://okanagancellars.com/products/3935720-bask-3l-pinot-noir | {category=W Boxed; in_stock=True; unit_size=3L; image_url=https://okanagancellars.com/static/custom/goods/131/000045/0000451790-6201.jpg}
  - BASK - PINOT NOIR | $12.99 | stock=32 | https://okanagancellars.com/products/3768136-bask-pinot-noir | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000000/0000009330-8943.jpg}
  - CEDAR CREEK - PINOT NOIR 2024 | $30.99 | stock=16 | https://okanagancellars.com/products/5057889-cedar-creek-pinot-noir-2024 | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000036/0000364875-3065.jpg}
  - CEDAR CREEK - PLAT EKS PINOT NOIR | $69.99 | stock=12 | https://okanagancellars.com/products/5127779-cedar-creek-plat-eks-pinot-noir | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000024/0000245489-4227.jpg}
  - CEDAR CREEK - PLAT SKS PINOT NOIR | $66.99 | stock=21 | https://okanagancellars.com/products/4315808-cedar-creek-plat-sks-pinot-noir | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000031/0000316971-2300.jpg}
  - CHABERTON - PINOT NOIR | $24.99 | stock=13 | https://okanagancellars.com/products/3896841-chaberton-pinot-noir | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000003/0000031322-6472.png}
  - GEHRINGER - OPT PINOT NOIR | $25.99 | stock=11 | https://okanagancellars.com/products/2643577-gehringer-opt-pinot-noir | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000053/0000534909-5137.png}
  - GEHRINGER - PINOT NOIR USA 2024 | $18.99 | stock=9 | https://okanagancellars.com/products/5019819-gehringer-pinot-noir-usa-2024 | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000033/0000334915-1724.jpg}
  - GRAY MONK - ODYSSEY PINOT NOIR | $34.99 | stock=20 | https://okanagancellars.com/products/3812156-gray-monk-odyssey-pinot-noir | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000059/0000593764-4450.jpg}
  - GRAY MONK - PINOT NOIR 2024 | $20.99 (reg $23.99) | stock=11 | https://okanagancellars.com/products/5074445-gray-monk-pinot-noir-2024 | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000065/0000650385-3273.jpg}
  - HAINLE - PINOT NOIR 2022 | $37.99 | stock=17 | https://okanagancellars.com/products/4681864-hainle-pinot-noir-2022 | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000029/0000296693-9652.jpg}
  - INNISKILLIN - ESTATE PINOT NOIR | $20.99 | stock=30 | https://okanagancellars.com/products/3410073-inniskillin-estate-pinot-noir | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000062/0000624767-4209.png}
  - LIQUIDITY - PINOT NOIR | $34.99 | stock=28 | https://okanagancellars.com/products/3272606-liquidity-pinot-noir | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000007/0000072570-5108.jpg}
  - LIQUIDITY - RSV PINOT NOIR | $59.99 | stock=11 | https://okanagancellars.com/products/4352201-liquidity-rsv-pinot-noir | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000043/0000431687-7563.jpg}
  - MARTINS LANE - JULIUS PINOT NOIR/RIES | $74.99 | stock=4 | https://okanagancellars.com/products/4301671-martins-lane-julius-pinot-noir-ries | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000033/0000337392-6619.jpg}

#### search_suttonplace_tool (status=ok, 15 results)
  - Averill Creek Pinot Noir  | $35.99 | 2021 | stock=5 | https://store.suttonplacewinemerchant.com/products/4144447-averill-creek-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000078/0000786657-5366.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.10; is_staff_pick=False; is_featured=False}
  - Benovia Tilton Hill Pinot Noir  | $124.99 | 2014 | stock=3 | https://store.suttonplacewinemerchant.com/products/4143336-benovia-tilton-hill-pinot-noir | {category=RED USA; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000013/0000131549-7833.png; country=USA; varietal=Pinot Noir; alcohol_pct=14.40; is_staff_pick=False; is_featured=False}
  - Birch Block Beau Soleil Pinot Noir | $50.49 | 2023 | stock=3 | https://store.suttonplacewinemerchant.com/products/5103142-birch-block-beau-soleil-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.10; is_staff_pick=False; is_featured=False}
  - Carmen Pinot Noir | $16.49 | 2021 | stock=51 | https://store.suttonplacewinemerchant.com/products/4229744-carmen-pinot-noir | {category=RED CHILE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000025/0000257659-2993.jpg; country=CHILE; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Cuvee Dissenay Pinot Noir | $20.99 | 2024 | stock=21 | https://store.suttonplacewinemerchant.com/products/4680962-cuvee-dissenay-pinot-noir | {category=RED FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000025/0000252242-8277.png; country=FRANCE; varietal=Pinot Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Divin Pinot Noir Non Alc | $29.99 | stock=9 | https://store.suttonplacewinemerchant.com/products/4862652-divin-pinot-noir-non-alc | {category=NON-ALCOHOLIC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000241/0002411651-6826.png; country=FRANCE; varietal=Pinot Noir; is_staff_pick=False; is_featured=False}
  - Divin Vigneron Pinot Noir | $45.99 | stock=6 | https://store.suttonplacewinemerchant.com/products/5229979-divin-vigneron-pinot-noir | {category=NON-ALCOHOLIC; in_stock=True; unit_size=750ML Bottle; country=FRANCE; varietal=Pinot Noir; is_staff_pick=False; is_featured=False}
  - Florian Mollet Roc de lAbbaye Pinot Noir | $32.99 | 2024 | stock=22 | https://store.suttonplacewinemerchant.com/products/5068270-florian-mollet-roc-de-labbaye-pinot-noir | {category=RED FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000025/0000258506-6717.png; country=FRANCE; varietal=Pinot Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Francois Labet Pinot Noir Ile de Beaute | $33.99 | 2023 | stock=10 | https://store.suttonplacewinemerchant.com/products/4217449-francois-labet-pinot-noir-ile-de-beaute | {category=RED FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000009/0000093331-3549.jpg; country=FRANCE; varietal=Pinot Noir; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}
  - La Frenz Desperation Hill Pinot Noir | $42.99 | 2022 | stock=18 | https://store.suttonplacewinemerchant.com/products/5101285-la-frenz-desperation-hill-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC234112.png; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - La Frenz Reserve Pinot Noir | $52.49 | 2021 | stock=8 | https://store.suttonplacewinemerchant.com/products/5060692-la-frenz-reserve-pinot-noir | {category=WHITE BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC409060.png; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - La Grande Colombe Pinot Noir | $29.99 | 2024 | stock=8 | https://store.suttonplacewinemerchant.com/products/5102883-la-grande-colombe-pinot-noir | {category=RED FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000070/0000700226-8407.jpg; country=FRANCE; varietal=Pinot Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Maison Idiart Pinot Noir | $25.99 | stock=55 | https://store.suttonplacewinemerchant.com/products/5102867-maison-idiart-pinot-noir | {category=RED FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000039/0000397946-1822.png; country=FRANCE; varietal=Pinot Noir; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}
  - Makers & Providers Corofin Settlement Vineyard Pinot Noir | $77.49 | 2020 | stock=2 | https://store.suttonplacewinemerchant.com/products/4163682-makers-providers-corofin-settlement-vineyard-pinot-noir | {category=RED N. ZEALAND; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000046/0000469519-4369.jpg; country=NEW ZEALAND; varietal=Pinot Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Makers & Providers Corofin Wrekin Pinot Noir | $77.49 | 2020 | stock=2 | https://store.suttonplacewinemerchant.com/products/4163683-makers-providers-corofin-wrekin-pinot-noir | {category=RED N. ZEALAND; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000046/0000469522-9234.jpg; country=NEW ZEALAND; varietal=Pinot Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 20 results)
  - Champagne Godme Brut Blanc de Noirs 750ml | $134.99 | stock=34 | https://www.marquis-wines.com/champagne-godme-brut-blanc-de-noirs-750ml/ | {sku=1014431; in_stock=True; categories=["Grower Champagne", "Marquis Exclusives", "Organic / Biodynamic Wine", "12 Days of Champagne"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7492/images/5028/hugues-godme-blanc-de-noirs__09888.1479494038.500.500.jpg?c=2}
  - Champagne Pierre Gerbais 2021 Les Grandes Cotes Blanc de Noirs 750ml | $144.99 | stock=27 | https://www.marquis-wines.com/champagne-pierre-gerbais-2021-les-grandes-cotes-blanc-de-noirs-750ml/ | {sku=1031241; in_stock=True; categories=["Marquis Exclusives", "Pierre Gerbais", "Champagne & Bubbles", "Champagne", "Grower Champagne", "Organic / Biodynamic Wine"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21631/images/17314/2026-03-30-13.13.17__75230.1775070147.500.500.png?c=2}
  - Cono Sur Bicicleta Pinot Noir 750ml | $12.99 (reg $12.99) | stock=11 | https://www.marquis-wines.com/cono-sur-bicicleta-pinot-noir-750ml/ | {sku=341602; in_stock=True; categories=["Red Wine", "Pinot Noir", "Chile", "On Sale"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21276/images/16912/cono_sur_bicicleta_pinot_noir__90250.1767218649.500.500.jpg?c=2}
  - Pont Neuf 2018 Pinot Noir "L'Origine" 750ml | $199.99 (reg $182.52) | stock=3 | https://www.marquis-wines.com/pont-neuf-2018-pinot-noir-l-origine-750ml/ | {sku=1024815; in_stock=True; categories=["Spring Cleaning Sale", "Black Friday Wine Sale", "Marquis Exclusives", "Red Wine", "Pinot Noir", "USA", "California", "Sonoma", "Russian River Valley", "On Sale"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/15065/images/10722/2021-08-10_11.47.35__37174.1628703006.500.500.png?c=2}
  - Little Engine 2022 Gold Pinot Noir 375ml | $32.99 | stock=5 | https://www.marquis-wines.com/little-engine-2022-gold-pinot-noir-375ml/ | {sku=1032057; in_stock=True; categories=["Half bottles"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21541/images/17204/IMG_0696__86383.1773168520.500.500.png?c=2}
  - Clos Henri 2024 Estate Pinot Noir 750ml | $44.99 | stock=44 | https://www.marquis-wines.com/clos-henri-2024-estate-pinot-noir-750ml/ | {sku=1032018; in_stock=True; categories=["Red Wine", "Pinot Noir", "Organic / Biodynamic Wine", "New Zealand", "Marlborough"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21487/images/17139/IMG_0634__38609.1771879167.500.500.png?c=2}
  - Keenan Wines 2023 Pinot Noir Rose 750ml | $34.99 | stock=3 | https://www.marquis-wines.com/keenan-wines-2023-pinot-noir-rose-750ml/ | {sku=1031531; in_stock=True; categories=["Organic / Biodynamic Wine", "Rosé Wine", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20887/images/16627/2025-09-24_14.34.00__44572.1758822434.500.500.png?c=2}
  - Giesen 2020 Uncharted Pinot Noir 750ml | $34.99 | stock=25 | https://www.marquis-wines.com/giesen-2020-uncharted-pinot-noir-750ml/ | {sku=1031365; in_stock=True; categories=["Fall Faves", "Red Wine", "Pinot Noir", "New Zealand", "Marlborough"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20732/images/16497/2025-08-14_14.52.56__72360.1755293358.500.500.png?c=2}
  - Siduri 2021 Santa Barbara Pinot Noir 750ml | $65.99 | stock=11 | https://www.marquis-wines.com/siduri-2021-santa-barbara-pinot-noir-750ml/ | {sku=1022107; in_stock=True; categories=["Red Wine", "Pinot Noir", "USA", "California", "Santa Barbara County", "Central Coast"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/11903/images/8876/Jesse_Richmond_-_0131__03205.1731698611.500.500.jpg?c=2}
  - Veramonte Organic Pinot Noir 750ml | $19.49 (reg $19.99) | stock=77 | https://www.marquis-wines.com/veramonte-organic-pinot-noir-750ml/ | {sku=1019676; in_stock=True; categories=["Red Wine", "Pinot Noir", "Chile", "On Sale"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9576/images/17434/2026-04-27_14.05.48__90291.1777398589.500.500.png?c=2}
  - Two Paddocks 2024 Picnic Pinot Noir 750ml | $51.99 | stock=6 | https://www.marquis-wines.com/two-paddocks-2024-picnic-pinot-noir-750ml/ | {sku=1017669; in_stock=True; categories=["Red Wine", "Pinot Noir", "New Zealand", "Central Otago"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21236/images/16921/IMG_0424__17370.1767640969.500.500.png?c=2}
  - Meyer Family 2023 Pinot Noir 750ml | $34.99 | stock=12 | https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/ | {sku=1014474; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7708/images/8652/Lindsey_Ail_-_IMG_15661__44130.1589559651.500.500.jpg?c=2}
  - Greywacke 2022 Pinot Noir 750ml | $69.99 | stock=2 | https://www.marquis-wines.com/greywacke-2022-pinot-noir-750ml-pkzs/ | {sku=1013887; in_stock=True; categories=["Red Wine", "Pinot Noir", "Marlborough", "New Zealand"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20061/images/15804/2025-02-27-15.09.38__45228.1740768412.500.500.png?c=2}
  - Felton Road 2023 Bannockburn Pinot Noir 750ml | $94.99 | stock=9 | https://www.marquis-wines.com/felton-road-2022-bannockburn-pinot-noir-750ml/ | {sku=92155; in_stock=True; categories=["Red Wine", "Pinot Noir", "Organic / Biodynamic Wine", "New Zealand", "Central Otago"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/6929/images/8604/IMG_15171__46156.1763492141.500.500.jpg?c=2}
  - Gray Monk 2021/24 Pinot Noir 750ml | $24.99 | stock=18 | https://www.marquis-wines.com/gray-monk-2019-pinot-noir-750ml/ | {sku=251835; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/15726/images/11434/2022-01-20-17.34.22__23087.1642793746.500.500.png?c=2}
  - Kumeu River 2025 Village Pinot Noir 750ml | $39.99 | stock=1 | https://www.marquis-wines.com/kumeu-river-2025-village-pinot-noir-750ml/ | {sku=1032165; in_stock=True; categories=["Red Wine", "Pinot Noir", "New Zealand", "Hawke's Bay"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21694/images/17389/2026-04-16-14.22.52__15522.1776445115.500.500.png?c=2}
  - Ovorra 2023 Casablanca Pinot Noir 750ml | $28.99 | stock=18 | https://www.marquis-wines.com/ovorra-2023-casablanca-pinot-noir-750ml/ | {sku=1031791; in_stock=True; categories=["Red Wine", "Pinot Noir", "Chile", "Casablanca"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21253/images/16877/IMG_0390__80350.1767116908.500.500.png?c=2}
  - Penfolds 2020 Bin 23 Pinot Noir 750ml | $44.99 | stock=7 | https://www.marquis-wines.com/penfolds-2020-bin-23-pinot-noir-750ml/ | {sku=1031758; in_stock=True; categories=["Red Wine", "Pinot Noir", "Australia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21212/images/16934/2026-01-05_16.21.42__35171.1767819321.500.500.png?c=2}
  - Little Engine 2023 Elevation Pinot Noir 750ml | $32.99 | stock=5 | https://www.marquis-wines.com/little-engine-2023-elevation-pinot-noir-750ml/ | {sku=1031041; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20287/images/16055/2025-04-29-14.26.19__33781.1746032523.500.500.png?c=2}
  - Crystallum 2024 Peter Max Pinot Noir 750ml | $69.99 | stock=2 | https://www.marquis-wines.com/crystallum-2023-peter-max-pinot-noir-750ml/ | {sku=1030763; in_stock=True; categories=["Red Wine", "Pinot Noir", "South Africa"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19932/images/15687/2025-01-31-12.24.12__98607.1738613104.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 20 results)
  - ARMAND HEITZ VIN DE FRANCE PINOT NOIR | $33.61 | stock=8 | https://www.legacyliquorstore.com/product/wine/armand-heitz-vin-de-france-pinot-noir-1-x-750ml | {slug=armand-heitz-vin-de-france-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=France; region=Burgundy; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Domaine Drouhin Pinot Noir | $68.99 | stock=6 | https://www.legacyliquorstore.com/product/wine/domaine-drouhin-dundee-hills-pinot-noir-1-x-750ml | {brand=Dundee Hills; slug=domaine-drouhin-dundee-hills-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=United States; region=Oregon; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - 40 Knots Pinot Noir Coastal | $36.66 | stock=12 | https://www.legacyliquorstore.com/product/wine/40-knots-pinot-noir-coastal-1-x-750ml | {slug=40-knots-pinot-noir-coastal-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Meyer Pinot Noir | $33.3 | stock=6 | https://www.legacyliquorstore.com/product/wine/meyer-pinot-noir-1-x-750ml | {slug=meyer-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - A Sunday in August Lilypond Pinot Noir | $40.3 | stock=13 | https://www.legacyliquorstore.com/product/wine/a-sunday-in-august-lilypond-pinot-noir-1-x-750ml | {slug=a-sunday-in-august-lilypond-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Birch Block Pinot Noir Rose | $32.84 | stock=17 | https://www.legacyliquorstore.com/product/wine/birch-block-pinot-noir-rose-1-x-750ml | {slug=birch-block-pinot-noir-rose-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "rose wine"]}
  - Spearhead Pinot Noir Rose | $29.82 | stock=5 | https://www.legacyliquorstore.com/product/wine/spearhead-pinot-noir-rose-1-x-750ml | {slug=spearhead-pinot-noir-rose-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "rose wine"]}
  - Hartford Court Pinot Noir Lands Edge | $47.79 | stock=7 | https://www.legacyliquorstore.com/product/wine/hartford-court-pinot-noir-lands-edge-1-x-750ml | {slug=hartford-court-pinot-noir-lands-edge-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=United States; region=Sonoma; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Etude Lyric Pinot Noir | $25.2 | stock=9 | https://www.legacyliquorstore.com/product/wine/etude-lyric-pinot-noir-1-x-750ml | {slug=etude-lyric-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=United States; region=California; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Concannon Vineyard Pinot Noir | $16.53 | stock=7 | https://www.legacyliquorstore.com/product/wine/concannon-vineyard-pinot-noir-1-x-750ml | {slug=concannon-vineyard-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=United States; region=California; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Garzon Estate Pinot Noir Rose | $24.41 | stock=18 | https://www.legacyliquorstore.com/product/wine/garzon-estate-pinot-noir-rose-1-x-750ml | {slug=garzon-estate-pinot-noir-rose-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Uruguay; in_stock=True; tags=["wine", "rose wine"]}
  - Henri Giraud Hommage Au Pinot Noir | $203.67 | stock=6 | https://www.legacyliquorstore.com/product/wine/henri-giraud-hommage-au-pinot-noir-1-x-750ml | {slug=henri-giraud-hommage-au-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=France; region=Champagne; in_stock=True; tags=["wine", "champagne & sparkling"]}
  - Clos Henri Pinot Noir | $41.75 | stock=16 | https://www.legacyliquorstore.com/product/wine/clos-henri-pinot-noir-1-x-750ml | {slug=clos-henri-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=New Zealand; region=Marlborough; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Modesta Rama Ridge Pinot Noir | $41.79 | stock=5 | https://www.legacyliquorstore.com/product/wine/modesta-rama-ridge-pinot-noir-1-x-750ml | {slug=modesta-rama-ridge-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - SOKOL BLOSSER PINOT NOIR | $59.35 | stock=3 | https://www.legacyliquorstore.com/product/wine/sokol-blosser-pinot-noir-1-x-750ml | {slug=sokol-blosser-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=United States; region=Oregon; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - TOM GORE PINOT NOIR | $21.09 | stock=9 | https://www.legacyliquorstore.com/product/wine/tom-gore-pinot-noir-1-x-750ml | {slug=tom-gore-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=United States; region=California; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - STOLLER PINOT NOIR WILLAMETTE VALLEY | $45.94 | stock=3 | https://www.legacyliquorstore.com/product/wine/stoller-pinot-noir-willamette-valley-1-x-750ml | {slug=stoller-pinot-noir-willamette-valley-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=United States; region=Oregon; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Vivo Reserva Pinot Noir | $17.85 | stock=31 | https://www.legacyliquorstore.com/product/wine/vivo-reserva-pinot-noir-1-x-750ml | {slug=vivo-reserva-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Chile; region=Central Valley; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Tracy & Cie Pinot Noir Val De Loire | $33.19 | stock=9 | https://www.legacyliquorstore.com/product/wine/tracy-cie-pinot-noir-val-de-loire-1-x-750ml | {slug=tracy-cie-pinot-noir-val-de-loire-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=France; region=Loire Valley; in_stock=True; tags=["wine", "red wine", "pinot noir"]}
  - Meiomi Pinot Noir | $34.94 | stock=12 | https://www.legacyliquorstore.com/product/wine/meiomi-pinot-noir-1-x-750ml | {slug=meiomi-pinot-noir-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=United States; in_stock=True; tags=["wine", "red wine", "pinot noir"]}

#### search_bcliquor_tool (status=ok, 25 results)
  - BEAUJOLAIS CHARDONNAY - FELLOT | $31.99 | stock=829 | in 53 stores | rating=4.9 | https://www.bcliquorstores.com/product/287499 | {sku=287499; product_type=White Wine; grape_type=CHARDONNAY; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Delicate nose of light apple and pear blossom, light tropical notes of pineapple and passion fruit, and a hint of candle wax. The lightly spicy palate is well balanced with grapefruit and citrus peel notes. It finishes fresh and crisp! Enjoy over the next couple of years.
; consumer_votes=30; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/287499.jpeg}
  - BEAUJOLAIS - BOUCHARD AINE | $17.99 (reg $19.99) | stock=2351 | in 154 stores | rating=3.7 | https://www.bcliquorstores.com/product/147546 | {sku=147546; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=12.0; sweetness=00; tasting_notes=Fresh and expressive with pleasant aromas of red fruit including cherries, gooseberries and plum. A supple and well-balanced wine with a subtle floral finish. Beaujolais is a pleasant wine to be appreciated at any time of the day, with picnics, before meals, or with cold meats and starters. Try also with a chicken liver salad, roast chicken and fresh cheese.
; consumer_votes=121; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/147546.jpeg}
  - BEAUJOLAIS BLANC - DOMAINE BERTRAND | $29.99 | stock=12 | in 3 stores | rating=4.4 | https://www.bcliquorstores.com/product/311132 | {sku=311132; product_type=White Wine; grape_type=CHARDONNAY; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=91 Points, James Suckling: "This joyful chardonnay from Beaujolais is brimming with sliced pear fruit and lemon zest freshness. On the generous palate the juicy fruit is backed up by plenty of chalky minerality. The long, elegant finish pulls you back for more. From organically grown grapes. Drink now." (February 2025)
; consumer_votes=5; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/311132.jpeg}
  - BEAUJOLAIS BLACE - MAISON BACHEVILLIER LA POINTE | $46.99 | stock=130 | in 17 stores | https://www.bcliquorstores.com/product/687973 | {sku=687973; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=0; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/687973.jpeg}
  - BEAUJOLAIS - VILLAGES LES 3 MADONES | $23.99 (reg $27.99) | stock=412 | in 34 stores | rating=4.4 | https://www.bcliquorstores.com/product/313922 | {sku=313922; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Deep and intense ruby red colour with vivid tints. Expressive, the nose offers spicy, toasted and vanilla scents with some fruity notes such as cherry and blackberry. The attack is full of harmony, round and greedy. The palate reveals the same aromas than the nose blended with black berries.
; consumer_votes=22; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/313922.jpeg}
  - BEAUJOLAIS VILLAGES - LOUIS JADOT COMBE AUX JACQUES | $29.99 | stock=1368 | in 112 stores | rating=4.0 | https://www.bcliquorstores.com/product/469924 | {sku=469924; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=95 Points, Decanter: "GOLD MEDAL -  Lip-smacking crushed bramble fruit and fulsome minerals with a youthful, leafy veneer. Cheerful and bright with ample, smooth tannins and attractive acidity. Juicy and long." (2025)
; consumer_votes=184; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/469924.jpeg}
  - BEAUJOLAIS NOUVEAU - JEAN-BAPTISTE  DUPERRAY VIEILLES VIGNES | $24.97 (reg $32.99) | stock=14 | in 4 stores | rating=4.4 | https://www.bcliquorstores.com/product/409386 | {sku=409386; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=12.0; sweetness=NA; tasting_notes=Traditionally crafted from organically farmed old gamay vines. Intense, vibrant and juicy nose with light bubblegum and fresh strawberries. The silky texture packed with red fruit offers a completely dry and savoury easy drinking wine, with pleasant grippy tannins on the finish.; consumer_votes=103; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/409386.jpeg}
  - BEAUJOLAIS VILLAGES - DOMAINE ANDRE COLONGE ET FILS LANCIE | $26.99 | stock=652 | in 41 stores | rating=4.5 | https://www.bcliquorstores.com/product/284222 | {sku=284222; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=90 Points Wine Enthusiast "This wine demands your attention at first and leans into your continued attention. Purple in color, the wine has a reserved nose of black plum, black olive, dried raspberry and pressed wildflower. Concentration takes the lead on the midpalate through to the end that wallows in grippy tannins." (September 2024)
; consumer_votes=21; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/284222.jpeg}
  - BEAUJOLAIS NOUVEAU - 2025 DOMAINE DU VIEUX BOURG | $24.97 (reg $32.99) | stock=22 | in 3 stores | rating=4.1 | https://www.bcliquorstores.com/product/321706 | {sku=321706; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Dominique Piron's Nouveau is a new addition to the line up this year and celebrates this producer whose family has been making wine in Beaujolais for 14 generations. Look for sour cherry, black pepper and floral notes on the nose with a quenching palate.; consumer_votes=26; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/321706.jpeg}
  - BEAUJOLAIS - J P BRUN TERRES DOREES L'ANCIEN 2018 | $29.99 | stock=189 | in 14 stores | rating=4.2 | https://www.bcliquorstores.com/product/681569 | {sku=681569; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=92 Points, Wine Advocate: "Brun's dependably superb 2018 Beaujolais l'Ancien offers up notes of rose petals, cherries and raspberries, followed by a medium to full-bodied, fleshy palate built around satiny tannins and juicy acids. It's a beautifully gourmand but precise wine, demonstrating the strengths of this vintage in the limestone soils of the southern Beaujolais. Drink Date: 2019 - 2029." (August 2019)
; consumer_votes=69; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/681569.jpeg}
  - BEAUJOLAIS BLANC - DOM DU VIEUX BOURG CLOS DU VIEUX BOURG | $28.99 | stock=104 | in 14 stores | rating=4.6 | https://www.bcliquorstores.com/product/429627 | {sku=429627; product_type=White Wine; grape_type=CHARDONNAY; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=This Chardonnay is grown on clay-limestone soil. It is fresh with intense floral notes while crisp and round on the palate with good minerality. A great sipping wine that is also versatile with food such as fish dishes and white meats. 
; consumer_votes=45; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/429627.jpeg}
  - MORGON - MATHIEU & CAMILLE LAPIERRE | $56.99 | stock=549 | in 42 stores | rating=4.5 | https://www.bcliquorstores.com/product/141366 | {sku=141366; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=94 Points, James Suckling : "Still has a whiff of youthful funk, but after a couple of swirls this blossoms, becoming fragrant and expressive. Wonderful texture from fine-grained tannins and mineral acidity unlike anything else in Beaujolais. Very long, silky finish. From organically grown grapes. Unfiltered." (April 2022)
; consumer_votes=117; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/141366.jpeg}
  - MOULIN A VENT - DOMAINE ANITA COEUR DE VIGNERONNE 2023 | $49.99 | stock=65 | in 7 stores | rating=4.7 | https://www.bcliquorstores.com/product/303969 | {sku=303969; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=99 Points, James Suckling: "An astonishing expression of the new spirit of Beaujolais... The mind-blowing, velvety texture is interwoven with amazing crushed-rock and wet-stone minerality on the expansive palate. The exceptionally long finish, at once firm and precise, just doesn't want to stop. " (March 2025)
; consumer_votes=10; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/303969.jpeg}
  - MORGON - MICHEL GUIGNIER CANON 2023 | $46.99 | stock=268 | in 24 stores | rating=4.8 | https://www.bcliquorstores.com/product/210506 | {sku=210506; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=12.8; sweetness=00; tasting_notes=99 Points, James Suckling: "This amazing Morgon has incredibly deep roots, but is also a flower reaching out towards the sun. Breathtaking mineral brilliance and energy on the medium-bodied palate. This embodies the spirit of Beaujolais in an extraordinary, uplifting way. Pristine and precise finish that's so long and so pure. Matured sur lie in oak casks. Bottled unfiltered. Drink or hold." (March 2025)
; consumer_votes=87; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/210506.jpeg}
  - FLEURIE - BURRIER | $54.99 | stock=49 | in 7 stores | rating=4.1 | https://www.bcliquorstores.com/product/177402 | {sku=177402; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=The pink granite and sandy soil typical of Fleurie  contribute to the wine's fragrance, minerally taste, and soft tannins. Notes of spice cake and rose petal accompany aromas and  flavors of ripe cherries and raspberries. 
; consumer_votes=6; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/177402.jpeg}
  - SAINT AMOUR - DOMAINE CHARDIGNY CLOS DU CHAPITRE ORGANIC | $55.99 | stock=5 | in 1 stores | rating=5.0 | https://www.bcliquorstores.com/product/283320 | {sku=283320; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=The wine is still quite expressive with its notes of red berries, rhubarb, sweet red rose, sweet greens and crushed rock. Solid, but fine tannins are backed by a fresh, gentle acidity that hits on all sides, revealing a nice long finish.; consumer_votes=4; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/283320.jpeg; certificates=["Organic"]}
  - BROUILLY - LES ROCHES BLEUES LA CROQUANTE 2023 | $35.99 | stock=31 | in 7 stores | rating=4.2 | https://www.bcliquorstores.com/product/296767 | {sku=296767; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=Certified Organic. There is an explosion of sweet raspberry fruit cut by white pepper, violet and blackcurrant and a delightful mineral core. This sees zero oak - it's all fresh, bright red fruit and floral, mineral elegance!
; consumer_votes=13; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/296767.jpeg}
  - REGNIE - DOMAINE LES CAPREOLES DIACLASE | $44.99 | stock=288 | in 20 stores | rating=4.0 | https://www.bcliquorstores.com/product/267201 | {sku=267201; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=93 Points, James Suckling: "This exudes notes of ripe blackberries, cherries and some chocolate, with a touch of rose essence. It's ripe and generous with a medium body and very bright acidity. Long, tasty and vibrant. Drink now or hold." (January 2024)
; consumer_votes=7; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/267201.jpeg}
  - CHIROUBLES - STEEVE CHARVET 2019 | $26.97 (reg $30.99) | stock=35 | in 6 stores | rating=4.5 | https://www.bcliquorstores.com/product/121135 | {sku=121135; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=The Chiroubles from Steeve Charvet reveals intense aromas of black fruit and spice, with round and juicy tannins. It is very well-balanced on the palate with a long, satisfying finish. This fruity red pairs well with appetizers, grilled or roasted white and red meats, poultry and game, as well as cheeses, pastas, rice, tomato sauces,  steamed vegetables and fish.
; consumer_votes=36; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/121135.jpeg}
  - COTE DE BROUILLY - DOMAINE BARON DE L'ECLUSE LES GARANCES 20 | $42.99 | stock=201 | in 17 stores | rating=4.8 | https://www.bcliquorstores.com/product/165636 | {sku=165636; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=14.1; sweetness=00; tasting_notes=93 Points, James Suckling: "A spicy Cote-de-Brouilly with strawberries, peach pits and cloves on the nose. It's medium-bodied, polished and fragrant with fine-grained tannins. Long and lingering with tasty spice notes to close. From over 90-year-old vines. Drink or hold." (February 2024)
; consumer_votes=99; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/165636.jpeg}
  - FLEURIE - MARC DELIENNE ABBAYE ROAD | $65.97 (reg $75.99) | stock=1 | in 1 stores | rating=4.2 | https://www.bcliquorstores.com/product/389968 | {sku=389968; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=A juicy, fragrant wine with notes of red fruits, blueberries and spice. Great balance with silky, succulent fruit and a core of acid holding things in place.
; consumer_votes=4; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/389968.jpeg}
  - BOURGOGNE GAMAY - LOUIS LATOUR 2023 | $28.99 (reg $30.99) | stock=823 | in 61 stores | rating=3.9 | https://www.bcliquorstores.com/product/822809 | {sku=822809; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=This Gamay opens with a complex bouquet of red fruits and delivers a fresh, structured palate with harmonious tannins. Elegant and subtle, the wine finishes with fine persistence, showcasing the vibrant character of Beaujolais Crus
; consumer_votes=95; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/822809.jpeg}
  - FLEURIE - DOMAINE DES MARRANS CLOS DU PAVILLON 2021 | $41.99 | stock=117 | in 16 stores | rating=4.8 | https://www.bcliquorstores.com/product/210509 | {sku=210509; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=92 Points, James Suckling: "This Fleurie is the opposite of the charming wines so many seek from this appellation, but in a very positive way. With a bit of aeration violet and wild strawberry notes develop. Sleek, tightly structured and compact with stacks of healthy tannins, but it has a delicate sweetness that balances all this very well. Long, subtle finish. Drinkable now, but best from 2024." (March, 2023)
; consumer_votes=72; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/210509.jpeg}
  - CHENAS - PASCAL AUFRANC NATURELLEMENT | $36.99 | stock=318 | in 24 stores | rating=5.0 | https://www.bcliquorstores.com/product/287514 | {sku=287514; product_type=Red Wine; grape_type=GAMAY; country=France; volume=0.750; alcohol_pct=13.28; sweetness=00; tasting_notes=90 Points, Wine Enthusiast: "Deep purple in color, this wine has a perfumed nose of ripe black plum, raspberry puree, just-ripened summer strawberry, black tea and violet blossom. The ChŽnas is complex with restrained fruit flavours showing as a whole rather than as individual fruits. Drink now and can age for five-plus years." (March 2024)
; consumer_votes=7; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/287514.jpeg}
  - GEHRINGER - DRY ROCK CABERNET MERLOT 2023 | $18.99 | stock=1034 | in 88 stores | rating=3.8 | https://www.bcliquorstores.com/product/556001 | {sku=556001; product_type=Red Wine; grape_type=CABERNET/MERLOT; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=This juicy red wine is done in stainless steel fermenters and could be easily mistaken for a fine Beaujolais with its damson plum, black cherry and blueberry aromas and its medium-bodied palate. Flavours of blackberry, blueberry, cassis and a touch of herbaceousness hang on the long finish. This lighter, juicier style red wine is a great match for quail, chicken and duck.
; consumer_votes=54; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/556001.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 24 results)
  - Bouchard Aine & Fils Beaujolais Superieur 750 mL | $17.99 | [North Vancouver:6, South Surrey:5, Langley Store:12, Vancouver:4] | https://www.everythingwine.ca/bouchard-aine-beaujolais | {sku=147546; country=France; image_url=https://www.everythingwine.ca/media/catalog/product/1/4/147546_bouchard_aine_fils_beaujolais_superieur.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Domaine Les Capreoles Chamodere Beaujolais 750 mL | $61.98 | https://www.everythingwine.ca/domaine-les-capreoles-chamodere-beaujolais-750-ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Domaine Les Capreoles L'Amourgandise Beaujolais 750 mL | $57.98 | https://www.everythingwine.ca/domaine-les-capreoles-l-amourgandise-beaujolais-750-ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Marcel Lapierre Morgon Beaujolais 750 mL | $56.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:2] | https://www.everythingwine.ca/marcel-lapierre-morgon | {sku=141366; country=France; image_url=https://www.everythingwine.ca/media/catalog/product/1/4/141366_marcel-lapierre-morgon-beaujolais.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - J Drouhin Beaujolais Villages 750 mL | $35.98 | [North Vancouver:3, South Surrey:7, Langley Store:12, Vancouver:15] | https://www.everythingwine.ca/j-drouhin-beaujolais-villages | {sku=199216; country=France; image_url=https://www.everythingwine.ca/media/catalog/product/1/9/199216_joseph_drouhin_gamay_beaujolais-villages.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Jean Foillard Morgon Gamay Beaujolais 750 mL | $54.98 | https://www.everythingwine.ca/jean-foillard-morgon-gamay-beaujolais-750ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - George Duboeuf Julienas Beaujolais Gamay 750 mL | $32.98 | https://www.everythingwine.ca/duboeuf-julienas | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Hospices de Beaujeu Morgon Beaujolais 750 mL | $39.99 | [North Vancouver:0, South Surrey:0, Langley Store:8, Vancouver:0] | https://www.everythingwine.ca/hospice-de-beaujeu-morgon-beaujolais-750-ml | {sku=131670; country=France; image_url=https://www.everythingwine.ca/media/catalog/product/1/3/131670_hospice_de_beaujeu_morgon.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Louis Jadot Beaujolais-Villages Gamay 750 mL | $29.99 | [North Vancouver:0, South Surrey:10, Langley Store:13, Vancouver:6] | https://www.everythingwine.ca/l-jadot-beaujolais-villages | {sku=469924; country=France; image_url=https://www.everythingwine.ca/media/catalog/product/4/6/469924_louis_jadot_beaujolais_villages.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Clos De La Roilette Fleurie Beaujolais 750 mL | $42.98 | https://www.everythingwine.ca/clos-de-la-roilette-fleurie-beaujolais-750ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Dominique Piron Domaine De La Combiaty Brouilly Beaujolais 750 mL | $32.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:6] | https://www.everythingwine.ca/dominique-piron-brouilly | {sku=142836; country=France; image_url=https://www.everythingwine.ca/media/catalog/product/1/4/142836_dominique_piron_domaine_de_la_combiaty_brouilly_beaujolais.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Chateau des Jacques Morgon Cote du Py 750 mL | $71.98 | https://www.everythingwine.ca/chateau-des-jacques-morgon-cote-du-py-750-ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Louis Bernard Cotes Du Rhone Rose 750 mL | $24.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:11] | https://www.everythingwine.ca/louis-bernard-cotes-du-rhone-rose-750-ml | {sku=751446; country=France; image_url=https://www.everythingwine.ca/media/catalog/product/7/5/751446_louis_bernard_cotes_du_rhone_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Clos de Luz Agreste Pais 2020 750 mL | $32.99 | [North Vancouver:7, South Surrey:22, Langley Store:21, Vancouver:8] | https://www.everythingwine.ca/clos-de-luz-agreste-pais-moscatel-750ml | {sku=498986; country=Chile; image_url=https://www.everythingwine.ca/media/catalog/product/4/9/498986_clos_de_luz_agreste_pais.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Richard Rottiers Brouilly 750 mL | $44.98 | https://www.everythingwine.ca/richard-rottiers-brouilly-750-ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - J Drouhin Morgon Gamay 750 mL | $49.98 | [North Vancouver:10, South Surrey:0, Langley Store:0, Vancouver:4] | https://www.everythingwine.ca/j-drouhin-morgon | {sku=51300; country=France; image_url=https://www.everythingwine.ca/media/catalog/product/5/1/51300_joseph_drouhin_morgon_gamay.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Jean Foillard Cuvee Corcelette Morgon 750 mL | $75.98 | https://www.everythingwine.ca/jean-foillard-cuvee-corcelette-morgon-750-ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Domaine Armand Heitz Julienas 1.5 L | $140.98 | https://www.everythingwine.ca/domaine-armand-heitz-julienas-1-5-l | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Marc Delienne Fleurie Abbaye Road 750 mL | $75.99 | https://www.everythingwine.ca/marc-deleinne-fleurie-abbaye-road | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Jean-Etienne Chermette Moulin-a-Vent Rochegres 750 mL | $55.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:5] | https://www.everythingwine.ca/jean-etienne-chermette-moulin-a-vent-rochegres | {sku=296440; country=France; image_url=https://www.everythingwine.ca/media/catalog/product/2/9/296440_jean-etienne_chermette_moulin-a-vent_rochegres.jpeg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Louis Jadot Chateau Des Jacques Moulin-a-Vent 750 mL | $55.98 | https://www.everythingwine.ca/louis-jadot-moulin-a-vent-750-ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Domaine Des Grottes Antilope Sparkling Non-Alcoholic 750 mL | $26.98 | https://www.everythingwine.ca/domaine-des-grottes-antilope-sparkling-non-alcoholic-750-ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Jean-Etienne Chermette Les Micouds Morgon 2020 750 mL | $59.98 | https://www.everythingwine.ca/jean-etienne-chermette-les-micouds-morgon-2020-750-ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Jean-Claude Lapalu La Croix des Rameaux Brouilly 750 mL | $65.98 | https://www.everythingwine.ca/jean-claude-lapalu-la-croix-des-rameaux-brouilly-750-ml | {country=France; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 2 results)
  - Chateau de Vaux Le Clos de Valentin Beaujolais Villages | $25.49 | 2016 | stock=17 | https://store.suttonplacewinemerchant.com/products/5102856-chateau-de-vaux-le-clos-de-valentin-beaujolais-villages | {category=RED FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000017/0000177720-6107.jpg; country=FRANCE; varietal=Gamay Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}
  - Paul Durdilly Cuvee de Garde Beaujolais | $30.99 | 2024 | stock=13 | https://store.suttonplacewinemerchant.com/products/4709248-paul-durdilly-cuvee-de-garde-beaujolais | {category=RED FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000020/0000209877-9783.jpg; country=FRANCE; varietal=Gamay Noir; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 16 results)
  - Jean Louis Dutraive 2023 Fleurie Grand Cour 750ml | $75.99 | stock=10 | https://www.marquis-wines.com/jean-louis-dutraive-2022-fleurie-grand-cour-750ml/ | {sku=1026684; in_stock=True; categories=["Red Wine", "Beaujolais", "Gamay", "France", "Fleurie"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/16013/images/11753/2022-03-17_16.14.09__37147.1712955508.500.500.png?c=2}
  - Domaine Gregoire Hoppenot 2022 Fleurie "Les Moriers" 750ml | $61.99 | stock=22 | https://www.marquis-wines.com/domaine-gregoire-hoppenot-2022-fleurie-les-moriers-750ml/ | {sku=1028082; in_stock=True; categories=["Red Wine", "Beaujolais", "Gamay", "France", "Fleurie"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19361/images/15100/2024-09-18-14.19.22__85651.1726767758.500.500.png?c=2}
  - Lapierre 2023 Morgon "Cuvée Camille" 750ml | $102.99 | stock=2 | https://www.marquis-wines.com/lapierre-2022-morgon-cuvee-camille-750ml/ | {sku=1026373; in_stock=True; categories=["Red Wine", "Beaujolais", "Gamay", "France", "Morgon"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19047/images/14865/2024-07-04_15.38.58__59286.1720216251.500.500.png?c=2}
  - Louis Claude Desvignes 2023 Morgon "Chateau Gaillard" 750ml | $51.99 | stock=1 | https://www.marquis-wines.com/louis-claude-desvignes-2023-morgon-chateau-gaillard-750ml/ | {sku=1030503; in_stock=True; categories=["Marquis Exclusives", "Louis‑Claude Desvignes", "Red Wine", "Gamay", "France", "Beaujolais", "Morgon"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20582/images/16421/2025-07-29-13.51.10__38600.1753896141.500.500.png?c=2}
  - Clos de Mez 2021 Fleurie "La Dot" 750ml | $57.99 | stock=2 | https://www.marquis-wines.com/clos-de-mez-2021-fleurie-la-dot-750ml/ | {sku=1018284; in_stock=True; categories=["Marquis Exclusives", "Clos de Mez", "Red Wine", "Gamay", "Organic / Biodynamic Wine", "France", "Beaujolais", "Fleurie"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21256/images/16866/IMG_0379__34747.1766603593.500.500.png?c=2}
  - Louis Boillot 2022 Moulin a Vent "La Rochelle" 750ml | $77.99 | stock=24 | https://www.marquis-wines.com/louis-boillot-2022-moulin-a-vent-la-rochelle-750ml/ | {sku=1030910; in_stock=True; categories=["Marquis Exclusives", "Louis Boillot", "Red Wine", "Gamay", "France", "Beaujolais", "Moulin a Vent"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21229/images/16898/IMG_0404__47471.1767205992.500.500.png?c=2}
  - Louis Boillot 2022 Moulin a Vent "Champ de Cour" 750ml | $71.99 | stock=22 | https://www.marquis-wines.com/louis-boillot-2022-moulin-a-vent-champ-de-cour-750ml/ | {sku=1030909; in_stock=True; categories=["Marquis Exclusives", "Louis Boillot", "Red Wine", "Gamay", "France", "Beaujolais", "Moulin a Vent"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21228/images/16897/IMG_0403__25420.1767205768.500.500.png?c=2}
  - Louis Boillot 2022 Moulin a Vent "Vieilles Vignes" 750ml | $51.99 | stock=33 | https://www.marquis-wines.com/louis-boillot-2022-moulin-a-vent-vieilles-vignes-750ml/ | {sku=1030908; in_stock=True; categories=["Marquis Exclusives", "Louis Boillot", "Red Wine", "Gamay", "France", "Beaujolais", "Moulin a Vent"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21248/images/16880/IMG_0393__83266.1767118339.500.500.png?c=2}
  - Louis Claude Desvignes 2023 Morgon Cote de Py "Javernieres Aux Pierres" 750ml | $76.99 | stock=31 | https://www.marquis-wines.com/louis-claude-desvignes-2023-morgon-cote-de-py-javernieres-aux-pierres-750ml/ | {sku=1026276; in_stock=True; categories=["Marquis Exclusives", "Louis‑Claude Desvignes", "Red Wine", "Gamay", "France", "Beaujolais", "Morgon"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20578/images/16424/2025-07-29-13.53.27__44003.1753896632.500.500.png?c=2}
  - Clos de Mez 2018 Morgon "Chateau Gaillard" 750ml | $55.99 | stock=40 | https://www.marquis-wines.com/clos-de-mez-2018-morgon-chateau-gaillard-750ml/ | {sku=1022026; in_stock=True; categories=["Marquis Exclusives", "Clos de Mez", "Red Wine", "Gamay", "Organic / Biodynamic Wine", "France", "Beaujolais", "Morgon"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21254/images/16867/IMG_0380__07384.1766603896.500.500.png?c=2}
  - Clos de Mez 2022 Fleurie "Mademoiselle M" 750ml | $49.99 | stock=54 | https://www.marquis-wines.com/clos-de-mez-2022-fleurie-mademoiselle-m-750ml/ | {sku=1022025; in_stock=True; categories=["Marquis Exclusives", "Clos de Mez", "Red Wine", "Gamay", "Organic / Biodynamic Wine", "France", "Beaujolais", "Fleurie"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21262/images/16865/IMG_0378__91030.1766603393.500.500.png?c=2}
  - Louis Claude Desvignes 2023 Morgon Cote du Py "Javernieres Les Impenitents" 750ml | $154.99 | stock=22 | https://www.marquis-wines.com/louis-claude-desvignes-2023-morgon-cote-du-py-javernieres-les-impenitents-750ml/ | {sku=1021964; in_stock=True; categories=["Marquis Exclusives", "Louis‑Claude Desvignes", "Red Wine", "Gamay", "France", "Beaujolais", "Morgon"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20573/images/16425/2025-07-29-13.54.02__39639.1753896823.500.500.png?c=2}
  - Louis Claude Desvignes 2023 Morgon Cote de Py "Javernieres" 750ml | $63.99 | stock=146 | https://www.marquis-wines.com/louis-claude-desvignes-2023-morgon-cote-de-py-javernieres-750ml/ | {sku=1021963; in_stock=True; categories=["Marquis Exclusives", "Louis‑Claude Desvignes", "Red Wine", "Gamay", "France", "Beaujolais", "Morgon"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20589/images/16423/2025-07-29-13.52.35__12501.1753896362.500.500.png?c=2}
  - Lapierre 2024 Raisins Gaulois VDP 750ml | $47.99 | stock=11 | https://www.marquis-wines.com/lapierre-2022-raisins-gaulois-vdp-750ml/ | {sku=1021373; in_stock=True; categories=["Red Wine", "Gamay", "France", "Organic / Biodynamic Wine"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/11113/images/6760/IMG_9257__64654.1772473822.500.500.JPG?c=2}
  - Maison Louis Jadot 2023 Macon Villages "Grange Magnien" 750ml | $46.99 | stock=4 | https://www.marquis-wines.com/maison-louis-jadot-2023-macon-villages-grange-magnien-750ml/ | {sku=1018066; in_stock=True; categories=["White Wine", "Chardonnay", "Mâcon", "Burgundy", "France"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20383/images/16125/2025-05-15-13.24.35__99553.1747419603.500.500.png?c=2}
  - Blue Mountain 2022 Gamay Noir 750ml | $35.99 | stock=12 | https://www.marquis-wines.com/blue-mountain-2019-gamay-noir-750ml/ | {sku=1014652; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8456/images/5067/blue-mountain-gamay-2015__59204.1533682531.500.500.jpg?c=2}

#### search_legacy_liquor_store_tool (status=ok, 4 results)
  - J P Brun Terres Dorees Beaujolais | $31.93 | stock=5 | https://www.legacyliquorstore.com/product/wine/j-p-brun-terres-dorees-beaujolais-1-x-750ml | {slug=j-p-brun-terres-dorees-beaujolais-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=France; region=Beaujolais; in_stock=True; tags=["wine", "red wine", "gamay"]}
  - Beaujolais Villages - Louis Jadot Combe Aux Jacques | $34.82 | stock=10 | https://www.legacyliquorstore.com/product/wine/beaujolais-villages-louis-jadot-combe-aux-jacques-1-x-750ml | {slug=beaujolais-villages-louis-jadot-combe-aux-jacques-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=France; region=Beaujolais; in_stock=True; tags=["wine", "red wine", "gamay"]}
  - Le Grappin Beaujolais Villages | $42.37 | stock=5 | https://www.legacyliquorstore.com/product/wine/le-grappin-beaujolais-villages-1-x-750ml | {slug=le-grappin-beaujolais-villages-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=France; region=Beaujolais; in_stock=True; tags=["wine", "red wine", "gamay"]}
  - Domaine Jean Loron Champ de Cour Moulin-à-Vent 2019 | $55.28 | stock=2 | https://www.legacyliquorstore.com/product/wine/domaine-jean-loron-champ-de-cour-moulin-vent-2019-1-x-750ml | {brand=Beaujolais; slug=domaine-jean-loron-champ-de-cour-moulin-vent-2019-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=France; region=Beaujolais, France; in_stock=True; tags=["wine", "red wine", "gamay"]}

````

</details>

### Latency

- 172.5s
