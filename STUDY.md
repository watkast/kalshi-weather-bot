# 1¢ Study

*Updated Sat Oct 31, 12:32 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

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
| 40657 | 2231 | 9 (0%) | 1.1% | -$208.65 (-62%) | Hold to the end: -$208.65 (-62%) |

*In play right now: 20. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 2231 | 14% | 9% | 7% | 3% | 1% | 1% |
| Unverified | 38406 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 9 | 0% | -$208.65 | -62% |
| Sell at 2¢ | 302 | 14% | -$256.13 | -77% |
| Sell at 3¢ | 211 | 9% | -$252.36 | -75% |
| Sell at 5¢ | 146 | 7% | -$239.75 | -72% |
| Sell at 10¢ | 67 | 3% | -$246.88 | -74% |
| Sell at 25¢ | 22 | 1% | -$261.83 | -78% |
| Sell at 50¢ | 15 | 1% | -$233.40 | -70% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 18501 | 12 | 1% | 1% | -94% | -99% | 3 min |
| Russia Liga Pro Match | ✘ | 2171 | 0 | 1% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 1820 | 3 | 2% | 1% | -85% | -92% | 2 min |
| ITF Women's Match | ✘ | 1404 | 6 | 14% | 6% | -60% | -77% | 4 min |
| ITF Men's Match | ✘ | 1319 | 1 | 13% | 5% | -93% | -78% | 5 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Counter-Strike 2 Game | ✘ | 1272 | 2 | 6% | 3% | -85% | -90% | 12 min |
| Challenger ATP  | ✘ | 789 | 2 | 11% | 4% | -76% | -81% | 5 min |
| eFootball Game | ✘ | 458 | 2 | 1% | 1% | -59% | -98% | 2 min |
| Darts Match | ✘ | 368 | 0 | 0% | 0% | -100% | -100% | 7 min |
| College Football Game | partly | 344 | 2 | 11% | 6% | -46% | -80% | 23 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Men's T20 Cricket Match | ✘ | 284 | 1 | 15% | 6% | -67% | -74% | 23 min |
| Women's College Volleyball Match | ✘ | 284 | 2 | 5% | 3% | -34% | -91% | 70 min |
| Dota 2 Game | ✘ | 254 | 1 | 1% | 1% | -63% | -98% | 30 min |
| Serie C Game | ✘ | 242 | 2 | 4% | 2% | -23% | -93% | 6 min |
| Challenger WTA | ✘ | 231 | 0 | 13% | 4% | -100% | -77% | 9 min |
| NHL Game | ✔ | 216 | 1 | 13% | 6% | -57% | -77% | 5 min |
| WTA Tennis Match | ✘ | 158 | 0 | 11% | 2% | -100% | -80% | 5 min |
| Major League Soccer Game | partly | 157 | 1 | 11% | 6% | -41% | -80% | 6 min |
| League of Legends Game | ✘ | 155 | 0 | 6% | 2% | -100% | -89% | 11 min |
| AHL Game | ✘ | 150 | 0 | 4% | 2% | -100% | -93% | 5 min |
| NBA Game | ✔ | 142 | 0 | 17% | 5% | -100% | -71% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Argentina Primera Division Game | ✘ | 124 | 1 | 14% | 8% | -25% | -76% | 7 min |
| KHL Game | ✘ | 122 | 0 | 5% | 2% | -100% | -91% | 6 min |
| Ettan Game | ✘ | 119 | 0 | 4% | 1% | -100% | -93% | 7 min |
| Liga DIMAYOR Game | ✘ | 115 | 1 | 9% | 3% | -19% | -85% | 6 min |
| Argentine Nacional B Game | ✘ | 112 | 0 | 9% | 6% | -100% | -85% | 8 min |
| Brasileiro Serie B Game | ✘ | 109 | 1 | 7% | 4% | -14% | -87% | 8 min |
| ATP Tennis Match | ✘ | 109 | 0 | 15% | 6% | -100% | -75% | 4 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| English National League Game | ✘ | 106 | 1 | 9% | 7% | -12% | -84% | 11 min |
| USL Championship Game | partly | 104 | 0 | 12% | 5% | -100% | -78% | 5 min |
| Brasileiro Serie A Game | partly | 102 | 1 | 12% | 7% | -8% | -80% | 7 min |
| Japan J2 League Game | ✘ | 102 | 0 | 12% | 5% | -100% | -80% | 6 min |
| Overwatch Game | ✘ | 99 | 0 | 2% | 0% | -100% | -96% | 6 min |
| College Hockey Game | ✘ | 98 | 0 | 0% | 0% | -100% | -100% | 6 min |
| LaLiga 2 Game | partly | 89 | 1 | 18% | 9% | +5% | -69% | 9 min |
| Liiga Game | ✘ | 88 | 0 | 0% | 0% | -100% | -100% | 5 min |
| EFL League One Game | ✔ | 88 | 0 | 10% | 3% | -100% | -82% | 10 min |
| National League Game | ✘ | 84 | 1 | 1% | 1% | +11% | -98% | 5 min |
| Valorant game winner | ✘ | 82 | 0 | 5% | 2% | -100% | -92% | 13 min |
| Chinese Basketball Association Game  | ✘ | 81 | 0 | 7% | 1% | -100% | -87% | 10 min |
| Japan J League Game | ✘ | 81 | 1 | 19% | 7% | +15% | -68% | 12 min |
| German 3. Liga Game | ✘ | 81 | 0 | 11% | 5% | -100% | -81% | 7 min |
| Liga Leumit Game | ✘ | 80 | 0 | 4% | 4% | -100% | -94% | 19 min |
| EFL Championship Game | ✔ | 80 | 0 | 9% | 5% | -100% | -85% | 9 min |
| Liga MX Game | ✔ | 79 | 0 | 14% | 9% | -100% | -76% | 6 min |
| Euroleague Game | ✘ | 78 | 0 | 21% | 6% | -100% | -64% | 13 min |
| Serie A Game | ✔ | 78 | 0 | 9% | 5% | -100% | -84% | 12 min |
| Eerste Divisie Game | ✘ | 77 | 0 | 10% | 6% | -100% | -82% | 8 min |
| Copa Del Rey Game | ✘ | 77 | 0 | 6% | 5% | -100% | -89% | 40 min |
| EuroCup Basketball Game | ✘ | 76 | 0 | 5% | 4% | -100% | -91% | 11 min |
| Serie B Game | ✘ | 76 | 0 | 14% | 7% | -100% | -75% | 9 min |
| R6 Game | ✘ | 75 | 1 | 9% | 4% | +24% | -84% | 9 min |
| TFF 1. Lig Game | ✘ | 74 | 0 | 16% | 9% | -100% | -72% | 10 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| ELH Game | ✘ | 72 | 0 | 1% | 1% | -100% | -98% | 4 min |
| Peru Liga 1 Game | ✘ | 72 | 0 | 14% | 6% | -100% | -76% | 11 min |
| Slovakian 2. Liga Game | ✘ | 70 | 0 | 7% | 6% | -100% | -88% | 83 min |
| Indonesia Super League Game | ✘ | 70 | 0 | 16% | 10% | -100% | -73% | 8 min |
| Saudi Pro League Game | ✘ | 70 | 2 | 19% | 11% | +167% | -68% | 14 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| Liga Expansion Game | ✘ | 69 | 0 | 7% | 3% | -100% | -87% | 10 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| Uruguay Primera Division Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 10 min |
| DEL Game | ✘ | 66 | 0 | 0% | 0% | -100% | -100% | 5 min |
| SHL Game | ✘ | 65 | 0 | 3% | 3% | -100% | -95% | 6 min |
| Ligue 2 Game | ✘ | 64 | 0 | 9% | 6% | -100% | -84% | 7 min |
| Mobile Legends Bang Bang Game | ✘ | 63 | 0 | 0% | 0% | -100% | -100% | 4 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| La Liga Game | ✔ | 62 | 0 | 21% | 15% | -100% | -64% | 7 min |
| Women's T20 Match | ✘ | 61 | 0 | 13% | 7% | -100% | -77% | 23 min |
| Allsvenskan Game | ✘ | 61 | 1 | 16% | 11% | +53% | -72% | 10 min |
| Men's ODI Cricket Match | ✘ | 60 | 3 | 22% | 8% | +367% | -62% | 43 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| NFL Game | ✔ | 59 | 1 | 20% | 8% | +58% | -65% | 5 min |
| Polish Ekstraklasa Game | ✘ | 59 | 0 | 12% | 7% | -100% | -79% | 8 min |
| LNBP Basketball Game | ✘ | 58 | 0 | 7% | 0% | -100% | -88% | 12 min |
| China League 1 Game | ✘ | 57 | 0 | 12% | 7% | -100% | -79% | 10 min |
| Bundesliga 2 Game | ✔ | 57 | 0 | 12% | 7% | -100% | -79% | 8 min |
| AFC Champions League Game | ✘ | 56 | 0 | 5% | 0% | -100% | -91% | 8 min |
| LNB Elite 2 Game | ✘ | 55 | 0 | 2% | 0% | -100% | -97% | 7 min |
| KBO Game | ✘ | 54 | 0 | 11% | 6% | -100% | -81% | 4 min |
| Turkish Super Lig Game | ✘ | 54 | 0 | 13% | 2% | -100% | -78% | 14 min |
| Ligue 1 Game | ✔ | 54 | 0 | 17% | 7% | -100% | -71% | 8 min |
| English Premier League Game | ✔ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| Japan B League Game | ✘ | 54 | 0 | 7% | 0% | -100% | -87% | 13 min |
| NWSL Game | ✔ | 52 | 0 | 10% | 2% | -100% | -83% | 7 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Italy Serie A2 Game | ✘ | 51 | 0 | 2% | 0% | -100% | -97% | 6 min |
| Czech National Football League Game | ✘ | 51 | 0 | 14% | 8% | -100% | -76% | 8 min |
| Eredivisie Game | ✔ | 51 | 0 | 10% | 8% | -100% | -83% | 4 min |
| Thai League 1 Game | ✘ | 50 | 0 | 18% | 6% | -100% | -69% | 11 min |
| Eliteserien Game | ✘ | 50 | 0 | 10% | 4% | -100% | -83% | 12 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Korea K-League 2 Game | ✘ | 48 | 0 | 12% | 6% | -100% | -78% | 9 min |
| Ecuador Liga Pro Game | ✘ | 48 | 0 | 8% | 2% | -100% | -86% | 8 min |
| Bolivia Premier Division Game | ✘ | 48 | 0 | 10% | 2% | -100% | -82% | 6 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| Bundesliga Game | ✔ | 47 | 1 | 13% | 9% | +99% | -78% | 7 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Finland Korisliiga Game | ✘ | 46 | 1 | 9% | 4% | +103% | -85% | 9 min |
| APF Division de Honor Game | ✘ | 45 | 0 | 22% | 7% | -100% | -61% | 8 min |
| Czech First League Game | ✘ | 45 | 0 | 11% | 0% | -100% | -81% | 8 min |
| Serbian SuperLiga Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 11 min |
| Egyptian Premier League Game | ✘ | 44 | 0 | 7% | 7% | -100% | -88% | 6 min |
| Vietnam V-League 1 Game | ✘ | 43 | 1 | 7% | 5% | +117% | -88% | 9 min |
| England Women's Super League Game | ✘ | 42 | 0 | 21% | 10% | -100% | -63% | 26 min |
| Israeli Premier League Game | ✘ | 42 | 0 | 5% | 0% | -100% | -92% | 9 min |
| Scottish Premiership Game | ✘ | 41 | 0 | 12% | 2% | -100% | -79% | 10 min |
| Adriatic ABA Game | ✘ | 40 | 0 | 5% | 2% | -100% | -91% | 11 min |
| Venezuela Liga FUTVE game | ✘ | 40 | 0 | 18% | 12% | -100% | -70% | 6 min |
| Super League Greece Game | ✘ | 39 | 0 | 18% | 5% | -100% | -69% | 14 min |
| FIBA Europe Cup Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 8 min |
| Liga Portugal Game | ✘ | 38 | 0 | 5% | 3% | -100% | -91% | 10 min |
| Chile Liga de Primera Game | ✘ | 37 | 0 | 11% | 0% | -100% | -81% | 7 min |
| Korea K League Game | ✘ | 37 | 1 | 19% | 11% | +152% | -67% | 8 min |
| Danish Superliga Game | ✘ | 37 | 0 | 11% | 5% | -100% | -81% | 10 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Champions League Women's Game | partly | 36 | 1 | 19% | 8% | +159% | -66% | 26 min |
| Serie A Femminile Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Spain Liga ACB Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 14 min |
| Belgian Pro League Game | ✘ | 36 | 0 | 11% | 0% | -100% | -81% | 19 min |
| Sweden SBL Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 14 min |
| Australia NBL Game | ✘ | 34 | 0 | 3% | 0% | -100% | -95% | 8 min |
| LNB Elite Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Rugby French 14 Match | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Czech NBL Game | ✘ | 32 | 0 | 3% | 0% | -100% | -95% | 17 min |
| Italy Serie A Game | ✘ | 32 | 0 | 3% | 3% | -100% | -95% | 6 min |
| Romanian Liga I Game | ✘ | 32 | 0 | 9% | 3% | -100% | -84% | 12 min |
| Spanish Liga F Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 7 min |
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
| German Women's Bundesliga Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| Austria BSL Game | ✘ | 27 | 0 | 11% | 7% | -100% | -81% | 8 min |
| Turkey BSL Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Singapore Premier League Game | ✘ | 26 | 0 | 15% | 4% | -100% | -73% | 18 min |
| Korea KBL Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Australian A League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 6 min |
| Indian Super League Game | ✘ | 26 | 0 | 15% | 8% | -100% | -73% | 8 min |
| Austrian Bundesliga Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 13 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| Croatia Premijer Liga Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 9 min |
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
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Malaysia Super League Game | ✘ | 13 | 0 | 15% | 0% | -100% | -73% | 9 min |
| Philippines PBA Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Colombia LBP Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| South African Premiership Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 2 min |
| United Rugby Championship Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 3 min |
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
| Under 5 min | 892 | 4% | 1% | 0% | -92% |
| 5–15 min | 526 | 17% | 7% | 1% | -70% |
| 15–30 min | 346 | 24% | 13% | 1% | -58% |
| 30–60 min | 259 | 19% | 12% | 0% | -67% |
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
| 10-31 06:31 | eSoccer Game | FC Barcelona (Nate) | ✘ | — | — | In play | — |
| 10-31 06:31 | eSoccer Game | Getafe CF (Ousmane) | ✘ | — | — | In play | — |
| 10-31 06:30 | eSoccer Game | Arsenal (Mia) | ✘ | — | — | In play | — |
| 10-31 06:30 | eSoccer Game | Manchester Utd (Rose) | ✘ | — | — | In play | — |
| 10-31 06:28 | Japan J League Game | Tie | ✘ | — | — | In play | — |
| 10-31 06:23 | Japan J League Game | Shimizu | ✘ | — | — | In play | — |
| 10-31 06:22 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:22 | Russia Liga Pro Match | Smyshnikov Maksim | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:21 | eSoccer Game | Toulouse FC (Poly) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:21 | Japan J League Game | Tie | ✘ | — | — | In play | — |
| 10-31 06:21 | Women's T20 Match | Assam Women | ✘ | — | — | In play | — |
| 10-31 06:20 | Russia Liga Pro Match | Bogomolov Albert | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:20 | Japan J League Game | Fagiano O | ✘ | — | — | In play | — |
| 10-31 06:20 | eSoccer Game | CA Osasuna (Elastico) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:20 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:19 | eSoccer Game | Manchester City (Annie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:19 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:19 | Dota 2 Game | Direborn | ✘ | — | — | In play | — |
| 10-31 06:17 | eSoccer Game | Girona (Rendeto) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:17 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:16 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:15 | eSoccer Game | Manchester Utd (Rose) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:14 | eBasketball Game | Dallas Mavericks (Cade) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:11 | eBasketball Game | New Orleans Pelicans (Davis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:09 | eSoccer Game | Stade Brestois 29 (Strudl) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:09 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:08 | Russia Liga Pro Match | Lobanov Aleksey | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:06 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:06 | eSoccer Game | RC Celta (Vini) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-31 06:05 | eSoccer Game | Manchester City (Annie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
