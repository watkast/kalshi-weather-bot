# 1¢ Study

*Updated Sat Oct 17, 8:08 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 57 finished bets | 2% | $5.45 | +64% | +9.56¢ | -$4.20 / $9.65 |

*Expect about **3 buys a day**, roughly **$0.49/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 57 | -$1.80 | -21% |
| ESPN win probability ≥ 2%, sell at 25¢ | 57 | -$5.24 | -61% |
| ESPN win probability ≥ 2%, sell at 2¢ | 57 | -$5.43 | -64% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 17340 | 1191 | 7 (1%) | 1.1% | -$80.65 (-45%) | Hold to the end: -$80.65 (-45%) |

*In play right now: 24. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 248 | 3.4% | 0.4% (1) | -54% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 248 | 1 | -62% | -75% | -76% | -74% |
| ESPN win probability ≥ 2% | 57 | 1 | +64% | -64% | -68% | -77% |
| ESPN win probability ≥ 5% | 27 | 1 | +246% | -81% | -81% | -84% |
| ESPN win probability ≥ 10% | 17 | 1 | +449% | -80% | -69% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1191 | 14% | 10% | 7% | 4% | 1% | 1% |
| Unverified | 16125 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 1% | -$80.65 | -45% |
| Sell at 2¢ | 170 | 14% | -$134.45 | -75% |
| Sell at 3¢ | 116 | 10% | -$133.41 | -75% |
| Sell at 5¢ | 80 | 7% | -$126.65 | -71% |
| Sell at 10¢ | 43 | 4% | -$122.32 | -68% |
| Sell at 25¢ | 14 | 1% | -$132.31 | -74% |
| Sell at 50¢ | 10 | 1% | -$111.15 | -62% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 6453 | 4 | 0% | 0% | -94% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 746 | 1 | 12% | 5% | -87% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 697 | 1 | 5% | 2% | -87% | -92% | 11 min |
| ITF Men's Match | ✘ | 680 | 1 | 12% | 6% | -86% | -79% | 5 min |
| eBasketball Game | ✘ | 647 | 1 | 0% | 0% | -86% | -85% | 2 min |
| Challenger ATP  | ✘ | 486 | 2 | 10% | 3% | -62% | -83% | 5 min |
| Russia Liga Pro Match | ✘ | 327 | 0 | 0% | 0% | -100% | -100% | 4 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Darts Match | ✘ | 220 | 0 | 0% | 0% | -100% | -99% | 8 min |
| College Football Game | partly | 198 | 2 | 14% | 7% | -6% | -76% | 28 min |
| Women's College Volleyball Match | ✘ | 185 | 2 | 7% | 3% | +1% | -88% | 81 min |
| Men's T20 Cricket Match | ✘ | 170 | 1 | 13% | 4% | -45% | -78% | 24 min |
| Challenger WTA | ✘ | 155 | 0 | 12% | 5% | -100% | -79% | 8 min |
| Dota 2 Game | ✘ | 155 | 0 | 1% | 1% | -100% | -98% | 29 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 131 | 0 | 8% | 2% | -100% | -87% | 11 min |
| NHL Game | ✔ | 119 | 0 | 13% | 6% | -100% | -78% | 5 min |
| Serie C Game | ✘ | 117 | 1 | 4% | 2% | -20% | -93% | 8 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| AHL Game | ✘ | 73 | 0 | 3% | 1% | -100% | -95% | 6 min |
| Brasileiro Serie B Game | ✘ | 70 | 0 | 6% | 1% | -100% | -90% | 10 min |
| Major League Soccer Game | partly | 69 | 1 | 12% | 3% | +35% | -80% | 8 min |
| KHL Game | ✘ | 67 | 0 | 3% | 1% | -100% | -95% | 5 min |
| R6 Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 9 min |
| NBA Game | ✔ | 64 | 0 | 12% | 3% | -100% | -78% | 7 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Overwatch Game | ✘ | 61 | 0 | 3% | 0% | -100% | -94% | 5 min |
| Ettan Game | ✘ | 61 | 0 | 7% | 2% | -100% | -89% | 5 min |
| Argentina Primera Division Game | ✘ | 61 | 0 | 15% | 5% | -100% | -74% | 6 min |
| WTA Tennis Match | ✘ | 60 | 0 | 12% | 0% | -100% | -80% | 4 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Japan J2 League Game | ✘ | 58 | 0 | 16% | 7% | -100% | -73% | 7 min |
| Argentine Nacional B Game | ✘ | 55 | 0 | 9% | 9% | -100% | -84% | 9 min |
| German 3. Liga Game | ✘ | 52 | 0 | 12% | 6% | -100% | -80% | 7 min |
| KBO Game | ✘ | 51 | 0 | 10% | 6% | -100% | -83% | 5 min |
| Liga Leumit Game | ✘ | 50 | 0 | 2% | 2% | -100% | -97% | 64 min |
| Liga DIMAYOR Game | ✘ | 49 | 1 | 12% | 4% | +90% | -79% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Euroleague Game | ✘ | 49 | 0 | 24% | 8% | -100% | -58% | 14 min |
| LaLiga 2 Game | partly | 48 | 0 | 19% | 8% | -100% | -68% | 8 min |
| ATP Tennis Match | ✘ | 47 | 0 | 11% | 4% | -100% | -82% | 3 min |
| Brasileiro Serie A Game | partly | 47 | 1 | 21% | 13% | +99% | -63% | 8 min |
| Liiga Game | ✘ | 45 | 0 | 0% | 0% | -100% | -100% | 5 min |
| USL Championship Game | partly | 45 | 0 | 11% | 2% | -100% | -81% | 4 min |
| EuroCup Basketball Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 9 min |
| Eerste Divisie Game | ✘ | 43 | 0 | 7% | 7% | -100% | -88% | 11 min |
| National League Game | ✘ | 42 | 1 | 2% | 2% | +122% | -96% | 4 min |
| EFL Championship Game | ✔ | 41 | 0 | 5% | 5% | -100% | -92% | 8 min |
| Uruguay Primera Division Game | ✘ | 40 | 0 | 8% | 5% | -100% | -87% | 10 min |
| LNBP Basketball Game | ✘ | 40 | 0 | 8% | 0% | -100% | -87% | 16 min |
| ELH Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Slovakian 2. Liga Game | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 107 min |
| Liga Expansion Game | ✘ | 37 | 0 | 8% | 5% | -100% | -86% | 10 min |
| UEFA Champions League Game | partly | 37 | 1 | 14% | 5% | +152% | -77% | 12 min |
| Mobile Legends Bang Bang Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Japan J League Game | ✘ | 36 | 0 | 17% | 6% | -100% | -71% | 13 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| China League 1 Game | ✘ | 35 | 0 | 9% | 6% | -100% | -85% | 9 min |
| SHL Game | ✘ | 35 | 0 | 3% | 3% | -100% | -95% | 5 min |
| DEL Game | ✘ | 35 | 0 | 0% | 0% | -100% | -100% | 4 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| College Hockey Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| TFF 1. Lig Game | ✘ | 33 | 0 | 15% | 6% | -100% | -74% | 10 min |
| Valorant game winner | ✘ | 32 | 0 | 6% | 3% | -100% | -89% | 15 min |
| NFL Game | ✔ | 32 | 1 | 19% | 6% | +192% | -68% | 3 min |
| Chinese Basketball Association Game  | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Ligue 2 Game | ✘ | 32 | 0 | 19% | 12% | -100% | -68% | 7 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| LNB Elite 2 Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Women's T20 Match | ✘ | 28 | 0 | 21% | 11% | -100% | -63% | 25 min |
| Tweede Divisie Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Bundesliga 2 Game | ✔ | 28 | 0 | 18% | 7% | -100% | -69% | 8 min |
| Czech National Football League Game | ✘ | 27 | 0 | 11% | 11% | -100% | -81% | 10 min |
| Korea K-League 2 Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 6 min |
| Indonesia Super League Game | ✘ | 26 | 0 | 15% | 8% | -100% | -73% | 9 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Liga MX Game | ✔ | 25 | 0 | 12% | 12% | -100% | -79% | 1 min |
| Finland Korisliiga Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Chinese Super League Game | ✘ | 25 | 0 | 8% | 4% | -100% | -86% | 27 min |
| Peru Liga 1 Game | ✘ | 24 | 0 | 21% | 17% | -100% | -64% | 7 min |
| Thai League 1 Game | ✘ | 24 | 0 | 21% | 4% | -100% | -64% | 8 min |
| Polish Ekstraklasa Game | ✘ | 23 | 0 | 13% | 4% | -100% | -77% | 10 min |
| NWSL Game | ✔ | 22 | 0 | 14% | 0% | -100% | -76% | 8 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Saudi Pro League Game | ✘ | 22 | 0 | 23% | 14% | -100% | -61% | 15 min |
| La Liga Game | ✔ | 22 | 0 | 36% | 27% | -100% | -37% | 4 min |
| Sweden SBL Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Australia NBL Game | ✘ | 21 | 0 | 5% | 0% | -100% | -92% | 6 min |
| Canadian Premier League | ✘ | 21 | 1 | 24% | 24% | +344% | -59% | 29 min |
| Adriatic ABA Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 9 min |
| EFL League One Game | ✔ | 21 | 0 | 14% | 5% | -100% | -75% | 2 min |
| Serie A Game | ✔ | 21 | 0 | 10% | 10% | -100% | -83% | 11 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Men's ODI Cricket Match | ✘ | 20 | 0 | 10% | 0% | -100% | -83% | 24 min |
| Italy Serie A2 Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Turkish Super Lig Game | ✘ | 20 | 0 | 10% | 0% | -100% | -83% | 14 min |
| Eredivisie Game | ✔ | 20 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Ligue 1 Game | ✔ | 20 | 0 | 20% | 10% | -100% | -65% | 12 min |
| APF Division de Honor Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 5 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Czech NBL Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Spain Liga ACB Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 18 min |
| Vietnam V-League 1 Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Eliteserien Game | ✘ | 18 | 0 | 17% | 11% | -100% | -71% | 10 min |
| Serie B Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 11 min |
| Ecuador Liga Pro Game | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 6 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Bolivia Premier Division Game | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 5 min |
| Russia VTB United Game | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 16 min |
| LNB Elite Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Czech First League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 10 min |
| Allsvenskan Game | ✘ | 17 | 0 | 18% | 18% | -100% | -69% | 14 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| England Women's Super League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 39 min |
| Italy Serie A Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 6 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| English Premier League Game | ✔ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Austria BSL Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Turkey BSL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| Serie A Femminile Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 25 min |
| Korea K League Game | ✘ | 14 | 0 | 36% | 14% | -100% | -38% | 14 min |
| Danish Superliga Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
| Serbian SuperLiga Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Israeli Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Super League Greece Game | ✘ | 14 | 0 | 21% | 7% | -100% | -63% | 13 min |
| Venezuela Liga FUTVE game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 10 min |
| Egyptian Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Women's ODI Cricket Match | ✘ | 13 | 0 | 15% | 8% | -100% | -73% | 50 min |
| Latvian Virsliga Game | ✘ | 13 | 0 | 23% | 8% | -100% | -60% | 18 min |
| Slovakia SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Croatia Premijer Liga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Singapore Premier League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 12 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| FIBA Europe Cup Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Slovenia 1. SKL Game | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 15 min |
| Finnish Ykkosliiga Game | ✘ | 11 | 1 | 9% | 9% | +748% | -84% | 15 min |
| Croatia HNL Game | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 20 min |
| Bundesliga Game | ✔ | 11 | 1 | 18% | 18% | +748% | -68% | 9 min |
| Slovenian Prva Liga Game | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 12 min |
| England Super League Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| CFL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| LKL Lithuania Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Australian A League Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 4 min |
| Japan B League Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 8 min |
| Scottish Premiership Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Korea KBL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 9 min |
| FIBA Champions League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Men's Iceland Basketball Premier League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| German Women's Bundesliga Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 18 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CONMEBOL Sudamericana Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Taca de Portugal Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 34 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Malaysia Super League Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 23 min |
| UAE Pro League | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 29 min |
| Indian Super League Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 10 min |
| Qatar Stars League | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 33 min |
| Romanian Liga I Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 8 min |
| Spanish Liga F Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Liga Nacional de Basquetbol Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Colombia LBP Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 17 min |
| BNXT League Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Austrian Bundesliga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Hungarian NB I Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| Philippines PBA Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 10 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 490 | 6% | 1% | 0% | -90% |
| 5–15 min | 259 | 16% | 7% | 1% | -72% |
| 15–30 min | 168 | 31% | 17% | 2% | -46% |
| 30–60 min | 139 | 18% | 10% | 0% | -69% |
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
| 10-17 14:07 | Serie B Game | L.R. Vicenza | ✘ | — | — | In play | — |
| 10-17 14:05 | Chinese Basketball Association Game  | Shanxi Loongs | ✘ | — | — | In play | — |
| 10-17 14:04 | Czech First League Game | Zlin | ✘ | — | — | In play | — |
| 10-17 14:02 | eSoccer Game | AS Monaco (Kevin) | ✘ | — | — | In play | — |
| 10-17 14:02 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-17 14:01 | Serie C Game | Inter Milano U23 | ✘ | — | — | In play | — |
| 10-17 14:00 | GBL Basketball Game | AO Mykonoy | ✘ | — | — | In play | — |
| 10-17 14:00 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 14:00 | eSoccer Game | Rennes (Bradley) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 14:00 | eSoccer Game | Chelsea (Olive) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 14:00 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:59 | Tweede Divisie Game | Kloetinge | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:58 | Tweede Divisie Game | GVVV | ✘ | — | — | In play | — |
| 10-17 13:58 | Tweede Divisie Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:58 | Mobile Legends Bang Bang Game | Invictus Gaming | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:57 | Serbian SuperLiga Game | Zemun | ✘ | — | — | In play | — |
| 10-17 13:55 | Men's ODI Cricket Match | Uganda A | ✘ | — | — | In play | — |
| 10-17 13:55 | German 3. Liga Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:55 | German 3. Liga Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:55 | ITF Men's Match | Florent Bax | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-17 13:54 | Dota 2 Game | Dawn Bulls | ✘ | — | — | In play | — |
| 10-17 13:54 | Ligue 2 Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:54 | Thai League 1 Game | Rayong FC | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:54 | Thai League 1 Game | Uthai Thani FC | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:54 | La Liga Game | Tie | ✔ | 90'+4' · ATM 1 - ESP 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:53 | eSoccer Game | FC Bayern (Kovboj) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:53 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:52 | Serie C Game | Sassari | ✘ | — | — | In play | — |
| 10-17 13:52 | German Women's Bundesliga Game | Leverkusen | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 13:52 | German Women's Bundesliga Game | Frankfurt | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
