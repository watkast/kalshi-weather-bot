# 1¢ Study

*Updated Tue Oct 20, 8:14 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 32 finished bets | 3% | $9.20 | +192% | +28.75¢ | $11.60 / -$2.40 |

*Expect about **2 buys a day**, roughly **$0.29/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 65 | $4.25 | +44% |
| ESPN win probability ≥ 5%, sell at 50¢ | 32 | $1.95 | +41% |
| ESPN win probability ≥ 5%, sell at 25¢ | 32 | -$1.49 | -31% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 22362 | 1485 | 7 (0%) | 1.1% | -$124.75 (-56%) | Hold to the end: -$124.75 (-56%) |

*In play right now: 35. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 281 | 3.4% | 0.4% (1) | -65% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 281 | 1 | -67% | -74% | -74% | -72% |
| ESPN win probability ≥ 2% | 65 | 1 | +44% | -65% | -68% | -73% |
| ESPN win probability ≥ 5% | 32 | 1 | +192% | -84% | -84% | -86% |
| ESPN win probability ≥ 10% | 19 | 1 | +391% | -82% | -73% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1485 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 20842 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$124.75 | -56% |
| Sell at 2¢ | 210 | 14% | -$168.15 | -75% |
| Sell at 3¢ | 143 | 10% | -$166.98 | -75% |
| Sell at 5¢ | 99 | 7% | -$158.40 | -71% |
| Sell at 10¢ | 51 | 3% | -$155.94 | -70% |
| Sell at 25¢ | 15 | 1% | -$173.10 | -78% |
| Sell at 50¢ | 10 | 1% | -$155.25 | -70% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 8867 | 5 | 1% | 0% | -95% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| eBasketball Game | ✘ | 888 | 1 | 0% | 0% | -89% | -89% | 2 min |
| ITF Women's Match | ✘ | 862 | 1 | 13% | 5% | -89% | -77% | 4 min |
| Counter-Strike 2 Game | ✘ | 807 | 2 | 4% | 2% | -77% | -92% | 11 min |
| ITF Men's Match | ✘ | 794 | 1 | 12% | 6% | -88% | -80% | 5 min |
| Russia Liga Pro Match | ✘ | 742 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Challenger ATP  | ✘ | 587 | 2 | 11% | 4% | -68% | -82% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 262 | 2 | 13% | 7% | -29% | -77% | 24 min |
| Darts Match | ✘ | 240 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Women's College Volleyball Match | ✘ | 208 | 2 | 6% | 3% | -10% | -89% | 74 min |
| Men's T20 Cricket Match | ✘ | 182 | 1 | 13% | 4% | -49% | -78% | 25 min |
| Dota 2 Game | ✘ | 174 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Serie C Game | ✘ | 174 | 2 | 5% | 3% | +7% | -91% | 8 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| NHL Game | ✔ | 139 | 0 | 12% | 6% | -100% | -79% | 4 min |
| League of Legends Game | ✘ | 133 | 0 | 8% | 2% | -100% | -87% | 11 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Major League Soccer Game | partly | 99 | 1 | 11% | 4% | -6% | -81% | 6 min |
| AHL Game | ✘ | 94 | 0 | 3% | 2% | -100% | -94% | 5 min |
| Argentina Primera Division Game | ✘ | 86 | 1 | 17% | 9% | +9% | -70% | 6 min |
| Ettan Game | ✘ | 85 | 0 | 5% | 1% | -100% | -92% | 6 min |
| Brasileiro Serie B Game | ✘ | 84 | 0 | 7% | 2% | -100% | -88% | 9 min |
| KHL Game | ✘ | 77 | 0 | 5% | 4% | -100% | -91% | 5 min |
| Argentine Nacional B Game | ✘ | 76 | 0 | 9% | 8% | -100% | -84% | 8 min |
| WTA Tennis Match | ✘ | 76 | 0 | 12% | 3% | -100% | -79% | 5 min |
| Overwatch Game | ✘ | 74 | 0 | 3% | 0% | -100% | -95% | 5 min |
| USL Championship Game | partly | 68 | 0 | 13% | 3% | -100% | -77% | 5 min |
| R6 Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 9 min |
| LaLiga 2 Game | partly | 66 | 0 | 21% | 9% | -100% | -63% | 8 min |
| Liga DIMAYOR Game | ✘ | 65 | 1 | 11% | 3% | +44% | -81% | 6 min |
| ATP Tennis Match | ✘ | 65 | 0 | 12% | 5% | -100% | -79% | 3 min |
| Brasileiro Serie A Game | partly | 65 | 1 | 15% | 9% | +44% | -73% | 8 min |
| NBA Game | ✔ | 64 | 0 | 12% | 3% | -100% | -78% | 7 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Japan J2 League Game | ✘ | 60 | 0 | 15% | 7% | -100% | -74% | 8 min |
| German 3. Liga Game | ✘ | 60 | 0 | 12% | 5% | -100% | -80% | 7 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Liga Leumit Game | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 138 min |
| Uruguay Primera Division Game | ✘ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| TFF 1. Lig Game | ✘ | 53 | 0 | 19% | 11% | -100% | -67% | 10 min |
| EFL Championship Game | ✔ | 53 | 0 | 8% | 4% | -100% | -87% | 8 min |
| Liiga Game | ✘ | 52 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Slovakian 2. Liga Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 100 min |
| Eerste Divisie Game | ✘ | 50 | 0 | 8% | 6% | -100% | -86% | 11 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Euroleague Game | ✘ | 49 | 0 | 24% | 8% | -100% | -58% | 14 min |
| National League Game | ✘ | 49 | 1 | 2% | 2% | +90% | -96% | 5 min |
| Liga Expansion Game | ✘ | 49 | 0 | 6% | 4% | -100% | -89% | 10 min |
| LNBP Basketball Game | ✘ | 48 | 0 | 6% | 0% | -100% | -89% | 14 min |
| ELH Game | ✘ | 46 | 0 | 2% | 2% | -100% | -96% | 5 min |
| EuroCup Basketball Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 9 min |
| NFL Game | ✔ | 44 | 1 | 20% | 9% | +112% | -65% | 4 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| Mobile Legends Bang Bang Game | ✘ | 44 | 0 | 0% | 0% | -100% | -100% | 4 min |
| College Hockey Game | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Chinese Basketball Association Game  | ✘ | 43 | 0 | 2% | 0% | -100% | -96% | 10 min |
| DEL Game | ✘ | 42 | 0 | 0% | 0% | -100% | -100% | 5 min |
| China League 1 Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 9 min |
| SHL Game | ✘ | 41 | 0 | 2% | 2% | -100% | -96% | 5 min |
| Women's T20 Match | ✘ | 41 | 0 | 20% | 10% | -100% | -66% | 26 min |
| Japan J League Game | ✘ | 40 | 0 | 15% | 5% | -100% | -74% | 13 min |
| Serie A Game | ✔ | 39 | 0 | 8% | 8% | -100% | -87% | 12 min |
| Peru Liga 1 Game | ✘ | 38 | 0 | 13% | 11% | -100% | -77% | 10 min |
| Indonesia Super League Game | ✘ | 38 | 0 | 13% | 5% | -100% | -77% | 8 min |
| La Liga Game | ✔ | 38 | 0 | 29% | 21% | -100% | -50% | 8 min |
| Liga MX Game | ✔ | 37 | 0 | 14% | 11% | -100% | -77% | 2 min |
| Polish Ekstraklasa Game | ✘ | 37 | 0 | 11% | 3% | -100% | -81% | 9 min |
| UEFA Champions League Game | partly | 37 | 1 | 14% | 5% | +152% | -77% | 12 min |
| NWSL Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 7 min |
| Bundesliga 2 Game | ✔ | 36 | 0 | 14% | 6% | -100% | -76% | 8 min |
| Serie B Game | ✘ | 36 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Eredivisie Game | ✔ | 36 | 0 | 11% | 8% | -100% | -81% | 4 min |
| Ligue 2 Game | ✘ | 36 | 0 | 17% | 11% | -100% | -71% | 7 min |
| Ligue 1 Game | ✔ | 36 | 0 | 17% | 8% | -100% | -71% | 9 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| EFL League One Game | ✔ | 35 | 0 | 11% | 3% | -100% | -80% | 5 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| Turkish Super Lig Game | ✘ | 34 | 0 | 18% | 0% | -100% | -69% | 14 min |
| English Premier League Game | ✔ | 34 | 0 | 12% | 6% | -100% | -80% | 12 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Valorant game winner | ✘ | 32 | 0 | 6% | 3% | -100% | -89% | 15 min |
| Korea K-League 2 Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 8 min |
| Thai League 1 Game | ✘ | 32 | 0 | 22% | 9% | -100% | -62% | 8 min |
| Eliteserien Game | ✘ | 32 | 0 | 12% | 6% | -100% | -78% | 16 min |
| Ecuador Liga Pro Game | ✘ | 32 | 0 | 9% | 3% | -100% | -84% | 6 min |
| Chinese Super League Game | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 18 min |
| Saudi Pro League Game | ✘ | 31 | 1 | 23% | 16% | +201% | -61% | 14 min |
| Czech National Football League Game | ✘ | 31 | 0 | 10% | 10% | -100% | -83% | 9 min |
| Czech First League Game | ✘ | 31 | 0 | 16% | 0% | -100% | -72% | 9 min |
| Allsvenskan Game | ✘ | 31 | 0 | 13% | 13% | -100% | -78% | 12 min |
| Italy Serie A2 Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Bolivia Premier Division Game | ✘ | 30 | 0 | 17% | 3% | -100% | -71% | 3 min |
| APF Division de Honor Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 5 min |
| Adriatic ABA Game | ✘ | 29 | 0 | 3% | 3% | -100% | -94% | 10 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Finland Korisliiga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| England Women's Super League Game | ✘ | 28 | 0 | 21% | 7% | -100% | -63% | 39 min |
| Israeli Premier League Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Venezuela Liga FUTVE game | ✘ | 28 | 0 | 18% | 14% | -100% | -69% | 6 min |
| Spain Liga ACB Game | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 17 min |
| Bundesliga Game | ✔ | 27 | 1 | 15% | 11% | +246% | -74% | 5 min |
| Serbian SuperLiga Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 17 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| Korea K League Game | ✘ | 25 | 1 | 24% | 12% | +273% | -58% | 8 min |
| Super League Greece Game | ✘ | 25 | 0 | 24% | 8% | -100% | -58% | 13 min |
| LNB Elite Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Serie A Femminile Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Italy Serie A Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Danish Superliga Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 9 min |
| Sweden SBL Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Australia NBL Game | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 6 min |
| Men's ODI Cricket Match | ✘ | 23 | 0 | 9% | 0% | -100% | -85% | 27 min |
| Czech NBL Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 17 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Vietnam V-League 1 Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Latvian Virsliga Game | ✘ | 21 | 0 | 14% | 5% | -100% | -75% | 17 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Russia VTB United Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 13 min |
| Faroe Islands Premier League Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 131 min |
| Egyptian Premier League Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Turkey BSL Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Croatia HNL Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 16 min |
| Scottish Premiership Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 11 min |
| Slovenian Prva Liga Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Japan B League Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 10 min |
| Austria BSL Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 6 min |
| Liga Portugal Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 10 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Croatia Premijer Liga Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Singapore Premier League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 16 min |
| Spanish Liga F Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's Pro Basketball Game | ✔ | 15 | 0 | 20% | 7% | -100% | -65% | 6 min |
| Slovakia SBL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 21 min |
| England Super League Basketball Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Women's ODI Cricket Match | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 56 min |
| LKL Lithuania Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Romanian Liga I Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Slovenia 1. SKL Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 15 min |
| CFL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| Korea KBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 9 min |
| FIBA Europe Cup Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Indian Super League Game | ✘ | 12 | 0 | 17% | 17% | -100% | -71% | 10 min |
| Qatar Stars League | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 4 min |
| German Women's Bundesliga Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 23 min |
| Austrian Bundesliga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Hungarian NB I Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Australian A League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 4 min |
| French Women's Première Ligue Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| BNXT League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| FIBA Champions League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Men's Iceland Basketball Premier League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Brazil NBB Basketball Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 13 min |
| eFootball Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 178 min |
| Liga Nacional de Basquetbol Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Colombia LBP Basketball Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CONMEBOL Sudamericana Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Israel Super League Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 16 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| Philippines PBA Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Women's Bundesliga Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| GBL Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 14 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 617 | 5% | 1% | 0% | -91% |
| 5–15 min | 328 | 17% | 7% | 1% | -70% |
| 15–30 min | 212 | 29% | 16% | 1% | -50% |
| 30–60 min | 173 | 20% | 12% | 0% | -65% |
| Over 60 min | 139 | 19% | 10% | 0% | -68% |

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
| 10-20 14:14 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-20 14:14 | eSoccer Game | Manchester City (Mei) | ✘ | — | — | In play | — |
| 10-20 14:13 | Russia Liga Pro Match | Surikov Viacheslav | ✘ | — | — | In play | — |
| 10-20 14:13 | eSoccer Game | Chelsea (Lotta) | ✘ | — | — | In play | — |
| 10-20 14:13 | eSoccer Game | Arsenal (Demi) | ✘ | — | — | In play | — |
| 10-20 14:13 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-20 14:11 | eSoccer Game | OGC Nice (Eder) | ✘ | — | — | In play | — |
| 10-20 14:09 | eBasketball Game | Indiana Pacers (Donovan) | ✘ | — | — | In play | — |
| 10-20 14:08 | ITF Women's Match | Anna-Lena Friedsam | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 14:07 | ITF Women's Match | Analu Freitas | ✘ | — | — | In play | — |
| 10-20 14:04 | eSoccer Game | Hoffenheim (SilentShooter) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 14:04 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 14:02 | Russia Liga Pro Match | Slesarev Vladimir | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 14:02 | ITF Men's Match | Kaan Isik Kosaner | ✘ | — | — | In play | — |
| 10-20 14:02 | ITF Men's Match | Yash Chaurasia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 14:02 | eSoccer Game | AS Monaco (Bony) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 14:02 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 14:01 | eFootball Game | Philadelphia (Pablo) | ✘ | — | — | In play | — |
| 10-20 14:01 | ITF Women's Match | Maria Martinez Vaquero | ✘ | — | — | In play | — |
| 10-20 14:00 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 14:00 | Dota 2 Game | Power Rangers | ✘ | — | — | In play | — |
| 10-20 14:00 | eSoccer Game | Toulouse FC (Holis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 13:59 | Indonesia Super League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 13:59 | eSoccer Game | Rennes (Eder) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 13:58 | ITF Women's Match | Isis Louise Van den Broek | ✘ | — | — | In play | — |
| 10-20 13:56 | ITF Men's Match | Pierre Antoine Tailleu | ✘ | — | — | In play | — |
| 10-20 13:54 | Russia Liga Pro Match | Murzakmatov Ernist | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 13:53 | ITF Women's Match | Lavinia Luciano | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 13:51 | Indonesia Super League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-20 13:49 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
