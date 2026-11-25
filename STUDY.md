# 1¢ Study

*Updated Tue Nov 24, 7:30 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 85 finished bets | 1% | $1.25 | +10% | +1.47¢ | $7.70 / -$6.45 |

*Expect about **2 buys a day**, roughly **$0.24/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 204 | -$2.60 | -8% |
| ESPN win probability ≥ 5%, sell at 50¢ | 85 | -$6.00 | -47% |
| ESPN win probability ≥ 5%, sell at 25¢ | 85 | -$6.13 | -48% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 74600 | 4066 | 17 (0%) | 1.1% | -$371.90 (-61%) | Hold to the end: -$371.90 (-61%) |

*In play right now: 44. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 1095 | 2.7% | 0.2% (2) | -210% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1095 | 2 | -83% | -71% | -70% | -71% |
| ESPN win probability ≥ 2% | 204 | 2 | -8% | -60% | -60% | -64% |
| ESPN win probability ≥ 5% | 85 | 1 | +10% | -82% | -85% | -85% |
| ESPN win probability ≥ 10% | 57 | 1 | +64% | -82% | -82% | -85% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 4066 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 70490 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 17 | 0% | -$371.90 | -61% |
| Sell at 2¢ | 578 | 14% | -$459.62 | -75% |
| Sell at 3¢ | 409 | 10% | -$450.39 | -74% |
| Sell at 5¢ | 274 | 7% | -$431.80 | -71% |
| Sell at 10¢ | 114 | 3% | -$460.56 | -76% |
| Sell at 25¢ | 44 | 1% | -$464.26 | -76% |
| Sell at 50¢ | 28 | 1% | -$420.90 | -69% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 35719 | 23 | 1% | 1% | -94% | -98% | 3 min |
| Russia Liga Pro Match | ✘ | 4678 | 0 | 2% | 1% | -100% | -97% | 4 min |
| eBasketball Game | ✘ | 3554 | 8 | 4% | 2% | -79% | -91% | 3 min |
| ITF Women's Match | ✘ | 2091 | 8 | 14% | 6% | -64% | -76% | 4 min |
| ITF Men's Match | ✘ | 2002 | 5 | 14% | 6% | -77% | -76% | 5 min |
| Counter-Strike 2 Game | ✘ | 1914 | 3 | 6% | 3% | -85% | -90% | 11 min |
| Challenger ATP  | ✘ | 1371 | 6 | 12% | 5% | -59% | -78% | 5 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Men's College Basketball Game | partly | 991 | 5 | 19% | 8% | -53% | -67% | 24 min |
| Women's College Basketball Game | partly | 947 | 3 | 14% | 5% | -70% | -76% | 30 min |
| eFootball Game | ✘ | 756 | 2 | 1% | 1% | -75% | -98% | 2 min |
| College Football Game | partly | 727 | 4 | 11% | 5% | -49% | -81% | 23 min |
| Darts Match | ✘ | 476 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Dota 2 Game | ✘ | 453 | 1 | 1% | 1% | -79% | -98% | 32 min |
| Women's College Volleyball Match | ✘ | 451 | 2 | 4% | 2% | -59% | -93% | 51 min |
| Men's T20 Cricket Match | ✘ | 439 | 2 | 15% | 6% | -57% | -75% | 26 min |
| Serie C Game | ✘ | 433 | 2 | 6% | 3% | -57% | -90% | 8 min |
| NHL Game | ✔ | 375 | 3 | 16% | 9% | -25% | -72% | 5 min |
| Challenger WTA | ✘ | 325 | 1 | 13% | 4% | -71% | -78% | 9 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| NBA Game | partly | 304 | 0 | 19% | 7% | -100% | -66% | 11 min |
| AHL Game | ✘ | 293 | 0 | 4% | 2% | -100% | -93% | 6 min |
| College Hockey Game | ✘ | 268 | 0 | 1% | 0% | -100% | -99% | 16 min |
| Major League Soccer Game | partly | 235 | 1 | 11% | 5% | -60% | -82% | 8 min |
| Valorant game winner | ✘ | 215 | 0 | 3% | 2% | -100% | -95% | 18 min |
| UEFA Nations League Game | ✔ | 215 | 0 | 13% | 7% | -100% | -78% | 10 min |
| WTA Tennis Match | ✘ | 203 | 0 | 13% | 3% | -100% | -77% | 5 min |
| Japan J2 League Game | ✘ | 193 | 1 | 10% | 5% | -52% | -82% | 7 min |
| Argentina Primera Division Game | ✘ | 185 | 2 | 16% | 9% | +1% | -72% | 9 min |
| KHL Game | ✘ | 184 | 0 | 3% | 2% | -100% | -94% | 6 min |
| Liga DIMAYOR Game | ✘ | 183 | 1 | 10% | 3% | -49% | -83% | 8 min |
| Ettan Game | ✘ | 177 | 0 | 5% | 1% | -100% | -92% | 10 min |
| EFL Championship Game | ✔ | 176 | 1 | 9% | 5% | -47% | -85% | 9 min |
| English National League Game | ✘ | 171 | 1 | 8% | 5% | -45% | -87% | 11 min |
| Brasileiro Serie B Game | ✘ | 166 | 1 | 7% | 3% | -44% | -87% | 10 min |
| League of Legends Game | ✘ | 165 | 0 | 7% | 2% | -100% | -87% | 12 min |
| Argentine Nacional B Game | ✘ | 163 | 0 | 8% | 5% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 156 | 2 | 20% | 8% | +20% | -66% | 20 min |
| ATP Tennis Match | ✘ | 155 | 0 | 15% | 6% | -100% | -73% | 4 min |
| Women's T20 Match | ✘ | 155 | 0 | 16% | 6% | -100% | -72% | 28 min |
| Brasileiro Serie A Game | partly | 152 | 1 | 12% | 7% | -39% | -79% | 9 min |
| LaLiga 2 Game | partly | 145 | 1 | 17% | 8% | -36% | -71% | 8 min |
| EFL League One Game | ✔ | 145 | 1 | 9% | 3% | -36% | -84% | 10 min |
| Serie B Game | ✘ | 141 | 0 | 11% | 5% | -100% | -80% | 10 min |
| Liiga Game | ✘ | 134 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Overwatch Game | ✘ | 133 | 0 | 2% | 1% | -100% | -96% | 6 min |
| Japan J League Game | ✘ | 133 | 1 | 17% | 6% | -30% | -71% | 11 min |
| German 3. Liga Game | ✘ | 133 | 0 | 10% | 4% | -100% | -83% | 11 min |
| Liga MX Game | ✔ | 128 | 0 | 14% | 8% | -100% | -76% | 6 min |
| Eerste Divisie Game | ✘ | 127 | 0 | 8% | 4% | -100% | -86% | 12 min |
| Serie A Game | ✔ | 127 | 0 | 10% | 6% | -100% | -82% | 14 min |
| R6 Game | ✘ | 121 | 1 | 10% | 4% | -23% | -83% | 8 min |
| Peru Liga 1 Game | ✘ | 120 | 0 | 15% | 7% | -100% | -74% | 14 min |
| USL Championship Game | partly | 120 | 0 | 11% | 4% | -100% | -81% | 5 min |
| Japan B League Game | ✘ | 119 | 0 | 8% | 1% | -100% | -87% | 13 min |
| UEFA Champions League Game | partly | 114 | 1 | 12% | 5% | -18% | -79% | 10 min |
| National League Game | ✘ | 113 | 1 | 1% | 1% | -17% | -98% | 6 min |
| NFL Game | ✔ | 113 | 1 | 19% | 7% | -17% | -68% | 9 min |
| ELH Game | ✘ | 112 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Tweede Divisie Game | ✘ | 110 | 0 | 2% | 1% | -100% | -97% | 8 min |
| TFF 1. Lig Game | ✘ | 110 | 0 | 11% | 6% | -100% | -81% | 11 min |
| AFCON Game Winner | ✘ | 109 | 1 | 17% | 6% | -14% | -71% | 20 min |
| EuroCup Basketball Game | ✘ | 109 | 0 | 5% | 4% | -100% | -92% | 11 min |
| English Premier League Game | ✔ | 109 | 1 | 7% | 4% | -14% | -87% | 10 min |
| Indonesia Super League Game | ✘ | 107 | 0 | 13% | 8% | -100% | -77% | 12 min |
| International Friendly Game | partly | 106 | 1 | 16% | 5% | -12% | -72% | 17 min |
| La Liga Game | ✔ | 106 | 0 | 18% | 10% | -100% | -69% | 8 min |
| Euroleague Game | ✘ | 103 | 0 | 19% | 6% | -100% | -66% | 12 min |
| Liga Expansion Game | ✘ | 103 | 0 | 7% | 3% | -100% | -88% | 13 min |
| Slovakian 2. Liga Game | ✘ | 100 | 0 | 5% | 4% | -100% | -91% | 44 min |
| Italy Serie A2 Game | ✘ | 100 | 1 | 2% | 1% | -7% | -97% | 6 min |
| Polish Ekstraklasa Game | ✘ | 99 | 0 | 11% | 6% | -100% | -81% | 12 min |
| Men's ODI Cricket Match | ✘ | 98 | 3 | 20% | 8% | +186% | -65% | 55 min |
| Korea K-League 2 Game | ✘ | 96 | 0 | 10% | 5% | -100% | -82% | 9 min |
| DEL Game | ✘ | 95 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Chinese Basketball Association Game  | ✘ | 95 | 0 | 8% | 2% | -100% | -85% | 10 min |
| Ligue 1 Game | ✔ | 95 | 1 | 16% | 8% | -2% | -73% | 8 min |
| Uruguay Primera Division Game | ✘ | 94 | 0 | 12% | 5% | -100% | -80% | 10 min |
| Ligue 2 Game | ✘ | 94 | 0 | 7% | 5% | -100% | -87% | 12 min |
| Allsvenskan Game | ✘ | 93 | 1 | 14% | 8% | +0% | -76% | 12 min |
| Bundesliga Game | ✔ | 93 | 1 | 15% | 8% | +0% | -74% | 9 min |
| SHL Game | ✘ | 91 | 0 | 3% | 2% | -100% | -94% | 6 min |
| Liga Leumit Game | ✘ | 90 | 0 | 4% | 3% | -100% | -92% | 18 min |
| Eliteserien Game | ✘ | 90 | 0 | 12% | 3% | -100% | -79% | 14 min |
| Turkish Super Lig Game | ✘ | 90 | 0 | 19% | 4% | -100% | -67% | 14 min |
| China League 1 Game | ✘ | 89 | 0 | 9% | 4% | -100% | -84% | 12 min |
| AFC Champions League Game | ✘ | 89 | 1 | 8% | 3% | +5% | -86% | 12 min |
| Czech First League Game | ✘ | 88 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Eredivisie Game | ✔ | 88 | 0 | 10% | 7% | -100% | -82% | 6 min |
| Ecuador Liga Pro Game | ✘ | 88 | 0 | 7% | 2% | -100% | -88% | 11 min |
| Bolivia Premier Division Game | ✘ | 88 | 0 | 7% | 1% | -100% | -88% | 11 min |
| UEFA Europa League Game | partly | 88 | 1 | 16% | 8% | +6% | -72% | 11 min |
| UEFA Conference League Game | partly | 88 | 0 | 15% | 9% | -100% | -74% | 13 min |
| Bundesliga 2 Game | ✔ | 87 | 0 | 13% | 6% | -100% | -78% | 8 min |
| APF Division de Honor Game | ✘ | 85 | 0 | 16% | 5% | -100% | -71% | 12 min |
| Copa Del Rey Game | ✘ | 85 | 0 | 6% | 5% | -100% | -90% | 40 min |
| NWSL Game | ✔ | 81 | 0 | 6% | 1% | -100% | -89% | 7 min |
| England Women's Super League Game | ✘ | 81 | 0 | 14% | 6% | -100% | -76% | 20 min |
| Mobile Legends Bang Bang Game | ✘ | 81 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Belgian Pro League Game | ✘ | 81 | 0 | 10% | 2% | -100% | -83% | 19 min |
| Chile Liga de Primera Game | ✘ | 79 | 0 | 15% | 4% | -100% | -74% | 13 min |
| Czech National Football League Game | ✘ | 79 | 0 | 14% | 8% | -100% | -76% | 11 min |
| Brazil NBB Basketball Game | ✘ | 79 | 0 | 6% | 3% | -100% | -89% | 18 min |
| Thai League 1 Game | ✘ | 78 | 0 | 14% | 6% | -100% | -76% | 15 min |
| Saudi Pro League Game | ✘ | 78 | 2 | 18% | 12% | +139% | -69% | 13 min |
| FIBA Europe Cup Game | ✘ | 78 | 0 | 6% | 3% | -100% | -89% | 9 min |
| Spanish Liga F Game | ✘ | 78 | 0 | 10% | 6% | -100% | -82% | 14 min |
| LNB Elite 2 Game | ✘ | 77 | 0 | 1% | 0% | -100% | -98% | 6 min |
| Serie A Femminile Game | ✘ | 77 | 1 | 8% | 4% | +21% | -86% | 15 min |
| Serbian SuperLiga Game | ✘ | 73 | 0 | 4% | 1% | -100% | -93% | 16 min |
| Super League Greece Game | ✘ | 73 | 0 | 15% | 3% | -100% | -74% | 14 min |
| Taca de Portugal Game | ✘ | 73 | 0 | 16% | 5% | -100% | -72% | 14 min |
| Korea K League Game | ✘ | 72 | 1 | 15% | 7% | +30% | -74% | 8 min |
| Romanian Liga I Game | ✘ | 70 | 1 | 13% | 4% | +33% | -78% | 13 min |
| Scottish Premiership Game | ✘ | 69 | 0 | 10% | 1% | -100% | -82% | 12 min |
| LNBP Basketball Game | ✘ | 68 | 0 | 10% | 3% | -100% | -82% | 12 min |
| Finland Korisliiga Game | ✘ | 68 | 1 | 6% | 3% | +37% | -90% | 9 min |
| Israeli Premier League Game | ✘ | 68 | 0 | 6% | 1% | -100% | -90% | 13 min |
| Adriatic ABA Game | ✘ | 67 | 1 | 6% | 3% | +39% | -90% | 9 min |
| Spain Liga ACB Game | ✘ | 67 | 0 | 6% | 3% | -100% | -90% | 14 min |
| Liga Portugal Game | ✘ | 67 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Vietnam V-League 1 Game | ✘ | 66 | 1 | 5% | 3% | +41% | -92% | 11 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Czech NBL Game | ✘ | 62 | 0 | 3% | 2% | -100% | -94% | 15 min |
| Chinese Super League Game | ✘ | 62 | 1 | 11% | 6% | +51% | -80% | 19 min |
| Egyptian Premier League Game | ✘ | 62 | 0 | 13% | 6% | -100% | -78% | 10 min |
| LNB Elite Game | ✘ | 61 | 0 | 2% | 0% | -100% | -97% | 9 min |
| Italy Serie A Game | ✘ | 60 | 0 | 3% | 2% | -100% | -94% | 7 min |
| Venezuela Liga FUTVE game | ✘ | 60 | 0 | 18% | 12% | -100% | -68% | 8 min |
| Bundesliga Basketball Game | ✘ | 59 | 0 | 7% | 3% | -100% | -88% | 13 min |
| KBO Game | ✘ | 57 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Australia NBL Game | ✘ | 57 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Qatar Stars League | ✘ | 57 | 0 | 14% | 7% | -100% | -76% | 10 min |
| Liga Nacional de Basquetbol Game | ✘ | 56 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Croatia HNL Game | ✘ | 55 | 0 | 7% | 4% | -100% | -87% | 11 min |
| Danish Superliga Game | ✘ | 55 | 0 | 9% | 5% | -100% | -84% | 13 min |
| French Women's Première Ligue Game | ✘ | 55 | 0 | 11% | 7% | -100% | -81% | 14 min |
| Champions League Women's Game | partly | 54 | 1 | 20% | 9% | +73% | -65% | 26 min |
| Swiss Super League Game | ✘ | 54 | 1 | 7% | 4% | +73% | -87% | 10 min |
| Slovenian Prva Liga Game | ✘ | 53 | 0 | 9% | 2% | -100% | -84% | 13 min |
| Sweden SBL Game | ✘ | 52 | 0 | 6% | 6% | -100% | -90% | 13 min |
| Hungarian NB I Game | ✘ | 52 | 0 | 6% | 6% | -100% | -90% | 9 min |
| Austria BSL Game | ✘ | 50 | 0 | 6% | 4% | -100% | -90% | 9 min |
| Rugby French 14 Match | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Korea KBL Game | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Indian Super League Game | ✘ | 50 | 0 | 12% | 6% | -100% | -79% | 8 min |
| German Women's Bundesliga Game | ✘ | 50 | 0 | 6% | 2% | -100% | -90% | 22 min |
| Turkey BSL Game | ✘ | 49 | 0 | 2% | 2% | -100% | -96% | 10 min |
| Eredivisie Vrouwen Game | ✘ | 48 | 0 | 4% | 4% | -100% | -93% | 8 min |
| Australian A League Game | ✘ | 48 | 0 | 10% | 4% | -100% | -82% | 11 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Austrian Bundesliga Game | ✘ | 46 | 0 | 7% | 4% | -100% | -89% | 13 min |
| Russia VTB United Game | ✘ | 45 | 0 | 4% | 0% | -100% | -92% | 16 min |
| Latvian Virsliga Game | ✘ | 45 | 0 | 16% | 7% | -100% | -73% | 22 min |
| BNXT League Game | ✘ | 42 | 0 | 5% | 2% | -100% | -92% | 11 min |
| Slovakia SBL Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 15 min |
| Canadian Premier League | ✘ | 40 | 1 | 15% | 12% | +133% | -74% | 17 min |
| England Super League Basketball Game | ✘ | 40 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| Polish Hockey Game | ✘ | 40 | 0 | 2% | 2% | -100% | -96% | 8 min |
| EFL League Two Game | ✔ | 40 | 0 | 10% | 5% | -100% | -83% | 3 min |
| EFL Trophy Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 46 min |
| FIBA Champions League Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 10 min |
| UAE Pro League | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 15 min |
| LKL Lithuania Game | ✘ | 37 | 0 | 3% | 0% | -100% | -95% | 10 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Croatia Premijer Liga Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Ligue Magnus Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Singapore Premier League Game | ✘ | 35 | 0 | 11% | 3% | -100% | -80% | 20 min |
| Slovenia 1. SKL Game | ✘ | 33 | 0 | 3% | 3% | -100% | -95% | 15 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| EuroBasket (W) Game | ✘ | 31 | 0 | 10% | 0% | -100% | -83% | 11 min |
| Slovakian Cup Game | ✘ | 30 | 0 | 7% | 3% | -100% | -88% | 16 min |
| Women's ODI Cricket Match | ✘ | 29 | 0 | 14% | 7% | -100% | -76% | 40 min |
| Men's Iceland Basketball Premier League Game | ✘ | 27 | 0 | 15% | 7% | -100% | -74% | 7 min |
| South African Premiership Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Call of Duty Games | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Malaysia Super League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 9 min |
| EuroLeague (W) Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 9 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| Lithuania NKL Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 73 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Colombia LBP Basketball Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Israel Super League Game | ✘ | 21 | 0 | 5% | 5% | -100% | -92% | 5 min |
| Slovakia Niké liga Game | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 19 min |
| CFL Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 8 min |
| Liga Portugal 2 Game | ✘ | 20 | 0 | 15% | 10% | -100% | -74% | 16 min |
| Women's Pro Basketball Game | ✔ | 18 | 0 | 22% | 6% | -100% | -61% | 6 min |
| Powerslap Match Winner | ✘ | 18 | 0 | 6% | 6% | -100% | -90% | 6 min |
| Japan B.League One Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 332 min |
| Philippines PBA Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Bare Knuckle Fight Match | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 23 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Coupe de France Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 141 min |
| GBL Basketball Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| Bulgaria First League Game | ✘ | 15 | 0 | 13% | 13% | -100% | -77% | 7 min |
| Women's Bundesliga Basketball Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Australia A League Women Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Scottish Championship Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 25 min |
| Ukraine SuperLeague Game | ✘ | 13 | 0 | 8% | 0% | -100% | -87% | 12 min |
| Poland PLK Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 14 min |
| RAF Match Result | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 2840 min |
| Champions League Hockey | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Portugal LPB Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 8 min |
| Ukrainian Premier League Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Super League Women Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 7 min |
| Uruguay LUB Basketball Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 8 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| CONMEBOL Sudamericana Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Mexican Pacific League | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 3 min |
| SAFF Championship Game | ✘ | 10 | 0 | 30% | 10% | -100% | -48% | 31 min |
| Scottish Women Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 8 min |
| Slovenian Cup Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 20 min |
| Belgium Challenger Pro League Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| NBL Australia (W) Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Serbia KLS Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 8 min |
| Copa do Brasil Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 17 min |
| Liga MX Women Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Latvian-Estonian Basketball League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 7 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Dominican Winter League (LIDOM) | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 133 min |
| Israel National League Game | ✘ | 7 | 1 | 14% | 14% | +1233% | -75% | 18 min |
| Romania Division A Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Padel Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Japan J League Cup Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Puerto Rico BSN (W) Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| T10 Match | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 18 min |
| Venezuelan Winter League (LVBP) | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 134 min |
| China CBA (W) Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Italy Serie A (W) Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Puerto Rican Winter League (LBPRC) | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 151 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Bosnia Division I Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 369 min |
| Paraguay Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Korea KBL (W) Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Serbian Cup Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 12 min |
| England Women League Cup Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 75 min |
| Turkey TBL Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 18 min |
| Denmark Basketligaen Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 38 min |
| Womens TGL Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 51 min |
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
| Women's PPL Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Sweden Superettan Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 121 min |
| France National Division 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| AFC Champions League Two Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Europe Adriatic League 2 Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Davis Cup Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 1436 | 4% | 1% | 0% | -94% |
| 5–15 min | 919 | 16% | 7% | 1% | -73% |
| 15–30 min | 647 | 24% | 12% | 0% | -58% |
| 30–60 min | 508 | 20% | 12% | 1% | -65% |
| Over 60 min | 527 | 22% | 10% | 0% | -61% |

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
| 11-25 02:29 | eSoccer Game | Manchester Utd (Strudl) | ✘ | — | — | In play | — |
| 11-25 02:29 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-25 02:29 | Men's College Basketball Game | UNC Greensboro | ✘ | — | — | In play | — |
| 11-25 02:29 | eBasketball Game | Dallas Mavericks (Clyde) | ✘ | — | — | In play | — |
| 11-25 02:29 | eBasketball Game | New Orleans Pelicans (Barry) | ✘ | — | — | In play | — |
| 11-25 02:29 | Russia Liga Pro Match | Ivanov Aleksandr | ✘ | — | — | In play | — |
| 11-25 02:28 | Dominican Winter League (LIDOM) | Leones del Escogido | ✘ | — | — | In play | — |
| 11-25 02:28 | Women's College Basketball Game | Western Kentucky | ✘ | — | — | In play | — |
| 11-25 02:27 | eSoccer Game | Montpellier (Trinity) | ✘ | — | — | In play | — |
| 11-25 02:27 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-25 02:26 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-25 02:25 | eSoccer Game | OL Lyonnes (Demi) | ✘ | — | — | In play | — |
| 11-25 02:24 | Men's College Basketball Game | Morgan St. | ✘ | — | — | In play | — |
| 11-25 02:22 | College Hockey Game | Brown | ✘ | — | — | In play | — |
| 11-25 02:21 | eFootball Game | Chicago (Lamar) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:21 | Women's College Basketball Game | Utah Valley | ✘ | — | — | In play | — |
| 11-25 02:21 | ITF Women's Match | Erika Sema | ✘ | — | — | In play | — |
| 11-25 02:20 | Challenger ATP  | Anton Shepp | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:19 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:18 | Women's College Basketball Game | Jacksonville | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:18 | eSoccer Game | Crystal Palace (Strudl) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:18 | Women's College Basketball Game | Alabama St. | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:17 | Men's College Basketball Game | Southeast Missouri St. | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:15 | Russia Liga Pro Match | Bazilevskiy Vitaliy | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:14 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:13 | eSoccer Game | Flamengo (Frost) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:13 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:13 | Challenger ATP  | Blake Ellis | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 11-25 02:13 | eSoccer Game | Olympique de Marseille (Gigi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-25 02:13 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
