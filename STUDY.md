# 1¢ Study

*Updated Sun Oct 18, 7:39 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 60 finished bets | 2% | $5.00 | +56% | +8.33¢ | -$4.50 / $9.50 |

*Expect about **3 buys a day**, roughly **$0.49/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 60 | -$2.25 | -25% |
| ESPN win probability ≥ 2%, sell at 25¢ | 60 | -$5.69 | -63% |
| ESPN win probability ≥ 2%, sell at 2¢ | 60 | -$5.88 | -65% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 19198 | 1380 | 7 (1%) | 1.1% | -$109.00 (-53%) | Hold to the end: -$109.00 (-53%) |

*In play right now: 38. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 268 | 3.3% | 0.4% (1) | -55% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 268 | 1 | -65% | -75% | -76% | -74% |
| ESPN win probability ≥ 2% | 60 | 1 | +56% | -65% | -70% | -78% |
| ESPN win probability ≥ 5% | 29 | 1 | +222% | -82% | -82% | -85% |
| ESPN win probability ≥ 10% | 18 | 1 | +419% | -81% | -71% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1380 | 14% | 9% | 7% | 3% | 1% | 1% |
| Unverified | 17780 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 1% | -$109.00 | -53% |
| Sell at 2¢ | 196 | 14% | -$156.04 | -75% |
| Sell at 3¢ | 131 | 9% | -$155.91 | -75% |
| Sell at 5¢ | 91 | 7% | -$147.85 | -71% |
| Sell at 10¢ | 47 | 3% | -$145.43 | -70% |
| Sell at 25¢ | 15 | 1% | -$157.35 | -76% |
| Sell at 50¢ | 10 | 1% | -$139.50 | -67% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 7155 | 4 | 1% | 1% | -95% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 766 | 1 | 12% | 5% | -88% | -79% | 4 min |
| eBasketball Game | ✘ | 729 | 1 | 0% | 0% | -87% | -87% | 2 min |
| Counter-Strike 2 Game | ✘ | 720 | 1 | 5% | 2% | -87% | -92% | 11 min |
| ITF Men's Match | ✘ | 700 | 1 | 12% | 6% | -87% | -79% | 5 min |
| Challenger ATP  | ✘ | 511 | 2 | 10% | 4% | -63% | -82% | 5 min |
| Russia Liga Pro Match | ✘ | 476 | 0 | 0% | 0% | -100% | -100% | 4 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 262 | 2 | 13% | 7% | -29% | -77% | 24 min |
| Darts Match | ✘ | 226 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Women's College Volleyball Match | ✘ | 190 | 2 | 7% | 3% | -2% | -88% | 80 min |
| Men's T20 Cricket Match | ✘ | 174 | 1 | 13% | 4% | -46% | -78% | 25 min |
| Dota 2 Game | ✘ | 164 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Challenger WTA | ✘ | 158 | 0 | 12% | 4% | -100% | -79% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Serie C Game | ✘ | 139 | 1 | 5% | 3% | -33% | -91% | 8 min |
| NHL Game | ✔ | 133 | 0 | 13% | 6% | -100% | -78% | 5 min |
| League of Legends Game | ✘ | 132 | 0 | 8% | 2% | -100% | -87% | 11 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Major League Soccer Game | partly | 97 | 1 | 11% | 4% | -4% | -80% | 6 min |
| AHL Game | ✘ | 87 | 0 | 2% | 1% | -100% | -96% | 5 min |
| Ettan Game | ✘ | 77 | 0 | 5% | 1% | -100% | -91% | 6 min |
| Brasileiro Serie B Game | ✘ | 74 | 0 | 8% | 3% | -100% | -86% | 10 min |
| Argentina Primera Division Game | ✘ | 71 | 0 | 14% | 6% | -100% | -76% | 7 min |
| Overwatch Game | ✘ | 70 | 0 | 3% | 0% | -100% | -95% | 5 min |
| KHL Game | ✘ | 69 | 0 | 3% | 1% | -100% | -95% | 5 min |
| WTA Tennis Match | ✘ | 68 | 0 | 12% | 1% | -100% | -80% | 4 min |
| Argentine Nacional B Game | ✘ | 66 | 0 | 9% | 9% | -100% | -84% | 10 min |
| R6 Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 9 min |
| USL Championship Game | partly | 66 | 0 | 14% | 3% | -100% | -76% | 5 min |
| NBA Game | ✔ | 64 | 0 | 12% | 3% | -100% | -78% | 7 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Japan J2 League Game | ✘ | 60 | 0 | 15% | 7% | -100% | -74% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| ATP Tennis Match | ✘ | 56 | 0 | 11% | 4% | -100% | -81% | 3 min |
| German 3. Liga Game | ✘ | 56 | 0 | 12% | 5% | -100% | -78% | 7 min |
| Liga DIMAYOR Game | ✘ | 55 | 1 | 13% | 4% | +70% | -78% | 7 min |
| Brasileiro Serie A Game | partly | 55 | 1 | 18% | 11% | +70% | -68% | 8 min |
| LaLiga 2 Game | partly | 54 | 0 | 20% | 11% | -100% | -65% | 8 min |
| EFL Championship Game | ✔ | 53 | 0 | 8% | 4% | -100% | -87% | 8 min |
| KBO Game | ✘ | 52 | 0 | 10% | 6% | -100% | -83% | 4 min |
| Liiga Game | ✘ | 52 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Liga Leumit Game | ✘ | 50 | 0 | 2% | 2% | -100% | -97% | 64 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Euroleague Game | ✘ | 49 | 0 | 24% | 8% | -100% | -58% | 14 min |
| National League Game | ✘ | 49 | 1 | 2% | 2% | +90% | -96% | 5 min |
| Slovakian 2. Liga Game | ✘ | 48 | 0 | 6% | 6% | -100% | -89% | 100 min |
| Eerste Divisie Game | ✘ | 47 | 0 | 9% | 6% | -100% | -85% | 11 min |
| Liga Expansion Game | ✘ | 47 | 0 | 6% | 4% | -100% | -89% | 10 min |
| Uruguay Primera Division Game | ✘ | 46 | 0 | 7% | 4% | -100% | -89% | 10 min |
| EuroCup Basketball Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 9 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| Mobile Legends Bang Bang Game | ✘ | 44 | 0 | 0% | 0% | -100% | -100% | 4 min |
| College Hockey Game | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 6 min |
| China League 1 Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 9 min |
| SHL Game | ✘ | 41 | 0 | 2% | 2% | -100% | -96% | 5 min |
| LNBP Basketball Game | ✘ | 40 | 0 | 8% | 0% | -100% | -87% | 16 min |
| Japan J League Game | ✘ | 40 | 0 | 15% | 5% | -100% | -74% | 13 min |
| ELH Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 5 min |
| TFF 1. Lig Game | ✘ | 39 | 0 | 13% | 5% | -100% | -78% | 8 min |
| Women's T20 Match | ✘ | 37 | 0 | 19% | 11% | -100% | -67% | 25 min |
| UEFA Champions League Game | partly | 37 | 1 | 14% | 5% | +152% | -77% | 12 min |
| Bundesliga 2 Game | ✔ | 36 | 0 | 14% | 6% | -100% | -76% | 8 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| Liga MX Game | ✔ | 35 | 0 | 11% | 9% | -100% | -80% | 2 min |
| DEL Game | ✘ | 35 | 0 | 0% | 0% | -100% | -100% | 4 min |
| EFL League One Game | ✔ | 35 | 0 | 11% | 3% | -100% | -80% | 5 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| Ligue 2 Game | ✘ | 34 | 0 | 18% | 12% | -100% | -69% | 7 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Chinese Basketball Association Game  | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Valorant game winner | ✘ | 32 | 0 | 6% | 3% | -100% | -89% | 15 min |
| NFL Game | ✔ | 32 | 1 | 19% | 6% | +192% | -68% | 3 min |
| Korea K-League 2 Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 8 min |
| Polish Ekstraklasa Game | ✘ | 31 | 0 | 10% | 3% | -100% | -83% | 8 min |
| NWSL Game | ✔ | 30 | 0 | 10% | 0% | -100% | -83% | 7 min |
| Peru Liga 1 Game | ✘ | 30 | 0 | 17% | 13% | -100% | -71% | 10 min |
| Indonesia Super League Game | ✘ | 30 | 0 | 13% | 7% | -100% | -77% | 8 min |
| Thai League 1 Game | ✘ | 30 | 0 | 23% | 10% | -100% | -60% | 8 min |
| Serie B Game | ✘ | 30 | 0 | 13% | 10% | -100% | -77% | 11 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Chinese Super League Game | ✘ | 29 | 0 | 7% | 3% | -100% | -88% | 19 min |
| Czech National Football League Game | ✘ | 29 | 0 | 10% | 10% | -100% | -82% | 9 min |
| Serie A Game | ✔ | 29 | 0 | 7% | 7% | -100% | -88% | 11 min |
| Finland Korisliiga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Turkish Super Lig Game | ✘ | 28 | 0 | 14% | 0% | -100% | -75% | 14 min |
| Eredivisie Game | ✔ | 28 | 0 | 11% | 7% | -100% | -81% | 5 min |
| La Liga Game | ✔ | 28 | 0 | 32% | 21% | -100% | -44% | 1 min |
| Czech First League Game | ✘ | 27 | 0 | 15% | 0% | -100% | -74% | 9 min |
| Saudi Pro League Game | ✘ | 26 | 0 | 19% | 12% | -100% | -67% | 14 min |
| Ligue 1 Game | ✔ | 26 | 0 | 15% | 8% | -100% | -73% | 10 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Taca de Portugal Game | ✘ | 26 | 0 | 12% | 4% | -100% | -80% | 7 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| Italy Serie A2 Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Korea K League Game | ✘ | 25 | 1 | 24% | 12% | +273% | -58% | 8 min |
| Spain Liga ACB Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 16 min |
| Ecuador Liga Pro Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 6 min |
| Bolivia Premier Division Game | ✘ | 24 | 0 | 12% | 0% | -100% | -78% | 5 min |
| English Premier League Game | ✔ | 24 | 0 | 17% | 8% | -100% | -71% | 9 min |
| Israeli Premier League Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 10 min |
| APF Division de Honor Game | ✘ | 23 | 0 | 9% | 0% | -100% | -85% | 5 min |
| Australia NBL Game | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 6 min |
| Adriatic ABA Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Bundesliga Game | ✔ | 23 | 1 | 13% | 13% | +306% | -77% | 5 min |
| Sweden SBL Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Eliteserien Game | ✘ | 22 | 0 | 14% | 9% | -100% | -76% | 14 min |
| Men's ODI Cricket Match | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 24 min |
| Czech NBL Game | ✘ | 21 | 0 | 5% | 0% | -100% | -92% | 16 min |
| LNB Elite Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Serie A Femminile Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 20 min |
| England Women's Super League Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 38 min |
| Vietnam V-League 1 Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Serbian SuperLiga Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Venezuela Liga FUTVE game | ✘ | 20 | 0 | 15% | 10% | -100% | -74% | 8 min |
| Russia VTB United Game | ✘ | 19 | 0 | 5% | 0% | -100% | -91% | 13 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Allsvenskan Game | ✘ | 19 | 0 | 16% | 16% | -100% | -73% | 14 min |
| Italy Serie A Game | ✘ | 18 | 0 | 6% | 6% | -100% | -90% | 6 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Austria BSL Game | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 5 min |
| Turkey BSL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Scottish Premiership Game | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Singapore Premier League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 16 min |
| Super League Greece Game | ✘ | 16 | 0 | 19% | 6% | -100% | -68% | 12 min |
| Croatia Premijer Liga Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 19 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Croatia HNL Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 16 min |
| Slovenian Prva Liga Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 6 min |
| Women's Pro Basketball Game | ✔ | 14 | 0 | 21% | 7% | -100% | -63% | 6 min |
| Women's ODI Cricket Match | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 56 min |
| Slovakia SBL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Danish Superliga Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
| Egyptian Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Slovenia 1. SKL Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 15 min |
| Latvian Virsliga Game | ✘ | 13 | 0 | 23% | 8% | -100% | -60% | 18 min |
| CFL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| LKL Lithuania Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Eredivisie Vrouwen Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 22 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| FIBA Europe Cup Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Japan B League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| Spanish Liga F Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 7 min |
| England Super League Basketball Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| Korea KBL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Australian A League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 4 min |
| French Women's Première Ligue Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| BNXT League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Malaysia Super League Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 7 min |
| UAE Pro League | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Indian Super League Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 8 min |
| Qatar Stars League | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 16 min |
| Romanian Liga I Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 6 min |
| Hungarian NB I Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 5 min |
| FIBA Champions League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Men's Iceland Basketball Premier League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| German Women's Bundesliga Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 18 min |
| Austrian Bundesliga Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 16 min |
| South African Premiership Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CONMEBOL Sudamericana Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Liga Nacional de Basquetbol Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Colombia LBP Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Brazil NBB Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| Philippines PBA Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 10 min |
| GBL Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Women's Bundesliga Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Israel Super League Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 19 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 576 | 5% | 1% | 0% | -91% |
| 5–15 min | 301 | 17% | 7% | 1% | -71% |
| 15–30 min | 194 | 31% | 17% | 2% | -45% |
| 30–60 min | 161 | 17% | 10% | 0% | -70% |
| Over 60 min | 134 | 19% | 10% | 0% | -66% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 48 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-18 13:38 | Thai League 1 Game | Pattani FC | ✘ | — | — | In play | — |
| 10-18 13:38 | Counter-Strike 2 Game | Revenge | ✘ | — | — | In play | — |
| 10-18 13:37 | Challenger ATP  | Ivan Gakhov | ✘ | — | — | In play | — |
| 10-18 13:37 | Chinese Basketball Association Game  | Jilin Northeast Tigers | ✘ | — | — | In play | — |
| 10-18 13:36 | eSoccer Game | FC Koln (Krocs) | ✘ | — | — | In play | — |
| 10-18 13:36 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-18 13:36 | England Women's Super League Game | Everton | ✘ | — | — | In play | — |
| 10-18 13:35 | eSoccer Game | Rennes (Frenkie) | ✘ | — | — | In play | — |
| 10-18 13:35 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-18 13:34 | Chinese Basketball Association Game  | Shandong Kirin | ✘ | — | — | In play | — |
| 10-18 13:34 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-18 13:34 | eSoccer Game | Manchester City (Maddy) | ✘ | — | — | In play | — |
| 10-18 13:33 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-18 13:33 | Russia Liga Pro Match | Troyanov Yaroslav | ✘ | — | — | In play | — |
| 10-18 13:31 | eSoccer Game | Toulouse FC (Rooney) | ✘ | — | — | In play | — |
| 10-18 13:31 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-18 13:31 | LaLiga 2 Game | Ceuta | ✔ | 66' · OVI 2 - CEU 0 | — | In play | — |
| 10-18 13:30 | Russia Liga Pro Match | Blinov Igor | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:28 | ITF Women's Match | Arina Arifullina | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:27 | Russia Liga Pro Match | Kogotkov Andrei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:27 | Malaysia Super League Game | Terengganu | ✘ | — | — | In play | — |
| 10-18 13:26 | Thai League 1 Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:25 | Bundesliga 2 Game | Tie | ✔ | 90'+6' · OSN 1 - DSC 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:24 | WTA Tennis Match | Sonay Kartal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:23 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:23 | eSoccer Game | Hoffenheim (Kovboj) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:23 | China League 1 Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:23 | Danish Superliga Game | Nordsjaelland | ✘ | — | — | In play | — |
| 10-18 13:23 | Thai League 1 Game | Pathum United | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 13:22 | China League 1 Game | Meizhou Hakka | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
