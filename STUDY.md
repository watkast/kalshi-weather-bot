# 1¢ Study

*Updated Thu Oct 22, 12:34 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 32 finished bets | 3% | $9.20 | +192% | +28.75¢ | $11.60 / -$2.40 |

*Expect about **2 buys a day**, roughly **$0.26/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 67 | $3.95 | +39% |
| ESPN win probability ≥ 5%, sell at 50¢ | 32 | $1.95 | +41% |
| ESPN win probability ≥ 5%, sell at 25¢ | 32 | -$1.49 | -31% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 25100 | 1597 | 7 (0%) | 1.1% | -$141.55 (-59%) | Hold to the end: -$141.55 (-59%) |

*In play right now: 18. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 299 | 3.2% | 0.3% (1) | -62% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 299 | 1 | -69% | -74% | -75% | -72% |
| ESPN win probability ≥ 2% | 67 | 1 | +39% | -66% | -69% | -74% |
| ESPN win probability ≥ 5% | 32 | 1 | +192% | -84% | -84% | -86% |
| ESPN win probability ≥ 10% | 19 | 1 | +391% | -82% | -73% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1597 | 14% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 23485 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$141.55 | -59% |
| Sell at 2¢ | 221 | 14% | -$182.09 | -76% |
| Sell at 3¢ | 151 | 9% | -$180.66 | -75% |
| Sell at 5¢ | 103 | 6% | -$172.60 | -72% |
| Sell at 10¢ | 51 | 3% | -$172.74 | -72% |
| Sell at 25¢ | 15 | 1% | -$189.90 | -79% |
| Sell at 50¢ | 10 | 1% | -$172.05 | -72% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 10391 | 5 | 1% | 0% | -96% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| eBasketball Game | ✘ | 1043 | 1 | 0% | 0% | -91% | -90% | 2 min |
| ITF Women's Match | ✘ | 999 | 2 | 14% | 5% | -81% | -76% | 4 min |
| Russia Liga Pro Match | ✘ | 968 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Counter-Strike 2 Game | ✘ | 913 | 2 | 5% | 3% | -80% | -91% | 11 min |
| ITF Men's Match | ✘ | 910 | 1 | 13% | 6% | -90% | -78% | 5 min |
| Challenger ATP  | ✘ | 616 | 2 | 11% | 4% | -70% | -81% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 266 | 2 | 13% | 7% | -30% | -77% | 24 min |
| Darts Match | ✘ | 241 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Women's College Volleyball Match | ✘ | 209 | 2 | 6% | 3% | -11% | -89% | 74 min |
| Men's T20 Cricket Match | ✘ | 199 | 1 | 14% | 4% | -53% | -76% | 26 min |
| Dota 2 Game | ✘ | 183 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Serie C Game | ✘ | 174 | 2 | 5% | 3% | +7% | -91% | 8 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| NHL Game | ✔ | 152 | 0 | 11% | 5% | -100% | -81% | 4 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 134 | 0 | 7% | 2% | -100% | -87% | 11 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| WTA Tennis Match | ✘ | 102 | 0 | 10% | 2% | -100% | -83% | 5 min |
| Major League Soccer Game | partly | 101 | 1 | 11% | 4% | -8% | -81% | 6 min |
| AHL Game | ✘ | 101 | 0 | 3% | 2% | -100% | -95% | 5 min |
| Brasileiro Serie B Game | ✘ | 86 | 0 | 7% | 2% | -100% | -88% | 9 min |
| Argentina Primera Division Game | ✘ | 86 | 1 | 17% | 9% | +9% | -70% | 6 min |
| KHL Game | ✘ | 85 | 0 | 6% | 4% | -100% | -90% | 5 min |
| Ettan Game | ✘ | 85 | 0 | 5% | 1% | -100% | -92% | 6 min |
| Japan J2 League Game | ✘ | 80 | 0 | 15% | 6% | -100% | -74% | 7 min |
| NBA Game | ✔ | 78 | 0 | 13% | 4% | -100% | -78% | 8 min |
| Liga DIMAYOR Game | ✘ | 77 | 1 | 10% | 4% | +21% | -82% | 6 min |
| Argentine Nacional B Game | ✘ | 76 | 0 | 9% | 8% | -100% | -84% | 8 min |
| Overwatch Game | ✘ | 74 | 0 | 3% | 0% | -100% | -95% | 5 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| USL Championship Game | partly | 72 | 0 | 12% | 3% | -100% | -78% | 5 min |
| ATP Tennis Match | ✘ | 70 | 0 | 13% | 6% | -100% | -78% | 3 min |
| R6 Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 9 min |
| LaLiga 2 Game | partly | 66 | 0 | 21% | 9% | -100% | -63% | 8 min |
| Brasileiro Serie A Game | partly | 65 | 1 | 15% | 9% | +44% | -73% | 8 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Liiga Game | ✘ | 60 | 0 | 0% | 0% | -100% | -100% | 5 min |
| EuroCup Basketball Game | ✘ | 60 | 0 | 5% | 3% | -100% | -91% | 10 min |
| Japan J League Game | ✘ | 60 | 0 | 15% | 7% | -100% | -74% | 13 min |
| German 3. Liga Game | ✘ | 60 | 0 | 12% | 5% | -100% | -80% | 7 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Liga Leumit Game | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 138 min |
| EFL League One Game | ✔ | 56 | 0 | 11% | 4% | -100% | -81% | 11 min |
| Liga MX Game | ✔ | 55 | 0 | 16% | 9% | -100% | -72% | 5 min |
| National League Game | ✘ | 55 | 1 | 2% | 2% | +70% | -97% | 5 min |
| EFL Championship Game | ✔ | 55 | 0 | 9% | 5% | -100% | -84% | 8 min |
| eFootball Game | ✘ | 55 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Uruguay Primera Division Game | ✘ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| TFF 1. Lig Game | ✘ | 53 | 0 | 19% | 11% | -100% | -67% | 10 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Slovakian 2. Liga Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 100 min |
| Euroleague Game | ✘ | 50 | 0 | 26% | 10% | -100% | -55% | 14 min |
| Eerste Divisie Game | ✘ | 50 | 0 | 8% | 6% | -100% | -86% | 11 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Liga Expansion Game | ✘ | 49 | 0 | 6% | 4% | -100% | -89% | 10 min |
| LNBP Basketball Game | ✘ | 48 | 0 | 6% | 0% | -100% | -89% | 14 min |
| ELH Game | ✘ | 48 | 0 | 2% | 2% | -100% | -96% | 5 min |
| Mobile Legends Bang Bang Game | ✘ | 45 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Chinese Basketball Association Game  | ✘ | 45 | 0 | 4% | 2% | -100% | -92% | 10 min |
| DEL Game | ✘ | 44 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NFL Game | ✔ | 44 | 1 | 20% | 9% | +112% | -65% | 4 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| SHL Game | ✘ | 43 | 0 | 2% | 2% | -100% | -96% | 6 min |
| Women's T20 Match | ✘ | 43 | 0 | 19% | 9% | -100% | -68% | 27 min |
| College Hockey Game | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Indonesia Super League Game | ✘ | 42 | 0 | 12% | 5% | -100% | -79% | 9 min |
| China League 1 Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 9 min |
| Valorant game winner | ✘ | 40 | 0 | 5% | 2% | -100% | -91% | 15 min |
| La Liga Game | ✔ | 40 | 0 | 28% | 20% | -100% | -52% | 8 min |
| Italy Serie A2 Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Saudi Pro League Game | ✘ | 39 | 1 | 18% | 13% | +139% | -69% | 11 min |
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
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
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
| Bolivia Premier Division Game | ✘ | 30 | 0 | 17% | 3% | -100% | -71% | 3 min |
| APF Division de Honor Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 5 min |
| Adriatic ABA Game | ✘ | 29 | 0 | 3% | 3% | -100% | -94% | 10 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| England Women's Super League Game | ✘ | 28 | 0 | 21% | 7% | -100% | -63% | 39 min |
| Israeli Premier League Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Venezuela Liga FUTVE game | ✘ | 28 | 0 | 18% | 14% | -100% | -69% | 6 min |
| Japan B League Game | ✘ | 28 | 0 | 7% | 0% | -100% | -88% | 15 min |
| Spain Liga ACB Game | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 17 min |
| Bundesliga Game | ✔ | 27 | 1 | 15% | 11% | +246% | -74% | 5 min |
| Serbian SuperLiga Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 17 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Men's ODI Cricket Match | ✘ | 25 | 0 | 12% | 0% | -100% | -79% | 35 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| Korea K League Game | ✘ | 25 | 1 | 24% | 12% | +273% | -58% | 8 min |
| Super League Greece Game | ✘ | 25 | 0 | 24% | 8% | -100% | -58% | 13 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| Australia NBL Game | ✘ | 24 | 0 | 4% | 0% | -100% | -93% | 6 min |
| LNB Elite Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Serie A Femminile Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Italy Serie A Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Danish Superliga Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 9 min |
| Sweden SBL Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Czech NBL Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 17 min |
| Russia VTB United Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 13 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Vietnam V-League 1 Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Latvian Virsliga Game | ✘ | 21 | 0 | 14% | 5% | -100% | -75% | 17 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Faroe Islands Premier League Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 131 min |
| FIBA Europe Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 9 min |
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
| Spanish Liga F Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's Pro Basketball Game | ✔ | 15 | 0 | 20% | 7% | -100% | -65% | 6 min |
| Slovenia 1. SKL Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 19 min |
| Slovakia SBL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 21 min |
| England Super League Basketball Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 7 min |
| LKL Lithuania Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| FIBA Champions League Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Women's ODI Cricket Match | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 56 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Romanian Liga I Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Korea KBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 9 min |
| CFL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| Indian Super League Game | ✘ | 12 | 0 | 17% | 17% | -100% | -71% | 10 min |
| Qatar Stars League | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 4 min |
| German Women's Bundesliga Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 23 min |
| Austrian Bundesliga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Hungarian NB I Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Brazil NBB Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Australian A League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 4 min |
| French Women's Première Ligue Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Liga Nacional de Basquetbol Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Colombia LBP Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 20 min |
| BNXT League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| CONMEBOL Libertadores Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 12 min |
| Men's Iceland Basketball Premier League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| EuroLeague (W) Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
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
| Under 5 min | 653 | 5% | 1% | 0% | -91% |
| 5–15 min | 355 | 17% | 6% | 1% | -71% |
| 15–30 min | 240 | 28% | 15% | 1% | -52% |
| 30–60 min | 184 | 20% | 11% | 0% | -66% |
| Over 60 min | 149 | 17% | 9% | 0% | -70% |

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
| 10-22 06:32 | eSoccer Game | Toulouse FC (Mavi) | ✘ | — | — | In play | — |
| 10-22 06:32 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-22 06:30 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:29 | eSoccer Game | RCD Mallorca (Luis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:29 | Russia Liga Pro Match | Rudenko Vasiliy | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:28 | eSoccer Game | Manchester City (Annie) | ✘ | — | — | In play | — |
| 10-22 06:28 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:27 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:27 | Challenger ATP  | Fajing Sun | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:27 | eSoccer Game | Real Betis (Hazard) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:26 | eSoccer Game | Chelsea (Alicia) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:26 | eSoccer Game | Arsenal (Leyla) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:26 | ITF Women's Match | Xi Luo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:20 | Russia Liga Pro Match | Blinov Igor | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:19 | Russia Liga Pro Match | Pustoselov Vladimir | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:18 | Russia Liga Pro Match | Skoblov Anton | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:18 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:17 | eBasketball Game | New Orleans Pelicans (IceKimi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:17 | eFootball Game | Philadelphia (Joey) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:16 | eBasketball Game | Denver Nuggets (Tatum) | ✘ | — | 4¢ | ❌ Lost | -$0.15 |
| 10-22 06:16 | eSoccer Game | Rennes (Strudl) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:15 | eSoccer Game | Real Madrid (Declan) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:15 | eSoccer Game | Sevilla FC (Pedri) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:14 | eSoccer Game | Manchester City (Annie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:14 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:13 | eSoccer Game | RCD Mallorca (Luis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:13 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:13 | eSoccer Game | Arsenal (Leyla) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:13 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-22 06:12 | WTA Tennis Match | Yara Alhaqbani | ✘ | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
