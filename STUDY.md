# 1¢ Study

*Updated Sat Oct 17, 2:19 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 57 finished bets | 2% | $5.45 | +64% | +9.56¢ | -$4.20 / $9.65 |

*Expect about **3 buys a day**, roughly **$0.48/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 57 | -$1.80 | -21% |
| ESPN win probability ≥ 2%, sell at 25¢ | 57 | -$5.24 | -61% |
| ESPN win probability ≥ 2%, sell at 2¢ | 57 | -$5.43 | -64% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 18016 | 1262 | 7 (1%) | 1.1% | -$91.30 (-48%) | Hold to the end: -$91.30 (-48%) |

*In play right now: 42. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 252 | 3.3% | 0.4% (1) | -53% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 252 | 1 | -63% | -75% | -76% | -74% |
| ESPN win probability ≥ 2% | 57 | 1 | +64% | -64% | -68% | -77% |
| ESPN win probability ≥ 5% | 27 | 1 | +246% | -81% | -81% | -84% |
| ESPN win probability ≥ 10% | 17 | 1 | +449% | -80% | -69% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1262 | 14% | 10% | 7% | 4% | 1% | 1% |
| Unverified | 16712 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 1% | -$91.30 | -48% |
| Sell at 2¢ | 182 | 14% | -$141.98 | -75% |
| Sell at 3¢ | 122 | 10% | -$141.72 | -75% |
| Sell at 5¢ | 85 | 7% | -$134.05 | -71% |
| Sell at 10¢ | 46 | 4% | -$129.04 | -68% |
| Sell at 25¢ | 14 | 1% | -$142.96 | -76% |
| Sell at 50¢ | 10 | 1% | -$121.80 | -64% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 6624 | 4 | 0% | 0% | -94% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 748 | 1 | 12% | 5% | -88% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 710 | 1 | 5% | 2% | -87% | -92% | 11 min |
| ITF Men's Match | ✘ | 682 | 1 | 12% | 6% | -86% | -79% | 5 min |
| eBasketball Game | ✘ | 668 | 1 | 0% | 0% | -86% | -86% | 2 min |
| Challenger ATP  | ✘ | 491 | 2 | 10% | 3% | -62% | -83% | 5 min |
| Russia Liga Pro Match | ✘ | 376 | 0 | 0% | 0% | -100% | -100% | 4 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Darts Match | ✘ | 221 | 0 | 0% | 0% | -100% | -99% | 8 min |
| College Football Game | partly | 215 | 2 | 13% | 7% | -13% | -77% | 26 min |
| Women's College Volleyball Match | ✘ | 185 | 2 | 7% | 3% | +1% | -88% | 81 min |
| Men's T20 Cricket Match | ✘ | 172 | 1 | 13% | 4% | -46% | -78% | 24 min |
| Dota 2 Game | ✘ | 161 | 0 | 1% | 1% | -100% | -98% | 29 min |
| Challenger WTA | ✘ | 156 | 0 | 12% | 4% | -100% | -79% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Serie C Game | ✘ | 135 | 1 | 5% | 3% | -31% | -91% | 8 min |
| League of Legends Game | ✘ | 131 | 0 | 8% | 2% | -100% | -87% | 11 min |
| NHL Game | ✔ | 120 | 0 | 12% | 6% | -100% | -78% | 5 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Ettan Game | ✘ | 73 | 0 | 5% | 1% | -100% | -91% | 5 min |
| AHL Game | ✘ | 73 | 0 | 3% | 1% | -100% | -95% | 6 min |
| Brasileiro Serie B Game | ✘ | 70 | 0 | 6% | 1% | -100% | -90% | 10 min |
| Major League Soccer Game | partly | 69 | 1 | 12% | 3% | +35% | -80% | 8 min |
| KHL Game | ✘ | 68 | 0 | 3% | 1% | -100% | -95% | 5 min |
| R6 Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 9 min |
| NBA Game | ✔ | 64 | 0 | 12% | 3% | -100% | -78% | 7 min |
| Overwatch Game | ✘ | 63 | 0 | 3% | 0% | -100% | -94% | 5 min |
| Argentina Primera Division Game | ✘ | 63 | 0 | 14% | 5% | -100% | -75% | 6 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| WTA Tennis Match | ✘ | 60 | 0 | 12% | 0% | -100% | -80% | 4 min |
| Argentine Nacional B Game | ✘ | 59 | 0 | 8% | 8% | -100% | -85% | 10 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Japan J2 League Game | ✘ | 58 | 0 | 16% | 7% | -100% | -73% | 7 min |
| German 3. Liga Game | ✘ | 54 | 0 | 11% | 6% | -100% | -81% | 7 min |
| EFL Championship Game | ✔ | 53 | 0 | 8% | 4% | -100% | -87% | 8 min |
| LaLiga 2 Game | partly | 52 | 0 | 21% | 12% | -100% | -63% | 8 min |
| Liiga Game | ✘ | 52 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KBO Game | ✘ | 51 | 0 | 10% | 6% | -100% | -83% | 5 min |
| ATP Tennis Match | ✘ | 50 | 0 | 10% | 4% | -100% | -83% | 3 min |
| Liga Leumit Game | ✘ | 50 | 0 | 2% | 2% | -100% | -97% | 64 min |
| Liga DIMAYOR Game | ✘ | 49 | 1 | 12% | 4% | +90% | -79% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Euroleague Game | ✘ | 49 | 0 | 24% | 8% | -100% | -58% | 14 min |
| National League Game | ✘ | 49 | 1 | 2% | 2% | +90% | -96% | 5 min |
| Brasileiro Serie A Game | partly | 47 | 1 | 21% | 13% | +99% | -63% | 8 min |
| Slovakian 2. Liga Game | ✘ | 46 | 0 | 7% | 7% | -100% | -89% | 98 min |
| USL Championship Game | partly | 45 | 0 | 11% | 2% | -100% | -81% | 4 min |
| Eerste Divisie Game | ✘ | 45 | 0 | 9% | 7% | -100% | -85% | 11 min |
| Uruguay Primera Division Game | ✘ | 44 | 0 | 7% | 5% | -100% | -88% | 10 min |
| EuroCup Basketball Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 9 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| SHL Game | ✘ | 41 | 0 | 2% | 2% | -100% | -96% | 5 min |
| LNBP Basketball Game | ✘ | 40 | 0 | 8% | 0% | -100% | -87% | 16 min |
| ELH Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Liga Expansion Game | ✘ | 39 | 0 | 8% | 5% | -100% | -87% | 10 min |
| Mobile Legends Bang Bang Game | ✘ | 37 | 0 | 0% | 0% | -100% | -100% | 3 min |
| TFF 1. Lig Game | ✘ | 37 | 0 | 14% | 5% | -100% | -77% | 8 min |
| UEFA Champions League Game | partly | 37 | 1 | 14% | 5% | +152% | -77% | 12 min |
| Japan J League Game | ✘ | 36 | 0 | 17% | 6% | -100% | -71% | 13 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| China League 1 Game | ✘ | 35 | 0 | 9% | 6% | -100% | -85% | 9 min |
| DEL Game | ✘ | 35 | 0 | 0% | 0% | -100% | -100% | 4 min |
| EFL League One Game | ✔ | 35 | 0 | 11% | 3% | -100% | -80% | 5 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| College Hockey Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Ligue 2 Game | ✘ | 34 | 0 | 18% | 12% | -100% | -69% | 7 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Chinese Basketball Association Game  | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Valorant game winner | ✘ | 32 | 0 | 6% | 3% | -100% | -89% | 15 min |
| NFL Game | ✔ | 32 | 1 | 19% | 6% | +192% | -68% | 3 min |
| Serie B Game | ✘ | 30 | 0 | 13% | 10% | -100% | -77% | 11 min |
| Women's T20 Match | ✘ | 29 | 0 | 21% | 10% | -100% | -64% | 25 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Polish Ekstraklasa Game | ✘ | 29 | 0 | 10% | 3% | -100% | -82% | 9 min |
| Finland Korisliiga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Indonesia Super League Game | ✘ | 28 | 0 | 14% | 7% | -100% | -75% | 8 min |
| Bundesliga 2 Game | ✔ | 28 | 0 | 18% | 7% | -100% | -69% | 8 min |
| Czech National Football League Game | ✘ | 27 | 0 | 11% | 11% | -100% | -81% | 10 min |
| Korea K-League 2 Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 6 min |
| Saudi Pro League Game | ✘ | 26 | 0 | 19% | 12% | -100% | -67% | 14 min |
| Turkish Super Lig Game | ✘ | 26 | 0 | 12% | 0% | -100% | -80% | 13 min |
| La Liga Game | ✔ | 26 | 0 | 35% | 23% | -100% | -40% | 4 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Liga MX Game | ✔ | 25 | 0 | 12% | 12% | -100% | -79% | 1 min |
| Chinese Super League Game | ✘ | 25 | 0 | 8% | 4% | -100% | -86% | 27 min |
| Czech First League Game | ✘ | 25 | 0 | 16% | 0% | -100% | -72% | 9 min |
| Serie A Game | ✔ | 25 | 0 | 8% | 8% | -100% | -86% | 11 min |
| NWSL Game | ✔ | 24 | 0 | 12% | 0% | -100% | -78% | 7 min |
| Peru Liga 1 Game | ✘ | 24 | 0 | 21% | 17% | -100% | -64% | 7 min |
| Thai League 1 Game | ✘ | 24 | 0 | 21% | 4% | -100% | -64% | 8 min |
| Eredivisie Game | ✔ | 24 | 0 | 8% | 4% | -100% | -86% | 4 min |
| English Premier League Game | ✔ | 24 | 0 | 17% | 8% | -100% | -71% | 9 min |
| Israeli Premier League Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Taca de Portugal Game | ✘ | 24 | 0 | 12% | 4% | -100% | -78% | 7 min |
| Canadian Premier League | ✘ | 23 | 1 | 22% | 22% | +306% | -62% | 29 min |
| Adriatic ABA Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Bundesliga Game | ✔ | 23 | 1 | 13% | 13% | +306% | -77% | 5 min |
| Sweden SBL Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Eliteserien Game | ✘ | 22 | 0 | 14% | 9% | -100% | -76% | 14 min |
| Ligue 1 Game | ✔ | 22 | 0 | 18% | 9% | -100% | -68% | 10 min |
| Australia NBL Game | ✘ | 21 | 0 | 5% | 0% | -100% | -92% | 6 min |
| Men's ODI Cricket Match | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 24 min |
| Czech NBL Game | ✘ | 21 | 0 | 5% | 0% | -100% | -92% | 16 min |
| LNB Elite Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Italy Serie A2 Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Spain Liga ACB Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 16 min |
| Ecuador Liga Pro Game | ✘ | 20 | 0 | 10% | 0% | -100% | -83% | 7 min |
| Serbian SuperLiga Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 20 min |
| APF Division de Honor Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 5 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Allsvenskan Game | ✘ | 19 | 0 | 16% | 16% | -100% | -73% | 14 min |
| Russia VTB United Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 14 min |
| Serie A Femminile Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Vietnam V-League 1 Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Bolivia Premier Division Game | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 5 min |
| Austria BSL Game | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 5 min |
| Turkey BSL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A Game | ✘ | 17 | 0 | 6% | 6% | -100% | -90% | 6 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| England Women's Super League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 39 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Super League Greece Game | ✘ | 16 | 0 | 19% | 6% | -100% | -68% | 12 min |
| Croatia Premijer Liga Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 19 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Croatia HNL Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 16 min |
| Scottish Premiership Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 11 min |
| Slovenian Prva Liga Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 6 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| Women's ODI Cricket Match | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 56 min |
| Slovakia SBL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Korea K League Game | ✘ | 14 | 0 | 36% | 14% | -100% | -38% | 14 min |
| Danish Superliga Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
| Venezuela Liga FUTVE game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 10 min |
| Egyptian Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Slovenia 1. SKL Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 15 min |
| Latvian Virsliga Game | ✘ | 13 | 0 | 23% | 8% | -100% | -60% | 18 min |
| LKL Lithuania Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Singapore Premier League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 12 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| FIBA Europe Cup Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 10 min |
| England Super League Basketball Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 8 min |
| CFL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| Australian A League Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 4 min |
| Japan B League Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 8 min |
| Malaysia Super League Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 7 min |
| UAE Pro League | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Qatar Stars League | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 16 min |
| Hungarian NB I Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Korea KBL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 9 min |
| FIBA Champions League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Men's Iceland Basketball Premier League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Indian Super League Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 3 min |
| Romanian Liga I Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| German Women's Bundesliga Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 18 min |
| Austrian Bundesliga Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Spanish Liga F Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| South African Premiership Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 2 min |
| French Women's Première Ligue Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| BNXT League Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 15 min |
| CONMEBOL Sudamericana Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Liga Nacional de Basquetbol Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Colombia LBP Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| Philippines PBA Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 10 min |
| GBL Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Women's Bundesliga Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Israel Super League Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 19 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 521 | 6% | 1% | 0% | -90% |
| 5–15 min | 277 | 16% | 6% | 1% | -72% |
| 15–30 min | 177 | 33% | 18% | 2% | -43% |
| 30–60 min | 147 | 18% | 10% | 0% | -69% |
| Over 60 min | 127 | 19% | 10% | 0% | -67% |

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
| 10-17 20:19 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-17 20:18 | eBasketball Game | Dallas Mavericks (Cade) | ✘ | — | — | In play | — |
| 10-17 20:18 | Counter-Strike 2 Game | MIBR | ✘ | — | — | In play | — |
| 10-17 20:17 | Eredivisie Game | Willem II | ✔ | 59' · WIL 1 - SPA 3 | — | In play | — |
| 10-17 20:17 | LaLiga 2 Game | Tie | ✔ | 55' · CAS 3 - LPA 0 | — | In play | — |
| 10-17 20:16 | LaLiga 2 Game | Las Palmas | ✔ | 55' · CAS 3 - LPA 0 | — | In play | — |
| 10-17 20:16 | Darts Match | Ashley Coleman | ✘ | — | — | In play | — |
| 10-17 20:15 | eSoccer Game | France (Annie) | ✘ | — | — | In play | — |
| 10-17 20:15 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-17 20:15 | eSoccer Game | Everton (Bradley) | ✘ | — | — | In play | — |
| 10-17 20:15 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-17 20:15 | BNXT League Game | Union Mons-Hainaut | ✘ | — | — | In play | — |
| 10-17 20:14 | Romanian Liga I Game | Corvinul Hunedoara 1921 | ✘ | — | — | In play | — |
| 10-17 20:14 | eSoccer Game | United States (Mia) | ✘ | — | — | In play | — |
| 10-17 20:14 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-17 20:13 | Spanish Liga F Game | Tie | ✘ | — | — | In play | — |
| 10-17 20:12 | Serie A Game | Genoa | ✔ | 69' · GEN 0 - ROMA 2 | — | In play | — |
| 10-17 20:11 | College Football Game | Morehead St. | ✘ | — | — | In play | — |
| 10-17 20:11 | BNXT League Game | Cb Liege | ✘ | — | — | In play | — |
| 10-17 20:10 | Counter-Strike 2 Game | Team Falcons | ✘ | — | — | In play | — |
| 10-17 20:09 | Italy Serie A2 Game | Montecatiniterme Basketball | ✘ | — | — | In play | — |
| 10-17 20:08 | College Football Game | Drake | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 20:07 | National League Game | HC Lugano | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 20:06 | Polish Ekstraklasa Game | Cracovia Krakow | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 20:06 | Polish Ekstraklasa Game | Legia Warszawa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 20:05 | Spanish Liga F Game | Espanyol | ✘ | — | — | In play | — |
| 10-17 20:04 | College Football Game | Butler | ✘ | — | — | In play | — |
| 10-17 20:04 | Ligue 1 Game | Troyes | ✔ | 57' · RCL 3 - TRY 1 | — | In play | — |
| 10-17 20:03 | Russia Liga Pro Match | Afanasev Ivan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-17 20:03 | National League Game | HC Davos | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
