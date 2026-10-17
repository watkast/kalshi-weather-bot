# 1¢ Study

*Updated Sat Oct 17, 5:12 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

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
| 17083 | 1171 | 7 (1%) | 1.1% | -$77.65 (-44%) | Hold to the end: -$77.65 (-44%) |

*In play right now: 17. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 1171 | 14% | 10% | 7% | 4% | 1% | 1% |
| Unverified | 15895 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 1% | -$77.65 | -44% |
| Sell at 2¢ | 167 | 14% | -$132.23 | -75% |
| Sell at 3¢ | 115 | 10% | -$130.80 | -74% |
| Sell at 5¢ | 79 | 7% | -$124.30 | -71% |
| Sell at 10¢ | 43 | 4% | -$119.32 | -68% |
| Sell at 25¢ | 14 | 1% | -$129.31 | -74% |
| Sell at 50¢ | 10 | 1% | -$108.15 | -62% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 6371 | 4 | 0% | 0% | -94% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 743 | 1 | 12% | 5% | -87% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 697 | 1 | 5% | 2% | -87% | -92% | 11 min |
| ITF Men's Match | ✘ | 677 | 1 | 12% | 6% | -86% | -79% | 5 min |
| eBasketball Game | ✘ | 635 | 1 | 0% | 0% | -85% | -85% | 2 min |
| Challenger ATP  | ✘ | 484 | 2 | 10% | 3% | -61% | -83% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Russia Liga Pro Match | ✘ | 305 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Darts Match | ✘ | 220 | 0 | 0% | 0% | -100% | -99% | 8 min |
| College Football Game | partly | 198 | 2 | 14% | 7% | -6% | -76% | 28 min |
| Women's College Volleyball Match | ✘ | 185 | 2 | 7% | 3% | +1% | -88% | 81 min |
| Men's T20 Cricket Match | ✘ | 169 | 1 | 13% | 4% | -45% | -77% | 24 min |
| Dota 2 Game | ✘ | 154 | 0 | 1% | 1% | -100% | -98% | 29 min |
| Challenger WTA | ✘ | 151 | 0 | 12% | 5% | -100% | -79% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 130 | 0 | 8% | 2% | -100% | -87% | 11 min |
| NHL Game | ✔ | 119 | 0 | 13% | 6% | -100% | -78% | 5 min |
| Serie C Game | ✘ | 117 | 1 | 4% | 2% | -20% | -93% | 8 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| AHL Game | ✘ | 73 | 0 | 3% | 1% | -100% | -95% | 6 min |
| Brasileiro Serie B Game | ✘ | 70 | 0 | 6% | 1% | -100% | -90% | 10 min |
| Major League Soccer Game | partly | 69 | 1 | 12% | 3% | +35% | -80% | 8 min |
| KHL Game | ✘ | 66 | 0 | 3% | 2% | -100% | -95% | 5 min |
| R6 Game | ✘ | 65 | 0 | 8% | 3% | -100% | -87% | 9 min |
| NBA Game | ✔ | 64 | 0 | 12% | 3% | -100% | -78% | 7 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Argentina Primera Division Game | ✘ | 61 | 0 | 15% | 5% | -100% | -74% | 6 min |
| WTA Tennis Match | ✘ | 60 | 0 | 12% | 0% | -100% | -80% | 4 min |
| Overwatch Game | ✘ | 60 | 0 | 3% | 0% | -100% | -94% | 5 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Ettan Game | ✘ | 57 | 0 | 7% | 2% | -100% | -88% | 6 min |
| Japan J2 League Game | ✘ | 56 | 0 | 16% | 7% | -100% | -72% | 7 min |
| Argentine Nacional B Game | ✘ | 55 | 0 | 9% | 9% | -100% | -84% | 9 min |
| KBO Game | ✘ | 51 | 0 | 10% | 6% | -100% | -83% | 5 min |
| Liga Leumit Game | ✘ | 50 | 0 | 2% | 2% | -100% | -97% | 64 min |
| Liga DIMAYOR Game | ✘ | 49 | 1 | 12% | 4% | +90% | -79% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Euroleague Game | ✘ | 49 | 0 | 24% | 8% | -100% | -58% | 14 min |
| Brasileiro Serie A Game | partly | 47 | 1 | 21% | 13% | +99% | -63% | 8 min |
| LaLiga 2 Game | partly | 46 | 0 | 15% | 7% | -100% | -74% | 8 min |
| Liiga Game | ✘ | 45 | 0 | 0% | 0% | -100% | -100% | 5 min |
| USL Championship Game | partly | 45 | 0 | 11% | 2% | -100% | -81% | 4 min |
| EuroCup Basketball Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 9 min |
| ATP Tennis Match | ✘ | 43 | 0 | 12% | 5% | -100% | -80% | 3 min |
| Eerste Divisie Game | ✘ | 43 | 0 | 7% | 7% | -100% | -88% | 11 min |
| National League Game | ✘ | 42 | 1 | 2% | 2% | +122% | -96% | 4 min |
| German 3. Liga Game | ✘ | 42 | 0 | 14% | 7% | -100% | -75% | 7 min |
| Uruguay Primera Division Game | ✘ | 40 | 0 | 8% | 5% | -100% | -87% | 10 min |
| LNBP Basketball Game | ✘ | 40 | 0 | 8% | 0% | -100% | -87% | 16 min |
| ELH Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Slovakian 2. Liga Game | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 107 min |
| Liga Expansion Game | ✘ | 37 | 0 | 8% | 5% | -100% | -86% | 10 min |
| UEFA Champions League Game | partly | 37 | 1 | 14% | 5% | +152% | -77% | 12 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| SHL Game | ✘ | 35 | 0 | 3% | 3% | -100% | -95% | 5 min |
| DEL Game | ✘ | 35 | 0 | 0% | 0% | -100% | -100% | 4 min |
| EFL Championship Game | ✔ | 35 | 0 | 6% | 6% | -100% | -90% | 9 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| College Hockey Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Japan J League Game | ✘ | 34 | 0 | 18% | 6% | -100% | -69% | 12 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| TFF 1. Lig Game | ✘ | 33 | 0 | 15% | 6% | -100% | -74% | 10 min |
| NFL Game | ✔ | 32 | 1 | 19% | 6% | +192% | -68% | 3 min |
| Mobile Legends Bang Bang Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Valorant game winner | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 15 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| LNB Elite 2 Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Chinese Basketball Association Game  | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Ligue 2 Game | ✘ | 28 | 0 | 18% | 14% | -100% | -69% | 7 min |
| China League 1 Game | ✘ | 27 | 0 | 11% | 7% | -100% | -81% | 6 min |
| Women's T20 Match | ✘ | 27 | 0 | 22% | 11% | -100% | -61% | 26 min |
| Czech National Football League Game | ✘ | 27 | 0 | 11% | 11% | -100% | -81% | 10 min |
| Tweede Divisie Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Korea K-League 2 Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 6 min |
| Indonesia Super League Game | ✘ | 26 | 0 | 15% | 8% | -100% | -73% | 9 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Liga MX Game | ✔ | 25 | 0 | 12% | 12% | -100% | -79% | 1 min |
| Finland Korisliiga Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Peru Liga 1 Game | ✘ | 24 | 0 | 21% | 17% | -100% | -64% | 7 min |
| Polish Ekstraklasa Game | ✘ | 23 | 0 | 13% | 4% | -100% | -77% | 10 min |
| NWSL Game | ✔ | 22 | 0 | 14% | 0% | -100% | -76% | 8 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Saudi Pro League Game | ✘ | 22 | 0 | 23% | 14% | -100% | -61% | 15 min |
| Bundesliga 2 Game | ✔ | 22 | 0 | 14% | 9% | -100% | -76% | 5 min |
| Sweden SBL Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Australia NBL Game | ✘ | 21 | 0 | 5% | 0% | -100% | -92% | 6 min |
| Canadian Premier League | ✘ | 21 | 1 | 24% | 24% | +344% | -59% | 29 min |
| Adriatic ABA Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Serie A Game | ✔ | 21 | 0 | 10% | 10% | -100% | -83% | 11 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Italy Serie A2 Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Eredivisie Game | ✔ | 20 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Ligue 1 Game | ✔ | 20 | 0 | 20% | 10% | -100% | -65% | 12 min |
| La Liga Game | ✔ | 20 | 0 | 40% | 30% | -100% | -31% | 5 min |
| APF Division de Honor Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 5 min |
| Men's ODI Cricket Match | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 24 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Czech NBL Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Spain Liga ACB Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 18 min |
| Thai League 1 Game | ✘ | 18 | 0 | 22% | 0% | -100% | -61% | 8 min |
| Turkish Super Lig Game | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 13 min |
| Serie B Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 11 min |
| Ecuador Liga Pro Game | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 6 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Bolivia Premier Division Game | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 5 min |
| LNB Elite Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 11 min |
| EFL League One Game | ✔ | 17 | 0 | 12% | 0% | -100% | -80% | 2 min |
| Chinese Super League Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 16 min |
| Czech First League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 10 min |
| Allsvenskan Game | ✘ | 17 | 0 | 18% | 18% | -100% | -69% | 14 min |
| Russia VTB United Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 16 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Italy Serie A Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 6 min |
| Eliteserien Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 9 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Austria BSL Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| Turkey BSL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 9 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Korea K League Game | ✘ | 14 | 0 | 36% | 14% | -100% | -38% | 14 min |
| Danish Superliga Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
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
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| FIBA Europe Cup Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Slovenia 1. SKL Game | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 15 min |
| Finnish Ykkosliiga Game | ✘ | 11 | 1 | 9% | 9% | +748% | -84% | 15 min |
| Croatia HNL Game | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 20 min |
| Bundesliga Game | ✔ | 11 | 1 | 18% | 18% | +748% | -68% | 9 min |
| Latvian Virsliga Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 17 min |
| Slovenian Prva Liga Game | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 12 min |
| England Super League Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| CFL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Singapore Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 17 min |
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
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CONMEBOL Sudamericana Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Taca de Portugal Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 34 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Malaysia Super League Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 23 min |
| UAE Pro League | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 29 min |
| Qatar Stars League | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 33 min |
| Romanian Liga I Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 8 min |
| Liga Nacional de Basquetbol Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Colombia LBP Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 17 min |
| BNXT League Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Indian Super League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| German Women's Bundesliga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Austrian Bundesliga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Hungarian NB I Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| Mexican Pacific League | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 16 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 481 | 5% | 1% | 0% | -91% |
| 5–15 min | 251 | 16% | 7% | 1% | -72% |
| 15–30 min | 166 | 31% | 17% | 2% | -46% |
| 30–60 min | 138 | 17% | 10% | 0% | -70% |
| Over 60 min | 122 | 20% | 11% | 0% | -66% |

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
| 10-17 11:10 | eSoccer Game | Arsenal (Mordor) | ✘ | — | — | In play | — |
| 10-17 11:10 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-17 11:08 | Overwatch Game | ZANSIDE GAMING | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 11:07 | eSoccer Game | Frankfurt (Niskanen15) | ✘ | — | — | In play | — |
| 10-17 11:07 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-17 11:05 | eSoccer Game | Mönchengladbach (Sheerpy) | ✘ | — | — | In play | — |
| 10-17 11:05 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-17 11:05 | eSoccer Game | France (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 11:05 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 11:04 | eSoccer Game | Portugal (Kate) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 11:02 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 11:01 | Malaysia Super League Game | Negeri Sembilan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 11:01 | Malaysia Super League Game | Sabah | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 11:00 | ATP Tennis Match | Ilya Ivashka | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:56 | eSoccer Game | Crystal Palace (Mantis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:55 | Japan J2 League Game | Kataller T | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:55 | eSoccer Game | Everton (Mordor) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:54 | Russia Liga Pro Match | Kutuzov Oleg Gennadyevich | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:53 | Japan J2 League Game | Shonan | ✘ | — | 9¢ | ❌ Lost | -$0.15 |
| 10-17 10:53 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:53 | eSoccer Game | Freiburg (Danny) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:52 | ITF Women's Match | Valentini Grammatikopoulou | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:52 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:51 | eSoccer Game | Frankfurt (Sheerpy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:51 | eSoccer Game | France (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:51 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:48 | eSoccer Game | United States (Rose) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:48 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:48 | R6 Game | CAG by VARREL | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 10:47 | Russia Liga Pro Match | Ivanov Aleksei Olegovich | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
