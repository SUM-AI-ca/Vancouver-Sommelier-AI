# MT-PREF-001 — MT-PREF

- Thread ID: `eval-MT-PREF-001-19483a00`
- Turns: 3

---
## Turn 0

### Query

> I'd like to start saving recommendations under $35 — that's my standing budget. Got it?

### Tool Calls (in order)

_(no tool calls)_

### Final Response

```markdown
Got it! I have noted your standing budget of **under $35**. 

From now on, whenever you ask for wine, beer, or spirits recommendations, I will focus on finding options that fit within this budget while sourcing real-time prices and availability from local Vancouver stores. 

What are we looking for first? Let me know if you have a specific style, occasion, or pairing in mind!
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
    "GENERAL_KNOWLEDGE": 0,
    "NOT_IN_EVIDENCE": 0,
    "CONTRADICTED": 0
  },
  "correctness_rationale": "The agent correctly acknowledged the user's preference without making any factual claims.",
  "issues": [],
  "strengths": [
    "Clearly acknowledges the user's budget constraint.",
    "Promptly asks for the first request to get started."
  ],
  "parse_error": false
}
```

### Claim Verdicts

_(no checkable factual claims extracted)_

### Evidence shown to judge

_0 tool messages, 0 chars (budget 2000000)_

<details><summary>Show evidence</summary>

````markdown
(none)
````

</details>

### Latency

- 4.24s

---
## Turn 1

### Query

> Recommend a BC red wine for a casual dinner tonight.

### Tool Calls (in order)

1. `sommelier_agent_tool` args={"request": "Recommend 3-4 BC red wines under $35 that are perfect for a casual dinner. Provide tasting notes, style descriptions, and food pairing suggestions."}
2. `sourcing_agent_tool` args={"request": "BC red wine under $35 in stock in Vancouver stores"}

### Final Response

```markdown
Here are four fantastic BC red wines under your **$35 budget** that are perfect for a casual dinner tonight. These options are currently **in stock** at local Vancouver retailers, complete with pricing, stock levels, and direct purchase links.

---

### 1. Meyer Family Vineyards 2023 Pinot Noir
* **Price:** $34.99 (12 in stock)
* **Where to Buy:** [Marquis Wine Cellars (Davie St)](https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/)
* **The Vibe:** Elegant, fresh, and highly versatile. Meyer is one of BC’s premier Pinot Noir producers, and this regional blend is incredibly approachable.
* **Tasting Notes & Reviews:** Reviewing the 2023 vintage, critic Anthony Gismondi (*Gismondi on Wine*) awarded it **89 points**, calling it a highly successful and approachable release. Shelley Boettcher (*Castanet*) praised it for its delicate, bright notes of cherry, pomegranate, and green tea.
* **Best Casual Pairings:** The ultimate food chameleon. It pairs beautifully with roast chicken, mushroom risotto, or a simple Margherita pizza.

### 2. Tinhorn Creek 2023 Cabernet Franc
* **Price:** $27.99 (47 in stock)
* **Where to Buy:** [Marquis Wine Cellars (Davie St)](https://www.marquis-wines.com/tinhorn-creek-2023-cabernet-franc-750ml/)
* **The Vibe:** Structured, savory, and slightly bolder. Cabernet Franc is BC's signature red grape, and Tinhorn Creek produces a benchmark expression that balances dark fruit with classic herbal notes.
* **Tasting Notes & Reviews:** While the 2023 is the current vintage on shelves, the preceding 2022 vintage took home a prestigious **Platinum Medal** at the 2025 National Wine Awards of Canada (*WineAlign*). For the 2021 vintage, John Schreiner awarded it **91 points**, noting its bright, fresh dark fruit flavors and excellent drinkability.
* **Best Casual Pairings:** Perfect for anything off the grill. Pair it with smash burgers, grilled pork chops, or roasted root vegetables.

### 3. Blue Mountain 2020 Gamay Noir
* **Price:** $33.99 (4 in stock)
* **Where to Buy:** [Sutton Place Wine Merchant (Yaletown)](https://store.suttonplacewinemerchant.com/products/4228470-blue-mountain-gamay)
* **The Vibe:** Juicy, vibrant, and incredibly easy-drinking. Blue Mountain in Okanagan Falls is legendary for its cool-climate estate wines, and their Gamay is a local favorite.
* **Tasting Notes:** Expect bright red berry fruit (cranberry and raspberry), subtle peppery spice, and a refreshing, clean acidity that keeps you coming back for another sip. 
* **Best Casual Pairings:** Excellent with a charcuterie board, grilled sausages, or casual takeout like roast duck or pork souvlaki.

### 4. Clos Du Soleil Célestiale 2019 (Red Blend)
* **Price:** $34.99 (41 in stock)
* **Where to Buy:** [Sutton Place Wine Merchant (Yaletown)](https://store.suttonplacewinemerchant.com/products/4205421-clos-du-soleil-celestiale)
* **The Vibe:** A sophisticated, organic Bordeaux-style blend from the Similkameen Valley. It offers a bit more depth and structure while remaining soft enough for a casual weeknight.
* **Tasting Notes:** A blend of Cabernet Sauvignon, Merlot, Cabernet Franc, Malbec, and Petit Verdot. It features elegant aromas of blackberry, plum, and graphite, backed by fine-grained tannins and a fresh, stony minerality.
* **Best Casual Pairings:** Ideal for heartier comfort foods like a rich lasagna, beef tacos, or a classic shepherd's pie.

---

### 🛒 Quick Pick-Up Option (BC Liquor Stores)
If you need to run to a government liquor store instead, look out for:
* **Mt. Boucherie OV PTG** — **$25.99** | [Buy at BCLS](https://www.bcliquorstores.com/product/78218)
  * *A classic, juicy blend of Pinot Noir and Gamay Noir that is light, lively, and incredibly food-friendly.*
```

### Judge Scores

```json
{
  "relevance": 5,
  "correctness": 4,
  "helpfulness": 5,
  "coherence": 5,
  "harmlessness": 5,
  "overall": 4,
  "claim_label_counts": {
    "SUPPORTED": 10,
    "GENERAL_KNOWLEDGE": 0,
    "NOT_IN_EVIDENCE": 1,
    "CONTRADICTED": 0
  },
  "correctness_rationale": "The agent provides highly accurate pricing, stock, and review information, but hallucinates the specific 5-grape blend for the Clos Du Soleil C\u00e9lestiale which was not in the provided evidence.",
  "issues": [
    "The agent hallucinated the specific 5-grape blend (Cabernet Sauvignon, Merlot, Cabernet Franc, Malbec, and Petit Verdot) for the Clos Du Soleil C\u00e9lestiale, which was not in the provided evidence."
  ],
  "strengths": [
    "Successfully adhered to the user's standing budget of under $35 from the previous turn.",
    "Provided exact stock counts, prices, and direct purchase links for local Vancouver stores."
  ],
  "parse_error": false
}
```

### Claim Verdicts

| Label | Claim | Evidence quote |
|---|---|---|
| SUPPORTED | Meyer Family Vineyards 2023 Pinot Noir is priced at $34.99 with 12 in stock at Marquis Wine Cellars. | Meyer Family 2023 Pinot Noir — $34.99 (12 in stock) |
| SUPPORTED | Anthony Gismondi awarded the 2023 Meyer Family Pinot Noir 89 points. | Anthony Gismondi (Gismondi on Wine / Vancouver Sun): 89 points (March 2025). |
| SUPPORTED | Shelley Boettcher noted the 2023 Meyer Family Pinot Noir has notes of cherry, pomegranate, and green tea. | Shelley Boettcher (Castanet): Reviewed in March 2025, she praised it as a fresh, balanced, and well-priced bottle that delivers delicate notes of cherry, pomegranate, and green tea. |
| SUPPORTED | Tinhorn Creek 2023 Cabernet Franc is priced at $27.99 with 47 in stock at Marquis Wine Cellars. | Tinhorn Creek 2023 Cabernet Franc — $27.99 (47 in stock) |
| SUPPORTED | The 2022 Tinhorn Creek Cabernet Franc won a Platinum Medal at the 2025 National Wine Awards of Canada. | National Wine Awards of Canada (WineAlign, 2025): Platinum Medal. |
| SUPPORTED | John Schreiner awarded the 2021 Tinhorn Creek Cabernet Franc 91 points. | John Schreiner: 91/100. |
| SUPPORTED | Blue Mountain 2020 Gamay Noir is priced at $33.99 with 4 in stock at Sutton Place Wine Merchant. | Blue Mountain Gamay 2020 — $33.99 (4 in stock) |
| SUPPORTED | Clos Du Soleil Célestiale 2019 is priced at $34.99 with 41 in stock at Sutton Place Wine Merchant. | Clos Du Soleil Célestiale 2019 (Red Blend) — $34.99 (41 in stock) |
| NOT_IN_EVIDENCE | Clos Du Soleil Célestiale is a blend of Cabernet Sauvignon, Merlot, Cabernet Franc, Malbec, and Petit Verdot. | — |
| SUPPORTED | Mt. Boucherie OV PTG is priced at $25.99 at BC Liquor Stores. | Mt. Boucherie OV PTG (BC VQA Pinot Noir/Gamay) — $25.99 |
| SUPPORTED | Mt. Boucherie OV PTG is a blend of Pinot Noir and Gamay Noir. | Mt. Boucherie OV PTG (BC VQA Pinot Noir/Gamay) |

### Evidence shown to judge

_2 tool messages, 89400 chars (budget 2000000)_

<details><summary>Show evidence</summary>

````markdown
### sommelier_agent_tool (status=ok)
**Sub-agent synthesis:**
For a casual dinner, you want wines that are approachable, versatile with food, and offer great value without sacrificing quality. British Columbia excels at producing vibrant, food-friendly reds that punch well above their weight class. 

Here are 4 excellent BC red wines that typically sit under the $35 mark, along with tasting notes, style descriptions, and pairing ideas. To ensure you have a complete beverage strategy for your dinner, I have also included some fantastic local beer, spirit, and sake alternatives.

### 1. Meyer Family Vineyards Okanagan Valley Pinot Noir
**Style:** Elegant, fresh, and highly versatile. Meyer is one of BC’s premier Pinot Noir producers, and their regional blend is a masterclass in approachability. 
*   **Tasting Notes & Scores:** Reviewing the 2023 vintage, Anthony Gismondi ([Gismondi on Wine](https://gismondionwine.com/)) awarded it 89 points, calling it a highly successful and approachable release despite recent challenging winter vintages in the Okanagan. Shelley Boettcher ([Castanet](https://www.castanet.net/)) praised the same vintage for its delicate notes of cherry, pomegranate, and green tea. 
*   **Food Pairing:** The ultimate casual dinner chameleon. It’s perfect for a classic roast chicken, mushroom risotto, or even a Margherita pizza. 

### 2. JoieFarm PTG (Passe-Tout-Grains)
**Style:** Fun, juicy, and "gulpable." This is a classic Burgundian-style blend of Pinot Noir and Gamay Noir from the Naramata Bench. It is lighthearted but exceptionally well-crafted.
*   **Tasting Notes & Scores:** Jamie Goode ([WineAlign](https://www.winealign.com/)) gave the 2023 vintage 91 points, describing it as vivid and juicy with a mineral texture and savory finish. *Gismondi on Wine* (89 points) highlighted its expressive spice, red cherry aromas, and silky tannins, noting its highly approachable character. 
*   **Food Pairing:** Serve this slightly chilled. It is phenomenal with charcuterie boards, grilled sausages, or a casual spread of soft cheeses and pâté.

### 3. Tinhorn Creek Cabernet Franc
**Style:** Structured, savoury, and slightly bolder. Cabernet Franc is arguably BC's signature red grape, and Tinhorn Creek produces a benchmark expression that balances dark fruit with classic herbal notes.
*   **Tasting Notes & Scores:** The 2022 vintage took home a Platinum Medal at the 2025 National Wine Awards of Canada ([WineAlign](https://www.winealign.com/)), where judges praised it as a lively, flashy, and youthful expression. For the 2021 vintage, John Schreiner ([John Schreiner on Wine](https://johnschreiner.blogspot.com/)) awarded 91 points, noting that it remained bright and fresh with clean dark fruit flavors despite a hot growing season.
*   **Food Pairing:** This is your go-to for casual BBQ. Pair it with smash burgers, grilled pork chops, or roasted root vegetables with herbs de Provence.

### 4. Bartier Bros. Syrah
**Style:** Bold, peppery, and savoury. Located on the Black Sage Bench, Bartier Bros. crafts Syrah that leans into the savoury, Northern Rhône style rather than a jammy Shiraz profile. *(Note: Due to recent winter freezes, the 2022 vintage is one of their final estate Syrah releases for the time being).*
*   **Tasting Notes & Scores:** Reviewing the 2022 vintage, John Schreiner awarded it 90 points, highlighting its generous texture, dark fruits, black pepper, and long finish. Treve Ring ([Gismondi on Wine](https://gismondionwine.com/)) praised the 2020 vintage for its plump blackberry and dusky plum notes, balanced by stony acidity and a violet-kissed finish.
*   **Food Pairing:** Ideal for heartier casual fare like braised short rib tacos, lamb burgers, or a rich, meaty lasagna.

---

### Casual Dinner Alternatives (Beer, Spirits & Sake)
A great beverage program always has options. If your guests prefer something other than wine, here are some fantastic BC alternatives that fit the casual dinner vibe:

*   **Beer:** **33 Acres of Ocean (West Coast Pale Ale)** from Vancouver. It’s crisp, piney, and perfectly balanced with a subtle malt backbone. It cuts through the richness of casual comfort foods like pizza, burgers, or fried chicken effortlessly.
*   **Spirit / Cocktail:** **Odd Society Wallflower Gin** (East Vancouver). Distilled from 100% BC-grown barley, it is highly aromatic. [BC Spirits](https://bcspirits.com/) highlights its woody lavender, spicy juniper, and earthy botanicals. Serve it as a pre-dinner Gin & Tonic using a dry, premium tonic (like Fever-Tree) and a simple citrus peel garnish to let the floral notes shine.
*   **Sake:** **Artisan SakeMaker Osake Fraser Valley Junmai** (Granville Island). Made from 100% BC-grown sake rice, this is a uniquely Canadian sake. [Sip Magazine](https://sipmagazine.com/) noted its aromas of sweet hay, honeysuckle, and hazelnut, backed by a crisp acidity. Its savoury umami profile makes it a brilliant, unexpected pairing for roast chicken or a casual cheese and charcuterie board.

#### search_web_grounded_tool (status=ok, 11 results)
Search answer: The **Meyer Family Vineyards Okanagan Valley Pinot Noir** is the winery's entry-level regional blend. Sourced from multiple vineyards across the region (typically including sites in Naramata, Osoyoos, Kaleden, and Okanagan Falls), it is widely praised by critics for offering exceptional value. 

Recent vintages have received the following review scores and critic assessments:

### **2023 Vintage**
*   **Anthony Gismondi (*Gismondi on Wine / Vancouver Sun*):** **89 points** (March 2025). He noted that despite severe winter crop damage across the Okanagan, this vintage is a highly successful, approachable release for Pinot fans.
*   **Shelley Boettcher (*Castanet*):** Reviewed in March 2025, she praised it as a fresh, balanced, and well-priced bottle that delivers delicate notes of cherry, pomegranate, and green tea.

### **2022 Vintage**
*   **Anthony Gismondi (*Gismondi on Wine*):** **90 points**. He called it a bargain-priced winner, highlighting its juicy cherry and raspberry profile, bright acidity, and excellent drinkability.
*   **WineAlign:** **91 points**.
*   **Robert K. Stephen (CSW):** **92 points** (July 2023). He described the wine as elegant and light on its feet, showing inviting aromas of red berries, milk chocolate, and subtle oak.

### **2021 Vintage**
*   **Anthony Gismondi & Treve Ring (*Gismondi on Wine*):** **88 points** (August 2022). They described it as a fleshy, ready-to-drink style with an earthy, slightly rustic undercurrent that balances out the bright black cherry fruit.

### **2019 Vintage**
*   **Natalie MacLean:** **89 points**. She described it as a fresh, medium-bodied, and silky blend featuring ripe cherry, forest floor, and savory herb notes.

### **2018 Vintage**
*   **WineAlign:** **91 points**.
*   **Anthony Gismondi (*Gismondi on Wine*):** **90 points**. He highlighted its soft, fresh red fruit character, touch of minerality, and effortless, silky finish.
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqG9yGhHD0hhPhMd8jTlrIIvT0pIFRavFzcYHy3exriZmTqkvzOpy6-R7UpKiy0_pW_CwK31XHRrmBG-BWUKfX14Ac0Kz6EFa0QfZ-71z9ARt2NH4TrbM4wwmNU2JIlWmsvLUb-2eIuTmxp8TN88zXD9R0Se7VP3GnHJeeFSl9bg==): 
  - [kensingtonwinemarket.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJBGUmuT6C9KtxbJKJvmTfse0-Kqxp92npljyJIIuF4FwbgTOLaO07iEkIm4KOU2HeTaL5y910zHjb7_jsJQVsH-uUosjRCi10nkVpgjktlvBXhzwn2daOLQVnyoQ0d5Glc1-KUVnST5eBMBcjcDVihOGqpl8wabISTvUZDchG3OZ-OEMEgaNMHhWUPhIB): 
  - [bcwinetrends.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET375S2vlVZVn8J8aYJIZSI5mNqQQP5ah7XKeNu94lCtM4cRG4U8X8b5y-KDO911xjwFRe697dhct8TZPCXDNiprt_e1K5HbZullDrF_3V8Jgwq9Zjuy3uyOFgngj2SX5p1JBrLZDYEetglDUdifhGbOLUgYTxBlqEwbUN3g75colOEAPgWaJwf6tgarxRuQF7fOIA6w==): 
  - [heavenlyvines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjIvbfx_VvzTWA3dtP-j89uJhqUN6yr3B8wfo9NhMwRrRHcOH5QjAmdoemmC7e1hvyfuIaFbSvaTx7oG1a6zCey4stPK7B3_cXmNF926AipC4wHYrPGV3ty6S_D7SeOQMghI2Za_tam8I7-bkuswcbWJdMqoITmifxxt1zIuw0xA==): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2JeXy7AOw-n2m4WB83DI6f5kY5Km_Vl6ud78uPgrM1GPNK_vfbGa3a6AWFEneEn3LfNpnc6mABxAGbXuEU8aCAqHSEM2LWw-mS8tUkBSdzptCMa2L_jGFJTEk3tDXAB0tFZDycYuA4Y75ARtU9Wr1Ds7EfuZb7TqKIP22bPNXSZnRXC9KQKr6vg==): 
  - [castanet.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUTqtfij9hGHV3TkuePvXcpHmodpZPQhgmTI6lq5_9VW1DTNqSXCvDINXvJcbwel5L3iSlH3WXH_sQm5_Pa9w_Mu8JNRdmI3mtPrmpBYoMHC6wFeQM6QqShjS8qBVzobdBHjRt8frTo7jhdMU0MzI-d5BN1BchQB_OuWaTvWMTb2uO-K-wLbVuwNWzwtFrtkJUqRw=): 
  - [npwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUaBsbRTEsjXow-x02bVsFyiW5egVxOw_Bi57IpgfuOa6MvvnB9lYDjRsLUdj0kK9xK52hECAIPMxDZA5YYK7erMXDlncQKBWhfNk0_0D0XuCVi_QvTJCpoSkQ3MZXpQFIvbxTzGkUXzV4XbObDs_D10owJKosBckO_rrCd7ddHHkrIBjVo05fm1png4v16w==): 
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGpcv6yqVO9DkpOFkO4Icjcqix4jpL5HEgOPgoxHgtTEWRXN6v-zc16OdV272cW3IjLWqlAVbJMrBkUYhOfVM1grwSzYW7QLRMEfkU7SoP0R6iqRfT1ejGIlvnbLCnMHEjrFCqV3L9xgnvKKUY0Yc4KuF68cgvMhdFhpbMNPlESti2rasy98FN7juE3_rQSaSePiO_LUfV5-QA7MbyhjX6XrGI0zjDlyx3omVFuDsvfyJoZqw=): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtaaQf0TaQ6KUKsYWHMkGHwOu8-u7gwJhP40u8YozFUHN04xBZD772jdVgFWzj-NVX-CzY1ijeObRChlEMZKucAispZxIsihjdcNFiPKlQkMDM6yQflZJkOxJHKMalXaWJqXC7MGRot5e_L-Ht3T6yTiDhPEU19FW7dBSZDOIYHcRpkNB2t62XPmJkTg==): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkR3uKMyPpaQ4U17SIhqV_ZWNr6HsL6ELjCioyC5ZqWApagfHBd1GfF4ffsY3KCletWKjAvRvUt6LQSz6slhsCzqR5kNvIobFqNa0NJNNT8eFlY7B3v3EbhPRmOIls9Of1309Sdr2B46Er3kwvK0RFoFDYoB9lkFYKPGK9KZPd0spUC2UsUcWwTH2PN2kW881npwoC): 
  - [npwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4NZbLCjq3tNqO9E93rjN-JUfRZhW-OHRONHofJJRzWdt3YUGbWImodFsgHANImA6Vf7FsRXhpWDr2tfM2aB35KZC4ZQSaYXeO-Y-OMoQprV3HE5L6nnSC0P-MloCuaYt2UoUEHjtgz_XwKN5scPv11kaJYpZWq88GLWWK8TOUcfciZGY7CB5KMDPaO1l8tw==): 

#### search_web_grounded_tool (status=ok, 8 results)
Search answer: **JoieFarm PTG** (Passe-Tout-Grains) is a classic Burgundian-style red blend of Pinot Noir and Gamay Noir produced on the Naramata Bench in British Columbia's Okanagan Valley. 

Review scores and tasting summaries from prominent Canadian and international critics include:

### **2023 Vintage**
* **Jamie Goode (WineAlign): 91 Points** 
  Goode praised the wine as a vivid, juicy, and intriguing blend with a mineral, grainy texture and a savory finish.
* **Anthony Gismondi & Treve Ring (Gismondi on Wine): 89 Points** (Tasted Sept 2025)
  The duo highlighted its expressive spice and red cherry aromas, noting a soft, round palate with silky tannins and a highly approachable, "gulpable" character.
* **National Wine Awards of Canada (2025): Silver Medal**

### **2022 Vintage**
* **Michael Godel (WineAlign): 90 Points** (Tasted June 2025)
  Godel described this vintage as a fun, well-crafted, and lighthearted take on the style, showing sweet red fruit, raspberry, and earthy mulch notes.

### **Older Vintages**
* **2016 Vintage:** Rated **88 Points** by Rick VanSickle (*Wines in Niagara*) and **88 Points** by *Gismondi on Wine*. Critics enjoyed its soft, jammy red fruit profile, peppery spice, and refreshing acidity.
* **2015 Vintage:** Rated **90 Points** by Neil Phillips (*Natalie MacLean*) and **89 Points** by *Gismondi on Wine*. Phillips noted its bright tart cherry flavors, vibrant acidity, and herbaceous, spicy finish.
* **2012 Vintage:** Rated **90 Points** by Neil Phillips (*Natalie MacLean*) and **90 Points** by *Gismondi on Wine*, praised for its light body, bright acidity, and notes of bramble, cherry, and sage.
  - [npwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER1Led2bPrREibM3RhuT0J5jJAfKM50Ebee_CQvCD8CQTMtMPgPl2QnDff8ynMn67HA4c7n7FIWJn3-_oyrC4jWp1gGAdPi0dASGxJuLKiG4XEKG3SvOngIkvvC3Sbug8AN6GjPjakmIXL60_sK1I3-Xc8eeGjIs_7): 
  - [joiefarm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-S_xDyKAVMpe9Vlzr-DSrXsF_BnjdaXEAfaoT4H9_m3tH-4cJYwG8dV1qngUFln7nvGOVwJmfm4SIcVchTJ9GbPSi483M24hDzkq6z-WE-6A13vt67VzDRqUN_bHWmXbp38KXAVdUJw==): 
  - [thebeerguy.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVieZUfT_6eYdpamYVmx9wPI4tErJHAqNgf9JOgC48-ehX0OuTBE8WvhZhMY-bPFYjVrHg99HIw_81Lz0LAEVNhWng-giHPum_RVGRwueYZZbLt_uImgHxhy7NSH9wT5evLr6y5PdYgfGQEbiZjXqtU49HV3AFoD2MYNqnAibpaKrr6Gl_QyZ0eRGLEw5ThNGVkLK3): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkTf41F8J436uGgnlyVVlj8X6rlbX3CcQP5Dx6thr50OuCoXKoNaR0uiJ_-N4diA8_OWiHWuATeKOUafjqlj_XjhospCHONwz9PkVQiLhGabrfSC1hbXIKQF1nz5FgVeyytQnEoeK_QFNvvCaDCcLN_X2zcIrD1yufoFq8X4APoUF7qQeJ76g=): 
  - [winesinniagara.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd8bQD9_vzeX0x4klOKHN59fM_7H3IdAQSTJRpR0CT0RVKHH1o676gQtWkIOKT55rJKBd87Syft6jVrsifmCtOiMax29I8WRbMR8kdvgnK4a_lmf563rkmh2hRZyfNa9hpF3EUbB3sXXtASfqgIH3KNK7m8Q-g_rYBg82thnuL8EvMs5jq7E6IBzzpGade5ZaAiO2mqC9m4WFIMw==): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWR0cpSEyZ0Vh1HIBUFYQ6ckutI2xR_CkA2Cnw_tq0jZKZ8cg4RjFbuaK-JQOCibL-jrrCr-h9ovQUOPLzLd-cPMWznWaCYHvlltSUJ3bHveiqnfbgk_LLVXog3tnDnbQ3w5ZexgzzMsTT9TIVupfVsHHnzk8XmHE0PLye6DVGo9S4IO-thLrGBfbuddUpYNRrP-AwWQ==): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtnRZXCyMZBiLC99ayv1lkaK3wQeMRdBES4aGxEGkCoKefiulAu3XMA_JayU21YZvkcvLtWhyFg9rGlF6vkM5xM9zPBP_mA0-690xpWbN4FFN5VjrjlT15d0poauoTnwZnpQh9q9mu5l5I3_-QhUBjU3Y9GJzeywr8-7EM4-oq): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERZItqaVomhQA3nnhfCrJH1hy3m3w8mDG5_vwF0EX1Ec0nGtReVmMTI7l_wfwHxN8qhsFjnu-tnFYBP7fto5jYQpVfY36B9c9IpVunjcP6HBmxUzmw9-X7rVDRUR6U1ZQrvr_SG3e_WHA9gN8ZiAVeCvWHPeCkCdoyqJ88ExhA-Q==): 

#### search_web_grounded_tool (status=ok, 11 results)
Search answer: Review scores for the **Tinhorn Creek Cabernet Franc** vary by vintage, with recent years receiving high praise from Canadian wine critics and competitions:

### **2022 Vintage**
* **National Wine Awards of Canada (WineAlign, 2025): Platinum Medal**. The judging panel highly praised this vintage, describing it as a lively, flashy, and youthful expression of the grape.

### **2021 Vintage**
* **National Wine Awards of Canada (WineAlign, 2023): Gold Medal**. 
* **John Schreiner: 91/100**. Schreiner noted that despite a very hot growing season, the wine remained bright, fresh, and highly drinkable with clean dark fruit flavors.
* **Wine Club Canada: 90–92/100**. The review highlighted its bold dark fruit, savory herbal undertones, and well-balanced structure.
* **Gismondi on Wine (Geoffrey Moss MW): 86/100**. Moss called it a strong effort for a challenging vintage, noting its balanced ripeness and classic herbal and dark berry varietal character.

### **2020 Vintage**
* **John Schreiner: 92/100** (Standard) & **94/100** (Reserve). Schreiner lauded the standard bottling for its spice and red fruit aromas, while praising the Reserve for its concentrated texture, oak integration, and exceptionally long finish.

### **2019 Vintage**
* **Natalie MacLean: 88/100** (Reserve). MacLean described the Reserve bottling as a ripe, juicy, and smooth red featuring vibrant red berry fruit, dried herbs, and toasty oak spice.

### **2015 Vintage**
* **Gismondi on Wine (Anthony Gismondi & Treve Ring): 90/100**. The critics highlighted its dark fruit profile and well-integrated oak aging.
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELGHVwZlofhNbWNKPh5HkR9IcPCPwr0rG4fzI2vNedJztww2fA5dQDMelsDM-tmNEDb9C0Yjt5aZm7PzlHA7NfGg2lSAmgeDsDyND1D307S4XrDyJmLN084wiOLr-c8qWFAg==): 
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIEnMZnvKT-oEM1POCjErypdfBPgc-Ia5O8f5EOyhXFJmA--o7mw-lQ5JcrRJwVv2MRZDLFA8DhEfeNXyM1NgsXnx1S4fOtT2uQP9yiijpdY-JXQntqVm6ldcN2Q_EIMOkJEe-kQ==): 
  - [alaymanswinemusings.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENFWqRf8IEHSalxKtOb_IxqiFmkG3WhCL83kIRZcfaUknAJgflJWJN7FAd1m6UPn2dJ0JMGMuT5jzzC3VyteCUlOFwRlAQKVOTgOtrCUIf6SLPEoOz1WCZaSOgrcGFnQilsAE6Oz69F4HUfkLIrHRFC-AvrxZ7hYB1HFjxEWmLF7vY3Zg=): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsiRe8xpAMLNR1Il4YuVCGXC0zt-W52udKva2bR_CEQkrWrdnyGi1CE998RfZDTooC2kZ3vU_l2GsWs0sCIfOrf1rNnJWWGyq984MfKbOHvPBixSyXx4-bhJSEw-TCHTsfyYJToPwx99p698U_inf9UP2m1oq6x6t1Zr3135xT7RQa1sP97xgMHdZGhbNhJbivPtS_UzV_s3O7cp6WaeFfen0Nyw==): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvKOfKaDP0WVd0-ITNQbRP0WpOVLfOMqtgG1uPIfK7dH8EpwyWS2WNaNfVAGuouZ_y52DTPOIO_NJscariRbM0XAMHo0E2eziqtLOnvvtXCBOu1WF-uEHtESUVmsHmHcQwD58qQuOu4c_xwDgagICbngxiyfoT_oxtPuolNYh0U94vfnzbfdAHuVmy4VQElThfjPGe6rgEdKmuqLFOlsMg9c1IoQ==): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzBUEhYoZ2wICbnJAky8bylQiWnJKJw-DSVaPFsN0nY3h4i4irBu74rekzKzp9a48FAX6JeGgCct8MGZvqEynUaLRliyzu4806ruJkr-siRnxCdw9bawAgszE5tme3rAqf2vMZ0GA2wnvtLaiT5usJ_A5WmOFA0Hx43pIMJjVSdLpEKzRuIbtZhw==): 
  - [wineclub.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsqMTRht0OWv9tpt3PhrAEyFA_WOm-_v6buDdmmgmaEfmaqS51sko2mQpcfRbsRudUX7hbqO131loA7E4esGZkitShzdUNKR86HSDHOk0aohZrYwr7I1R2dnF6mf01gBaU8-jB_ll35mij3zJBCu5KJ7dC6hfgYyuo1eCjIV4=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuWzz0mX3PRJHVIlewHMunhpTulZ02MK5yv28zClK8tJzEyHBUAEj4-Kd17rM7-ap4ujKGRzyUjxAF-30Bzpsd47gC45XwHO8IOO6fV-DM1IbYCHJa9pxFf7_aujFUrlmDLdz1E4TKFbB-q30uOvLWIHB2DS1e-dR6zWLfMyC6elv4pUUqnTiYCKIpHhs1L5xB9oB-c1dghyOg91u_H6s9-E4=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfIiQaFxmMNUFB_VuroSoxTAnz1WXqiqd7HnER1y-Kpxf2HiyrVenaaYe8eIg1cNAarpF9rJiwapbvam57ZmpmPAdNNBNvXHuQiVkziPY9D3SAra9upJK-M8phpGLbSP3QIX8fWFIGJCM2l69mS5Nh-evHSh6zX2ZsiqlPS3GlWt-tHHrcjqWB_m8d0WUXzLgDaSI2Om3jPA-8EO-ILlSzGmA=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFQKl7WWjiy2fGCCxzhlxz2dTX5pXtH2CKK5LEJDqvS0BUZmdcoFPIyom1MAMxGNtB1_Hvoys3vIXhPeEsbPShwUBZRdB8JlYwW7y308r4BQvlsLNw9fGpg-1_tevCCHMa_vIMDOhmJXXqEnob5zoV_S_LKIX8xwb787wN0awwNVcxiFLvoBjj9emFyPhnXScwz-K39G1dfU2w3kM5383Bug==): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRfTpK7J9Ec1NXcxn60vQ8Xp1_qq1UyoicL6cCNp1XJnBZ4qzb7Fl6kdZBHo6zGJs7HaTMIwCx5Z9bocb_A8dTznEV0Zl6x57aikRCvcBwQwwwEJSOKrbUiTw0wSpNHn9YuMWppGCqmZDZ7XP1kP5WSfTrs7n8ExbhMZcJg0aY_sN-r7LS_BkLJhPjyryT-OvBKknyt3SWaA==): 

#### search_web_grounded_tool (status=ok, 10 results)
Search answer: Bartier Bros. (located on the Black Sage Bench in Oliver, BC) has historically produced highly regarded Syrahs from their Cerqueira Vineyard. Due to devastating winter freezes in late 2022 and early 2024, the winery unfortunately had to pull their Syrah vines, making the 2022 vintage one of their final estate Syrah releases. 

Review scores and tasting summaries from prominent Canadian and international critics include:

### **2022 Vintage**
* **John Schreiner (Goodgrog): 90 points**  
  Schreiner noted that this vintage (which includes 7% Merlot) offers a generous texture with aromas and flavours of dark fruits and black pepper, leading to a long finish.

### **2020 Vintage**
* **Treve Ring (Gismondi on Wine):**  
  Ring praised this vintage for its plump, ripe palate of blackberries, black cherries, and dusky plum, balanced by bright stony acidity and a peppery, violet-kissed finish. 
* **Wine-Searcher:** Lists an overall average critic score of **89/100** across all vintages.

### **2018 Vintage**
* **John Schreiner (Goodgrog): 91 points**  
  Schreiner highlighted its bold palate of cassis, black cherry, and mocha, supported by long, ripe tannins and a persistent finish.
* **Anthony Gismondi (Gismondi on Wine): 90 points**  
  Gismondi praised its open nose of sweet cassis and violet, its silky, savoury palate of wild blackberry jam, and its strong minerality.
* **Decanter World Wine Awards: 90 points**

### **2016 Vintage**
* **Natalie MacLean: 92 points**  
  MacLean described it as a beautifully balanced, full-bodied, and velvety Syrah with ripe blackberry, dark plum, and warm smoky notes.
* **Jennifer Havers (WSET Level 3): 91 points**

### **Related Blend: Grenache-Syrah (2021 Vintage)**
If you are looking for their popular Rhône-style blend:
* **Rick VanSickle (Wines in Niagara): 93 points**  
  VanSickle praised its Rhône-like character, noting peppery red berries, anise, and wild blueberries on a smooth palate.
* **WineScores.ca: 92 points**
  - [foodindustrynetwork.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpMLbTsluHvTzfnagglPCeC3-bTOIblIqBy4yuzmS2L3Y3aBrQKz1KyLogNw0wra7AQbIW_asO54v3NPDzr42DSQ5dqYLFQ0ZGWWZWRV7b-SjqNgbzqkfOR8bewtffA5De5xqmkVrlLf35-oR7JkDLeIqLnjd-ZYR6Bl0HX_wqz89YEAFhMd0a8wc=): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjYzEqoAJe2jib7LxTmJsdMqrlmMdAFPiZfZzwhkinj85pg-WaGHtN9XyR5SB7KEMeTjxptgPqEU2dRZgLkMncsXCtD4yqNIObBCG3PgYugh5-BO4CsMJYWIDkCO8tXr4CTNx_5iiLx8A3ERg75E0Zwr7rkFXWis4b1Bd_l4rd39jVqbw0MSbUaTIhnQ==): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLXtRY_gwu-CISdnVqDjvI8Y2J2Fe-XmVbQU1Wz9PjALQLgDv5lSWjXBnbhieBBrzcZHgijM25IU_tdVTP7iYlYbkREf6p2LMoiMQNtM-UTHcped5DdRz5mOWSHhcI1d_MAX_2szuYU2cKwtG5HpZAhth3ekIzWtW9DvutUXwd0nurvH02tinRAqLsEBM=): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv736K4t1G0IlP4s7TsdVfiq0BeIRHDsPalljC9EyRQdh-yT03WYxwtZiuwx4HQc56Ewglo0EueFWYxgPlnrkXf0iklsQHYFpfjAxkEYatQrD3A0gzMFcE4d52YgGaIN3NiiLwMLNnrIKpueCqZbvK4zBZ3Bu6Z3Hx8U2bodmmWIuujNadOZAM59fo8g==): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtOpFeqKO40cCzDm3fjVyWoQAuYgnUXdxfhxLn5wxLkMn1iRUAi5ycZHIIUOlMVJoncQBNcAUqzT7mYAE8CrWpeC0uh4JvqIC8VjkJfKh4ZK3d94Np8UsVnmayPijxc7r1gcOIvQ==): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbGNXxQnWCKfsnCAvyyD3CheYsQtASvgDt1Er4A6eiXUIZGcazatUSML64T3_JpYN-kWGOcfDIQYGSUVFo9KEOj1UX--yuBK1nf8tCkOp5IoMQqauKBsc-sb2JtoEEWq5Wt8Z8Ma6nu_ZmTTXlCASIEBS0bXcy9pmrS-Fm9zdoK-9PXg75kSFqjc5IGcjUkj0Tssja3RP-vck=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRfa4zkhzm0PeO7W0pm3mQSs3OPmIxtyz6hEKy5IsEA-Gt7aO__N3e7FiL7ggIuOaQ8g-i-MQ_v5SwXQMgrpPRxUil8rmpVjUkvQNSQygu_MrsWZBOMbMsa6MTbFYLQlIfEyXxRJf56oP7_XOT23Yx7gKr17Oehy2yN7f5w4RcSbIuK_TSePlNxPvYcv0k2YuXTTmtd06e83V3): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWyLIVADQlgq26hbof0zEPgXCapk92DaORUzpueY86D-e6lBFEkrkpkF6P6wxN8iyak3jOaQGa-3UXTIgNn8ZH4_ZdOMx1OkqvQopI1gLRBo6vMO2z5AnlAEAKorsbDFkFEnwghfH9UB9jEVKBjm8T5qibJjFxZdOsqBF87xlTNdJdEogcriKtyjb2GQXkXT6XoyJ6FLvY): 
  - [winesinniagara.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvy_X6q-AxigtcUQ_leji-t3HI-SliAjK448S2y-Jh9m0_rjEYIt2usrg1Q_vqH9HvOf6u8FIHn9q25IJm3dI8jmCpVccXdRyX0JlAg0sSLQ-zMIowmiOxuIhZd5vInnemhK57ePbef4XHzY3ru4t-uY9O3UqOrU3LUwL-0wJg8FFGOmJ2HCC8SGza-IsGqw7Fa3k8Xv7Ut_-wvDpkP5f0DNJm): 
  - [winescores.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIKsxM3R5swcDaZ6sUi7CCkdb1iKPDx-xRMpz4KNxHzCk5Du3ueJ7JsOq9EHRDmupXW2jGr6OHAormz_NBGtvNWWMnZZN7iy_-5-_rmtl6dPM94C7PhjfYQbr_1CbSFSNx7YJr3PuV5v-dNyWny_3UHhV0Can-Lr2vl9X_OTbgLGxJ3SodKRSI00cIpkL6IovEdEpdCSDYv3Q6ORDbMLKS5iwDz8poKyxYBBvfFiZBr_nkWROGmOA1byroK5WPsejajWNYQodcCG4negBmDL057WuMvsGAqh8lq1h0qf-wP2ByI1zhatWqPGCsLXC2sZrYsklUg6JpkSY1heeqcihRq44=): 

#### search_web_grounded_tool (status=ok, 11 results)
Search answer: **Artisan SakeMaker’s Osake Fraser Valley Junmai – Renaissance** is a pioneering Canadian sake crafted by maker Masa Shiroki on Granville Island in Vancouver, BC. It is notable for being a "farm-to-glass" sake made with 100% British Columbia-grown Ginpu sake rice cultivated in Abbotsford (Fraser Valley). 

### Tasting Profile & Reviews
* **Sip Magazine:** In a review of the Pacific Northwest sake scene, the publication described the sake as having an aromatic profile of sweet hay, meadow herbs, honeysuckle, and hazelnut. On the palate, they noted a predominantly herbal and moderately honeyed character, balanced by a crisp acidity over a sweet cereal base.
* **Elle Canada & Air Canada’s EnRoute Magazine:** Both publications highlighted the sake as rich, savoury, and complex, praising its racy acidity and delicate touch of sweetness. 
* **Wayward Wine:** An early review of the Fraser Valley-sourced batches noted that the local rice yielded a sake that was waxier, drier, and more mineral-driven than the producer's standard Calrose-based Junmai.
* **The Producer's Profile:** Artisan SakeMaker describes this off-dry sake as having an unprecedented level of acidity, complex flavours, and a mature, superior balance designed to appeal to modern wine aficionados. 

### Awards
* **Judge's Selection** – Alberta Beverage Awards (2016)
* **Silver Medal** – NorthWest Wine Summit (2017)

### Food Pairings
Because of its pronounced acidity and savoury umami profile, this sake is highly versatile at the table. The winery and local critics recommend pairing it with:
* Charcuterie and cheeses
* Roasted chicken or pizza
* Miso/kasu black cod or seafood chowder
* Richer Japanese dishes (it has been featured in premium local kaiseki pairings at Vancouver's Kishimoto restaurant)
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSq8-ToUuBYthqbn5fUM3JBPsL7BPJ3X9xjKdw8v92-HunYuF3aIj02MMWq9YNCPcWv60IUKm-8caM077wcYRY3TlsuLlRdVWN0XlAuUiNCQAHmw3vR3jE): 
  - [sipmagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkaiGI53_ioX7vNqaLXTjeJa1cLQziIQqK_VzkBOdhSkH1EEWzfRMQ2kh5RHhHzQ_emu2ApbU4AIoNJUb_hYozOaY2RjIyMWx5Gfnfdpcs-Lh9pprbha0fOQYtTe5da2e_EVR5AK8gfz-onxiLLA==): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8d8M0jCiKH5H6KM57mnKCS0x6Lt3pAawCfezEg6kCWQPVj_JMSr5nVt7yNYKaTcHM2Um0xao9sKRHzp790fVeihJuw9TPejxGHoneL34lmLPZGyhEsXYL86pHEoGmxFU8-5ZY0FFE6lXmgOYu1WncxdkwxvA9mk7_NhtCBkxuxzUPQ5Yaxw==): 
  - [ellecanada.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4MwDAa_N02gADMiTFOzXAGJkWycuSLsFZQVu6h06VMJ5H3UOLZ0ZLEwlVB5Is-rmHx2YCT9V5iTqnKR-1INIlqJgQpnwow5T0kGqXxI3z1UX6er0gCVCIPvYcXDDmoUNJlnvrJM-1XbLYz1rPBaQGNMSi2RreMcHwf4faZV4iaa8bikLL_cxc5d40xRkKYCTEGYiyLwIzrCisTEmSBFs-G1SyCyAmkuPN): 
  - [ellecanada.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSrB2oBADbD3ZB0-aI6bxJ1zmm0UbtWNTD8HxbYfFNvltmQ9AwL4Q9VftSRGNdCyb1k14ATPV5ThSZ3IPVMPJ7jyH2tmub_A-sO5QwKRtd6sj06sKmzLZss12X9jAd88l5eYBj66jfupnPm2SECP6ZkIdMsvw39BNhoZ4H--LKPYPzcizjRWFBY9Rn4FhoBDZBOWVceqYx9rxjrQ==): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcdkulyyXTtr_liC5RSEq2ef_Ht4UYlpI0_sKj6xKLkIoTrxyP4Uz1pJNFNPA44XN9IC6HDEdcSorCHoZZcAkAOAeUfzUSPeF5sK8EgnMZAkAZKKEH2HlBxN7hW9xH_S2fzP4zDVEx71GssN9_tqvLJqvq7AYYJQlNORVeMDeTRP4hQQU1fgWulUZFBXAGYOhemg==): 
  - [waywardwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQwqxbeZQFt4NxBIrr-6AraP-2SOVO_NVoDHa8ea14mOfS7vesrLhAdXGsmr5g0EyCkV19tIJG1PuWhnBPbAlecyhddZ0XrVfBep6zdUbXtpcoyzO64DaV0h38hp6gdDRcCN7Nt7dVw-Kg): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAGkw34IO3ZX9tte2hCbZM1sF0HeNTU8XgY--LBV9qWBNQsLFLAlkQAmhq0ym-QJ_llf8bWhE_xIW42fv4zjNYrL9U_VLL-sN4mcBkwFwm3zG6Nsgq7shvZkTIxq-OVIl6EpJrqB3JoQc-): 
  - [wixsite.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH95Pn1PPx6mwLYkcnPYj2vDa6Zdnl1lujLDtay8HWLm7O9SdwUQbfFfW8jatWMgDcHqJzPXkmfs1jazkpBncKyZHRG68FCq_peZW-sF1JPzNS2MQ8tyRy7bdV-NHTwkOPp95WHBEkS3EgzVYYAl4sbHmxOEF6q8c95ncjWiBZUoWKuOAgsWK7sqJGEzx-b_Vj8Vpcoq_RHyOPkIgq18lPqXRdQTdU=): 
  - [pendulummag.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBrheJYeHa1AYUMvbDKbrj8efju4eSLoVJ5UHukqCpgxdzyOjapdU9HHvc8gTmg4nFAtaKPKfIZlGzSKd1i9MPi9bQAQNKPBLKTD5xF2jRiWm9o52v2OIXgJzvxic85CXc_2hgAW7z2grlOgvKiB_j_QuDKVkHU_7amInK2z9hIHw7pqJQwLHbfDHl6cGhMgx6QsY3fltAR8noWpIQxdpAb4GdI2KkF86pLMkl-JCN5fYJH9K_kY5Y): 
  - [myvancity.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV1CBb1o2UJ7-qGnQZ3SmID9xv8ygcofTG8mCsN1yi0w5aPMI18iEYEeIB6OwEvfxftXhOUP6Nu-LN7WQq6M6eY_AIVmb3Lfa457djTjYfhSRcqLD9wX2XK-xBbQlAa8pnp9G7xtHckOHqXOhX_91M4JdBeRVOC14I): 

#### search_web_grounded_tool (status=ok, 6 results)
Search answer: **Odd Society Wallflower Gin** is a signature craft spirit produced by Odd Society Spirits, located in East Vancouver, British Columbia. 

### Overview and Production
Wallflower Gin is crafted from a base of 100% BC-grown barley. It is distilled in small batches using a custom-designed copper pot still that utilizes both maceration and vapour extraction to infuse a mix of local coastal and international botanicals. The gin is bottled at 44% ABV.

### Tasting Notes Summary
* **Nose:** Reviewers describe the aroma as highly aromatic and floral-forward. *BC Spirits* highlights notes of woody lavender, spicy juniper, and earthy botanicals. Other reviews, such as one from *Gingineerist*, note elegant coriander and soft floral tones, while a community review on Reddit points to bright citrus elements like mandarin orange zest and yuzu.
* **Palate:** On the palate, the initial floral sweetness subsides to the background. *BC Spirits* notes that the spirit leans into a complex, piney, and classic juniper-forward profile. *Gingineerist* describes the taste as bright, delicately sweet, and clean, while the Reddit review highlights a unique combination of mandarin orange juice, pink peppercorn, and herbal chartreuse-like notes.
* **Finish:** The finish is widely regarded as long, clean, and complex, with lingering juniper and soft, elegant floral notes.

### Serving Recommendations
* **In a G&T:** *BC Spirits* recommends Wallflower as an excellent choice for a classic Gin & Tonic. *Gingineerist* suggests pairing it with a light, dry tonic (such as Fever-Tree) or club soda with a citrus peel garnish to avoid masking the gin's delicate floral sweetness. 
* **Neat:** While it can be enjoyed neat, reviewers note that mixing it with tonic particularly helps to amplify its lavender and citrus characteristics.

### Notable Variants
Odd Society also produces two popular spin-offs of this flagship gin:
* **Wallflower Oaken Gin:** An expression aged in oak barrels. *BC Spirits* describes it as a rich, full-bodied gin that balances the original botanicals with sweet pine, vanilla, and dry oak, making it an excellent substitute for whiskey in an Old Fashioned.
* **Strawberry Wallflower Gin:** A seasonal variation steeped with fresh Fraser Valley strawberries from Driediger Farms. It offers a pink hue with a sweet, juicy strawberry nose and a tart, refreshing palate.
  - [bcspirits.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa-p5_Ur2o85FDPWXET12jCWzL_3LhSGm6eTJmm7ltGVC2KPRewl6Qs53fO76Tyun6EpHpeVUwV9Ws4kUCTYINySv4bNHZmF-Lc3mD8xTVBVwPvKoftyT0RsNwjvwlsiosVBlOsFHCVh5--mSU2xK2uCLDuqF7ElHwA7Z_JkT2KqIKwyvOKB-1o65c0pEpGw==): 
  - [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrr4YT7labFoDptf1pvMcDT4N87-Pke91G-AQg1jDddrFF-_ChUa9_4SV-nTevfcl0-A_wJ2drljwJlSVRnLhgLpp00WWfxk428KMV9M_VZzXUVzLrgKUv9cPglLYC86_dHXw-GJPZHS2EjZG1sOpXFc9ER4HFccYbS_BZ7hf2ePJ1BIcIvGIt1W4qQVVEkrx3VZzVZE5D6Q==): 
  - [edgefurnish.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI_ipSe0sohL0TWlB0JJ_bYZf6pOOBEJTbC5z3VaTUZypG01Vl4yRZq3FY_ZEwwG8V_pnlJS7HuedRmoDSTJRuEj2OdDW7WTV3v8HUDvibYInkjtGXZO3T5IU_nBkhf4xPVOCWaboERS9zQ7OoidkZHV0dDxc=): 
  - [iscotch.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4HZ9hHoRk8VwMXXgcd1s5IoymPAhmGc86JEZyHD-TXzzlJrYWNiHC8slTxovfKKmlJTN_BX7-z7XGDwnOQ4O55b8GgkPkEjRZmwqAzN1k0nT_1CRYqBnYvyNN0Es95kHuKYhVqP-p7qhhHGxqTee1wKVct8u55HZl): 
  - [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRjEYCTUDVuuS8AXx09verpkJ9kLZ4BFR3FW6IUp7Kj2TBz56pZ1XvLxJKR2-e5bW4rh6w96j0pilMZNZUzuFBR6qx9X0HPC-MvjAmnVtcIVgh0erLJZkJsrG0pEuvrNR0IPslGg==): 
  - [thedrinkguy.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc7219EKT7dE3huZ6eBwasiD3Ev_Z72i0huNZiIvYM3jZ9x-QS_b_8HBaWauvL76UC6bjVN6F7tP111lMSxeKEx-e61XlYRJwBG8PvUHx-k20eOtPeoSNWg72bmOBnxzN1mf5wLrNQQT_ihZ9P1SZgF0jwk7XBrtZrhqDnR9ghNW6XTUtf8AvXIOulLxuVEaHTmxyp0ouaC2NHEykY): 


### sourcing_agent_tool (status=ok)
**Sub-agent synthesis:**
Here is a curated list of BC red wines under $35 that are currently **in stock** at Vancouver retail locations. 

---

### **Sutton Place Wine Merchant** (Yaletown, Vancouver)
*Boutique selection with exact stock quantities.*

* **Clos Du Soleil Célestiale 2019** (Red Blend) — **$34.99** (41 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4205421-clos-du-soleil-celestiale)
* **Blue Mountain Gamay 2020** — **$33.99** (4 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4228470-blue-mountain-gamay)
* **Bartier Bros Granite 2021** (Red Blend) — **$32.99** (12 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4944430-bartier-bros-granite)
* **Bench 1775 Syrah 2021** — **$32.99** (2 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4571295-bench-1775-syrah)
* **Bonamici Cellars Merlot - Cabernet Franc 2021** — **$32.99** (7 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4143755-bonamici-cellars-merlot-cabernet-franc)
* **Bench 1775 Cabernet Sauvignon Merlot 2019** — **$31.49** (5 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4571291-bench-1775-cabernet-sauvignon-merlot)
* **Averill Creek Joue Red 2021** (Red Blend) — **$29.49** (6 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4143614-averill-creek-joue-red)

---

### **Marquis Wine Cellars** (Davie St, Vancouver)
*Curated boutique selection with exact stock quantities.*

* **Meyer Family 2023 Pinot Noir** — **$34.99** (12 in stock) | [Buy here](https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/)
* **Pamplemousse Jus 2025 Foch Nouveau** — **$34.99** (8 in stock) | [Buy here](https://www.marquis-wines.com/pamplemousse-jus-2025-foch-nouveau-750ml/)
* **Nichol 2022 Cabernet Franc 'The Village'** — **$32.99** (4 in stock) | [Buy here](https://www.marquis-wines.com/nichol-2022-cabernet-franc-the-village-750ml/)
* **Quails Gate 2022 Old Vines Foch** — **$31.99** (2 in stock) | [Buy here](https://www.marquis-wines.com/quails-gate-2019-old-vines-foch-750ml/)
* **Vasanti 2022 Cabernet Sauvignon** — **$31.99** (10 in stock) | [Buy here](https://www.marquis-wines.com/vasanti-2022-cabernet-sauvignon-750ml/)
* **Cassini 2023 Pinot Noir "Red Carpet"** — **$29.99** (24 in stock) | [Buy here](https://www.marquis-wines.com/cassini-2022-pinot-noir-red-carpet-750ml/)
* **Lock & Worth 2023 Merlot** — **$27.99** (9 in stock) | [Buy here](https://www.marquis-wines.com/lock-worth-2022-merlot-750ml/)
* **Tinhorn Creek 2023 Cabernet Franc** — **$27.99** (47 in stock) | [Buy here](https://www.marquis-wines.com/tinhorn-creek-2023-cabernet-franc-750ml/)
* **Three Sisters Bench Red** — **$25.99** (4 in stock) | [Buy here](https://www.marquis-wines.com/three-sisters-bench-red-750ml/)
* **Gray Monk 2021/24 Pinot Noir** — **$24.99** (18 in stock) | [Buy here](https://www.marquis-wines.com/gray-monk-2019-pinot-noir-750ml/)
* **Domaine Artema 2022 Black Sage Road Rouge** — **$24.49** (14 in stock) | [Buy here](https://www.marquis-wines.com/domaine-artema-2022-black-sage-road-rouge-750ml/)
* **Mission Hill Five Vineyards Cabernet/Merlot** — **$20.99** (68 in stock) | [Buy here](https://www.marquis-wines.com/mission-hill-2018-five-vineyards-cabernet-merlot-750ml/)

---

### **Everything Wine** (River District, Vancouver)
*Exact stock quantities for the Vancouver store location.*

* **Crown & Thieves Scoundrels Punch Red Blend** — **$34.98** (9 in stock) | [Buy here](https://www.everythingwine.ca/crown-thieves-scoundrels-punch-red-blend-750-ml)
* **Evolve Cellars Momento Red Blend** — **$24.99** (3 in stock) | [Buy here](https://www.everythingwine.ca/evolve-cellars-momento-red-blend-750-ml)
* **Narrative By Okanagan Crush Pad Red Blend** — **$24.98** (18 in stock) | [Buy here](https://www.everythingwine.ca/narrative-red)
* **Chaberton Estate Winery Red Blend** — **$23.98** (4 in stock) | [Buy here](https://www.everythingwine.ca/chaberton-cuvee-rouge)

---

### **BC Liquor Stores** (Multiple Vancouver Locations)
*Widely distributed across Vancouver government stores. Prices are standard.*

* **Daydreamer Jasper Merlot Cabernet** (BC VQA) — **$32.99** | [Buy here](https://www.bcliquorstores.com/product/768408)
* **Mt. Boucherie Reserve Meritage 2024** — **$29.99** | [Buy here](https://www.bcliquorstores.com/product/658474)
* **Hester Creek Syrah** (BC VQA) — **$27.99** | [Buy here](https://www.bcliquorstores.com/product/504399)
* **Screaming Frenzy Meritage** (BC VQA) — **$26.99** | [Buy here](https://www.bcliquorstores.com/product/179372)
* **Mt. Boucherie OV PTG** (BC VQA Pinot Noir/Gamay) — **$25.99** | [Buy here](https://www.bcliquorstores.com/product/78218)
* **Modest Wines Blaufränkisch** (BC VQA) — **$25.99** | [Buy here](https://www.bcliquorstores.com/product/369760)
* **Gneiss Pendulum** (BC VQA Red Blend) — **$25.99** | [Buy here](https://www.bcliquorstores.com/product/399223)

#### search_bcliquor_tool (status=ok, 48 results)
  - PHANTOM CREEK ESTATES - BC ROSE 2025 | $29.99 | stock=804 | in 73 stores | rating=4.6 | https://www.bcliquorstores.com/product/329902 | {sku=329902; product_type=Rose Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=From the dedicated blocks of Becker, Ryegrass, Richter and Evernden Spring Vineyards, Phantom Creek Estates Rosé reflects the complexity that comes from our organic-certified terroirs of the Okanagan and Similkameen Valleys. It is dry, finessed and nuanced, with delicate red berries and layers of spice.
; consumer_votes=35; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/329902.jpeg; certificates=["BC VQA", "All VQA"]}
  - GRIGNOLINO DEL MONFERRATO CASALESE - ACCORNERO BRICCO DEL BO | $31.99 | stock=58 | in 8 stores | rating=4.6 | https://www.bcliquorstores.com/product/63584 | {sku=63584; product_type=Red Wine; grape_type=OTHER GRAPE VARIETY; country=Italy; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=92 Points, Vinous: "The 2020 Grignolino Bricco del Bosco is a classic wine from this often overlooked red variety. Ethereal and weightless in the glass, the 2020 offers up scents of rosewater, cinnamon, orange peel, mint and sweet pipe tobacco, all framed by silky tannins that lend finesse. What a beautiful wine this is. Drinking Window: 2022 - 2028." (January 2022)
; consumer_votes=74; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/63584.jpeg}
  - SAUMUR CABERNET FRANC - DOMAINE DE ROCHEVILLE LES PIERRES BL | $28.99 (reg $32.99) | stock=261 | in 25 stores | rating=4.6 | https://www.bcliquorstores.com/product/192945 | {sku=192945; product_type=Red Wine; grape_type=CABERNET FRANC; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=On the palate, the wine is vibrant and well-structured, showcasing a core of bright red fruit, cherry, raspberry, and wild strawberry. Balanced by refined tannins and lively acidity. Delicate notes of graphite and gentle spice emerge with aeration, adding complexity and finesse. The finish is long and harmonious, with persistent red fruit flavors and a subtle savory character that lingers gracefully.
; consumer_votes=6; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/192945.jpeg}
  - RED TRUCK -  ORIGINAL PILSNER CAN | $27.99 | stock=1435 | in 95 stores | rating=4.0 | https://www.bcliquorstores.com/product/669034 | {sku=669034; country=Canada; volume=0.355; alcohol_pct=5.0; consumer_votes=16; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/669034.jpeg}
  - PARALLEL 49 - TRICYCLE GRAPEFRUIT RADLER TALL CAN | $2.99 | stock=7016 | in 107 stores | rating=3.3 | https://www.bcliquorstores.com/product/294962 | {sku=294962; country=Canada; volume=0.473; alcohol_pct=3.5; tasting_notes=A crisp lager infused with ruby red grapefruit for a refreshing, citrus-forward experience.
; consumer_votes=61; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/294962.jpeg}
  - RED TRUCK - LAGER CAN | $16.99 | stock=2129 | in 143 stores | rating=4.0 | https://www.bcliquorstores.com/product/4215 | {sku=4215; country=Canada; volume=0.355; alcohol_pct=5.0; tasting_notes=This traditional European-style lager is made with all Canadian malts and Saaz hops, a classic "noble" aroma hop with longstanding traditions just like the style itself. Clean and crisp in style, this lager is designed to be an easy-drinking, full-bodied beer that doesn't compete with anything you're eating.
; consumer_votes=210; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/4215.jpeg}
  - RED RACER - SESSION IPA 4PK | $10.99 | stock=2737 | in 118 stores | rating=3.6 | https://www.bcliquorstores.com/product/711396 | {sku=711396; country=Canada; volume=0.473; alcohol_pct=4.0; tasting_notes=Crisp and light-bodied with vibrant grapefruit and pine notes. A balanced citrusy hop character complements a subtle malt backbone, delivering a clean, refreshing finish ideal for warm weather sipping.; consumer_votes=9; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/711396.jpeg}
  - RED TRUCK - ORIGINAL LAGER TALL CAN | $1.99 (reg $2.69) | stock=7597 | in 94 stores | rating=4.3 | https://www.bcliquorstores.com/product/711680 | {sku=711680; country=Canada; volume=0.473; alcohol_pct=5.0; consumer_votes=13; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/711680.jpeg}
  - BODACIOUS - BOURBON | $11.99 | stock=2516 | in 169 stores | rating=3.9 | https://www.bcliquorstores.com/product/165991 | {sku=165991; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=12.0; sweetness=02; tasting_notes=Rich, bold, smooth and tasty, with aromas of black cherry, vanilla and spice.
; consumer_votes=139; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/165991.jpeg}
  - BODACIOUS - CABERNET SAUVIGNON | $11.97 | stock=1069 | in 108 stores | rating=3.6 | https://www.bcliquorstores.com/product/430959 | {sku=430959; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=02; tasting_notes=Juicy, ripe and robust, with aromas of blackberry and blackcurrant.
; consumer_votes=183; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/430959.jpeg}
  - MT. BOUCHERIE - RESERVE MERITAGE 2024 | $29.99 | stock=1569 | in 142 stores | rating=5.0 | https://www.bcliquorstores.com/product/658474 | {sku=658474; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=13.3; sweetness=00; consumer_votes=1; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/658474.jpeg}
  - RED TRUCK BEER - HARD DAY NORTHWEST IPA 8 CAN | $14.99 (reg $17.49) | stock=1738 | in 140 stores | rating=4.1 | https://www.bcliquorstores.com/product/136901 | {sku=136901; country=Canada; volume=0.355; alcohol_pct=6.3; tasting_notes=Crystal malts balanced with a truckload of hops bring you a toffee malty sweetness with a dry fresh finish. This IPA will stand up to even the most intense dishes. Take it for a spin with the spiciest wings you can find.
; consumer_votes=93; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/136901.jpeg}
  - RED TRUCK - ORIGINAL IPA TALL CAN | $2.59 (reg $3.19) | stock=9526 | in 109 stores | rating=3.5 | https://www.bcliquorstores.com/product/295168 | {sku=295168; country=Canada; volume=0.473; alcohol_pct=6.3; tasting_notes=The "Original IPA" stands as the cornerstone recipe behind our acclaimed IPAs. Crafted with a nod to to a simpler era, this original masterpiece combines late kettle additions and a touch of dry hopping, capturing the true spirit of the Pacific Northwest; consumer_votes=20; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/295168.jpeg}
  - RED TRUCK -  ORIGINAL IPA CAN | $29.79 | stock=2438 | in 149 stores | rating=3.8 | https://www.bcliquorstores.com/product/379076 | {sku=379076; country=Canada; volume=0.355; alcohol_pct=6.3; tasting_notes=The "Original IPA" stands as the cornerstone recipe behind our acclaimed IPAs. Crafted with a nod to to a simpler brewing era, this original masterpiece combines late kettle additions and a touch of dry hopping, capturing the true spirit of the Pacific Northwest - the very region in which our brewery was founded.
; consumer_votes=106; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/379076.jpeg}
  - BODACIOUS - SMOOTH RED | $19.99 | stock=2343 | in 163 stores | rating=3.5 | https://www.bcliquorstores.com/product/39313 | {sku=39313; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=1.500; alcohol_pct=12.5; sweetness=02; tasting_notes=A bold, ripe, juicy and full-bodied red that blends together Merlot and Cabernet Sauvignon. Rich flavours and aromas of blueberries and blackcurrant are present from start to finish.
; consumer_votes=211; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/39313.jpeg}
  - DOMAINE D'OR - RED | $37.99 | stock=1609 | in 165 stores | rating=3.5 | https://www.bcliquorstores.com/product/108688 | {sku=108688; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=4.000; alcohol_pct=11.5; sweetness=00; tasting_notes=A medium-bodied wine with aromas and flavours of ripe red berries, strawberries and cherries.
; consumer_votes=71; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/108688.jpeg}
  - MISSION RIDGE - PREMIUM DRY RED | $37.99 | stock=1669 | in 177 stores | rating=3.5 | https://www.bcliquorstores.com/product/215590 | {sku=215590; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=4.000; alcohol_pct=11.0; sweetness=01; tasting_notes=A well-balanced red wine with supple tannins and notes of cassis. The finish is velvety with notes of spice.
; consumer_votes=166; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/215590.jpeg}
  - BODACIOUS - SMOOTH RED | $11.99 | stock=3599 | in 194 stores | rating=3.6 | https://www.bcliquorstores.com/product/459677 | {sku=459677; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=02; tasting_notes=A bold, ripe, juicy and full-bodied red that blends together Merlot and Cabernet Sauvignon. Rich flavours and aromas of blueberries and blackcurrant are present from start to finish.
; consumer_votes=446; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/459677.jpeg}
  - RED RACER -  WEST COAST IPA CAN | $10.99 (reg $12.99) | stock=3172 | in 144 stores | rating=4.0 | https://www.bcliquorstores.com/product/663977 | {sku=663977; country=Canada; volume=0.473; alcohol_pct=6.5; tasting_notes=The IPA was fashioned to survive the long voyage from England to India during the British colonization. Hops, hops, and more hops! Red Racer IPA has an intense aroma and a long lingering finish. A beer for the connoisseur, this is the brew master's choice.; consumer_votes=4; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/663977.jpeg}
  - PELLER FAMILY VINEYARDS - CABERNET MERLOT | $42.99 | stock=1778 | in 160 stores | rating=3.4 | https://www.bcliquorstores.com/product/617696 | {sku=617696; product_type=Red Wine; grape_type=CABERNET/MERLOT; country=Canada; volume=4.000; alcohol_pct=12.0; sweetness=00; tasting_notes=Rich aromas of black fruit are followed by a smooth, fruity finish that goes well with grilled meats and pizza.
; consumer_votes=70; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/617696.jpeg}
  - CALONA - ROYAL RED | $16.99 | stock=1328 | in 168 stores | rating=3.2 | https://www.bcliquorstores.com/product/2303 | {sku=2303; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=2.000; alcohol_pct=12.5; sweetness=04; tasting_notes=This semi-sweet red wine is perfect for drinking on its own or for making summer sangria. It pairs well with chocolate desserts.
; consumer_votes=128; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/2303.jpeg}
  - DOMAINE D'OR - RED | $15.99 | stock=1291 | in 150 stores | rating=3.0 | https://www.bcliquorstores.com/product/87965 | {sku=87965; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=1.500; alcohol_pct=11.5; sweetness=00; tasting_notes=A medium-bodied wine with aromas and flavours of ripe red berries, strawberries and cherries.
; consumer_votes=58; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/87965.jpeg}
  - BODACIOUS - SMOOTH RED | $44.99 | stock=2643 | in 197 stores | rating=3.9 | https://www.bcliquorstores.com/product/125680 | {sku=125680; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=4.000; alcohol_pct=12.5; sweetness=00; tasting_notes=A bold, ripe, juicy and full-bodied red that blends together Merlot and Cabernet Sauvignon. Rich flavours and aromas of blueberries and blackcurrant are present from start to finish.
; consumer_votes=71; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/125680.jpeg}
  - RED TRUCK - CLASSIC LAGER CAN | $19.99 (reg $27.99) | stock=6331 | in 157 stores | rating=4.0 | https://www.bcliquorstores.com/product/36577 | {sku=36577; country=Canada; volume=0.355; alcohol_pct=5.0; tasting_notes=This traditional European-style lager is made with all Canadian malts and Saaz hops, a classic "noble" aroma hop with longstanding traditions just like the style itself. Clean and crisp in style, this lager is designed to be an easy-drinking, full-bodied beer that doesn't compete with anything you're eating.
; consumer_votes=217; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/36577.jpeg}
  - MT. BOUCHERIE - OV PTG | $25.99 | stock=561 | in 51 stores | rating=4.0 | https://www.bcliquorstores.com/product/78218 | {sku=78218; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=14; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/78218.jpeg; certificates=["BC VQA", "All VQA"]}
  - MT. BOUCHERIE - RSV GSM | $39.99 | stock=451 | in 27 stores | rating=5.0 | https://www.bcliquorstores.com/product/130708 | {sku=130708; product_type=Red Wine; grape_type=GRENACHE/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; consumer_votes=1; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/130708.jpeg; certificates=["BC VQA", "All VQA"]}
  - HESTER CREEK - GARLAND 2015 | $79.99 | stock=109 | in 21 stores | rating=5.0 | https://www.bcliquorstores.com/product/145362 | {sku=145362; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=2; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/145362.jpeg; certificates=["BC VQA", "All VQA"]}
  - MODEST WINES - BLAUFRANKISCH | $25.99 | stock=260 | in 36 stores | rating=4.3 | https://www.bcliquorstores.com/product/369760 | {sku=369760; product_type=Red Wine; grape_type=OTHER GRAPE VARIETY; country=Canada; volume=0.750; alcohol_pct=13.4; sweetness=01; consumer_votes=3; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/369760.jpeg; certificates=["BC VQA", "All VQA"]}
  - GNEISS - PENDULUM | $25.99 | stock=430 | in 27 stores | rating=4.6 | https://www.bcliquorstores.com/product/399223 | {sku=399223; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=13.7; sweetness=00; consumer_votes=5; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/399223.jpeg; certificates=["BC VQA", "All VQA"]}
  - KALALA - ASPIRE | $30.99 | stock=11 | in 1 stores | https://www.bcliquorstores.com/product/548693 | {sku=548693; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=14.4; sweetness=00; consumer_votes=0; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/548693.jpeg; certificates=["BC VQA", "All VQA"]}
  - DAYDREAMER - JASPER MERLOT CABERNET | $32.99 | stock=327 | in 27 stores | rating=4.0 | https://www.bcliquorstores.com/product/768408 | {sku=768408; product_type=Red Wine; grape_type=MERLOT; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; consumer_votes=3; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/768408.jpeg; certificates=["BC VQA", "All VQA"]}
  - FERNIE BREWING - CRAFT COLLECTION PACK CAN | $24.79 | stock=947 | in 90 stores | rating=3.3 | https://www.bcliquorstores.com/product/392343 | {sku=392343; country=Canada; volume=0.355; alcohol_pct=5.0; tasting_notes=This popular 12-pack has something to satisfy the tastes of every craft beer lover. Featuring three cans of each - Project 9 Pils, Headwall Hazy Pale Ale, Waymark West Coast IPA and Ridgewalk Red Ale. The perfect pairing to any and all adventures. 
; consumer_votes=57; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/392343.jpeg}
  - STEAMWORKS - MASH-UP 8 TALL CAN PACK | $22.99 | stock=1599 | in 146 stores | rating=4.3 | https://www.bcliquorstores.com/product/862375 | {sku=862375; country=Canada; volume=0.473; alcohol_pct=5.0; tasting_notes=Experience the ultimate fusion of Steamworks' finest brews with our original Mash-Up. Whether you crave hazy and hoppy or prefer clear and crisp, this collection caters to every palate. Each pack includes the Flagship IPA, Pale Ale, Pilsner and Heroica Red Ale.
; consumer_votes=183; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/862375.jpeg}
  - PELLER FAMILY VINEYARDS - CABERNET SAUVIGNON | $10.47 | stock=1191 | in 93 stores | rating=3.2 | https://www.bcliquorstores.com/product/164616 | {sku=164616; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Garnet colour with a bouquet of blackcurrant, black cherry and just a whiff of smoke and spice. It goes well with grilled meats and mild chili.
; consumer_votes=88; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/164616.jpeg}
  - PELLER FAMILY VINEYARDS - CABERNET SAUVIGNON | $17.99 | stock=2089 | in 161 stores | rating=3.3 | https://www.bcliquorstores.com/product/198226 | {sku=198226; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=1.500; alcohol_pct=12.5; sweetness=00; tasting_notes=Garnet colour with a bouquet of blackcurrant, black cherry and just a whiff of smoke and spice. It goes well with grilled meats and mild chili.
; consumer_votes=34; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/198226.jpeg}
  - JACKSON TRIGGS PROPRIETOR'S SELECTION SHIRAZ | $44.99 | stock=1965 | in 180 stores | rating=3.3 | https://www.bcliquorstores.com/product/201368 | {sku=201368; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=4.000; alcohol_pct=13.0; sweetness=00; tasting_notes=Aromas of raspberry and blackberry with hints of cracked pepper follow through the long spicy finish.
; consumer_votes=74; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/201368.jpeg}
  - COPPER MOON - SMOOTH RED | $11.99 | stock=646 | in 66 stores | rating=3.2 | https://www.bcliquorstores.com/product/132253 | {sku=132253; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=02; tasting_notes=Purple garnet in colour. A bouquet of blue plum, blueberry, black cherry, sweet vanilla and sweet spice. A medium-bodied red wine with a smooth mouthfeel and flavours of juicy dark fruits which linger on the finish.
; consumer_votes=28; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/132253.jpeg}
  - KALALA - ZWEIGELT 2021 | $24.49 | stock=28 | in 1 stores | https://www.bcliquorstores.com/product/89326 | {sku=89326; product_type=Red Wine; grape_type=OTHER GRAPE VARIETY; country=Canada; volume=0.750; alcohol_pct=12.8; sweetness=00; consumer_votes=0; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/89326.jpeg; certificates=["BC VQA", "All VQA"]}
  - SCREAMING FRENZY - MERITAGE | $26.99 | stock=173 | in 19 stores | rating=4.0 | https://www.bcliquorstores.com/product/179372 | {sku=179372; product_type=Red Wine; grape_type=CABERNET/MERLOT; country=Canada; volume=0.750; alcohol_pct=14.6; sweetness=00; consumer_votes=7; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/179372.jpeg; certificates=["BC VQA", "All VQA"]}
  - RUST WINE CO - ZINFANDEL | $38.99 | stock=414 | in 35 stores | rating=4.5 | https://www.bcliquorstores.com/product/298723 | {sku=298723; product_type=Red Wine; grape_type=ZINFANDEL; country=Canada; volume=0.750; alcohol_pct=14.8; sweetness=00; consumer_votes=11; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/298723.jpeg; certificates=["BC VQA", "All VQA"]}
  - HESTER CREEK - GSM | $37.99 | stock=708 | in 54 stores | rating=4.4 | https://www.bcliquorstores.com/product/356983 | {sku=356983; product_type=Red Wine; grape_type=OTHER GRAPE VARIETY; country=Canada; volume=0.750; alcohol_pct=13.8; sweetness=00; consumer_votes=11; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/356983.jpeg; certificates=["BC VQA", "All VQA"]}
  - HESTER CREEK - SYRAH | $27.99 | stock=10 | in 2 stores | rating=3.9 | https://www.bcliquorstores.com/product/504399 | {sku=504399; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=13.8; sweetness=00; consumer_votes=16; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/504399.jpeg; certificates=["BC VQA", "All VQA"]}
  - PELLER FAMILY VINEYARDS - SHIRAZ | $42.99 | stock=1482 | in 140 stores | rating=3.2 | https://www.bcliquorstores.com/product/361022 | {sku=361022; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=4.000; alcohol_pct=13.0; sweetness=00; tasting_notes=Flavours of black cherry and a hint of spice are enhanced by rich red fruit aromas. It pairs well with grilled steak, roast beef and lamb.
; consumer_votes=68; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/361022.jpeg}
  - SCREW IT! - THE RED | $10.99 | stock=14 | in 3 stores | rating=3.3 | https://www.bcliquorstores.com/product/485003 | {sku=485003; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Openly fruity, lush and layered, Screw it! The Red is a tantalizing combination of ripe fruits and velvety textures. Full-bodied and supple, this wine is made in a rich style that ends in a long, juicy red fruit finish. An inviting treat!
; consumer_votes=146; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/485003.jpeg}
  - BASK - PINOT NOIR | $12.99 | stock=2420 | in 167 stores | rating=3.3 | https://www.bcliquorstores.com/product/9330 | {sku=9330; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=Just BASK in 0g sugar per serving. That's one less thing to worry about, so you can zero in on the moment and savour every second. BASK Pinot Noir has aromas of dark cherry and subtle notes of spice. Well-balanced and perfect on its own or with a meal.
; consumer_votes=353; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/9330.jpeg}
  - COPPER MOON - MERLOT | $16.99 (reg $19.99) | stock=1425 | in 134 stores | rating=3.2 | https://www.bcliquorstores.com/product/129684 | {sku=129684; product_type=Red Wine; grape_type=MERLOT; country=Canada; volume=1.500; alcohol_pct=12.5; sweetness=00; tasting_notes=Enjoy a rich bouquet of black cherry, blackcurrants, blue plums and hints of spice and oak.
; consumer_votes=49; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/129684.jpeg}
  - COPPER MOON - MALBEC | $10.49 (reg $11.99) | stock=3389 | in 185 stores | rating=3.4 | https://www.bcliquorstores.com/product/164368 | {sku=164368; product_type=Red Wine; grape_type=MALBEC; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=A bouquet of vanilla, chocolate and field berries is complemented by cherry and blackcurrant flavours.
; consumer_votes=230; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/164368.jpeg}
  - SAWMILL CREEK - CABERNET SAUVIGNON | $42.99 | stock=1593 | in 177 stores | rating=3.2 | https://www.bcliquorstores.com/product/374108 | {sku=374108; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=4.000; alcohol_pct=12.5; sweetness=00; tasting_notes=This wine captivates with its deep ruby colour and rich aromas of blackberries, blackcurrants, and black cherries. On the palate, it's full-bodied and powerful, showcasing layers of dark fruit flavours like blackcurrant and blueberries. The finish is smooth, with subtle woody notes that add a satisfying touch of warmth.
; consumer_votes=61; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/374108.jpeg}

#### search_everything_wine_tool (status=ok, 24 results)
  - Fairview Cellars Two Hoots Red Blend 750 mL | $36.98 | [North Vancouver:20, South Surrey:11, Langley Store:11, Vancouver:11] | https://www.everythingwine.ca/fairview-cellars-two-hoots-red-blend-750-ml | {sku=250087; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/5/250087_fairview_twohoots_nl.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Evolve Cellars Momento Red Blend 750 mL | $24.99 | [North Vancouver:0, South Surrey:0, Langley Store:8, Vancouver:3] | https://www.everythingwine.ca/evolve-cellars-momento-red-blend-750-ml | {sku=389273; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/8/389273_evolve_momento_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Dirty Laundry Vineyard Hush Red 750 mL | $21.99 | [North Vancouver:14, South Surrey:0, Langley Store:6, Vancouver:0] | https://www.everythingwine.ca/dirty-laundry-vineyard-hush-red-750-ml | {sku=11888; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/1/11888_dirty_laundry_hush_red_blend.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Pacific Breeze Killer Cab Red Blend 750 mL | $27.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/pacific-breeze-killer-cab | {sku=114769; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/1/114769_pacific-breeze-killer-cab.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - French Door Estate Winery Fleur Red Blend 750 mL | $39.98 | [North Vancouver:8, South Surrey:0, Langley Store:10, Vancouver:0] | https://www.everythingwine.ca/french-door-estate-winery-fleur-red-blend-750-ml | {sku=396661; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/9/396661_french_door_fleur_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Chaberton Estate Winery Red Blend 750 mL | $23.98 | [North Vancouver:12, South Surrey:16, Langley Store:8, Vancouver:4] | https://www.everythingwine.ca/chaberton-cuvee-rouge | {sku=969790; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/9/6/969790_chaberton_red_blend.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Pentage Winery Hiatus Red Blend 750 mL | $31.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/pentage-haitus-red-blend-750-ml-1 | {sku=25200; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/5/25200_pentage_hiatus_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Intrigue Wines Social Red Blend 750 mL | $27.98 | https://www.everythingwine.ca/intrigue-wines-social-red-blend-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Chaberton Estate Winery Red Blend 4 L Box | $65.98 | [North Vancouver:3, South Surrey:8, Langley Store:4, Vancouver:4] | https://www.everythingwine.ca/chaberton-cuvee-rouge-4l | {sku=599332; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/9/599332_chaberton_red_blend_4l.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Vanessa Vineyard Right Bank Red Blend 750 mL | $61.98 | [North Vancouver:2, South Surrey:5, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/vanessa-vineyard-right-bank-red-blend-750-ml | {sku=52194; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/2/52194_vanessa-right-bank.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Narrative By Okanagan Crush Pad Red Blend 750 mL | $24.98 | [North Vancouver:0, South Surrey:0, Langley Store:13, Vancouver:18] | https://www.everythingwine.ca/narrative-red | {sku=771196; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/7/771196_narrative_red_blend.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Church & State Wines Lost Inhibitions Red Blend 250 mL | $7.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/church-state-wines-lost-inhibitions-red-blend-250-ml | {sku=467322; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/6/467322_lost_inhibitions_red_blend_250ml_1.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Crown & Thieves Scoundrels Punch Red Blend 750 mL | $34.98 | [North Vancouver:0, South Surrey:0, Langley Store:7, Vancouver:9] | https://www.everythingwine.ca/crown-thieves-scoundrels-punch-red-blend-750-ml | {sku=14919; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/4/14919_crownthieves_scoundrels_punch_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Calliope Wines Figure 8 Red Blend 750 mL | $26.99 | https://www.everythingwine.ca/calliope-figure-8-red | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/c/a/calliope_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Bordertown Estate Winery Living Desert Red Blend 750 mL | $27.98 | https://www.everythingwine.ca/bordertown-vineyards-estate-winery-ltd-desert-red-750-ml | {sku=165405; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/6/165405_bordertown-living-desert-red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Church & State Wines Lost Inhibitions - Lewd Edition Red Blend 750 mL | $24.98 | https://www.everythingwine.ca/church-state-wines-2014-lost-inhibitions-red-blend-750ml | {sku=553008; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/5/553008_church-and-state-lost-inhibitions-red-blend.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Maverick Estate Winery Renegade Red 750 mL | $25.99 | https://www.everythingwine.ca/maverick-estate-winery-renegade-red-750-ml | {sku=131605; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/3/131605_maverick_renegade_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - The Hatch Ross.O Red Blend 750 mL | $23.98 (reg $25.98) | https://www.everythingwine.ca/the-hatch-ross-o-wa-red-blend-750-ml | {sku=709764; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/0/709764_hatch_rosso_2.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Culmina Family Estate Winery R&D Red Blend 750 mL | $19.99 | https://www.everythingwine.ca/culmina-family-estate-winery-r-d-red-blend-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/c/u/culmina_r_d_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Church & State Wines Meritage 750 mL | $34.98 | https://www.everythingwine.ca/church-state-wines-coyote-bowl-meritage-750-ml | {sku=278267; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/278267_church-and-state-meritage.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Mt Boucherie Estate Winery Similkameen Valley Blaufrankisch 750 mL | $30.98 | https://www.everythingwine.ca/mt-boucherie-blaufrankisch | {sku=64428; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/6/4/64428_mt_boucherie_blaufrankisch.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Moraine Estate Winery Cabernet Merlot 750 mL | $28.98 | https://www.everythingwine.ca/moraine-estate-winery-cabernet-merlot-750-ml | {sku=382794; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/8/382794_moraine_cabmerlot.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Beautiful BC Gift Basket Delivery Version | $128.97 | https://www.everythingwine.ca/beautiful-bc-gift-basket-delivery-version | {image_url=https://www.everythingwine.ca/media/catalog/product/b/e/beautiful-bc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366}
  - A Taste of BC Gift Basket Delivery Version | $115.99 | https://www.everythingwine.ca/a-taste-of-bc-gift-basket-delivery-version | {image_url=https://www.everythingwine.ca/media/catalog/product/a/-/a-taste-of-bc-main-image.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 15 results)
  - Averill Creek Joue Red | $29.49 | 2021 | stock=6 | https://store.suttonplacewinemerchant.com/products/4143614-averill-creek-joue-red | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000022/0000227954-5166.jpg; country=CANADA; varietal=Red Blend; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}
  - Averill Creek Pinot Noir  | $35.99 | 2021 | stock=5 | https://store.suttonplacewinemerchant.com/products/4144447-averill-creek-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000078/0000786657-5366.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.10; is_staff_pick=False; is_featured=False}
  - Bartier Bros Granite | $32.99 | 2021 | stock=12 | https://store.suttonplacewinemerchant.com/products/4944430-bartier-bros-granite | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000016/0000169496-1522.png; country=CANADA; varietal=Red Blend; alcohol_pct=14.50; is_staff_pick=False; is_featured=False}
  - Bench 1775 Cabernet Sauvignon Merlot | $31.49 | 2019 | stock=5 | https://store.suttonplacewinemerchant.com/products/4571291-bench-1775-cabernet-sauvignon-merlot | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000048/0000483529-1106.jpg; country=CANADA; varietal=Cabernet Sauvignon/Merlot; alcohol_pct=14.80; is_staff_pick=False; is_featured=False}
  - Bench 1775 Syrah | $32.99 | 2021 | stock=2 | https://store.suttonplacewinemerchant.com/products/4571295-bench-1775-syrah | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000044/0000441741-7370.jpg; country=CANADA; varietal=Syrah; alcohol_pct=14.00; is_staff_pick=False; is_featured=False}
  - Bench 1775 Viognier | $22.99 | stock=5 | https://store.suttonplacewinemerchant.com/products/5056699-bench-1775-viognier | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC425751.jpg; country=CANADA; varietal=Viognier; alcohol_pct=12.60; is_staff_pick=False; is_featured=False}
  - Birch Block Beau Soleil Pinot Noir | $50.49 | 2023 | stock=3 | https://store.suttonplacewinemerchant.com/products/5103142-birch-block-beau-soleil-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.10; is_staff_pick=False; is_featured=False}
  - Black Hills Estate Winery Nota Bene | $76.99 | 2022 | stock=38 | https://store.suttonplacewinemerchant.com/products/4144375-black-hills-estate-winery-nota-bene | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000070/0000708073-8356.jpg; country=CANADA; varietal=Bordeaux Blend; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Black Sage Vineyard Cabernet Franc | $38.49 | 2020 | stock=19 | https://store.suttonplacewinemerchant.com/products/4144211-black-sage-vineyard-cabernet-franc | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000059/0000593038-3276.jpg; country=CANADA; varietal=Cabernet Franc; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Black Sage Vineyard Cabernet Sauvignon  | $38.49 | 2020 | stock=15 | https://store.suttonplacewinemerchant.com/products/4144212-black-sage-vineyard-cabernet-sauvignon | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000059/0000593095-6502.jpg; country=CANADA; varietal=Cabernet Sauvignon; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Blue Mountain Gamay | $33.99 | 2020 | stock=4 | https://store.suttonplacewinemerchant.com/products/4228470-blue-mountain-gamay | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000038/0000389882-3198.png; country=CANADA; varietal=Gamay Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Bonamici Cellars Belviaggio | $51.99 | 2020 | stock=7 | https://store.suttonplacewinemerchant.com/products/4144339-bonamici-cellars-belviaggio | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000067/0000673954-1986.jpg; country=CANADA; varietal=Red Blend; alcohol_pct=14.50; is_staff_pick=False; is_featured=False}
  - Bonamici Cellars Merlot - Cabernet Franc | $32.99 | 2021 | stock=7 | https://store.suttonplacewinemerchant.com/products/4143755-bonamici-cellars-merlot-cabernet-franc | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000032/0000326249-3594.png; country=CANADA; varietal=Red Blend; alcohol_pct=14.90; is_staff_pick=False; is_featured=False}
  - Clos Du Soleil Célestiale | $34.99 | 2019 | stock=41 | https://store.suttonplacewinemerchant.com/products/4205421-clos-du-soleil-celestiale | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000002/0000021249-3380.jpg; country=CANADA; varietal=Red Blend; alcohol_pct=14.20; is_staff_pick=False; is_featured=False}
  - Clos du Soleil Signature 2021 | $62.49 | 2021 | stock=12 | https://store.suttonplacewinemerchant.com/products/5140824-clos-du-soleil-signature-2021 | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC298158.jpg; country=CANADA; varietal=Bordeaux Blend; alcohol_pct=13.40; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 20 results)
  - Cassini 2023 Pinot Noir "Red Carpet" 750ml | $29.99 | stock=24 | https://www.marquis-wines.com/cassini-2022-pinot-noir-red-carpet-750ml/ | {sku=1014905; in_stock=True; categories=["Celebrate BC Wine Month", "Drink Local", "Red Wine", "Pinot Noir", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8886/images/6958/cassini-2016-pinot-noir-red__12126.1732902163.500.500.jpg?c=2}
  - Sunrock 2020 Red Meritage 750ml | $35.99 | stock=5 | https://www.marquis-wines.com/sunrock-2016-red-meritage-750ml/ | {sku=1010560; in_stock=True; categories=["Red Wine", "Red Blends", "Merlot", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/10684/images/10027/2021-03-11-17.21.05__93677.1615850902.500.500.png?c=2}
  - Esquimalt Bitter Red Americano 500ml | $33.99 | stock=1 | https://www.marquis-wines.com/esquimalt-bitter-red-americano-500ml/ | {sku=1031661; in_stock=True; categories=["Spirits", "Liqueurs", "Distilled in BC"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20972/images/16785/2025-11-12_12.19.55__58307.1763069208.500.500.png?c=2}
  - Three Sisters Bench Red 750ml | $25.99 | stock=4 | https://www.marquis-wines.com/three-sisters-bench-red-750ml/ | {sku=1021001; in_stock=True; categories=["Red Wine", "Red Blends", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18920/images/14931/2024-07-26_11.42.18__97445.1722292995.500.500.png?c=2}
  - Hester Creek 2022 The Judge Red Blend 750ml | $59.99 | stock=10 | https://www.marquis-wines.com/hester-creek-2020-the-judge-red-blend-750ml/ | {sku=1020782; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18498/images/14441/2024-02-27_12.22.40__84615.1709148372.500.500.png?c=2}
  - Black Hills 2022 Nota Bene 750ml | $72.99 | stock=21 | https://www.marquis-wines.com/black-hills-2022-nota-bene-750ml/ | {sku=708073; in_stock=True; categories=["Celebrate BC Wine Month", "Drink Local", "Red Wine", "Red Blends", "British Columbia", "Okanagan Falls"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7944/images/9204/2020-10-01-15.42.34__26769.1780440169.500.500.jpg?c=2}
  - Nichol 2022 Cabernet Franc 'The Village' 750ml | $32.99 | stock=4 | https://www.marquis-wines.com/nichol-2022-cabernet-franc-the-village-750ml/ | {sku=1030412; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Cabernet Franc", "Celebrate BC Wine Month"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19423/images/15276/2024-10-29-11.34.44__90023.1730308360.500.500.png?c=2}
  - Quails Gate 2022 Old Vines Foch 750ml | $31.99 | stock=2 | https://www.marquis-wines.com/quails-gate-2019-old-vines-foch-750ml/ | {sku=639625; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8458/images/10815/IMG_41941__18319.1631131104.500.500.png?c=2}
  - Burrowing Owl 2022 Cabernet Franc 750ml | $42.99 | stock=19 | https://www.marquis-wines.com/burrowing-owl-2022-cabernet-franc-750ml/ | {sku=556621; in_stock=True; categories=["Red Wine", "Cabernet Franc", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20920/images/16669/burrowing_owl_franc__20214.1760725789.500.500.jpg?c=2}
  - Lock & Worth 2023 Merlot 750ml | $27.99 | stock=9 | https://www.marquis-wines.com/lock-worth-2022-merlot-750ml/ | {sku=1019960; in_stock=True; categories=["Red Wine", "Merlot", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9932/images/8452/29229_Lock_Worth_Merlot__53926.1698439471.500.500.jpg?c=2}
  - Meyer Family 2023 Pinot Noir 750ml | $34.99 | stock=12 | https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/ | {sku=1014474; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7708/images/8652/Lindsey_Ail_-_IMG_15661__44130.1589559651.500.500.jpg?c=2}
  - Tinhorn Creek 2023 Cabernet Franc 750ml | $27.99 | stock=47 | https://www.marquis-wines.com/tinhorn-creek-2023-cabernet-franc-750ml/ | {sku=530717; in_stock=True; categories=["Red Wine", "Red Blends", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9723/images/5511/2014-tinhorn-creek-cab-franc-vqa__10878.1779383184.500.500.jpg?c=2}
  - Burrowing Owl 2011 Cabernet Sauvignon 750ml | $134.99 | stock=16 | https://www.marquis-wines.com/burrowing-owl-2011-cabernet-sauvignon-750ml/ | {sku=508200; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20712/images/16485/burrowing_owl_cabernet_sauvignon__56618.1755199208.500.500.jpg?c=2}
  - Mission Hill Five Vineyards Cabernet/Merlot 750ml | $20.99 | stock=68 | https://www.marquis-wines.com/mission-hill-2018-five-vineyards-cabernet-merlot-750ml/ | {sku=257816; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Red Blends", "Merlot", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/6097/images/5467/five-vienyards-mission-hill-2014-cab-merlot__34443.1504217533.500.500.jpg?c=2}
  - Gray Monk 2021/24 Pinot Noir 750ml | $24.99 | stock=18 | https://www.marquis-wines.com/gray-monk-2019-pinot-noir-750ml/ | {sku=251835; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/15726/images/11434/2022-01-20-17.34.22__23087.1642793746.500.500.png?c=2}
  - Pamplemousse Jus 2025 Foch Nouveau 750ml | $34.99 | stock=8 | https://www.marquis-wines.com/pamplemousse-jus-2025-foch-nouveau-750ml/ | {sku=1032320; in_stock=True; categories=["Red Wine", "Organic / Biodynamic Wine", "Canada", "British Columbia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21828/images/17539/2026-05-28-12.34.21__76443.1780090872.500.500.png?c=2}
  - Vasanti 2022 Cabernet Sauvignon 750ml | $31.99 | stock=10 | https://www.marquis-wines.com/vasanti-2022-cabernet-sauvignon-750ml/ | {sku=1032200; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21813/images/17502/2026-05-15-12.10.25__01232.1779221223.500.500.png?c=2}
  - Domaine Artema 2022 Black Sage Road Rouge 750ml | $24.49 | stock=14 | https://www.marquis-wines.com/domaine-artema-2022-black-sage-road-rouge-750ml/ | {sku=1032199; in_stock=True; categories=["Red Wine", "Syrah & Shiraz", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21816/images/17501/2026-05-15-12.09.58__73486.1779221076.500.500.png?c=2}
  - Moon Curser 2022 Cabernet Sauvignon 750ml | $54.99 | stock=10 | https://www.marquis-wines.com/moon-curser-2022-cabernet-sauvignon-750ml/ | {sku=1032177; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21684/images/17401/2026-04-16-14.28.04__73861.1776448816.500.500.png?c=2}
  - Spearhead 2024 Dual Citizen Pinot Noir 777 750ml | $46.99 | stock=5 | https://www.marquis-wines.com/spearhead-2024-dual-citizen-pinot-noir-777-750ml/ | {sku=1032034; in_stock=True; categories=["Red Wine", "Pinot Noir", "Canada", "British Columbia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21522/images/17200/IMG_0692__32204.1773167006.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 0 results)

````

</details>

### Latency

- 100.21s

---
## Turn 2

### Query

> What about a BC sparkling for this weekend?

### Tool Calls (in order)

1. `sommelier_agent_tool` args={"request": "Recommend BC sparkling wines under $35. Provide tasting notes, reviews, scores, and food pairings."}
2. `sourcing_agent_tool` args={"request": "BC sparkling wine under $35 in stock in Vancouver stores (BCLS, Marquis, Sutton Place, Legacy, etc.)"}

### Final Response

```markdown
Here are four excellent BC sparkling wines under your **$35 budget** that are currently in stock in Vancouver and perfect for the weekend. I’ve also included a "just over budget" benchmark option if you want to splurge by a single dollar!

---

### 1. Haywire 2018 Sparkling "The Bub"
* **Price:** $32.99 (34 in stock)
* **Where to Buy:** [Marquis Wine Cellars (Davie St)](https://www.marquis-wines.com/haywire-2015-sparkling-the-bub-750ml/)
* **The Vibe:** Serious, crisp, and bone-dry. This traditional-method sparkling wine is made from Pinot Noir and Chardonnay by Okanagan Crush Pad in Summerland.
* **Tasting Notes & Reviews:** Critic Treve Ring (*Gismondi on Wine*) awarded the 2018 vintage **90 points**, describing it as a racy, crisp, and serious zero-dosage bubble with lively notes of lemon pith, broken stones, pear skin, and dried sage.
* **Best Food Pairings:** Because it is bone-dry with high acidity, it cuts beautifully through rich, salty, or fried foods. Pair it with sushi, tempura, or a bowl of salty potato chips.

### 2. Monte Creek Living Land Sparkling Organic
* **Price:** $24.99 (520 in stock across 37 stores)
* **Where to Buy:** [BC Liquor Stores](https://www.bcliquorstores.com/product/21764)
* **The Vibe:** Fresh, organic, and widely available. This is a fantastic, crowd-pleasing option if you need to grab a bottle quickly.
* **Tasting Notes & Reviews:** Awarded **89 points** by *WineAlign*, critics praise its bright, fresh aromas of peach and pineapple on the nose, followed by green apple and Bosc pear on the palate. It features a creamy mousse and a clean, refreshing finish.
* **Best Food Pairings:** Perfect for a weekend brunch with eggs benedict, or served alongside a fresh fruit and cheese platter.
* *Note: If you prefer a pink bubble, the organic **Monte Creek Living Land Sparkling Rosé** is also in stock at BCLS for the same price ($24.99) with notes of ripe strawberry and juicy watermelon.* [Buy Rosé here](https://www.bcliquorstores.com/product/228385).

### 3. Ursa Major x Bella Wines 2025 "Ode to Sappho"
* **Price:** $34.99 (43 in stock)
* **Where to Buy:** [Marquis Wine Cellars (Davie St)](https://www.marquis-wines.com/ursa-major-x-bella-wines-2024-ode-to-sappho-750ml/)
* **The Vibe:** Artisanal, natural, and unique. Bella Wines is BC's only winery dedicated exclusively to sparkling wine. This collaboration with natural wine producer Ursa Major is a highly expressive, low-intervention bubble.
* **Tasting Notes:** Expect a vibrant, textured, and lively sparkling wine with bright orchard fruit and a distinct, mineral-driven personality.
* **Best Food Pairings:** Great on its own as a celebratory toast, or paired with a local charcuterie board featuring cured meats and soft cheeses.

### 4. 8th Generation Vineyard "Confidence"
* **Price:** $22.99 (426 in stock across 39 stores)
* **Where to Buy:** [BC Liquor Stores](https://www.bcliquorstores.com/product/79307)
* **The Vibe:** Fun, fruity, and highly approachable. 8th Generation is a family-owned winery in Summerland known for making incredibly clean, fruit-forward wines.
* **Tasting Notes:** A slightly off-dry style with gentle, frothy bubbles, bursting with fresh aromas of red berries, peach, and citrus.
* **Best Food Pairings:** Excellent as an aperitif to kick off the weekend, or paired with lightly spiced dishes like pad thai or fish tacos.

---

### 🍾 The "Just Over Budget" Splurge: Blue Mountain Gold Label Brut
* **Price:** $35.99 (26 in stock)
* **Where to Buy:** [Sutton Place Wine Merchant (Yaletown)](https://store.suttonplacewinemerchant.com/products/4144014-blue-mountain-brut-gold-label)
* **Why it's worth the extra $1:** This is widely considered the absolute benchmark for Canadian traditional-method sparkling wine. Geoffrey Moss MW (*Gismondi on Wine*) awarded it **90 points**, calling it a benchmark that overdelivers, while John Szabo MS (*WineAlign*) scored it **92 points**, praising its complex, toasty, Champagne-like brioche character and bright green apple acidity. 
* **Best Food Pairings:** Fresh oysters on the half shell, truffle fries, or crispy fried chicken.
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
    "GENERAL_KNOWLEDGE": 2,
    "NOT_IN_EVIDENCE": 0,
    "CONTRADICTED": 0
  },
  "correctness_rationale": "The agent perfectly extracted pricing, stock, and review scores from the evidence, and correctly applied general knowledge for winery locations and specialties.",
  "issues": [],
  "strengths": [
    "Excellent adherence to the user's budget constraint, with a thoughtful 'splurge' option just $1 over.",
    "Accurate real-time pricing, stock levels, and purchase links."
  ],
  "parse_error": false
}
```

### Claim Verdicts

| Label | Claim | Evidence quote |
|---|---|---|
| SUPPORTED | Haywire 2018 Sparkling 'The Bub' is priced at $32.99 with 34 in stock at Marquis Wine Cellars. | Haywire 2018 Sparkling "The Bub" 750ml \| $32.99 \| stock=34 \| https://www.marquis-wines.com/haywire-2015-sparkling-the-bub-750ml/ |
| SUPPORTED | Haywire 'The Bub' is a traditional-method sparkling wine made from Pinot Noir and Chardonnay by Okanagan Crush Pad in Summerland. | Haywire "The Bub" is a traditional-method, zero-dosage sparkling wine produced by Okanagan Crush Pad in Summerland, British Columbia. Typically crafted from a blend of Pinot Noir and Chardonnay |
| SUPPORTED | Treve Ring (Gismondi on Wine) awarded the 2018 vintage of Haywire 'The Bub' 90 points. | Treve Ring (Gismondi on Wine) – 90 Points: Ring described this vintage ... as a racy, crisp, and serious zero-dosage sparkling wine. |
| SUPPORTED | Monte Creek Living Land Sparkling Organic is priced at $24.99 with 520 in stock across 37 BC Liquor Stores. | MONTE CREEK  - LIVING LAND SPARKLING ORGANIC \| $24.99 \| stock=520 \| in 37 stores |
| SUPPORTED | WineAlign awarded Monte Creek Living Land Sparkling Organic 89 points. | 89 Points, WineAlign: "Bright with fresh aromas of peach and pineapple on the nose and green apple, bosc pear on the palate. |
| SUPPORTED | Monte Creek Living Land Sparkling Rosé is priced at $24.99 at BC Liquor Stores. | MONTE CREEK - LIVING LAND SPARKLING ROSE ORGANIC \| $24.99 \| stock=677 \| in 62 stores |
| SUPPORTED | Ursa Major x Bella Wines 2025 'Ode to Sappho' is priced at $34.99 with 43 in stock at Marquis Wine Cellars. | Ursa Major x Bella Wines 2025 Ode to Sappho 750ml \| $34.99 \| stock=43 \| https://www.marquis-wines.com/ursa-major-x-bella-wines-2024-ode-to-sappho-750ml/ |
| GENERAL_KNOWLEDGE | Bella Wines is BC's only winery dedicated exclusively to sparkling wine. | — |
| SUPPORTED | 8th Generation Vineyard 'Confidence' is priced at $22.99 with 426 in stock across 39 BC Liquor Stores. | 8TH GENERATION VINEYARD - CONFIDENCE \| $22.99 \| stock=426 \| in 39 stores |
| GENERAL_KNOWLEDGE | 8th Generation is a family-owned winery in Summerland. | — |
| SUPPORTED | Blue Mountain Gold Label Brut is priced at $35.99 with 26 in stock at Sutton Place Wine Merchant. | Blue Mountain Brut Gold Label  \| $35.99 \| stock=26 \| https://store.suttonplacewinemerchant.com/products/4144014-blue-mountain-brut-gold-label |
| SUPPORTED | Geoffrey Moss MW (Gismondi on Wine) awarded Blue Mountain Gold Label Brut 90 points. | Geoffrey Moss MW (Gismondi on Wine) – 90/100: Reviewing the 2019-based bottling, Moss called it a benchmark for Canadian sparkling wine |
| SUPPORTED | John Szabo MS (WineAlign) scored Blue Mountain Gold Label Brut 92 points. | John Szabo, MS (WineAlign) – 92/100: Tasted in November 2023, Szabo praised the 2019 vintage as a "terrific value" |

### Evidence shown to judge

_4 tool messages, 180457 chars (budget 2000000)_

<details><summary>Show evidence</summary>

````markdown
### sommelier_agent_tool (status=ok)
**Sub-agent synthesis:**
For a casual dinner, you want wines that are approachable, versatile with food, and offer great value without sacrificing quality. British Columbia excels at producing vibrant, food-friendly reds that punch well above their weight class. 

Here are 4 excellent BC red wines that typically sit under the $35 mark, along with tasting notes, style descriptions, and pairing ideas. To ensure you have a complete beverage strategy for your dinner, I have also included some fantastic local beer, spirit, and sake alternatives.

### 1. Meyer Family Vineyards Okanagan Valley Pinot Noir
**Style:** Elegant, fresh, and highly versatile. Meyer is one of BC’s premier Pinot Noir producers, and their regional blend is a masterclass in approachability. 
*   **Tasting Notes & Scores:** Reviewing the 2023 vintage, Anthony Gismondi ([Gismondi on Wine](https://gismondionwine.com/)) awarded it 89 points, calling it a highly successful and approachable release despite recent challenging winter vintages in the Okanagan. Shelley Boettcher ([Castanet](https://www.castanet.net/)) praised the same vintage for its delicate notes of cherry, pomegranate, and green tea. 
*   **Food Pairing:** The ultimate casual dinner chameleon. It’s perfect for a classic roast chicken, mushroom risotto, or even a Margherita pizza. 

### 2. JoieFarm PTG (Passe-Tout-Grains)
**Style:** Fun, juicy, and "gulpable." This is a classic Burgundian-style blend of Pinot Noir and Gamay Noir from the Naramata Bench. It is lighthearted but exceptionally well-crafted.
*   **Tasting Notes & Scores:** Jamie Goode ([WineAlign](https://www.winealign.com/)) gave the 2023 vintage 91 points, describing it as vivid and juicy with a mineral texture and savory finish. *Gismondi on Wine* (89 points) highlighted its expressive spice, red cherry aromas, and silky tannins, noting its highly approachable character. 
*   **Food Pairing:** Serve this slightly chilled. It is phenomenal with charcuterie boards, grilled sausages, or a casual spread of soft cheeses and pâté.

### 3. Tinhorn Creek Cabernet Franc
**Style:** Structured, savoury, and slightly bolder. Cabernet Franc is arguably BC's signature red grape, and Tinhorn Creek produces a benchmark expression that balances dark fruit with classic herbal notes.
*   **Tasting Notes & Scores:** The 2022 vintage took home a Platinum Medal at the 2025 National Wine Awards of Canada ([WineAlign](https://www.winealign.com/)), where judges praised it as a lively, flashy, and youthful expression. For the 2021 vintage, John Schreiner ([John Schreiner on Wine](https://johnschreiner.blogspot.com/)) awarded 91 points, noting that it remained bright and fresh with clean dark fruit flavors despite a hot growing season.
*   **Food Pairing:** This is your go-to for casual BBQ. Pair it with smash burgers, grilled pork chops, or roasted root vegetables with herbs de Provence.

### 4. Bartier Bros. Syrah
**Style:** Bold, peppery, and savoury. Located on the Black Sage Bench, Bartier Bros. crafts Syrah that leans into the savoury, Northern Rhône style rather than a jammy Shiraz profile. *(Note: Due to recent winter freezes, the 2022 vintage is one of their final estate Syrah releases for the time being).*
*   **Tasting Notes & Scores:** Reviewing the 2022 vintage, John Schreiner awarded it 90 points, highlighting its generous texture, dark fruits, black pepper, and long finish. Treve Ring ([Gismondi on Wine](https://gismondionwine.com/)) praised the 2020 vintage for its plump blackberry and dusky plum notes, balanced by stony acidity and a violet-kissed finish.
*   **Food Pairing:** Ideal for heartier casual fare like braised short rib tacos, lamb burgers, or a rich, meaty lasagna.

---

### Casual Dinner Alternatives (Beer, Spirits & Sake)
A great beverage program always has options. If your guests prefer something other than wine, here are some fantastic BC alternatives that fit the casual dinner vibe:

*   **Beer:** **33 Acres of Ocean (West Coast Pale Ale)** from Vancouver. It’s crisp, piney, and perfectly balanced with a subtle malt backbone. It cuts through the richness of casual comfort foods like pizza, burgers, or fried chicken effortlessly.
*   **Spirit / Cocktail:** **Odd Society Wallflower Gin** (East Vancouver). Distilled from 100% BC-grown barley, it is highly aromatic. [BC Spirits](https://bcspirits.com/) highlights its woody lavender, spicy juniper, and earthy botanicals. Serve it as a pre-dinner Gin & Tonic using a dry, premium tonic (like Fever-Tree) and a simple citrus peel garnish to let the floral notes shine.
*   **Sake:** **Artisan SakeMaker Osake Fraser Valley Junmai** (Granville Island). Made from 100% BC-grown sake rice, this is a uniquely Canadian sake. [Sip Magazine](https://sipmagazine.com/) noted its aromas of sweet hay, honeysuckle, and hazelnut, backed by a crisp acidity. Its savoury umami profile makes it a brilliant, unexpected pairing for roast chicken or a casual cheese and charcuterie board.

#### search_web_grounded_tool (status=ok, 11 results)
Search answer: The **Meyer Family Vineyards Okanagan Valley Pinot Noir** is the winery's entry-level regional blend. Sourced from multiple vineyards across the region (typically including sites in Naramata, Osoyoos, Kaleden, and Okanagan Falls), it is widely praised by critics for offering exceptional value. 

Recent vintages have received the following review scores and critic assessments:

### **2023 Vintage**
*   **Anthony Gismondi (*Gismondi on Wine / Vancouver Sun*):** **89 points** (March 2025). He noted that despite severe winter crop damage across the Okanagan, this vintage is a highly successful, approachable release for Pinot fans.
*   **Shelley Boettcher (*Castanet*):** Reviewed in March 2025, she praised it as a fresh, balanced, and well-priced bottle that delivers delicate notes of cherry, pomegranate, and green tea.

### **2022 Vintage**
*   **Anthony Gismondi (*Gismondi on Wine*):** **90 points**. He called it a bargain-priced winner, highlighting its juicy cherry and raspberry profile, bright acidity, and excellent drinkability.
*   **WineAlign:** **91 points**.
*   **Robert K. Stephen (CSW):** **92 points** (July 2023). He described the wine as elegant and light on its feet, showing inviting aromas of red berries, milk chocolate, and subtle oak.

### **2021 Vintage**
*   **Anthony Gismondi & Treve Ring (*Gismondi on Wine*):** **88 points** (August 2022). They described it as a fleshy, ready-to-drink style with an earthy, slightly rustic undercurrent that balances out the bright black cherry fruit.

### **2019 Vintage**
*   **Natalie MacLean:** **89 points**. She described it as a fresh, medium-bodied, and silky blend featuring ripe cherry, forest floor, and savory herb notes.

### **2018 Vintage**
*   **WineAlign:** **91 points**.
*   **Anthony Gismondi (*Gismondi on Wine*):** **90 points**. He highlighted its soft, fresh red fruit character, touch of minerality, and effortless, silky finish.
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqG9yGhHD0hhPhMd8jTlrIIvT0pIFRavFzcYHy3exriZmTqkvzOpy6-R7UpKiy0_pW_CwK31XHRrmBG-BWUKfX14Ac0Kz6EFa0QfZ-71z9ARt2NH4TrbM4wwmNU2JIlWmsvLUb-2eIuTmxp8TN88zXD9R0Se7VP3GnHJeeFSl9bg==): 
  - [kensingtonwinemarket.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJBGUmuT6C9KtxbJKJvmTfse0-Kqxp92npljyJIIuF4FwbgTOLaO07iEkIm4KOU2HeTaL5y910zHjb7_jsJQVsH-uUosjRCi10nkVpgjktlvBXhzwn2daOLQVnyoQ0d5Glc1-KUVnST5eBMBcjcDVihOGqpl8wabISTvUZDchG3OZ-OEMEgaNMHhWUPhIB): 
  - [bcwinetrends.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET375S2vlVZVn8J8aYJIZSI5mNqQQP5ah7XKeNu94lCtM4cRG4U8X8b5y-KDO911xjwFRe697dhct8TZPCXDNiprt_e1K5HbZullDrF_3V8Jgwq9Zjuy3uyOFgngj2SX5p1JBrLZDYEetglDUdifhGbOLUgYTxBlqEwbUN3g75colOEAPgWaJwf6tgarxRuQF7fOIA6w==): 
  - [heavenlyvines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjIvbfx_VvzTWA3dtP-j89uJhqUN6yr3B8wfo9NhMwRrRHcOH5QjAmdoemmC7e1hvyfuIaFbSvaTx7oG1a6zCey4stPK7B3_cXmNF926AipC4wHYrPGV3ty6S_D7SeOQMghI2Za_tam8I7-bkuswcbWJdMqoITmifxxt1zIuw0xA==): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2JeXy7AOw-n2m4WB83DI6f5kY5Km_Vl6ud78uPgrM1GPNK_vfbGa3a6AWFEneEn3LfNpnc6mABxAGbXuEU8aCAqHSEM2LWw-mS8tUkBSdzptCMa2L_jGFJTEk3tDXAB0tFZDycYuA4Y75ARtU9Wr1Ds7EfuZb7TqKIP22bPNXSZnRXC9KQKr6vg==): 
  - [castanet.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUTqtfij9hGHV3TkuePvXcpHmodpZPQhgmTI6lq5_9VW1DTNqSXCvDINXvJcbwel5L3iSlH3WXH_sQm5_Pa9w_Mu8JNRdmI3mtPrmpBYoMHC6wFeQM6QqShjS8qBVzobdBHjRt8frTo7jhdMU0MzI-d5BN1BchQB_OuWaTvWMTb2uO-K-wLbVuwNWzwtFrtkJUqRw=): 
  - [npwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUaBsbRTEsjXow-x02bVsFyiW5egVxOw_Bi57IpgfuOa6MvvnB9lYDjRsLUdj0kK9xK52hECAIPMxDZA5YYK7erMXDlncQKBWhfNk0_0D0XuCVi_QvTJCpoSkQ3MZXpQFIvbxTzGkUXzV4XbObDs_D10owJKosBckO_rrCd7ddHHkrIBjVo05fm1png4v16w==): 
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGpcv6yqVO9DkpOFkO4Icjcqix4jpL5HEgOPgoxHgtTEWRXN6v-zc16OdV272cW3IjLWqlAVbJMrBkUYhOfVM1grwSzYW7QLRMEfkU7SoP0R6iqRfT1ejGIlvnbLCnMHEjrFCqV3L9xgnvKKUY0Yc4KuF68cgvMhdFhpbMNPlESti2rasy98FN7juE3_rQSaSePiO_LUfV5-QA7MbyhjX6XrGI0zjDlyx3omVFuDsvfyJoZqw=): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtaaQf0TaQ6KUKsYWHMkGHwOu8-u7gwJhP40u8YozFUHN04xBZD772jdVgFWzj-NVX-CzY1ijeObRChlEMZKucAispZxIsihjdcNFiPKlQkMDM6yQflZJkOxJHKMalXaWJqXC7MGRot5e_L-Ht3T6yTiDhPEU19FW7dBSZDOIYHcRpkNB2t62XPmJkTg==): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkR3uKMyPpaQ4U17SIhqV_ZWNr6HsL6ELjCioyC5ZqWApagfHBd1GfF4ffsY3KCletWKjAvRvUt6LQSz6slhsCzqR5kNvIobFqNa0NJNNT8eFlY7B3v3EbhPRmOIls9Of1309Sdr2B46Er3kwvK0RFoFDYoB9lkFYKPGK9KZPd0spUC2UsUcWwTH2PN2kW881npwoC): 
  - [npwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4NZbLCjq3tNqO9E93rjN-JUfRZhW-OHRONHofJJRzWdt3YUGbWImodFsgHANImA6Vf7FsRXhpWDr2tfM2aB35KZC4ZQSaYXeO-Y-OMoQprV3HE5L6nnSC0P-MloCuaYt2UoUEHjtgz_XwKN5scPv11kaJYpZWq88GLWWK8TOUcfciZGY7CB5KMDPaO1l8tw==): 

#### search_web_grounded_tool (status=ok, 8 results)
Search answer: **JoieFarm PTG** (Passe-Tout-Grains) is a classic Burgundian-style red blend of Pinot Noir and Gamay Noir produced on the Naramata Bench in British Columbia's Okanagan Valley. 

Review scores and tasting summaries from prominent Canadian and international critics include:

### **2023 Vintage**
* **Jamie Goode (WineAlign): 91 Points** 
  Goode praised the wine as a vivid, juicy, and intriguing blend with a mineral, grainy texture and a savory finish.
* **Anthony Gismondi & Treve Ring (Gismondi on Wine): 89 Points** (Tasted Sept 2025)
  The duo highlighted its expressive spice and red cherry aromas, noting a soft, round palate with silky tannins and a highly approachable, "gulpable" character.
* **National Wine Awards of Canada (2025): Silver Medal**

### **2022 Vintage**
* **Michael Godel (WineAlign): 90 Points** (Tasted June 2025)
  Godel described this vintage as a fun, well-crafted, and lighthearted take on the style, showing sweet red fruit, raspberry, and earthy mulch notes.

### **Older Vintages**
* **2016 Vintage:** Rated **88 Points** by Rick VanSickle (*Wines in Niagara*) and **88 Points** by *Gismondi on Wine*. Critics enjoyed its soft, jammy red fruit profile, peppery spice, and refreshing acidity.
* **2015 Vintage:** Rated **90 Points** by Neil Phillips (*Natalie MacLean*) and **89 Points** by *Gismondi on Wine*. Phillips noted its bright tart cherry flavors, vibrant acidity, and herbaceous, spicy finish.
* **2012 Vintage:** Rated **90 Points** by Neil Phillips (*Natalie MacLean*) and **90 Points** by *Gismondi on Wine*, praised for its light body, bright acidity, and notes of bramble, cherry, and sage.
  - [npwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER1Led2bPrREibM3RhuT0J5jJAfKM50Ebee_CQvCD8CQTMtMPgPl2QnDff8ynMn67HA4c7n7FIWJn3-_oyrC4jWp1gGAdPi0dASGxJuLKiG4XEKG3SvOngIkvvC3Sbug8AN6GjPjakmIXL60_sK1I3-Xc8eeGjIs_7): 
  - [joiefarm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-S_xDyKAVMpe9Vlzr-DSrXsF_BnjdaXEAfaoT4H9_m3tH-4cJYwG8dV1qngUFln7nvGOVwJmfm4SIcVchTJ9GbPSi483M24hDzkq6z-WE-6A13vt67VzDRqUN_bHWmXbp38KXAVdUJw==): 
  - [thebeerguy.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVieZUfT_6eYdpamYVmx9wPI4tErJHAqNgf9JOgC48-ehX0OuTBE8WvhZhMY-bPFYjVrHg99HIw_81Lz0LAEVNhWng-giHPum_RVGRwueYZZbLt_uImgHxhy7NSH9wT5evLr6y5PdYgfGQEbiZjXqtU49HV3AFoD2MYNqnAibpaKrr6Gl_QyZ0eRGLEw5ThNGVkLK3): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkTf41F8J436uGgnlyVVlj8X6rlbX3CcQP5Dx6thr50OuCoXKoNaR0uiJ_-N4diA8_OWiHWuATeKOUafjqlj_XjhospCHONwz9PkVQiLhGabrfSC1hbXIKQF1nz5FgVeyytQnEoeK_QFNvvCaDCcLN_X2zcIrD1yufoFq8X4APoUF7qQeJ76g=): 
  - [winesinniagara.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd8bQD9_vzeX0x4klOKHN59fM_7H3IdAQSTJRpR0CT0RVKHH1o676gQtWkIOKT55rJKBd87Syft6jVrsifmCtOiMax29I8WRbMR8kdvgnK4a_lmf563rkmh2hRZyfNa9hpF3EUbB3sXXtASfqgIH3KNK7m8Q-g_rYBg82thnuL8EvMs5jq7E6IBzzpGade5ZaAiO2mqC9m4WFIMw==): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWR0cpSEyZ0Vh1HIBUFYQ6ckutI2xR_CkA2Cnw_tq0jZKZ8cg4RjFbuaK-JQOCibL-jrrCr-h9ovQUOPLzLd-cPMWznWaCYHvlltSUJ3bHveiqnfbgk_LLVXog3tnDnbQ3w5ZexgzzMsTT9TIVupfVsHHnzk8XmHE0PLye6DVGo9S4IO-thLrGBfbuddUpYNRrP-AwWQ==): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtnRZXCyMZBiLC99ayv1lkaK3wQeMRdBES4aGxEGkCoKefiulAu3XMA_JayU21YZvkcvLtWhyFg9rGlF6vkM5xM9zPBP_mA0-690xpWbN4FFN5VjrjlT15d0poauoTnwZnpQh9q9mu5l5I3_-QhUBjU3Y9GJzeywr8-7EM4-oq): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERZItqaVomhQA3nnhfCrJH1hy3m3w8mDG5_vwF0EX1Ec0nGtReVmMTI7l_wfwHxN8qhsFjnu-tnFYBP7fto5jYQpVfY36B9c9IpVunjcP6HBmxUzmw9-X7rVDRUR6U1ZQrvr_SG3e_WHA9gN8ZiAVeCvWHPeCkCdoyqJ88ExhA-Q==): 

#### search_web_grounded_tool (status=ok, 11 results)
Search answer: Review scores for the **Tinhorn Creek Cabernet Franc** vary by vintage, with recent years receiving high praise from Canadian wine critics and competitions:

### **2022 Vintage**
* **National Wine Awards of Canada (WineAlign, 2025): Platinum Medal**. The judging panel highly praised this vintage, describing it as a lively, flashy, and youthful expression of the grape.

### **2021 Vintage**
* **National Wine Awards of Canada (WineAlign, 2023): Gold Medal**. 
* **John Schreiner: 91/100**. Schreiner noted that despite a very hot growing season, the wine remained bright, fresh, and highly drinkable with clean dark fruit flavors.
* **Wine Club Canada: 90–92/100**. The review highlighted its bold dark fruit, savory herbal undertones, and well-balanced structure.
* **Gismondi on Wine (Geoffrey Moss MW): 86/100**. Moss called it a strong effort for a challenging vintage, noting its balanced ripeness and classic herbal and dark berry varietal character.

### **2020 Vintage**
* **John Schreiner: 92/100** (Standard) & **94/100** (Reserve). Schreiner lauded the standard bottling for its spice and red fruit aromas, while praising the Reserve for its concentrated texture, oak integration, and exceptionally long finish.

### **2019 Vintage**
* **Natalie MacLean: 88/100** (Reserve). MacLean described the Reserve bottling as a ripe, juicy, and smooth red featuring vibrant red berry fruit, dried herbs, and toasty oak spice.

### **2015 Vintage**
* **Gismondi on Wine (Anthony Gismondi & Treve Ring): 90/100**. The critics highlighted its dark fruit profile and well-integrated oak aging.
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELGHVwZlofhNbWNKPh5HkR9IcPCPwr0rG4fzI2vNedJztww2fA5dQDMelsDM-tmNEDb9C0Yjt5aZm7PzlHA7NfGg2lSAmgeDsDyND1D307S4XrDyJmLN084wiOLr-c8qWFAg==): 
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIEnMZnvKT-oEM1POCjErypdfBPgc-Ia5O8f5EOyhXFJmA--o7mw-lQ5JcrRJwVv2MRZDLFA8DhEfeNXyM1NgsXnx1S4fOtT2uQP9yiijpdY-JXQntqVm6ldcN2Q_EIMOkJEe-kQ==): 
  - [alaymanswinemusings.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENFWqRf8IEHSalxKtOb_IxqiFmkG3WhCL83kIRZcfaUknAJgflJWJN7FAd1m6UPn2dJ0JMGMuT5jzzC3VyteCUlOFwRlAQKVOTgOtrCUIf6SLPEoOz1WCZaSOgrcGFnQilsAE6Oz69F4HUfkLIrHRFC-AvrxZ7hYB1HFjxEWmLF7vY3Zg=): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsiRe8xpAMLNR1Il4YuVCGXC0zt-W52udKva2bR_CEQkrWrdnyGi1CE998RfZDTooC2kZ3vU_l2GsWs0sCIfOrf1rNnJWWGyq984MfKbOHvPBixSyXx4-bhJSEw-TCHTsfyYJToPwx99p698U_inf9UP2m1oq6x6t1Zr3135xT7RQa1sP97xgMHdZGhbNhJbivPtS_UzV_s3O7cp6WaeFfen0Nyw==): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvKOfKaDP0WVd0-ITNQbRP0WpOVLfOMqtgG1uPIfK7dH8EpwyWS2WNaNfVAGuouZ_y52DTPOIO_NJscariRbM0XAMHo0E2eziqtLOnvvtXCBOu1WF-uEHtESUVmsHmHcQwD58qQuOu4c_xwDgagICbngxiyfoT_oxtPuolNYh0U94vfnzbfdAHuVmy4VQElThfjPGe6rgEdKmuqLFOlsMg9c1IoQ==): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzBUEhYoZ2wICbnJAky8bylQiWnJKJw-DSVaPFsN0nY3h4i4irBu74rekzKzp9a48FAX6JeGgCct8MGZvqEynUaLRliyzu4806ruJkr-siRnxCdw9bawAgszE5tme3rAqf2vMZ0GA2wnvtLaiT5usJ_A5WmOFA0Hx43pIMJjVSdLpEKzRuIbtZhw==): 
  - [wineclub.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsqMTRht0OWv9tpt3PhrAEyFA_WOm-_v6buDdmmgmaEfmaqS51sko2mQpcfRbsRudUX7hbqO131loA7E4esGZkitShzdUNKR86HSDHOk0aohZrYwr7I1R2dnF6mf01gBaU8-jB_ll35mij3zJBCu5KJ7dC6hfgYyuo1eCjIV4=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuWzz0mX3PRJHVIlewHMunhpTulZ02MK5yv28zClK8tJzEyHBUAEj4-Kd17rM7-ap4ujKGRzyUjxAF-30Bzpsd47gC45XwHO8IOO6fV-DM1IbYCHJa9pxFf7_aujFUrlmDLdz1E4TKFbB-q30uOvLWIHB2DS1e-dR6zWLfMyC6elv4pUUqnTiYCKIpHhs1L5xB9oB-c1dghyOg91u_H6s9-E4=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfIiQaFxmMNUFB_VuroSoxTAnz1WXqiqd7HnER1y-Kpxf2HiyrVenaaYe8eIg1cNAarpF9rJiwapbvam57ZmpmPAdNNBNvXHuQiVkziPY9D3SAra9upJK-M8phpGLbSP3QIX8fWFIGJCM2l69mS5Nh-evHSh6zX2ZsiqlPS3GlWt-tHHrcjqWB_m8d0WUXzLgDaSI2Om3jPA-8EO-ILlSzGmA=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFQKl7WWjiy2fGCCxzhlxz2dTX5pXtH2CKK5LEJDqvS0BUZmdcoFPIyom1MAMxGNtB1_Hvoys3vIXhPeEsbPShwUBZRdB8JlYwW7y308r4BQvlsLNw9fGpg-1_tevCCHMa_vIMDOhmJXXqEnob5zoV_S_LKIX8xwb787wN0awwNVcxiFLvoBjj9emFyPhnXScwz-K39G1dfU2w3kM5383Bug==): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRfTpK7J9Ec1NXcxn60vQ8Xp1_qq1UyoicL6cCNp1XJnBZ4qzb7Fl6kdZBHo6zGJs7HaTMIwCx5Z9bocb_A8dTznEV0Zl6x57aikRCvcBwQwwwEJSOKrbUiTw0wSpNHn9YuMWppGCqmZDZ7XP1kP5WSfTrs7n8ExbhMZcJg0aY_sN-r7LS_BkLJhPjyryT-OvBKknyt3SWaA==): 

#### search_web_grounded_tool (status=ok, 10 results)
Search answer: Bartier Bros. (located on the Black Sage Bench in Oliver, BC) has historically produced highly regarded Syrahs from their Cerqueira Vineyard. Due to devastating winter freezes in late 2022 and early 2024, the winery unfortunately had to pull their Syrah vines, making the 2022 vintage one of their final estate Syrah releases. 

Review scores and tasting summaries from prominent Canadian and international critics include:

### **2022 Vintage**
* **John Schreiner (Goodgrog): 90 points**  
  Schreiner noted that this vintage (which includes 7% Merlot) offers a generous texture with aromas and flavours of dark fruits and black pepper, leading to a long finish.

### **2020 Vintage**
* **Treve Ring (Gismondi on Wine):**  
  Ring praised this vintage for its plump, ripe palate of blackberries, black cherries, and dusky plum, balanced by bright stony acidity and a peppery, violet-kissed finish. 
* **Wine-Searcher:** Lists an overall average critic score of **89/100** across all vintages.

### **2018 Vintage**
* **John Schreiner (Goodgrog): 91 points**  
  Schreiner highlighted its bold palate of cassis, black cherry, and mocha, supported by long, ripe tannins and a persistent finish.
* **Anthony Gismondi (Gismondi on Wine): 90 points**  
  Gismondi praised its open nose of sweet cassis and violet, its silky, savoury palate of wild blackberry jam, and its strong minerality.
* **Decanter World Wine Awards: 90 points**

### **2016 Vintage**
* **Natalie MacLean: 92 points**  
  MacLean described it as a beautifully balanced, full-bodied, and velvety Syrah with ripe blackberry, dark plum, and warm smoky notes.
* **Jennifer Havers (WSET Level 3): 91 points**

### **Related Blend: Grenache-Syrah (2021 Vintage)**
If you are looking for their popular Rhône-style blend:
* **Rick VanSickle (Wines in Niagara): 93 points**  
  VanSickle praised its Rhône-like character, noting peppery red berries, anise, and wild blueberries on a smooth palate.
* **WineScores.ca: 92 points**
  - [foodindustrynetwork.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpMLbTsluHvTzfnagglPCeC3-bTOIblIqBy4yuzmS2L3Y3aBrQKz1KyLogNw0wra7AQbIW_asO54v3NPDzr42DSQ5dqYLFQ0ZGWWZWRV7b-SjqNgbzqkfOR8bewtffA5De5xqmkVrlLf35-oR7JkDLeIqLnjd-ZYR6Bl0HX_wqz89YEAFhMd0a8wc=): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjYzEqoAJe2jib7LxTmJsdMqrlmMdAFPiZfZzwhkinj85pg-WaGHtN9XyR5SB7KEMeTjxptgPqEU2dRZgLkMncsXCtD4yqNIObBCG3PgYugh5-BO4CsMJYWIDkCO8tXr4CTNx_5iiLx8A3ERg75E0Zwr7rkFXWis4b1Bd_l4rd39jVqbw0MSbUaTIhnQ==): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLXtRY_gwu-CISdnVqDjvI8Y2J2Fe-XmVbQU1Wz9PjALQLgDv5lSWjXBnbhieBBrzcZHgijM25IU_tdVTP7iYlYbkREf6p2LMoiMQNtM-UTHcped5DdRz5mOWSHhcI1d_MAX_2szuYU2cKwtG5HpZAhth3ekIzWtW9DvutUXwd0nurvH02tinRAqLsEBM=): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv736K4t1G0IlP4s7TsdVfiq0BeIRHDsPalljC9EyRQdh-yT03WYxwtZiuwx4HQc56Ewglo0EueFWYxgPlnrkXf0iklsQHYFpfjAxkEYatQrD3A0gzMFcE4d52YgGaIN3NiiLwMLNnrIKpueCqZbvK4zBZ3Bu6Z3Hx8U2bodmmWIuujNadOZAM59fo8g==): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtOpFeqKO40cCzDm3fjVyWoQAuYgnUXdxfhxLn5wxLkMn1iRUAi5ycZHIIUOlMVJoncQBNcAUqzT7mYAE8CrWpeC0uh4JvqIC8VjkJfKh4ZK3d94Np8UsVnmayPijxc7r1gcOIvQ==): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbGNXxQnWCKfsnCAvyyD3CheYsQtASvgDt1Er4A6eiXUIZGcazatUSML64T3_JpYN-kWGOcfDIQYGSUVFo9KEOj1UX--yuBK1nf8tCkOp5IoMQqauKBsc-sb2JtoEEWq5Wt8Z8Ma6nu_ZmTTXlCASIEBS0bXcy9pmrS-Fm9zdoK-9PXg75kSFqjc5IGcjUkj0Tssja3RP-vck=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRfa4zkhzm0PeO7W0pm3mQSs3OPmIxtyz6hEKy5IsEA-Gt7aO__N3e7FiL7ggIuOaQ8g-i-MQ_v5SwXQMgrpPRxUil8rmpVjUkvQNSQygu_MrsWZBOMbMsa6MTbFYLQlIfEyXxRJf56oP7_XOT23Yx7gKr17Oehy2yN7f5w4RcSbIuK_TSePlNxPvYcv0k2YuXTTmtd06e83V3): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWyLIVADQlgq26hbof0zEPgXCapk92DaORUzpueY86D-e6lBFEkrkpkF6P6wxN8iyak3jOaQGa-3UXTIgNn8ZH4_ZdOMx1OkqvQopI1gLRBo6vMO2z5AnlAEAKorsbDFkFEnwghfH9UB9jEVKBjm8T5qibJjFxZdOsqBF87xlTNdJdEogcriKtyjb2GQXkXT6XoyJ6FLvY): 
  - [winesinniagara.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvy_X6q-AxigtcUQ_leji-t3HI-SliAjK448S2y-Jh9m0_rjEYIt2usrg1Q_vqH9HvOf6u8FIHn9q25IJm3dI8jmCpVccXdRyX0JlAg0sSLQ-zMIowmiOxuIhZd5vInnemhK57ePbef4XHzY3ru4t-uY9O3UqOrU3LUwL-0wJg8FFGOmJ2HCC8SGza-IsGqw7Fa3k8Xv7Ut_-wvDpkP5f0DNJm): 
  - [winescores.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIKsxM3R5swcDaZ6sUi7CCkdb1iKPDx-xRMpz4KNxHzCk5Du3ueJ7JsOq9EHRDmupXW2jGr6OHAormz_NBGtvNWWMnZZN7iy_-5-_rmtl6dPM94C7PhjfYQbr_1CbSFSNx7YJr3PuV5v-dNyWny_3UHhV0Can-Lr2vl9X_OTbgLGxJ3SodKRSI00cIpkL6IovEdEpdCSDYv3Q6ORDbMLKS5iwDz8poKyxYBBvfFiZBr_nkWROGmOA1byroK5WPsejajWNYQodcCG4negBmDL057WuMvsGAqh8lq1h0qf-wP2ByI1zhatWqPGCsLXC2sZrYsklUg6JpkSY1heeqcihRq44=): 

#### search_web_grounded_tool (status=ok, 11 results)
Search answer: **Artisan SakeMaker’s Osake Fraser Valley Junmai – Renaissance** is a pioneering Canadian sake crafted by maker Masa Shiroki on Granville Island in Vancouver, BC. It is notable for being a "farm-to-glass" sake made with 100% British Columbia-grown Ginpu sake rice cultivated in Abbotsford (Fraser Valley). 

### Tasting Profile & Reviews
* **Sip Magazine:** In a review of the Pacific Northwest sake scene, the publication described the sake as having an aromatic profile of sweet hay, meadow herbs, honeysuckle, and hazelnut. On the palate, they noted a predominantly herbal and moderately honeyed character, balanced by a crisp acidity over a sweet cereal base.
* **Elle Canada & Air Canada’s EnRoute Magazine:** Both publications highlighted the sake as rich, savoury, and complex, praising its racy acidity and delicate touch of sweetness. 
* **Wayward Wine:** An early review of the Fraser Valley-sourced batches noted that the local rice yielded a sake that was waxier, drier, and more mineral-driven than the producer's standard Calrose-based Junmai.
* **The Producer's Profile:** Artisan SakeMaker describes this off-dry sake as having an unprecedented level of acidity, complex flavours, and a mature, superior balance designed to appeal to modern wine aficionados. 

### Awards
* **Judge's Selection** – Alberta Beverage Awards (2016)
* **Silver Medal** – NorthWest Wine Summit (2017)

### Food Pairings
Because of its pronounced acidity and savoury umami profile, this sake is highly versatile at the table. The winery and local critics recommend pairing it with:
* Charcuterie and cheeses
* Roasted chicken or pizza
* Miso/kasu black cod or seafood chowder
* Richer Japanese dishes (it has been featured in premium local kaiseki pairings at Vancouver's Kishimoto restaurant)
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSq8-ToUuBYthqbn5fUM3JBPsL7BPJ3X9xjKdw8v92-HunYuF3aIj02MMWq9YNCPcWv60IUKm-8caM077wcYRY3TlsuLlRdVWN0XlAuUiNCQAHmw3vR3jE): 
  - [sipmagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkaiGI53_ioX7vNqaLXTjeJa1cLQziIQqK_VzkBOdhSkH1EEWzfRMQ2kh5RHhHzQ_emu2ApbU4AIoNJUb_hYozOaY2RjIyMWx5Gfnfdpcs-Lh9pprbha0fOQYtTe5da2e_EVR5AK8gfz-onxiLLA==): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8d8M0jCiKH5H6KM57mnKCS0x6Lt3pAawCfezEg6kCWQPVj_JMSr5nVt7yNYKaTcHM2Um0xao9sKRHzp790fVeihJuw9TPejxGHoneL34lmLPZGyhEsXYL86pHEoGmxFU8-5ZY0FFE6lXmgOYu1WncxdkwxvA9mk7_NhtCBkxuxzUPQ5Yaxw==): 
  - [ellecanada.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4MwDAa_N02gADMiTFOzXAGJkWycuSLsFZQVu6h06VMJ5H3UOLZ0ZLEwlVB5Is-rmHx2YCT9V5iTqnKR-1INIlqJgQpnwow5T0kGqXxI3z1UX6er0gCVCIPvYcXDDmoUNJlnvrJM-1XbLYz1rPBaQGNMSi2RreMcHwf4faZV4iaa8bikLL_cxc5d40xRkKYCTEGYiyLwIzrCisTEmSBFs-G1SyCyAmkuPN): 
  - [ellecanada.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSrB2oBADbD3ZB0-aI6bxJ1zmm0UbtWNTD8HxbYfFNvltmQ9AwL4Q9VftSRGNdCyb1k14ATPV5ThSZ3IPVMPJ7jyH2tmub_A-sO5QwKRtd6sj06sKmzLZss12X9jAd88l5eYBj66jfupnPm2SECP6ZkIdMsvw39BNhoZ4H--LKPYPzcizjRWFBY9Rn4FhoBDZBOWVceqYx9rxjrQ==): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcdkulyyXTtr_liC5RSEq2ef_Ht4UYlpI0_sKj6xKLkIoTrxyP4Uz1pJNFNPA44XN9IC6HDEdcSorCHoZZcAkAOAeUfzUSPeF5sK8EgnMZAkAZKKEH2HlBxN7hW9xH_S2fzP4zDVEx71GssN9_tqvLJqvq7AYYJQlNORVeMDeTRP4hQQU1fgWulUZFBXAGYOhemg==): 
  - [waywardwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQwqxbeZQFt4NxBIrr-6AraP-2SOVO_NVoDHa8ea14mOfS7vesrLhAdXGsmr5g0EyCkV19tIJG1PuWhnBPbAlecyhddZ0XrVfBep6zdUbXtpcoyzO64DaV0h38hp6gdDRcCN7Nt7dVw-Kg): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAGkw34IO3ZX9tte2hCbZM1sF0HeNTU8XgY--LBV9qWBNQsLFLAlkQAmhq0ym-QJ_llf8bWhE_xIW42fv4zjNYrL9U_VLL-sN4mcBkwFwm3zG6Nsgq7shvZkTIxq-OVIl6EpJrqB3JoQc-): 
  - [wixsite.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH95Pn1PPx6mwLYkcnPYj2vDa6Zdnl1lujLDtay8HWLm7O9SdwUQbfFfW8jatWMgDcHqJzPXkmfs1jazkpBncKyZHRG68FCq_peZW-sF1JPzNS2MQ8tyRy7bdV-NHTwkOPp95WHBEkS3EgzVYYAl4sbHmxOEF6q8c95ncjWiBZUoWKuOAgsWK7sqJGEzx-b_Vj8Vpcoq_RHyOPkIgq18lPqXRdQTdU=): 
  - [pendulummag.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBrheJYeHa1AYUMvbDKbrj8efju4eSLoVJ5UHukqCpgxdzyOjapdU9HHvc8gTmg4nFAtaKPKfIZlGzSKd1i9MPi9bQAQNKPBLKTD5xF2jRiWm9o52v2OIXgJzvxic85CXc_2hgAW7z2grlOgvKiB_j_QuDKVkHU_7amInK2z9hIHw7pqJQwLHbfDHl6cGhMgx6QsY3fltAR8noWpIQxdpAb4GdI2KkF86pLMkl-JCN5fYJH9K_kY5Y): 
  - [myvancity.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV1CBb1o2UJ7-qGnQZ3SmID9xv8ygcofTG8mCsN1yi0w5aPMI18iEYEeIB6OwEvfxftXhOUP6Nu-LN7WQq6M6eY_AIVmb3Lfa457djTjYfhSRcqLD9wX2XK-xBbQlAa8pnp9G7xtHckOHqXOhX_91M4JdBeRVOC14I): 

#### search_web_grounded_tool (status=ok, 6 results)
Search answer: **Odd Society Wallflower Gin** is a signature craft spirit produced by Odd Society Spirits, located in East Vancouver, British Columbia. 

### Overview and Production
Wallflower Gin is crafted from a base of 100% BC-grown barley. It is distilled in small batches using a custom-designed copper pot still that utilizes both maceration and vapour extraction to infuse a mix of local coastal and international botanicals. The gin is bottled at 44% ABV.

### Tasting Notes Summary
* **Nose:** Reviewers describe the aroma as highly aromatic and floral-forward. *BC Spirits* highlights notes of woody lavender, spicy juniper, and earthy botanicals. Other reviews, such as one from *Gingineerist*, note elegant coriander and soft floral tones, while a community review on Reddit points to bright citrus elements like mandarin orange zest and yuzu.
* **Palate:** On the palate, the initial floral sweetness subsides to the background. *BC Spirits* notes that the spirit leans into a complex, piney, and classic juniper-forward profile. *Gingineerist* describes the taste as bright, delicately sweet, and clean, while the Reddit review highlights a unique combination of mandarin orange juice, pink peppercorn, and herbal chartreuse-like notes.
* **Finish:** The finish is widely regarded as long, clean, and complex, with lingering juniper and soft, elegant floral notes.

### Serving Recommendations
* **In a G&T:** *BC Spirits* recommends Wallflower as an excellent choice for a classic Gin & Tonic. *Gingineerist* suggests pairing it with a light, dry tonic (such as Fever-Tree) or club soda with a citrus peel garnish to avoid masking the gin's delicate floral sweetness. 
* **Neat:** While it can be enjoyed neat, reviewers note that mixing it with tonic particularly helps to amplify its lavender and citrus characteristics.

### Notable Variants
Odd Society also produces two popular spin-offs of this flagship gin:
* **Wallflower Oaken Gin:** An expression aged in oak barrels. *BC Spirits* describes it as a rich, full-bodied gin that balances the original botanicals with sweet pine, vanilla, and dry oak, making it an excellent substitute for whiskey in an Old Fashioned.
* **Strawberry Wallflower Gin:** A seasonal variation steeped with fresh Fraser Valley strawberries from Driediger Farms. It offers a pink hue with a sweet, juicy strawberry nose and a tart, refreshing palate.
  - [bcspirits.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa-p5_Ur2o85FDPWXET12jCWzL_3LhSGm6eTJmm7ltGVC2KPRewl6Qs53fO76Tyun6EpHpeVUwV9Ws4kUCTYINySv4bNHZmF-Lc3mD8xTVBVwPvKoftyT0RsNwjvwlsiosVBlOsFHCVh5--mSU2xK2uCLDuqF7ElHwA7Z_JkT2KqIKwyvOKB-1o65c0pEpGw==): 
  - [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrr4YT7labFoDptf1pvMcDT4N87-Pke91G-AQg1jDddrFF-_ChUa9_4SV-nTevfcl0-A_wJ2drljwJlSVRnLhgLpp00WWfxk428KMV9M_VZzXUVzLrgKUv9cPglLYC86_dHXw-GJPZHS2EjZG1sOpXFc9ER4HFccYbS_BZ7hf2ePJ1BIcIvGIt1W4qQVVEkrx3VZzVZE5D6Q==): 
  - [edgefurnish.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI_ipSe0sohL0TWlB0JJ_bYZf6pOOBEJTbC5z3VaTUZypG01Vl4yRZq3FY_ZEwwG8V_pnlJS7HuedRmoDSTJRuEj2OdDW7WTV3v8HUDvibYInkjtGXZO3T5IU_nBkhf4xPVOCWaboERS9zQ7OoidkZHV0dDxc=): 
  - [iscotch.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4HZ9hHoRk8VwMXXgcd1s5IoymPAhmGc86JEZyHD-TXzzlJrYWNiHC8slTxovfKKmlJTN_BX7-z7XGDwnOQ4O55b8GgkPkEjRZmwqAzN1k0nT_1CRYqBnYvyNN0Es95kHuKYhVqP-p7qhhHGxqTee1wKVct8u55HZl): 
  - [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRjEYCTUDVuuS8AXx09verpkJ9kLZ4BFR3FW6IUp7Kj2TBz56pZ1XvLxJKR2-e5bW4rh6w96j0pilMZNZUzuFBR6qx9X0HPC-MvjAmnVtcIVgh0erLJZkJsrG0pEuvrNR0IPslGg==): 
  - [thedrinkguy.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc7219EKT7dE3huZ6eBwasiD3Ev_Z72i0huNZiIvYM3jZ9x-QS_b_8HBaWauvL76UC6bjVN6F7tP111lMSxeKEx-e61XlYRJwBG8PvUHx-k20eOtPeoSNWg72bmOBnxzN1mf5wLrNQQT_ihZ9P1SZgF0jwk7XBrtZrhqDnR9ghNW6XTUtf8AvXIOulLxuVEaHTmxyp0ouaC2NHEykY): 


### sourcing_agent_tool (status=ok)
**Sub-agent synthesis:**
Here is a curated list of BC red wines under $35 that are currently **in stock** at Vancouver retail locations. 

---

### **Sutton Place Wine Merchant** (Yaletown, Vancouver)
*Boutique selection with exact stock quantities.*

* **Clos Du Soleil Célestiale 2019** (Red Blend) — **$34.99** (41 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4205421-clos-du-soleil-celestiale)
* **Blue Mountain Gamay 2020** — **$33.99** (4 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4228470-blue-mountain-gamay)
* **Bartier Bros Granite 2021** (Red Blend) — **$32.99** (12 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4944430-bartier-bros-granite)
* **Bench 1775 Syrah 2021** — **$32.99** (2 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4571295-bench-1775-syrah)
* **Bonamici Cellars Merlot - Cabernet Franc 2021** — **$32.99** (7 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4143755-bonamici-cellars-merlot-cabernet-franc)
* **Bench 1775 Cabernet Sauvignon Merlot 2019** — **$31.49** (5 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4571291-bench-1775-cabernet-sauvignon-merlot)
* **Averill Creek Joue Red 2021** (Red Blend) — **$29.49** (6 in stock) | [Buy here](https://store.suttonplacewinemerchant.com/products/4143614-averill-creek-joue-red)

---

### **Marquis Wine Cellars** (Davie St, Vancouver)
*Curated boutique selection with exact stock quantities.*

* **Meyer Family 2023 Pinot Noir** — **$34.99** (12 in stock) | [Buy here](https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/)
* **Pamplemousse Jus 2025 Foch Nouveau** — **$34.99** (8 in stock) | [Buy here](https://www.marquis-wines.com/pamplemousse-jus-2025-foch-nouveau-750ml/)
* **Nichol 2022 Cabernet Franc 'The Village'** — **$32.99** (4 in stock) | [Buy here](https://www.marquis-wines.com/nichol-2022-cabernet-franc-the-village-750ml/)
* **Quails Gate 2022 Old Vines Foch** — **$31.99** (2 in stock) | [Buy here](https://www.marquis-wines.com/quails-gate-2019-old-vines-foch-750ml/)
* **Vasanti 2022 Cabernet Sauvignon** — **$31.99** (10 in stock) | [Buy here](https://www.marquis-wines.com/vasanti-2022-cabernet-sauvignon-750ml/)
* **Cassini 2023 Pinot Noir "Red Carpet"** — **$29.99** (24 in stock) | [Buy here](https://www.marquis-wines.com/cassini-2022-pinot-noir-red-carpet-750ml/)
* **Lock & Worth 2023 Merlot** — **$27.99** (9 in stock) | [Buy here](https://www.marquis-wines.com/lock-worth-2022-merlot-750ml/)
* **Tinhorn Creek 2023 Cabernet Franc** — **$27.99** (47 in stock) | [Buy here](https://www.marquis-wines.com/tinhorn-creek-2023-cabernet-franc-750ml/)
* **Three Sisters Bench Red** — **$25.99** (4 in stock) | [Buy here](https://www.marquis-wines.com/three-sisters-bench-red-750ml/)
* **Gray Monk 2021/24 Pinot Noir** — **$24.99** (18 in stock) | [Buy here](https://www.marquis-wines.com/gray-monk-2019-pinot-noir-750ml/)
* **Domaine Artema 2022 Black Sage Road Rouge** — **$24.49** (14 in stock) | [Buy here](https://www.marquis-wines.com/domaine-artema-2022-black-sage-road-rouge-750ml/)
* **Mission Hill Five Vineyards Cabernet/Merlot** — **$20.99** (68 in stock) | [Buy here](https://www.marquis-wines.com/mission-hill-2018-five-vineyards-cabernet-merlot-750ml/)

---

### **Everything Wine** (River District, Vancouver)
*Exact stock quantities for the Vancouver store location.*

* **Crown & Thieves Scoundrels Punch Red Blend** — **$34.98** (9 in stock) | [Buy here](https://www.everythingwine.ca/crown-thieves-scoundrels-punch-red-blend-750-ml)
* **Evolve Cellars Momento Red Blend** — **$24.99** (3 in stock) | [Buy here](https://www.everythingwine.ca/evolve-cellars-momento-red-blend-750-ml)
* **Narrative By Okanagan Crush Pad Red Blend** — **$24.98** (18 in stock) | [Buy here](https://www.everythingwine.ca/narrative-red)
* **Chaberton Estate Winery Red Blend** — **$23.98** (4 in stock) | [Buy here](https://www.everythingwine.ca/chaberton-cuvee-rouge)

---

### **BC Liquor Stores** (Multiple Vancouver Locations)
*Widely distributed across Vancouver government stores. Prices are standard.*

* **Daydreamer Jasper Merlot Cabernet** (BC VQA) — **$32.99** | [Buy here](https://www.bcliquorstores.com/product/768408)
* **Mt. Boucherie Reserve Meritage 2024** — **$29.99** | [Buy here](https://www.bcliquorstores.com/product/658474)
* **Hester Creek Syrah** (BC VQA) — **$27.99** | [Buy here](https://www.bcliquorstores.com/product/504399)
* **Screaming Frenzy Meritage** (BC VQA) — **$26.99** | [Buy here](https://www.bcliquorstores.com/product/179372)
* **Mt. Boucherie OV PTG** (BC VQA Pinot Noir/Gamay) — **$25.99** | [Buy here](https://www.bcliquorstores.com/product/78218)
* **Modest Wines Blaufränkisch** (BC VQA) — **$25.99** | [Buy here](https://www.bcliquorstores.com/product/369760)
* **Gneiss Pendulum** (BC VQA Red Blend) — **$25.99** | [Buy here](https://www.bcliquorstores.com/product/399223)

#### search_bcliquor_tool (status=ok, 48 results)
  - PHANTOM CREEK ESTATES - BC ROSE 2025 | $29.99 | stock=804 | in 73 stores | rating=4.6 | https://www.bcliquorstores.com/product/329902 | {sku=329902; product_type=Rose Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=From the dedicated blocks of Becker, Ryegrass, Richter and Evernden Spring Vineyards, Phantom Creek Estates Rosé reflects the complexity that comes from our organic-certified terroirs of the Okanagan and Similkameen Valleys. It is dry, finessed and nuanced, with delicate red berries and layers of spice.
; consumer_votes=35; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/329902.jpeg; certificates=["BC VQA", "All VQA"]}
  - GRIGNOLINO DEL MONFERRATO CASALESE - ACCORNERO BRICCO DEL BO | $31.99 | stock=58 | in 8 stores | rating=4.6 | https://www.bcliquorstores.com/product/63584 | {sku=63584; product_type=Red Wine; grape_type=OTHER GRAPE VARIETY; country=Italy; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=92 Points, Vinous: "The 2020 Grignolino Bricco del Bosco is a classic wine from this often overlooked red variety. Ethereal and weightless in the glass, the 2020 offers up scents of rosewater, cinnamon, orange peel, mint and sweet pipe tobacco, all framed by silky tannins that lend finesse. What a beautiful wine this is. Drinking Window: 2022 - 2028." (January 2022)
; consumer_votes=74; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/63584.jpeg}
  - SAUMUR CABERNET FRANC - DOMAINE DE ROCHEVILLE LES PIERRES BL | $28.99 (reg $32.99) | stock=261 | in 25 stores | rating=4.6 | https://www.bcliquorstores.com/product/192945 | {sku=192945; product_type=Red Wine; grape_type=CABERNET FRANC; country=France; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=On the palate, the wine is vibrant and well-structured, showcasing a core of bright red fruit, cherry, raspberry, and wild strawberry. Balanced by refined tannins and lively acidity. Delicate notes of graphite and gentle spice emerge with aeration, adding complexity and finesse. The finish is long and harmonious, with persistent red fruit flavors and a subtle savory character that lingers gracefully.
; consumer_votes=6; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/192945.jpeg}
  - RED TRUCK -  ORIGINAL PILSNER CAN | $27.99 | stock=1435 | in 95 stores | rating=4.0 | https://www.bcliquorstores.com/product/669034 | {sku=669034; country=Canada; volume=0.355; alcohol_pct=5.0; consumer_votes=16; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/669034.jpeg}
  - PARALLEL 49 - TRICYCLE GRAPEFRUIT RADLER TALL CAN | $2.99 | stock=7016 | in 107 stores | rating=3.3 | https://www.bcliquorstores.com/product/294962 | {sku=294962; country=Canada; volume=0.473; alcohol_pct=3.5; tasting_notes=A crisp lager infused with ruby red grapefruit for a refreshing, citrus-forward experience.
; consumer_votes=61; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/294962.jpeg}
  - RED TRUCK - LAGER CAN | $16.99 | stock=2129 | in 143 stores | rating=4.0 | https://www.bcliquorstores.com/product/4215 | {sku=4215; country=Canada; volume=0.355; alcohol_pct=5.0; tasting_notes=This traditional European-style lager is made with all Canadian malts and Saaz hops, a classic "noble" aroma hop with longstanding traditions just like the style itself. Clean and crisp in style, this lager is designed to be an easy-drinking, full-bodied beer that doesn't compete with anything you're eating.
; consumer_votes=210; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/4215.jpeg}
  - RED RACER - SESSION IPA 4PK | $10.99 | stock=2737 | in 118 stores | rating=3.6 | https://www.bcliquorstores.com/product/711396 | {sku=711396; country=Canada; volume=0.473; alcohol_pct=4.0; tasting_notes=Crisp and light-bodied with vibrant grapefruit and pine notes. A balanced citrusy hop character complements a subtle malt backbone, delivering a clean, refreshing finish ideal for warm weather sipping.; consumer_votes=9; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/711396.jpeg}
  - RED TRUCK - ORIGINAL LAGER TALL CAN | $1.99 (reg $2.69) | stock=7597 | in 94 stores | rating=4.3 | https://www.bcliquorstores.com/product/711680 | {sku=711680; country=Canada; volume=0.473; alcohol_pct=5.0; consumer_votes=13; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/711680.jpeg}
  - BODACIOUS - BOURBON | $11.99 | stock=2516 | in 169 stores | rating=3.9 | https://www.bcliquorstores.com/product/165991 | {sku=165991; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=12.0; sweetness=02; tasting_notes=Rich, bold, smooth and tasty, with aromas of black cherry, vanilla and spice.
; consumer_votes=139; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/165991.jpeg}
  - BODACIOUS - CABERNET SAUVIGNON | $11.97 | stock=1069 | in 108 stores | rating=3.6 | https://www.bcliquorstores.com/product/430959 | {sku=430959; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=02; tasting_notes=Juicy, ripe and robust, with aromas of blackberry and blackcurrant.
; consumer_votes=183; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/430959.jpeg}
  - MT. BOUCHERIE - RESERVE MERITAGE 2024 | $29.99 | stock=1569 | in 142 stores | rating=5.0 | https://www.bcliquorstores.com/product/658474 | {sku=658474; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=13.3; sweetness=00; consumer_votes=1; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/658474.jpeg}
  - RED TRUCK BEER - HARD DAY NORTHWEST IPA 8 CAN | $14.99 (reg $17.49) | stock=1738 | in 140 stores | rating=4.1 | https://www.bcliquorstores.com/product/136901 | {sku=136901; country=Canada; volume=0.355; alcohol_pct=6.3; tasting_notes=Crystal malts balanced with a truckload of hops bring you a toffee malty sweetness with a dry fresh finish. This IPA will stand up to even the most intense dishes. Take it for a spin with the spiciest wings you can find.
; consumer_votes=93; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/136901.jpeg}
  - RED TRUCK - ORIGINAL IPA TALL CAN | $2.59 (reg $3.19) | stock=9526 | in 109 stores | rating=3.5 | https://www.bcliquorstores.com/product/295168 | {sku=295168; country=Canada; volume=0.473; alcohol_pct=6.3; tasting_notes=The "Original IPA" stands as the cornerstone recipe behind our acclaimed IPAs. Crafted with a nod to to a simpler era, this original masterpiece combines late kettle additions and a touch of dry hopping, capturing the true spirit of the Pacific Northwest; consumer_votes=20; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/295168.jpeg}
  - RED TRUCK -  ORIGINAL IPA CAN | $29.79 | stock=2438 | in 149 stores | rating=3.8 | https://www.bcliquorstores.com/product/379076 | {sku=379076; country=Canada; volume=0.355; alcohol_pct=6.3; tasting_notes=The "Original IPA" stands as the cornerstone recipe behind our acclaimed IPAs. Crafted with a nod to to a simpler brewing era, this original masterpiece combines late kettle additions and a touch of dry hopping, capturing the true spirit of the Pacific Northwest - the very region in which our brewery was founded.
; consumer_votes=106; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/379076.jpeg}
  - BODACIOUS - SMOOTH RED | $19.99 | stock=2343 | in 163 stores | rating=3.5 | https://www.bcliquorstores.com/product/39313 | {sku=39313; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=1.500; alcohol_pct=12.5; sweetness=02; tasting_notes=A bold, ripe, juicy and full-bodied red that blends together Merlot and Cabernet Sauvignon. Rich flavours and aromas of blueberries and blackcurrant are present from start to finish.
; consumer_votes=211; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/39313.jpeg}
  - DOMAINE D'OR - RED | $37.99 | stock=1609 | in 165 stores | rating=3.5 | https://www.bcliquorstores.com/product/108688 | {sku=108688; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=4.000; alcohol_pct=11.5; sweetness=00; tasting_notes=A medium-bodied wine with aromas and flavours of ripe red berries, strawberries and cherries.
; consumer_votes=71; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/108688.jpeg}
  - MISSION RIDGE - PREMIUM DRY RED | $37.99 | stock=1669 | in 177 stores | rating=3.5 | https://www.bcliquorstores.com/product/215590 | {sku=215590; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=4.000; alcohol_pct=11.0; sweetness=01; tasting_notes=A well-balanced red wine with supple tannins and notes of cassis. The finish is velvety with notes of spice.
; consumer_votes=166; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/215590.jpeg}
  - BODACIOUS - SMOOTH RED | $11.99 | stock=3599 | in 194 stores | rating=3.6 | https://www.bcliquorstores.com/product/459677 | {sku=459677; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=02; tasting_notes=A bold, ripe, juicy and full-bodied red that blends together Merlot and Cabernet Sauvignon. Rich flavours and aromas of blueberries and blackcurrant are present from start to finish.
; consumer_votes=446; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/459677.jpeg}
  - RED RACER -  WEST COAST IPA CAN | $10.99 (reg $12.99) | stock=3172 | in 144 stores | rating=4.0 | https://www.bcliquorstores.com/product/663977 | {sku=663977; country=Canada; volume=0.473; alcohol_pct=6.5; tasting_notes=The IPA was fashioned to survive the long voyage from England to India during the British colonization. Hops, hops, and more hops! Red Racer IPA has an intense aroma and a long lingering finish. A beer for the connoisseur, this is the brew master's choice.; consumer_votes=4; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/663977.jpeg}
  - PELLER FAMILY VINEYARDS - CABERNET MERLOT | $42.99 | stock=1778 | in 160 stores | rating=3.4 | https://www.bcliquorstores.com/product/617696 | {sku=617696; product_type=Red Wine; grape_type=CABERNET/MERLOT; country=Canada; volume=4.000; alcohol_pct=12.0; sweetness=00; tasting_notes=Rich aromas of black fruit are followed by a smooth, fruity finish that goes well with grilled meats and pizza.
; consumer_votes=70; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/617696.jpeg}
  - CALONA - ROYAL RED | $16.99 | stock=1328 | in 168 stores | rating=3.2 | https://www.bcliquorstores.com/product/2303 | {sku=2303; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=2.000; alcohol_pct=12.5; sweetness=04; tasting_notes=This semi-sweet red wine is perfect for drinking on its own or for making summer sangria. It pairs well with chocolate desserts.
; consumer_votes=128; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/2303.jpeg}
  - DOMAINE D'OR - RED | $15.99 | stock=1291 | in 150 stores | rating=3.0 | https://www.bcliquorstores.com/product/87965 | {sku=87965; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=1.500; alcohol_pct=11.5; sweetness=00; tasting_notes=A medium-bodied wine with aromas and flavours of ripe red berries, strawberries and cherries.
; consumer_votes=58; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/87965.jpeg}
  - BODACIOUS - SMOOTH RED | $44.99 | stock=2643 | in 197 stores | rating=3.9 | https://www.bcliquorstores.com/product/125680 | {sku=125680; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=4.000; alcohol_pct=12.5; sweetness=00; tasting_notes=A bold, ripe, juicy and full-bodied red that blends together Merlot and Cabernet Sauvignon. Rich flavours and aromas of blueberries and blackcurrant are present from start to finish.
; consumer_votes=71; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/125680.jpeg}
  - RED TRUCK - CLASSIC LAGER CAN | $19.99 (reg $27.99) | stock=6331 | in 157 stores | rating=4.0 | https://www.bcliquorstores.com/product/36577 | {sku=36577; country=Canada; volume=0.355; alcohol_pct=5.0; tasting_notes=This traditional European-style lager is made with all Canadian malts and Saaz hops, a classic "noble" aroma hop with longstanding traditions just like the style itself. Clean and crisp in style, this lager is designed to be an easy-drinking, full-bodied beer that doesn't compete with anything you're eating.
; consumer_votes=217; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/36577.jpeg}
  - MT. BOUCHERIE - OV PTG | $25.99 | stock=561 | in 51 stores | rating=4.0 | https://www.bcliquorstores.com/product/78218 | {sku=78218; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=14; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/78218.jpeg; certificates=["BC VQA", "All VQA"]}
  - MT. BOUCHERIE - RSV GSM | $39.99 | stock=451 | in 27 stores | rating=5.0 | https://www.bcliquorstores.com/product/130708 | {sku=130708; product_type=Red Wine; grape_type=GRENACHE/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; consumer_votes=1; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/130708.jpeg; certificates=["BC VQA", "All VQA"]}
  - HESTER CREEK - GARLAND 2015 | $79.99 | stock=109 | in 21 stores | rating=5.0 | https://www.bcliquorstores.com/product/145362 | {sku=145362; product_type=Red Wine; grape_type=BORDEAUX BLEND; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; consumer_votes=2; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/145362.jpeg; certificates=["BC VQA", "All VQA"]}
  - MODEST WINES - BLAUFRANKISCH | $25.99 | stock=260 | in 36 stores | rating=4.3 | https://www.bcliquorstores.com/product/369760 | {sku=369760; product_type=Red Wine; grape_type=OTHER GRAPE VARIETY; country=Canada; volume=0.750; alcohol_pct=13.4; sweetness=01; consumer_votes=3; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/369760.jpeg; certificates=["BC VQA", "All VQA"]}
  - GNEISS - PENDULUM | $25.99 | stock=430 | in 27 stores | rating=4.6 | https://www.bcliquorstores.com/product/399223 | {sku=399223; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=13.7; sweetness=00; consumer_votes=5; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/399223.jpeg; certificates=["BC VQA", "All VQA"]}
  - KALALA - ASPIRE | $30.99 | stock=11 | in 1 stores | https://www.bcliquorstores.com/product/548693 | {sku=548693; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=14.4; sweetness=00; consumer_votes=0; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/548693.jpeg; certificates=["BC VQA", "All VQA"]}
  - DAYDREAMER - JASPER MERLOT CABERNET | $32.99 | stock=327 | in 27 stores | rating=4.0 | https://www.bcliquorstores.com/product/768408 | {sku=768408; product_type=Red Wine; grape_type=MERLOT; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; consumer_votes=3; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/768408.jpeg; certificates=["BC VQA", "All VQA"]}
  - FERNIE BREWING - CRAFT COLLECTION PACK CAN | $24.79 | stock=947 | in 90 stores | rating=3.3 | https://www.bcliquorstores.com/product/392343 | {sku=392343; country=Canada; volume=0.355; alcohol_pct=5.0; tasting_notes=This popular 12-pack has something to satisfy the tastes of every craft beer lover. Featuring three cans of each - Project 9 Pils, Headwall Hazy Pale Ale, Waymark West Coast IPA and Ridgewalk Red Ale. The perfect pairing to any and all adventures. 
; consumer_votes=57; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/392343.jpeg}
  - STEAMWORKS - MASH-UP 8 TALL CAN PACK | $22.99 | stock=1599 | in 146 stores | rating=4.3 | https://www.bcliquorstores.com/product/862375 | {sku=862375; country=Canada; volume=0.473; alcohol_pct=5.0; tasting_notes=Experience the ultimate fusion of Steamworks' finest brews with our original Mash-Up. Whether you crave hazy and hoppy or prefer clear and crisp, this collection caters to every palate. Each pack includes the Flagship IPA, Pale Ale, Pilsner and Heroica Red Ale.
; consumer_votes=183; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/862375.jpeg}
  - PELLER FAMILY VINEYARDS - CABERNET SAUVIGNON | $10.47 | stock=1191 | in 93 stores | rating=3.2 | https://www.bcliquorstores.com/product/164616 | {sku=164616; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Garnet colour with a bouquet of blackcurrant, black cherry and just a whiff of smoke and spice. It goes well with grilled meats and mild chili.
; consumer_votes=88; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/164616.jpeg}
  - PELLER FAMILY VINEYARDS - CABERNET SAUVIGNON | $17.99 | stock=2089 | in 161 stores | rating=3.3 | https://www.bcliquorstores.com/product/198226 | {sku=198226; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=1.500; alcohol_pct=12.5; sweetness=00; tasting_notes=Garnet colour with a bouquet of blackcurrant, black cherry and just a whiff of smoke and spice. It goes well with grilled meats and mild chili.
; consumer_votes=34; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/198226.jpeg}
  - JACKSON TRIGGS PROPRIETOR'S SELECTION SHIRAZ | $44.99 | stock=1965 | in 180 stores | rating=3.3 | https://www.bcliquorstores.com/product/201368 | {sku=201368; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=4.000; alcohol_pct=13.0; sweetness=00; tasting_notes=Aromas of raspberry and blackberry with hints of cracked pepper follow through the long spicy finish.
; consumer_votes=74; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/201368.jpeg}
  - COPPER MOON - SMOOTH RED | $11.99 | stock=646 | in 66 stores | rating=3.2 | https://www.bcliquorstores.com/product/132253 | {sku=132253; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=02; tasting_notes=Purple garnet in colour. A bouquet of blue plum, blueberry, black cherry, sweet vanilla and sweet spice. A medium-bodied red wine with a smooth mouthfeel and flavours of juicy dark fruits which linger on the finish.
; consumer_votes=28; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/132253.jpeg}
  - KALALA - ZWEIGELT 2021 | $24.49 | stock=28 | in 1 stores | https://www.bcliquorstores.com/product/89326 | {sku=89326; product_type=Red Wine; grape_type=OTHER GRAPE VARIETY; country=Canada; volume=0.750; alcohol_pct=12.8; sweetness=00; consumer_votes=0; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/89326.jpeg; certificates=["BC VQA", "All VQA"]}
  - SCREAMING FRENZY - MERITAGE | $26.99 | stock=173 | in 19 stores | rating=4.0 | https://www.bcliquorstores.com/product/179372 | {sku=179372; product_type=Red Wine; grape_type=CABERNET/MERLOT; country=Canada; volume=0.750; alcohol_pct=14.6; sweetness=00; consumer_votes=7; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/179372.jpeg; certificates=["BC VQA", "All VQA"]}
  - RUST WINE CO - ZINFANDEL | $38.99 | stock=414 | in 35 stores | rating=4.5 | https://www.bcliquorstores.com/product/298723 | {sku=298723; product_type=Red Wine; grape_type=ZINFANDEL; country=Canada; volume=0.750; alcohol_pct=14.8; sweetness=00; consumer_votes=11; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/298723.jpeg; certificates=["BC VQA", "All VQA"]}
  - HESTER CREEK - GSM | $37.99 | stock=708 | in 54 stores | rating=4.4 | https://www.bcliquorstores.com/product/356983 | {sku=356983; product_type=Red Wine; grape_type=OTHER GRAPE VARIETY; country=Canada; volume=0.750; alcohol_pct=13.8; sweetness=00; consumer_votes=11; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/356983.jpeg; certificates=["BC VQA", "All VQA"]}
  - HESTER CREEK - SYRAH | $27.99 | stock=10 | in 2 stores | rating=3.9 | https://www.bcliquorstores.com/product/504399 | {sku=504399; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=13.8; sweetness=00; consumer_votes=16; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/504399.jpeg; certificates=["BC VQA", "All VQA"]}
  - PELLER FAMILY VINEYARDS - SHIRAZ | $42.99 | stock=1482 | in 140 stores | rating=3.2 | https://www.bcliquorstores.com/product/361022 | {sku=361022; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=4.000; alcohol_pct=13.0; sweetness=00; tasting_notes=Flavours of black cherry and a hint of spice are enhanced by rich red fruit aromas. It pairs well with grilled steak, roast beef and lamb.
; consumer_votes=68; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/361022.jpeg}
  - SCREW IT! - THE RED | $10.99 | stock=14 | in 3 stores | rating=3.3 | https://www.bcliquorstores.com/product/485003 | {sku=485003; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Openly fruity, lush and layered, Screw it! The Red is a tantalizing combination of ripe fruits and velvety textures. Full-bodied and supple, this wine is made in a rich style that ends in a long, juicy red fruit finish. An inviting treat!
; consumer_votes=146; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/485003.jpeg}
  - BASK - PINOT NOIR | $12.99 | stock=2420 | in 167 stores | rating=3.3 | https://www.bcliquorstores.com/product/9330 | {sku=9330; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=00; tasting_notes=Just BASK in 0g sugar per serving. That's one less thing to worry about, so you can zero in on the moment and savour every second. BASK Pinot Noir has aromas of dark cherry and subtle notes of spice. Well-balanced and perfect on its own or with a meal.
; consumer_votes=353; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/9330.jpeg}
  - COPPER MOON - MERLOT | $16.99 (reg $19.99) | stock=1425 | in 134 stores | rating=3.2 | https://www.bcliquorstores.com/product/129684 | {sku=129684; product_type=Red Wine; grape_type=MERLOT; country=Canada; volume=1.500; alcohol_pct=12.5; sweetness=00; tasting_notes=Enjoy a rich bouquet of black cherry, blackcurrants, blue plums and hints of spice and oak.
; consumer_votes=49; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/129684.jpeg}
  - COPPER MOON - MALBEC | $10.49 (reg $11.99) | stock=3389 | in 185 stores | rating=3.4 | https://www.bcliquorstores.com/product/164368 | {sku=164368; product_type=Red Wine; grape_type=MALBEC; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=A bouquet of vanilla, chocolate and field berries is complemented by cherry and blackcurrant flavours.
; consumer_votes=230; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/164368.jpeg}
  - SAWMILL CREEK - CABERNET SAUVIGNON | $42.99 | stock=1593 | in 177 stores | rating=3.2 | https://www.bcliquorstores.com/product/374108 | {sku=374108; product_type=Red Wine; grape_type=CABERNET SAUVIGNON; country=Canada; volume=4.000; alcohol_pct=12.5; sweetness=00; tasting_notes=This wine captivates with its deep ruby colour and rich aromas of blackberries, blackcurrants, and black cherries. On the palate, it's full-bodied and powerful, showcasing layers of dark fruit flavours like blackcurrant and blueberries. The finish is smooth, with subtle woody notes that add a satisfying touch of warmth.
; consumer_votes=61; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/374108.jpeg}

#### search_everything_wine_tool (status=ok, 24 results)
  - Fairview Cellars Two Hoots Red Blend 750 mL | $36.98 | [North Vancouver:20, South Surrey:11, Langley Store:11, Vancouver:11] | https://www.everythingwine.ca/fairview-cellars-two-hoots-red-blend-750-ml | {sku=250087; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/5/250087_fairview_twohoots_nl.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Evolve Cellars Momento Red Blend 750 mL | $24.99 | [North Vancouver:0, South Surrey:0, Langley Store:8, Vancouver:3] | https://www.everythingwine.ca/evolve-cellars-momento-red-blend-750-ml | {sku=389273; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/8/389273_evolve_momento_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Dirty Laundry Vineyard Hush Red 750 mL | $21.99 | [North Vancouver:14, South Surrey:0, Langley Store:6, Vancouver:0] | https://www.everythingwine.ca/dirty-laundry-vineyard-hush-red-750-ml | {sku=11888; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/1/11888_dirty_laundry_hush_red_blend.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Pacific Breeze Killer Cab Red Blend 750 mL | $27.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/pacific-breeze-killer-cab | {sku=114769; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/1/114769_pacific-breeze-killer-cab.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - French Door Estate Winery Fleur Red Blend 750 mL | $39.98 | [North Vancouver:8, South Surrey:0, Langley Store:10, Vancouver:0] | https://www.everythingwine.ca/french-door-estate-winery-fleur-red-blend-750-ml | {sku=396661; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/9/396661_french_door_fleur_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Chaberton Estate Winery Red Blend 750 mL | $23.98 | [North Vancouver:12, South Surrey:16, Langley Store:8, Vancouver:4] | https://www.everythingwine.ca/chaberton-cuvee-rouge | {sku=969790; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/9/6/969790_chaberton_red_blend.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Pentage Winery Hiatus Red Blend 750 mL | $31.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/pentage-haitus-red-blend-750-ml-1 | {sku=25200; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/5/25200_pentage_hiatus_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Intrigue Wines Social Red Blend 750 mL | $27.98 | https://www.everythingwine.ca/intrigue-wines-social-red-blend-750ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Chaberton Estate Winery Red Blend 4 L Box | $65.98 | [North Vancouver:3, South Surrey:8, Langley Store:4, Vancouver:4] | https://www.everythingwine.ca/chaberton-cuvee-rouge-4l | {sku=599332; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/9/599332_chaberton_red_blend_4l.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Vanessa Vineyard Right Bank Red Blend 750 mL | $61.98 | [North Vancouver:2, South Surrey:5, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/vanessa-vineyard-right-bank-red-blend-750-ml | {sku=52194; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/2/52194_vanessa-right-bank.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Narrative By Okanagan Crush Pad Red Blend 750 mL | $24.98 | [North Vancouver:0, South Surrey:0, Langley Store:13, Vancouver:18] | https://www.everythingwine.ca/narrative-red | {sku=771196; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/7/771196_narrative_red_blend.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Church & State Wines Lost Inhibitions Red Blend 250 mL | $7.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/church-state-wines-lost-inhibitions-red-blend-250-ml | {sku=467322; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/4/6/467322_lost_inhibitions_red_blend_250ml_1.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Crown & Thieves Scoundrels Punch Red Blend 750 mL | $34.98 | [North Vancouver:0, South Surrey:0, Langley Store:7, Vancouver:9] | https://www.everythingwine.ca/crown-thieves-scoundrels-punch-red-blend-750-ml | {sku=14919; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/4/14919_crownthieves_scoundrels_punch_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Calliope Wines Figure 8 Red Blend 750 mL | $26.99 | https://www.everythingwine.ca/calliope-figure-8-red | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/c/a/calliope_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Bordertown Estate Winery Living Desert Red Blend 750 mL | $27.98 | https://www.everythingwine.ca/bordertown-vineyards-estate-winery-ltd-desert-red-750-ml | {sku=165405; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/6/165405_bordertown-living-desert-red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Church & State Wines Lost Inhibitions - Lewd Edition Red Blend 750 mL | $24.98 | https://www.everythingwine.ca/church-state-wines-2014-lost-inhibitions-red-blend-750ml | {sku=553008; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/5/553008_church-and-state-lost-inhibitions-red-blend.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Maverick Estate Winery Renegade Red 750 mL | $25.99 | https://www.everythingwine.ca/maverick-estate-winery-renegade-red-750-ml | {sku=131605; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/3/131605_maverick_renegade_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - The Hatch Ross.O Red Blend 750 mL | $23.98 (reg $25.98) | https://www.everythingwine.ca/the-hatch-ross-o-wa-red-blend-750-ml | {sku=709764; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/0/709764_hatch_rosso_2.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Culmina Family Estate Winery R&D Red Blend 750 mL | $19.99 | https://www.everythingwine.ca/culmina-family-estate-winery-r-d-red-blend-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/c/u/culmina_r_d_nv.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Church & State Wines Meritage 750 mL | $34.98 | https://www.everythingwine.ca/church-state-wines-coyote-bowl-meritage-750-ml | {sku=278267; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/278267_church-and-state-meritage.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Mt Boucherie Estate Winery Similkameen Valley Blaufrankisch 750 mL | $30.98 | https://www.everythingwine.ca/mt-boucherie-blaufrankisch | {sku=64428; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/6/4/64428_mt_boucherie_blaufrankisch.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Moraine Estate Winery Cabernet Merlot 750 mL | $28.98 | https://www.everythingwine.ca/moraine-estate-winery-cabernet-merlot-750-ml | {sku=382794; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/8/382794_moraine_cabmerlot.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Beautiful BC Gift Basket Delivery Version | $128.97 | https://www.everythingwine.ca/beautiful-bc-gift-basket-delivery-version | {image_url=https://www.everythingwine.ca/media/catalog/product/b/e/beautiful-bc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366}
  - A Taste of BC Gift Basket Delivery Version | $115.99 | https://www.everythingwine.ca/a-taste-of-bc-gift-basket-delivery-version | {image_url=https://www.everythingwine.ca/media/catalog/product/a/-/a-taste-of-bc-main-image.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366}

#### search_okanagan_cellars_tool (status=ok, 0 results)

#### search_suttonplace_tool (status=ok, 15 results)
  - Averill Creek Joue Red | $29.49 | 2021 | stock=6 | https://store.suttonplacewinemerchant.com/products/4143614-averill-creek-joue-red | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000022/0000227954-5166.jpg; country=CANADA; varietal=Red Blend; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}
  - Averill Creek Pinot Noir  | $35.99 | 2021 | stock=5 | https://store.suttonplacewinemerchant.com/products/4144447-averill-creek-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000078/0000786657-5366.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.10; is_staff_pick=False; is_featured=False}
  - Bartier Bros Granite | $32.99 | 2021 | stock=12 | https://store.suttonplacewinemerchant.com/products/4944430-bartier-bros-granite | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000016/0000169496-1522.png; country=CANADA; varietal=Red Blend; alcohol_pct=14.50; is_staff_pick=False; is_featured=False}
  - Bench 1775 Cabernet Sauvignon Merlot | $31.49 | 2019 | stock=5 | https://store.suttonplacewinemerchant.com/products/4571291-bench-1775-cabernet-sauvignon-merlot | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000048/0000483529-1106.jpg; country=CANADA; varietal=Cabernet Sauvignon/Merlot; alcohol_pct=14.80; is_staff_pick=False; is_featured=False}
  - Bench 1775 Syrah | $32.99 | 2021 | stock=2 | https://store.suttonplacewinemerchant.com/products/4571295-bench-1775-syrah | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000044/0000441741-7370.jpg; country=CANADA; varietal=Syrah; alcohol_pct=14.00; is_staff_pick=False; is_featured=False}
  - Bench 1775 Viognier | $22.99 | stock=5 | https://store.suttonplacewinemerchant.com/products/5056699-bench-1775-viognier | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC425751.jpg; country=CANADA; varietal=Viognier; alcohol_pct=12.60; is_staff_pick=False; is_featured=False}
  - Birch Block Beau Soleil Pinot Noir | $50.49 | 2023 | stock=3 | https://store.suttonplacewinemerchant.com/products/5103142-birch-block-beau-soleil-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.10; is_staff_pick=False; is_featured=False}
  - Black Hills Estate Winery Nota Bene | $76.99 | 2022 | stock=38 | https://store.suttonplacewinemerchant.com/products/4144375-black-hills-estate-winery-nota-bene | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000070/0000708073-8356.jpg; country=CANADA; varietal=Bordeaux Blend; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Black Sage Vineyard Cabernet Franc | $38.49 | 2020 | stock=19 | https://store.suttonplacewinemerchant.com/products/4144211-black-sage-vineyard-cabernet-franc | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000059/0000593038-3276.jpg; country=CANADA; varietal=Cabernet Franc; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Black Sage Vineyard Cabernet Sauvignon  | $38.49 | 2020 | stock=15 | https://store.suttonplacewinemerchant.com/products/4144212-black-sage-vineyard-cabernet-sauvignon | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000059/0000593095-6502.jpg; country=CANADA; varietal=Cabernet Sauvignon; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Blue Mountain Gamay | $33.99 | 2020 | stock=4 | https://store.suttonplacewinemerchant.com/products/4228470-blue-mountain-gamay | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000038/0000389882-3198.png; country=CANADA; varietal=Gamay Noir; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}
  - Bonamici Cellars Belviaggio | $51.99 | 2020 | stock=7 | https://store.suttonplacewinemerchant.com/products/4144339-bonamici-cellars-belviaggio | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000067/0000673954-1986.jpg; country=CANADA; varietal=Red Blend; alcohol_pct=14.50; is_staff_pick=False; is_featured=False}
  - Bonamici Cellars Merlot - Cabernet Franc | $32.99 | 2021 | stock=7 | https://store.suttonplacewinemerchant.com/products/4143755-bonamici-cellars-merlot-cabernet-franc | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000032/0000326249-3594.png; country=CANADA; varietal=Red Blend; alcohol_pct=14.90; is_staff_pick=False; is_featured=False}
  - Clos Du Soleil Célestiale | $34.99 | 2019 | stock=41 | https://store.suttonplacewinemerchant.com/products/4205421-clos-du-soleil-celestiale | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000002/0000021249-3380.jpg; country=CANADA; varietal=Red Blend; alcohol_pct=14.20; is_staff_pick=False; is_featured=False}
  - Clos du Soleil Signature 2021 | $62.49 | 2021 | stock=12 | https://store.suttonplacewinemerchant.com/products/5140824-clos-du-soleil-signature-2021 | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC298158.jpg; country=CANADA; varietal=Bordeaux Blend; alcohol_pct=13.40; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 20 results)
  - Cassini 2023 Pinot Noir "Red Carpet" 750ml | $29.99 | stock=24 | https://www.marquis-wines.com/cassini-2022-pinot-noir-red-carpet-750ml/ | {sku=1014905; in_stock=True; categories=["Celebrate BC Wine Month", "Drink Local", "Red Wine", "Pinot Noir", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8886/images/6958/cassini-2016-pinot-noir-red__12126.1732902163.500.500.jpg?c=2}
  - Sunrock 2020 Red Meritage 750ml | $35.99 | stock=5 | https://www.marquis-wines.com/sunrock-2016-red-meritage-750ml/ | {sku=1010560; in_stock=True; categories=["Red Wine", "Red Blends", "Merlot", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/10684/images/10027/2021-03-11-17.21.05__93677.1615850902.500.500.png?c=2}
  - Esquimalt Bitter Red Americano 500ml | $33.99 | stock=1 | https://www.marquis-wines.com/esquimalt-bitter-red-americano-500ml/ | {sku=1031661; in_stock=True; categories=["Spirits", "Liqueurs", "Distilled in BC"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20972/images/16785/2025-11-12_12.19.55__58307.1763069208.500.500.png?c=2}
  - Three Sisters Bench Red 750ml | $25.99 | stock=4 | https://www.marquis-wines.com/three-sisters-bench-red-750ml/ | {sku=1021001; in_stock=True; categories=["Red Wine", "Red Blends", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18920/images/14931/2024-07-26_11.42.18__97445.1722292995.500.500.png?c=2}
  - Hester Creek 2022 The Judge Red Blend 750ml | $59.99 | stock=10 | https://www.marquis-wines.com/hester-creek-2020-the-judge-red-blend-750ml/ | {sku=1020782; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18498/images/14441/2024-02-27_12.22.40__84615.1709148372.500.500.png?c=2}
  - Black Hills 2022 Nota Bene 750ml | $72.99 | stock=21 | https://www.marquis-wines.com/black-hills-2022-nota-bene-750ml/ | {sku=708073; in_stock=True; categories=["Celebrate BC Wine Month", "Drink Local", "Red Wine", "Red Blends", "British Columbia", "Okanagan Falls"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7944/images/9204/2020-10-01-15.42.34__26769.1780440169.500.500.jpg?c=2}
  - Nichol 2022 Cabernet Franc 'The Village' 750ml | $32.99 | stock=4 | https://www.marquis-wines.com/nichol-2022-cabernet-franc-the-village-750ml/ | {sku=1030412; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Cabernet Franc", "Celebrate BC Wine Month"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19423/images/15276/2024-10-29-11.34.44__90023.1730308360.500.500.png?c=2}
  - Quails Gate 2022 Old Vines Foch 750ml | $31.99 | stock=2 | https://www.marquis-wines.com/quails-gate-2019-old-vines-foch-750ml/ | {sku=639625; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8458/images/10815/IMG_41941__18319.1631131104.500.500.png?c=2}
  - Burrowing Owl 2022 Cabernet Franc 750ml | $42.99 | stock=19 | https://www.marquis-wines.com/burrowing-owl-2022-cabernet-franc-750ml/ | {sku=556621; in_stock=True; categories=["Red Wine", "Cabernet Franc", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20920/images/16669/burrowing_owl_franc__20214.1760725789.500.500.jpg?c=2}
  - Lock & Worth 2023 Merlot 750ml | $27.99 | stock=9 | https://www.marquis-wines.com/lock-worth-2022-merlot-750ml/ | {sku=1019960; in_stock=True; categories=["Red Wine", "Merlot", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9932/images/8452/29229_Lock_Worth_Merlot__53926.1698439471.500.500.jpg?c=2}
  - Meyer Family 2023 Pinot Noir 750ml | $34.99 | stock=12 | https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/ | {sku=1014474; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7708/images/8652/Lindsey_Ail_-_IMG_15661__44130.1589559651.500.500.jpg?c=2}
  - Tinhorn Creek 2023 Cabernet Franc 750ml | $27.99 | stock=47 | https://www.marquis-wines.com/tinhorn-creek-2023-cabernet-franc-750ml/ | {sku=530717; in_stock=True; categories=["Red Wine", "Red Blends", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9723/images/5511/2014-tinhorn-creek-cab-franc-vqa__10878.1779383184.500.500.jpg?c=2}
  - Burrowing Owl 2011 Cabernet Sauvignon 750ml | $134.99 | stock=16 | https://www.marquis-wines.com/burrowing-owl-2011-cabernet-sauvignon-750ml/ | {sku=508200; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20712/images/16485/burrowing_owl_cabernet_sauvignon__56618.1755199208.500.500.jpg?c=2}
  - Mission Hill Five Vineyards Cabernet/Merlot 750ml | $20.99 | stock=68 | https://www.marquis-wines.com/mission-hill-2018-five-vineyards-cabernet-merlot-750ml/ | {sku=257816; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Red Blends", "Merlot", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/6097/images/5467/five-vienyards-mission-hill-2014-cab-merlot__34443.1504217533.500.500.jpg?c=2}
  - Gray Monk 2021/24 Pinot Noir 750ml | $24.99 | stock=18 | https://www.marquis-wines.com/gray-monk-2019-pinot-noir-750ml/ | {sku=251835; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/15726/images/11434/2022-01-20-17.34.22__23087.1642793746.500.500.png?c=2}
  - Pamplemousse Jus 2025 Foch Nouveau 750ml | $34.99 | stock=8 | https://www.marquis-wines.com/pamplemousse-jus-2025-foch-nouveau-750ml/ | {sku=1032320; in_stock=True; categories=["Red Wine", "Organic / Biodynamic Wine", "Canada", "British Columbia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21828/images/17539/2026-05-28-12.34.21__76443.1780090872.500.500.png?c=2}
  - Vasanti 2022 Cabernet Sauvignon 750ml | $31.99 | stock=10 | https://www.marquis-wines.com/vasanti-2022-cabernet-sauvignon-750ml/ | {sku=1032200; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21813/images/17502/2026-05-15-12.10.25__01232.1779221223.500.500.png?c=2}
  - Domaine Artema 2022 Black Sage Road Rouge 750ml | $24.49 | stock=14 | https://www.marquis-wines.com/domaine-artema-2022-black-sage-road-rouge-750ml/ | {sku=1032199; in_stock=True; categories=["Red Wine", "Syrah & Shiraz", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21816/images/17501/2026-05-15-12.09.58__73486.1779221076.500.500.png?c=2}
  - Moon Curser 2022 Cabernet Sauvignon 750ml | $54.99 | stock=10 | https://www.marquis-wines.com/moon-curser-2022-cabernet-sauvignon-750ml/ | {sku=1032177; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21684/images/17401/2026-04-16-14.28.04__73861.1776448816.500.500.png?c=2}
  - Spearhead 2024 Dual Citizen Pinot Noir 777 750ml | $46.99 | stock=5 | https://www.marquis-wines.com/spearhead-2024-dual-citizen-pinot-noir-777-750ml/ | {sku=1032034; in_stock=True; categories=["Red Wine", "Pinot Noir", "Canada", "British Columbia"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21522/images/17200/IMG_0692__32204.1773167006.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 0 results)


### sommelier_agent_tool (status=ok)
**Sub-agent synthesis:**
Here are some excellent British Columbia sparkling wines that typically fall into the accessible, value-driven tier you are looking for (under $35). I have also included some fantastic local sparkling alternatives across beer, spirits, and sake to round out your options. 

*(Note: I focus on the tasting notes, pairings, and producer details. The Sourcing specialist will follow up with exact real-time pricing and availability).*

### **BC Sparkling Wine Recommendations**

**1. Blue Mountain Vineyard and Cellars Gold Label Brut (Okanagan Falls)**
*   **Style & Notes:** Widely considered a benchmark for Canadian traditional-method sparkling wine. It offers a complex, Champagne-like profile with a strong toasty, brioche character from extended lees aging, balanced by bright crystalline lemon, green apple, and a saline finish.
*   **Reviews & Scores:** Geoffrey Moss MW (*Gismondi on Wine*) awarded the 2019-based bottling **90/100**, calling it a benchmark that overdelivers for its price point, highlighting its generous brioche and yellow apple notes [Gismondi on Wine](https://gismondionwine.com/wine/blue-mountain-gold-label-brut-nv-2/). John Szabo MS (*WineAlign*) scored the 2019 vintage **92/100**, praising it as a "terrific value" with a strong toasty-autolysis character [WineAlign via Wine-Searcher](https://www.wine-searcher.com/find/blue+mountain+gold+label+brut+okanagan+valley+canada/1/canada). Natalie MacLean rated it **93/100**, noting its persistent mousse and vibrant zestiness [Natalie MacLean](https://www.nataliemaclean.com/wine-reviews/blue-mountain-vineyard-and-cellars-brut/285511).
*   **Food Pairing:** Classic with fresh oysters on the half shell, truffle fries, or crispy fried chicken.

**2. Unsworth Vineyards Charme de L'île White (Vancouver Island)**
*   **Style & Notes:** "Charme de L'île" is a trademarked style of Vancouver Island sparkling wine made using the Charmat method (similar to Prosecco). Crafted from 100% island-grown grapes (Sauvignette, Pinot Gris, and Pinot Noir), it is crisp, lean, and lightly effervescent with inviting aromas of fresh-cut apple, pear skin, and subtle lees.
*   **Reviews & Scores:** Anthony Gismondi (*Vancouver Sun* / *Gismondi on Wine*) scored it **89/100**, praising its impressively small bubbles and highly food-friendly, crisp profile [Vancouver Sun](https://vancouversun.com/life/food/local-food-reviews/anthony-gismondi-b-c-wine-of-the-week-and-wines-to-add-to-your-cellar-43). Natalie MacLean awarded it **90/100**, noting its golden apple aromas and toasty edges [Natalie MacLean](https://www.nataliemaclean.com/wine-reviews/unsworth-vineyards-charme-de-lile/290076).
*   **Food Pairing:** Excellent as an aperitif or paired with local BC spot prawns, crab cakes, or a mild goat cheese tart.

**3. Fitzpatrick Family Vineyards Fitz Crémant (Peachland)**
*   **Style & Notes:** A 100% estate-grown Pinot Blanc traditional-method sparkler from Greata Ranch. It is highly approachable and creamy, featuring gentle bubbles, fresh-baked bread, almonds, and crisp orchard fruit.
*   **Reviews & Scores:** *Gismondi on Wine* awarded both the 2016 and 2021 vintages **88/100**, noting the 2021's use of 1996-planted estate fruit and its clean, well-crafted character [Gismondi on Wine](https://gismondionwine.com/wine/fitzpatrick-fitz-cremant-2021/). Shelley Boettcher (*Castanet*) praised the 2019 vintage for its refreshing minerality and Alsace-inspired profile [Castanet](https://www.castanet.net/news/Wine/393166/Fitz-Cremant-2019).
*   **Food Pairing:** Pairs beautifully with seafood salads, quiche lorraine, or a creamy baked brie.

**4. Haywire "The Bub" (Summerland)**
*   **Style & Notes:** Produced by Okanagan Crush Pad, this is a traditional-method, zero-dosage (bone dry) sparkling wine made from Pinot Noir and Chardonnay. It is racy and energetic with notes of lemon pith, green apple, and a chalky minerality.
*   **Reviews & Scores:** Treve Ring (*Gismondi on Wine*) gave the 2018 vintage **90/100**, describing it as a serious, crisp zero-dosage bubble with lively lemon pith and broken stone notes [Gismondi on Wine](https://gismondionwine.com/wine/haywire-the-bub-2018/). Deborah Podurgiel (*Natalie MacLean*) rated the 2017 vintage **93/100**, calling it an elegant, bone-dry sparkler with a long, zesty finish [Natalie MacLean](https://www.nataliemaclean.com/wine-reviews/haywire-the-bub-sparkling-2017/295130).
*   **Food Pairing:** The bone-dry acidity cuts perfectly through rich, fatty, or salty foods like tempura, sushi, or potato chips.

---

### **Beyond Wine: BC Sparkling Alternatives**
To ensure you have options across all beverage categories for a sparkling-themed occasion, here are some fantastic local alternatives:

*   **Beer (Champagne-Style):** Look to Vancouver's **Strange Fellows Brewing** or **33 Acres Brewing Company**, both of which have experimented with Champagne-style Brut IPAs and highly effervescent sours. Strange Fellows' *Illustrum Brut IPA* (barrel-aged with wild yeast) offers a highly effervescent, dry, "Chablis-like" character with notes of pear and white grape [Strange Fellows](https://strangefellowsbrewing.com/beer/illustrum/). It is a brilliant pairing for soft cheeses or charcuterie.
*   **Spirit / Cocktail (The BC French 75):** Build a local twist on the classic French 75. Combine 1.5 oz of **Sheringham Seaside Gin** (distilled on Vancouver Island with local winged kelp for a subtle maritime salinity) with 0.5 oz fresh lemon juice and 0.5 oz simple syrup. Shake, strain into a flute, and top with the **Unsworth Charme de L'île** recommended above. This makes for a bright, botanical, and refreshing celebratory cocktail.
*   **Sake (Sparkling):** **Artisan Sake Maker (Osake) Junmai Sparkling Sake**. Handcrafted on Granville Island, this is a light, crisp, and semi-sweet sparkling sake with bright notes of apple, melon, and citrus. *Vancouver Magazine* highly recommended it as a unique local pour [VanMag](https://www.vanmag.com/taste/wine-and-drinks/international-wine-competition-2019-other-wines/), and it pairs exceptionally well with local oysters or spicy tuna rolls.

#### search_web_grounded_tool (status=ok, 7 results)
Search answer: The **Blue Mountain Vineyard and Cellars Gold Label Brut** (Okanagan Falls, BC) is widely regarded as one of British Columbia's benchmark traditional-method sparkling wines. 

Review scores and tasting summaries from prominent Canadian wine critics and publications include:

*   **Geoffrey Moss MW (*Gismondi on Wine*) – 90/100:** Reviewing the 2019-based bottling, Moss called it a benchmark for Canadian sparkling wine that outperforms its price point. He noted its complexity, highlighting flavors of crystalline lemon, yellow apple, red berries, and generous brioche.
*   **John Szabo, MS (*WineAlign*) – 92/100:** Tasted in November 2023, Szabo praised the 2019 vintage as a "terrific value" that easily rivals Champagnes at twice the price. He described it as having a strong toasty-autolysis character alongside bright citrus and green apple flavors.
*   **Treve Ring (*Gismondi on Wine*) – 91/100:** Reviewing the 2018 vintage, Ring noted it was the first year Pinot Gris was omitted from the blend (leaving 62% Pinot Noir and 38% Chardonnay). She described it as a serious yet highly drinkable sparkler with notes of green apple, subtle brioche, and a driving, saline-slicked palate.
*   **Anthony Gismondi (*Gismondi on Wine*) – 90/100:** Gismondi awarded the non-vintage (NV) bottling 90 points, praising its high drinkability, pure citrus and toast notes, and fresh, mineral-driven finish. 
*   **Natalie MacLean – 93/100:** MacLean rated the sparkling wine 93 points in January 2021, describing it as a crisp, refreshing, and zesty bubbly with vibrant green apple notes and a persistent mousse that challenges non-vintage Champagnes.
  - [scoutmagazine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFX2eAU9KGtNqpwxqPwUiPI0wuKKE6XmOtKr3zKwsVlt9BZlbRTESHTZYj8jN8O7BEjVQQSJRsUlKkwGIWDWCHlqLH5F5HpRxwwFRE7hw9K4qs2Vc-D6YxMHRDr6kQdKfxmkZ4VyKNLPKfnY_VOxyVUtCAE2CEXxGtE4SnC9pLuNlxVhR52BhSV0miCQjJyiTIxyArYQH7WOJP7I3HbHA4jo6ui): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgkeiEAUtadJ5RzBD46EAonWs6dE5BHEE2HCn5rlPUD3f9sWDF5WLtaj24qD8qHI3pdJN-f9fen6ZcIQ0pAh9aI77-Z-zmp_u5myifuJLr81hGUkeqPP9_6WtziNDjKnUdlnKxg5I5yrNZ9rKVs1t0nRNQxc3P4DGeBM2PWGq5YhdCYkZHBpbtBd3Mu6fVzz7V5wZlqQ0SOQ==): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaIho4BIDR-Pg13e5aK_4fu9B7uLEgXaGxVd_T1i15CEaBL21lOpc7bf7Cy0_viQBmuCKSsTOSJOe0wAug82ec7Ym0RoQqlqWH7Q8JpbpiKTzO5rHMMSSvvYXTMChWu1cY4EJTIHaV-HMr5CrkerzyZ5NEPXJ6Zob1Zgn4Znw9UaQOfjHG4aWMvSacKCHdXZ0O-FE=): 
  - [rogcowines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuY2RBC9YfKexAppM9BmYu_tBeiMzlgFcKzP-QWmvobjI8ntXTrBlVNVLJnNhBn_i5uQBejHw8G4skMm881ADaIJGl0ervnlhQL4p5wR7hfTARKhv5JGeT1NN7N7-xELs2NwIsua6d6kZv0JRyelFh27837VawNas=): 
  - [marquis-wines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsVNwhMDChUx89kfRwTiofAp_GPxI-RbB4KE7BEQAwOZCR4jdn6R86WWJ3tez_kZ5HnsI1dns126YfPiflgNh7sh7uhdKUQorEXWjyiVXpfNrFs5UEHcqKB1NNkUYOCxuJvnlvBoW3T5QIqXCOY3pQsWnmjgrg4w_n7ML46Us5pg==): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBJ8dShR0_uPzNyXOqNt93WBvzGcIu-oadk67WKHFbelMWQOym2m4YCYGPFmRtcdqf8QgMO2bSrjRL-Ix4D461tSc3sgs6U4qVPVv-HDUEWsMke992ayhu0R8faG-nbWPHinwpOCvLJQfJoVXfWVSLzeGVU3grDAUtcxUBO3O9WAsN3cXPugU=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDEy6qaXr2yw3X0-ZZ0Hu5XMBSMgawidMsIvwDXhQaKIb2jrmKCPzHdNTiOzp1QjP9sSK_D6lDHWxEXQCl4LKCGSMDV9x0sVdc7jXftBl9tXvmiapkqcMgSjaJcpuT0uZHO-J3KpV8707914zpEeFIrbKaFzHQGpltJkFQh1bz5F_jcoJvtr4We5cTzrxyVj8RROIA2FXskOQ=): 

#### search_web_grounded_tool (status=ok, 7 results)
Search answer: **Charme de L’île** is a trademarked style of sparkling wine native to Vancouver Island and the Gulf Islands, crafted using the Charmat method with 100% island-grown grapes. Unsworth Vineyards produces both a white and a rosé version of this signature bubble. 

Review scores and tasting summaries from prominent British Columbia and Canadian wine critics include:

### **Unsworth Charme de L’île (White)**
* **Gismondi on Wine / Vancouver Sun (Anthony Gismondi): 89/100** (Reviewed April/May 2026)
  Gismondi highlights this lightly effervescent sparkling wine for its impressively small bubbles. He notes that the blend has evolved to lead with Sauvignette, followed by Pinot Gris and a touch of Pinot Noir. Describing the latest version as crisper, leaner, and highly food-friendly, he points out inviting aromas of lees, fresh-cut apple, and pear skin.
* **Natalie MacLean: 90/100**
  MacLean rates it as a crisp and toasty BC sparkling wine. She notes aromas of golden apple and toast, recommending it as an excellent pairing for shellfish or to enjoy as an aperitif. 

### **Unsworth Charme de L’île Rosé**
* **Gismondi on Wine (Geoffrey Moss MW): 89/100**
  Moss describes this Pinot Noir-based bubble as a solid, aperitif-style Charmat rosé. He notes a soft but generous mousse and a balanced, chalky finish, with a flavor profile defined by green strawberries, red apple, rhubarb, cream, and subtle lees.
* **Gismondi on Wine (Anthony Gismondi)**
  Gismondi notes that this pale orange-pink rosé offers a weightier mouthfeel than many of its white competitors. He describes it as an easy-drinking bubble featuring a mix of cranberry, rhubarb, and a touch of earth.
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMpv4gbF5JQ--OP9F7w-Bks_IwL3ecSyd1x1vgOh3lt6k2lEny4WMDDGHTXezwkp2nOGQB8zd2EE68f6MYmXXZIBh4viovD1RlY0HNp0DsH5sVlKaNdQoM3nmSuzFhYeoekW47qDKzy_RtuQ7PypFYJpSSkff_oxBi_Ptd_3UZeMAKQIRrBT2teedL1cN1-r7ni1wg1YjtjZkVd40aRifmmZUsquEnjKlAh8kG6xy8): 
  - [ediblecommunities.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpMjuYl_NooPBX-GxdkHUzmDqPBfIBXph4Ubs52A6B3Klq29CBW_v4dufTaNcOxDqLoHFa5QCcPd1nt2CHismvCoZdgmq4-tcKZZJd4qzfHBhJcVk4qT9CPwKwGG_bWB77PZBEQuQaodTsze_f7WwzxXvgRfe9s9PzOd4yQItwLM6mbWr6mtO5Uy0=): 
  - [unsworthvineyards.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZeha9f7KdMcCVRU1UistZM2zCI0iGEaC6Nh3PvGLWCmTVAxZOgxNHQt5arfWrpxUVOicXu8_ioVrRcRv75kN0Rt-CU6NJxMEZPoaa2v07KqelaXZnlARL2SQryyzSc5uBCyzr378-c1_elw==): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIrCL3WJIBf9nnoSPuAqz_jaE3wc03ME4IF7_2lvdSCHn9vaOnW4fLwxtS5wfrfhwQT8clRQB5Y_TL7kNlBHgeLpO_1_4RBAL2lhmb_L-tM4P65g1gsRtFkcCSy0WBkGJSDxQY7I2pYZjLbA==): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnCfyFOZi-dp5TURD1iKI9ED3_p-2BPZiXRLZbdJCUYt-SHrciGbitvvxsLxX2NSxNNBGVo5chFnSSJRknlHo2yqF-GWA21FoQ7jvmmKIKiLoSOZwVkmPulChkNP7_jURESMCgboSCZkbpxWTf-t_duC12B8kxDZFVbeyMtxrAK1g=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmXCTv2Nw9tXfkB-Cl63-jDeRsqJFd5z5Li1-_MuUjxlJl3pQ46zn9Yl2HVwlz_Cpcqf1jQ54dNQhMaFnYxELLc0asW-Oo6KBVuKUIiD_9SDIwfozCjccFITy3EY37iHCi3SFD1zmi_6K2id1QlMU2Xy-EBngh0-vzQ_rlfxd9_RJNzLoZmKWEbLI0WmMwFw==): 
  - [bswliquor.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4ph8L0QzrcfLa79N46VJeUGlH7s_oMZFEfvKwNKvDc1_5w_9zknXJH3PQAM543ApQKJbLz5JGlEKcobqb72FM0iMRLBEtM6-YDY3TPYrHChCrT9pKIBhIKt78bQXx6LZ6h3oOMUiQuAnUr-kZP5NGNfp3xE=): 

#### search_web_grounded_tool (status=ok, 9 results)
Search answer: The **Fitz Crémant** from Fitzpatrick Family Vineyards (located at Greata Ranch in Peachland, BC) is a traditional-method sparkling wine crafted from 100% estate-grown Pinot Blanc. 

Review scores and summaries from prominent BC and Canadian wine critics include:

* **Gismondi on Wine:** 
  * **2021 Vintage – 88/100:** Tasted in September 2022, this vintage was noted for utilizing estate fruit planted in 1996, with a portion of the grapes receiving brief skin contact to add character.
  * **2016 Vintage – 88/100:** Reviewed as a clean, approachable, and well-crafted addition to the winery's sparkling lineup.
* **Daenna van Mulligen (WineDiva):** 
  * **2019 Vintage:** Described the wine as a "soft and yummy" sparkling option.
* **Shelley Boettcher (Castanet):** 
  * **2019 Vintage:** Praised this Alsace-inspired Pinot Blanc sparkler for its aromas of fresh-baked bread, almonds, and green apple, noting its gentle bubbles and refreshing minerality.
* **Jessica Payette (Crush Food + Wine):** 
  * **2018 Vintage:** Described the wine as dry and fruit-forward, highlighting a creamy mousse with notes of apricot, pear, golden apple, and toasted biscuit.
* **Yvonne Turgeon (Trends Magazine):** 
  * **2020 Vintage:** Highlighted the wine's softer, creamier bubbles—achieved through nine months of bottle aging on the lees—and its delicate peach and pear aromatics.
* **Vivino Community:** 
  * The wine holds an average rating of **3.9 out of 5 stars** across more than 130 user reviews, with members frequently praising its crisp orchard fruit and approachable, creamy texture.
  - [castanet.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuxNPml38M8O9-u-_6drxtX-sBf7NN57BMVW7cJpkZlexWeU8HJ46EMAny9PNr9VR15AUpCzub3OLbOtQVMLRV6zvspSyXPYzXVcVzJsL6u63QLbs7F1EolqQ4J6g70qlciuY9AoJRRouJjG518FRmNuKm2qPsV-6BZl7COh1XyGHWbuy7j892p858lBxHIfP6Y1sx2jxwNjAWyA==): 
  - [marquis-wines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtRPIO25rfMnsER1sJV2mGdIlSwRF3rfe9-1l7L0EBh9FemRZyr8dOG1lDdw_twJt5RXJgxoLvvEfw7SA0kSa9P5FQzzog-1oWpiPN5HtLz_efb73oYVPNjg6kMeRceuZ5Y2KzbvKfgfOdTmmfXZYOu_-uasRmMWPL9UFloP-x): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECIYZy1BRNIKDEsX-Nx7lW19AJrauzRDfQz2SPIKpe3lOrWOkcPOKPVqQHWU1h220hmuO3SCyEGQMw8zGIJnh1w0ehaGm3trbXI1yPRneguWywPfDCJzoMhuvvPzg7zIv-fxLotzou4NgIEly9QIgu53x0hMGc0gfEOzUYkUSxuaNEmUJR5JxjacMO7x7z7l_t7isLt-gr): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkDwbVkJjI0zNDg235pJknyHXJuqio-u9MU1roB_27YzrvQQoydOocVczp210EbvVdf_BempdaLyY4dzsT1Q_uIcJq6i7BI3VqeL15JtO9ujVqfYTTAc3AnGsjI_sH7seL20dgBFXj4Ex_Bg==): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgkn91QvWAAe8Qdm_ywGqULwRqP906ugqcicntxMCXQM6C2o9AGUW9I9sTwqDou2Jp4VU5L8smq8BYKC8lTIpm6al0siLpOFoqxPVf0yu0vAJr5ZD-7srMopCogvQupDN_BxiJXJ48VOQpOg==): 
  - [mulliganstew.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjWzsDXzrao16SKEhKC4uwRZIf-iefiKDmE6NI_etRVSCDOPuIB-NUhWDBaRdHn_fQBNNznngTdiftm_yzv6kbVKFVpQgXNcOJbnmj1q5CfX05YWUsfOWwQ2FAYj9PVthXnIu0VMDsMh7DpaXGR-ePVwuhAhBWCVcDSSnn0Iywfgs=): 
  - [crushfoodandwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERvOgOqhU-enNesa5Lyx1KZfHGfhSdjEfY5pLNXyV_SRJj-SH_ToVslpI9QBBpy-S21ZKHYeiKktAJU4sNYbWMpYN57gcnG6etQj3XQgK1ms5tnGwDjYiZoZx-YFK1LNWY012Wq50h4CkbtBCKqlrxk_vyAtYc_K33NHlv): 
  - [trendsmag.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMip1S-l59GHtkGnnM3ZU0oFT9IigIdc3cwB8Pcf9TUk-pJKmETlTmXzuke496iUyL8rh3FJ8yPxvHhDoG2KIBBK9HIkpSu1Wr5BAiWzlu20qrYpCOvuMVMztifB-JguFWbiQwoa5ySooYaPVo6A==): 
  - [vivino.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKBGib7wQko6EPWh8vOjjLT8dkB_5jzP3HzQuqvkVpRRhbJiqITibwdubmxyu-2sFOMFKO4tTn7GpCQmc-P1GhVLMaWPS7k3SZxsUggpZ-_Wj9IJtJ8i3LAkUk171SJO6NWfw2V112MFv5EUQ2inAnFoZ-HBeqx-9fFy0FfCUFJRJKXmrjM_jM): 

#### search_web_grounded_tool (status=ok, 7 results)
Search answer: **Haywire "The Bub"** is a traditional-method, zero-dosage sparkling wine produced by Okanagan Crush Pad in Summerland, British Columbia. Typically crafted from a blend of Pinot Noir and Chardonnay, the wine is named after co-founder Steve Lornie and Christine Coletta's daughter, Alison Scholefield, whose childhood nickname was "The Bub". 

Review scores and tasting summaries from prominent British Columbia and Canadian wine critics include:

### **2018 Vintage**
* **Treve Ring (*Gismondi on Wine*) – 90 Points:** Ring described this vintage (a blend of 64% Chardonnay and 36% Pinot Noir aged 30 months on the lees) as a racy, crisp, and serious zero-dosage sparkling wine. She noted lively characteristics of lemon pith, broken stones, pear skin, and dried sage.
* **Geoffrey Moss MW (*Gismondi on Wine*):** Moss praised the wine's precise, bright lemon, green apple, and chalky profile. He highlighted its crisp yet balanced acidity and subtle toasty notes from its extended time on the lees.

### **2017 Vintage**
* **Deborah Podurgiel (*Natalie MacLean*) – 93 Points:** Podurgiel rated this vintage highly, calling it an elegant, bone-dry, and frothy sparkler. She noted soft citrus, apple, and toasty notes on a lively, fine perlage with a long, zesty finish.
* **Carl Boucher (*Carl's Wine Club*) – 91 Points:** Boucher highlighted the wine's zippy, energetic delivery and zero-dosage style. He noted aromas of citrus, hazelnut, and white flowers, followed by a palate of key lime, green apple, and a chalky finish.

### **2016 Vintage**
* **Deborah Podurgiel (*Natalie MacLean*) – 93 Points:** Podurgiel described this bottling as a lively, bone-dry, and textured sparkler. She noted a persistent mousse with flavors of toasted white bread, bright apple crunch, and zesty lemon.

### **2014 Vintage**
* **Daenna Van Mulligen (*Wine Diva*):** Van Mulligen noted that the wine had evolved from "sassy" to complex and sophisticated. She described aromas of warm apple turnovers, dried pears, roasted hazelnuts, and a hint of smoke, leading to a tangy, creamy palate with a long lemony finish.

### **2011 Vintage**
* **Treve Ring (*Gismondi on Wine*) – 88 Points:** Ring noted a foamy pour with aromas of apple, stone, and pear skin, alongside tart white peach and crisp lemon on the palate.
* **Anthony Gismondi & Stuart Tobe (*Gismondi on Wine*) – 86 Points:** The tasting team described it as a fresh, crisp, and somewhat sweet-edged sparkler with a foamy mousse, featuring toasty, buttery, baked apple, and lemon rind flavors.
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzlsrIgEWHdpTNIW2NEPiy2vMwrpJsLmr3uCzTiLcNCYZOcIT61_UIHETrylpyHIL13F7aV3RtEavN4emshn4xgwMnLmiKCRB3kmc7AtM5BCP3os3fBIvqaqEFVwcHplKcv9cUpqogIwza5EzFdgRdolBH1FiVbL5B2ySPDTU5R0Ix1H6WA5S39NwxMCuU5E9CioENgJtUWPioPO8hNOQc3glE_xOJESzM): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBm_Q9UbPlzgg0aOl7mkHPwmW3dH2ot07vYE9fDXeH73-2KpT2rRvRgIWITIA56pCg5Mzt6Bb-rvyzcfH9M7rW85L-YRsb_JEIlZTuOy0pMva-wfNwGUketreEihDGNfXNZxFVaEaLqezRBkqsAnL5LqT9xeoVFuLFIcqfUUXEkl-pZp8Y3Y3M-7QhmMU3I99sfJ3yuaPqRhwJlpGaAUP0SzrO): 
  - [okanagancrushpad.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8kXNXHLp9oOhK0Ss_e_0jEeV1sBZQOIyEseOUpI1Nd7GXp4_rGg43b0PbaOG6nZ_yeeV-sQQ6fLrN1CIIyseyYpFYwC4oVLi7aTqptA30nGorI3f1woG7BL8LLB7vtIa62KJ5RpGiSz2BrgeIBUiQTVVucg==): 
  - [carlswineclub.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhpJU2HtXtezBRQuY2T3A_jOMlErc1EnVv4x3hQtmzOM1H59b141Gstt-9jy96P36i5CKltREHaMedpLG97jre4p6E-25I390-gXS9psVfo-bw2E_PtCHiv3wKWc52k0UneqL7WgBRzMCDPR7RYrUOraCH4p1T3Q==): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6LRApRk6pSx3zRdJwfQ9UDvyg1_U5r-8EAS4QkfnRvynEmc10wNNw2YQTbNw8nBra2uIlEUtVL2X9cl33cxWNTF0DnMygHcXdWwCWhZ7Sg4idxcNN56LDeNtutuGdXDmhVnjuPHHCp9di9ii9-20qasnCptkKZUv6nkJdK6rBWUonFWgqW1xC02y0UUUKv9zZG3ndMJod_sMsXUiSpRlrt1nY): 
  - [winediva.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq4iXbRbR8aYkK8qLR9G1IQwVGRpnvIt9CEvB2k3-ic2GcS2YousbzIbyWeZazWJTARgC_cKZkAUQPH-gRt6yUKySS88A09UH2cff_eHuvshXHf8X0DuKZluL8SUjGB5QoikxFGdc82drFNu33H25TEX79radBBtm04rw4_9mVIXqKPCenJnoxhMjq0oACr8qAA2Oy0FtjJ6zLLkNSmQCpsg3G8Oe9px_I3YVwQ_CKFGc57ArETSyAjDxGpDLZbr22olEKTdGAwHGk0bGzE0LQLnkGZwztFNq-E0rzRN6qtiwGZareDfXKiXlIyRE_hIs5-oHP_vVHoPY=): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCpDgBQ1elLYaKyGb73W_qSFeSK0Crgj77jUUQcMi673M2fjgA2iIdZB3TtXRWcwA1upHIfH-5wcdNgt6vIxDH-hJK_8MdORxxBES3gVW-Xkp3fQh2hvc11yavB87o7N9FE7Cte8CIBn7uUt_0M9244x--dfYQtX8Pszi9VH5G54UcFdaow6Q7C7gIBx7kEZWwn1hVG8e8mAS-ZPL5GPZwY5hg59qLPbgYSM1nYWvlGDAubHIZafU=): 

#### search_web_grounded_tool (status=ok, 9 results)
Search answer: **Artisan Sake Maker**, located in Railspur Alley on Granville Island in Vancouver, BC, was founded in 2007 by master sake maker Masa Shiroki. Operating as Canada's first boutique sake winery, they produce small-batch, unpasteurized (*nama*) sakes under the **OSAKE** brand. 

Among their lineup, they produce three distinct sparkling sakes, which have received highly positive reviews from local BC critics, publications, and restaurants:

### 1. Osake Junmai Sparkling Sake
This is their signature, light-style sparkling sake. The winery describes it as a light, crisp, and semi-sweet sake featuring bright notes of apple, pear, melon, and citrus with a delicate finish.
* **Vancouver Magazine:** In its International Wine Competition coverage, the magazine highlighted this bottle as a unique, "unusual sparkling sake" from "local hero Masa Shiroki" and highly recommended pairing it with local shellfish.
* **Henry Yuen (BC Wine & Food Writer):** Reviewed the sake as "crisp and light" with a "seductive sweetness," calling it a beautiful sparkling option to kick off any gathering.
* **The Keefer Bar (Vancouver):** Bartender Lucas praised the sake's palate-cleansing effervescence, noting that it leaves pleasant, lingering flavors of pear and nougat.
* **Historical Milestone:** The sake's quality was notably recognized when the Japanese Consulate in Vancouver selected it to toast the Emperor and Empress of Japan during a royal visit to Canada.

### 2. Osake Junmai Nigori Sparkling Sake
This is a cloudy, unfiltered sparkling sake that retains some of its rice sediment (*lees*) in the bottle. The winery describes it as velvety, off-dry, and creamy, balancing deep rice flavors with bright acidity and a smooth finish. 
* **Pairing Notes:** Because of its rich texture and effervescence, it is highly recommended as a companion for smoky, savory, or spicy dishes.

### 3. Mirai Traditional Method Sparkling Sake
This is a premium, dry sparkling sake crafted using the traditional Champagne method, produced in collaboration with Summerhill Pyramid Winery in Kelowna, BC. 
* **Joanne Sasvari (West Coast Food):** Reviewed the *Mirai* as a pleasantly dry, clean, and crisp bubble, noting distinct aromas of brioche and apples alongside a long, savory umami finish.
* **Chef Ken Nakano (Aura Restaurant, Victoria):** Highlighted the *Mirai* as an exceptional local treat for diners, praising the meticulous, small-lot production process that utilizes rice grown locally in BC's Fraser Valley.
  - [foodietours.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdPOmQ4bYuoJIWE7D1HnEFoK0mYWKA0tnHr2Ec6TlTKFMsjuZqjmwCqjZvsS7G-NsrH5cl_JjRnv4SXXfyhCasj9kU1R7A3kqd6c6rg2IIjvgyfruvcE6jCec-GgKBGMU2Om9jjtfu0RqqV4sNZg_29t6y): 
  - [chainevictoria.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2BykNj1KPUJV6s-WVCZj7Gm_2KPpnsnhiJ_iwAUdPM5KtOo0eubKsoL7DSGXObIfUa0VlpBrg12IkXd8iwBNvmw07Q-wWhNtZVxP060FdutXvhSNUuaRpa-YmMg6gXdWBOokBq_FDjTiOj4nBaUZNnkdurUZn1LjqbBBg0P_kja4=): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWj2q9hljCXakAyyz1L8NDRDzslBgmlIOtCVuB3KZP1ezFMcGoPtNjflrt4ROLxFKurCs3fyRYqT5_9FS5AbanTz511h_7j7wucvi7pYWW7c8Oasea9eWwaXdsbw==): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxVsGiuqfyyFZ7JaAe2d7nl404uxwWFZuenubGH80998s9YomPP1HVZ4Rp9YloGWZf9M7VUmqzpMdVsQXu1N14zX0iBPN7oXmATYAU3SP51YIm3ZKJXOa_Ap8Q2dwDPUi_nMQMDGQI0R8AEVFWK7I_mtONdQKzZo22FUm-lvrO9rU1C2kNrnoy72ZonXKArTNMH4kA6X8=): 
  - [vanmag.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIUh1lz5YGcVdfXOL0E8NMjo8914qJeJTFCFQcrJW7-4rGFzB7OqK0J-06m5ujGqKeR6S5vZwcypnbvsBDlYS_cHBEyeaT-wacYZEn7UhIzeSpfyGVjsRHq8Yl7YEgeNpiyKtkHmUzwjCRLGf3nhAtV1lFuownRknm5i7a): 
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf316LicQuvPje8jP30VhbcLF11AJwYw_kxeTjGJ9K5X4t8uiyeB1QJUBwDFNeJ4ImAS7ioLS67O9CEVKMzcBbIIqlQ7X0bbVWQx2izvzbmTfN2vRgU5KJSG4ywBxFiqoBhQAsHHd_r0p8uYSUwn-njAXh37y8IT4kjKAB_6O5qCt0RUHMkYg=): 
  - [bourbonplus.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb-zEVFHYWypaHRFIS7iPatvPEv1fsck1P9JdlDPwgGqfUOjJvTXWzTY4zvqyFwSn4iC_kujT7uaTTTfR5NIwPpo6sH65Bpa3bK0fb9NtURYhoJzLiNtayrpbu3-o5CfUMyCf277v9SjcLyW0682p1): 
  - [montecristomagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJ1ZAfdvuTyLt8QgRstiQTAp1wf7mnGmLih34jmjXC2MJE5RDZrgucCbClGQn_CqKXCl1FVtu6q69TEVqgZNuJvu09c-ipiE7FWUztvh67SRQ57_dwT7WeGcu94B7aPxQ9ybXrSAQRwSGjXLeVmXImldNtuGaxhIycKosqLUfdkTB9IiD2yT86Li0fVPLQUg==): 
  - [westcoastfood.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqgy76u7qNaOMUx1yFtTZZ_efqAJP1XUA5TikrCb7W69MrwuxA1YqXqinveF52QwPfR05HRrekqNS9cPrU5PTrMN1NQ6WZRu4B6AnXPV8I4MHyd_jpGd_kYwJAJO8yFmTiNyWoXeERdRfb5MKTmsnDh8a6NazwqnIgn2LcqqVuRwhLCNvMB_GzBZt6Qex2BXqrzRhUhH3FIAVLfLskbwxE3DMHFRGKjhGWei0w92fqM7-fvQ==): 

#### search_web_grounded_tool (status=ok, 11 results)
Search answer: Both **33 Acres Brewing Company** (and its experimental branch, **33 Brewing Experiment**) and **Strange Fellows Brewing**—two prominent craft breweries in Vancouver, BC—have produced sparkling, champagne-style beers and highly effervescent, wine-adjacent beverages. 

### 33 Acres Brewing Company / 33 Brewing Experiment
* **33B-EXP.004.MKV Brut IPA:** This experimental release was specifically crafted to emulate a very dry glass of Champagne. It features a highly carbonated, dry, and aromatic profile with minerality and fruit notes from heavy hopping.
* **Honour Roll Tropical Brut IPA:** A collaboration with Sooke Brewing Co. and BREWHALL. It is a tropical-style Brut IPA brewed with German Pilsner malt and Wakatu and Amarillo hops, resulting in a dry, spritzy, and effervescent finish.
* **33 X Boomtown: Sparkling Lager:** A collaborative, highly refreshing, and crisp sparkling lager featuring citrus and light floral notes.
* **Superberliner:** A Berliner Weisse brewed with tamarind and peach. The brewery notes that this style was historically dubbed the "Champagne of Beer" by Napoleon's troops due to its refreshing, effervescent qualities.

### Strange Fellows Brewing
* **Illustrum Brut IPA:** Released as a 5th-anniversary beer, this classic Brut IPA was barrel-aged with wild yeast strains (*Brett D* and *Sac Trois*). It is highly effervescent with a "Brett fizz" and offers a dry, bright, "Chablis-like" character with notes of pear and white grape.
* **Raspberry & Pineapple Berliner Weisse:** Brewed in the traditional German sour wheat style historically referred to as the "champagne of the north". These beers are packaged with high carbonation to deliver a sharp, refreshing, and bubbly mouthfeel.
* **The Strangers Rosé & POMPOM Piquette:** While not beers, Strange Fellows also produces sparkling wine products in-house using Okanagan grapes. *The Strangers Rosé* is a lightly sparkling, deep-hued rosé wine (12% ABV), while *POMPOM* is a highly effervescent, sessionable rosé wine spritz (6.5% ABV).
  - [33acresbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ24fOskZL6IIwS09w4NEBYitdueS2BQq9OONGk1H9seeDcvjENlQULMfHAAQOZS35JdG1ARSw2X57DwNjb9Rgs6C2AqXdlf2l31B9tHzTPB2q8Y42W23OcGKVIQCaEe1QfEsklFVXFQ==): 
  - [thegrowler.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiWqsmnQeimcvShcepH4Sv6JUvTv0TPSYADT3PcK9OtovU3-KAsQBQwSFeyGZvbJ0Uxj4A9KSNkyPgN7M9k3wkRHOPZrMYoXWr3oN72hhwuR-UA6q1c2wOldk2aZJm6u2vUVX0TtN-5rythWykwBDDgx9g1uXwa9rIxpvsydMLrFmNn3oYx4zPLBwWsgGP7zv_gsDNx-Od): 
  - [brewhall.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE14IIUfYck36_WK7axfHdulF4OnsGHmhayBmL4P7VU-pm6ittyoPTvOtQv8-9-0jWr3yGH8FG1nj17YYHst8wGTtrxo7PrPGkbFe0XvEIcnpBdPR1hqZGMb2H0UjUbx8F2Lcf5mlsyWNXMPw4O656cJE=): 
  - [untappd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNdGsG1H8mXAIIm2BZbCymquTUCB9cE7AiB25QBJKZ4gTvmCpfK_l5P39nKnf-oYhEMXO4zw2RXoxNVVXqA8D4pXdd6gJ9g8pcOX-l4OXMxLLIBRFkjITZJp1OaPvY3tlmd5fQChT-6OAZ5P8P4PjCXfuzP6xsYbxrYgO4DzulLKjmmlKmR-6LeA==): 
  - [yyctours.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnB7Y5X4JHShg7Nzhq3P6YBhlzekgbhL_HkkivAd_pFVQjOu5WnQEXChANI25oUDRVCWUtEFwOE8OPTHM0RFcbaT7PgHYTdWwPH3RHop8WlPDQs0LaAimlAdud-fJfxkWq3EqH5CW8g0zIkZZwSpJRYnFzRlzzwKpV): 
  - [strangefellowsbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNzyWqxZlCFIG-LenA68xCVHlodTA18L2wOJFHSM5FM0SowcrJTAqGOH3PP7NZC9ui6C0OCgCO55kGv-PfZR0OMESfpHj7JDi9mjLm_p2VUrMRXULw7tlb9zLYyeUOuFZYuVsA4h5cRK5pzzavwVE0ow==): 
  - [untappd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcdtsGrzyY1QexxHDaOA38Zh48CMpWrAHyyRAqRTXdm7N4V0OWzTVa3Zv1pA26AL9kqk0VJsroEkRWdymo9S3YJgbQqFOo4OqjB47aOiIArWn99Q5KkMbLTEIF--WOpGEzz-4y25rQVGWLKC1zs6aTDnQVVAUJg3fY): 
  - [strangefellowsbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpovCrayhFadNdv6QeDHQNiZl3McQCjgRWR55Xd9UIQT4xU4sFRQdt11HA4QwTII2QgBgJugtGt3HibIIJZi54ZXgcJesjQjleViwxddLceJ6CRiml1v5VeLGBf5u_W3VVyTl3rqWiD-od7DiMCfupvp_mSyDZwdmY3PnKxjA=): 
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvG46Xg0FkQAkTLaNgtKnKcvLhlGVUQNnr_7t9aIpFfKeOntwj4TF5-29MOjiNh-oC5ohFFiHQsgKPOQJxcKZkTlc8sN2-zSn97yz1lvWA9uv00RszGVH8Prls_TIxDx-lee65x3DV5ZWcdVhk-PU0z9Bu7SyvwnVv_CqST5bF7ZmWqvbhRB4ZFxDCw2kMV0cfmw-kkwfcBvT97IHF): 
  - [strangefellowsbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuvyfYnDZ7yU9vMmmMvw9i6rmJGbxACGdZfY1bGCwxHPymqHKojGcA8Ugg-dFoExYcqpT7O9o80A9udpLd2E4isDSBUaGkcEi7XIho-4pvh17eM16oprSwTugg0yFlzXeMiX0CK4PVKIh-ilD6uE4Bi-dX06JRMLYyGfo=): 
  - [strangefellowsbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIDbu0_c7JCxZwuwBbG34ZlMmAZktmcVNCFi5oBE4Xl_DQi87JNoQNsKSqcyLIxaM7oVeA8oTZaI1QVf2wIU9egYMb82f0PlBqJXVtuRDg8BI7D1Q8sBQIUnE6qtGFY8G-c08EqQsHc-LS5HFxTIvFGvyoOivHQ9HAjn-Hw1qsOpubg74=): 


### sourcing_agent_tool (status=ok)
**Sub-agent synthesis:**
Here is a comprehensive summary of BC sparkling wines under $35 currently in stock at Vancouver retailers. 

### **BC Liquor Stores (BCLS)**
*   **Monte Creek Living Land Sparkling Organic** – **$24.99** (520 units in stock across 37 stores) | [Product Link](https://www.bcliquorstores.com/product/21764)
*   **Monte Creek Living Land Sparkling Rosé Organic** – **$24.99** (677 units in stock across 62 stores) | [Product Link](https://www.bcliquorstores.com/product/228385)
*   **8th Generation Vineyard Confidence** – **$22.99** (426 units in stock across 39 stores) | [Product Link](https://www.bcliquorstores.com/product/79307)
*   **Stoneboat Vineyards Bubble Boat Brut** – **$19.99** (69 units in stock across 7 stores) | [Product Link](https://www.bcliquorstores.com/product/125118)
*   **Saintly The Good Sparkling Rosé Limited Release 2024** 
    *   750ml: **$19.99** (1,030 units in stock across 120 stores) | [Product Link](https://www.bcliquorstores.com/product/365659)
    *   200ml: **$7.49** (2,549 units in stock across 111 stores) | [Product Link](https://www.bcliquorstores.com/product/281830)
*   **Meadow Vista Bliss Sparkling Cherry Honey Wine** – **$16.99** (383 units in stock across 44 stores) | [Product Link](https://www.bcliquorstores.com/product/785915)
*   **Monte Creek Split Decision Sparkling** – **$21.99** (18 units in stock, 1 store) | [Product Link](https://www.bcliquorstores.com/product/102379)
*   **Sandhill Small Lots Sparkling Brut** – **$24.99** (1 unit in stock, 1 store) | [Product Link](https://www.bcliquorstores.com/product/281413)

---

### **Marquis Wine Cellars**
*   **Ursa Major x Bella Wines 2025 Ode to Sappho (750ml)** – **$34.99** (43 in stock) | [Product Link](https://www.marquis-wines.com/ursa-major-x-bella-wines-2024-ode-to-sappho-750ml/)
*   **Haywire 2018 Sparkling "The Bub" (750ml)** – **$32.99** (34 in stock) | [Product Link](https://www.marquis-wines.com/haywire-2015-sparkling-the-bub-750ml/)

---

### **Legacy Liquor Store**
*   **Church & State Sparkling Pinot Gris** – **$31.33** (13 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/church-state-sparkling-pinot-gris-1-x-750ml)
*   **Mt. Boucherie Estate Winery Mt. Bubbles Sparkling Wine** – **$29.84** (5 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/mt-boucherie-mt-bubbles-sparkling-1-x-750ml)
*   **Terravista Sparkling Albarino** – **$32.82** (3 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/terravista-sparkling-albarino-washington-1-x-750ml)
*   **Narrative XC Method Sparkling** – **$22.39** (5 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/narrative-xc-method-sparkling-1-x-750ml)
*   **Sidney Sparkling Rosé 7%** – **$19.78** (6 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/sidney-sparkling-rose-7-1-x-750ml)
*   **Sidney Sparkling Pinot Grigio 7%** – **$19.78** (4 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/sidney-sparkling-pinot-grigio-7-1-x-750ml)
*   **Mayhem Sparkling Rosé Can (250ml)** – **$9.58** (2 in stock) | [Product Link](https://www.legacyliquorstore.com/product/wine/mayhem-sparkling-rose-can-1-x-250ml)
*   **Glimmer Sparkling Blanc de Blancs (Non-Alcoholic)** 
    *   750ml: **$26.95** (7 in stock) | [Product Link](https://www.legacyliquorstore.com/product/non-alcoholic/glimmer-sparkling-blanc-de-blancs-non-alcoholic-1-x-750ml)
    *   250ml: **$10.67** (24 in stock) | [Product Link](https://www.legacyliquorstore.com/product/non-alcoholic/glimmer-sparkling-blanc-de-blanc-non-alcoholic-1-x-250ml)

---

### **Okanagan Cellars**
*   **Jackson Triggs Reserve Esprit Sparkling** – **$19.99** (38 in stock) | [Product Link](https://okanagancellars.com/products/2643401-jackson-triggs-reserve-esprit-sparkling)
*   **Honest Lot Sparkling** – **$12.99** (20 in stock) | [Product Link](https://okanagancellars.com/products/4990661-honest-lot-sparkling)
*   **ONES+ Non-Alcoholic Sparkling Pink** – **$24.99** (12 in stock) | [Product Link](https://okanagancellars.com/products/4460460-non-alc-ones-sparkling-pink)
*   **ONES+ Non-Alcoholic Sparkling White** – **$24.99** (3 in stock) | [Product Link](https://okanagancellars.com/products/4513441-non-alc-ones-sparkling-white)
*   **ONES+ Non-Alcoholic Sparkling Red** – **$24.99** (2 in stock) | [Product Link](https://okanagancellars.com/products/4460461-non-alc-ones-sparkling-red)

---

### **Sutton Place Wine Merchant**
*   *Note:* No BC sparkling options under $35 are currently in stock. The closest option is **Blue Mountain Brut Gold Label** at **$35.99** (26 in stock) | [Product Link](https://store.suttonplacewinemerchant.com/products/4144014-blue-mountain-brut-gold-label).

---

### **Everything Wine**
*   No matching BC sparkling wines under $35 are currently showing in-stock results.

#### search_bcliquor_tool (status=ok, 48 results)
  - FRESITA - SPARKLING WINE INFUSED WITH STRAWBERRIES | $21.49 | stock=1633 | in 123 stores | rating=3.9 | https://www.bcliquorstores.com/product/299404 | {sku=299404; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Chile; volume=0.750; alcohol_pct=8.0; sweetness=03; tasting_notes=The unique combination of the best sparkling wine with carefully selected strawberries, created through the Charmat method to deliver a natural, balanced and elegant taste.
; consumer_votes=261; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/299404.jpeg}
  - DIVAL COTEL - BRUT | $55.99 | stock=209 | in 28 stores | rating=2.8 | https://www.bcliquorstores.com/product/324387 | {sku=324387; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=01; consumer_votes=9; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/324387.jpeg}
  - VEUVE CLICQUOT VANCOUVER | $105.99 | stock=375 | in 24 stores | rating=5.0 | https://www.bcliquorstores.com/product/536920 | {sku=536920; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=00; consumer_votes=3; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/536920.jpeg}
  - VEUVE CLICQUOT - ROSE COOLER | $119.99 | stock=243 | in 20 stores | rating=3.7 | https://www.bcliquorstores.com/product/313861 | {sku=313861; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.5; sweetness=01; consumer_votes=33; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/313861.jpeg}
  - BOLLINGER - SPECIAL CUVEE BOND LABEL WITH GIFT BOX | $114.99 | stock=89 | in 19 stores | rating=4.6 | https://www.bcliquorstores.com/product/619500 | {sku=619500; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; consumer_votes=10; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/619500.jpeg}
  - DOM PERIGNON - WHITE LUMINOUS LABEL 2013 | $433.99 | stock=1 | in 1 stores | rating=4.5 | https://www.bcliquorstores.com/product/812685 | {sku=812685; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; consumer_votes=26; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/812685.jpeg}
  - MONTE CREEK  - LIVING LAND SPARKLING ORGANIC | $24.99 | stock=520 | in 37 stores | rating=4.6 | https://www.bcliquorstores.com/product/21764 | {sku=21764; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=12.3; sweetness=01; tasting_notes=89 Points, WineAlign: "Bright with fresh aromas of peach and pineapple on the nose and green apple, bosc pear on the palate. Very refreshing with a creamy mousse and long finish. Drink chilled on the patio with friends and small plates." (July 2025)
; consumer_votes=25; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/21764.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - UNDURRAGA - SPARKLING ROSE ROYALVALLE DE LEYDA | $25.99 | stock=72 | in 7 stores | rating=4.4 | https://www.bcliquorstores.com/product/177670 | {sku=177670; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Chile; volume=0.750; alcohol_pct=12.5; sweetness=01; tasting_notes=95 Points, Decanter: "Beautiful summer fruit and red apple nose. The palate is fruit-forward, juicy and elegant with refreshing acidity, a crisp mousse and a long, red cherry finish. Really well put together, expressive, joyful and cultured."
; consumer_votes=39; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/177670.jpeg}
  - SANDHILL - SMALL LOTS SPARKLING BRUT | $24.99 | stock=1 | in 1 stores | rating=4.1 | https://www.bcliquorstores.com/product/281413 | {sku=281413; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=11.7; sweetness=01; tasting_notes=Bright and expressive, with pristine, ripe lemon and apple that's lifted by fresh biscuit and honeysuckle. The fruit is beautifully framed by layered toast and brioche notes, with a soft, creamy mousse that coats the palate. Crisp and vibrant, the finish is long and full of fruit flavours.
; consumer_votes=11; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/281413.jpeg; certificates=["BC VQA", "All VQA"]}
  - SAINTLY - THE GOOD SPARKLING ROSE LIMITED RELEASE 2024 | $7.49 | stock=2549 | in 111 stores | rating=4.7 | https://www.bcliquorstores.com/product/281830 | {sku=281830; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.200; alcohol_pct=12.0; sweetness=00; tasting_notes=CRAFTED IN BC. On the nose, it's bursting with strawberry, raspberry, peach, and a splash of lime. The palate is crisp, dry, and textural—with juicy fruit, subtle florals, and a finish that lingers just long enough to tempt another sip.
; consumer_votes=7; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/281830.jpeg}
  - SAINTLY - THE GOOD SPARKLING ROSE LIMITED RELEASE 2024 | $19.99 | stock=1030 | in 120 stores | rating=4.4 | https://www.bcliquorstores.com/product/365659 | {sku=365659; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=12.0; sweetness=00; tasting_notes=CRAFTED IN BC. On the nose, it's bursting with strawberry, raspberry, peach, and a splash of lime. The palate is crisp, dry, and textural—with juicy fruit, subtle florals, and a finish that lingers just long enough to tempt another sip.
; consumer_votes=17; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/365659.jpeg}
  - MEADOW VISTA - BLISS SPARKLING CHERRY HONEY WINE | $16.99 | stock=383 | in 44 stores | rating=3.8 | https://www.bcliquorstores.com/product/785915 | {sku=785915; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.500; alcohol_pct=12.0; sweetness=01; tasting_notes=Dark, juicy Okanagan cherries were added to give BLISS a beautiful blush colour, notes of cherry, plum and pinot noir. Delight in this bubbly with grilled foods such as seasonal veggies, meats and fruit.
; consumer_votes=137; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/785915.jpeg}
  - DE CHANCENY - CREMANT DE LOIRE ROSE BRUT | $28.99 | stock=397 | in 36 stores | rating=4.4 | https://www.bcliquorstores.com/product/15727 | {sku=15727; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=10.5; sweetness=00; consumer_votes=232; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/15727.jpeg}
  - GILDA - BLANC DE BLANCS MILLESIMATO | $16.99 | stock=2053 | in 120 stores | rating=4.6 | https://www.bcliquorstores.com/product/772432 | {sku=772432; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Italy; volume=0.750; alcohol_pct=11.5; sweetness=00; consumer_votes=49; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/772432.jpeg}
  - MONTE CREEK - SPLIT DECISION SPARKLING | $21.99 | stock=18 | in 1 stores | rating=5.0 | https://www.bcliquorstores.com/product/102379 | {sku=102379; product_type=Other Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=02; consumer_votes=1; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/102379.jpeg}
  - BABY CANADIAN SPARKLING | $9.99 | stock=3041 | in 172 stores | rating=3.5 | https://www.bcliquorstores.com/product/3814 | {sku=3814; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=6.9; sweetness=04; tasting_notes=Aromas of fresh apple and pear carry through on the palate. This sparkling wine has just a touch of sweetness balanced by refreshing acidity and a delicate mouthfeel. Serve with lightly spiced chicken or pork or enjoy on it's own as a refreshing sipping wine.
; consumer_votes=352; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/3814.jpeg}
  - BOTTEGA - SPARKLING SET IN ICE BAG | $46.99 | stock=675 | in 112 stores | rating=4.1 | https://www.bcliquorstores.com/product/262860 | {sku=262860; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Italy; volume=0.200; alcohol_pct=11.0; sweetness=00; tasting_notes=A festive sparkling wine set with bright aromas of apple, pear, and citrus. The palate is lively and refreshing, showing orchard fruit, lemon zest, and gentle floral notes. Fine bubbles carry through to a clean, crisp finish.
; consumer_votes=93; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/262860.jpeg}
  - PELLER FAMILY VINEYARDS - PINOT GRIGIO SPARKLING | $12.49 | stock=1960 | in 139 stores | rating=4.4 | https://www.bcliquorstores.com/product/333925 | {sku=333925; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=12.0; sweetness=02; tasting_notes=Look for aromas of yellow apple and pear on the nose. This sparkling Pinot Grigio is light bodied, with refreshing acidity, and a lively expanding mousse. Flavours of ripe tree fruits excite the palate, then notes of citrus and apple linger on the dry-ish finish. Enjoy while young and fresh.
; consumer_votes=80; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/333925.jpeg}
  - 8TH GENERATION VINEYARD - CONFIDENCE | $22.99 | stock=426 | in 39 stores | rating=4.2 | https://www.bcliquorstores.com/product/79307 | {sku=79307; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=12.7; sweetness=02; consumer_votes=17; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/79307.jpeg; certificates=["BC VQA", "All VQA"]}
  - STONEBOAT VINEYARDS - BUBBLE BOAT BRUT | $19.99 | stock=69 | in 7 stores | rating=4.4 | https://www.bcliquorstores.com/product/125118 | {sku=125118; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=12.6; sweetness=00; consumer_votes=19; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/125118.jpeg; certificates=["BC VQA", "All VQA"]}
  - MISSION HILL FAMILY ESTATE - RESERVE BRUT MENDOCINO COUNTY | $28.99 | stock=11 | in 1 stores | rating=5.0 | https://www.bcliquorstores.com/product/284922 | {sku=284922; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=11.5; sweetness=01; consumer_votes=1; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/284922.jpeg}
  - GERARD BERTRAND - ESPRIT DE COTE DES ROSES BRUT ROSE | $32.99 | stock=329 | in 28 stores | https://www.bcliquorstores.com/product/753379 | {sku=753379; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=01; consumer_votes=0; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/753379.jpeg}
  - MOET AND CHANDON - NIRO LIGHT UP | $189.99 | stock=7 | in 2 stores | rating=5.0 | https://www.bcliquorstores.com/product/188081 | {sku=188081; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=1.500; alcohol_pct=12.0; sweetness=00; consumer_votes=4; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/188081.jpeg}
  - ARTHUR METZ - CREMANT D'ALSACE 1904 BLANC | $29.99 | stock=165 | in 31 stores | rating=4.0 | https://www.bcliquorstores.com/product/717813 | {sku=717813; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=01; tasting_notes=Light yellow with golden highlights, fine mousse. Delicate, floral and white fruits on the nose. Fine, pleasant bubbles, elegant palate with a fruity finish.; consumer_votes=16; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/717813.jpeg}
  - MONTE CREEK - LIVING LAND SPARKLING ROSE ORGANIC | $24.99 | stock=677 | in 62 stores | rating=4.5 | https://www.bcliquorstores.com/product/228385 | {sku=228385; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=13.3; sweetness=02; tasting_notes=No special occasion is required for this elegant, bubbly rose. With aromas of strawberries, citrus and a hint of peach, it is crisp and worth celebrating in itself. Ripe strawberry and juicy watermelon come through clearly on the palate. Made from 100% estate grown Marquette using the Charmat method.
; consumer_votes=43; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/228385.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - TAITTINGER - COMTES DE CHAMPAGNE BLANC DE BLANCS 2012 | $350.99 | stock=83 | in 15 stores | rating=4.6 | https://www.bcliquorstores.com/product/43644 | {sku=43644; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.5; sweetness=01; tasting_notes=99 Points, James Suckling: "Full-bodied with a lovely framework of acidity and dry fruit, such as apples, pears and peaches. Opulent. Dense and muscular. Yet, it's balanced and harmonious. One for the cellar." Nov 2019; consumer_votes=45; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/43644.jpeg}
  - PERRIER-JOUET BELLE EPOQUE ROSE | $289.99 | stock=134 | in 15 stores | rating=5.0 | https://www.bcliquorstores.com/product/153973 | {sku=153973; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.5; sweetness=01; tasting_notes=Belle Epoque Rosé 2013 is a rich, fresh and aromatic cuvée distinguished by aromas of rose and peony, complemented by delicious hints of raspberries, wild strawberries, pink grapefruit. A perfectly balanced wine with a frank attack followed by a beautifully rounded sensation on the palate, and a long, silken finish.
; consumer_votes=2; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/153973.jpeg}
  - PIPER HEIDSIECK - ROSE SAUVAGE | $75.99 (reg $84.99) | stock=145 | in 18 stores | rating=5.0 | https://www.bcliquorstores.com/product/186650 | {sku=186650; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=01; consumer_votes=1; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/186650.jpeg}
  - DOM PERIGNON - BASQUIAT | $356.99 | stock=36 | in 9 stores | rating=4.1 | https://www.bcliquorstores.com/product/197614 | {sku=197614; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Dom Pérignon pays tribute to an artist who formed one of the most iconic and powerful expressions of our time: Jean-Michel Basquiat. Dom Pérignon Vintage 2015 stands out for its complex aromatic flavour profile combining intense roasted and cocoa notes, balanced by delicate floral aromas of blossom, jasmine and peony. 
; consumer_votes=22; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/197614.jpeg}
  - POL ROGER - PURE  EXTRA BRUT | $114.99 | stock=39 | in 4 stores | rating=4.1 | https://www.bcliquorstores.com/product/256354 | {sku=256354; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=0.750; alcohol_pct=12.5; sweetness=01; tasting_notes=94 Points, James Suckling: "A creamy and round-textured Champagne with a pretty back bone of phenolics and acidity. It's medium-to full-bodied with layers melted together and a flavourful finish. Attractive bitter lemon at the end. 1/3 pinot noir, 1/3 chardonnay and 1/3 pinot meunier. Drink now." (June 2022)
; consumer_votes=9; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/256354.jpeg}
  - LOUIS ROEDERER - CRISTAL BRUT | $1160.00 | stock=1 | in 1 stores | rating=4.4 | https://www.bcliquorstores.com/product/350173 | {sku=350173; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=1.500; alcohol_pct=12.0; sweetness=00; tasting_notes=Amber hue with green and orange tints. Fine, even and lively effervescence. A complex and intense bouquet disclosing candied citrus, yellow fruit, pear, pollen and toasted almonds. The delicately seductive bouquet shows depth with a well-honed precision.
; consumer_votes=36; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/350173.jpeg}
  - VEUVE CLICQUOT - BRUT | $50.99 | stock=1679 | in 133 stores | rating=3.5 | https://www.bcliquorstores.com/product/389056 | {sku=389056; product_type=Sparkling Wine; grape_type=OTHER GRAPE VARIETY; country=France; volume=0.375; alcohol_pct=12.0; sweetness=00; tasting_notes=94 Points, Decanter: "Lemony richness on the nose, a struck match character that falls in with lemon vanilla note. Toffee apple allure on the palate with chalky coolness and a savoury, nutty finish." (2021)
; consumer_votes=147; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/389056.jpeg}
  - LAURENT-PERRIER - BLANC DE BLANCS BRUT NATURE | $174.99 | stock=68 | in 16 stores | rating=3.6 | https://www.bcliquorstores.com/product/390867 | {sku=390867; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=00; tasting_notes=94 Points, James Suckling: "A dense and flavorful chardonnay with creamy texture and flavor. Lots of citrus and grapefruit and very vinous. A blanc de blancs with weight yet freshness. Pure chardonnay with no dosage. A new wine. Lovely finish. 40% 2009 and 60% 2012. Drink now." (Sept 2019)
; consumer_votes=10; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/390867.jpeg}
  - TAITTINGER - BRUT RESERVE | $83.99 | stock=1345 | in 157 stores | rating=4.5 | https://www.bcliquorstores.com/product/457713 | {sku=457713; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=0.750; alcohol_pct=12.0; sweetness=00; tasting_notes=92 Points, James Suckling: "Lemon, biscuit, fresh peach and pie crust on the nose. It's creamy and silky with excellent freshness and very soft bubbles. 40% chardonnay, 35% pinot noir and 25% pinot meunier. Base wine from 2020 (70%) with 30% reserve wines." July 2024
; consumer_votes=356; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/457713.jpeg}
  - MOET AND CHANDON - NECTAR IMPERIAL | $90.99 | stock=438 | in 65 stores | rating=3.8 | https://www.bcliquorstores.com/product/509695 | {sku=509695; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=0.750; alcohol_pct=12.0; sweetness=03; tasting_notes=Nectar Impérial is a delicious expression of the Moët & Chandon style, a style distinguished by its bright fruitiness, its seductive palate and its elegant maturity.
; consumer_votes=153; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/509695.jpeg}
  - VEUVE CLICQUOT - BRUT | $85.99 | stock=3000 | in 196 stores | rating=3.8 | https://www.bcliquorstores.com/product/563338 | {sku=563338; product_type=Sparkling Wine; grape_type=OTHER GRAPE VARIETY; country=France; volume=0.750; alcohol_pct=12.0; sweetness=00; tasting_notes=94 Points, Decanter: "Lemony richness on the nose, a struck match character that falls in with lemon vanilla note. Toffee apple allure on the palate with chalky coolness and a savoury, nutty finish." (2021); consumer_votes=440; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/563338.jpeg}
  - VEUVE CLICQUOT - ROSE | $104.99 | stock=806 | in 107 stores | rating=3.9 | https://www.bcliquorstores.com/product/945261 | {sku=945261; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.3; sweetness=00; tasting_notes=91 Points, Wine Spectator. "A mouthwatering rosé Champagne, with a lacy, delicate mousse, this bursts with tangerine and pomelo flavors, plus accents of toast point, pastry cream, smoke and chamomile. Pinot Noir, Chardonnay and Pinot Meunier. Drink now." (November 2024)
; consumer_votes=128; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/945261.jpeg}
  - HENRIOT - BLANC DE BLANCS BRUT | $86.99 | stock=24 | in 3 stores | rating=3.5 | https://www.bcliquorstores.com/product/76356 | {sku=76356; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=0.750; alcohol_pct=12.0; sweetness=01; tasting_notes=93 Points, Wine Spectator: "Multiple aromas intertwine, bringing great complexity, from flambéed pineapple and fresh citrus fruit notes to wet chalk and subtle pastry aromas. On the palate, this Champagne has an incredible velvety texture accompanied by an extraordinary freshness" (November 2024)
; consumer_votes=22; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/76356.jpeg}
  - BEAUMONT DES CRAYERES - JACQUES LORENT GRANDE  RESERVE | $51.99 | stock=382 | in 36 stores | rating=3.3 | https://www.bcliquorstores.com/product/132900 | {sku=132900; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=00; tasting_notes=91 Points, Decanter: "Authentic, elegant and fruity. Light yellow golden robe with fine and shiny bubbles.Expressive and fruity nose over notes of Mirabelle plums, pinapple, butter and yeast. Honey flavored palate with fresh plum and cherry stones notes. Pleasant finish with a good length." (2020)
; consumer_votes=37; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/132900.jpeg}
  - LAURENT PERRIER - CUVEE ROSE BRUT | $119.99 | stock=720 | in 91 stores | rating=4.2 | https://www.bcliquorstores.com/product/158550 | {sku=158550; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=00; tasting_notes=94 Points, Wine Enthusiast: "This great rosé combines texture with bright fruit and a bit of age. It is poised between a ripe dosage and a crisp texture, with red fruits and toastiness marking the flavors. It is a fine bottling to enjoy now." (December 2020)
; consumer_votes=131; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/158550.jpeg}
  - TAITTINGER - BRUT RESERVE FIFA 2026 | $114.99 | stock=371 | in 14 stores | rating=4.6 | https://www.bcliquorstores.com/product/168060 | {sku=168060; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.5; sweetness=01; tasting_notes=91 Points, Wine Spectator - "Hints of smoke and spice underscore flavors of poached pear and white raspberry in this delicate, aperitif-style Champagne, with a lacy mousse. Crisp and lightly citrusy. Drink now through 2021." (November 2017)
; consumer_votes=18; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/168060.jpeg}
  - POL ROGER - RESERVE BRUT | $56.99 | stock=102 | in 9 stores | rating=4.2 | https://www.bcliquorstores.com/product/195818 | {sku=195818; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=0.375; alcohol_pct=12.0; sweetness=00; tasting_notes=92 Points, Wine Advocate: "The current release of Pol Roger's NV Brut Réserve is quite dramatic, bursting with aromas of mandarin oil, honeycomb, elderflower, fresh bread and musky peach. Medium to full-bodied, fleshy and enveloping, it's generous and textural, with a rich core of fruit, lively acids and a pillowy mousse. Drink Date: 2021 - 2035." (March 2021)
; consumer_votes=71; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/195818.jpeg}
  - PIPER HEIDSECK - CUVEE BRUT GLASS PACK | $89.99 | stock=78 | in 7 stores | rating=3.2 | https://www.bcliquorstores.com/product/262855 | {sku=262855; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=00; tasting_notes=95 Points, International Wine Challenge: "Lovely broad autolytic attack. Very fine mousse. Tight, taut style with great breadth and length. Creamy apple and lemon flavours with long, elegant and savoury finish. Delicious."
; consumer_votes=24; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/262855.jpeg}
  - POL ROGER - BRUT VINTAGE BLACK FOIL 2018 | $134.99 | stock=194 | in 24 stores | rating=4.5 | https://www.bcliquorstores.com/product/343702 | {sku=343702; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.0; sweetness=01; tasting_notes=94 Points, James Suckling: "I like the berry fruit aromas mingling with bread crust, grapefruit and lemon pastries. It's lively on the palate, with excellent structure and a bright wild-berry character. Clean and nicely focused. 60% Pinot Noir and 40% Chardonnay. Disgorged 2024. Drink or hold." (July 2025); consumer_votes=2; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/343702.jpeg}
  - TAITTINGER - CUVEE PRESTIGE ROSE | $99.99 | stock=511 | in 63 stores | rating=4.7 | https://www.bcliquorstores.com/product/372367 | {sku=372367; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.5; sweetness=01; tasting_notes=92 Points, James Suckling: "A lovely, deep ruby color with aromas of sliced apples, oranges, pomegranates and dried flowers. Some honey, too. It's deliciously fruity, ripe and silky. Delicate finish. Blend of 45% pinot noir, 35% chardonnay and the rest pinot meunier with 14% red wine." (July 2025)
; consumer_votes=14; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/372367.jpeg}
  - BOLLINGER - SPECIAL CUVEE BRUT | $109.99 | stock=440 | in 69 stores | rating=4.4 | https://www.bcliquorstores.com/product/384529 | {sku=384529; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=0.750; alcohol_pct=12.0; sweetness=01; tasting_notes=92 points Wine Spectator: "This focused Champagne shows lovely balance, with its satinlike mousse and well-honed acidity enmeshed with flavors of white cherry, pureed raspberry, toast point and creamed almond. Hints of spices and smoke play on the lingering finish. Pinot Noir, Chardonnay and Pinot Meunier." - September 2024
; consumer_votes=243; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/384529.jpeg}
  - MOET AND CHANDON - BRUT IMPERIAL | $48.99 | stock=870 | in 74 stores | rating=3.7 | https://www.bcliquorstores.com/product/453076 | {sku=453076; product_type=Sparkling Wine; grape_type=OTHER BLEND; country=France; volume=0.375; alcohol_pct=12.0; sweetness=00; tasting_notes=91 Points, Wine Spectator: "A rich note of grilled nut meets flavors of Asian pear, preserved lemon and mineral on the palate of this creamy Champagne, driven by a firm streak of refreshing acidity. Drink now through 2022." (December 2019)
; consumer_votes=98; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/453076.jpeg}
  - MOET AND CHANDON - ROSE IMPERIAL | $98.99 | stock=753 | in 104 stores | rating=3.9 | https://www.bcliquorstores.com/product/482026 | {sku=482026; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=France; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=91 Points, Wine Spectator: "An elegant, mouthwatering rosé Champagne, with a fine, zesty mousse, this offers flavours of baked raspberry and white cherry fruit and candied pink grapefruit peel, plus rich hints of pastry cream and blanched almond. Pinot Noir, Pinot Meunier and Chardonnay. Drink now." (November 2024)
; consumer_votes=145; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/482026.jpeg}

#### search_everything_wine_tool (status=ok, 0 results)

#### search_okanagan_cellars_tool (status=ok, 15 results)
  - HAINLE - NO.72 VOL 2 SPARKLING | $40.99 | stock=5 | https://okanagancellars.com/products/4580996-hainle-no-72-vol-2-sparkling | {category=Bubbles; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000035/0000356504-3279.png}
  - HESTER CREEK - SPARKLING PINOT BLANC | $39.99 | stock=17 | https://okanagancellars.com/products/4317051-hester-creek-sparkling-pinot-blanc | {category=Bubbles; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000006/0000062139-4695.png}
  - HONEST LOT - SPARKLING | $12.99 | stock=20 | https://okanagancellars.com/products/4990661-honest-lot-sparkling | {category=Bubbles; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000070/0000700813-7808.jpg}
  - JACKSON TRIGGS - RESERVE ESPRIT SPARKLING | $19.99 | stock=38 | https://okanagancellars.com/products/2643401-jackson-triggs-reserve-esprit-sparkling | {category=Bubbles; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000042/0000425918-8302.png}
  - NON-ALC - BB NOVA PINK SPARKLING | $4.99 | stock=26 | https://okanagancellars.com/products/5014399-non-alc-bb-nova-pink-sparkling | {category=Non Alcoholic; in_stock=True; unit_size=250ml; image_url=https://okanagancellars.com/static/custom/goods/131/0000W2/0000W20788-3613.jpg}
  - NON-ALC - HENKELL SPARKLING | $16.99 | stock=1 | https://okanagancellars.com/products/4993899-non-alc-henkell-sparkling | {category=Non Alcoholic; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/all/BC499696.png}
  - NON-ALC - LEITZ SPARKLING | $19.99 | stock=5 | https://okanagancellars.com/products/4744343-non-alc-leitz-sparkling | {category=Non Alcoholic; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/0000w1/0000w17917-6314.jpg}
  - NON-ALC - LEITZ SPARKLING ROSE | $19.99 | stock=3 | https://okanagancellars.com/products/4744345-non-alc-leitz-sparkling-rose | {category=Non Alcoholic; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/0000w1/0000w17920-1208.jpg}
  - NON-ALC - ONES+ MINI RED SPARKLING | $7.99 | stock=5 | https://okanagancellars.com/products/5070742-non-alc-ones-mini-red-sparkling | {category=Non Alcoholic; in_stock=True; unit_size=200ml; image_url=https://okanagancellars.com/static/custom/goods/131/1s+min/1s+miniredspark-7127.jpg}
  - NON-ALC - ONES+ MINI WHITE SPARKLING | $7.99 | stock=16 | https://okanagancellars.com/products/5070743-non-alc-ones-mini-white-sparkling | {category=Non Alcoholic; in_stock=True; unit_size=200ml; image_url=https://okanagancellars.com/static/custom/goods/131/1s+min/1s+miniwhitspark-2357.jpg}
  - NON-ALC - ONES+ SPARKLING PINK | $24.99 | stock=12 | https://okanagancellars.com/products/4460460-non-alc-ones-sparkling-pink | {category=Non Alcoholic; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/1s+pin/1s+pinkspark-5669.jpg}
  - NON-ALC - ONES+ SPARKLING RED | $24.99 | stock=2 | https://okanagancellars.com/products/4460461-non-alc-ones-sparkling-red | {category=Non Alcoholic; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/1s+red/1s+redspark-6378.jpg}
  - NON-ALC - ONES+ SPARKLING WHITE | $24.99 | stock=3 | https://okanagancellars.com/products/4513441-non-alc-ones-sparkling-white | {category=Non Alcoholic; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/1s+wht/1s+whtspark-7474.jpg}
  - NON-ALC - RUFFINO SPARKLING | $21.99 | stock=22 | https://okanagancellars.com/products/5216727-non-alc-ruffino-sparkling | {category=Non Alcoholic; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/0000w2/0000w22229-2726.jpg}
  - ROAD 13 - SPARKLING CHENIN BLANC | $44.99 | stock=16 | https://okanagancellars.com/products/3420958-road-13-sparkling-chenin-blanc | {category=Bubbles; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000082/0000820696-7288.png}

#### search_suttonplace_tool (status=ok, 15 results)
  - Andre & Mireille Tissot Cremant du Jura 1.5L | $140.49 | stock=3 | https://store.suttonplacewinemerchant.com/products/4480025-andre-mireille-tissot-cremant-du-jura-1-5l | {category=SPARKLING FRANCE; in_stock=True; unit_size=1.5 L Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000021/0000217527-4877.png; country=FRANCE; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}
  - Anna de Codorniu Cava | $24.49 | stock=35 | https://store.suttonplacewinemerchant.com/products/4671632-anna-de-codorniu-cava | {category=SPARKLING ITALY; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000015/0000156075-2047.jpg; country=SPAIN; alcohol_pct=12.00; is_staff_pick=False; is_featured=False}
  - Batasiolo Moscato | $25.49 | 2021 | stock=20 | https://store.suttonplacewinemerchant.com/products/4143697-batasiolo-moscato | {category=SPARKLING ITALY; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000028/0000288449-7265.png; country=ITALY; varietal=Moscato; alcohol_pct=5.50; is_staff_pick=False; is_featured=False}
  - Birch Block Blanc de Franc Pet Nat | $42.49 | 2022 | stock=5 | https://store.suttonplacewinemerchant.com/products/4625402-birch-block-blanc-de-franc-pet-nat | {category=SPARKLING CANADA; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000024/0000245349-8031.png; country=CANADA; varietal=Cabernet Franc; alcohol_pct=9.80; is_staff_pick=False; is_featured=False}
  - Blue Mountain Brut Gold Label  | $35.99 | stock=26 | https://store.suttonplacewinemerchant.com/products/4144014-blue-mountain-brut-gold-label | {category=SPARKLING CANADA; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000047/0000471672-6624.jpg; country=CANADA; alcohol_pct=12.50; is_staff_pick=False; is_featured=False}
  - Bottega Gold | $37.99 | stock=17 | https://store.suttonplacewinemerchant.com/products/5103019-bottega-gold | {category=SPARKLING ITALY; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC663187.png; country=ITALY; is_staff_pick=False; is_featured=False}
  - Bottega Gold Prosecco 200ml | $11.99 | stock=31 | https://store.suttonplacewinemerchant.com/products/4578754-bottega-gold-prosecco-200ml | {category=SPARKLING ITALY; in_stock=True; unit_size=200ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC20605.jpg; country=ITALY; varietal=Glera; alcohol_pct=11.00; is_staff_pick=False; is_featured=False}
  - Bottega Rose Gold | $35.99 | stock=16 | https://store.suttonplacewinemerchant.com/products/5103018-bottega-rose-gold | {category=SPARKLING ITALY; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/all/BC223669.jpg; country=ITALY; is_staff_pick=False; is_featured=False}
  - Caves de Lugny Cremant de Bourgogne Rose | $32.99 | stock=41 | https://store.suttonplacewinemerchant.com/products/4143517-caves-de-lugny-cremant-de-bourgogne-rose | {category=SPARKLING FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000019/0000195545-5164.jpg; country=FRANCE; alcohol_pct=12.00; is_staff_pick=False; is_featured=False}
  - Cleto Chiarli Premium Lambrusco di Sorbara | $34.49 | stock=3 | https://store.suttonplacewinemerchant.com/products/4144555-cleto-chiarli-premium-lambrusco-di-sorbara | {category=SPARKLING ITALY; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000088/0000884791-4864.jpg; country=ITALY; varietal=Lambrusco; alcohol_pct=11.00; is_staff_pick=False; is_featured=False}
  - DRAPPIER CARTE DOR BRUT | $85.99 | stock=12 | https://store.suttonplacewinemerchant.com/products/4144384-drappier-carte-dor-brut | {category=SPARKLING ITALY; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000072/0000726281-8235.jpg; country=FRANCE; alcohol_pct=12.00; is_staff_pick=False; is_featured=False}
  - Domaine Rolet Cremant de Jura Brut | $40.99 | stock=13 | https://store.suttonplacewinemerchant.com/products/4197720-domaine-rolet-cremant-de-jura-brut | {category=SPARKLING FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000030/0000304246-9165.png; country=FRANCE; alcohol_pct=12.00; is_staff_pick=False; is_featured=False}
  - Drappier Carte dOr 1.5L | $192.49 | stock=4 | https://store.suttonplacewinemerchant.com/products/4656333-drappier-carte-dor-1-5l | {category=SPARKLING FRANCE; in_stock=True; unit_size=1.5 L Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000023/0000233596-7291.jpg; country=FRANCE; is_staff_pick=False; is_featured=False}
  - Feudi di San Gregorio DUBL Rosato | $74.49 | stock=2 | https://store.suttonplacewinemerchant.com/products/4741543-feudi-di-san-gregorio-dubl-rosato | {category=SPARKLING ITALY; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000005/0000052030-2921.png; country=ITALY; alcohol_pct=12.00; is_staff_pick=False; is_featured=False}
  - Francois Pinon Vouvray Brut | $47.99 | 2018 | stock=2 | https://store.suttonplacewinemerchant.com/products/4207318-francois-pinon-vouvray-brut | {category=SPARKLING FRANCE; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000050/0000502118-3754.jpg; country=FRANCE; varietal=Chenin Blanc; alcohol_pct=13.00; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 20 results)
  - Tement MUSKAT Brut Sparkling Gelber Muskateller 750ml | $51.99 | stock=72 | https://www.marquis-wines.com/tement-muska-t-brut-sparkling-gelber-muskateller-750ml/ | {sku=1030332; in_stock=True; categories=["Organic Biodynamic Wine Sale", "Marquis Exclusives", "Tement", "Champagne & Bubbles", "Sparkling", "Organic / Biodynamic Wine", "Austria", "Steiermark"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20641/images/16367/2025-07-18_10.48.23__66344.1753113579.500.500.png?c=2}
  - Zeno Low Alcohol Sparkling Rose 750ml | $28.99 | stock=29 | https://www.marquis-wines.com/zeno-low-alcohol-sparkling-rose-750ml/ | {sku=1030222; in_stock=True; categories=["Non-Alcoholic"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19233/images/14964/2024-08-19-15.10.56__66570.1724174956.500.500.png?c=2}
  - Noughty Sparkling Chardonnay Non-Alcoholic 750ml | $24.99 | stock=4 | https://www.marquis-wines.com/noughty-sparkling-chardonnay-non-alcoholic-750ml/ | {sku=1029645; in_stock=True; categories=["Non-Alcoholic"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18565/images/14452/2024-02-29_15.32.18__88912.1709321408.500.500.png?c=2}
  - Catena Domaine EdeM Sparkling Blonde Non-Alcoholic 750ml | $31.99 | stock=11 | https://www.marquis-wines.com/catena-domaine-edem-sparkling-blonde-non-alcoholic-750ml/ | {sku=1032221; in_stock=True; categories=["Non-Alcoholic"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21753/images/17460/2026-04-30_15.02.44__91726.1777654814.500.500.png?c=2}
  - Catena Domaine EdeM Sparkling Brunette Non-Alcoholic 750ml | $29.49 | stock=12 | https://www.marquis-wines.com/catena-domaine-edem-sparkling-brunette-non-alcoholic-750ml/ | {sku=1032220; in_stock=True; categories=["Non-Alcoholic"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21754/images/17472/2026-04-30_15.03.18__10256.1778188482.500.500.png?c=2}
  - R & O Sparkling Brut 750ml | $19.99 | stock=12 | https://www.marquis-wines.com/r-o-sparkling-brut-750ml/ | {sku=1031699; in_stock=True; categories=["Champagne & Bubbles", "Sparkling"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21103/images/16810/2025-11-13-16.07.42__17823.1763153973.500.500.png?c=2}
  - Lightfoot & Wolfville 2019 Sparkling Brut 750ml | $58.99 | stock=36 | https://www.marquis-wines.com/lightfoot-wolfville-2019-sparkling-brut-750ml/ | {sku=1031326; in_stock=True; categories=["Champagne & Bubbles", "Champagne", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20617/images/16473/2025-08-12-13.37.02__72743.1755105972.500.500.png?c=2}
  - Lightfoot & Wolfville 2021 Sparkling Rose Brut 750ml | $58.99 | stock=22 | https://www.marquis-wines.com/lightfoot-wolfville-2021-sparkling-rose-brut-750ml/ | {sku=1031320; in_stock=True; categories=["Sparkling", "Champagne & Bubbles"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20631/images/16433/2025-07-31_13.59.46__36979.1754070703.500.500.png?c=2}
  - Coravin Sparkling Wine Access System | $624.99 | stock=1 | https://www.marquis-wines.com/coravin-sparkling-wine-access-system/ | {sku=1029233; in_stock=True; categories=["Wine Gadgets"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18218/images/14092/IMG-Sparkling__71945.1700595158.500.500.jpg?c=2}
  - Coravin Pure Sparkling CO2 Capsules (6 pack) | $74.99 | stock=3 | https://www.marquis-wines.com/coravin-pure-sparkling-co2-capsules-6-pack/ | {sku=1029232; in_stock=True; categories=["Wine Gadgets"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18212/images/14088/IMG-Sparkling-Capsules-6__89224.1700594334.500.500.jpg?c=2}
  - Cuvee Jean-Louis Sparkling Rose 750ml | $20.99 | stock=16 | https://www.marquis-wines.com/cuvee-jean-louis-sparkling-rose-750ml/ | {sku=1018160; in_stock=True; categories=["Champagne & Bubbles", "Sparkling"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20723/images/16498/2025-08-14_14.53.34__49238.1755293425.500.500.png?c=2}
  - Haywire 2018 Sparkling "The Bub" 750ml | $32.99 | stock=34 | https://www.marquis-wines.com/haywire-2015-sparkling-the-bub-750ml/ | {sku=1016651; in_stock=True; categories=["Sparkling"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7093/images/4972/Haywire-Bub-2014-web__77435.1541525609.500.500.jpg?c=2}
  - Blue Mountain N/V Gold Label Brut 750ml | $37.99 | stock=33 | https://www.marquis-wines.com/blue-mountain-n-v-gold-label-brut-750ml/ | {sku=471672; in_stock=True; categories=["Sparkling", "Okanagan Falls", "British Columbia", "Lunar New Year"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/6072/images/11775/blue-mountain-gold-brut__28311.1648759359.500.500.jpg?c=2}
  - Henkell Trocken 750ml | $17.99 | stock=16 | https://www.marquis-wines.com/henkell-trocken-750ml/ | {sku=122689; in_stock=True; categories=["Sparkling"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7095/images/6519/henkell__42697.1523467661.500.500.jpg?c=2}
  - Bella Wines 2025 Traditional Method Gamay 750ml | $44.99 | stock=15 | https://www.marquis-wines.com/bella-wines-2025-traditional-method-gamay-750ml/ | {sku=1032270; in_stock=True; categories=["Champagne & Bubbles", "Sparkling", "Organic / Biodynamic Wine", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21809/images/17500/2026-05-15-12.08.53__71393.1779220922.500.500.png?c=2}
  - Ursa Major x Bella Wines 2025 Ode to Sappho 750ml | $34.99 | stock=43 | https://www.marquis-wines.com/ursa-major-x-bella-wines-2024-ode-to-sappho-750ml/ | {sku=1030830; in_stock=True; categories=["Sparkling", "Champagne & Bubbles", "Celebrate BC Wine Month"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19990/images/15730/2025-02-11-16.03.50__29139.1739474333.500.500.png?c=2}
  - Erwin Sabathi 2019 Chardonnay Brut 750ml | $69.99 | stock=33 | https://www.marquis-wines.com/erwin-sabathi-2019-chardonnay-brut-750ml/ | {sku=1027471; in_stock=True; categories=["Marquis Exclusives", "Champagne & Bubbles", "Sparkling", "Austria", "Steiermark"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/17491/images/17152/IMG_0644__05764.1772585411.500.500.png?c=2}
  - Cuvee Jean-Louis Blanc de Blanc 750ml | $20.99 | stock=12 | https://www.marquis-wines.com/cuvee-jean-louis-blanc-de-blanc-750ml/ | {sku=1016190; in_stock=True; categories=["Sparkling", "Champagne & Bubbles", "Happy Mother's Day"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19899/images/15656/2025-01-24_12.51.12__53668.1738004392.500.500.png?c=2}
  - Henkell Piccolo 3 Pack 200ml | $18.99 | stock=7 | https://www.marquis-wines.com/henkell-piccolo-3-pack/ | {sku=9118; in_stock=True; categories=["Sparkling", "Germany"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7094/images/3880/cq5dam.web.1280.1280__27143.1604339624.500.500.jpg?c=2}
  - Wolfberger Cremant D'Alsace 750ml | $34.99 | stock=13 | https://www.marquis-wines.com/wolfberger-cremant-dalsace-750ml/ | {sku=710111; in_stock=True; categories=["Sparkling", "Alsace", "France", "Crémant"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/13920/images/9409/Wolfberger-Cremant__90666.1606168038.500.500.jpg?c=2}

#### search_legacy_liquor_store_tool (status=ok, 20 results)
  - 33 Acres of Pacific Juniper & Sea Buckthorn Adaptogenic Sparkling Water | $11.19 | stock=3 | https://www.legacyliquorstore.com/product/non-alcoholic/33-acres-of-pacific-juniper-sea-buckthorn-adaptogenic-sparkling-water-4-x-355ml | {slug=33-acres-of-pacific-juniper-sea-buckthorn-adaptogenic-sparkling-water-4-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["Non-Alcoholic"]}
  - Ruffino Sparkling (Non Alcoholic) | $23.63 | stock=4 | https://www.legacyliquorstore.com/product/non-alcoholic/ruffino-sparkling-non-alcoholic-1-x-750ml | {slug=ruffino-sparkling-non-alcoholic-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Italy; in_stock=True; tags=["Non-Alcoholic"]}
  - Glimmer Sparkling Blanc de Blanc (Non Alcoholic) | $10.67 | stock=24 | https://www.legacyliquorstore.com/product/non-alcoholic/glimmer-sparkling-blanc-de-blanc-non-alcoholic-1-x-250ml | {slug=glimmer-sparkling-blanc-de-blanc-non-alcoholic-1-x-250ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["Non-Alcoholic", "Wine"]}
  - Church & State Sparkling Pinot Gris | $31.33 | stock=13 | https://www.legacyliquorstore.com/product/wine/church-state-sparkling-pinot-gris-1-x-750ml | {slug=church-state-sparkling-pinot-gris-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}
  - Salt Spring Island Mead Soured Cherry Sparkling Draft | $17.91 | stock=3 | https://www.legacyliquorstore.com/product/wine/salt-spring-island-mead-soured-cherry-sparkling-draft-1-x-750ml | {slug=salt-spring-island-mead-soured-cherry-sparkling-draft-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "other"]}
  - Edenvale Sparkling Cuvee 200ml (Non-Alc) | $7.09 | stock=23 | https://www.legacyliquorstore.com/product/non-alcoholic/edenvale-sparkling-cuvee-200ml-non-alc-1-x-200ml | {slug=edenvale-sparkling-cuvee-200ml-non-alc-1-x-200ml; is_staff_pick=False; is_new_arrival=False; country=Australia; in_stock=True; tags=["Non-Alcoholic"]}
  - Edenvale Sparkling Rose 200ml (Non-Alc) | $7.09 | stock=23 | https://www.legacyliquorstore.com/product/non-alcoholic/edenvale-sparkling-rose-200ml-non-alc-1-x-200ml | {slug=edenvale-sparkling-rose-200ml-non-alc-1-x-200ml; is_staff_pick=False; is_new_arrival=False; country=Australia; in_stock=True; tags=["Non-Alcoholic", "Wine"]}
  - Mayhem Sparkling Rose Can | $9.58 | stock=2 | https://www.legacyliquorstore.com/product/wine/mayhem-sparkling-rose-can-1-x-250ml | {slug=mayhem-sparkling-rose-can-1-x-250ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}
  - Terravista Sparkling Albarino (Washington) | $32.82 | stock=3 | https://www.legacyliquorstore.com/product/wine/terravista-sparkling-albarino-washington-1-x-750ml | {slug=terravista-sparkling-albarino-washington-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}
  - Leitz Sparkling Rose (Non Alcoholic) | $5.61 | stock=27 | https://www.legacyliquorstore.com/product/non-alcoholic/leitz-sparkling-rose-non-alcoholic-1-x-250ml | {slug=leitz-sparkling-rose-non-alcoholic-1-x-250ml; is_staff_pick=False; is_new_arrival=False; country=Germany; region=Rheingau; in_stock=True; tags=["Non-Alcoholic", "Wine"]}
  - Zeno Sparkling Rose (Non Alcoholic) | $26.85 | stock=11 | https://www.legacyliquorstore.com/product/non-alcoholic/zeno-sparkling-rose-non-alcoholic-1-x-750ml | {slug=zeno-sparkling-rose-non-alcoholic-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Spain; in_stock=True; tags=["Non-Alcoholic", "Wine"]}
  - Narrative XC Method Sparkling | $22.39 | stock=5 | https://www.legacyliquorstore.com/product/wine/narrative-xc-method-sparkling-1-x-750ml | {slug=narrative-xc-method-sparkling-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}
  - Glimmer Sparkling Blanc de Blancs (Non-Alcoholic) | $26.95 | stock=7 | https://www.legacyliquorstore.com/product/non-alcoholic/glimmer-sparkling-blanc-de-blancs-non-alcoholic-1-x-750ml | {slug=glimmer-sparkling-blanc-de-blancs-non-alcoholic-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["Non-Alcoholic", "Wine"]}
  - Sidney Sparkling Rose 7% | $19.78 | stock=6 | https://www.legacyliquorstore.com/product/wine/sidney-sparkling-rose-7-1-x-750ml | {slug=sidney-sparkling-rose-7-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}
  - Sidney Sparkling Pinot Grigio 7% | $19.78 | stock=4 | https://www.legacyliquorstore.com/product/wine/sidney-sparkling-pinot-grigio-7-1-x-750ml | {slug=sidney-sparkling-pinot-grigio-7-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}
  - Leitz Sparkling Riesling (Non Alcoholic) | $5.61 | stock=8 | https://www.legacyliquorstore.com/product/non-alcoholic/leitz-sparkling-riesling-non-alcoholic-1-x-250ml | {slug=leitz-sparkling-riesling-non-alcoholic-1-x-250ml; is_staff_pick=False; is_new_arrival=False; country=Germany; region=Rheingau; in_stock=True; tags=["Non-Alcoholic", "Wine"]}
  - Kizuna Sparkling Sake | $29.85 | stock=7 | https://www.legacyliquorstore.com/product/sake/kizuna-sparkling-sake-1-x-500ml | {brand=Kizuna Sake; slug=kizuna-sparkling-sake-1-x-500ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["sake", "sake", "sparkling"]}
  - Mt. Boucherie Estate Winery Mt. Bubbles Sparkling Wine | $29.84 | stock=5 | https://www.legacyliquorstore.com/product/wine/mt-boucherie-mt-bubbles-sparkling-1-x-750ml | {slug=mt-boucherie-mt-bubbles-sparkling-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "champagne & sparkling", "BC sparkling"]}
  - Jacob's Creek Sparkling Moscato 1.5L | $27.58 | stock=2 | https://www.legacyliquorstore.com/product/wine/jacobs-creek-sparkling-moscato-1-5l-1-x-1-5l | {brand=Moscato; slug=jacobs-creek-sparkling-moscato-1-5l-1-x-1-5l; is_staff_pick=False; is_new_arrival=False; in_stock=True; tags=["wine", "champagne & sparkling"]}
  - Freixenet Sparkling Rose | $28.25 | stock=31 | https://www.legacyliquorstore.com/product/wine/freixenet-sparkling-rose-1-x-750ml | {brand=Freixenet; slug=freixenet-sparkling-rose-1-x-750ml; is_staff_pick=False; is_new_arrival=False; in_stock=True; tags=["wine", "champagne & sparkling", "prosecco"]}

````

</details>

### Latency

- 147.88s
