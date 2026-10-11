# 1¢ Study

*Updated Sun Oct 11, 2:41 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 39 finished bets | 3% | $8.15 | +139% | +20.90¢ | -$2.85 / $11.00 |

*Expect about **3 buys a day**, roughly **$0.50/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 39 | $0.90 | +15% |
| ESPN win probability ≥ 2%, sell at 25¢ | 39 | -$2.54 | -43% |
| ESPN win probability ≥ 2%, sell at 3¢ | 39 | -$3.90 | -67% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 9897 | 866 | 6 (1%) | 1.1% | -$45.90 (-35%) | Hold to the end: -$45.90 (-35%) |

*In play right now: 48. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 196 | 3.1% | 0.5% (1) | -27% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 196 | 1 | -52% | -74% | -73% | -71% |
| ESPN win probability ≥ 2% | 39 | 1 | +139% | -69% | -67% | -78% |
| ESPN win probability ≥ 5% | 16 | 1 | +483% | -78% | -68% | -73% |
| ESPN win probability ≥ 10% | 10 | 1 | +833% | -65% | -48% | -57% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 866 | 15% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 8983 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 6 | 1% | -$45.90 | -35% |
| Sell at 2¢ | 126 | 15% | -$97.14 | -75% |
| Sell at 3¢ | 87 | 10% | -$95.97 | -74% |
| Sell at 5¢ | 59 | 7% | -$91.55 | -70% |
| Sell at 10¢ | 30 | 3% | -$90.60 | -70% |
| Sell at 25¢ | 12 | 1% | -$90.18 | -69% |
| Sell at 50¢ | 9 | 1% | -$69.15 | -53% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 2234 | 0 | 0% | 0% | -100% | -100% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 536 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 530 | 1 | 4% | 3% | -82% | -93% | 11 min |
| ITF Men's Match | ✘ | 455 | 1 | 9% | 5% | -79% | -84% | 5 min |
| Challenger ATP  | ✘ | 345 | 2 | 9% | 2% | -46% | -85% | 5 min |
| eBasketball Game | ✘ | 234 | 1 | 0% | 0% | -60% | -60% | 1 min |
| TT Star Series Match | ✘ | 225 | 1 | 2% | 2% | -59% | -96% | 4 min |
| College Football Game | partly | 188 | 2 | 13% | 6% | -1% | -78% | 31 min |
| Darts Match | ✘ | 164 | 0 | 1% | 1% | -100% | -99% | 9 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 120 | 0 | 7% | 2% | -100% | -88% | 11 min |
| Men's T20 Cricket Match | ✘ | 117 | 1 | 14% | 4% | -20% | -76% | 20 min |
| Women's College Volleyball Match | ✘ | 110 | 2 | 6% | 3% | +70% | -89% | 63 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Serie C Game | ✘ | 105 | 1 | 4% | 1% | -11% | -93% | 8 min |
| Challenger WTA | ✘ | 90 | 0 | 12% | 7% | -100% | -79% | 8 min |
| NHL Game | ✔ | 83 | 0 | 16% | 7% | -100% | -73% | 5 min |
| Dota 2 Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 30 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| R6 Game | ✘ | 53 | 0 | 4% | 2% | -100% | -93% | 9 min |
| Ettan Game | ✘ | 51 | 0 | 8% | 2% | -100% | -86% | 6 min |
| AHL Game | ✘ | 50 | 0 | 4% | 2% | -100% | -93% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Brasileiro Serie B Game | ✘ | 46 | 0 | 2% | 0% | -100% | -96% | 11 min |
| KHL Game | ✘ | 46 | 0 | 4% | 2% | -100% | -92% | 5 min |
| KBO Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 7 min |
| USL Championship Game | partly | 41 | 0 | 12% | 2% | -100% | -79% | 6 min |
| Argentina Primera Division Game | ✘ | 41 | 0 | 17% | 7% | -100% | -70% | 8 min |
| Overwatch Game | ✘ | 40 | 0 | 5% | 0% | -100% | -91% | 5 min |
| Japan J2 League Game | ✘ | 40 | 0 | 12% | 2% | -100% | -78% | 8 min |
| Liga DIMAYOR Game | ✘ | 39 | 1 | 10% | 3% | +139% | -82% | 6 min |
| Major League Soccer Game | partly | 37 | 1 | 16% | 5% | +152% | -72% | 6 min |
| Uruguay Primera Division Game | ✘ | 36 | 0 | 8% | 6% | -100% | -86% | 10 min |
| ATP Tennis Match | ✘ | 36 | 0 | 11% | 6% | -100% | -81% | 3 min |
| National League Game | ✘ | 35 | 1 | 3% | 3% | +167% | -95% | 5 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| Argentine Nacional B Game | ✘ | 34 | 0 | 6% | 6% | -100% | -90% | 11 min |
| Liga Leumit Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 10 min |
| LaLiga 2 Game | partly | 34 | 0 | 15% | 6% | -100% | -75% | 10 min |
| Liiga Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 5 min |
| ELH Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovakian 2. Liga Game | ✘ | 32 | 0 | 6% | 6% | -100% | -89% | 111 min |
| WTA Tennis Match | ✘ | 31 | 0 | 6% | 0% | -100% | -89% | 4 min |
| Liga Expansion Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 10 min |
| NBA Game | ✔ | 31 | 0 | 13% | 3% | -100% | -78% | 4 min |
| LNBP Basketball Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 12 min |
| FIFA Women's Game | ✘ | 30 | 0 | 10% | 7% | -100% | -83% | 43 min |
| Euroleague Game | ✘ | 29 | 0 | 21% | 3% | -100% | -64% | 14 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| EuroCup Basketball Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| SHL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 5 min |
| DEL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Brasileiro Serie A Game | partly | 28 | 0 | 18% | 11% | -100% | -69% | 4 min |
| Japan NPB Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Chinese Basketball Association Game  | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Valorant game winner | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 15 min |
| NFL Game | ✔ | 26 | 1 | 23% | 8% | +259% | -60% | 5 min |
| Tweede Divisie Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| China League 1 Game | ✘ | 25 | 0 | 12% | 8% | -100% | -79% | 6 min |
| Mobile Legends Bang Bang Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Finland Korisliiga Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Rugby French 14 Match | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Italy Serie A2 Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Japan J League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 12 min |
| German 3. Liga Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 7 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| LNB Elite 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| TFF 1. Lig Game | ✘ | 19 | 0 | 16% | 5% | -100% | -73% | 8 min |
| Adriatic ABA Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Bundesliga 2 Game | ✔ | 18 | 0 | 17% | 11% | -100% | -71% | 8 min |
| Eredivisie Game | ✔ | 18 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Professional Baseball Game | partly | 17 | 0 | 12% | 6% | -100% | -80% | 2 min |
| Spain Liga ACB Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 17 min |
| College Hockey Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Australia NBL Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 7 min |
| Czech NBL Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Peru Liga 1 Game | ✘ | 16 | 0 | 25% | 19% | -100% | -57% | 6 min |
| LNB Elite Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 12 min |
| EFL League One Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 4 min |
| Italy Serie A Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 6 min |
| Korea K-League 2 Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 6 min |
| Indonesia Super League Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 10 min |
| Thai League 1 Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 7 min |
| Serie B Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 15 min |
| Ligue 2 Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 5 min |
| Ligue 1 Game | ✔ | 16 | 0 | 19% | 12% | -100% | -68% | 12 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Chinese Super League Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 22 min |
| Polish Ekstraklasa Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 18 min |
| Czech First League Game | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 11 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| APF Division de Honor Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 5 min |
| Austria BSL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Saudi Pro League Game | ✘ | 14 | 0 | 21% | 21% | -100% | -63% | 15 min |
| Eliteserien Game | ✘ | 14 | 0 | 21% | 14% | -100% | -63% | 9 min |
| Turkish Super Lig Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 13 min |
| La Liga Game | ✔ | 14 | 0 | 43% | 29% | -100% | -26% | 19 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Liga MX Game | ✔ | 13 | 0 | 15% | 15% | -100% | -73% | 1 min |
| Sweden SBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Men's ODI Cricket Match | ✘ | 13 | 0 | 8% | 0% | -100% | -87% | 20 min |
| Canadian Premier League | ✘ | 13 | 1 | 31% | 31% | +618% | -47% | 29 min |
| Czech National Football League Game | ✘ | 13 | 0 | 15% | 15% | -100% | -73% | 12 min |
| Serie A Game | ✔ | 13 | 0 | 8% | 8% | -100% | -87% | 11 min |
| Slovakia SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Turkey BSL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Vietnam V-League 1 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Korea K League Game | ✘ | 12 | 0 | 42% | 17% | -100% | -28% | 14 min |
| Ecuador Liga Pro Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Liga Portugal Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| English Premier League Game | ✔ | 12 | 0 | 8% | 8% | -100% | -86% | 4 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| Israeli Premier League Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Super League Greece Game | ✘ | 12 | 0 | 25% | 8% | -100% | -57% | 13 min |
| Women's ODI Cricket Match | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 50 min |
| Finnish Ykkosliiga Game | ✘ | 11 | 1 | 9% | 9% | +748% | -84% | 15 min |
| Allsvenskan Game | ✘ | 11 | 0 | 27% | 27% | -100% | -53% | 14 min |
| EFL Championship Game | ✔ | 11 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Russia VTB United Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 12 min |
| Croatia Premijer Liga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Chile Liga de Primera Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 12 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Danish Superliga Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 10 min |
| Serbian SuperLiga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| LKL Lithuania Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Croatia HNL Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 16 min |
| Bundesliga Game | ✔ | 9 | 1 | 22% | 22% | +937% | -61% | 13 min |
| Slovenian Prva Liga Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 14 min |
| Slovenia 1. SKL Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 11 min |
| England Super League Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| CFL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Latvian Virsliga Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Scottish Premiership Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Bolivia Premier Division Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 5 min |
| Singapore Premier League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Venezuela Liga FUTVE game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 20 min |
| Women's T20 Match | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Egyptian Premier League Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 364 | 6% | 1% | 0% | -90% |
| 5–15 min | 173 | 18% | 6% | 2% | -69% |
| 15–30 min | 124 | 30% | 16% | 2% | -48% |
| 30–60 min | 111 | 16% | 10% | 0% | -72% |
| Over 60 min | 90 | 21% | 13% | 0% | -63% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 48 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-11 20:40 | Argentine Nacional B Game | Chicago | ✘ | — | — | In play | — |
| 10-11 20:38 | Serie A Game | Cagliari | ✔ | 90'+4' · JUV 1 - CAG 1 | — | In play | — |
| 10-11 20:38 | Serie A Game | Juventus | ✔ | 90'+4' · JUV 1 - CAG 1 | — | In play | — |
| 10-11 20:37 | Ligue 1 Game | Tie | ✔ | 90'+7' · OLM 1 - TRY 0 | — | In play | — |
| 10-11 20:37 | Italy Serie A2 Game | Rinascita Basket Rimini | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:32 | Argentine Nacional B Game | Guemes | ✘ | — | — | In play | — |
| 10-11 20:31 | eSoccer Game | France (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:31 | eSoccer Game | Manchester City (Antonio) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:31 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:29 | eSoccer Game | Portugal (Kate) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:29 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:28 | Ligue 1 Game | Troyes | ✔ | 88' · OLM 1 - TRY 0 | — | In play | — |
| 10-11 20:28 | Argentine Nacional B Game | Almirante Brown | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:26 | Challenger ATP  | Franco Ribero | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:20 | eSoccer Game | Benfica (Minjori) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:20 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:18 | eSoccer Game | Sunderland (Shaq) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:18 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:18 | Argentine Nacional B Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:18 | eSoccer Game | France (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:17 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:17 | eBasketball Game | Dallas Mavericks (Ray) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:16 | eSoccer Game | Everton (Sheerpy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:16 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:15 | eSoccer Game | Spain (Adri) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:14 | Argentine Nacional B Game | Moron | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:12 | Argentine Nacional B Game | San Miguel | ✘ | — | 9¢ | ❌ Lost | -$0.15 |
| 10-11 20:10 | NFL Game | Cleveland | ✔ | 0:57 - 4th · CLE 12 - NYJ 17 | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:07 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 20:07 | ITF Women's Match | Margaret Sohns | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
