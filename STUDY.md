# 1¢ Study

*Updated Thu Oct 22, 10:24 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 33 finished bets | 3% | $9.05 | +183% | +27.42¢ | $11.60 / -$2.55 |

*Expect about **2 buys a day**, roughly **$0.26/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 68 | $3.80 | +37% |
| ESPN win probability ≥ 5%, sell at 50¢ | 33 | $1.80 | +36% |
| ESPN win probability ≥ 5%, sell at 25¢ | 33 | -$1.64 | -33% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 26521 | 1670 | 7 (0%) | 1.1% | -$152.50 (-61%) | Hold to the end: -$152.50 (-61%) |

*In play right now: 17. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 304 | 3.3% | 0.3% (1) | -69% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 304 | 1 | -69% | -74% | -75% | -73% |
| ESPN win probability ≥ 2% | 68 | 1 | +37% | -67% | -69% | -75% |
| ESPN win probability ≥ 5% | 33 | 1 | +183% | -84% | -84% | -87% |
| ESPN win probability ≥ 10% | 20 | 1 | +367% | -83% | -74% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1670 | 14% | 9% | 7% | 3% | 1% | 1% |
| Unverified | 24834 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$152.50 | -61% |
| Sell at 2¢ | 230 | 14% | -$190.70 | -76% |
| Sell at 3¢ | 157 | 9% | -$189.27 | -76% |
| Sell at 5¢ | 109 | 7% | -$179.65 | -72% |
| Sell at 10¢ | 52 | 3% | -$182.38 | -73% |
| Sell at 25¢ | 15 | 1% | -$200.85 | -80% |
| Sell at 50¢ | 10 | 1% | -$183.00 | -73% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 11207 | 5 | 1% | 0% | -96% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| eBasketball Game | ✘ | 1125 | 1 | 0% | 0% | -92% | -91% | 2 min |
| Russia Liga Pro Match | ✘ | 1083 | 0 | 0% | 0% | -100% | -100% | 4 min |
| ITF Women's Match | ✘ | 1045 | 2 | 14% | 5% | -82% | -76% | 4 min |
| Counter-Strike 2 Game | ✘ | 967 | 2 | 5% | 3% | -81% | -92% | 11 min |
| ITF Men's Match | ✘ | 955 | 1 | 12% | 5% | -90% | -79% | 5 min |
| Challenger ATP  | ✘ | 627 | 2 | 11% | 4% | -70% | -82% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 269 | 2 | 13% | 7% | -31% | -77% | 23 min |
| Darts Match | ✘ | 248 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Women's College Volleyball Match | ✘ | 214 | 2 | 6% | 3% | -13% | -89% | 73 min |
| Men's T20 Cricket Match | ✘ | 209 | 1 | 15% | 5% | -55% | -74% | 26 min |
| Dota 2 Game | ✘ | 192 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Serie C Game | ✘ | 174 | 2 | 5% | 3% | +7% | -91% | 8 min |
| NHL Game | ✔ | 162 | 0 | 10% | 5% | -100% | -82% | 4 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 134 | 0 | 7% | 2% | -100% | -87% | 11 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| WTA Tennis Match | ✘ | 106 | 0 | 9% | 2% | -100% | -84% | 5 min |
| Major League Soccer Game | partly | 101 | 1 | 11% | 4% | -8% | -81% | 6 min |
| AHL Game | ✘ | 101 | 0 | 3% | 2% | -100% | -95% | 5 min |
| eFootball Game | ✘ | 100 | 0 | 0% | 0% | -100% | -100% | 2 min |
| KHL Game | ✘ | 88 | 0 | 6% | 3% | -100% | -90% | 5 min |
| Brasileiro Serie B Game | ✘ | 86 | 0 | 7% | 2% | -100% | -88% | 9 min |
| Argentina Primera Division Game | ✘ | 86 | 1 | 17% | 9% | +9% | -70% | 6 min |
| Ettan Game | ✘ | 85 | 0 | 5% | 1% | -100% | -92% | 6 min |
| Japan J2 League Game | ✘ | 80 | 0 | 15% | 6% | -100% | -74% | 7 min |
| Liga DIMAYOR Game | ✘ | 79 | 1 | 10% | 4% | +18% | -82% | 6 min |
| NBA Game | ✔ | 79 | 0 | 13% | 4% | -100% | -78% | 7 min |
| Argentine Nacional B Game | ✘ | 76 | 0 | 9% | 8% | -100% | -84% | 8 min |
| ATP Tennis Match | ✘ | 74 | 0 | 14% | 7% | -100% | -77% | 4 min |
| Overwatch Game | ✘ | 74 | 0 | 3% | 0% | -100% | -95% | 5 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| USL Championship Game | partly | 72 | 0 | 12% | 3% | -100% | -78% | 5 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| R6 Game | ✘ | 68 | 0 | 7% | 3% | -100% | -87% | 9 min |
| LaLiga 2 Game | partly | 66 | 0 | 21% | 9% | -100% | -63% | 8 min |
| Brasileiro Serie A Game | partly | 65 | 1 | 15% | 9% | +44% | -73% | 8 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Liiga Game | ✘ | 61 | 0 | 0% | 0% | -100% | -100% | 5 min |
| EuroCup Basketball Game | ✘ | 60 | 0 | 5% | 3% | -100% | -91% | 10 min |
| Japan J League Game | ✘ | 60 | 0 | 15% | 7% | -100% | -74% | 13 min |
| German 3. Liga Game | ✘ | 60 | 0 | 12% | 5% | -100% | -80% | 7 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Liga Leumit Game | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 138 min |
| Euroleague Game | ✘ | 56 | 0 | 25% | 9% | -100% | -57% | 14 min |
| EFL League One Game | ✔ | 56 | 0 | 11% | 4% | -100% | -81% | 11 min |
| Liga MX Game | ✔ | 55 | 0 | 16% | 9% | -100% | -72% | 5 min |
| National League Game | ✘ | 55 | 1 | 2% | 2% | +70% | -97% | 5 min |
| EFL Championship Game | ✔ | 55 | 0 | 9% | 5% | -100% | -84% | 8 min |
| Uruguay Primera Division Game | ✘ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| TFF 1. Lig Game | ✘ | 53 | 0 | 19% | 11% | -100% | -67% | 10 min |
| Valorant game winner | ✘ | 52 | 0 | 4% | 2% | -100% | -93% | 15 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Liga Expansion Game | ✘ | 51 | 0 | 6% | 4% | -100% | -90% | 10 min |
| LNBP Basketball Game | ✘ | 50 | 0 | 6% | 0% | -100% | -90% | 12 min |
| Slovakian 2. Liga Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 100 min |
| Eerste Divisie Game | ✘ | 50 | 0 | 8% | 6% | -100% | -86% | 11 min |
| Chinese Basketball Association Game  | ✘ | 50 | 0 | 6% | 2% | -100% | -90% | 10 min |
| ELH Game | ✘ | 49 | 0 | 2% | 2% | -100% | -96% | 5 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| SHL Game | ✘ | 49 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Indonesia Super League Game | ✘ | 48 | 0 | 12% | 6% | -100% | -78% | 9 min |
| Mobile Legends Bang Bang Game | ✘ | 47 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NFL Game | ✔ | 45 | 1 | 22% | 9% | +107% | -61% | 4 min |
| College Hockey Game | ✘ | 45 | 0 | 0% | 0% | -100% | -100% | 6 min |
| DEL Game | ✘ | 44 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| Women's T20 Match | ✘ | 43 | 0 | 19% | 9% | -100% | -68% | 27 min |
| Saudi Pro League Game | ✘ | 43 | 1 | 19% | 12% | +117% | -68% | 11 min |
| China League 1 Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 9 min |
| La Liga Game | ✔ | 40 | 0 | 28% | 20% | -100% | -52% | 8 min |
| Italy Serie A2 Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Serie A Game | ✔ | 39 | 0 | 8% | 8% | -100% | -87% | 12 min |
| Peru Liga 1 Game | ✘ | 38 | 0 | 13% | 11% | -100% | -77% | 10 min |
| LNB Elite 2 Game | ✘ | 37 | 0 | 3% | 0% | -100% | -95% | 7 min |
| Polish Ekstraklasa Game | ✘ | 37 | 0 | 11% | 3% | -100% | -81% | 9 min |
| NWSL Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 7 min |
| Bundesliga 2 Game | ✔ | 36 | 0 | 14% | 6% | -100% | -76% | 8 min |
| Serie B Game | ✘ | 36 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Eredivisie Game | ✔ | 36 | 0 | 11% | 8% | -100% | -81% | 4 min |
| Ligue 2 Game | ✘ | 36 | 0 | 17% | 11% | -100% | -71% | 7 min |
| Ligue 1 Game | ✔ | 36 | 0 | 17% | 8% | -100% | -71% | 9 min |
| Finland Korisliiga Game | ✘ | 34 | 1 | 3% | 3% | +175% | -95% | 8 min |
| Turkish Super Lig Game | ✘ | 34 | 0 | 18% | 0% | -100% | -69% | 14 min |
| English Premier League Game | ✔ | 34 | 0 | 12% | 6% | -100% | -80% | 12 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Korea K-League 2 Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 8 min |
| Thai League 1 Game | ✘ | 32 | 0 | 22% | 9% | -100% | -62% | 8 min |
| Eliteserien Game | ✘ | 32 | 0 | 12% | 6% | -100% | -78% | 16 min |
| Ecuador Liga Pro Game | ✘ | 32 | 0 | 9% | 3% | -100% | -84% | 6 min |
| Chinese Super League Game | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 18 min |
| Czech National Football League Game | ✘ | 31 | 0 | 10% | 10% | -100% | -83% | 9 min |
| Czech First League Game | ✘ | 31 | 0 | 16% | 0% | -100% | -72% | 9 min |
| Allsvenskan Game | ✘ | 31 | 0 | 13% | 13% | -100% | -78% | 12 min |
| Egyptian Premier League Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 11 min |
| Men's ODI Cricket Match | ✘ | 30 | 1 | 17% | 3% | +211% | -71% | 44 min |
| Adriatic ABA Game | ✘ | 30 | 0 | 3% | 3% | -100% | -94% | 9 min |
| Bolivia Premier Division Game | ✘ | 30 | 0 | 17% | 3% | -100% | -71% | 3 min |
| Japan B League Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 15 min |
| APF Division de Honor Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 5 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| England Women's Super League Game | ✘ | 28 | 0 | 21% | 7% | -100% | -63% | 39 min |
| Israeli Premier League Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Venezuela Liga FUTVE game | ✘ | 28 | 0 | 18% | 14% | -100% | -69% | 6 min |
| Spain Liga ACB Game | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 17 min |
| Bundesliga Game | ✔ | 27 | 1 | 15% | 11% | +246% | -74% | 5 min |
| Serbian SuperLiga Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 17 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Australia NBL Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 6 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| Korea K League Game | ✘ | 25 | 1 | 24% | 12% | +273% | -58% | 8 min |
| Super League Greece Game | ✘ | 25 | 0 | 24% | 8% | -100% | -58% | 13 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| LNB Elite Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Serie A Femminile Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Italy Serie A Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Vietnam V-League 1 Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 10 min |
| Danish Superliga Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 9 min |
| Sweden SBL Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Russia VTB United Game | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 13 min |
| Czech NBL Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 17 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| FIBA Europe Cup Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 9 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Latvian Virsliga Game | ✘ | 21 | 0 | 14% | 5% | -100% | -75% | 17 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Faroe Islands Premier League Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 131 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Turkey BSL Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Croatia HNL Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 16 min |
| Scottish Premiership Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 11 min |
| Slovenian Prva Liga Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Austria BSL Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 6 min |
| Liga Portugal Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 10 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Croatia Premijer Liga Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Singapore Premier League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 16 min |
| Qatar Stars League | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 5 min |
| Spanish Liga F Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's Pro Basketball Game | ✔ | 15 | 0 | 20% | 7% | -100% | -65% | 6 min |
| Slovenia 1. SKL Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 19 min |
| Slovakia SBL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 21 min |
| England Super League Basketball Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 7 min |
| LKL Lithuania Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| FIBA Champions League Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Brazil NBB Basketball Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Women's ODI Cricket Match | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 56 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| Korea KBL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 8 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Romanian Liga I Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| CFL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| Indian Super League Game | ✘ | 12 | 0 | 17% | 17% | -100% | -71% | 10 min |
| German Women's Bundesliga Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 23 min |
| Austrian Bundesliga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Hungarian NB I Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Men's Iceland Basketball Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 14 min |
| Australian A League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 4 min |
| French Women's Première Ligue Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Liga Nacional de Basquetbol Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Colombia LBP Basketball Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 17 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| BNXT League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| EuroLeague (W) Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 7 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Philippines PBA Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Israel Super League Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 16 min |
| Polish Hockey Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| Women's Bundesliga Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| GBL Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 14 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 676 | 5% | 1% | 0% | -91% |
| 5–15 min | 377 | 17% | 7% | 1% | -71% |
| 15–30 min | 251 | 27% | 15% | 1% | -52% |
| 30–60 min | 191 | 19% | 11% | 0% | -67% |
| Over 60 min | 158 | 17% | 9% | 0% | -70% |

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
| 10-23 04:22 | WTA Tennis Match | Hye Jin Elliott | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:20 | eSoccer Game | Spurs (Drakon) | ✘ | — | — | In play | — |
| 10-23 04:20 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-23 04:17 | eSoccer Game | Frankfurt (Fede) | ✘ | — | — | In play | — |
| 10-23 04:17 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-23 04:17 | eBasketball Game | Indiana Pacers (Lenny) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:16 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-23 04:16 | eSoccer Game | England (Trinity) | ✘ | — | — | In play | — |
| 10-23 04:16 | eBasketball Game | Denver Nuggets (Larry) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:14 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:14 | eSoccer Game | Mönchengladbach (Eder) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:14 | eFootball Game | Seattle (Justin) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:13 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:12 | eSoccer Game | Spain (Lotta) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:12 | NBA Game | Denver | ✔ | 3:31 - 4th · DEN 73 - OKC 88 | — | In play | — |
| 10-23 04:06 | LNBP Basketball Game | Lobos de Puebla | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:06 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:06 | eSoccer Game | Manchester Utd (Zaroth) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:02 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:01 | eSoccer Game | Stuttgart (Hurricane) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:01 | WTA Tennis Match | Aylara Kakabayeva | ✘ | — | — | In play | — |
| 10-23 04:00 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:00 | eSoccer Game | England (Trinity) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:00 | eSoccer Game | Frankfurt (Fede) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:00 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 04:00 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 03:59 | NHL Game | Vancouver | ✔ | 16:07 - 3rd · DET 4 - VAN 1 | — | In play | — |
| 10-23 03:58 | eSoccer Game | Portugal (Lexi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-23 03:56 | NHL Game | Carolina | ✔ | In SO · CAR 5 - EDM 5 | 0¢ | ❌ Lost | -$0.15 |
| 10-23 03:55 | WTA Tennis Match | Hana Avdal Hasan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
