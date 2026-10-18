# 1¢ Study

*Updated Sun Oct 18, 12:25 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 60 finished bets | 2% | $5.00 | +56% | +8.33¢ | -$4.50 / $9.50 |

*Expect about **3 buys a day**, roughly **$0.48/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 60 | -$2.25 | -25% |
| ESPN win probability ≥ 2%, sell at 25¢ | 60 | -$5.69 | -63% |
| ESPN win probability ≥ 2%, sell at 2¢ | 60 | -$5.88 | -65% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 19749 | 1416 | 7 (0%) | 1.1% | -$114.40 (-54%) | Hold to the end: -$114.40 (-54%) |

*In play right now: 37. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 268 | 3.3% | 0.4% (1) | -55% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 268 | 1 | -65% | -75% | -76% | -74% |
| ESPN win probability ≥ 2% | 60 | 1 | +56% | -65% | -70% | -78% |
| ESPN win probability ≥ 5% | 29 | 1 | +222% | -82% | -82% | -85% |
| ESPN win probability ≥ 10% | 18 | 1 | +419% | -81% | -71% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1416 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 18296 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$114.40 | -54% |
| Sell at 2¢ | 201 | 14% | -$160.14 | -75% |
| Sell at 3¢ | 135 | 10% | -$159.75 | -75% |
| Sell at 5¢ | 93 | 7% | -$151.95 | -72% |
| Sell at 10¢ | 49 | 3% | -$148.21 | -70% |
| Sell at 25¢ | 15 | 1% | -$162.75 | -77% |
| Sell at 50¢ | 10 | 1% | -$144.90 | -68% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 7301 | 4 | 1% | 1% | -95% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 782 | 1 | 13% | 5% | -88% | -78% | 4 min |
| eBasketball Game | ✘ | 746 | 1 | 0% | 0% | -87% | -87% | 2 min |
| Counter-Strike 2 Game | ✘ | 732 | 1 | 5% | 2% | -87% | -92% | 11 min |
| ITF Men's Match | ✘ | 715 | 1 | 12% | 6% | -87% | -79% | 5 min |
| Challenger ATP  | ✘ | 526 | 2 | 10% | 4% | -65% | -82% | 5 min |
| Russia Liga Pro Match | ✘ | 515 | 0 | 0% | 0% | -100% | -100% | 4 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 262 | 2 | 13% | 7% | -29% | -77% | 24 min |
| Darts Match | ✘ | 226 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Women's College Volleyball Match | ✘ | 191 | 2 | 7% | 3% | -2% | -88% | 80 min |
| Men's T20 Cricket Match | ✘ | 178 | 1 | 12% | 4% | -48% | -79% | 25 min |
| Dota 2 Game | ✘ | 166 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Serie C Game | ✘ | 164 | 2 | 5% | 3% | +14% | -92% | 8 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| NHL Game | ✔ | 133 | 0 | 13% | 6% | -100% | -78% | 5 min |
| League of Legends Game | ✘ | 132 | 0 | 8% | 2% | -100% | -87% | 11 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Major League Soccer Game | partly | 97 | 1 | 11% | 4% | -4% | -80% | 6 min |
| AHL Game | ✘ | 87 | 0 | 2% | 1% | -100% | -96% | 5 min |
| Ettan Game | ✘ | 85 | 0 | 5% | 1% | -100% | -92% | 6 min |
| Brasileiro Serie B Game | ✘ | 74 | 0 | 8% | 3% | -100% | -86% | 10 min |
| KHL Game | ✘ | 73 | 0 | 4% | 3% | -100% | -93% | 5 min |
| Argentina Primera Division Game | ✘ | 71 | 0 | 14% | 6% | -100% | -76% | 7 min |
| Overwatch Game | ✘ | 70 | 0 | 3% | 0% | -100% | -95% | 5 min |
| WTA Tennis Match | ✘ | 68 | 0 | 12% | 1% | -100% | -80% | 4 min |
| Argentine Nacional B Game | ✘ | 66 | 0 | 9% | 9% | -100% | -84% | 10 min |
| R6 Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 9 min |
| USL Championship Game | partly | 66 | 0 | 14% | 3% | -100% | -76% | 5 min |
| NBA Game | ✔ | 64 | 0 | 12% | 3% | -100% | -78% | 7 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Japan J2 League Game | ✘ | 60 | 0 | 15% | 7% | -100% | -74% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| LaLiga 2 Game | partly | 58 | 0 | 21% | 10% | -100% | -64% | 9 min |
| German 3. Liga Game | ✘ | 58 | 0 | 12% | 5% | -100% | -79% | 7 min |
| ATP Tennis Match | ✘ | 57 | 0 | 12% | 5% | -100% | -79% | 3 min |
| Liga DIMAYOR Game | ✘ | 55 | 1 | 13% | 4% | +70% | -78% | 7 min |
| Brasileiro Serie A Game | partly | 55 | 1 | 18% | 11% | +70% | -68% | 8 min |
| EFL Championship Game | ✔ | 53 | 0 | 8% | 4% | -100% | -87% | 8 min |
| KBO Game | ✘ | 52 | 0 | 10% | 6% | -100% | -83% | 4 min |
| Liiga Game | ✘ | 52 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Liga Leumit Game | ✘ | 50 | 0 | 2% | 2% | -100% | -97% | 64 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Euroleague Game | ✘ | 49 | 0 | 24% | 8% | -100% | -58% | 14 min |
| National League Game | ✘ | 49 | 1 | 2% | 2% | +90% | -96% | 5 min |
| Eerste Divisie Game | ✘ | 49 | 0 | 8% | 6% | -100% | -86% | 11 min |
| Uruguay Primera Division Game | ✘ | 48 | 0 | 6% | 4% | -100% | -89% | 10 min |
| Slovakian 2. Liga Game | ✘ | 48 | 0 | 6% | 6% | -100% | -89% | 100 min |
| Taca de Portugal Game | ✘ | 48 | 0 | 15% | 4% | -100% | -75% | 14 min |
| Liga Expansion Game | ✘ | 47 | 0 | 6% | 4% | -100% | -89% | 10 min |
| ELH Game | ✘ | 45 | 0 | 0% | 0% | -100% | -100% | 5 min |
| TFF 1. Lig Game | ✘ | 45 | 0 | 13% | 7% | -100% | -77% | 10 min |
| EuroCup Basketball Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 9 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| Mobile Legends Bang Bang Game | ✘ | 44 | 0 | 0% | 0% | -100% | -100% | 4 min |
| College Hockey Game | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 6 min |
| China League 1 Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 9 min |
| SHL Game | ✘ | 41 | 0 | 2% | 2% | -100% | -96% | 5 min |
| DEL Game | ✘ | 41 | 0 | 0% | 0% | -100% | -100% | 5 min |
| LNBP Basketball Game | ✘ | 40 | 0 | 8% | 0% | -100% | -87% | 16 min |
| Japan J League Game | ✘ | 40 | 0 | 15% | 5% | -100% | -74% | 13 min |
| Women's T20 Match | ✘ | 38 | 0 | 18% | 11% | -100% | -68% | 25 min |
| Chinese Basketball Association Game  | ✘ | 37 | 0 | 3% | 0% | -100% | -95% | 10 min |
| UEFA Champions League Game | partly | 37 | 1 | 14% | 5% | +152% | -77% | 12 min |
| Bundesliga 2 Game | ✔ | 36 | 0 | 14% | 6% | -100% | -76% | 8 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| Liga MX Game | ✔ | 35 | 0 | 11% | 9% | -100% | -80% | 2 min |
| EFL League One Game | ✔ | 35 | 0 | 11% | 3% | -100% | -80% | 5 min |
| Polish Ekstraklasa Game | ✘ | 35 | 0 | 11% | 3% | -100% | -80% | 9 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| Serie B Game | ✘ | 34 | 0 | 18% | 9% | -100% | -69% | 11 min |
| Ligue 2 Game | ✘ | 34 | 0 | 18% | 12% | -100% | -69% | 7 min |
| Ligue 1 Game | ✔ | 34 | 0 | 15% | 6% | -100% | -75% | 9 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Serie A Game | ✔ | 33 | 0 | 9% | 9% | -100% | -84% | 12 min |
| Valorant game winner | ✘ | 32 | 0 | 6% | 3% | -100% | -89% | 15 min |
| Peru Liga 1 Game | ✘ | 32 | 0 | 16% | 12% | -100% | -73% | 10 min |
| NFL Game | ✔ | 32 | 1 | 19% | 6% | +192% | -68% | 3 min |
| Korea K-League 2 Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 8 min |
| Indonesia Super League Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 8 min |
| Thai League 1 Game | ✘ | 32 | 0 | 22% | 9% | -100% | -62% | 8 min |
| Turkish Super Lig Game | ✘ | 32 | 0 | 19% | 0% | -100% | -68% | 14 min |
| Eredivisie Game | ✔ | 32 | 0 | 9% | 6% | -100% | -84% | 5 min |
| La Liga Game | ✔ | 32 | 0 | 31% | 22% | -100% | -46% | 6 min |
| English Premier League Game | ✔ | 32 | 0 | 12% | 6% | -100% | -78% | 12 min |
| Chinese Super League Game | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 18 min |
| Czech National Football League Game | ✘ | 31 | 0 | 10% | 10% | -100% | -83% | 9 min |
| Czech First League Game | ✘ | 31 | 0 | 16% | 0% | -100% | -72% | 9 min |
| NWSL Game | ✔ | 30 | 0 | 10% | 0% | -100% | -83% | 7 min |
| Italy Serie A2 Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Eliteserien Game | ✘ | 30 | 0 | 13% | 7% | -100% | -77% | 17 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Allsvenskan Game | ✘ | 29 | 0 | 14% | 14% | -100% | -76% | 12 min |
| Finland Korisliiga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| England Women's Super League Game | ✘ | 28 | 0 | 21% | 7% | -100% | -63% | 39 min |
| Adriatic ABA Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Bundesliga Game | ✔ | 27 | 1 | 15% | 11% | +246% | -74% | 5 min |
| Spain Liga ACB Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 16 min |
| Saudi Pro League Game | ✘ | 26 | 0 | 19% | 12% | -100% | -67% | 14 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| Korea K League Game | ✘ | 25 | 1 | 24% | 12% | +273% | -58% | 8 min |
| Serie A Femminile Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Ecuador Liga Pro Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 6 min |
| Bolivia Premier Division Game | ✘ | 24 | 0 | 12% | 0% | -100% | -78% | 5 min |
| Serbian SuperLiga Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Israeli Premier League Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 10 min |
| APF Division de Honor Game | ✘ | 23 | 0 | 9% | 0% | -100% | -85% | 5 min |
| Australia NBL Game | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 6 min |
| Men's ODI Cricket Match | ✘ | 23 | 0 | 9% | 0% | -100% | -85% | 27 min |
| LNB Elite Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Italy Serie A Game | ✘ | 23 | 0 | 4% | 4% | -100% | -92% | 6 min |
| Sweden SBL Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Czech NBL Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 17 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Vietnam V-League 1 Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Danish Superliga Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 10 min |
| Super League Greece Game | ✘ | 22 | 0 | 27% | 9% | -100% | -53% | 16 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Russia VTB United Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 13 min |
| Venezuela Liga FUTVE game | ✘ | 20 | 0 | 15% | 10% | -100% | -74% | 8 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Croatia HNL Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 16 min |
| Scottish Premiership Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 11 min |
| Slovenian Prva Liga Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Austria BSL Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 6 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Turkey BSL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Latvian Virsliga Game | ✘ | 17 | 0 | 18% | 6% | -100% | -69% | 18 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Singapore Premier League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 16 min |
| Spanish Liga F Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Slovakia SBL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Croatia Premijer Liga Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 19 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Women's Pro Basketball Game | ✔ | 14 | 0 | 21% | 7% | -100% | -63% | 6 min |
| Women's ODI Cricket Match | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 56 min |
| England Super League Basketball Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 7 min |
| LKL Lithuania Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| Egyptian Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Slovenia 1. SKL Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 15 min |
| CFL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| FIBA Europe Cup Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Japan B League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| Austrian Bundesliga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Hungarian NB I Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| Korea KBL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Australian A League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 4 min |
| Indian Super League Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 12 min |
| Qatar Stars League | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 8 min |
| Romanian Liga I Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 6 min |
| French Women's Première Ligue Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| BNXT League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| German Women's Bundesliga Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 15 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| FIBA Champions League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Men's Iceland Basketball Premier League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liga Nacional de Basquetbol Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CONMEBOL Sudamericana Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Brazil NBB Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Colombia LBP Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| Philippines PBA Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Women's Bundesliga Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Israel Super League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| GBL Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 14 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 586 | 5% | 1% | 0% | -91% |
| 5–15 min | 313 | 17% | 7% | 1% | -71% |
| 15–30 min | 199 | 31% | 17% | 2% | -47% |
| 30–60 min | 167 | 19% | 10% | 0% | -68% |
| Over 60 min | 137 | 19% | 10% | 0% | -67% |

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
| 10-18 18:25 | Russia Liga Pro Match | Abanokov Zalimgeri | ✘ | — | — | In play | — |
| 10-18 18:23 | Overwatch Game | Virtus.pro | ✘ | — | — | In play | — |
| 10-18 18:23 | eSoccer Game | Portugal (Leyla) | ✘ | — | — | In play | — |
| 10-18 18:23 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-18 18:20 | Ecuador Liga Pro Game | Manta | ✘ | — | — | In play | — |
| 10-18 18:19 | Serbian SuperLiga Game | Partizan Belgrade | ✘ | — | — | In play | — |
| 10-18 18:18 | Russia Liga Pro Match | Kutuzov Oleg | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:14 | LaLiga 2 Game | Tie | ✔ | 83' · AND 0 - GIR 2 | — | In play | — |
| 10-18 18:13 | eSoccer Game | Slavia Praha (Krocs) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:13 | eSoccer Game | Juventus (Zaroth) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:12 | eSoccer Game | Arsenal (Rooney) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:12 | eSoccer Game | Brighton (Sheerpy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:11 | eSoccer Game | France (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:11 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:09 | eSoccer Game | Fulham (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:09 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:07 | Italy Serie A2 Game | Juvi Cremona 1952 | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:06 | Russia Liga Pro Match | Iudin Anton | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:05 | Faroe Islands Premier League Game | Argir | ✘ | — | — | In play | — |
| 10-18 18:05 | Faroe Islands Premier League Game | Tie | ✘ | — | — | In play | — |
| 10-18 18:03 | Italy Serie A Game | Basket Scafati 1969 | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 18:02 | La Liga Game | Tie | ✔ | 74' · RSO 4 - MCF 2 | — | In play | — |
| 10-18 18:01 | eBasketball Game | Brooklyn Nets (James) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 17:58 | ITF Women's Match | Hiroko Kuwata | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 17:58 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 17:58 | eSoccer Game | Nantes (Gigi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 17:57 | Czech NBL Game | USK Prague | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 17:57 | eSoccer Game | Chelsea (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 17:57 | eSoccer Game | Spurs (Rooney) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 17:57 | Russia Liga Pro Match | Meteleshko Igor | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
