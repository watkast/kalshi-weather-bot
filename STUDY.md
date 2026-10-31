# 1¢ Study

*Updated Sat Oct 31, 9:44 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 44 finished bets | 2% | $7.40 | +112% | +16.82¢ | $10.70 / -$3.30 |

*Expect about **2 buys a day**, roughly **$0.24/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 92 | $0.20 | +1% |
| ESPN win probability ≥ 5%, sell at 50¢ | 44 | $0.15 | +2% |
| ESPN win probability ≥ 5%, sell at 25¢ | 44 | $0.02 | +0% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 41404 | 2253 | 9 (0%) | 1.1% | -$211.95 (-63%) | Hold to the end: -$211.95 (-63%) |

*In play right now: 35. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 413 | 3.2% | 0.2% (1) | -89% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 413 | 1 | -77% | -73% | -72% | -73% |
| ESPN win probability ≥ 2% | 92 | 1 | +1% | -62% | -66% | -72% |
| ESPN win probability ≥ 5% | 44 | 1 | +112% | -76% | -76% | -80% |
| ESPN win probability ≥ 10% | 29 | 1 | +222% | -70% | -64% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 2253 | 13% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 39116 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 9 | 0% | -$211.95 | -63% |
| Sell at 2¢ | 303 | 13% | -$259.17 | -77% |
| Sell at 3¢ | 211 | 9% | -$255.66 | -76% |
| Sell at 5¢ | 146 | 6% | -$243.05 | -72% |
| Sell at 10¢ | 67 | 3% | -$250.18 | -74% |
| Sell at 25¢ | 22 | 1% | -$265.13 | -78% |
| Sell at 50¢ | 15 | 1% | -$236.70 | -70% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 18855 | 12 | 1% | 1% | -94% | -99% | 3 min |
| Russia Liga Pro Match | ✘ | 2245 | 0 | 1% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 1855 | 3 | 2% | 1% | -85% | -92% | 2 min |
| ITF Women's Match | ✘ | 1406 | 6 | 14% | 6% | -60% | -77% | 4 min |
| ITF Men's Match | ✘ | 1325 | 2 | 13% | 5% | -86% | -77% | 5 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Counter-Strike 2 Game | ✘ | 1282 | 2 | 6% | 3% | -85% | -90% | 12 min |
| Challenger ATP  | ✘ | 791 | 2 | 11% | 4% | -76% | -81% | 5 min |
| eFootball Game | ✘ | 472 | 2 | 1% | 1% | -60% | -98% | 2 min |
| Darts Match | ✘ | 368 | 0 | 0% | 0% | -100% | -100% | 7 min |
| College Football Game | partly | 344 | 2 | 11% | 6% | -46% | -80% | 23 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Men's T20 Cricket Match | ✘ | 286 | 1 | 15% | 6% | -67% | -73% | 23 min |
| Women's College Volleyball Match | ✘ | 284 | 2 | 5% | 3% | -34% | -91% | 70 min |
| Dota 2 Game | ✘ | 257 | 1 | 1% | 1% | -64% | -98% | 30 min |
| Serie C Game | ✘ | 252 | 2 | 4% | 2% | -26% | -93% | 6 min |
| Challenger WTA | ✘ | 233 | 0 | 13% | 4% | -100% | -78% | 9 min |
| NHL Game | ✔ | 216 | 1 | 13% | 6% | -57% | -77% | 5 min |
| WTA Tennis Match | ✘ | 166 | 0 | 12% | 2% | -100% | -79% | 5 min |
| Major League Soccer Game | partly | 157 | 1 | 11% | 6% | -41% | -80% | 6 min |
| League of Legends Game | ✘ | 155 | 0 | 6% | 2% | -100% | -89% | 11 min |
| AHL Game | ✘ | 150 | 0 | 4% | 2% | -100% | -93% | 5 min |
| NBA Game | ✔ | 142 | 0 | 17% | 5% | -100% | -71% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Argentina Primera Division Game | ✘ | 124 | 1 | 14% | 8% | -25% | -76% | 7 min |
| KHL Game | ✘ | 123 | 0 | 5% | 2% | -100% | -92% | 6 min |
| Ettan Game | ✘ | 123 | 0 | 4% | 1% | -100% | -93% | 7 min |
| Japan J2 League Game | ✘ | 120 | 0 | 11% | 4% | -100% | -81% | 6 min |
| Liga DIMAYOR Game | ✘ | 115 | 1 | 9% | 3% | -19% | -85% | 6 min |
| ATP Tennis Match | ✘ | 113 | 0 | 14% | 6% | -100% | -75% | 4 min |
| Argentine Nacional B Game | ✘ | 112 | 0 | 9% | 6% | -100% | -85% | 8 min |
| English National League Game | ✘ | 110 | 1 | 9% | 6% | -15% | -84% | 11 min |
| Brasileiro Serie B Game | ✘ | 109 | 1 | 7% | 4% | -14% | -87% | 8 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Overwatch Game | ✘ | 104 | 0 | 2% | 0% | -100% | -97% | 6 min |
| USL Championship Game | partly | 104 | 0 | 12% | 5% | -100% | -78% | 5 min |
| Brasileiro Serie A Game | partly | 102 | 1 | 12% | 7% | -8% | -80% | 7 min |
| College Hockey Game | ✘ | 98 | 0 | 0% | 0% | -100% | -100% | 6 min |
| EFL League One Game | ✔ | 94 | 0 | 10% | 3% | -100% | -83% | 10 min |
| Japan J League Game | ✘ | 93 | 1 | 16% | 6% | +0% | -72% | 14 min |
| LaLiga 2 Game | partly | 91 | 1 | 18% | 9% | +3% | -70% | 9 min |
| German 3. Liga Game | ✘ | 89 | 0 | 11% | 6% | -100% | -81% | 7 min |
| Liiga Game | ✘ | 88 | 0 | 0% | 0% | -100% | -100% | 5 min |
| EFL Championship Game | ✔ | 86 | 0 | 8% | 5% | -100% | -86% | 9 min |
| Valorant game winner | ✘ | 84 | 0 | 5% | 2% | -100% | -92% | 12 min |
| National League Game | ✘ | 84 | 1 | 1% | 1% | +11% | -98% | 5 min |
| Chinese Basketball Association Game  | ✘ | 84 | 0 | 7% | 1% | -100% | -88% | 10 min |
| Liga Leumit Game | ✘ | 80 | 0 | 4% | 4% | -100% | -94% | 19 min |
| TFF 1. Lig Game | ✘ | 80 | 0 | 15% | 9% | -100% | -74% | 10 min |
| Liga MX Game | ✔ | 79 | 0 | 14% | 9% | -100% | -76% | 6 min |
| Euroleague Game | ✘ | 78 | 0 | 21% | 6% | -100% | -64% | 13 min |
| Indonesia Super League Game | ✘ | 78 | 0 | 14% | 9% | -100% | -76% | 9 min |
| Serie A Game | ✔ | 78 | 0 | 9% | 5% | -100% | -84% | 12 min |
| Eerste Divisie Game | ✘ | 77 | 0 | 10% | 6% | -100% | -82% | 8 min |
| Copa Del Rey Game | ✘ | 77 | 0 | 6% | 5% | -100% | -89% | 40 min |
| Slovakian 2. Liga Game | ✘ | 76 | 0 | 7% | 5% | -100% | -89% | 79 min |
| EuroCup Basketball Game | ✘ | 76 | 0 | 5% | 4% | -100% | -91% | 11 min |
| Serie B Game | ✘ | 76 | 0 | 14% | 7% | -100% | -75% | 9 min |
| R6 Game | ✘ | 75 | 1 | 9% | 4% | +24% | -84% | 9 min |
| China League 1 Game | ✘ | 73 | 0 | 10% | 5% | -100% | -83% | 9 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| ELH Game | ✘ | 72 | 0 | 1% | 1% | -100% | -98% | 4 min |
| Peru Liga 1 Game | ✘ | 72 | 0 | 14% | 6% | -100% | -76% | 11 min |
| Saudi Pro League Game | ✘ | 72 | 2 | 19% | 12% | +159% | -66% | 13 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| Liga Expansion Game | ✘ | 69 | 0 | 7% | 3% | -100% | -87% | 10 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| Uruguay Primera Division Game | ✘ | 68 | 0 | 9% | 3% | -100% | -85% | 10 min |
| Women's T20 Match | ✘ | 67 | 0 | 13% | 6% | -100% | -77% | 25 min |
| Mobile Legends Bang Bang Game | ✘ | 67 | 0 | 0% | 0% | -100% | -100% | 4 min |
| DEL Game | ✘ | 66 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Ligue 2 Game | ✘ | 66 | 0 | 9% | 6% | -100% | -84% | 7 min |
| SHL Game | ✘ | 65 | 0 | 3% | 3% | -100% | -95% | 6 min |
| La Liga Game | ✔ | 64 | 0 | 20% | 14% | -100% | -65% | 8 min |
| Japan B League Game | ✘ | 64 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Men's ODI Cricket Match | ✘ | 63 | 3 | 22% | 8% | +344% | -61% | 41 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Bundesliga 2 Game | ✔ | 63 | 0 | 11% | 6% | -100% | -81% | 8 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| Polish Ekstraklasa Game | ✘ | 61 | 0 | 11% | 7% | -100% | -80% | 8 min |
| Allsvenskan Game | ✘ | 61 | 1 | 16% | 11% | +53% | -72% | 10 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| NFL Game | ✔ | 59 | 1 | 20% | 8% | +58% | -65% | 5 min |
| LNBP Basketball Game | ✘ | 58 | 0 | 7% | 0% | -100% | -88% | 12 min |
| Turkish Super Lig Game | ✘ | 58 | 0 | 14% | 2% | -100% | -76% | 13 min |
| Korea K-League 2 Game | ✘ | 56 | 0 | 12% | 7% | -100% | -78% | 8 min |
| English Premier League Game | ✔ | 56 | 0 | 9% | 4% | -100% | -85% | 10 min |
| AFC Champions League Game | ✘ | 56 | 0 | 5% | 0% | -100% | -91% | 8 min |
| LNB Elite 2 Game | ✘ | 55 | 0 | 2% | 0% | -100% | -97% | 7 min |
| KBO Game | ✘ | 54 | 0 | 11% | 6% | -100% | -81% | 4 min |
| Thai League 1 Game | ✘ | 54 | 0 | 19% | 7% | -100% | -68% | 11 min |
| Ligue 1 Game | ✔ | 54 | 0 | 17% | 7% | -100% | -71% | 8 min |
| NWSL Game | ✔ | 52 | 0 | 10% | 2% | -100% | -83% | 7 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Italy Serie A2 Game | ✘ | 51 | 0 | 2% | 0% | -100% | -97% | 6 min |
| Czech National Football League Game | ✘ | 51 | 0 | 14% | 8% | -100% | -76% | 8 min |
| Eredivisie Game | ✔ | 51 | 0 | 10% | 8% | -100% | -83% | 4 min |
| Eliteserien Game | ✘ | 50 | 0 | 10% | 4% | -100% | -83% | 12 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Vietnam V-League 1 Game | ✘ | 48 | 1 | 6% | 4% | +94% | -89% | 10 min |
| Ecuador Liga Pro Game | ✘ | 48 | 0 | 8% | 2% | -100% | -86% | 8 min |
| Bolivia Premier Division Game | ✘ | 48 | 0 | 10% | 2% | -100% | -82% | 6 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| Bundesliga Game | ✔ | 47 | 1 | 13% | 9% | +99% | -78% | 7 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Finland Korisliiga Game | ✘ | 46 | 1 | 9% | 4% | +103% | -85% | 9 min |
| APF Division de Honor Game | ✘ | 45 | 0 | 22% | 7% | -100% | -61% | 8 min |
| Czech First League Game | ✘ | 45 | 0 | 11% | 0% | -100% | -81% | 8 min |
| England Women's Super League Game | ✘ | 44 | 0 | 20% | 9% | -100% | -65% | 21 min |
| Serbian SuperLiga Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 11 min |
| Israeli Premier League Game | ✘ | 44 | 0 | 5% | 0% | -100% | -92% | 9 min |
| Egyptian Premier League Game | ✘ | 44 | 0 | 7% | 7% | -100% | -88% | 6 min |
| Korea K League Game | ✘ | 41 | 1 | 17% | 10% | +128% | -70% | 7 min |
| Scottish Premiership Game | ✘ | 41 | 0 | 12% | 2% | -100% | -79% | 10 min |
| Adriatic ABA Game | ✘ | 40 | 0 | 5% | 2% | -100% | -91% | 11 min |
| Venezuela Liga FUTVE game | ✘ | 40 | 0 | 18% | 12% | -100% | -70% | 6 min |
| Super League Greece Game | ✘ | 39 | 0 | 18% | 5% | -100% | -69% | 14 min |
| FIBA Europe Cup Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 8 min |
| Serie A Femminile Game | ✘ | 38 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga Portugal Game | ✘ | 38 | 0 | 5% | 3% | -100% | -91% | 10 min |
| Chile Liga de Primera Game | ✘ | 37 | 0 | 11% | 0% | -100% | -81% | 7 min |
| Danish Superliga Game | ✘ | 37 | 0 | 11% | 5% | -100% | -81% | 10 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Australia NBL Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 9 min |
| Champions League Women's Game | partly | 36 | 1 | 19% | 8% | +159% | -66% | 26 min |
| Spain Liga ACB Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 14 min |
| Belgian Pro League Game | ✘ | 36 | 0 | 11% | 0% | -100% | -81% | 19 min |
| Spanish Liga F Game | ✘ | 36 | 0 | 8% | 6% | -100% | -86% | 7 min |
| Sweden SBL Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 14 min |
| Rugby French 14 Match | ✘ | 35 | 0 | 0% | 0% | -100% | -100% | 6 min |
| LNB Elite Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Czech NBL Game | ✘ | 32 | 0 | 3% | 0% | -100% | -95% | 17 min |
| Italy Serie A Game | ✘ | 32 | 0 | 3% | 3% | -100% | -95% | 6 min |
| Romanian Liga I Game | ✘ | 32 | 0 | 9% | 3% | -100% | -84% | 12 min |
| Brazil NBB Basketball Game | ✘ | 32 | 0 | 6% | 3% | -100% | -89% | 17 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| Canadian Premier League | ✘ | 31 | 1 | 16% | 16% | +201% | -72% | 23 min |
| Croatia HNL Game | ✘ | 31 | 0 | 10% | 6% | -100% | -83% | 9 min |
| Latvian Virsliga Game | ✘ | 31 | 0 | 13% | 3% | -100% | -78% | 18 min |
| Faroe Islands Premier League Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 84 min |
| Qatar Stars League | ✘ | 30 | 0 | 10% | 3% | -100% | -83% | 7 min |
| Russia VTB United Game | ✘ | 29 | 0 | 3% | 0% | -100% | -94% | 15 min |
| Bundesliga Basketball Game | ✘ | 29 | 0 | 14% | 7% | -100% | -76% | 12 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Slovenian Prva Liga Game | ✘ | 29 | 0 | 7% | 3% | -100% | -88% | 6 min |
| Korea KBL Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Turkey BSL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Singapore Premier League Game | ✘ | 28 | 0 | 14% | 4% | -100% | -75% | 18 min |
| Australian A League Game | ✘ | 28 | 0 | 7% | 0% | -100% | -88% | 6 min |
| Indian Super League Game | ✘ | 28 | 0 | 14% | 7% | -100% | -75% | 7 min |
| German Women's Bundesliga Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| Austria BSL Game | ✘ | 27 | 0 | 11% | 7% | -100% | -81% | 8 min |
| Austrian Bundesliga Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 13 min |
| Croatia Premijer Liga Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| England Super League Basketball Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Swiss Super League Game | ✘ | 24 | 0 | 4% | 0% | -100% | -93% | 18 min |
| Hungarian NB I Game | ✘ | 24 | 0 | 8% | 8% | -100% | -86% | 6 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| Slovakia SBL Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 19 min |
| FIBA Champions League Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Ligue Magnus Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| LKL Lithuania Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Eredivisie Vrouwen Game | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 8 min |
| Women's ODI Cricket Match | ✘ | 19 | 0 | 21% | 11% | -100% | -64% | 61 min |
| Slovenia 1. SKL Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 15 min |
| Liga Nacional de Basquetbol Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 5 min |
| BNXT League Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 15 min |
| Men's Iceland Basketball Premier League Game | ✘ | 18 | 0 | 22% | 11% | -100% | -61% | 11 min |
| Women's Pro Basketball Game | ✔ | 17 | 0 | 18% | 6% | -100% | -69% | 6 min |
| French Women's Première Ligue Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 6 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| CFL Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Polish Hockey Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 6 min |
| EuroLeague (W) Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 18 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Malaysia Super League Game | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 9 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Philippines PBA Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 10 min |
| South African Premiership Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Colombia LBP Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| United Rugby Championship Match | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Israel Super League Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 8 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Powerslap Match Winner | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 12 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Ukraine SuperLeague Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 9 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| GBL Basketball Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's Bundesliga Basketball Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 3 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Portugal LPB Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 49 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Serbia KLS Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Denmark Basketligaen Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Premier League Cup Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| NBL Australia (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Hungary NB I. A Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 897 | 4% | 1% | 0% | -92% |
| 5–15 min | 529 | 17% | 7% | 1% | -70% |
| 15–30 min | 351 | 24% | 13% | 1% | -59% |
| 30–60 min | 268 | 19% | 11% | 0% | -67% |
| Over 60 min | 184 | 20% | 11% | 0% | -65% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 38 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-31 15:43 | eFootball Game | Seattle (Joey) | ✘ | — | — | In play | — |
| 10-31 15:43 | Serie A Game | Monza | ✔ | 85' · MON 1 - BOL 2 | — | In play | — |
| 10-31 15:43 | eSoccer Game | OGC Nice (Eder) | ✘ | — | — | In play | — |
| 10-31 15:43 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-31 15:43 | eBasketball Game | Indiana Pacers (Zach) | ✘ | — | — | In play | — |
| 10-31 15:42 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-31 15:42 | eSoccer Game | Everton (Megan) | ✘ | — | — | In play | — |
| 10-31 15:42 | Serie B Game | Mantova | ✘ | — | — | In play | — |
| 10-31 15:40 | eSoccer Game | Olympique Lyon (Holis) | ✘ | — | — | In play | — |
| 10-31 15:40 | eSoccer Game | Olympique de Marseille (Bony) | ✘ | — | — | In play | — |
| 10-31 15:40 | eSoccer Game | Manchester Utd (Nicol) | ✘ | — | — | In play | — |
| 10-31 15:40 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-31 15:37 | EFL Championship Game | Blackburn | ✔ | 37' · BLK 0 - SWA 3 | — | In play | — |
| 10-31 15:37 | ATP Tennis Match | Taylor Fritz | ✘ | — | — | In play | — |
| 10-31 15:32 | Finland Korisliiga Game | Bisons Loimaa | ✘ | — | — | In play | — |
| 10-31 15:31 | Polish Ekstraklasa Game | Tie | ✘ | — | — | In play | — |
| 10-31 15:31 | Polish Ekstraklasa Game | Wieczysta Krakow | ✘ | — | — | In play | — |
| 10-31 15:31 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:31 | eSoccer Game | Leverkusen (Haze) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:31 | Russia Liga Pro Match | Glazun Evgeniy | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:30 | Russia Liga Pro Match | SHkolnikov IUrii | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:30 | Challenger WTA | Julia Riera | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:30 | eSoccer Game | Paris Saint-Germain (Sheerpy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:30 | eSoccer Game | Strasbourg (Fede) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:28 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:28 | eSoccer Game | Manchester City (Quinnie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:28 | Russia Liga Pro Match | Kondratev Gennadii | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:28 | Rugby French 14 Match | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:28 | Rugby French 14 Match | Racing 92 | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 15:28 | South African Premiership Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
