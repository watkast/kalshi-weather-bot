# 1¢ Study

*Updated Sun Nov 22, 6:49 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 83 finished bets | 1% | $1.55 | +12% | +1.87¢ | $7.85 / -$6.30 |

*Expect about **2 buys a day**, roughly **$0.25/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 200 | -$2.00 | -7% |
| ESPN win probability ≥ 5%, sell at 50¢ | 83 | -$5.70 | -46% |
| ESPN win probability ≥ 5%, sell at 25¢ | 83 | -$5.83 | -47% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 72779 | 4021 | 17 (0%) | 1.1% | -$365.15 (-61%) | Hold to the end: -$365.15 (-61%) |

*In play right now: 28. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 1071 | 2.8% | 0.2% (2) | -212% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1071 | 2 | -83% | -71% | -70% | -72% |
| ESPN win probability ≥ 2% | 200 | 2 | -7% | -61% | -62% | -68% |
| ESPN win probability ≥ 5% | 83 | 1 | +12% | -83% | -87% | -90% |
| ESPN win probability ≥ 10% | 57 | 1 | +64% | -82% | -82% | -85% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 4021 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 68730 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 17 | 0% | -$365.15 | -61% |
| Sell at 2¢ | 571 | 14% | -$454.69 | -75% |
| Sell at 3¢ | 402 | 10% | -$446.37 | -74% |
| Sell at 5¢ | 268 | 7% | -$428.95 | -71% |
| Sell at 10¢ | 112 | 3% | -$456.43 | -76% |
| Sell at 25¢ | 43 | 1% | -$460.82 | -76% |
| Sell at 50¢ | 28 | 1% | -$414.15 | -69% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 34709 | 22 | 1% | 1% | -94% | -98% | 3 min |
| Russia Liga Pro Match | ✘ | 4531 | 0 | 2% | 1% | -100% | -97% | 4 min |
| eBasketball Game | ✘ | 3448 | 8 | 3% | 2% | -78% | -91% | 3 min |
| ITF Women's Match | ✘ | 2050 | 8 | 14% | 6% | -64% | -76% | 4 min |
| ITF Men's Match | ✘ | 1997 | 5 | 14% | 6% | -77% | -76% | 5 min |
| Counter-Strike 2 Game | ✘ | 1877 | 3 | 6% | 3% | -85% | -90% | 11 min |
| Challenger ATP  | ✘ | 1320 | 6 | 12% | 5% | -58% | -79% | 5 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Men's College Basketball Game | partly | 925 | 5 | 20% | 9% | -50% | -66% | 25 min |
| Women's College Basketball Game | partly | 907 | 2 | 14% | 5% | -79% | -76% | 30 min |
| College Football Game | partly | 727 | 4 | 11% | 5% | -49% | -81% | 23 min |
| eFootball Game | ✘ | 695 | 2 | 1% | 1% | -73% | -98% | 2 min |
| Darts Match | ✘ | 476 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Women's College Volleyball Match | ✘ | 450 | 2 | 4% | 2% | -59% | -94% | 51 min |
| Dota 2 Game | ✘ | 442 | 1 | 1% | 1% | -79% | -98% | 32 min |
| Serie C Game | ✘ | 433 | 2 | 6% | 3% | -57% | -90% | 8 min |
| Men's T20 Cricket Match | ✘ | 429 | 2 | 14% | 6% | -56% | -75% | 26 min |
| NHL Game | ✔ | 368 | 3 | 16% | 9% | -24% | -72% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Challenger WTA | ✘ | 313 | 1 | 12% | 4% | -70% | -78% | 9 min |
| NBA Game | partly | 293 | 0 | 19% | 6% | -100% | -67% | 11 min |
| AHL Game | ✘ | 290 | 0 | 4% | 2% | -100% | -93% | 6 min |
| College Hockey Game | ✘ | 267 | 0 | 1% | 0% | -100% | -99% | 16 min |
| Major League Soccer Game | partly | 231 | 1 | 11% | 5% | -60% | -81% | 8 min |
| UEFA Nations League Game | ✔ | 215 | 0 | 13% | 7% | -100% | -78% | 10 min |
| WTA Tennis Match | ✘ | 203 | 0 | 13% | 3% | -100% | -77% | 5 min |
| Valorant game winner | ✘ | 203 | 0 | 3% | 2% | -100% | -95% | 16 min |
| Japan J2 League Game | ✘ | 193 | 1 | 10% | 5% | -52% | -82% | 7 min |
| Argentina Primera Division Game | ✘ | 183 | 2 | 16% | 8% | +2% | -73% | 9 min |
| Liga DIMAYOR Game | ✘ | 181 | 1 | 10% | 3% | -48% | -83% | 8 min |
| KHL Game | ✘ | 180 | 0 | 3% | 2% | -100% | -94% | 6 min |
| Ettan Game | ✘ | 177 | 0 | 5% | 1% | -100% | -92% | 10 min |
| EFL Championship Game | ✔ | 173 | 1 | 9% | 5% | -46% | -85% | 9 min |
| English National League Game | ✘ | 169 | 1 | 7% | 5% | -45% | -88% | 11 min |
| Brasileiro Serie B Game | ✘ | 166 | 1 | 7% | 3% | -44% | -87% | 10 min |
| League of Legends Game | ✘ | 165 | 0 | 7% | 2% | -100% | -87% | 12 min |
| Argentine Nacional B Game | ✘ | 161 | 0 | 8% | 5% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 156 | 2 | 20% | 8% | +20% | -66% | 20 min |
| ATP Tennis Match | ✘ | 155 | 0 | 15% | 6% | -100% | -73% | 4 min |
| Brasileiro Serie A Game | partly | 152 | 1 | 12% | 7% | -39% | -79% | 9 min |
| Women's T20 Match | ✘ | 151 | 0 | 16% | 5% | -100% | -72% | 28 min |
| LaLiga 2 Game | partly | 145 | 1 | 17% | 8% | -36% | -71% | 8 min |
| EFL League One Game | ✔ | 145 | 1 | 9% | 3% | -36% | -84% | 10 min |
| Overwatch Game | ✘ | 133 | 0 | 2% | 1% | -100% | -96% | 6 min |
| Japan J League Game | ✘ | 133 | 1 | 17% | 6% | -30% | -71% | 11 min |
| German 3. Liga Game | ✘ | 133 | 0 | 10% | 4% | -100% | -83% | 11 min |
| Liiga Game | ✘ | 131 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Serie B Game | ✘ | 129 | 0 | 11% | 5% | -100% | -81% | 9 min |
| Liga MX Game | ✔ | 126 | 0 | 13% | 7% | -100% | -77% | 6 min |
| Serie A Game | ✔ | 126 | 0 | 10% | 6% | -100% | -82% | 13 min |
| Eerste Divisie Game | ✘ | 123 | 0 | 8% | 4% | -100% | -86% | 12 min |
| R6 Game | ✘ | 121 | 1 | 10% | 4% | -23% | -83% | 8 min |
| Peru Liga 1 Game | ✘ | 120 | 0 | 15% | 7% | -100% | -74% | 14 min |
| USL Championship Game | partly | 120 | 0 | 11% | 4% | -100% | -81% | 5 min |
| Japan B League Game | ✘ | 119 | 0 | 8% | 1% | -100% | -87% | 13 min |
| NFL Game | ✔ | 111 | 1 | 19% | 7% | -16% | -67% | 9 min |
| Tweede Divisie Game | ✘ | 110 | 0 | 2% | 1% | -100% | -97% | 8 min |
| AFCON Game Winner | ✘ | 109 | 1 | 17% | 6% | -14% | -71% | 20 min |
| EuroCup Basketball Game | ✘ | 109 | 0 | 5% | 4% | -100% | -92% | 11 min |
| UEFA Champions League Game | partly | 109 | 1 | 11% | 5% | -14% | -81% | 10 min |
| TFF 1. Lig Game | ✘ | 108 | 0 | 11% | 6% | -100% | -81% | 11 min |
| English Premier League Game | ✔ | 108 | 1 | 7% | 4% | -14% | -87% | 10 min |
| National League Game | ✘ | 107 | 1 | 1% | 1% | -13% | -98% | 6 min |
| Indonesia Super League Game | ✘ | 107 | 0 | 13% | 8% | -100% | -77% | 12 min |
| International Friendly Game | partly | 106 | 1 | 16% | 5% | -12% | -72% | 17 min |
| La Liga Game | ✔ | 106 | 0 | 18% | 10% | -100% | -69% | 8 min |
| ELH Game | ✘ | 105 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Liga Expansion Game | ✘ | 103 | 0 | 7% | 3% | -100% | -88% | 13 min |
| Slovakian 2. Liga Game | ✘ | 100 | 0 | 5% | 4% | -100% | -91% | 44 min |
| Euroleague Game | ✘ | 100 | 0 | 20% | 6% | -100% | -65% | 12 min |
| Italy Serie A2 Game | ✘ | 100 | 1 | 2% | 1% | -7% | -97% | 6 min |
| Polish Ekstraklasa Game | ✘ | 97 | 0 | 11% | 6% | -100% | -80% | 13 min |
| Men's ODI Cricket Match | ✘ | 96 | 3 | 20% | 8% | +192% | -66% | 55 min |
| Korea K-League 2 Game | ✘ | 96 | 0 | 10% | 5% | -100% | -82% | 9 min |
| Chinese Basketball Association Game  | ✘ | 95 | 0 | 8% | 2% | -100% | -85% | 10 min |
| Ligue 1 Game | ✔ | 95 | 1 | 16% | 8% | -2% | -73% | 8 min |
| Ligue 2 Game | ✘ | 94 | 0 | 7% | 5% | -100% | -87% | 12 min |
| Uruguay Primera Division Game | ✘ | 93 | 0 | 12% | 5% | -100% | -79% | 10 min |
| Bundesliga Game | ✔ | 93 | 1 | 15% | 8% | +0% | -74% | 9 min |
| Liga Leumit Game | ✘ | 90 | 0 | 4% | 3% | -100% | -92% | 18 min |
| DEL Game | ✘ | 90 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Eliteserien Game | ✘ | 90 | 0 | 12% | 3% | -100% | -79% | 14 min |
| China League 1 Game | ✘ | 89 | 0 | 9% | 4% | -100% | -84% | 12 min |
| SHL Game | ✘ | 89 | 0 | 3% | 2% | -100% | -94% | 6 min |
| Allsvenskan Game | ✘ | 89 | 1 | 12% | 8% | +5% | -79% | 12 min |
| Czech First League Game | ✘ | 88 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Turkish Super Lig Game | ✘ | 88 | 0 | 19% | 5% | -100% | -67% | 15 min |
| Eredivisie Game | ✔ | 88 | 0 | 10% | 7% | -100% | -82% | 6 min |
| Ecuador Liga Pro Game | ✘ | 88 | 0 | 7% | 2% | -100% | -88% | 11 min |
| UEFA Europa League Game | partly | 88 | 1 | 16% | 8% | +6% | -72% | 11 min |
| UEFA Conference League Game | partly | 88 | 0 | 15% | 9% | -100% | -74% | 13 min |
| Bundesliga 2 Game | ✔ | 87 | 0 | 13% | 6% | -100% | -78% | 8 min |
| Bolivia Premier Division Game | ✘ | 86 | 0 | 7% | 1% | -100% | -88% | 11 min |
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
| LNB Elite 2 Game | ✘ | 77 | 0 | 1% | 0% | -100% | -98% | 6 min |
| Serie A Femminile Game | ✘ | 77 | 1 | 8% | 4% | +21% | -86% | 15 min |
| Spanish Liga F Game | ✘ | 76 | 0 | 11% | 7% | -100% | -82% | 14 min |
| Serbian SuperLiga Game | ✘ | 73 | 0 | 4% | 1% | -100% | -93% | 16 min |
| Taca de Portugal Game | ✘ | 73 | 0 | 16% | 5% | -100% | -72% | 14 min |
| Korea K League Game | ✘ | 72 | 1 | 15% | 7% | +30% | -74% | 8 min |
| AFC Champions League Game | ✘ | 72 | 0 | 6% | 1% | -100% | -90% | 12 min |
| Super League Greece Game | ✘ | 71 | 0 | 15% | 3% | -100% | -73% | 15 min |
| Finland Korisliiga Game | ✘ | 68 | 1 | 6% | 3% | +37% | -90% | 9 min |
| Scottish Premiership Game | ✘ | 68 | 0 | 9% | 1% | -100% | -85% | 11 min |
| Israeli Premier League Game | ✘ | 68 | 0 | 6% | 1% | -100% | -90% | 13 min |
| Romanian Liga I Game | ✘ | 68 | 1 | 13% | 4% | +37% | -77% | 13 min |
| LNBP Basketball Game | ✘ | 67 | 0 | 10% | 3% | -100% | -82% | 12 min |
| Adriatic ABA Game | ✘ | 67 | 1 | 6% | 3% | +39% | -90% | 9 min |
| Spain Liga ACB Game | ✘ | 67 | 0 | 6% | 3% | -100% | -90% | 14 min |
| Liga Portugal Game | ✘ | 67 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Vietnam V-League 1 Game | ✘ | 66 | 1 | 5% | 3% | +41% | -92% | 11 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Czech NBL Game | ✘ | 62 | 0 | 3% | 2% | -100% | -94% | 15 min |
| Chinese Super League Game | ✘ | 62 | 1 | 11% | 6% | +51% | -80% | 19 min |
| LNB Elite Game | ✘ | 61 | 0 | 2% | 0% | -100% | -97% | 9 min |
| Italy Serie A Game | ✘ | 60 | 0 | 3% | 2% | -100% | -94% | 7 min |
| Venezuela Liga FUTVE game | ✘ | 60 | 0 | 18% | 12% | -100% | -68% | 8 min |
| Bundesliga Basketball Game | ✘ | 59 | 0 | 7% | 3% | -100% | -88% | 13 min |
| KBO Game | ✘ | 57 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Australia NBL Game | ✘ | 57 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Qatar Stars League | ✘ | 57 | 0 | 14% | 7% | -100% | -76% | 10 min |
| Liga Nacional de Basquetbol Game | ✘ | 56 | 0 | 2% | 0% | -100% | -97% | 7 min |
| French Women's Première Ligue Game | ✘ | 55 | 0 | 11% | 7% | -100% | -81% | 14 min |
| Champions League Women's Game | partly | 54 | 1 | 20% | 9% | +73% | -65% | 26 min |
| Swiss Super League Game | ✘ | 54 | 1 | 7% | 4% | +73% | -87% | 10 min |
| Croatia HNL Game | ✘ | 53 | 0 | 8% | 4% | -100% | -87% | 12 min |
| Danish Superliga Game | ✘ | 53 | 0 | 9% | 6% | -100% | -84% | 13 min |
| Sweden SBL Game | ✘ | 52 | 0 | 6% | 6% | -100% | -90% | 13 min |
| Hungarian NB I Game | ✘ | 52 | 0 | 6% | 6% | -100% | -90% | 9 min |
| Slovenian Prva Liga Game | ✘ | 51 | 0 | 10% | 2% | -100% | -83% | 12 min |
| Austria BSL Game | ✘ | 50 | 0 | 6% | 4% | -100% | -90% | 9 min |
| Rugby French 14 Match | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| Korea KBL Game | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Turkey BSL Game | ✘ | 49 | 0 | 2% | 2% | -100% | -96% | 10 min |
| Eredivisie Vrouwen Game | ✘ | 48 | 0 | 4% | 4% | -100% | -93% | 8 min |
| Australian A League Game | ✘ | 48 | 0 | 10% | 4% | -100% | -82% | 11 min |
| Indian Super League Game | ✘ | 48 | 0 | 12% | 6% | -100% | -78% | 9 min |
| German Women's Bundesliga Game | ✘ | 48 | 0 | 4% | 2% | -100% | -93% | 22 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Austrian Bundesliga Game | ✘ | 46 | 0 | 7% | 4% | -100% | -89% | 13 min |
| Russia VTB United Game | ✘ | 45 | 0 | 4% | 0% | -100% | -92% | 16 min |
| Latvian Virsliga Game | ✘ | 45 | 0 | 16% | 7% | -100% | -73% | 22 min |
| BNXT League Game | ✘ | 42 | 0 | 5% | 2% | -100% | -92% | 11 min |
| Slovakia SBL Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 15 min |
| Canadian Premier League | ✘ | 40 | 1 | 15% | 12% | +133% | -74% | 17 min |
| England Super League Basketball Game | ✘ | 40 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| EFL League Two Game | ✔ | 40 | 0 | 10% | 5% | -100% | -83% | 3 min |
| EFL Trophy Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 46 min |
| FIBA Champions League Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Polish Hockey Game | ✘ | 39 | 0 | 3% | 3% | -100% | -96% | 7 min |
| UAE Pro League | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 15 min |
| LKL Lithuania Game | ✘ | 37 | 0 | 3% | 0% | -100% | -95% | 10 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Croatia Premijer Liga Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Ligue Magnus Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Singapore Premier League Game | ✘ | 35 | 0 | 11% | 3% | -100% | -80% | 20 min |
| Slovenia 1. SKL Game | ✘ | 33 | 0 | 3% | 3% | -100% | -95% | 15 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| EuroBasket (W) Game | ✘ | 31 | 0 | 10% | 0% | -100% | -83% | 11 min |
| Women's ODI Cricket Match | ✘ | 29 | 0 | 14% | 7% | -100% | -76% | 40 min |
| Slovakian Cup Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| Men's Iceland Basketball Premier League Game | ✘ | 27 | 0 | 15% | 7% | -100% | -74% | 7 min |
| Call of Duty Games | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Malaysia Super League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 9 min |
| EuroLeague (W) Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 9 min |
| South African Premiership Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
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
| Lithuania NKL Game | ✘ | 17 | 0 | 6% | 6% | -100% | -90% | 119 min |
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
| SAFF Championship Game | ✘ | 10 | 0 | 30% | 10% | -100% | -48% | 31 min |
| Scottish Women Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 8 min |
| Slovenian Cup Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 20 min |
| Belgium Challenger Pro League Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| NBL Australia (W) Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Copa do Brasil Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 17 min |
| Liga MX Women Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Latvian-Estonian Basketball League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 7 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Serbia KLS Game | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 9 min |
| Romania Division A Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Padel Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Mexican Pacific League | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Japan J League Cup Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 4 min |
| T10 Match | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 18 min |
| Dominican Winter League (LIDOM) | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 84 min |
| China CBA (W) Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Puerto Rico BSN (W) Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Italy Serie A (W) Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Paraguay Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Korea KBL (W) Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Serbian Cup Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 12 min |
| England Women League Cup Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 75 min |
| Turkey TBL Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 18 min |
| Denmark Basketligaen Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 38 min |
| Womens TGL Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 51 min |
| Bosnia Division I Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 428 min |
| Venezuelan Winter League (LVBP) | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 132 min |
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
| Women's PPL Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Sweden Superettan Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 121 min |
| France National Division 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Europe Adriatic League 2 Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Israel National League Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 27 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 1424 | 4% | 1% | 0% | -94% |
| 5–15 min | 907 | 16% | 7% | 1% | -73% |
| 15–30 min | 643 | 24% | 12% | 0% | -58% |
| 30–60 min | 497 | 21% | 12% | 1% | -64% |
| Over 60 min | 521 | 22% | 10% | 0% | -61% |

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
| 11-23 01:48 | eFootball Game | Cincinnati (Speed) | ✘ | — | — | In play | — |
| 11-23 01:46 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-23 01:45 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-23 01:44 | eSoccer Game | Estudiantes (Antonio) | ✘ | — | — | In play | — |
| 11-23 01:44 | Valorant game winner | SaD Esports | ✘ | — | — | In play | — |
| 11-23 01:42 | Women's College Basketball Game | Pepperdine | ✘ | — | — | In play | — |
| 11-23 01:42 | eSoccer Game | Botafogo (Fede) | ✘ | — | — | In play | — |
| 11-23 01:39 | Major League Soccer Game | Tie | ✔ | 90'+12' · CLT 1 - CHI 1 | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:38 | Challenger ATP  | Eric Padgham | ✘ | — | — | In play | — |
| 11-23 01:38 | Russia Liga Pro Match | Krygin Nikolai | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:35 | eBasketball Game | Dallas Mavericks (Zach) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:33 | Major League Soccer Game | Chicago Fire | ✔ | 90'+6' · CLT 1 - CHI 1 | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:33 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:32 | eSoccer Game | Estudiantes (Antonio) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:32 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:32 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:31 | eSoccer Game | São Paulo (Holis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:31 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:31 | eSoccer Game | Olympique de Marseille (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:30 | eSoccer Game | Paris Saint-Germain (Adri) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:29 | Valorant game winner | Arranca Dreams | ✘ | — | — | In play | — |
| 11-23 01:26 | eFootball Game | Dallas (Walter) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:26 | Russia Liga Pro Match | Olshakov Konstantin | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 11-23 01:26 | Chile Liga de Primera Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:24 | eBasketball Game | Indiana Pacers (Kyle) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:23 | Russia Liga Pro Match | Bystrushkin Konstantin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:22 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:22 | eSoccer Game | Real Madrid (Mavi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:19 | Russia Liga Pro Match | Tarasenkov Nikolay | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-23 01:18 | eSoccer Game | Universitario (Bony) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
