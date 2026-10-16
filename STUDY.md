# 1¢ Study

*Updated Fri Oct 16, 1:13 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 52 finished bets | 2% | $6.20 | +79% | +11.92¢ | -$3.90 / $10.10 |

*Expect about **3 buys a day**, roughly **$0.47/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 52 | -$1.05 | -13% |
| ESPN win probability ≥ 2%, sell at 25¢ | 52 | -$4.49 | -58% |
| ESPN win probability ≥ 2%, sell at 2¢ | 52 | -$4.94 | -63% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 16047 | 1131 | 7 (1%) | 1.1% | -$71.65 (-42%) | Hold to the end: -$71.65 (-42%) |

*In play right now: 32. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 234 | 3.3% | 0.4% (1) | -46% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 234 | 1 | -60% | -74% | -74% | -72% |
| ESPN win probability ≥ 2% | 52 | 1 | +79% | -63% | -65% | -75% |
| ESPN win probability ≥ 5% | 25 | 1 | +273% | -79% | -79% | -83% |
| ESPN win probability ≥ 10% | 16 | 1 | +483% | -78% | -68% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1131 | 15% | 10% | 7% | 4% | 1% | 1% |
| Unverified | 14884 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 1% | -$71.65 | -42% |
| Sell at 2¢ | 165 | 15% | -$126.75 | -75% |
| Sell at 3¢ | 114 | 10% | -$125.19 | -74% |
| Sell at 5¢ | 79 | 7% | -$118.30 | -70% |
| Sell at 10¢ | 43 | 4% | -$113.32 | -67% |
| Sell at 25¢ | 14 | 1% | -$123.31 | -73% |
| Sell at 50¢ | 10 | 1% | -$102.15 | -60% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 5830 | 4 | 0% | 0% | -94% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 730 | 1 | 12% | 5% | -87% | -80% | 4 min |
| Counter-Strike 2 Game | ✘ | 684 | 1 | 5% | 2% | -86% | -92% | 11 min |
| ITF Men's Match | ✘ | 667 | 1 | 12% | 6% | -86% | -80% | 5 min |
| eBasketball Game | ✘ | 581 | 1 | 0% | 0% | -84% | -83% | 2 min |
| Challenger ATP  | ✘ | 478 | 2 | 10% | 3% | -61% | -83% | 5 min |
| TT Star Series Match | ✘ | 317 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Russia Liga Pro Match | ✘ | 219 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Darts Match | ✘ | 208 | 0 | 0% | 0% | -100% | -99% | 8 min |
| College Football Game | partly | 195 | 2 | 14% | 7% | -4% | -76% | 30 min |
| Men's T20 Cricket Match | ✘ | 167 | 1 | 13% | 4% | -44% | -77% | 23 min |
| Women's College Volleyball Match | ✘ | 165 | 2 | 7% | 3% | +13% | -87% | 91 min |
| Challenger WTA | ✘ | 149 | 0 | 12% | 5% | -100% | -79% | 8 min |
| Dota 2 Game | ✘ | 147 | 0 | 1% | 1% | -100% | -98% | 29 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 128 | 0 | 7% | 2% | -100% | -88% | 11 min |
| NHL Game | ✔ | 117 | 0 | 13% | 6% | -100% | -78% | 5 min |
| Serie C Game | ✘ | 113 | 1 | 4% | 2% | -17% | -92% | 8 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Major League Soccer Game | partly | 69 | 1 | 12% | 3% | +35% | -80% | 8 min |
| Brasileiro Serie B Game | ✘ | 66 | 0 | 5% | 2% | -100% | -92% | 10 min |
| KHL Game | ✘ | 65 | 0 | 3% | 2% | -100% | -95% | 5 min |
| AHL Game | ✘ | 63 | 0 | 3% | 2% | -100% | -94% | 6 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| R6 Game | ✘ | 62 | 0 | 6% | 3% | -100% | -89% | 9 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Argentina Primera Division Game | ✘ | 57 | 0 | 16% | 5% | -100% | -73% | 6 min |
| Overwatch Game | ✘ | 56 | 0 | 4% | 0% | -100% | -94% | 5 min |
| Ettan Game | ✘ | 55 | 0 | 7% | 2% | -100% | -87% | 6 min |
| NBA Game | ✔ | 53 | 0 | 13% | 4% | -100% | -77% | 7 min |
| Argentine Nacional B Game | ✘ | 51 | 0 | 10% | 10% | -100% | -83% | 10 min |
| Liga Leumit Game | ✘ | 50 | 0 | 2% | 2% | -100% | -97% | 64 min |
| KBO Game | ✘ | 50 | 0 | 8% | 6% | -100% | -86% | 4 min |
| Liga DIMAYOR Game | ✘ | 49 | 1 | 12% | 4% | +90% | -79% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| WTA Tennis Match | ✘ | 46 | 0 | 11% | 0% | -100% | -81% | 3 min |
| USL Championship Game | partly | 45 | 0 | 11% | 2% | -100% | -81% | 4 min |
| Brasileiro Serie A Game | partly | 45 | 1 | 22% | 13% | +107% | -61% | 7 min |
| LaLiga 2 Game | partly | 44 | 0 | 16% | 7% | -100% | -72% | 8 min |
| Liiga Game | ✘ | 44 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Euroleague Game | ✘ | 44 | 0 | 25% | 7% | -100% | -57% | 14 min |
| EuroCup Basketball Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 9 min |
| German 3. Liga Game | ✘ | 42 | 0 | 14% | 7% | -100% | -75% | 7 min |
| LNBP Basketball Game | ✘ | 40 | 0 | 8% | 0% | -100% | -87% | 16 min |
| Japan J2 League Game | ✘ | 40 | 0 | 12% | 2% | -100% | -78% | 8 min |
| ELH Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Uruguay Primera Division Game | ✘ | 38 | 0 | 8% | 5% | -100% | -86% | 10 min |
| ATP Tennis Match | ✘ | 38 | 0 | 11% | 5% | -100% | -82% | 3 min |
| Slovakian 2. Liga Game | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 107 min |
| UEFA Champions League Game | partly | 37 | 1 | 14% | 5% | +152% | -77% | 12 min |
| National League Game | ✘ | 36 | 1 | 3% | 3% | +159% | -95% | 5 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| SHL Game | ✘ | 35 | 0 | 3% | 3% | -100% | -95% | 5 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| Liga Expansion Game | ✘ | 33 | 0 | 9% | 6% | -100% | -84% | 11 min |
| TFF 1. Lig Game | ✘ | 33 | 0 | 15% | 6% | -100% | -74% | 10 min |
| EFL Championship Game | ✔ | 33 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Japan NPB Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 2 min |
| NFL Game | ✔ | 32 | 1 | 19% | 6% | +192% | -68% | 3 min |
| Valorant game winner | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 15 min |
| DEL Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 4 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Mobile Legends Bang Bang Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Chinese Basketball Association Game  | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Czech National Football League Game | ✘ | 27 | 0 | 11% | 11% | -100% | -81% | 10 min |
| Tweede Divisie Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| China League 1 Game | ✘ | 25 | 0 | 12% | 8% | -100% | -79% | 6 min |
| Finland Korisliiga Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Indonesia Super League Game | ✘ | 24 | 0 | 17% | 8% | -100% | -71% | 8 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Saudi Pro League Game | ✘ | 22 | 0 | 23% | 14% | -100% | -61% | 15 min |
| Bundesliga 2 Game | ✔ | 22 | 0 | 14% | 9% | -100% | -76% | 5 min |
| Women's T20 Match | ✘ | 21 | 0 | 24% | 14% | -100% | -59% | 30 min |
| Polish Ekstraklasa Game | ✘ | 21 | 0 | 14% | 5% | -100% | -75% | 10 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Sweden SBL Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Peru Liga 1 Game | ✘ | 20 | 0 | 25% | 20% | -100% | -57% | 7 min |
| Adriatic ABA Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Italy Serie A2 Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 5 min |
| College Hockey Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Japan J League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 12 min |
| Liga MX Game | ✔ | 19 | 0 | 16% | 16% | -100% | -73% | 1 min |
| Australia NBL Game | ✘ | 19 | 0 | 5% | 0% | -100% | -91% | 5 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| LNB Elite 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Serie A Game | ✔ | 19 | 0 | 11% | 11% | -100% | -82% | 11 min |
| Men's ODI Cricket Match | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 24 min |
| Czech NBL Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Spain Liga ACB Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 18 min |
| Thai League 1 Game | ✘ | 18 | 0 | 22% | 0% | -100% | -61% | 8 min |
| Turkish Super Lig Game | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 13 min |
| Eredivisie Game | ✔ | 18 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Ligue 2 Game | ✘ | 18 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Ligue 1 Game | ✔ | 18 | 0 | 17% | 11% | -100% | -71% | 10 min |
| La Liga Game | ✔ | 18 | 0 | 44% | 33% | -100% | -23% | 9 min |
| APF Division de Honor Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 5 min |
| Canadian Premier League | ✘ | 17 | 1 | 24% | 24% | +449% | -59% | 29 min |
| EFL League One Game | ✔ | 17 | 0 | 12% | 0% | -100% | -80% | 2 min |
| Chinese Super League Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 16 min |
| Czech First League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 10 min |
| Allsvenskan Game | ✘ | 17 | 0 | 18% | 18% | -100% | -69% | 14 min |
| LNB Elite Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Italy Serie A Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 6 min |
| Korea K-League 2 Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 6 min |
| Eliteserien Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 9 min |
| Serie B Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 15 min |
| Ecuador Liga Pro Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 6 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Russia VTB United Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 17 min |
| Austria BSL Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| Turkey BSL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 9 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Danish Superliga Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
| Bolivia Premier Division Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| English Premier League Game | ✔ | 14 | 0 | 7% | 7% | -100% | -88% | 7 min |
| Serbian SuperLiga Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Israeli Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Super League Greece Game | ✘ | 14 | 0 | 21% | 7% | -100% | -63% | 13 min |
| Venezuela Liga FUTVE game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 10 min |
| Egyptian Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Women's ODI Cricket Match | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 56 min |
| Slovakia SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Croatia Premijer Liga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Vietnam V-League 1 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Korea K League Game | ✘ | 12 | 0 | 42% | 17% | -100% | -28% | 14 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| FIBA Europe Cup Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Slovenia 1. SKL Game | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 15 min |
| Finnish Ykkosliiga Game | ✘ | 11 | 1 | 9% | 9% | +748% | -84% | 15 min |
| Croatia HNL Game | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 20 min |
| Latvian Virsliga Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 17 min |
| Slovenian Prva Liga Game | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 12 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Singapore Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 17 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| LKL Lithuania Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Bundesliga Game | ✔ | 9 | 1 | 22% | 22% | +937% | -61% | 13 min |
| England Super League Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| CFL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Scottish Premiership Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 39 min |
| FIBA Champions League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Korea KBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 11 min |
| CONMEBOL Sudamericana Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Men's Iceland Basketball Premier League Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 21 min |
| UAE Pro League | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 29 min |
| Qatar Stars League | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 33 min |
| Colombia LBP Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Japan B League Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 7 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Liga Nacional de Basquetbol Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Taca de Portugal Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 41 min |
| Australian A League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Malaysia Super League Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 59 min |
| Indian Super League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Romanian Liga I Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 11 min |
| German Women's Bundesliga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 18 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| BNXT League Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 15 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 466 | 5% | 1% | 0% | -91% |
| 5–15 min | 236 | 17% | 7% | 1% | -70% |
| 15–30 min | 161 | 32% | 18% | 2% | -45% |
| 30–60 min | 135 | 18% | 10% | 0% | -69% |
| Over 60 min | 122 | 20% | 11% | 0% | -66% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 47 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-16 19:13 | Eerste Divisie Game | Helmond | ✘ | — | — | In play | — |
| 10-16 19:11 | Austrian Bundesliga Game | Tie | ✘ | — | — | In play | — |
| 10-16 19:10 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-16 19:10 | eSoccer Game | Real Madrid (SilentShooter) | ✘ | — | — | In play | — |
| 10-16 19:08 | eSoccer Game | Aston Villa (Castle) | ✘ | — | — | In play | — |
| 10-16 19:08 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-16 19:07 | Ligue 2 Game | Stade Lavallois | ✘ | — | — | In play | — |
| 10-16 19:07 | Sweden SBL Game | Nassjo Basket | ✘ | — | — | In play | — |
| 10-16 19:05 | eSoccer Game | France (Annie) | ✘ | — | — | In play | — |
| 10-16 19:05 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-16 19:05 | Russia Liga Pro Match | Denisov Artem Igorevich | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 19:05 | Counter-Strike 2 Game | Sangal | ✘ | — | — | In play | — |
| 10-16 19:04 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 19:03 | eSoccer Game | Arsenal (Kylian) | ✘ | — | — | In play | — |
| 10-16 19:03 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-16 19:03 | eSoccer Game | Portugal (Olive) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 19:03 | TT Star Series Match | Hencl Ivan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 19:01 | Russia Liga Pro Match | Kalashnikov Evgeny Igorevich | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 19:00 | Austrian Bundesliga Game | Hartberg | ✘ | — | — | In play | — |
| 10-16 18:57 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 18:56 | Austria BSL Game | SKN St. Polten Basketball | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 18:55 | Ettan Game | Tie | ✘ | — | — | In play | — |
| 10-16 18:55 | eSoccer Game | Juventus (Haze) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 18:54 | Russia Liga Pro Match | KHarlamov Dmitrii Olegovich | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 18:53 | National League Game | EHC Kloten | ✘ | — | — | In play | — |
| 10-16 18:53 | eSoccer Game | Brighton (Fernando) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 18:53 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 18:52 | German 3. Liga Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 18:52 | eSoccer Game | France (Annie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 18:52 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
