# DISC-002 — DISC

_Notes:_ Open-ended 'best' — should combine reputation + price + availability

- Thread ID: `eval-DISC-002-9dc43b97`
- Turns: 1

---
## Turn 0

### Query

> What's the best BC red wine I can buy for under $50?

### Tool Calls (in order)

1. `sommelier_agent_tool` args={"request": "What are some of the best, highly-rated BC red wines (such as Pinot Noir, Syrah, Cabernet Franc, or Bordeaux-style blends) under $50? Please provide tasting notes, scores, or critic reviews if available."}
2. `sourcing_agent_tool` args={"request": "BC red wine under $50 in stock in Vancouver stores. Looking for top-rated or highly popular options like Pinot Noir, Syrah, Cabernet Franc, or Meritage blends."}

### Final Response

```markdown
Here are some of the best, highly-rated British Columbia red wines under $50 that are currently in stock at Vancouver-area retailers. These selections span elegant Pinot Noirs, savory Syrahs, structured Cabernet Francs, and rich red blends, complete with critic scores, tasting notes, and direct purchase links.

---

### 🍷 Pinot Noir

#### **Meyer Family Vineyards Okanagan Valley Pinot Noir**
* **The Wine:** Sourced from multiple premium vineyard sites across the Okanagan, Meyer Family Vineyards is widely considered one of Canada’s premier producers of Burgundian-style Pinot Noir.
* **Critic Scores & Tasting Notes:** 
  * **2023 Vintage:** Awarded **91 points** by *BC Wine Trends*, which praised its bright acidity and smooth, velvety layers of red cherry, wild strawberry, and forest floor. ([Source: BC Wine Trends](https://bcwinetrends.com))
  * **2022 Vintage:** Rated **90 points** by Anthony Gismondi (*Gismondi on Wine*), who highlighted it as an "eminently drinkable" bargain featuring juicy cherry and raspberry fruit with no heavy oak influence. ([Source: Gismondi on Wine](https://gismondionwine.com))
* **Where to Buy in Vancouver:**
  * **Sutton Place Wine Merchant:** $33.49 (27 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4298314-meyer-family-vineyards-okanagan-valley-pinot-noir)
  * **Marquis Wine Cellars:** $34.99 (12 in stock) | [Buy at Marquis](https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/)

---

### 🍇 Syrah

#### **Le Vieux Pin Syrah "Cuvée Violette"**
* **The Wine:** An elegant, Northern Rhône-inspired Syrah from the South Okanagan, known for its floral, savory, and peppery complexity rather than heavy, jammy fruit.
* **Critic Scores & Tasting Notes:**
  * **2022 Vintage:** Awarded **92 points** by Anthony Gismondi (*Gismondi on Wine*), who praised its lively profile of violet, blueberry, smoked meat, and sagebrush, all balanced by silky tannins and fresh acidity. ([Source: Gismondi on Wine](https://gismondionwine.com))
* **Where to Buy in Vancouver:**
  * **Marquis Wine Cellars:** $46.99 (25 in stock) | [Buy at Marquis](https://www.marquis-wines.com/le-vieux-pin-2022-cuvee-violette-syrah-750ml/)

---

### 🌿 Cabernet Franc

#### **Burrowing Owl Estate Winery Cabernet Franc**
* **The Wine:** A robust, structured, and spicy Cabernet Franc from one of the South Okanagan's most consistent and beloved estate wineries.
* **Critic Scores & Tasting Notes:**
  * **2022 Vintage:** Awarded **90 points** by Anthony Gismondi (*Gismondi on Wine*), noting bright black raspberry, red plum, savory desert scrub, and roasted coffee. He suggested its firm, gritty tannins make it a perfect candidate for a hearty cut of beef. ([Source: Gismondi on Wine](https://gismondionwine.com))
* **Where to Buy in Vancouver:**
  * **Marquis Wine Cellars:** $42.99 (19 in stock) | [Buy at Marquis](https://www.marquis-wines.com/burrowing-owl-2022-cabernet-franc-750ml/)

#### **Phantom Creek Estates Estate Cabernet Franc**
* **The Wine:** Sourced from premium estate vineyards on the Black Sage Bench and Golden Mile Bench, this is a classic, full-bodied South Okanagan Cabernet Franc.
* **Tasting Notes:** Highly popular with a **4.6/5 consumer rating** on BC Liquor. It delivers ripe black and red bramble berry notes with a lingering sagebrush finish.
* **Where to Buy in Vancouver:**
  * **BC Liquor Stores:** $41.99 (1,603 available across 117 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/90203)

#### **Bartier Bros Cabernet Franc**
* **The Wine:** Sourced from the Cerqueira vineyard in the heart of the Black Sage zone, this is a highly distinctive, terroir-driven expression of the grape.
* **Tasting Notes:** Rated **4.4/5** by consumers. It features black and blue fruits, sturdy tannins, and a classic desert-scrub character.
* **Where to Buy in Vancouver:**
  * **BC Liquor Stores:** $29.99 (620 available across 56 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/993139)

---

### 🍁 Meritage & Red Blends

#### **La Stella "Fortissimo"**
* **The Wine:** A Tuscan-inspired red blend (primarily Merlot, Cabernet Sauvignon, Cabernet Franc, and Sangiovese) that offers fantastic structure, depth, and savory complexity.
* **Where to Buy in Vancouver:**
  * **Marquis Wine Cellars:** $40.99 (15 in stock) | [Buy at Marquis](https://www.marquis-wines.com/la-stella-2022-fortissimo-750ml/)

#### **Phantom Creek "Quartz and Yarrow" Sustainable Red**
* **The Wine:** A rich, full-bodied blend of Cabernet Sauvignon, Merlot, Cabernet Franc, and Syrah sourced from sustainably farmed vineyards across the Okanagan Valley.
* **Tasting Notes:** Rated **4.6/5** by consumers. It features fresh, fruit-forward aromas of cherry, black currant, plum, and vanilla, backed by ripe tannins and an opulent texture.
* **Where to Buy in Vancouver:**
  * **BC Liquor Stores:** $35.99 (428 available across 45 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/194330)
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
    "SUPPORTED": 17,
    "GENERAL_KNOWLEDGE": 0,
    "NOT_IN_EVIDENCE": 0,
    "CONTRADICTED": 0
  },
  "correctness_rationale": "The agent accurately extracted and synthesized all pricing, stock, rating, and tasting note information from the provided tool results without any hallucinations.",
  "issues": [],
  "strengths": [
    "Excellent formatting with clear categorization by grape varietal.",
    "Provides highly actionable purchase links, prices, and stock levels for every recommendation."
  ],
  "parse_error": false
}
```

### Claim Verdicts

| Label | Claim | Evidence quote |
|---|---|---|
| SUPPORTED | Meyer Family Vineyards Okanagan Valley Pinot Noir 2023 Vintage was awarded 91 points by BC Wine Trends. | **2023 Vintage:** Rated **91 Points** by *BC Wine Trends* |
| SUPPORTED | Meyer Family Vineyards Okanagan Valley Pinot Noir 2022 Vintage was rated 90 points by Anthony Gismondi. | **2022 Vintage:** Rated **90 Points** by Anthony Gismondi (*Gismondi on Wine*) |
| SUPPORTED | Meyer Family Vineyards Okanagan Valley Pinot Noir is available at Sutton Place Wine Merchant for $33.49 with 27 in stock. | **Sutton Place Wine Merchant:** $33.49 (27 in stock) \| [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4298314-meyer-family-vineyards-okanagan-valley-pinot-noir) |
| SUPPORTED | Meyer Family Vineyards Okanagan Valley Pinot Noir is available at Marquis Wine Cellars for $34.99 with 12 in stock. | **Marquis Wine Cellars:** $34.99 (12 in stock) \| [Buy at Marquis](https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/) |
| SUPPORTED | Le Vieux Pin Syrah 'Cuvée Violette' 2022 Vintage was awarded 92 points by Anthony Gismondi. | **Anthony Gismondi (Gismondi on Wine, May 2024) – 92 Points:** |
| SUPPORTED | Le Vieux Pin Syrah 'Cuvée Violette' is available at Marquis Wine Cellars for $46.99 with 25 in stock. | **Marquis Wine Cellars:** $46.99 (25 in stock) \| [Buy at Marquis](https://www.marquis-wines.com/le-vieux-pin-2022-cuvee-violette-syrah-750ml/) |
| SUPPORTED | Burrowing Owl Estate Winery Cabernet Franc 2022 Vintage was awarded 90 points by Anthony Gismondi. | **Score: 90/100** – Anthony Gismondi, *Gismondi on Wine* (Tasted Dec 2024) |
| SUPPORTED | Burrowing Owl Estate Winery Cabernet Franc is available at Marquis Wine Cellars for $42.99 with 19 in stock. | **Marquis Wine Cellars:** $42.99 (19 in stock) \| [Buy at Marquis](https://www.marquis-wines.com/burrowing-owl-2022-cabernet-franc-750ml/) |
| SUPPORTED | Phantom Creek Estates Estate Cabernet Franc has a 4.6/5 consumer rating on BC Liquor. | **Phantom Creek Estates Estate Cabernet Franc** (Rating: 4.6/5) |
| SUPPORTED | Phantom Creek Estates Estate Cabernet Franc is available at BC Liquor Stores for $41.99 with 1,603 available across 117 stores. | **BC Liquor Stores:** $41.99 (1,603 available across 117 stores) \| [Buy at BC Liquor](https://www.bcliquorstores.com/product/90203) |
| SUPPORTED | Bartier Bros Cabernet Franc has a 4.4/5 consumer rating. | **Bartier Bros Cabernet Franc 2022** (Rating: 4.4/5) |
| SUPPORTED | Bartier Bros Cabernet Franc is available at BC Liquor Stores for $29.99 with 620 available across 56 stores. | **BC Liquor Stores:** $29.99 (620 available across 56 stores) \| [Buy at BC Liquor](https://www.bcliquorstores.com/product/993139) |
| SUPPORTED | La Stella 'Fortissimo' is a blend primarily of Merlot, Cabernet Sauvignon, Cabernet Franc, and Sangiovese. | **La Stella Fortissimo 2023** (Merlot, Cab Sauv, Cab Franc, Sangiovese) |
| SUPPORTED | La Stella 'Fortissimo' is available at Marquis Wine Cellars for $40.99 with 15 in stock. | **Marquis Wine Cellars:** $40.99 (15 in stock) \| [Buy at Marquis](https://www.marquis-wines.com/la-stella-2022-fortissimo-750ml/) |
| SUPPORTED | Phantom Creek 'Quartz and Yarrow' Sustainable Red is a blend of Cabernet Sauvignon, Merlot, Cabernet Franc, and Syrah. | **Phantom Creek Quartz and Yarrow Sustainable Red 2016** (Cab Sauv, Merlot, Cab Franc, Syrah) |
| SUPPORTED | Phantom Creek 'Quartz and Yarrow' Sustainable Red has a 4.6/5 consumer rating. | **Phantom Creek Quartz and Yarrow Sustainable Red 2016** (Cab Sauv, Merlot, Cab Franc, Syrah) (Rating: 4.6/5) |
| SUPPORTED | Phantom Creek 'Quartz and Yarrow' Sustainable Red is available at BC Liquor Stores for $35.99 with 428 available across 45 stores. | **BC Liquor Stores:** $35.99 (428 available across 45 stores) \| [Buy at BC Liquor](https://www.bcliquorstores.com/product/194330) |

### Evidence shown to judge

_2 tool messages, 105793 chars (budget 2000000)_

<details><summary>Show evidence</summary>

````markdown
### sommelier_agent_tool (status=ok)
**Sub-agent synthesis:**
Here are some of the most highly regarded BC red wines that generally fit your target style and budget, along with some fantastic red-wine-adjacent options across other beverage categories to explore. 

### **Wine: Top BC Red Picks**

**1. Meyer Family Vineyards Okanagan Valley Pinot Noir**
Meyer Family Vineyards is widely considered one of Canada’s premier producers of Burgundian-style Pinot Noir. Their regional Okanagan Valley blend is an exceptional, approachable representation of the grape.
*   **Critic Score & Notes:** *BC Wine Trends* awarded the **2023 vintage 91 points**, praising its bright acidity and smooth, velvety layers of red cherry, wild strawberry, and forest floor. ([Source: BC Wine Trends](https://bcwinetrends.com))

**2. Le Vieux Pin Syrah "Cuvée Violette"**
If you enjoy elegant, Northern Rhône-inspired Syrah, this South Okanagan producer is a benchmark. The Cuvée Violette is known for its floral and savory characteristics rather than heavy, jammy fruit.
*   **Critic Score & Notes:** Anthony Gismondi (*Gismondi on Wine*) awarded the **2022 vintage 92 points**, highlighting its lively profile of violet, blueberry, smoked meat, and sagebrush, all balanced by silky tannins and fresh acidity. ([Source: Gismondi on Wine](https://gismondionwine.com))

**3. Burrowing Owl Estate Winery Cabernet Franc**
Burrowing Owl produces some of the most consistent and beloved robust reds in the South Okanagan. Their Cabernet Franc is a fantastic expression of the varietal's spicy, structured nature.
*   **Critic Score & Notes:** Anthony Gismondi scored the **2022 vintage 90 points**, noting bright black raspberry and red plum alongside savory desert scrub and roasted coffee. He suggested its firm tannins make it a perfect candidate for a hearty cut of beef. ([Source: Gismondi on Wine](https://gismondionwine.com))

**4. Laughing Stock Vineyards "Portfolio"**
Sourced from the Naramata Bench, Portfolio is one of British Columbia's definitive Bordeaux-style blends (typically leading with Merlot and Cabernet Sauvignon). 
*   **Critic Score & Notes:** For its 20th-anniversary **2022 vintage**, David Lawrason (*WineAlign*) awarded it **91 points**, praising its complex mix of red and black plum, cassis, sage, and a dark chocolate finish. ([Source: Laughing Stock Vineyards](https://laughingstock.ca))

---

### **Beyond Wine: BC Red-Adjacent Pairings**
*To round out your options, here are some exceptional local BC beverages in other categories that share the dark fruit, oak, or savory complexity of a great red wine.*

**Beer: Strange Fellows Brewing "Reynard" Oud Bruin**
If you appreciate the complex, tart, and fruity notes of a Pinot Noir, this limited-release Flemish-style sour brown ale from Vancouver is a must-try. Blended from French oak barrel-aged vintages, it offers a delicate malt backbone with rich notes of cherry, leather, oak, and vanilla. ([Source: Strange Fellows Brewing](https://strangefellowsbrewing.com))

**Spirit: Shelter Point Distillery "Double Barreled" (Pinot Noir Finish)**
For a spirit that bridges the gap between whisky and wine, this Vancouver Island single malt is finished in French oak barrels that previously held Quails' Gate Pinot Noir. Whisky critic Mark Kaufmann (*Whisky Whistle*) scored it **92 points**, noting its elegant sweetness, light tartness, and a chocolatey raspberry finish. ([Source: Shelter Point Distillery](https://shelterpoint.ca))

**Sake: Artisan SakeMaker "Osake Fraser Valley Junmai Renaissance"**
Crafted on Granville Island using 100% BC-grown sake rice, this sake is specifically styled to appeal to wine lovers. It features a rich, savoury profile with pronounced acidity that pairs beautifully with charcuterie or roasted meats—much like a good, earthy red wine. ([Source: Artisan SakeMaker](https://artisansakemaker.com)) 

*(Note: Our Sourcing specialist will follow up with exact pricing, vintage availability, and links to purchase these recommendations!)*

#### search_web_grounded_tool (status=ok, 19 results)
Search answer: **Meyer Family Vineyards** (based in Okanagan Falls, BC) is widely recognized as one of Canada's premier producers of Burgundian-style Pinot Noir. Local and international critics consistently award high scores to their portfolio:

### 1. Okanagan Valley Pinot Noir (Regional Blend)
This approachable, value-driven bottling is sourced from multiple vineyard sites across the Okanagan (including Naramata, Kaleden, Osoyoos, and Okanagan Falls).
* **2023 Vintage:** Rated **91 Points** by *BC Wine Trends*, which highlighted its exceptional value, bright acidity, and smooth, velvety layers of red cherry, wild strawberry, and forest floor.
* **2022 Vintage:** Rated **90 Points** by Anthony Gismondi (*Gismondi on Wine*), who praised it as an "eminently drinkable" bargain featuring juicy cherry and raspberry fruit with no heavy oak influence. 
* **2021 Vintage:** Received **88 Points** from Anthony Gismondi and Treve Ring (*Gismondi on Wine*), noted for its fleshy, earthy style and black cherry core.

### 2. McLean Creek Road Vineyard Pinot Noir (Estate Single Vineyard)
Sourced from the estate's home vineyard in Okanagan Falls, which features glacial gravel and sandy loam soils.
* **2023 Vintage:** Rated **91 Points** by BC wine authority John Schreiner. Geoffrey Moss MW also praised the vintage, noting its sappy dark cherry, black raspberry, and well-integrated toasted oak.
* **2022 Vintage:** Awarded **91 Points** at the *Decanter World Wine Awards*.
* **2019 Vintage:** Rated **92 Points** by *WineAlign*.

### 3. "Old Block" Pinot Noir
This single-vineyard bottling comes from a one-acre plot of the estate's original 1994 plantings.
* **2022 Vintage:** Highly acclaimed, earning **94 Points** at the 2024 *Decanter World Wine Awards* and **93 Points** (Platinum Medal) at the 2024 *National Wine Awards of Canada*. Anthony Gismondi and Treve Ring (*Gismondi on Wine*) rated it **92 Points**, describing it as silken and smooth with dark plum, black raspberry, and pipe tobacco notes.

### 4. Micro Cuvée Pinot Noir
Winemaker Chris Carson's premium, small-lot barrel selection of the finest estate fruit.
* **2022 Vintage:** Rated **94 Points** by *BC Wine Trends*, which described it as a rich, concentrated, and beautifully constructed wine with expressive black cherry, raspberry, and vanilla notes.
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqyOIb9OYCzwMhlxn8pwqwdnDfFT2ePgb9OMl-hZFYwU2Rw3KXfDdHR5SzTR2rWg04Oa6VUq66CeycppePoEChNr8Gph9nqUCDaHwiIYsLIw==): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-HnhW61wvdjiJ_lHGLvtMOxHfzfo0ijsFaqfoQg7D6p9jxWdsltpPlpjVGVIZnzaw1hpWQIMwWcFHHsXwMBE2yKl_fWJLzG49hDEAOiReHzJOdAQw7nhxa17b-ZXr0jwsTMpfqM0=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJ7lYnOaJg6aulDdraGGv-PdW9GpqFOVd4MuP9XsWft77-xR2elUPz6TEZl6xCOOfzzUOryZHmyw1XRASqHWKg9VpFQe69YKgxSzpbhj6o9NPlMQjKMTrmkIFFohniqFHS-WMd6lSQJib4KP8OD5-1YwyZpT7phgpO2ImoYcEAlEl4fI-JTfIu17d1qLheSY6KmveH_yRNbW0IqA==): 
  - [mywinepal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGR6jJzIEP3uXx-12gbT2mhG2X0PRuMtj0gkhdiMwlSBycxRvBfQY9S6-5zJGuw_JSffUNmAmtyNhrzw8dlo9tYobvM7EPMwYKeNgmiub9wAQmz2UO7DEBhcNs0aQ11XoPW9hYHKMvNZSzAultXu24TDAXtGq5TeVCVIAik4cYqYckQKtvE6ToOSVoawX10oSM=): 
  - [bcwinetrends.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbnnj0mTZzVTibLZG4VnEYNHm4C4HJclSbScKXjSgFWFongu6H8AnucjHyQvoVFpJwvLrcAgrSk255Maed_kKGWT0rk_YaH5VVCyf0sZWxJeWZN4j_qIiYc4BoOimYZgUT01I8hihfz4B7ywV9GCHPp2l61-HOFMzBGn83TbE9XI6fc0dVwRa9Dtmin7G4JmD24Z31og==): 
  - [heavenlyvines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZSVroemelRUVW7CYuJLx6C3L9x0QLFIeVR7zah_yfHJEWiTB0BfWmOyuBGc03He9e7N0kPadwu4LctsQ22ScZvtuPPvizaEWQesTsm3VXvlzKFumM6xRmoZzmgzpzLgsVzrRdMqG2_oM4WpmGa0r5KNtMQeB_ooPvk-MjgXSZJuA=): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPMmUTXDc1XqrLxhaFwTRsl6dlbin2_C97z1fgZ5I29oN5kZ5cVKBWDFv02nRvb01h7Q3nFG_H2r_GjN6szMYGYZueOGocmozL8yN7xsx85uTXmwVLLhA8LOuSXlYnesecVydAks2Fn_cb_WKY55xtqzBAvgQuMuB3hX82O1iv9O-iviT6cByQ5ec5dw==): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEASGIvyy1Ab6lzCVdJ7qUubvUaBJKh_iAb8zZxCLpsNwi8rUG0jd7hLdmC4TwEA2CD24CIKv4Z2WdVabGvXI6TH4ACRMd69NkpCiFBUGHeqCKmlqAeJ0Eq6t8_OPto-5mSvNPr0qRFYH7CSY7UgYS91evLJ6dSThz_e0QK8xZn4dC4fsZbU17-p2yIH_R7SJFI5sp-mk6C_iqNgN4BtTq4Z3ukehMdGBhk9mopogvrgAz_81UTytwX): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEUnwUawi-o1FC7QCnkugHuTvkhLSeTpv71A9ZB1E2H2nTo4UuZnipqC3fs2J6fzriswyacf7P4TRbZP_xPomb9Q6_y31rJj-Bs7JPIIkw0jI246WM4yRthb3efoHWwgyV6TZ8VaEtjCR1kSwlLnQeKt0x44UKbokPyUa0lr0oSzORpXt4U_kD): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH0Q7D0ogmQHlf4NHE9UmcdVForRx2JimTMzJ5OerOObvSlgykZ5L5kf7U5r8Fa1ls-V6ik0OFEemf9-TQpgUQRTWXS8i33om65eYvDj4TmX4q-o0slvzZEb7VvInmPElI8EsGkxz-XsllbGv72uJEPkZ7z8GpeI8=): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQILAslpmh8K9_cmG-khQk5g4vpncz7AwVyGsZAWE9wYiJuXQJZTWvBfePh1P1L8GlAXXAJ46XHV-mEJK4VIqMLO438eg0BYuyvAWk3-99ZPfMo3h_fA8NTeHbLeaoJyWMyGSeq2258jythoIiyCjhX_7dQ1YYl-A=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHstQAe8DlZc1JLrsF0BiQ5oyGfDwgc2_y9sFcf8v_ScFCUflj2JlpAjXJgTc5jwa4bImfA0MC3Cw_jAiwWUKEhLP6VWJqmA3ECYPBJOB2TVeS8e3831rGDm3ohJBTwL2l93HYn6PqevbVBYN1YDaPCs_8WyHvFeoMbGL9G1eWmBCUW5YoqBCHOsvoBQyOJUWAIF3sIdB-ZG4Q9dx1e0uNMjetV1VUjFnooGbo8BhHl5NBciQ==): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHfOET5KrGbh-xk1xRt26KwMxawiDbADgH7hBKs3ntTA5_QnaHpd3T68Cv-idtlRrC6fuFwSqnvffZUE3P9RdikiZC8ZlM7QmD74g-4L02nA==): 
  - [npwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSrJe0s7PJPwxSyU7vLCCt8wBMe6ib0Uhf0TEBTCeWyn8FJWbS_oN8PZVazYPjYQBeSQOAvA98u6aMmhOLbuKDHTzILooNUXzbAVQBRh0ph0taTI6WlJX_4qgDakKSbP625tHQXPPHOewqoE4SFfQ1DxLD17yoEzuwfYBfKUopgDotDeTH): 
  - [kensingtonwinemarket.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJTorBZ7Rh91KLiwq2wtytX8A4DmdMNT9KEiaLRo8pijQsEGs9Cc0TF7RNG4OF4g_gfNedXic1ZXusTwn1jPEpG7hzRcxLfcW4rs63dPQzsY8dtMxftT-zWMWiIIEKZfaCcduaatHWoRjWZM_ZjDhGa5XjDK-olgkxpchyAeptf9kYoTu4t9qEUQ==): 
  - [bcwinetrends.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc1Cpgh7eL-jLrhLq7JKpe7uBCSH4XP7gIlpV5jD4n8Bc4mUN3_EHiBuSeqOho1w-VVM-9OftP4CyRMbI7hAKTsOh3rKAsFLEwQy_8WDEQkq5JB6caQ4Ndf7PXKVFr6ri1bLsQqDmkSz_FOhu_NSHVce8pN3AofHLPQb580LZyX59UayjRF2QprpUZZilYfgLYaMM=): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnb47DDhWEnKnnqeGBmuyccU_cth_ig-bQPpq2TwDN-Kmt-wlh5QbTDlhIIjvh1Oai4gQ94WNmC4D9pkxCfnj_272yaT7SmBuSvxE9FFk3YFzMFQ2I4ZuALDYilxX2w9R4ctZkh0uc4VsLkckM8Og1pW46BoqJm2UPF4tC-FMzwaeh-ujcdMKTfFvQMzU_YKjaHX5a0e0g0R3uEB4XnNALms9nQe_fElXgD4QGh2aMK8VP1QxMTAkhHA10ZHvL): 
  - [mfvwines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXEmoUWh_eBaurZ_4N0aPdxOZ5JIUj-rTdJlhLA4rbwPN3rl0gG7qV0l2WpMUllOYDI2DcXZfbmsaNqYy3sLGumj7na4udnh5GwG6UBqHcHu4MS9ZbhEhWH5l2Qa_1A0MwPPuQzpTyTqXjYCsEfIT2xkYxt_xAdA==): 
  - [mywinepal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlfPrBh6DcYQLAg8bWsxLlc7l-5PIL7VqCAcFF3VChnG6gNpvfJbA7KhMCrhhOpNhRPVNx8SS4_JflVXZqMoBG1k6ncpWs7aSYsDsnFm9fEnUPU4Z5HpdYWwtozI-S1cbT63xmb7r5B4_ILAhTmYkrU0uHkdKf98-lqpi6g4hY2jJZmJ5nlAr4wjt0xKV11ro=): 

#### search_web_grounded_tool (status=ok, 8 results)
Search answer: **Le Vieux Pin Syrah Cuvée Violette** is highly regarded in the British Columbia wine market, known for showcasing the elegant, floral, and Northern Rhône-inspired side of South Okanagan Syrah. 

Review scores and tasting summaries from prominent BC and Canadian wine critics include:

### **2022 Vintage**
* **Anthony Gismondi (Gismondi on Wine, May 2024) – 92 Points:** Gismondi praised the wine as a complete and lively Syrah, highlighting its classic notes of violet, blueberry, meat, licorice, and sagebrush, balanced by silky tannins and fresh acidity.
* **Treve Ring (Gismondi on Wine, Sept 2024) – 92 Points:** Ring noted the wine's poise and delicacy, describing a medium-bodied profile filled with fragrant violets, wild blueberries, blackberries, and a peppery finish.

### **2019 Vintage**
* **BC Wine Trends (April 2021) – 94 Points:** The review highlighted a full-bodied, fruit-forward style with beautiful aromas of dark fruit and violets, leading to a palate of mixed berries, licorice, and pepper.

### **2018 Vintage**
* **Natalie MacLean (June 2021) – 92/100:** MacLean described it as an elegant, medium-bodied, and refined Syrah featuring notes of violets, ripe cherry, savory herbs, and pepper.
* **Deborah Podurgiel (Certified Sommelier via Natalie MacLean, June 2021) – 93/100:** Podurgiel called it silky and elegant, noting fragrant violet, cherry, and plum aromas with a peppery finish.

### **Older Vintages**
* **2016 Vintage – Daenna Van Mulligen (WineDiva.ca):** Ranked **#1** in a blind tasting, Van Mulligen described it as a classic, juicy, sweet-and-savory wine with notes of berry compote, vanilla, licorice, and white pepper.
* **2014 Vintage – John Schreiner (April 2016) – 91 Points:** Schreiner noted classic black pepper on the nose, accompanied by flavors of fig, plum, black olives, and dark chocolate.
* **2012 Vintage – Daenna Van Mulligen (WineDiva.ca, August 2014) – 5/5 Stars:** Van Mulligen called the wine feminine, stylish, and spicy, highlighting aromas of blackberry jam, Turkish coffee, and crushed violets.
* **2012 Vintage – John Schreiner (October 2014) – 90 Points:** Schreiner described this vintage as softer and juicier than the winery's Cuvée Classique, showing cherry and blackberry flavors.
  - [levieuxpin.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlYeh8jMcR6fftucCIxv8bxODExydfGCdHfWTQ7G0LoZx2ktm1lkxeIiCyptd3X1wyXxKr3mxPeGkAnRi_qQnQF-_GYlSqDV-moDy1DP7Eztd_iFhfN2Ipr3SzlXtdVmU=): 
  - [levieuxpin.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6NnASuL_m_Tg1k2wED3d-N5DzzIVZ11HHQ7EDHS1aRf5QlaZgOsFC4q7VcisUM6iA4uyysJTxceAl3LqxvRkWLIHdfPaSlHpGNLwjp_yWInCz57djAFt-1gczIK5t-hBM0m3G-QSGCQdXNpXnJBERKkoT): 
  - [bcwinetrends.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDhWSzgrpXgaL-3JI0_WvnO5RL0ArsHijp27CrI2dWFozrVDhZbiD7mdnVCjZtsCgMX-kHqW3oB4QX66-GcTfQS579KA3TA28RZASvwvRe8AUGKJZbZPj2Idt3qcnSBAkJqEe3Wonph7f8ujiAKdzZuY0UJln36q2Rl5AFIIp47ixxKT8ipIrvNU-5): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlpK-RdE-EYQpxXjsi8YFgjFsCLvuG9nIZ8LC3DhutBb_tJAtg6ogCxL_bozSz9J61RdvHYJtbtTXUMttW8_1JuvrGP6fwxK3CfDQisbpVqdjupsyli9sZNPJ5S9DxjSJoaTJc6WN9X7YMil2l4hsxaMqlFU_bVpaUlmlJTiP6_GvDIyxUqWaYf_5TUtZFzzG4lC8=): 
  - [winediva.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfG-m3pwFpxpFgrm-_yrA5Bb3OoO6FmiqQjWctW-yNtfBxukmG2h2gnk30NvFHSIIctZDss-Hta-k_l-67zUPjcScl2dwwssVCg1IbKyyTGm5Mihmamor8LOHlaCUGqOZhp04SG0h0GbfvAStGsp0QutaVbRY5yCULdjKtgMz5Q0HZr1J3P1B66ix9BRxXZoYdfrJb-UmsVRSeycel7sNoznAHfPYbeXVRETiqNRXJr18TpUJ0WHSSo0dQVPeAHwezxZn6IrprAEH1DaKzxNFFts2W12XbUsmv5ui1IHAZHlyLsEQQjdiHhgijEu6d66_9r0_2-7vambNk9BQpnjRhWO4jPc6IGAb_yJ-NH6qqzgMuxWN3AHDM4NytQim54bqmatbl1Hf_qS4vksPybLeGKt7w-62WjBmCsrKLRJWKfGMHeaPwSUZUDUKH-hj27m2tOa5ODG2T_fIAnP_JQq4omfi1): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOLtGUpVy3ImN5SRrfCrwyZ8mcFcNqW-ERehDslLEZhKtaHPTFqNuLkog6NW7XmiCxCf_Yk-gkqU48SUMoOHmot2jp0uFESZi74PIZx76Jedm5vKw2nbKjleOj4mV7XcDBYgAmvCzvSZm_QFlMhbxjAnbpTVADhAPFuygvLJnngUsF4hky7Fq-VeUSJ8StO1xi): 
  - [levieuxpin.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPL3sTNwG5M3cqZrbxq6c269Oxqe9balK6gqH2IfGDDKh1YzzvVzkNkTd_rYr6Nv1hRPOAStymBf8X9lzJQjU2qX_FL2nHw1IYC8arHpQMWxqCFRIZ_NqAdHqPCxqf_cMgC9o0DE9rEgAMf6zie8KF9uA=): 
  - [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW5IIwbaERMmG0U74J_v87WG3hZPXoczNKzMyFDyHUwQ_aOZ23FBUReuNVnaq9QfkpDPxWEnTSnScwuvN25-xUuLPmA7ThpY7GV7jnbrDYo8jCpUwf_gbB9zJPwbKMRXPeJwzfP33AZpzDP99ExF_VIFiCUvC7rK4IpSHZWdsqyA6SJEjwhjA7LvBeXyfNYw==): 

#### search_web_grounded_tool (status=ok, 8 results)
Search answer: **Burrowing Owl Estate Winery Cabernet Franc** is a highly regarded red wine from the South Okanagan Valley in British Columbia. Here is a summary of recent vintage reviews and scores from prominent critics relevant to the BC market:

### **2022 Vintage**
* **Score: 90/100** – Anthony Gismondi, *Gismondi on Wine* (Tasted Dec 2024)
  * **Review Summary:** Gismondi highlights this as a modern, fresh expression of the grape, showcasing bright black raspberry, red plum, and red currant fruit alongside savory desert scrub, roasted coffee, and five-spice. He notes that the wine is ripe and dense with firm, gritty tannins and a bitter cocoa finish, suggesting it needs some bottle age or a hearty cut of beef to soften.
* **Award:** Gold Medal – *WineAlign National Wine Awards of Canada* (June 2025)

### **2021 Vintage**
* **Score: 93/100** – Norm Roby, *Wine Review Online* (Tasted Jul 2025)
  * **Review Summary:** Roby praises this warm-vintage release as concentrated and complex, offering plum, cassis, light tobacco, and dried herbs. He describes the palate as big and smooth with gentle, structured tannins.
* **Anthony Gismondi's Review:** Gismondi notes a spicy, savory dark plum nose leading to a palate of cassis, blueberries, balsamic, and espresso, advising that it needs about five years to fully settle.
* **Awards:** Silver Medal – *International Wine & Spirit Competition* (April 2024); Silver Medal – *San Francisco International Wine Competition* (Dec 2023)

### **2019 Vintage**
* **Score: 90/100** – Anthony Gismondi, *Gismondi on Wine* (Tasted Mar 2022)
  * **Review Summary:** Gismondi describes this full-bodied wine as silky smooth, featuring flavors of black cherry, cedar, black raspberry, and cassis, accented by a smoky herbal note and ample, well-absorbed tannins.
* **Award:** Double Gold – *San Francisco International Wine Competition* (Nov 2022)

### **2018 Vintage**
* **Score: 91/100** – Natalie MacLean (Nov 2022)
  * **Review Summary:** MacLean characterizes this vintage as dry, juicy, and full-bodied, with a fragrant profile of spiced plum, cassis, blueberry, coffee, and savory herbs, backed by firm, fine tannins.
* **Score: 89/100** – Anthony Gismondi, *Gismondi on Wine* (Tasted Oct 2020)
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdSTIz-0mCiyjmmPZeBNZl9o1Yw7x0vxHo17E5krfqwZH0PjHN1NDWyffULxj-6YNT-2byY8jCEmlpRcRMtiCFo99y4VMnMC4SPk-4_Z7gJ-0uuLbeFFAhatQU4oA2HZ5HLFmbWNkCptCkiNrLtwU0zGPJtv15itAze13WHjbU7WUNFLT4vlLsrynk465lqLtzw0LVvmW-D8xMrfWwYHR8KFSp4M36FBurymzwO22DDjd17lMSdEvbpChGLcoejHMO): 
  - [gismondionwine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-8WADn9g_bR7lUViQZsiAigsdq3rvVQbwOI8MzPhXtxYudMgRDLlZc8ydPBKiDo0CJfw3jyrJbmC8JFXrXNu4mbJV0LAe4pgCK0M7Nd2yffphMAiyykQv9tg7OpPhqP1cRhghBagztuyRlFtvZv1_vAcPNuRYCfOdPvgbPa3cwz5P8nvInQbwJTfYarCCoRJ6ELNserrRAQ==): 
  - [marquis-wines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvJ9ZLRjZw789z9Y8GQdiMn-xyd5sdO0RmOV4Q9EezB7xLXaG4I6SuzgqdIPsPVx-xv1M9q5jGemZnjheUTB6F1iYpnK-08e89uAsBUMVI1M_im0hnFqiccg265StmPbB_7fll37PznD46fCNOzqu6myGZEFB7DxvLx-fODcJCMHI=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGrZFdyN7fcRrPgsD97lCT4RE5to8UCKAnt0mUZrMz-t4pmqtJg5SdRZ_UdJOqNzeSSRELiXrpZzR9VO7jYjGG_5eU796BtK6VN196pwC2IQLQdrxlvE3l0Z4PLztWcHx10Oamm9EdzP1dTvqs-1P5M5DRaEWoBBdFh-BE1fStkBpqTQr3L7lBqkVsCtKlycrv48RKkxP99tflSKZt9yiROSMkvyPjH9DJUgvO4_Ij6L5wenp1IJYqlcYXgmEq6mNT): 
  - [burrowingowlwine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgGngaU2MQsTCLKZ1MrCtujzQxR95eNdOFiUDWvcrqq2Cpixp6litEL3YQy8ELlkb9-pFJ6QROmnHwh-zef5poL2EuaWyWHDjsYA82IfIxf3NZKxSWrzrk3rPGUXxGRQWcP5aJdB1q9mVkbQ==): 
  - [marquis-wines.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkZN7YjAciSRgDLH038qSyIvh16e6lOvUvrk5_coIPfhtKYsbN1Ogi_KfoiSeW1-vgGxw-GV6p5TvyshxfMkBdYsKnHlddK4mF5PYquM3UPwfVx4KYDpvTCzxVXVrHTtgJjVbIG-VZ9nQ0eY2rc9WsBeX_vU7wdtkSuNgODiU7Xxs=): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeJRyJRyI1nYmK0UFUu8p8AG-fJHR_vhukGHe8tbuHLts42pPr0HUE_NQyGWKBJrwJdJdzGaKAqIWaDwpNAhou1smPiy8naU4eW1wGgZR5xtFWDHkU7R2T7zPZ1QGjbEyBbD7kqfpFYZKXNUZpoMdXBLxTkKx2PyHK8vHlzlpxYae-T0AA0QSeB79jnbrvPpu-mUrIisNSEs-oIAWaKfrYJoAQfFIWuXg0fQi_1D5_wFYSNqH3jcek9MraDaM=): 
  - [nataliemaclean.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaqaAh3IYrDxwjjKLDSbTmOLhZGH66i3mIAVreWVJ1zkBRcr4YRrr5vbzUz0Fh5TDk_9U3JWfKXq8Zmaxzzs5L4R179YCY6N_F5Hc3fM_M1h53FA9SLRKjVTha5kKyao4rboEJB5XeRxUue3bAAIfutoe8wNVS-bZwixNjOVJBtJRZI9hgoe3Ex3R8nsIZeHGvS3GU71ErWrbR4Wgy): 

#### search_web_grounded_tool (status=ok, 8 results)
Search answer: Laughing Stock Vineyards’ flagship Bordeaux-style red blend, **Portfolio** (sourced from the Naramata Bench in the Okanagan Valley), is widely regarded as one of British Columbia's benchmark red wines. It has consistently earned 90+ point ratings from WineAlign in the majority of its submissions. 

Review scores and accolades for recent vintages include:

### **2022 Vintage** (Celebrating Portfolio's 20th Anniversary)
* **Anthony Gismondi (*Gismondi on Wine*): 91 Points**  
  Gismondi described the anniversary vintage as having a fragrant, Napa-like nose featuring black cherry, cocoa, cedar, and sweet oak, noting that it possesses excellent structure and is surprisingly approachable in its youth.
* **David Lawrason (*WineAlign*): 91 Points**  
  Lawrason praised the wine's complexity, noting a mix of red and black plum, cassis, sage, and a dark chocolate finish, calling Portfolio one of the definitive benchmark blends of BC.
* **WineAlign National Wine Awards of Canada (2025): Gold Medal**

### **2021 Vintage**
* **International Wine & Spirit Competition (2024): 92 Points**
* **WineAlign National Wine Awards of Canada:** Earning top marks, this vintage helped Laughing Stock secure the title of *Best Performing Small Winery in BC*.

### **2020 Vintage**
* **International Wine & Spirit Competition (2023): 90 Points**
* **WineAlign National Wine Awards of Canada (2023): Gold Medal**
* **BC Lieutenant Governor's Wine Awards (2023): Gold Medal**

### **Notable Historical Accolades**
* **2018 Vintage:** Won a **Gold Medal** at the 2021 WineAlign National Wine Awards of Canada.
* **2015 Vintage:** Placed **2nd overall** in the 2018 *Judgement of BC* blind tasting, competing directly against premium international red blends.
* **2011 & 2014 Vintages:** Both received **94 Points** from *Gismondi on Wine* in historical tastings.
  - [laughingstock.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERLVs41p-tr7nu6oy8BLPxMIWJ5oobkG_lTBx9UwDUyqc5_aZT3eOa4qMdW9Ti09ACzL_4vdMkGm_xZyYFp5udxz7a2uSzNuRRo5DcUn-1CA6HaulhiGX5A7RNWLSSDvTwV4XujTQSt8B1Frqm_J7kkd1XQUYCloWSEPNaRVQ8q9wGIHsPd98M3Z1KAeutkWsuA7nEoSSQpQPGloPCFz6thM8MdFd0vjiDsM0HZ0U=): 
  - [laughingstock.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIneMvPRKyA_OJ5MbcS5aZgkdnkr9nAbHVowAOYM01W1HSMpRzLuayfX10wqB8W_PThLYRuzQaBeQ2yA4DHViVqltWLTlxlFlo-guNt_tC6XcZZ3RdhMud): 
  - [bcliquorstores.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1CAMjLzC6xEzzGE2mmnNEl9IOKYJXPDkXcp5pnJPDWpTLzDiyuAgviyQyZ_rDot2ZX0lVKH-00fw_tfiu8yCt_SvehwGv-zI8YFQThy_usBUVPgfFbot9pcANK-BH3j_MFken-Elxjw==): 
  - [laughingstock.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNT763ZB0le1dQCTPximIiBCYjRS5wcfBhZv9Uwq94bj49h3cr1lAg7PpISH7BrPtT0Xu252QqWNazWyajtNUjoeRIsojAEw7torVQlvTdYSQqHjxm8NBHXq9rhYLd4DZ9EsXAVzmhYhb2B08IWSDSyUvhz3LgBTQZ7uabF3H_YvhFmg40BNHnQPQ9PHysUy8AavkaT-1loZnEvpGdFStlXjeDfhHAVVqeabiK6gE=): 
  - [vancouversun.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbiQ_-n8Wj2740BokIV_UNjPJ7mUP62D9j77rf3nw1BdW42awIk5ujpsOqp0HAYEgnRG-wkxiJxmmnmtGWBQVH_PCKnRBtTah12SwGP6FcaYjq_-9Ihj2E3GHgPShIHkcvbEd2g_1FlZ1xk-itjNY3_FV9kGgAjtmZvxKAVUMuYQzqpVMO): 
  - [laughingstock.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBvm0fHhe39qbZ3nNBpSsXBk-5--UNuud0eYuY80NOgHh6SXjGKkaEqAdcZ6BQasyE9aLvRRLTfhtXko2wMF86NgwaSBW21M6pdaYhCeuVDG_vVitFo--9QmJTn1iYiu6gZbyjykOoAEHd-U03z-UG9TKBlALyJSk_FDu-aTP7p5M000dkQ75XLyrMXIEiSvxhKUNvvGOec1PIFR-DLjIcCiV0kalQr1bWhEuKtcI=): 
  - [laughingstock.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0v_IfO7FJDqso2U4qAq2NoFNwYdwhT_t84Tsno2w-7hJG4KogahPOyblwDIeVcxkqI8tiv1EG2XQZ-EMek0YVudRpkP0XIN9QSNyHI3Ol__h4747pfrN9KeqSAiWhKmAOTLcgxESw1_FGTW599kBt): 
  - [wine-searcher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFh-JGeyANlOsLaAim4f08ZEyRt6OoK8u058E84b9hSLCbwxg8SGjSyT-rQCl6OBUmdAfStVIEi8wkMlj-gI0vnrbFN6cNZMyc5Am-YQz3ZkO1cSrCGXM7DuKqkttC_lCDQif7XtuIiIa2MG62LqVYTjH-nt1uapcnv8bNhyG3AwmS2JfozOC1tbvpeWNKSP-tBnfvKLhiyLEguGxpssmcDQms=): 

#### search_web_grounded_tool (status=ok, 11 results)
Search answer: **Shelter Point Distillery**, located on a seaside estate farm on Vancouver Island (Oyster River/Campbell River, BC), is highly regarded for its estate-grown, traditional pot-distilled single malt whiskies. 

The distillery's most notable Pinot Noir cask expression is released under its **Double Barreled** series.

### Shelter Point Double Barreled (Pinot Noir Finish)
* **The Collaboration:** This expression is a special collaboration with the Okanagan Valley’s renowned **Quails' Gate Estate Winery**. 
* **Maturation:** The single malt is first aged in American oak (ex-bourbon barrels) for 5.5 years, then finished for 335 days in French oak wine barrels that previously held Quails' Gate Pinot Noir. 
* **Specs:** Bottled at 50% ABV, natural color, and non-chill filtered.
* **Tasting Profile:** The distillery notes a profile of rich berry jam, dark chocolate, and vanilla on the nose, leading to a sweet, juicy palate of stewed fruits and cherry pie, ending with a warm, peppery finish. 

### Reviews & Accolades
* **Whisky Whistle:** Critic Mark Kaufmann scored the Pinot Noir finish **92 out of 100**, highlighting its elegant sweetness, light tartness, and a chocolatey raspberry finish.
* **Toronto Whisky Society (TWS):** The TWS awarded it "Best in Category" for Single Malts in 2019, praising its depth of character and the seamless integration of the wine cask influence.

### Other Pinot Noir Cask Releases
Shelter Point occasionally integrates Pinot Noir casks into other limited-run offerings:
* **Evans Family Reserve:** This annual series has featured a wine-cask-finished expression blending ex-BC Syrah, Foch, and Pinot Noir casks.
* **Wee Rocky Whisky Club:** The distillery has also produced exclusive single-cask bottlings finished in French Pinot Noir barrels for local whisky clubs.

### Availability in BC
Because these are limited, small-batch releases, they are not always part of the core, year-round lineup. When available, they can be purchased directly from the distillery's online store, at select private liquor retailers across BC (such as Everything Wine), or during specialty release events at BC Liquor Stores.
  - [shelterpoint.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHm1b_H-4DvZx71KK5QywrMKO_HulycUua9VrLYrM1Ytr20ItkGmbvOEKp_B3V-aR3wjU24q5VcPFnuZILOmk3wNWoMk-EtOdcS5wqW2GHZG8ASRL70Zx72rE7AXgZXGhDDLlnOvxRbt89MtQ0-ixIX5SMGzqiivUKzqrf5alCJoCDujmWgymygNOLVUv5ztgotAcQ8jwi3gQ=): 
  - [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVpasw6Efu9INsJw_JkuBItfValxsu7_30rr7lsM4sgknQMKU-87T5JPPTPxmYgt_qd_Of3fC7e28-BtdlfLEXtj6yogo7Ur4f7b2FSVEW2OZZG0053tIuO7oFmjJqNEV_4zKz9aZ9lWXLOGL3fL8owEfTKv2KxU9ejc_Gof4kHPUA9F_NKyFNk_CpIEmnbYdU7KSOjt9PGM9NaBs-j-c=): 
  - [dramsofwhisky.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHglypx1UcT4g_5QkyNsBCyU4Cmd4D6kELiLoHy1jbuBVK_Ipa77I7Rl5cwTWHLicYU_1-cC9Ko-1URo5wrt5Ear6RLWilm38ozcoDJnilS50K8GsepTt3_DQIk0rLR5BlDhaLqNr8JCuxSxS6tLi_8QGgSk2xuaVtyaKTM4_adGSddutBVXfYhPI5I5S2KOQ-TZyQ=): 
  - [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGygDaheWL6PeOOE861-p8zgYddzAhSy5V4bKxJZ-bsQu1PH8tAjUmK_XkKlZyvZCutgIES-vuUam3KOcefbF4-jBhWcf94dgkJqvOk2ou0o6msDiGHr2s4MB2H8adUNxBckOAdn73M59EmhJ_qe9OBccDhXiRE30Bnw25Y2tChzuW9pRGrJzlPKkgfdIg0KtqS7r-o_3SH_Sv-DJyzDg==): 
  - [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDQCdbfdlXE6sBEKwiVoDAqpERhJ0ayuTnGyrvlvPjE_WW73xITGlcJYoD3nY0pjms3AeR91YQWlMRJWfSDnDTM2AySawNam44kYWPdOpG4TyjEemhvsX02T_AMnsWxnujSMYLYg8=): 
  - [torontowhiskysociety.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2czUbcprF4ANlj66hfWBV1fxvrzsyUutKWo6HSTi7DO9wnrs7WAgFKZYaVATMOqolgFngJu41U8rBLavgFaPlclG0g2418XQWWH6-rmFjzPubuTIJHgYMZXe1AizJDD543zK-oLwl8Uk_8lwr4IPTPjPo-MGFUsAHpAaZKAAKdNu0wSqanrZ_wPb6D5SEBFmsSA==): 
  - [thealchemistmagazine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-TTY_U48Zr0v9lkWRY3JDrJ6nMJZEFeClHOdfHFDSCbmG5qqCKTxz9mU_WNXGgU8junJU8-8ZzxD7gz7xV-o0wJI45ogEwUnPghvXiql54TRQFaeb-XmIQjXxcvfZOlYt1__YYRH-H7cfNH-Nsxgrk9gJBk5T0ijwOoR03_ZALnW2sGg=): 
  - [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwARC_3wGs8MDaaUlPj7hIvOqG7jIiby4tZ7Dg8frwPGya4m0d0wWkK_lPtOgJ8k-gd5CSEUJJWLdvqBAapg5zlwb-iOSN_AsBUosCHFMWIBuBo3Xycv5dgYcva7cnzzAXZ6xMKeA=): 
  - [dramsofwhisky.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaKacEav6e5rM9B26N-J_Z4kzDw0zeQptvcNWty5pnsDWoxg1N4EqDNhLb7bUrnfpmunLSpfVHRcp_UlUkoUn60hftWYPqcQ5CcLvqqSLrW_29I51GtCpCWotej74EuiBoZLjgsGo7RpDYXKUgXkJudkeE9wxLJjhoU1J3PFIr7IdzMwRLyWiqylZHyZntwO3Xbg==): 
  - [everythingwine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK_cfGx5RfbmYtsb6NRgRLLQHUKCJvdzbLVYF60OQTR2IC1HQO-02_BONH4XOyST0MjowDdgSphelXYG7bfaetIdpX_3PmaatZt4LxehVyK9PlrJsRhLkffzwYBDO91L6TF_yDfEdf9n4N3bkCp1VUzgQcSQ2gfp-0InXyiEp6znsH1wUWl3hGYElNDLia5PzgHWPoDQ_zhoVQMQ==): 
  - [bcliquorstores.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGssu4RGaF0a13vpxlLE4XizNErxO-0Ter4nd9NvpebeQJy0tbndZY2AabGpJY0u_a2k7ea6N79niT_1OiuBy0C2sF9Tc_rq2KndakqNUGqP05YND5GkO1QLmDXCHhxFZPrUKXA0RmgGw==): 

#### search_web_grounded_tool (status=ok, 5 results)
Search answer: **Reynard Oud Bruin** is a highly regarded, limited-release Flemish-style sour beer brewed by **Strange Fellows Brewing** in Vancouver, BC. 

### Key Details
* **Style:** Flanders Oud Bruin (Flemish-style sour brown ale).
* **ABV:** 6.5%.
* **Aging & Blending:** The beer is blended from several French oak barrel-aged vintages spanning up to three years.
* **Profile:** It pours a rich mahogany brown. The brewery describes its character as a complex balance of sweet and sour with a cider-like tartness, a delicate malt backbone, and notes of cherry, chocolate, licorice, leather, oak, and vanilla.

### Background & History
* **The Brewer:** Brewmaster Iain Hill is a pioneer in the BC craft beer scene, recognized for introducing Vancouverites to Belgian-style sours (including Oud Bruins and Flanders Reds) dating back to his tenure at Yaletown Brewing Company in the 1990s. 
* **Release:** Originally debuting in June 2016 as Strange Fellows' first-ever barrel-aged sour, Reynard has been re-released in subsequent limited vintages (including 2018, 2020, and 2021).

### Reviews & Reception
* **Scout Magazine:** In a review of the inaugural release, the publication praised the beer's depth and complexity, highlighting its balance of black cherry, caramel, vanilla, and bittersweet chocolate, followed by a lingering, spicy, and tart finish.
* **Beer Me BC:** A review of the 2016 release noted a complex aroma of dark fruits, leather, and oak, with a palate dominated by cherry, toffee, and a distinct vinegar-like tartness.
* **Untappd:** The beer holds a strong rating of 3.9 out of 5 stars on the platform.

### Food Pairings
The brewery recommends pairing Reynard with classic Belgian fare like *moules frites* or *carbonnade Flamande*, as well as earthy cheeses, vinegary salads, and rich chocolate desserts.
  - [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIGncCFrTQWeUyv46o8_adQ4QVIZkkE6rdGGClROuALRErTfjm-ueO_QRw7yrYUWHdgqoeQRL-JXOl6fVf27ul0jz1NsDRLsCDxFDrNOH1APxe99Pb_GPF3yK2C8_sx-Z5UGpi9hkqw4Ddrcygb1nciu18PLP0k5UYQhl4DVHEe67ZO44m5ncyPzm5mOcFzo_1iv6Klg==): 
  - [ridgerockbrewco.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVzUf7T-vztHV6h4V2RLLgxGkxb-J-ouq2s2nQs5xU-B8yvXTaVDnwr1Fy7PHlqW-2RUwjYgWqhEITGVqG-kdvGwBLBxyamuf4h4exlgiKcKuEAGMaWOTKo2-6z4ybTPhQ0MtB-4gz0n-HddfQkfuDkKCe0D1vYoYJ_7W8FdMnXKEtnrhh-f4sWLJ-p-uF7P7BeIJurr0irTTJVz4nNlM-HKy7ylV78QcIHQ==): 
  - [untappd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT6D20S34Ku8HGePrI-1h_MTayEqOgcO1BgaJpsvw6W75xdj_eo-DYR6ipsP8oiVNMXNsvvTooBBbiiSeoIWvLTPk_Xaz_ukjmh5fZOg7KLWYmmkaVyLe3M2zsyiDls3Hf2qi8oWoyP1-GxmQeIjYC2e4kJ5Trz6I=): 
  - [strangefellowsbrewing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6o2xub-ge3eaHmnl89LSKYMXv6lB_ZpobQkOkYmpz-elj3rF53pmLV2_hQ-ooFTqEU0zo8Ph42ruX63uKSpK_V02Yub1oBFQvv6nl5HobMrj-V0s-1XSvSop1bex9RntiD_YZZlZexdO2wk7aCUX8Jh7-aEMMGlgmuw==): 
  - [scoutmagazine.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDdiuSh2n5Eg6MOBCttRYuAoK3-xBOmHuPepizt9WDMVo5KYxAGy4nUF8EjwxNeUQShx5uRuFCWoz-w1O2uhpZSeGWbJuH70XTtDQjKsfvWChje3FUWKQZsV97yZwcCBSvrMcTE_BZDXoLQy5-6uvyP-oHKYhhOSlPPV5b4nKc4JceTLpI1-h8dvne45S790whC6wOYkfLkMT7AMDRHFla): 

#### search_web_grounded_tool (status=ok, 9 results)
Search answer: **"Osake Fraser Valley Junmai – Renaissance"** is a premium, "farm-to-glass" sake produced by **Artisan SakeMaker**, a boutique sake winery located in Railspur Alley on Granville Island in Vancouver, BC. Founded by Masataka "Masa" Shiroki in 2007, the winery is a pioneer in crafting local Canadian sake.

### Key Details & Production
* **Rice Source:** This sake is made using 100% British Columbia-grown sake rice cultivated in Abbotsford in the Fraser Valley. 
* **Rice Variety:** It is brewed from *Ginpu* rice (originally from Hokkaido, Japan). The specific strain grown locally is sometimes referred to as CGP49L (Canadian Ginpu 49 Degrees Latitude).
* **Style & Profile:** It is styled as a rich, savoury, and off-dry sake. It is crafted to appeal to wine lovers, featuring a pronounced level of acidity, complex flavours, and a balanced, mature finish. 
* **Alcohol by Volume (ABV):** 14.5%.
* **Pricing:** It typically retails for approximately $24.49 CAD for a 375ml bottle.

### Awards & Recognition
* **Judge's Selection** – Alberta Beverage Awards (2016)
* **Silver Medal** – NorthWest Wine Summit (2017)

### Food Pairings
Because of its high acidity and savoury umami profile, the winery recommends pairing this sake with a wide variety of Western and Asian dishes, including:
* Charcuterie and pizza
* Roasted chicken
* Miso or Kasu Black Cod
* Fish or clam chowder
* Mango pudding

### Related Variations
Artisan SakeMaker also produces a **Pacific Coast Blend** version of this sake, which is a 50/50 blend of the Abbotsford-grown Ginpu *Junmai Renaissance* and a California Calrose-based *Junmai Genshu*. Additionally, they offer a **Junmai Nigori – Renaissance** version, which is complex, creamy, and semi-sweet.
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRMC2gnnMXgR_TZUtlG7Puw5Tye66xPJ00cDwriO34w-dkCkWa1DDrncTHk5yRCc83CaQL2PfZ15bVCFMk6Mj-o338q413TwBcgwUtBMRFox428o45r4ZzvtKJ__ePAZ-4oHwEXmDInRefWwq4G6eqwHWYBiZFJQOfjD9ywfFJ7A0ut2DYEA==): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5dMol56CEk2oqeb16hvOmfkuurhcfLZYZipo-ej9TFgoht8AR7mOfAdL9yBSoyCsHAgKVQBP6yxP4-DwI3807Rldu71Az83fAvIqtM68jbInyzdnNheIduyTzBxKe1J6UeSTQrRZRUu36): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOK4u2yC08YS2ORIEMwtIi0nmwSK81g_KpqU2bjOX-2TazbYV9ucuS1uU0MnwgcrCJyzgeRe4YPlP2gyCmmYjcrNu3uylW539SFXiWq_FJ6kC3q_OHa8cbou91EP6pOqfA): 
  - [maryinvancity.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3es-ZCVCicZzUG-V-aY62j1TOi3zVeGiCu44sciuQe60T1FP_6Q82AXbPQlLphsGjaDk8yOf8caoeDX29OKaModa3Bw9qvcoHuplNfkOPBMRcWdspRCdBZuskszvGLrijFAkWsgl_XV9DfKAckgVs5frsKVT0hVM2Md4gEPW5l0xkGmAU90VP1JU=): 
  - [wixsite.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzXepY1LO6dI4WSqgYtD9vMqw433MvMtaecIrj80Acuumspcig_bq5x4CWdXDZEkN-OS4C9GJWUmxW7NUTAI623hurMkazJe3YlygEP4FK4DrirQ-YuzQj_WQuPVHKfDkAhY-V6NiAl88=): 
  - [ellecanada.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQQuEz0xMUkMjdsquP_xXTvkoaRdunX0P5RKnoBC3_l3QkvDP9QQQXCMoTb5T4a2HWj53xwzZOdj-zJLSssj23ftoaMeHoJR0P8-0gTFiHR7KmT9r1Re1hHqqBG93sIdgsfkXfTGSYdqeBFZkAlfGaPMJaKJMQvI-Q5BAEid2b1BPpY1oiDFHmIdyA8_HW12hYr2lGsFTzAc0KMhlmSwbhwTY1fcNOhzYQkQ==): 
  - [wixsite.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcOPsh-bliwMCkG1HVhOsbUxq1CH_0Yb2lnNQWlxaf_y6OD4n9GAyFhf34p7O7KWIRdbTBqxQg5MKOJtVsL93Rvdo5MfuoUWbzRdh8-jXf8YAJB2LWiLgH2Gbz9iz8VE8xo8XKdq5jwpCIscZzNp75Uk8IYSvfRJDDvRB3_wQ0yTcTFwMoJTzluM3ISz80iA5G2GlCGs87CfyAzwUcs_P9mk3BHHo=): 
  - [eatnorth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM_RH-hV3c8Pf-8rCFqKNcr_AvbRSWQbmwWN4qUu88zl9iu8jns_6hVUn1Esd389PMXWZ8UDkG1rh00nBVSyEC3GKZE35syaGdgTgIwtUAnEjBrTl6Z0eyCQqVAGgSLiPciLMxXb4JbSZmfXD8c2sSDL2YOtb6u3OOd5m1MyJ4o0Hq-GiE416YYQ==): 
  - [artisansakemaker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgT6e7hAIDF9F4m2Z76yuK2rhyPrmEsmyHEQxXF0Jh-Dh_qfZaExuFZoNfxhrl6akUtaE3wKPyThk8osmOtkG2iZwYA4DWpE21DalOPV8emgmgD0uAakIX-XpqdEg=): 


### sourcing_agent_tool (status=ok)
**Sub-agent synthesis:**
Here is a curated selection of top-rated and highly popular BC red wines under $50, currently in stock at Vancouver-area retailers. 

---

### 🍷 Pinot Noir

*   **Meyer Family Vineyards Okanagan Valley Pinot Noir**
    *   **Sutton Place Wine Merchant:** $33.49 (27 in stock) | [Buy at Sutton Place](https://store.suttonplacewinemerchant.com/products/4298314-meyer-family-vineyards-okanagan-valley-pinot-noir)
    *   **Marquis Wine Cellars:** $34.99 (12 in stock) | [Buy at Marquis](https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/)
*   **Quails' Gate Field & Flight Pinot Noir 2024**
    *   **Marquis Wine Cellars:** $24.99 (25 in stock) | [Buy at Marquis](https://www.marquis-wines.com/quails-gate-2023-field-flight-pinot-noir-750ml/)
*   **Little Engine Elevation Pinot Noir 2023**
    *   **Marquis Wine Cellars:** $32.99 (5 in stock) | [Buy at Marquis](https://www.marquis-wines.com/little-engine-2023-elevation-pinot-noir-750ml/)
*   **Gray Monk Pinot Noir 2021/24**
    *   **Marquis Wine Cellars:** $24.99 (18 in stock) | [Buy at Marquis](https://www.marquis-wines.com/gray-monk-2019-pinot-noir-750ml/)
*   **Cassini Pinot Noir "Red Carpet" 2023**
    *   **Marquis Wine Cellars:** $29.99 (24 in stock) | [Buy at Marquis](https://www.marquis-wines.com/cassini-2022-pinot-noir-red-carpet-750ml/)
*   **Inniskillin Okanagan Pinot Noir 2023** (Rating: 3.8/5)
    *   **BC Liquor Stores:** $19.99 (2,406 available across 174 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/624767)

---

### 🍇 Syrah / Shiraz

*   **Black Sage Vineyard Shiraz (Oliver)** (Rating: 4.1/5)
    *   **BC Liquor Stores:** $32.99 (1,503 available across 108 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/596841)
*   **Nichol Syrah 'The Village' 2022**
    *   **Marquis Wine Cellars:** $32.99 (23 in stock) | [Buy at Marquis](https://www.marquis-wines.com/nichol-2021-syrah-the-village-750ml/)
*   **Le Vieux Pin Cuvee Violette Syrah 2023**
    *   **Marquis Wine Cellars:** $46.99 (25 in stock) | [Buy at Marquis](https://www.marquis-wines.com/le-vieux-pin-2022-cuvee-violette-syrah-750ml/)
*   **Moon Curser Vineyards Syrah**
    *   **Everything Wine (Vancouver River District):** $36.98 (3 in stock) | [Buy at Everything Wine](https://www.everythingwine.ca/moon-curser-syrah)
*   **Daydreamer Amelia Syrah Viognier 2022**
    *   **Marquis Wine Cellars:** $46.99 (13 in stock) | [Buy at Marquis](https://www.marquis-wines.com/daydreamer-2022-amelia-syrah-viognier-750ml/)

---

### 🌿 Cabernet Franc

*   **Bartier Bros Cabernet Franc 2022** (Rating: 4.4/5)
    *   **BC Liquor Stores:** $29.99 (620 available across 56 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/993139)
*   **Phantom Creek Estates Estate Cabernet Franc** (Rating: 4.6/5)
    *   **BC Liquor Stores:** $41.99 (1,603 available across 117 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/90203)
*   **Black Sage Vineyard Cabernet Franc 2023** (Rating: 4.0/5)
    *   **BC Liquor Stores:** $32.99 (2,570 available across 172 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/593038)
*   **Tinhorn Creek Cabernet Franc 2023**
    *   **Marquis Wine Cellars:** $27.99 (47 in stock) | [Buy at Marquis](https://www.marquis-wines.com/tinhorn-creek-2023-cabernet-franc-750ml/)
*   **Burrowing Owl Cabernet Franc 2022**
    *   **Marquis Wine Cellars:** $42.99 (19 in stock) | [Buy at Marquis](https://www.marquis-wines.com/burrowing-owl-2022-cabernet-franc-750ml/)
*   **Tantalus Cabernet Franc 2022**
    *   **Marquis Wine Cellars:** $36.99 (16 in stock) | [Buy at Marquis](https://www.marquis-wines.com/tantalus-2022-cabernet-franc-750ml/)
*   **Blasted Church Vineyards Cabernet Franc**
    *   **Everything Wine (Vancouver River District):** $34.99 (10 in stock) | [Buy at Everything Wine](https://www.everythingwine.ca/blasted-church-vineyards-okanagan-valley-cabernet-franc-750-ml)
*   **Inniskillin Okanagan Cabernet Franc** (Rating: 3.9/5)
    *   **Okanagan Cellars:** $17.99 (17 in stock) | [Buy at Okanagan Cellars](https://okanagancellars.com/products/4340630-inniskillin-estate-cab-franc)
    *   **BC Liquor Stores:** $17.99 (1,661 available across 130 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/372461)

---

### 🍁 Meritage & Red Blends

*   **Phantom Creek Quartz and Yarrow Sustainable Red 2016** (Cab Sauv, Merlot, Cab Franc, Syrah) (Rating: 4.6/5)
    *   **BC Liquor Stores:** $35.99 (428 available across 45 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/194330)
*   **La Stella Fortissimo 2023** (Merlot, Cab Sauv, Cab Franc, Sangiovese)
    *   **Marquis Wine Cellars:** $40.99 (15 in stock) | [Buy at Marquis](https://www.marquis-wines.com/la-stella-2022-fortissimo-750ml/)
*   **Goldhill Charisma Red Blend 2019** (Syrah, Merlot, Malbec) (Rating: 4.7/5)
    *   **BC Liquor Stores:** $17.99 (54 available across 5 stores) | [Buy at BC Liquor](https://www.bcliquorstores.com/product/770008)
*   **Narrative Non-Fiction Red Blend**
    *   **Marquis Wine Cellars:** $16.49 (4 in stock) | [Buy at Marquis](https://www.marquis-wines.com/okanagan-crushpad-2019-narrative-non-fiction-750ml/)
    *   **Legacy Liquor Store:** $29.78 (8 in stock) | [Buy at Legacy](https://www.legacyliquorstore.com/product/wine/narrative-non-fiction-1-x-750ml)
*   **Hester Creek Cabernet/Merlot 2022**
    *   **Marquis Wine Cellars:** $23.99 (17 in stock) | [Buy at Marquis](https://www.marquis-wines.com/hester-creek-2022-cabernet-merlot-750ml/)

#### search_bcliquor_tool (status=ok, 3 results)
  - INNISKILLIN OKANAGAN - PINOT NOIR 2023 | $19.99 | stock=2406 | in 174 stores | rating=3.8 | https://www.bcliquorstores.com/product/624767 | {sku=624767; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=12.5; sweetness=00; tasting_notes=Known as the heartbreak grape, Pinot Noir is tough to grow and tough to produce. But the end result when done well is a silky medium-bodied red with cherry and raspberry flavours that magically linger. Match to tuna steaks, roast poultry or everyday casseroles.
; consumer_votes=123; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/624767.jpeg; certificates=["BC VQA", "All VQA"]}
  - QUAILS GATE - PINOT NOIR STEWART FAMILY RESERVE 2022 | $59.99 | stock=37 | in 12 stores | rating=4.0 | https://www.bcliquorstores.com/product/639658 | {sku=639658; product_type=Red Wine; grape_type=PINOT NOIR; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=Graceful and sophisticated. An herbaceous bouquet of Okanagan sage lifts from the glass followed by black cherry that unfolds perfectly on the palate. Exceptional structure and strong, noble tannins are balanced with elegant natural acids and elevated flavours of cocoa and baking spice.
; consumer_votes=66; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/639658.jpeg; certificates=["BC VQA", "All VQA"]}
  - MEADOW VISTA - BLISS SPARKLING CHERRY HONEY WINE | $16.99 | stock=383 | in 44 stores | rating=3.8 | https://www.bcliquorstores.com/product/785915 | {sku=785915; product_type=Sparkling Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.500; alcohol_pct=12.0; sweetness=01; tasting_notes=Dark, juicy Okanagan cherries were added to give BLISS a beautiful blush colour, notes of cherry, plum and pinot noir. Delight in this bubbly with grilled foods such as seasonal veggies, meats and fruit.
; consumer_votes=137; is_bc_vqa=False; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/785915.jpeg}

#### search_everything_wine_tool (status=ok, 9 results)
  - Inniskillin Okanagan Pinot Noir 750 mL | $19.99 | [North Vancouver:6, South Surrey:44, Langley Store:25, Vancouver:0] | https://www.everythingwine.ca/inniskillin-reserve-pinot-noir | {sku=624767; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/6/2/624767_inniskillin_pn_wo_c.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Charisma Wines by Gold Hill Pinot Noir 750 mL | $25.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/gold-hill-winery-charisma-pinot-noir-750-ml | {sku=843094; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/4/843094_charisma_pinot_noir.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Martins Lane Winery Naramata Ranch Pinot Noir 2022 750 mL | $92.98 | [North Vancouver:0, South Surrey:6, Langley Store:0, Vancouver:0] | https://www.everythingwine.ca/martins-lane-winery-naramata-ranch-pinot-noir-2022-750-ml-ew10029457 | {sku=266195; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/6/266195_martins-lane-winery-naramata-ranch-pinot-noir-2022-750-ml.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Burrowing Owl Estate Winery Pinot Noir 2018 750 mL | $89.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:1] | https://www.everythingwine.ca/burrowing-owl-estate-winery-pinot-noir-2018-750-ml | {sku=17884818; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/7/17884818_burrowing-owl-estate-winery-pinot-noir-2018-750-ml.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Many Hands by Okanagan Crush Pad White Blend 750 mL | $26.99 | [North Vancouver:9, South Surrey:78, Langley Store:3, Vancouver:0] | https://www.everythingwine.ca/okanagan-crush-pad-many-hands-white-blend-750-ml | {sku=272339; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/7/272339_many_hands_white_blend.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Martins Lane Winery Vineyard Set 3 x 750 mL | $329.99 | https://www.everythingwine.ca/martins-lane-winery-vineyard-set-3-x-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Free Form By Okanagan Crush Pad Vin Gris 750 mL | $38.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:11] | https://www.everythingwine.ca/free-form-by-okanagan-crush-pad-vin-gris-750-ml | {sku=190205; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/9/190205_ocp_free_form_vin_gris_nl2.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Frind Estate Winery Rose 750 mL | $20.99 | [North Vancouver:7, South Surrey:9, Langley Store:5, Vancouver:15] | https://www.everythingwine.ca/frind-estate-winery-okanagan-valley-pinot-noir-rose-750-ml | {sku=50870; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/5/0/50870_frind_rose_1.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Meadow Vista Bliss Cherry Sparkling Honey Wine 500 mL | $16.99 | [North Vancouver:0, South Surrey:0, Langley Store:7, Vancouver:13] | https://www.everythingwine.ca/meadow-vista-honey-wines-bliss-sparkling | {sku=785915; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/8/785915_meadow_vista_honey_wines_bliss_sparkling.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 3 results)
  - INNISKILLIN - ESTATE CAB FRANC | $17.99 | stock=17 | https://okanagancellars.com/products/4340630-inniskillin-estate-cab-franc | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000037/0000372461-2735.jpg}
  - OKANAGAN VINEYARDS - CHARDONNAY 2024 | $10.99 | stock=14 | https://okanagancellars.com/products/4857514-okanagan-vineyards-chardonnay-2024 | {category=White Wine; in_stock=True; unit_size=750ml}
  - OKANAGAN VINEYARDS - MERLOT CABERNET | $10.99 | stock=10 | https://okanagancellars.com/products/4746564-okanagan-vineyards-merlot-cabernet | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000012/0000121228-9856.jpg}

#### search_suttonplace_tool (status=ok, 1 results)
  - Meyer Family Vineyards Okanagan Valley Pinot Noir | $33.49 | 2025 | stock=27 | https://store.suttonplacewinemerchant.com/products/4298314-meyer-family-vineyards-okanagan-valley-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000015/0000154310-1810.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 20 results)
  - Keenan Wines 2023 Pinot Noir Rose 750ml | $34.99 | stock=3 | https://www.marquis-wines.com/keenan-wines-2023-pinot-noir-rose-750ml/ | {sku=1031531; in_stock=True; categories=["Organic / Biodynamic Wine", "Rosé Wine", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20887/images/16627/2025-09-24_14.34.00__44572.1758822434.500.500.png?c=2}
  - Meyer Family 2023 Pinot Noir 750ml | $34.99 | stock=12 | https://www.marquis-wines.com/meyer-family-2022-pinot-noir-750ml/ | {sku=1014474; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7708/images/8652/Lindsey_Ail_-_IMG_15661__44130.1589559651.500.500.jpg?c=2}
  - Gray Monk 2021/24 Pinot Noir 750ml | $24.99 | stock=18 | https://www.marquis-wines.com/gray-monk-2019-pinot-noir-750ml/ | {sku=251835; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/15726/images/11434/2022-01-20-17.34.22__23087.1642793746.500.500.png?c=2}
  - Quails Gate 2024 Field & Flight Pinot Noir 750ml | $24.99 | stock=25 | https://www.marquis-wines.com/quails-gate-2023-field-flight-pinot-noir-750ml/ | {sku=1031446; in_stock=True; categories=["Red Wine", "Pinot Noir", "By Country / Region", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20759/images/16516/quailsgate_fieldflight_pn__03049.1756244759.500.500.jpg?c=2}
  - Little Engine 2023 Elevation Pinot Noir 750ml | $32.99 | stock=5 | https://www.marquis-wines.com/little-engine-2023-elevation-pinot-noir-750ml/ | {sku=1031041; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20287/images/16055/2025-04-29-14.26.19__33781.1746032523.500.500.png?c=2}
  - Tender Hope 2022 Pinot Noir 750ml | $29.99 | stock=6 | https://www.marquis-wines.com/tender-hope-2022-pinot-noir-750ml/ | {sku=1029669; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18566/images/14454/2024-02-29_15.32.56__59905.1709321559.500.500.png?c=2}
  - Fox & Archer 2020 3 Blocks Pinot Noir 750ml | $42.99 | stock=15 | https://www.marquis-wines.com/fox-archer-2020-3-blocks-pinot-noir-750ml/ | {sku=1027574; in_stock=True; categories=["Red Wine", "Pinot Noir", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21434/images/17192/fox_archer_3_blocks_pinot__77598.1773093147.500.500.jpg?c=2}
  - La Frenz 2022 Desperation Hill Pinot Noir 750ml | $44.99 | stock=6 | https://www.marquis-wines.com/la-frenz-2022-desperation-hill-pinot-noir-750ml/ | {sku=1023751; in_stock=True; categories=["Red Wine", "Pinot Noir", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20886/images/16628/2025-09-24_14.34.31__62701.1758822527.500.500.png?c=2}
  - Blue Mountain 2023 Reserve Cuvee Pinot Noir 750ml | $51.99 | stock=11 | https://www.marquis-wines.com/blue-mountain-2022-reserve-cuvee-pinot-noir-750ml/ | {sku=1023129; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19489/images/15288/2024-10-31-14.17.17__41020.1730481578.500.500.png?c=2}
  - Little Engine 2022 Silver Pinot Noir 750ml | $46.99 | stock=1 | https://www.marquis-wines.com/little-engine-2021-silver-pinot-noir-750ml/ | {sku=1021298; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19579/images/15376/2024-11-12_12.45.54__52424.1731532840.500.500.png?c=2}
  - Burrowing Owl 2018 Pinot Noir 750ml | $101.99 | stock=14 | https://www.marquis-wines.com/burrowing-owl-2015-pinot-noir-750ml/ | {sku=1020263; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19714/images/15680/burrowing_owl_pinot__71112.1738348551.500.500.jpg?c=2}
  - Tantalus 2023 Maija Pinot Noir 750ml | $40.99 | stock=7 | https://www.marquis-wines.com/tantalus-2017-maija-pinot-noir-750ml/ | {sku=1016222; in_stock=True; categories=["Red Wine", "Pinot Noir", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9531/images/7177/IMG_9636__76411.1544468344.500.500.JPG?c=2}
  - Cassini 2023 Pinot Noir "Red Carpet" 750ml | $29.99 | stock=24 | https://www.marquis-wines.com/cassini-2022-pinot-noir-red-carpet-750ml/ | {sku=1014905; in_stock=True; categories=["Celebrate BC Wine Month", "Drink Local", "Red Wine", "Pinot Noir", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/8886/images/6958/cassini-2016-pinot-noir-red__12126.1732902163.500.500.jpg?c=2}
  - Meyer 2023 McLean Creek Pinot Noir VQA 750ml | $51.99 | stock=4 | https://www.marquis-wines.com/meyer-2023-mclean-creek-pinot-noir-vqa-750ml/ | {sku=1014177; in_stock=True; categories=["Red Wine", "Pinot Noir", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21527/images/17235/2026-03-16_12.34.49__64507.1773856823.500.500.png?c=2}
  - Martin’s Lane 2020 Vineyard Pinot Noir Set 750ml | $374.99 | stock=5 | https://www.marquis-wines.com/martin-s-lane-2020-vineyard-pinot-noir-set-750ml/ | {sku=1031998; in_stock=True; categories=["Red Wine", "Pinot Noir", "Gifts & Merchandise", "Gift Packs & Bundles", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21532/images/17213/IMG_0701__60509.1773251446.500.500.png?c=2}
  - Carson 2022 Naramata Vineyard Pinot Noir 750ml | $54.99 | stock=1 | https://www.marquis-wines.com/carson-2020-naramata-vineyard-pinot-noir-750ml/ | {sku=1016343; in_stock=True; categories=["Red Wine", "Pinot Noir", "Naramata Bench", "British Columbia", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/6671/images/5086/carson-pinot-noir-naramata__41209.1646247134.500.500.jpg?c=2}
  - Joie Farm 2022 "En Famille" Pinot Meunier 750ml | $40.99 | stock=1 | https://www.marquis-wines.com/joie-farm-2022-en-famille-pinot-meunier-750ml/ | {sku=1030729; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Other Red Varieties", "Drink Local"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19853/images/15557/2025-01-14_14.06.55__99797.1736967525.500.500.png?c=2}
  - Ursa Major 2025 Rose 750ml | $37.99 | stock=26 | https://www.marquis-wines.com/ursa-major-2025-rose-750ml/ | {sku=1032124; in_stock=True; categories=["Organic / Biodynamic Wine", "Rosé Wine", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21637/images/17316/2026-03-30-13.14.08__34450.1775070501.500.500.png?c=2}
  - Tantalus 2025 Rose 750ml | $30.99 | stock=17 | https://www.marquis-wines.com/tantalus-2025-rose-750ml/ | {sku=1017799; in_stock=True; categories=["Rosé Wine", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21728/images/17421/2026-04-23-13.31.48__31357.1777054370.500.500.png?c=2}
  - Le Vieux Pin 2023 Vaila Rose 750ml | $37.99 | stock=2 | https://www.marquis-wines.com/le-vieux-pin-2021-vaila-rose-750ml/ | {sku=1024520; in_stock=True; categories=["Rosé Wine", "British Columbia", "Okanagan", "Le Vieux Pin & La Stella"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/14568/images/10165/2021-04-07_13.35.17__30128.1617904852.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 12 results)
  - Inniskillin Shiraz Cabernet | $17.99 | stock=10 | https://www.legacyliquorstore.com/product/wine/inniskillin-shiraz-cabernet-1-x-750ml | {brand=Inniskillin Okanagan; slug=inniskillin-shiraz-cabernet-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Okanagan Spirits Maraschino Liqueur | $37.61 | stock=12 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-maraschino-liqueur-1-x-375ml | {slug=okanagan-spirits-maraschino-liqueur-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["spirits", "liqueurs"]}
  - Okanagan Spirits Amaro Classico | $37.61 | stock=3 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-amaro-classico-1-x-375ml | {slug=okanagan-spirits-amaro-classico-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["spirits", "liqueurs"]}
  - Narrative Two Pinots | $23.88 | stock=12 | https://www.legacyliquorstore.com/product/wine/narrative-two-pinots-1-x-750ml | {brand=Okanagan Crush Pad; slug=narrative-two-pinots-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "blend"]}
  - Narrative Non-Fiction | $29.78 | stock=8 | https://www.legacyliquorstore.com/product/wine/narrative-non-fiction-1-x-750ml | {brand=Okanagan Crush Pad; slug=narrative-non-fiction-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Narrative Red | $23.88 | stock=10 | https://www.legacyliquorstore.com/product/wine/narrative-red-1-x-750ml | {brand=Okanagan Crush Pad; slug=narrative-red-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Okanagan Apple Cider | $14.76 | stock=6 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-crisp-apple-cider-6c-6-x-355ml | {brand=Okanagan Apple Ciders; slug=okanagan-crisp-apple-cider-6c-6-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Spirits Raspberry | $37.99 | stock=4 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-raspberry-1-x-375ml | {brand=Raspberry; slug=okanagan-spirits-raspberry-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["spirits", "liqueurs", "other liqueurs"]}
  - Okanagan Orchard Peach Cider | $15.0 | stock=6 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-orchard-peach-cider-6c-6-x-355ml | {brand=Okanagan Apple Ciders; slug=okanagan-orchard-peach-cider-6c-6-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Apple Cider | $4.45 | stock=24 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-crisp-apple-tc-1-x-473ml | {brand=Okanagan Apple Ciders; slug=okanagan-crisp-apple-tc-1-x-473ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Harvest Pear Cider | $15.5 | stock=6 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-harvest-pear-cider-6c-6-x-355ml | {brand=Okanagan Apple Ciders; slug=okanagan-harvest-pear-cider-6c-6-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Spirits Cherry | $43.88 | stock=3 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-cherry-1-x-375ml | {brand=Cherry Liqueur; slug=okanagan-spirits-cherry-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["spirits", "liqueurs", "other liqueurs"]}

#### search_bcliquor_tool (status=ok, 6 results)
  - WAYNE GRETZKY OKANAGAN - CABERNET SYRAH 2022 | $16.99 (reg $19.99) | stock=818 | in 92 stores | rating=3.5 | https://www.bcliquorstores.com/product/835348 | {sku=835348; product_type=Red Wine; grape_type=CABERNET/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=13.0; sweetness=01; tasting_notes=Noted puck man Wayne Gretzky scores in the glass with this tasty red blend. Very complimentary to each other, the Cabernet fruit essence and Syrah spice offer great flavours to savour. Try with roasted meats, lamb chops or burger sliders.
; consumer_votes=235; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/835348.jpeg; certificates=["BC VQA", "All VQA"]}
  - CEDARCREEK - PLATINUM SYRAH 2021 | $64.90 | stock=29 | in 7 stores | rating=2.8 | https://www.bcliquorstores.com/product/83400 | {sku=83400; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=14.5; sweetness=00; tasting_notes=The Syrah that grows at our southern Okanagan vineyards is situated on unique south-west facing slopes. At midday in summer, the heat is powerful, but Syrah likes that; the terroir evokes its Rhone Valley origins. The wine is structured and balanced with delicate tannins and spice - the direct result of a decision to plant it where it feels right at home.
; consumer_votes=5; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/83400.jpeg; certificates=["BC VQA", "All VQA", "Organic"]}
  - BLACK SAGE VINEYARD OLIVER - SHIRAZ | $32.99 | stock=1503 | in 108 stores | rating=4.1 | https://www.bcliquorstores.com/product/596841 | {sku=596841; product_type=Red Wine; grape_type=SYRAH/SHIRAZ; country=Canada; volume=0.750; alcohol_pct=14.5; sweetness=00; tasting_notes=Black Sage Vineyard expertly crafts big, bold reds. Our wines are a daring expression of the best red varietals crafted in the raw power of the Black Sage Bench in the Okanagan Valley. With over 130 awards since 2017, we invite you to indulge in our award-winning collection. Luxurious dark red fruits, vanilla spice, and a hint of white pepper spice linger on this indulgent Shiraz.
; consumer_votes=26; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/596841.jpeg; certificates=["BC VQA", "All VQA"]}
  - GOLDHILL - CHARISMA RED BLEND 2019 | $17.99 | stock=54 | in 5 stores | rating=4.7 | https://www.bcliquorstores.com/product/770008 | {sku=770008; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=14.5; sweetness=00; tasting_notes=Noted growers then with their own winery and brand, Gold Hill is a southern Okanagan force now led by viticulturist/winemaker Val Tait. A visit in November found a number of options under the Charisma label. Starting with Charisma Red 2019 which is a single vineyard wine—Oxbow Reach in Osoyoos— that is about Syrah, Merlot and Malbec. A good southern Okanagan flavour profile, the herb/spice garrigue of the valley plus red/blue/black fruit notes, a hint of jam and softer tannins. A soothing red for your favourite recipes.
; consumer_votes=73; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/770008.jpeg; certificates=["BC VQA", "All VQA"]}
  - PHANTOM CREEK - QUARTZ AND YARROW SUSTAINABLE RED 2016 | $35.99 | stock=428 | in 45 stores | rating=4.6 | https://www.bcliquorstores.com/product/194330 | {sku=194330; product_type=Red Wine; grape_type=CABERNET BLEND; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=Quartz & Yarrow sources sustainably farmed grapes from across the Okanagan Valley to produce fresh, fruit-forward and perfectly balanced BC VQA wines. This blend of 53% Cabernet Sauvignon, 36% Merlot, 9% Cabernet Franc and 2% Syrah is rich and full-bodied, with aromas and flavours of cherry, black currant, plum and vanilla, ripe tannins and an opulent texture and finish.
; consumer_votes=44; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/194330.jpeg; certificates=["BC VQA", "All VQA"]}
  - IMBZZL OLIVER - RUSE ROSE | $24.99 | stock=1294 | in 107 stores | rating=4.3 | https://www.bcliquorstores.com/product/387299 | {sku=387299; product_type=Rose Wine; grape_type=NOT APPLICABLE; country=Canada; volume=0.750; alcohol_pct=13.9; sweetness=00; tasting_notes=RUSE can easily pass for anything that the South of France can muster. Yet this streetwise Okanagan grown rosé is no mere imposter. This Syrah-dominant blend offers an abundance of vibrant cherry, raspberry and white pepper notes vying to make their intentions known. Deceptively fresh citrus lingers on the finish, keeping your palate in the game no matter what the occasion.
; consumer_votes=32; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/387299.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 6 results)
  - Blasted Church Vineyards Syrah 750 mL | $29.99 | [North Vancouver:0, South Surrey:0, Langley Store:7, Vancouver:0] | https://www.everythingwine.ca/blasted-church-syrah | {sku=37531; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/7/37531_blasted_church_syrah.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Moon Curser Vineyards Syrah 750 mL | $36.98 | [North Vancouver:0, South Surrey:11, Langley Store:6, Vancouver:3] | https://www.everythingwine.ca/moon-curser-syrah | {sku=91843; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/9/1/91843_moon_curser_syrah.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Ex Nihilo Vineyards Reserve Syrah 2021 750 mL | $69.98 | https://www.everythingwine.ca/ex-nihilo-vineyards-reserve-syrah-2021-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Moon Curser Vineyards Dead Of Night Red Blend 750 mL | $50.98 | [North Vancouver:0, South Surrey:0, Langley Store:17, Vancouver:9] | https://www.everythingwine.ca/moon-curser-vineyards-dead-of-night-red-blend-750-ml | {sku=806117; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/8/0/806117_moon_curser_dead_of_night_red.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Le Vieux Pin Washington Petit Rouge 750 mL | $31.98 | https://www.everythingwine.ca/le-vieux-pin-washington-petit-rouge-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - French Door Estate Winery Heritage 2020 750 mL | $64.98 | https://www.everythingwine.ca/french-door-estate-winery-heritage-2020-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 3 results)
  - INNISKILLIN - ESTATE CAB FRANC | $17.99 | stock=17 | https://okanagancellars.com/products/4340630-inniskillin-estate-cab-franc | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000037/0000372461-2735.jpg}
  - OKANAGAN VINEYARDS - CHARDONNAY 2024 | $10.99 | stock=14 | https://okanagancellars.com/products/4857514-okanagan-vineyards-chardonnay-2024 | {category=White Wine; in_stock=True; unit_size=750ml}
  - OKANAGAN VINEYARDS - MERLOT CABERNET | $10.99 | stock=10 | https://okanagancellars.com/products/4746564-okanagan-vineyards-merlot-cabernet | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000012/0000121228-9856.jpg}

#### search_suttonplace_tool (status=ok, 1 results)
  - Meyer Family Vineyards Okanagan Valley Pinot Noir | $33.49 | 2025 | stock=27 | https://store.suttonplacewinemerchant.com/products/4298314-meyer-family-vineyards-okanagan-valley-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000015/0000154310-1810.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 8 results)
  - Nichol 2022 Syrah 'The Village' 750ml | $32.99 | stock=23 | https://www.marquis-wines.com/nichol-2021-syrah-the-village-750ml/ | {sku=1028278; in_stock=True; categories=["Red Wine", "Syrah & Shiraz", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/17368/images/13314/2023-04-17_13.22.31__85735.1681844488.500.500.png?c=2}
  - Okanagan Crushpad 2019 Narrative Non-Fiction 750ml | $16.49 | stock=4 | https://www.marquis-wines.com/okanagan-crushpad-2019-narrative-non-fiction-750ml/ | {sku=1027658; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/16835/images/12571/Narrative-NonFiction-2017-1024x1024__31601.1761843835.500.500.jpg?c=2}
  - Nichol 2022 Syrah "Old Vines" 750ml | $62.99 | stock=2 | https://www.marquis-wines.com/nichol-2019-syrah-old-vines-750ml/ | {sku=1021490; in_stock=True; categories=["Red Wine", "Syrah & Shiraz", "Naramata Bench", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/11170/images/6873/IMG_93441__18478.1655935844.500.500.jpg?c=2}
  - Daydreamer 2022 Amelia Syrah Viognier 750ml | $46.99 | stock=13 | https://www.marquis-wines.com/daydreamer-2022-amelia-syrah-viognier-750ml/ | {sku=1021285; in_stock=True; categories=["Red Wine", "Syrah & Shiraz", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20896/images/16648/2025-09-29_14.38.36__99442.1759340864.500.500.png?c=2}
  - Le Vieux Pin 2023 Cuvee Violette Syrah 750ml | $46.99 | stock=25 | https://www.marquis-wines.com/le-vieux-pin-2022-cuvee-violette-syrah-750ml/ | {sku=1019866; in_stock=True; categories=["Le Vieux Pin & La Stella", "Red Wine", "Syrah & Shiraz", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/16092/images/11835/vieux_pin_violette__21625.1758139060.500.500.jpg?c=2}
  - Domaine Artema 2022 Black Sage Road Rouge 750ml | $24.49 | stock=14 | https://www.marquis-wines.com/domaine-artema-2022-black-sage-road-rouge-750ml/ | {sku=1032199; in_stock=True; categories=["Red Wine", "Syrah & Shiraz", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21816/images/17501/2026-05-15-12.09.58__73486.1779221076.500.500.png?c=2}
  - Le Vieux Pin 2023 Vaila Rose 750ml | $37.99 | stock=2 | https://www.marquis-wines.com/le-vieux-pin-2021-vaila-rose-750ml/ | {sku=1024520; in_stock=True; categories=["Rosé Wine", "British Columbia", "Okanagan", "Le Vieux Pin & La Stella"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/14568/images/10165/2021-04-07_13.35.17__30128.1617904852.500.500.png?c=2}
  - Le Vieux Pin 2024 Petit Rouge 750ml | $32.99 | stock=27 | https://www.marquis-wines.com/le-vieux-pin-2022-petit-rouge-750ml/ | {sku=1021316; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan", "Canada", "Le Vieux Pin & La Stella"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/11068/images/8503/Lindsey_Ail_-_IMG_13861__26749.1586107273.500.500.jpg?c=2}

#### search_legacy_liquor_store_tool (status=ok, 12 results)
  - Inniskillin Shiraz Cabernet | $17.99 | stock=10 | https://www.legacyliquorstore.com/product/wine/inniskillin-shiraz-cabernet-1-x-750ml | {brand=Inniskillin Okanagan; slug=inniskillin-shiraz-cabernet-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Okanagan Spirits Maraschino Liqueur | $37.61 | stock=12 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-maraschino-liqueur-1-x-375ml | {slug=okanagan-spirits-maraschino-liqueur-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["spirits", "liqueurs"]}
  - Okanagan Spirits Amaro Classico | $37.61 | stock=3 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-amaro-classico-1-x-375ml | {slug=okanagan-spirits-amaro-classico-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["spirits", "liqueurs"]}
  - Narrative Two Pinots | $23.88 | stock=12 | https://www.legacyliquorstore.com/product/wine/narrative-two-pinots-1-x-750ml | {brand=Okanagan Crush Pad; slug=narrative-two-pinots-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "blend"]}
  - Narrative Non-Fiction | $29.78 | stock=8 | https://www.legacyliquorstore.com/product/wine/narrative-non-fiction-1-x-750ml | {brand=Okanagan Crush Pad; slug=narrative-non-fiction-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Narrative Red | $23.88 | stock=10 | https://www.legacyliquorstore.com/product/wine/narrative-red-1-x-750ml | {brand=Okanagan Crush Pad; slug=narrative-red-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Okanagan Apple Cider | $14.76 | stock=6 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-crisp-apple-cider-6c-6-x-355ml | {brand=Okanagan Apple Ciders; slug=okanagan-crisp-apple-cider-6c-6-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Spirits Raspberry | $37.99 | stock=4 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-raspberry-1-x-375ml | {brand=Raspberry; slug=okanagan-spirits-raspberry-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["spirits", "liqueurs", "other liqueurs"]}
  - Okanagan Orchard Peach Cider | $15.0 | stock=6 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-orchard-peach-cider-6c-6-x-355ml | {brand=Okanagan Apple Ciders; slug=okanagan-orchard-peach-cider-6c-6-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Apple Cider | $4.45 | stock=24 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-crisp-apple-tc-1-x-473ml | {brand=Okanagan Apple Ciders; slug=okanagan-crisp-apple-tc-1-x-473ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Harvest Pear Cider | $15.5 | stock=6 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-harvest-pear-cider-6c-6-x-355ml | {brand=Okanagan Apple Ciders; slug=okanagan-harvest-pear-cider-6c-6-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Spirits Cherry | $43.88 | stock=3 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-cherry-1-x-375ml | {brand=Cherry Liqueur; slug=okanagan-spirits-cherry-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["spirits", "liqueurs", "other liqueurs"]}

#### search_bcliquor_tool (status=ok, 6 results)
  - INNISKILLIN OKANAGAN - CABERNET FRANC | $17.99 | stock=1661 | in 130 stores | rating=3.9 | https://www.bcliquorstores.com/product/372461 | {sku=372461; product_type=Red Wine; grape_type=CABERNET FRANC; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=Our Estate Series Cabernet Franc has aromas of strawberry with hints of plum and a slight herbaceous note. On the palate, medium tannins with bright acidity complemented by flavours of red cherry, earth tones, and hints of vanilla and spice.
; consumer_votes=23; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/372461.jpeg; certificates=["BC VQA", "All VQA"]}
  - BLACK SAGE VINEYARD OLIVER - CABERNET FRANC 2023 | $32.99 | stock=2570 | in 172 stores | rating=4.0 | https://www.bcliquorstores.com/product/593038 | {sku=593038; product_type=Red Wine; grape_type=CABERNET FRANC; country=Canada; volume=0.750; alcohol_pct=14.5; sweetness=00; tasting_notes=Black Sage Vineyard expertly crafts big, bold reds. Our wines are a daring expression of the best red varietals crafted in the raw power of the Black Sage Bench in the Okanagan Valley. With over 130 awards since 2017, we invite you to indulge in our award-winning collection. Our Cabernet Franc has magnetic aromas of red berries, red currants, strawberries, and mocha. 
; consumer_votes=299; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/593038.jpeg; certificates=["BC VQA", "All VQA"]}
  - BARTIER BROS - CABERNET FRANC 2022 | $29.99 | stock=620 | in 56 stores | rating=4.4 | https://www.bcliquorstores.com/product/993139 | {sku=993139; product_type=Red Wine; grape_type=CABERNET FRANC; country=Canada; volume=0.750; alcohol_pct=14.0; sweetness=00; tasting_notes=Long, long ago the popularity of Merlot found success in the New World including our own Okanagan. Old timers though noted that Cabernet Franc is also an early starter and a good choice for the valley. Many years later the realization is that Cabernet Franc with climate change in the background, is all potential, with the vines getting older and so distinctive in the glass. From the Bartier home Cerquiera vineyard in the heart of the Black Sage zone. Black and blue fruits, sturdy tannins and some Black Sage character denote this wine. 
; consumer_votes=115; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/993139.jpeg; certificates=["BC VQA", "All VQA"]}
  - PHANTOM CREEK ESTATES - ESTATE CABERNET FRANC | $41.99 | stock=1603 | in 117 stores | rating=4.6 | https://www.bcliquorstores.com/product/90203 | {sku=90203; product_type=Red Wine; grape_type=CABERNET FRANC; country=Canada; volume=0.750; alcohol_pct=15.5; sweetness=00; tasting_notes=To create a classic South Okanagan Cabernet Franc, we selected blocks of fruit that displayed great varietal expression from our estate vineyards on the Black Sage Bench and Golden Mile Bench. Our Estate Cabernet Franc is full bodied and delivers ripe black and red bramble berry notes with a lingering sagebrtush finish. This wine will age effortlessly.
; consumer_votes=101; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/90203.jpeg; certificates=["BC VQA", "All VQA"]}
  - PHANTOM CREEK - QUARTZ AND YARROW SUSTAINABLE RED 2016 | $35.99 | stock=428 | in 45 stores | rating=4.6 | https://www.bcliquorstores.com/product/194330 | {sku=194330; product_type=Red Wine; grape_type=CABERNET BLEND; country=Canada; volume=0.750; alcohol_pct=13.5; sweetness=00; tasting_notes=Quartz & Yarrow sources sustainably farmed grapes from across the Okanagan Valley to produce fresh, fruit-forward and perfectly balanced BC VQA wines. This blend of 53% Cabernet Sauvignon, 36% Merlot, 9% Cabernet Franc and 2% Syrah is rich and full-bodied, with aromas and flavours of cherry, black currant, plum and vanilla, ripe tannins and an opulent texture and finish.
; consumer_votes=44; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/194330.jpeg; certificates=["BC VQA", "All VQA"]}
  - PHANTOM CREEK ESTATES - BECKER VINEYARD CUVEE | $68.99 | stock=327 | in 34 stores | rating=4.4 | https://www.bcliquorstores.com/product/58459 | {sku=58459; product_type=Red Wine; grape_type=OTHER BLEND; country=Canada; volume=0.750; alcohol_pct=14.1; sweetness=00; tasting_notes=It has now been over 25 years since Becker Vineyard was replanted to Cabernet family varieties, proving that late ripening red varieties could thrive in the South Okanagan. First planted in 1977 as part of the pioneering Becker Project, Becker Vineyard produces finessed, elegant wines from the upper terrace of the Black Sage Bench. Nestled against the Okanagan Highland mountains, the Becker vineyard sits on the upper terrace of the Black Sage Bench. At a higher elevation, the vineyard enjoys a gradual growing season and maintains a sense of vibrancy and freshness.The nose of this wine exhibits ripe baked fruit notes of dark cherry and black currant combined with subtle savoury notes of black sage and forest floor. This Cabernet Franc dominant Bordeaux blend has a complex and balanced palate offering layers of ripe red bramble fruit with herbaceous and peppery undertones. The mouthfeel is smooth and supple with finegrained tannins and a long satisfying finish.
; consumer_votes=31; is_bc_vqa=True; image_url=http://www.bcliquorstores.com/sites/default/files/imagecache/height400px/58459.jpeg; certificates=["BC VQA", "All VQA"]}

#### search_everything_wine_tool (status=ok, 12 results)
  - Inniskillin Okanagan Cabernet Franc 750 mL | $17.99 | [North Vancouver:0, South Surrey:0, Langley Store:7, Vancouver:0] | https://www.everythingwine.ca/inniskillin-okanagan-cabernet-franc-750-ml | {sku=372461; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/7/372461_inniskillin_okanagan_cabernet_franc_750_ml.jpeg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Narrative by Okanagan Crush Pad Cabernet Franc 750 mL | $29.99 | [North Vancouver:1, South Surrey:0, Langley Store:18, Vancouver:0] | https://www.everythingwine.ca/okanagan-crush-pad-winery-narrative-cabernet-franc-750-ml | {sku=232810; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/3/232810_narrative_cabernet_franc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "unavailable"}, {"method": "Check other stores", "status": "other-store"}]}
  - Blasted Church Vineyards Cabernet Franc 750 mL | $34.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:10] | https://www.everythingwine.ca/blasted-church-vineyards-okanagan-valley-cabernet-franc-750-ml | {sku=141232; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/4/141232_blasted_church_vineyards_cabernet_franc_750_ml.jpeg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Free Form By Okanagan Crush Pad Cabernet Franc 750 mL | $43.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:13] | https://www.everythingwine.ca/free-form-by-okanagan-crush-pad-okanagan-valley-cabernet-franc-750-ml | {sku=202849; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/0/202849_free_form_cab_franc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Fairview Cellars Premier Series Cabernet Franc 750 mL | $41.98 | https://www.everythingwine.ca/fairview-cellars-cabernet-franc-premier-series-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Country Vines Cabernet Franc 750 mL | $25.98 | [North Vancouver:0, South Surrey:0, Langley Store:11, Vancouver:10] | https://www.everythingwine.ca/country-vines-cabernet-franc-750-ml | {sku=730273; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/3/730273_country-vines-cabernet-franc-750-ml.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Rust Wine Co. Cabernet Franc 750 mL | $29.99 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:8] | https://www.everythingwine.ca/rust-wine-co-ok-falls-cabernet-franc-750-ml | {sku=150439; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/1/5/150439_rust_wine_co_cabernet_franc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Free Form By Okanagan Crush Pad Rose 750 mL | $31.98 | [North Vancouver:0, South Surrey:0, Langley Store:0, Vancouver:21] | https://www.everythingwine.ca/free-form-by-okanagan-crush-pad-rose-750-ml | {sku=228180; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/2/2/228180_free_form_rose.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Mission Hill Family Estate Compendium 2020 Red Blend 750 mL | $90.98 | [North Vancouver:2, South Surrey:7, Langley Store:9, Vancouver:15] | https://www.everythingwine.ca/mission-hill-family-estate-compendium-2020-red-blend-750-ml | {sku=385939; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/3/8/385939_mission-hill-family-estate-compendium-2020-red-blend-750-ml.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Black Hills Estate Winery Nota Bene Red Blend 750 mL | $69.99 | [North Vancouver:3, South Surrey:8, Langley Store:6, Vancouver:30] | https://www.everythingwine.ca/black-hills-nota-bene | {sku=708073; country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/7/0/708073_black-hills-estate-winery-nota-bene-red-blend-750-ml.gif?quality=80&bg-color=255,255,255&fit=bounds&height=366&width=366&canvas=366:366; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - Le Vieux Pin Washington Petit Rouge 750 mL | $31.98 | https://www.everythingwine.ca/le-vieux-pin-washington-petit-rouge-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}
  - French Door Estate Winery Heritage 2020 750 mL | $64.98 | https://www.everythingwine.ca/french-door-estate-winery-heritage-2020-750-ml | {country=Canada; image_url=https://www.everythingwine.ca/media/catalog/product/placeholder/default/Placeholder_Image_red_2025_1.jpg; stock=[{"method": "Warehouse delivery", "status": "available"}, {"method": "Pick up, delivery from store", "status": "available"}]}

#### search_okanagan_cellars_tool (status=ok, 3 results)
  - INNISKILLIN - ESTATE CAB FRANC | $17.99 | stock=17 | https://okanagancellars.com/products/4340630-inniskillin-estate-cab-franc | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000037/0000372461-2735.jpg}
  - OKANAGAN VINEYARDS - CHARDONNAY 2024 | $10.99 | stock=14 | https://okanagancellars.com/products/4857514-okanagan-vineyards-chardonnay-2024 | {category=White Wine; in_stock=True; unit_size=750ml}
  - OKANAGAN VINEYARDS - MERLOT CABERNET | $10.99 | stock=10 | https://okanagancellars.com/products/4746564-okanagan-vineyards-merlot-cabernet | {category=Red Wine; in_stock=True; unit_size=750ml; image_url=https://okanagancellars.com/static/custom/goods/131/000012/0000121228-9856.jpg}

#### search_suttonplace_tool (status=ok, 1 results)
  - Meyer Family Vineyards Okanagan Valley Pinot Noir | $33.49 | 2025 | stock=27 | https://store.suttonplacewinemerchant.com/products/4298314-meyer-family-vineyards-okanagan-valley-pinot-noir | {category=RED BC; in_stock=True; unit_size=750ML Bottle; image_url=https://store.suttonplacewinemerchant.com/static/custom/goods/124/000015/0000154310-1810.jpg; country=CANADA; varietal=Pinot Noir; alcohol_pct=13.50; is_staff_pick=False; is_featured=False}

#### search_marquis_tool (status=ok, 20 results)
  - Okanagan Crushpad 2019 Narrative Cabernet Franc 750ml | $16.49 | stock=1 | https://www.marquis-wines.com/okanagan-crushpad-2019-narrative-cabernet-franc-750ml/ | {sku=1021466; in_stock=True; categories=["Red Wine", "Cabernet Franc", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21497/images/17145/narrative-cab-franc__82547.1771974792.500.500.png?c=2}
  - Lock & Worth 2025 Cabernet Franc Rose 750ml | $29.99 | stock=7 | https://www.marquis-wines.com/lock-worth-2022-cabernet-franc-rose-750ml/ | {sku=1019489; in_stock=True; categories=["Rosé Wine", "Naramata Bench", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9522/images/12107/lock_worth_greay_label_rose__77396.1654899741.500.500.png?c=2}
  - Burrowing Owl 2022 Cabernet Franc 750ml | $42.99 | stock=19 | https://www.marquis-wines.com/burrowing-owl-2022-cabernet-franc-750ml/ | {sku=556621; in_stock=True; categories=["Red Wine", "Cabernet Franc", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20920/images/16669/burrowing_owl_franc__20214.1760725789.500.500.jpg?c=2}
  - Tinhorn Creek 2023 Cabernet Franc 750ml | $27.99 | stock=47 | https://www.marquis-wines.com/tinhorn-creek-2023-cabernet-franc-750ml/ | {sku=530717; in_stock=True; categories=["Red Wine", "Red Blends", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/9723/images/5511/2014-tinhorn-creek-cab-franc-vqa__10878.1779383184.500.500.jpg?c=2}
  - Nichol 2022 Cabernet Franc 'The Village' 750ml | $32.99 | stock=4 | https://www.marquis-wines.com/nichol-2022-cabernet-franc-the-village-750ml/ | {sku=1030412; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Cabernet Franc", "Celebrate BC Wine Month"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19423/images/15276/2024-10-29-11.34.44__90023.1730308360.500.500.png?c=2}
  - Tantalus 2022 Cabernet Franc 750ml | $36.99 | stock=16 | https://www.marquis-wines.com/tantalus-2022-cabernet-franc-750ml/ | {sku=1029801; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Cabernet Franc", "Drink Local"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18670/images/14640/2024-05-08_11.38.04__97448.1715278618.500.500.png?c=2}
  - Synchromesh 2022 Storm Haven Cabernet Franc 750ml | $38.99 | stock=2 | https://www.marquis-wines.com/synchromesh-2022-storm-haven-cabernet-franc-750ml/ | {sku=1024164; in_stock=True; categories=["Red Wine", "British Columbia", "Okanagan", "Canada", "Cabernet Franc"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19917/images/15695/2025-02-03-15.48.24__56977.1738705473.500.500.png?c=2}
  - Hester Creek 2022 Old Vines Cabernet Franc 750ml | $31.99 | stock=2 | https://www.marquis-wines.com/hester-creek-2022-old-vines-cabernet-franc-750ml/ | {sku=1007582; in_stock=True; categories=["Red Wine", "Cabernet Franc", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/18350/images/14180/IMG_7421__77685.1704395713.500.500.png?c=2}
  - Moraine Estate 2024 Cabernet Merlot 750ml | $27.99 | stock=3 | https://www.marquis-wines.com/moraine-estate-2024-cabernet-merlot-750ml/ | {sku=1031616; in_stock=True; categories=["Red Wine", "Cabernet Franc", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/20962/images/16740/2025-11-05_14.44.52__86340.1762449427.500.500.png?c=2}
  - Okanagan Crushpad 2019 Narrative Non-Fiction 750ml | $16.49 | stock=4 | https://www.marquis-wines.com/okanagan-crushpad-2019-narrative-non-fiction-750ml/ | {sku=1027658; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/16835/images/12571/Narrative-NonFiction-2017-1024x1024__31601.1761843835.500.500.jpg?c=2}
  - Mission Hill Five Vineyards Cabernet/Merlot 750ml | $20.99 | stock=68 | https://www.marquis-wines.com/mission-hill-2018-five-vineyards-cabernet-merlot-750ml/ | {sku=257816; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Red Blends", "Merlot", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/6097/images/5467/five-vienyards-mission-hill-2014-cab-merlot__34443.1504217533.500.500.jpg?c=2}
  - Maverick 2022 Rubeus 750ml | $27.99 | stock=11 | https://www.marquis-wines.com/maverick-2022-rubeus-750ml/ | {sku=1016248; in_stock=True; categories=["Red Wine", "Cabernet Franc", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21512/images/17188/IMG_0677__42929.1772840208.500.500.png?c=2}
  - Hester Creek 2022 Cabernet/Merlot 750ml | $23.99 | stock=17 | https://www.marquis-wines.com/hester-creek-2022-cabernet-merlot-750ml/ | {sku=1007410; in_stock=True; categories=["Red Wine", "Cabernet Sauvignon", "Merlot", "British Columbia", "Okanagan", "Oliver"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/12362/images/13140/Hester_Creek_Cab_Merlot__53582.1753818511.500.500.png?c=2}
  - La Stella 2025 LaStellina Rosato 750ml | $31.99 (reg $31.99) | stock=1 | https://www.marquis-wines.com/la-stella-2025-lastellina-rosato-750ml/ | {sku=1018696; in_stock=True; categories=["Rosé Wine", "British Columbia", "Okanagan", "On Sale"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/16178/images/11961/2022-04-28_14.53.57__80119.1779914210.500.500.png?c=2}
  - Ursa Major 2025 Rose 750ml | $37.99 | stock=26 | https://www.marquis-wines.com/ursa-major-2025-rose-750ml/ | {sku=1032124; in_stock=True; categories=["Organic / Biodynamic Wine", "Rosé Wine", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21637/images/17316/2026-03-30-13.14.08__34450.1775070501.500.500.png?c=2}
  - La Stella 2023 Fortissimo 750ml | $40.99 | stock=15 | https://www.marquis-wines.com/la-stella-2022-fortissimo-750ml/ | {sku=1018686; in_stock=True; categories=["Le Vieux Pin & La Stella", "Red Wine", "Red Blends", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/11043/images/6684/IMG_9150%25281%2529__16746.1740698127.500.500.jpg?c=2}
  - Black Hills 2022 Nota Bene 750ml | $72.99 | stock=21 | https://www.marquis-wines.com/black-hills-2022-nota-bene-750ml/ | {sku=708073; in_stock=True; categories=["Celebrate BC Wine Month", "Drink Local", "Red Wine", "Red Blends", "British Columbia", "Okanagan Falls"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/7944/images/9204/2020-10-01-15.42.34__26769.1780440169.500.500.jpg?c=2}
  - Domaine Artema 2022 Black Sage Road Rouge 750ml | $24.49 | stock=14 | https://www.marquis-wines.com/domaine-artema-2022-black-sage-road-rouge-750ml/ | {sku=1032199; in_stock=True; categories=["Red Wine", "Syrah & Shiraz", "Canada", "British Columbia", "Okanagan"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/21816/images/17501/2026-05-15-12.09.58__73486.1779221076.500.500.png?c=2}
  - Mission Hill 2020 Oculus Estate 750ml | $229.99 | stock=11 | https://www.marquis-wines.com/mission-hill-2020-oculus-estate-750ml/ | {sku=1030217; in_stock=True; categories=["Red Wine", "Red Blends", "95+ Point Wines", "British Columbia", "Okanagan", "Canada"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19225/images/14982/2024-08-20_15.35.18__03695.1724273240.500.500.png?c=2}
  - La Stella 2022 Espressivo 750ml | $51.99 | stock=23 | https://www.marquis-wines.com/la-stella-2020-espressivo-750ml/ | {sku=1024635; in_stock=True; categories=["Red Wine", "Red Blends", "British Columbia", "Okanagan", "Canada", "Le Vieux Pin & La Stella"]; image_url=https://cdn11.bigcommerce.com/s-oyi93ews/products/19089/images/14914/2024-07-18-14.17.19__78254.1721408074.500.500.png?c=2}

#### search_legacy_liquor_store_tool (status=ok, 12 results)
  - Inniskillin Shiraz Cabernet | $17.99 | stock=10 | https://www.legacyliquorstore.com/product/wine/inniskillin-shiraz-cabernet-1-x-750ml | {brand=Inniskillin Okanagan; slug=inniskillin-shiraz-cabernet-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Okanagan Spirits Maraschino Liqueur | $37.61 | stock=12 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-maraschino-liqueur-1-x-375ml | {slug=okanagan-spirits-maraschino-liqueur-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["spirits", "liqueurs"]}
  - Okanagan Spirits Amaro Classico | $37.61 | stock=3 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-amaro-classico-1-x-375ml | {slug=okanagan-spirits-amaro-classico-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["spirits", "liqueurs"]}
  - Narrative Two Pinots | $23.88 | stock=12 | https://www.legacyliquorstore.com/product/wine/narrative-two-pinots-1-x-750ml | {brand=Okanagan Crush Pad; slug=narrative-two-pinots-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "white wine", "blend"]}
  - Narrative Non-Fiction | $29.78 | stock=8 | https://www.legacyliquorstore.com/product/wine/narrative-non-fiction-1-x-750ml | {brand=Okanagan Crush Pad; slug=narrative-non-fiction-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Narrative Red | $23.88 | stock=10 | https://www.legacyliquorstore.com/product/wine/narrative-red-1-x-750ml | {brand=Okanagan Crush Pad; slug=narrative-red-1-x-750ml; is_staff_pick=False; is_new_arrival=False; country=Canada; region=British Columbia; in_stock=True; tags=["wine", "red wine", "blend"]}
  - Okanagan Apple Cider | $14.76 | stock=6 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-crisp-apple-cider-6c-6-x-355ml | {brand=Okanagan Apple Ciders; slug=okanagan-crisp-apple-cider-6c-6-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Spirits Raspberry | $37.99 | stock=4 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-raspberry-1-x-375ml | {brand=Raspberry; slug=okanagan-spirits-raspberry-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["spirits", "liqueurs", "other liqueurs"]}
  - Okanagan Orchard Peach Cider | $15.0 | stock=6 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-orchard-peach-cider-6c-6-x-355ml | {brand=Okanagan Apple Ciders; slug=okanagan-orchard-peach-cider-6c-6-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Apple Cider | $4.45 | stock=24 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-crisp-apple-tc-1-x-473ml | {brand=Okanagan Apple Ciders; slug=okanagan-crisp-apple-tc-1-x-473ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Harvest Pear Cider | $15.5 | stock=6 | https://www.legacyliquorstore.com/product/beer-cider/okanagan-harvest-pear-cider-6c-6-x-355ml | {brand=Okanagan Apple Ciders; slug=okanagan-harvest-pear-cider-6c-6-x-355ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["beer / cider", "cider"]}
  - Okanagan Spirits Cherry | $43.88 | stock=3 | https://www.legacyliquorstore.com/product/spirits/okanagan-spirits-cherry-1-x-375ml | {brand=Cherry Liqueur; slug=okanagan-spirits-cherry-1-x-375ml; is_staff_pick=False; is_new_arrival=False; country=Canada; in_stock=True; tags=["spirits", "liqueurs", "other liqueurs"]}

````

</details>

### Latency

- 102.74s
