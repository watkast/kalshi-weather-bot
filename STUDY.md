# 1¢ Study

*Updated Sat Nov 21, 11:35 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 81 finished bets | 1% | $1.85 | +15% | +2.28¢ | $8.00 / -$6.15 |

*Expect about **2 buys a day**, roughly **$0.25/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 196 | -$1.40 | -5% |
| ESPN win probability ≥ 5%, sell at 50¢ | 81 | -$5.40 | -44% |
| ESPN win probability ≥ 5%, sell at 25¢ | 81 | -$5.53 | -46% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 71302 | 3943 | 16 (0%) | 1.1% | -$367.45 (-62%) | Hold to the end: -$367.45 (-62%) |

*In play right now: 40. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 1047 | 2.7% | 0.2% (2) | -208% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1047 | 2 | -82% | -71% | -70% | -71% |
| ESPN win probability ≥ 2% | 196 | 2 | -5% | -60% | -62% | -67% |
| ESPN win probability ≥ 5% | 81 | 1 | +15% | -83% | -87% | -89% |
| ESPN win probability ≥ 10% | 55 | 1 | +70% | -81% | -81% | -84% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 3943 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 67319 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 16 | 0% | -$367.45 | -62% |
| Sell at 2¢ | 558 | 14% | -$446.37 | -75% |
| Sell at 3¢ | 392 | 10% | -$438.57 | -74% |
| Sell at 5¢ | 263 | 7% | -$420.50 | -71% |
| Sell at 10¢ | 108 | 3% | -$449.97 | -76% |
| Sell at 25¢ | 42 | 1% | -$452.43 | -76% |
| Sell at 50¢ | 27 | 1% | -$409.20 | -69% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 34067 | 22 | 1% | 1% | -94% | -98% | 3 min |
| Russia Liga Pro Match | ✘ | 4413 | 0 | 2% | 1% | -100% | -97% | 4 min |
| eBasketball Game | ✘ | 3378 | 8 | 3% | 2% | -78% | -91% | 3 min |
| ITF Women's Match | ✘ | 2041 | 8 | 14% | 6% | -63% | -76% | 4 min |
| ITF Men's Match | ✘ | 1989 | 5 | 14% | 6% | -77% | -76% | 5 min |
| Counter-Strike 2 Game | ✘ | 1862 | 3 | 6% | 3% | -85% | -90% | 11 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 1273 | 6 | 12% | 5% | -56% | -79% | 5 min |
| Men's College Basketball Game | partly | 895 | 5 | 20% | 9% | -48% | -65% | 25 min |
| Women's College Basketball Game | partly | 855 | 2 | 14% | 5% | -78% | -75% | 31 min |
| College Football Game | partly | 724 | 4 | 11% | 5% | -48% | -81% | 23 min |
| eFootball Game | ✘ | 668 | 2 | 1% | 1% | -72% | -98% | 2 min |
| Darts Match | ✘ | 476 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Dota 2 Game | ✘ | 438 | 1 | 1% | 1% | -79% | -98% | 32 min |
| Women's College Volleyball Match | ✘ | 437 | 2 | 4% | 2% | -57% | -94% | 52 min |
| Serie C Game | ✘ | 417 | 2 | 5% | 2% | -55% | -92% | 8 min |
| Men's T20 Cricket Match | ✘ | 411 | 2 | 15% | 6% | -55% | -75% | 26 min |
| NHL Game | ✔ | 366 | 3 | 16% | 9% | -23% | -72% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Challenger WTA | ✘ | 310 | 1 | 13% | 4% | -70% | -78% | 9 min |
| NBA Game | partly | 291 | 0 | 19% | 7% | -100% | -67% | 11 min |
| AHL Game | ✘ | 284 | 0 | 4% | 2% | -100% | -93% | 6 min |
| College Hockey Game | ✘ | 265 | 0 | 1% | 0% | -100% | -99% | 16 min |
| Major League Soccer Game | partly | 227 | 1 | 11% | 5% | -59% | -81% | 8 min |
| UEFA Nations League Game | ✔ | 215 | 0 | 13% | 7% | -100% | -78% | 10 min |
| WTA Tennis Match | ✘ | 203 | 0 | 13% | 3% | -100% | -77% | 5 min |
| Japan J2 League Game | ✘ | 191 | 1 | 10% | 4% | -51% | -83% | 7 min |
| Valorant game winner | ✘ | 188 | 0 | 3% | 2% | -100% | -94% | 14 min |
| Liga DIMAYOR Game | ✘ | 181 | 1 | 10% | 3% | -48% | -83% | 8 min |
| Argentina Primera Division Game | ✘ | 179 | 2 | 16% | 8% | +4% | -72% | 9 min |
| KHL Game | ✘ | 177 | 0 | 3% | 2% | -100% | -94% | 6 min |
| Ettan Game | ✘ | 177 | 0 | 5% | 1% | -100% | -92% | 10 min |
| EFL Championship Game | ✔ | 171 | 1 | 9% | 5% | -45% | -85% | 9 min |
| English National League Game | ✘ | 169 | 1 | 7% | 5% | -45% | -88% | 11 min |
| League of Legends Game | ✘ | 165 | 0 | 7% | 2% | -100% | -87% | 12 min |
| Brasileiro Serie B Game | ✘ | 162 | 1 | 7% | 3% | -42% | -87% | 10 min |
| Argentine Nacional B Game | ✘ | 161 | 0 | 8% | 5% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 156 | 2 | 20% | 8% | +20% | -66% | 20 min |
| ATP Tennis Match | ✘ | 155 | 0 | 15% | 6% | -100% | -73% | 4 min |
| Brasileiro Serie A Game | partly | 146 | 1 | 12% | 7% | -36% | -80% | 9 min |
| EFL League One Game | ✔ | 145 | 1 | 9% | 3% | -36% | -84% | 10 min |
| Women's T20 Match | ✘ | 144 | 0 | 15% | 5% | -100% | -74% | 28 min |
| LaLiga 2 Game | partly | 137 | 1 | 17% | 7% | -32% | -71% | 8 min |
| Overwatch Game | ✘ | 133 | 0 | 2% | 1% | -100% | -96% | 6 min |
| Japan J League Game | ✘ | 133 | 1 | 17% | 6% | -30% | -71% | 11 min |
| Liiga Game | ✘ | 131 | 0 | 0% | 0% | -100% | -100% | 6 min |
| German 3. Liga Game | ✘ | 127 | 0 | 10% | 4% | -100% | -82% | 11 min |
| Serie B Game | ✘ | 127 | 0 | 11% | 6% | -100% | -81% | 10 min |
| Liga MX Game | ✔ | 124 | 0 | 14% | 7% | -100% | -76% | 6 min |
| Eerste Divisie Game | ✘ | 123 | 0 | 8% | 4% | -100% | -86% | 12 min |
| R6 Game | ✘ | 121 | 1 | 10% | 4% | -23% | -83% | 8 min |
| USL Championship Game | partly | 120 | 0 | 11% | 4% | -100% | -81% | 5 min |
| Serie A Game | ✔ | 120 | 0 | 10% | 6% | -100% | -83% | 12 min |
| Japan B League Game | ✘ | 119 | 0 | 8% | 1% | -100% | -87% | 13 min |
| Peru Liga 1 Game | ✘ | 116 | 0 | 16% | 7% | -100% | -73% | 14 min |
| Tweede Divisie Game | ✘ | 110 | 0 | 2% | 1% | -100% | -97% | 8 min |
| AFCON Game Winner | ✘ | 109 | 1 | 17% | 6% | -14% | -71% | 20 min |
| EuroCup Basketball Game | ✘ | 109 | 0 | 5% | 4% | -100% | -92% | 11 min |
| UEFA Champions League Game | partly | 109 | 1 | 11% | 5% | -14% | -81% | 10 min |
| National League Game | ✘ | 107 | 1 | 1% | 1% | -13% | -98% | 6 min |
| International Friendly Game | partly | 106 | 1 | 16% | 5% | -12% | -72% | 17 min |
| English Premier League Game | ✔ | 106 | 1 | 8% | 4% | -12% | -87% | 9 min |
| TFF 1. Lig Game | ✘ | 104 | 0 | 12% | 7% | -100% | -80% | 11 min |
| Liga Expansion Game | ✘ | 103 | 0 | 7% | 3% | -100% | -88% | 13 min |
| Indonesia Super League Game | ✘ | 103 | 0 | 12% | 7% | -100% | -80% | 12 min |
| NFL Game | ✔ | 101 | 1 | 18% | 7% | -8% | -69% | 9 min |
| Slovakian 2. Liga Game | ✘ | 100 | 0 | 5% | 4% | -100% | -91% | 44 min |
| Euroleague Game | ✘ | 100 | 0 | 20% | 6% | -100% | -65% | 12 min |
| La Liga Game | ✔ | 100 | 0 | 18% | 11% | -100% | -69% | 8 min |
| ELH Game | ✘ | 99 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Men's ODI Cricket Match | ✘ | 95 | 3 | 20% | 8% | +195% | -65% | 56 min |
| Chinese Basketball Association Game  | ✘ | 95 | 0 | 8% | 2% | -100% | -85% | 10 min |
| Ligue 2 Game | ✘ | 94 | 0 | 7% | 5% | -100% | -87% | 12 min |
| Uruguay Primera Division Game | ✘ | 93 | 0 | 12% | 5% | -100% | -79% | 10 min |
| Polish Ekstraklasa Game | ✘ | 93 | 0 | 11% | 6% | -100% | -81% | 13 min |
| Italy Serie A2 Game | ✘ | 92 | 1 | 2% | 1% | +1% | -96% | 6 min |
| Bundesliga Game | ✔ | 91 | 1 | 15% | 8% | +3% | -73% | 9 min |
| Liga Leumit Game | ✘ | 90 | 0 | 4% | 3% | -100% | -92% | 18 min |
| Ligue 1 Game | ✔ | 90 | 0 | 16% | 8% | -100% | -73% | 8 min |
| China League 1 Game | ✘ | 89 | 0 | 9% | 4% | -100% | -84% | 12 min |
| SHL Game | ✘ | 89 | 0 | 3% | 2% | -100% | -94% | 6 min |
| Korea K-League 2 Game | ✘ | 88 | 0 | 11% | 6% | -100% | -80% | 10 min |
| UEFA Europa League Game | partly | 88 | 1 | 16% | 8% | +6% | -72% | 11 min |
| UEFA Conference League Game | partly | 88 | 0 | 15% | 9% | -100% | -74% | 13 min |
| Allsvenskan Game | ✘ | 87 | 1 | 13% | 8% | +7% | -78% | 12 min |
| DEL Game | ✘ | 86 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Copa Del Rey Game | ✘ | 85 | 0 | 6% | 5% | -100% | -90% | 40 min |
| Bundesliga 2 Game | ✔ | 85 | 0 | 13% | 6% | -100% | -78% | 8 min |
| Czech First League Game | ✘ | 84 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Eliteserien Game | ✘ | 84 | 0 | 12% | 4% | -100% | -79% | 16 min |
| Turkish Super Lig Game | ✘ | 84 | 0 | 19% | 5% | -100% | -67% | 16 min |
| Eredivisie Game | ✔ | 82 | 0 | 9% | 6% | -100% | -85% | 6 min |
| Ecuador Liga Pro Game | ✘ | 82 | 0 | 6% | 1% | -100% | -89% | 11 min |
| NWSL Game | ✔ | 81 | 0 | 6% | 1% | -100% | -89% | 7 min |
| APF Division de Honor Game | ✘ | 81 | 0 | 17% | 5% | -100% | -70% | 13 min |
| Mobile Legends Bang Bang Game | ✘ | 81 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Bolivia Premier Division Game | ✘ | 80 | 0 | 8% | 1% | -100% | -87% | 11 min |
| Saudi Pro League Game | ✘ | 78 | 2 | 18% | 12% | +139% | -69% | 13 min |
| FIBA Europe Cup Game | ✘ | 78 | 0 | 6% | 3% | -100% | -89% | 9 min |
| England Women's Super League Game | ✘ | 77 | 0 | 14% | 6% | -100% | -75% | 22 min |
| LNB Elite 2 Game | ✘ | 76 | 0 | 1% | 0% | -100% | -98% | 6 min |
| Brazil NBB Basketball Game | ✘ | 76 | 0 | 7% | 3% | -100% | -89% | 18 min |
| Belgian Pro League Game | ✘ | 75 | 0 | 9% | 1% | -100% | -84% | 20 min |
| Czech National Football League Game | ✘ | 74 | 0 | 14% | 8% | -100% | -77% | 10 min |
| Chile Liga de Primera Game | ✘ | 73 | 0 | 16% | 4% | -100% | -72% | 14 min |
| Thai League 1 Game | ✘ | 72 | 0 | 15% | 7% | -100% | -74% | 13 min |
| AFC Champions League Game | ✘ | 72 | 0 | 6% | 1% | -100% | -90% | 12 min |
| Serie A Femminile Game | ✘ | 71 | 1 | 7% | 4% | +31% | -88% | 14 min |
| Serbian SuperLiga Game | ✘ | 69 | 0 | 4% | 1% | -100% | -92% | 15 min |
| Finland Korisliiga Game | ✘ | 68 | 1 | 6% | 3% | +37% | -90% | 9 min |
| Korea K League Game | ✘ | 68 | 1 | 15% | 7% | +37% | -75% | 8 min |
| Scottish Premiership Game | ✘ | 68 | 0 | 9% | 1% | -100% | -85% | 11 min |
| Israeli Premier League Game | ✘ | 68 | 0 | 6% | 1% | -100% | -90% | 13 min |
| Spanish Liga F Game | ✘ | 68 | 0 | 10% | 7% | -100% | -82% | 11 min |
| LNBP Basketball Game | ✘ | 67 | 0 | 10% | 3% | -100% | -82% | 12 min |
| Liga Portugal Game | ✘ | 67 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Romanian Liga I Game | ✘ | 64 | 1 | 12% | 5% | +46% | -78% | 13 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Super League Greece Game | ✘ | 63 | 0 | 17% | 3% | -100% | -70% | 14 min |
| Taca de Portugal Game | ✘ | 63 | 0 | 16% | 5% | -100% | -72% | 14 min |
| Vietnam V-League 1 Game | ✘ | 62 | 1 | 5% | 3% | +51% | -92% | 11 min |
| Chinese Super League Game | ✘ | 62 | 1 | 11% | 6% | +51% | -80% | 19 min |
| Adriatic ABA Game | ✘ | 61 | 1 | 7% | 3% | +53% | -89% | 9 min |
| Spain Liga ACB Game | ✘ | 61 | 0 | 7% | 3% | -100% | -89% | 14 min |
| Czech NBL Game | ✘ | 59 | 0 | 3% | 2% | -100% | -94% | 15 min |
| LNB Elite Game | ✘ | 59 | 0 | 2% | 0% | -100% | -97% | 9 min |
| Venezuela Liga FUTVE game | ✘ | 58 | 0 | 19% | 12% | -100% | -67% | 8 min |
| KBO Game | ✘ | 57 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Qatar Stars League | ✘ | 57 | 0 | 14% | 7% | -100% | -76% | 10 min |
| Australia NBL Game | ✘ | 56 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Bundesliga Basketball Game | ✘ | 55 | 0 | 7% | 4% | -100% | -87% | 13 min |
| Liga Nacional de Basquetbol Game | ✘ | 55 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Champions League Women's Game | partly | 54 | 1 | 20% | 9% | +73% | -65% | 26 min |
| Italy Serie A Game | ✘ | 54 | 0 | 4% | 2% | -100% | -94% | 7 min |
| French Women's Première Ligue Game | ✘ | 54 | 0 | 11% | 7% | -100% | -81% | 14 min |
| Croatia HNL Game | ✘ | 51 | 0 | 8% | 4% | -100% | -86% | 11 min |
| Sweden SBL Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 14 min |
| Austria BSL Game | ✘ | 50 | 0 | 6% | 4% | -100% | -90% | 9 min |
| Rugby French 14 Match | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Swiss Super League Game | ✘ | 50 | 1 | 6% | 4% | +87% | -90% | 11 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| Korea KBL Game | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Danish Superliga Game | ✘ | 49 | 0 | 10% | 6% | -100% | -82% | 13 min |
| Slovenian Prva Liga Game | ✘ | 49 | 0 | 8% | 2% | -100% | -86% | 12 min |
| Australian A League Game | ✘ | 48 | 0 | 10% | 4% | -100% | -82% | 11 min |
| Indian Super League Game | ✘ | 48 | 0 | 12% | 6% | -100% | -78% | 9 min |
| Hungarian NB I Game | ✘ | 48 | 0 | 6% | 6% | -100% | -89% | 8 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Turkey BSL Game | ✘ | 45 | 0 | 2% | 2% | -100% | -96% | 10 min |
| Latvian Virsliga Game | ✘ | 45 | 0 | 16% | 7% | -100% | -73% | 22 min |
| German Women's Bundesliga Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 26 min |
| Austrian Bundesliga Game | ✘ | 44 | 0 | 7% | 5% | -100% | -88% | 14 min |
| Russia VTB United Game | ✘ | 43 | 0 | 5% | 0% | -100% | -92% | 16 min |
| BNXT League Game | ✘ | 42 | 0 | 5% | 2% | -100% | -92% | 11 min |
| Canadian Premier League | ✘ | 40 | 1 | 15% | 12% | +133% | -74% | 17 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| EFL League Two Game | ✔ | 40 | 0 | 10% | 5% | -100% | -83% | 3 min |
| Slovakia SBL Game | ✘ | 39 | 0 | 3% | 0% | -100% | -96% | 15 min |
| EFL Trophy Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 46 min |
| FIBA Champions League Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Eredivisie Vrouwen Game | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 8 min |
| UAE Pro League | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 15 min |
| England Super League Basketball Game | ✘ | 37 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Croatia Premijer Liga Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LKL Lithuania Game | ✘ | 35 | 0 | 3% | 0% | -100% | -95% | 10 min |
| Polish Hockey Game | ✘ | 34 | 0 | 3% | 3% | -100% | -95% | 7 min |
| Slovenia 1. SKL Game | ✘ | 33 | 0 | 3% | 3% | -100% | -95% | 15 min |
| Ligue Magnus Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 7 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| Singapore Premier League Game | ✘ | 31 | 0 | 13% | 3% | -100% | -78% | 18 min |
| EuroBasket (W) Game | ✘ | 31 | 0 | 10% | 0% | -100% | -83% | 11 min |
| Women's ODI Cricket Match | ✘ | 29 | 0 | 14% | 7% | -100% | -76% | 40 min |
| Slovakian Cup Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| Men's Iceland Basketball Premier League Game | ✘ | 27 | 0 | 15% | 7% | -100% | -74% | 7 min |
| Call of Duty Games | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Malaysia Super League Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 9 min |
| EuroLeague (W) Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 9 min |
| South African Premiership Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Colombia LBP Basketball Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 15 min |
| CFL Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 8 min |
| Liga Portugal 2 Game | ✘ | 20 | 0 | 15% | 10% | -100% | -74% | 16 min |
| Slovakia Niké liga Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 19 min |
| Women's Pro Basketball Game | ✔ | 18 | 0 | 22% | 6% | -100% | -61% | 6 min |
| Powerslap Match Winner | ✘ | 18 | 0 | 6% | 6% | -100% | -90% | 6 min |
| Israel Super League Game | ✘ | 18 | 0 | 6% | 6% | -100% | -90% | 10 min |
| Philippines PBA Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Bare Knuckle Fight Match | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 23 min |
| Lithuania NKL Game | ✘ | 17 | 0 | 6% | 6% | -100% | -90% | 119 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Coupe de France Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 141 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| GBL Basketball Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Australia A League Women Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Scottish Championship Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 25 min |
| RAF Match Result | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 2840 min |
| Champions League Hockey | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's Bundesliga Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Ukraine SuperLeague Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| USL Super League Women Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 7 min |
| Uruguay LUB Basketball Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 8 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| CONMEBOL Sudamericana Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Portugal LPB Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 7 min |
| Bulgaria First League Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 7 min |
| SAFF Championship Game | ✘ | 10 | 0 | 30% | 10% | -100% | -48% | 31 min |
| Poland PLK Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Scottish Women Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 8 min |
| Slovenian Cup Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 20 min |
| Japan B.League One Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 284 min |
| NBL Australia (W) Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Copa do Brasil Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 17 min |
| Ukrainian Premier League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liga MX Women Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 12 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Romania Division A Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Padel Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Mexican Pacific League | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Latvian-Estonian Basketball League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Japan J League Cup Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Belgium Challenger Pro League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Dominican Winter League (LIDOM) | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 84 min |
| China CBA (W) Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| T10 Match | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Serbia KLS Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 12 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Paraguay Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Puerto Rico BSN (W) Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Serbian Cup Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 12 min |
| Denmark Basketligaen Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 38 min |
| Womens TGL Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 51 min |
| Bosnia Division I Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 428 min |
| Korea KBL (W) Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Turkey TBL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Puerto Rican Winter League (LBPRC) | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 151 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Hungary NB I. A Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Premier League Cup Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| UEFA Women Europa Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Argentina Super Cup Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 16 min |
| Argentina Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 24 min |
| USL League One Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 12 min |
| Peru League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 87 min |
| England Women League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 109 min |
| Women's PPL Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Venezuelan Winter League (LVBP) | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 83 min |
| Sweden Superettan Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 121 min |
| France National Division 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Europe Adriatic League 2 Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Israel National League Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Italy Serie A (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 10 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 1401 | 4% | 1% | 0% | -94% |
| 5–15 min | 888 | 16% | 7% | 1% | -72% |
| 15–30 min | 632 | 25% | 12% | 0% | -57% |
| 30–60 min | 487 | 20% | 12% | 1% | -65% |
| Over 60 min | 506 | 22% | 10% | 0% | -62% |

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
| 11-22 06:35 | eSoccer Game | Rennes (Ryft) | ✘ | — | — | In play | — |
| 11-22 06:32 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-22 06:32 | Korea K League Game | Bucheon | ✘ | — | — | In play | — |
| 11-22 06:31 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-22 06:31 | eSoccer Game | FC Barcelona (Luis) | ✘ | — | — | In play | — |
| 11-22 06:31 | eSoccer Game | Getafe CF (Pedri) | ✘ | — | — | In play | — |
| 11-22 06:30 | College Hockey Game | Alaska Anchorage | ✘ | — | — | In play | — |
| 11-22 06:30 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-22 06:30 | eSoccer Game | Manchester Utd (Nicol) | ✘ | — | — | In play | — |
| 11-22 06:29 | eSoccer Game | Everton (Lucy) | ✘ | — | — | In play | — |
| 11-22 06:28 | eSoccer Game | Girona (Declan) | ✘ | — | — | In play | — |
| 11-22 06:27 | Russia Liga Pro Match | Innazarov Aleksei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:27 | ITF Women's Match | Christina Dodaj | ✘ | — | — | In play | — |
| 11-22 06:27 | Korea K-League 2 Game | Tie | ✘ | — | — | In play | — |
| 11-22 06:26 | eFootball Game | Philadelphia (Charlie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:26 | Challenger ATP  | Shogo Sanada | ✘ | — | — | In play | — |
| 11-22 06:23 | eSoccer Game | Toulouse FC (Homie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:23 | eSoccer Game | Nantes (Kovboj) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:22 | Japan J2 League Game | Vortis | ✘ | — | — | In play | — |
| 11-22 06:18 | Men's T20 Cricket Match | Mizoram | ✘ | — | — | In play | — |
| 11-22 06:17 | eSoccer Game | Getafe CF (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:17 | eSoccer Game | CA Osasuna (Declan) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:17 | eSoccer Game | RC Celta (Pedri) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:17 | eSoccer Game | Spurs (July) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:17 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:17 | College Football Game | Hawai'i | ✔ | 11:03 - 4th · HAW 0 - NEV 13 | — | In play | — |
| 11-22 06:17 | Korea K-League 2 Game | Gimhae | ✘ | — | — | In play | — |
| 11-22 06:16 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:16 | eSoccer Game | Chelsea (Ellie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-22 06:15 | eSoccer Game | Manchester Utd (Nicol) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
