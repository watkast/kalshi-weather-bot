# 1¢ Study

*Updated Thu Oct 15, 9:27 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 50 finished bets | 2% | $6.50 | +87% | +13.00¢ | -$3.75 / $10.25 |

*Expect about **3 buys a day**, roughly **$0.48/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 50 | -$0.75 | -10% |
| ESPN win probability ≥ 2%, sell at 25¢ | 50 | -$4.19 | -56% |
| ESPN win probability ≥ 2%, sell at 3¢ | 50 | -$4.77 | -64% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 15113 | 1123 | 7 (1%) | 1.1% | -$70.45 (-42%) | Hold to the end: -$70.45 (-42%) |

*In play right now: 18. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 232 | 3.2% | 0.4% (1) | -41% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 232 | 1 | -60% | -75% | -74% | -72% |
| ESPN win probability ≥ 2% | 50 | 1 | +87% | -65% | -64% | -74% |
| ESPN win probability ≥ 5% | 24 | 1 | +289% | -78% | -78% | -82% |
| ESPN win probability ≥ 10% | 15 | 1 | +522% | -77% | -65% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1123 | 15% | 10% | 7% | 4% | 1% | 1% |
| Unverified | 13972 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 1% | -$70.45 | -42% |
| Sell at 2¢ | 164 | 15% | -$125.81 | -75% |
| Sell at 3¢ | 114 | 10% | -$123.99 | -74% |
| Sell at 5¢ | 79 | 7% | -$117.10 | -70% |
| Sell at 10¢ | 43 | 4% | -$112.12 | -67% |
| Sell at 25¢ | 14 | 1% | -$122.11 | -72% |
| Sell at 50¢ | 10 | 1% | -$100.95 | -60% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 5337 | 3 | 0% | 0% | -95% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 718 | 1 | 12% | 5% | -87% | -79% | 4 min |
| ITF Men's Match | ✘ | 653 | 1 | 12% | 6% | -86% | -80% | 5 min |
| Counter-Strike 2 Game | ✘ | 650 | 1 | 5% | 2% | -86% | -92% | 11 min |
| eBasketball Game | ✘ | 528 | 1 | 0% | 0% | -82% | -82% | 2 min |
| Challenger ATP  | ✘ | 463 | 2 | 10% | 3% | -60% | -83% | 5 min |
| TT Star Series Match | ✘ | 304 | 1 | 2% | 2% | -69% | -97% | 5 min |
| Darts Match | ✘ | 195 | 0 | 1% | 1% | -100% | -99% | 8 min |
| College Football Game | partly | 194 | 2 | 13% | 7% | -4% | -77% | 29 min |
| Women's College Volleyball Match | ✘ | 164 | 2 | 7% | 2% | +14% | -88% | 91 min |
| Men's T20 Cricket Match | ✘ | 160 | 1 | 14% | 4% | -42% | -76% | 24 min |
| Challenger WTA | ✘ | 140 | 0 | 13% | 5% | -100% | -78% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Dota 2 Game | ✘ | 133 | 0 | 2% | 2% | -100% | -97% | 29 min |
| League of Legends Game | ✘ | 128 | 0 | 7% | 2% | -100% | -88% | 11 min |
| Russia Liga Pro Match | ✘ | 118 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NHL Game | ✔ | 115 | 0 | 13% | 6% | -100% | -77% | 5 min |
| Serie C Game | ✘ | 113 | 1 | 4% | 2% | -17% | -92% | 8 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Major League Soccer Game | partly | 69 | 1 | 12% | 3% | +35% | -80% | 8 min |
| Brasileiro Serie B Game | ✘ | 66 | 0 | 5% | 2% | -100% | -92% | 10 min |
| AHL Game | ✘ | 63 | 0 | 3% | 2% | -100% | -94% | 6 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| KHL Game | ✘ | 61 | 0 | 3% | 2% | -100% | -94% | 5 min |
| R6 Game | ✘ | 60 | 0 | 7% | 3% | -100% | -88% | 9 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Argentina Primera Division Game | ✘ | 57 | 0 | 16% | 5% | -100% | -73% | 6 min |
| Overwatch Game | ✘ | 53 | 0 | 4% | 0% | -100% | -93% | 5 min |
| Ettan Game | ✘ | 53 | 0 | 8% | 2% | -100% | -87% | 5 min |
| NBA Game | ✔ | 53 | 0 | 13% | 4% | -100% | -77% | 7 min |
| Argentine Nacional B Game | ✘ | 51 | 0 | 10% | 10% | -100% | -83% | 10 min |
| KBO Game | ✘ | 50 | 0 | 8% | 6% | -100% | -86% | 4 min |
| Liga DIMAYOR Game | ✘ | 49 | 1 | 12% | 4% | +90% | -79% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| USL Championship Game | partly | 45 | 0 | 11% | 2% | -100% | -81% | 4 min |
| Brasileiro Serie A Game | partly | 45 | 1 | 22% | 13% | +107% | -61% | 7 min |
| WTA Tennis Match | ✘ | 44 | 0 | 11% | 0% | -100% | -80% | 3 min |
| LaLiga 2 Game | partly | 44 | 0 | 16% | 7% | -100% | -72% | 8 min |
| EuroCup Basketball Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 9 min |
| Euroleague Game | ✘ | 43 | 0 | 26% | 7% | -100% | -56% | 14 min |
| Liga Leumit Game | ✘ | 40 | 0 | 2% | 2% | -100% | -96% | 14 min |
| Japan J2 League Game | ✘ | 40 | 0 | 12% | 2% | -100% | -78% | 8 min |
| German 3. Liga Game | ✘ | 40 | 0 | 15% | 8% | -100% | -74% | 7 min |
| Liiga Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Uruguay Primera Division Game | ✘ | 38 | 0 | 8% | 5% | -100% | -86% | 10 min |
| LNBP Basketball Game | ✘ | 38 | 0 | 8% | 0% | -100% | -86% | 14 min |
| ATP Tennis Match | ✘ | 38 | 0 | 11% | 5% | -100% | -82% | 3 min |
| UEFA Champions League Game | partly | 37 | 1 | 14% | 5% | +152% | -77% | 12 min |
| National League Game | ✘ | 36 | 1 | 3% | 3% | +159% | -95% | 5 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| SHL Game | ✘ | 35 | 0 | 3% | 3% | -100% | -95% | 5 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| ELH Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Slovakian 2. Liga Game | ✘ | 34 | 0 | 6% | 6% | -100% | -90% | 111 min |
| Liga Expansion Game | ✘ | 33 | 0 | 9% | 6% | -100% | -84% | 11 min |
| TFF 1. Lig Game | ✘ | 33 | 0 | 15% | 6% | -100% | -74% | 10 min |
| EFL Championship Game | ✔ | 33 | 0 | 6% | 6% | -100% | -89% | 9 min |
| NFL Game | ✔ | 31 | 1 | 19% | 6% | +201% | -66% | 4 min |
| Japan NPB Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Valorant game winner | ✘ | 30 | 0 | 7% | 3% | -100% | -88% | 15 min |
| DEL Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 4 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Chinese Basketball Association Game  | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Tweede Divisie Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| China League 1 Game | ✘ | 25 | 0 | 12% | 8% | -100% | -79% | 6 min |
| Finland Korisliiga Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Mobile Legends Bang Bang Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Peru Liga 1 Game | ✘ | 20 | 0 | 25% | 20% | -100% | -57% | 7 min |
| Italy Serie A2 Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Japan J League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 12 min |
| Saudi Pro League Game | ✘ | 20 | 0 | 20% | 15% | -100% | -65% | 14 min |
| Liga MX Game | ✔ | 19 | 0 | 16% | 16% | -100% | -73% | 1 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Adriatic ABA Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| College Hockey Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Polish Ekstraklasa Game | ✘ | 19 | 0 | 16% | 5% | -100% | -73% | 11 min |
| Serie A Game | ✔ | 19 | 0 | 11% | 11% | -100% | -82% | 11 min |
| Sweden SBL Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Australia NBL Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 6 min |
| Men's ODI Cricket Match | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 24 min |
| Spain Liga ACB Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 18 min |
| Bundesliga 2 Game | ✔ | 18 | 0 | 17% | 11% | -100% | -71% | 8 min |
| Eredivisie Game | ✔ | 18 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Ligue 2 Game | ✘ | 18 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Ligue 1 Game | ✔ | 18 | 0 | 17% | 11% | -100% | -71% | 10 min |
| La Liga Game | ✔ | 18 | 0 | 44% | 33% | -100% | -23% | 9 min |
| APF Division de Honor Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 5 min |
| Czech NBL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Canadian Premier League | ✘ | 17 | 1 | 24% | 24% | +449% | -59% | 29 min |
| EFL League One Game | ✔ | 17 | 0 | 12% | 0% | -100% | -80% | 2 min |
| Czech First League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 10 min |
| LNB Elite Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Women's T20 Match | ✘ | 16 | 0 | 19% | 6% | -100% | -68% | 27 min |
| Italy Serie A Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 6 min |
| Korea K-League 2 Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 6 min |
| Indonesia Super League Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 10 min |
| Thai League 1 Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 7 min |
| Eliteserien Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 9 min |
| Turkish Super Lig Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 14 min |
| Serie B Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 15 min |
| Ecuador Liga Pro Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 6 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Russia VTB United Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 17 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Chinese Super League Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 22 min |
| Czech National Football League Game | ✘ | 15 | 0 | 20% | 20% | -100% | -65% | 12 min |
| Allsvenskan Game | ✘ | 15 | 0 | 20% | 20% | -100% | -65% | 14 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| Austria BSL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Bolivia Premier Division Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| English Premier League Game | ✔ | 14 | 0 | 7% | 7% | -100% | -88% | 7 min |
| Israeli Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Super League Greece Game | ✘ | 14 | 0 | 21% | 7% | -100% | -63% | 13 min |
| Venezuela Liga FUTVE game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 10 min |
| Egyptian Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Turkey BSL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's ODI Cricket Match | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 56 min |
| Slovakia SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Croatia Premijer Liga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Vietnam V-League 1 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Korea K League Game | ✘ | 12 | 0 | 42% | 17% | -100% | -28% | 14 min |
| Danish Superliga Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Serbian SuperLiga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| FIBA Europe Cup Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Finnish Ykkosliiga Game | ✘ | 11 | 1 | 9% | 9% | +748% | -84% | 15 min |
| Latvian Virsliga Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 17 min |
| Slovenia 1. SKL Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 18 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| LKL Lithuania Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Croatia HNL Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 16 min |
| Bundesliga Game | ✔ | 9 | 1 | 22% | 22% | +937% | -61% | 13 min |
| Slovenian Prva Liga Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 14 min |
| England Super League Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| CFL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Singapore Premier League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Scottish Premiership Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 39 min |
| FIBA Champions League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CONMEBOL Sudamericana Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Men's Iceland Basketball Premier League Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Korea KBL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Colombia LBP Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Liga Nacional de Basquetbol Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Taca de Portugal Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 41 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| BNXT League Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 15 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 460 | 5% | 1% | 0% | -91% |
| 5–15 min | 236 | 17% | 7% | 1% | -70% |
| 15–30 min | 161 | 32% | 18% | 2% | -45% |
| 30–60 min | 134 | 18% | 10% | 0% | -69% |
| Over 60 min | 121 | 19% | 11% | 0% | -67% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 46 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-16 03:24 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-16 03:23 | eBasketball Game | Los Angeles Lakers (Larry) | ✘ | — | — | In play | — |
| 10-16 03:23 | eSoccer Game | Manchester Utd (NINJA) | ✘ | — | — | In play | — |
| 10-16 03:23 | Women's College Volleyball Match | Arizona | ✘ | — | — | In play | — |
| 10-16 03:21 | eBasketball Game | Brooklyn Nets (Shaq) | ✘ | — | — | In play | — |
| 10-16 03:19 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-16 03:19 | eSoccer Game | England (Quinnie) | ✘ | — | — | In play | — |
| 10-16 03:19 | eSoccer Game | Frankfurt (Elastico) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:19 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:18 | College Football Game | East Carolina | ✔ | OT · ECU 17 - UAB 30 | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:17 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:16 | eSoccer Game | Spain (Lotta) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:08 | eSoccer Game | Chelsea (NINJA) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:08 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:06 | eSoccer Game | Leverkusen (Elastico) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:06 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:06 | eSoccer Game | 1. FC Köln (Rendeto) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:05 | eSoccer Game | England (Quinnie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:05 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:05 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:03 | eSoccer Game | United States (Demi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 03:03 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 02:55 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 02:54 | eSoccer Game | Crystal Palace (Poly) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 02:53 | NHL Game | Nashville | ✔ | In SO · SJ 2 - NSH 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-16 02:53 | eSoccer Game | FC Augsburg (Ousmane) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 02:52 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 02:51 | eSoccer Game | England (Quinnie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 02:50 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-16 02:50 | eSoccer Game | Dortmund (Nate) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
