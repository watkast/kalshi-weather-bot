# 1¢ Study

*Updated Wed Oct 14, 12:19 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 47 finished bets | 2% | $6.95 | +99% | +14.79¢ | -$3.45 / $10.40 |

*Expect about **3 buys a day**, roughly **$0.48/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 47 | -$0.30 | -4% |
| ESPN win probability ≥ 2%, sell at 25¢ | 47 | -$3.74 | -53% |
| ESPN win probability ≥ 2%, sell at 2¢ | 47 | -$4.71 | -67% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 13171 | 986 | 6 (1%) | 1.1% | -$63.90 (-43%) | Hold to the end: -$63.90 (-43%) |

*In play right now: 25. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 218 | 3.3% | 0.5% (1) | -40% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 218 | 1 | -57% | -75% | -75% | -74% |
| ESPN win probability ≥ 2% | 47 | 1 | +99% | -67% | -67% | -82% |
| ESPN win probability ≥ 5% | 22 | 1 | +324% | -76% | -76% | -80% |
| ESPN win probability ≥ 10% | 14 | 1 | +567% | -75% | -63% | -69% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 986 | 14% | 10% | 7% | 4% | 1% | 1% |
| Unverified | 12160 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 6 | 1% | -$63.90 | -43% |
| Sell at 2¢ | 142 | 14% | -$110.98 | -75% |
| Sell at 3¢ | 99 | 10% | -$109.29 | -74% |
| Sell at 5¢ | 68 | 7% | -$103.70 | -70% |
| Sell at 10¢ | 37 | 4% | -$99.43 | -67% |
| Sell at 25¢ | 13 | 1% | -$104.87 | -71% |
| Sell at 50¢ | 9 | 1% | -$87.15 | -59% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 4195 | 0 | 0% | 0% | -100% | -100% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 660 | 0 | 12% | 5% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 595 | 1 | 5% | 3% | -84% | -92% | 11 min |
| ITF Men's Match | ✘ | 579 | 1 | 11% | 6% | -84% | -81% | 5 min |
| Challenger ATP  | ✘ | 436 | 2 | 9% | 3% | -57% | -84% | 5 min |
| eBasketball Game | ✘ | 434 | 1 | 0% | 0% | -78% | -78% | 2 min |
| TT Star Series Match | ✘ | 268 | 1 | 2% | 2% | -65% | -97% | 4 min |
| College Football Game | partly | 190 | 2 | 13% | 6% | -2% | -78% | 31 min |
| Darts Match | ✘ | 174 | 0 | 1% | 1% | -100% | -99% | 9 min |
| Women's College Volleyball Match | ✘ | 158 | 2 | 7% | 3% | +18% | -88% | 103 min |
| Men's T20 Cricket Match | ✘ | 144 | 1 | 14% | 4% | -35% | -76% | 23 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Challenger WTA | ✘ | 134 | 0 | 13% | 5% | -100% | -77% | 8 min |
| League of Legends Game | ✘ | 127 | 0 | 7% | 2% | -100% | -88% | 11 min |
| Serie C Game | ✘ | 113 | 1 | 4% | 2% | -17% | -92% | 8 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| NHL Game | ✔ | 105 | 0 | 13% | 6% | -100% | -77% | 5 min |
| Dota 2 Game | ✘ | 101 | 0 | 2% | 2% | -100% | -97% | 29 min |
| Brasileiro Serie B Game | ✘ | 66 | 0 | 5% | 2% | -100% | -92% | 10 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| AHL Game | ✘ | 59 | 0 | 3% | 2% | -100% | -94% | 6 min |
| R6 Game | ✘ | 58 | 0 | 7% | 3% | -100% | -88% | 9 min |
| KHL Game | ✘ | 56 | 0 | 4% | 2% | -100% | -94% | 5 min |
| Overwatch Game | ✘ | 53 | 0 | 4% | 0% | -100% | -93% | 5 min |
| Ettan Game | ✘ | 53 | 0 | 8% | 2% | -100% | -87% | 5 min |
| Argentina Primera Division Game | ✘ | 53 | 0 | 15% | 6% | -100% | -74% | 8 min |
| Argentine Nacional B Game | ✘ | 51 | 0 | 10% | 10% | -100% | -83% | 10 min |
| KBO Game | ✘ | 50 | 0 | 8% | 6% | -100% | -86% | 4 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Liga DIMAYOR Game | ✘ | 47 | 1 | 11% | 4% | +99% | -82% | 6 min |
| Brasileiro Serie A Game | partly | 45 | 1 | 22% | 13% | +107% | -61% | 7 min |
| LaLiga 2 Game | partly | 44 | 0 | 16% | 7% | -100% | -72% | 8 min |
| NBA Game | ✔ | 44 | 0 | 14% | 2% | -100% | -76% | 6 min |
| USL Championship Game | partly | 41 | 0 | 12% | 2% | -100% | -79% | 6 min |
| Liga Leumit Game | ✘ | 40 | 0 | 2% | 2% | -100% | -96% | 14 min |
| Japan J2 League Game | ✘ | 40 | 0 | 12% | 2% | -100% | -78% | 8 min |
| Major League Soccer Game | partly | 39 | 1 | 18% | 5% | +139% | -69% | 6 min |
| WTA Tennis Match | ✘ | 39 | 0 | 10% | 0% | -100% | -82% | 4 min |
| Uruguay Primera Division Game | ✘ | 38 | 0 | 8% | 5% | -100% | -86% | 10 min |
| LNBP Basketball Game | ✘ | 38 | 0 | 8% | 0% | -100% | -86% | 14 min |
| ATP Tennis Match | ✘ | 38 | 0 | 11% | 5% | -100% | -82% | 3 min |
| Euroleague Game | ✘ | 37 | 0 | 22% | 3% | -100% | -63% | 14 min |
| Liiga Game | ✘ | 35 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 35 | 1 | 3% | 3% | +167% | -95% | 5 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| Slovakian 2. Liga Game | ✘ | 34 | 0 | 6% | 6% | -100% | -90% | 111 min |
| EuroCup Basketball Game | ✘ | 34 | 0 | 3% | 0% | -100% | -95% | 10 min |
| ELH Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liga Expansion Game | ✘ | 33 | 0 | 9% | 6% | -100% | -84% | 11 min |
| NFL Game | ✔ | 31 | 1 | 19% | 6% | +201% | -66% | 4 min |
| German 3. Liga Game | ✘ | 30 | 0 | 13% | 3% | -100% | -77% | 7 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Japan NPB Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 2 min |
| SHL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 5 min |
| DEL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Valorant game winner | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 16 min |
| Chinese Basketball Association Game  | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Tweede Divisie Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| China League 1 Game | ✘ | 25 | 0 | 12% | 8% | -100% | -79% | 6 min |
| EFL Championship Game | ✔ | 25 | 0 | 4% | 4% | -100% | -93% | 8 min |
| TFF 1. Lig Game | ✘ | 23 | 0 | 17% | 4% | -100% | -70% | 8 min |
| Finland Korisliiga Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Mobile Legends Bang Bang Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Peru Liga 1 Game | ✘ | 20 | 0 | 25% | 20% | -100% | -57% | 7 min |
| Italy Serie A2 Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Japan J League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 12 min |
| Russia Liga Pro Match | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liga MX Game | ✔ | 19 | 0 | 16% | 16% | -100% | -73% | 1 min |
| Professional Baseball Game | partly | 19 | 0 | 11% | 5% | -100% | -82% | 2 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Adriatic ABA Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Polish Ekstraklasa Game | ✘ | 19 | 0 | 16% | 5% | -100% | -73% | 11 min |
| Serie A Game | ✔ | 19 | 0 | 11% | 11% | -100% | -82% | 11 min |
| Sweden SBL Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Bundesliga 2 Game | ✔ | 18 | 0 | 17% | 11% | -100% | -71% | 8 min |
| Eredivisie Game | ✔ | 18 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Ligue 2 Game | ✘ | 18 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Ligue 1 Game | ✔ | 18 | 0 | 17% | 11% | -100% | -71% | 10 min |
| La Liga Game | ✔ | 18 | 0 | 44% | 33% | -100% | -23% | 9 min |
| UEFA Champions League Game | ✔ | 18 | 0 | 11% | 6% | -100% | -81% | 10 min |
| APF Division de Honor Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 5 min |
| Australia NBL Game | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 5 min |
| Men's ODI Cricket Match | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 24 min |
| Canadian Premier League | ✘ | 17 | 1 | 24% | 24% | +449% | -59% | 29 min |
| Spain Liga ACB Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 17 min |
| College Hockey Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Czech First League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 10 min |
| Czech NBL Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 11 min |
| LNB Elite Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| EFL League One Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 4 min |
| Italy Serie A Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 6 min |
| Korea K-League 2 Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 6 min |
| Indonesia Super League Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 10 min |
| Thai League 1 Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 7 min |
| Eliteserien Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 9 min |
| Turkish Super Lig Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 14 min |
| Serie B Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 15 min |
| Ecuador Liga Pro Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 6 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Chinese Super League Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 22 min |
| Czech National Football League Game | ✘ | 15 | 0 | 20% | 20% | -100% | -65% | 12 min |
| Allsvenskan Game | ✘ | 15 | 0 | 20% | 20% | -100% | -65% | 14 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| Russia VTB United Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 24 min |
| Austria BSL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Saudi Pro League Game | ✘ | 14 | 0 | 21% | 21% | -100% | -63% | 15 min |
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
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Women's T20 Match | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 20 min |
| Vietnam V-League 1 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Korea K League Game | ✘ | 12 | 0 | 42% | 17% | -100% | -28% | 14 min |
| Danish Superliga Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Serbian SuperLiga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| Croatia Premijer Liga Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Finnish Ykkosliiga Game | ✘ | 11 | 1 | 9% | 9% | +748% | -84% | 15 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| Slovenia 1. SKL Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 15 min |
| LKL Lithuania Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Croatia HNL Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 16 min |
| Bundesliga Game | ✔ | 9 | 1 | 22% | 22% | +937% | -61% | 13 min |
| Latvian Virsliga Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 10 min |
| Slovenian Prva Liga Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 14 min |
| FIBA Europe Cup Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 6 min |
| England Super League Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| CFL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Singapore Premier League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Scottish Premiership Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| FIBA Champions League Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Korea KBL Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 46 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| CONMEBOL Sudamericana Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Liga Nacional de Basquetbol Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Colombia LBP Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Champions League Hockey | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 15 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 411 | 6% | 1% | 0% | -89% |
| 5–15 min | 206 | 17% | 7% | 1% | -71% |
| 15–30 min | 143 | 31% | 17% | 1% | -47% |
| 30–60 min | 116 | 16% | 9% | 0% | -73% |
| Over 60 min | 103 | 19% | 13% | 0% | -66% |

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
| 10-14 18:18 | TT Star Series Match | Olave Alfonso | ✘ | — | — | In play | — |
| 10-14 18:17 | German 3. Liga Game | Aachen | ✘ | — | — | In play | — |
| 10-14 18:16 | TFF 1. Lig Game | Tie | ✘ | — | — | In play | — |
| 10-14 18:12 | Russia Liga Pro Match | Martyukhin Sergey Vyacheslavovich | ✘ | — | — | In play | — |
| 10-14 18:11 | eSoccer Game | England (Lucy) | ✘ | — | — | In play | — |
| 10-14 18:11 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-14 18:11 | eSoccer Game | Arsenal (Declan) | ✘ | — | — | In play | — |
| 10-14 18:11 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-14 18:09 | ITF Women's Match | Jessica Hinojosa Gomez | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 10-14 18:09 | Liiga Game | HIFK Helsinki | ✘ | — | — | In play | — |
| 10-14 18:08 | German 3. Liga Game | Großaspach | ✘ | — | — | In play | — |
| 10-14 18:08 | ITF Women's Match | Gabriela Kawano Cho | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 18:04 | ITF Men's Match | Marko Mesarovic | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-14 18:03 | FIBA Europe Cup Game | Promitheas Patras BC | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 18:00 | ITF Men's Match | Francisco Fontes Damorim | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 18:00 | Liiga Game | Lukko Rauma | ✘ | — | — | In play | — |
| 10-14 17:58 | eSoccer Game | Paris Saint-Germain (Ellie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:58 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:55 | EuroCup Basketball Game | KK Cedevita Olimpija Ljubljana | ✘ | — | — | In play | — |
| 10-14 17:55 | Russia Liga Pro Match | Chernov Artem Viacheslavovich | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:53 | ITF Men's Match | Michael Bassem Sobhy | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:53 | FIBA Europe Cup Game | BC Kalev | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:52 | ITF Men's Match | Victor Bini | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:52 | TT Star Series Match | Kargarmazraeh Salar | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:51 | Czech First League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:50 | FIBA Europe Cup Game | Nitra Blue Wings | ✘ | — | 10¢ | ❌ Lost | -$0.15 |
| 10-14 17:50 | TFF 1. Lig Game | Antalyaspor | ✘ | — | — | In play | — |
| 10-14 17:48 | Liiga Game | KalPa Kuopio | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:45 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-14 17:45 | eSoccer Game | Slavia Praha (Nairo) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
