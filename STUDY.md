# 1¢ Study

*Updated Sat Oct 24, 1:31 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 37 finished bets | 3% | $8.45 | +152% | +22.84¢ | $11.30 / -$2.85 |

*Expect about **2 buys a day**, roughly **$0.26/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 74 | $2.90 | +26% |
| ESPN win probability ≥ 5%, sell at 50¢ | 37 | $1.20 | +22% |
| ESPN win probability ≥ 5%, sell at 25¢ | 37 | $1.07 | +19% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 29608 | 1816 | 7 (0%) | 1.1% | -$174.40 (-64%) | Hold to the end: -$174.40 (-64%) |

*In play right now: 29. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 323 | 3.3% | 0.3% (1) | -75% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 323 | 1 | -71% | -73% | -73% | -70% |
| ESPN win probability ≥ 2% | 74 | 1 | +26% | -65% | -68% | -71% |
| ESPN win probability ≥ 5% | 37 | 1 | +152% | -77% | -79% | -77% |
| ESPN win probability ≥ 10% | 23 | 1 | +306% | -70% | -66% | -62% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1816 | 14% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 27763 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$174.40 | -64% |
| Sell at 2¢ | 247 | 14% | -$208.18 | -76% |
| Sell at 3¢ | 170 | 9% | -$206.10 | -76% |
| Sell at 5¢ | 116 | 6% | -$197.00 | -72% |
| Sell at 10¢ | 54 | 3% | -$201.66 | -74% |
| Sell at 25¢ | 16 | 1% | -$219.44 | -81% |
| Sell at 50¢ | 10 | 1% | -$204.90 | -75% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 12672 | 5 | 0% | 0% | -96% | -99% | 2 min |
| Russia Liga Pro Match | ✘ | 1319 | 0 | 0% | 0% | -100% | -100% | 4 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| eBasketball Game | ✘ | 1260 | 1 | 1% | 0% | -93% | -91% | 2 min |
| ITF Women's Match | ✘ | 1081 | 2 | 13% | 5% | -83% | -77% | 4 min |
| Counter-Strike 2 Game | ✘ | 1021 | 2 | 5% | 3% | -82% | -91% | 12 min |
| ITF Men's Match | ✘ | 983 | 1 | 12% | 5% | -91% | -79% | 5 min |
| Challenger ATP  | ✘ | 646 | 2 | 11% | 4% | -71% | -81% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 278 | 2 | 13% | 6% | -33% | -78% | 23 min |
| Darts Match | ✘ | 253 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Men's T20 Cricket Match | ✘ | 234 | 1 | 14% | 4% | -60% | -76% | 24 min |
| Women's College Volleyball Match | ✘ | 230 | 2 | 6% | 3% | -19% | -89% | 73 min |
| Dota 2 Game | ✘ | 208 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Serie C Game | ✘ | 204 | 2 | 5% | 2% | -8% | -92% | 6 min |
| eFootball Game | ✘ | 188 | 0 | 0% | 0% | -100% | -100% | 2 min |
| NHL Game | ✔ | 166 | 0 | 11% | 5% | -100% | -81% | 4 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| League of Legends Game | ✘ | 140 | 0 | 7% | 2% | -100% | -88% | 11 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| WTA Tennis Match | ✘ | 132 | 0 | 11% | 2% | -100% | -82% | 5 min |
| AHL Game | ✘ | 111 | 0 | 3% | 2% | -100% | -95% | 5 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Ettan Game | ✘ | 107 | 0 | 5% | 1% | -100% | -92% | 6 min |
| Major League Soccer Game | partly | 101 | 1 | 11% | 4% | -8% | -81% | 6 min |
| KHL Game | ✘ | 96 | 0 | 6% | 3% | -100% | -89% | 5 min |
| ATP Tennis Match | ✘ | 94 | 0 | 14% | 6% | -100% | -76% | 4 min |
| Argentina Primera Division Game | ✘ | 92 | 1 | 16% | 9% | +1% | -72% | 6 min |
| NBA Game | ✔ | 92 | 0 | 15% | 5% | -100% | -74% | 7 min |
| Brasileiro Serie B Game | ✘ | 90 | 0 | 8% | 3% | -100% | -87% | 9 min |
| Japan J2 League Game | ✘ | 84 | 0 | 14% | 6% | -100% | -75% | 7 min |
| Liga DIMAYOR Game | ✘ | 83 | 1 | 10% | 4% | +12% | -83% | 6 min |
| Overwatch Game | ✘ | 83 | 0 | 2% | 0% | -100% | -96% | 5 min |
| English National League Game | ✘ | 79 | 0 | 9% | 6% | -100% | -85% | 10 min |
| EFL League One Game | ✔ | 79 | 0 | 11% | 4% | -100% | -80% | 10 min |
| EFL Championship Game | ✔ | 78 | 0 | 9% | 5% | -100% | -84% | 9 min |
| Argentine Nacional B Game | ✘ | 76 | 0 | 9% | 8% | -100% | -84% | 8 min |
| LaLiga 2 Game | partly | 76 | 0 | 18% | 8% | -100% | -68% | 8 min |
| R6 Game | ✘ | 74 | 0 | 8% | 3% | -100% | -86% | 9 min |
| German 3. Liga Game | ✘ | 74 | 0 | 11% | 4% | -100% | -81% | 7 min |
| Liiga Game | ✘ | 73 | 0 | 0% | 0% | -100% | -100% | 5 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| Liga Leumit Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 39 min |
| USL Championship Game | partly | 72 | 0 | 12% | 3% | -100% | -78% | 5 min |
| Eerste Divisie Game | ✘ | 70 | 0 | 10% | 7% | -100% | -83% | 9 min |
| Japan J League Game | ✘ | 70 | 0 | 17% | 7% | -100% | -70% | 13 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| Brasileiro Serie A Game | partly | 67 | 1 | 15% | 9% | +39% | -74% | 8 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| National League Game | ✘ | 62 | 1 | 2% | 2% | +51% | -97% | 5 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| TFF 1. Lig Game | ✘ | 62 | 0 | 16% | 10% | -100% | -72% | 11 min |
| Valorant game winner | ✘ | 61 | 0 | 5% | 3% | -100% | -91% | 14 min |
| Slovakian 2. Liga Game | ✘ | 60 | 0 | 5% | 5% | -100% | -91% | 86 min |
| EuroCup Basketball Game | ✘ | 60 | 0 | 5% | 3% | -100% | -91% | 10 min |
| College Hockey Game | ✘ | 60 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liga MX Game | ✔ | 59 | 0 | 15% | 8% | -100% | -74% | 5 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Euroleague Game | ✘ | 59 | 0 | 25% | 8% | -100% | -56% | 14 min |
| Chinese Basketball Association Game  | ✘ | 58 | 0 | 7% | 2% | -100% | -88% | 10 min |
| Uruguay Primera Division Game | ✘ | 56 | 0 | 7% | 4% | -100% | -88% | 10 min |
| ELH Game | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 5 min |
| SHL Game | ✘ | 56 | 0 | 4% | 4% | -100% | -94% | 6 min |
| LNBP Basketball Game | ✘ | 54 | 0 | 6% | 0% | -100% | -90% | 12 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| Liga Expansion Game | ✘ | 53 | 0 | 6% | 4% | -100% | -90% | 10 min |
| Saudi Pro League Game | ✘ | 53 | 1 | 17% | 11% | +76% | -71% | 14 min |
| Mobile Legends Bang Bang Game | ✘ | 52 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Indonesia Super League Game | ✘ | 52 | 0 | 12% | 6% | -100% | -80% | 9 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| China League 1 Game | ✘ | 51 | 0 | 12% | 6% | -100% | -80% | 10 min |
| DEL Game | ✘ | 51 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Serie B Game | ✘ | 50 | 0 | 14% | 6% | -100% | -76% | 9 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Ligue 2 Game | ✘ | 48 | 0 | 12% | 8% | -100% | -78% | 7 min |
| La Liga Game | ✔ | 48 | 0 | 27% | 19% | -100% | -53% | 8 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| Polish Ekstraklasa Game | ✘ | 47 | 0 | 15% | 9% | -100% | -74% | 9 min |
| Bundesliga 2 Game | ✔ | 46 | 0 | 13% | 7% | -100% | -77% | 7 min |
| Serie A Game | ✔ | 46 | 0 | 7% | 7% | -100% | -89% | 13 min |
| NFL Game | ✔ | 45 | 1 | 22% | 9% | +107% | -61% | 4 min |
| Czech National Football League Game | ✘ | 45 | 0 | 13% | 7% | -100% | -77% | 7 min |
| LNB Elite 2 Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 7 min |
| English Premier League Game | ✔ | 44 | 0 | 9% | 5% | -100% | -84% | 10 min |
| Women's T20 Match | ✘ | 43 | 0 | 19% | 9% | -100% | -68% | 27 min |
| Allsvenskan Game | ✘ | 43 | 1 | 14% | 14% | +117% | -76% | 11 min |
| NWSL Game | ✔ | 42 | 0 | 7% | 0% | -100% | -88% | 7 min |
| Peru Liga 1 Game | ✘ | 42 | 0 | 14% | 10% | -100% | -75% | 10 min |
| Turkish Super Lig Game | ✘ | 42 | 0 | 14% | 0% | -100% | -75% | 13 min |
| Eredivisie Game | ✔ | 42 | 0 | 10% | 7% | -100% | -83% | 5 min |
| Bundesliga Game | ✔ | 41 | 1 | 12% | 7% | +128% | -79% | 2 min |
| Finland Korisliiga Game | ✘ | 40 | 1 | 8% | 5% | +133% | -87% | 9 min |
| Thai League 1 Game | ✘ | 40 | 0 | 22% | 8% | -100% | -61% | 10 min |
| Japan B League Game | ✘ | 40 | 0 | 10% | 0% | -100% | -83% | 13 min |
| Italy Serie A2 Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Czech First League Game | ✘ | 39 | 0 | 13% | 0% | -100% | -78% | 8 min |
| Ligue 1 Game | ✔ | 38 | 0 | 18% | 8% | -100% | -68% | 9 min |
| Serbian SuperLiga Game | ✘ | 38 | 0 | 3% | 0% | -100% | -95% | 12 min |
| Israeli Premier League Game | ✘ | 38 | 0 | 3% | 0% | -100% | -95% | 8 min |
| Men's ODI Cricket Match | ✘ | 37 | 2 | 19% | 8% | +405% | -67% | 36 min |
| Korea K League Game | ✘ | 37 | 1 | 19% | 11% | +152% | -67% | 8 min |
| Adriatic ABA Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 11 min |
| Korea K-League 2 Game | ✘ | 36 | 0 | 17% | 8% | -100% | -71% | 9 min |
| Eliteserien Game | ✘ | 36 | 0 | 11% | 6% | -100% | -81% | 14 min |
| Ecuador Liga Pro Game | ✘ | 36 | 0 | 11% | 3% | -100% | -81% | 6 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| APF Division de Honor Game | ✘ | 33 | 0 | 12% | 3% | -100% | -79% | 6 min |
| Vietnam V-League 1 Game | ✘ | 33 | 1 | 9% | 6% | +183% | -84% | 10 min |
| England Women's Super League Game | ✘ | 32 | 0 | 19% | 6% | -100% | -68% | 34 min |
| Super League Greece Game | ✘ | 31 | 0 | 19% | 6% | -100% | -66% | 12 min |
| Egyptian Premier League Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 11 min |
| Serie A Femminile Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Bolivia Premier Division Game | ✘ | 30 | 0 | 17% | 3% | -100% | -71% | 3 min |
| Rugby French 14 Match | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 8 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Sweden SBL Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 15 min |
| Australia NBL Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| LNB Elite Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Spain Liga ACB Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| Venezuela Liga FUTVE game | ✘ | 28 | 0 | 18% | 14% | -100% | -69% | 6 min |
| Scottish Premiership Game | ✘ | 27 | 0 | 11% | 0% | -100% | -81% | 17 min |
| Czech NBL Game | ✘ | 26 | 0 | 4% | 0% | -100% | -93% | 17 min |
| Danish Superliga Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 11 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Spanish Liga F Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| Russia VTB United Game | ✘ | 24 | 0 | 4% | 0% | -100% | -93% | 14 min |
| Italy Serie A Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Liga Portugal Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 10 min |
| Qatar Stars League | ✘ | 24 | 0 | 12% | 4% | -100% | -78% | 7 min |
| Austria BSL Game | ✘ | 23 | 0 | 9% | 4% | -100% | -85% | 5 min |
| Croatia HNL Game | ✘ | 23 | 0 | 9% | 4% | -100% | -85% | 11 min |
| Latvian Virsliga Game | ✘ | 23 | 0 | 13% | 4% | -100% | -77% | 17 min |
| Turkey BSL Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Belgian Pro League Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 11 min |
| FIBA Europe Cup Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 9 min |
| Romanian Liga I Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 8 min |
| Professional Baseball Game | partly | 21 | 0 | 14% | 10% | -100% | -75% | 2 min |
| Bundesliga Basketball Game | ✘ | 21 | 0 | 10% | 5% | -100% | -83% | 12 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Croatia Premijer Liga Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 20 | 0 | 10% | 0% | -100% | -83% | 12 min |
| Faroe Islands Premier League Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 131 min |
| Austrian Bundesliga Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 13 min |
| Slovakia SBL Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovenian Prva Liga Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 6 min |
| England Super League Basketball Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Singapore Premier League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 15 min |
| Korea KBL Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Australian A League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 6 min |
| German Women's Bundesliga Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 29 min |
| Women's ODI Cricket Match | ✘ | 17 | 0 | 18% | 6% | -100% | -69% | 50 min |
| Slovenia 1. SKL Game | ✘ | 17 | 0 | 6% | 6% | -100% | -90% | 15 min |
| LKL Lithuania Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Brazil NBB Basketball Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Swiss Super League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 22 min |
| Indian Super League Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 10 min |
| Hungarian NB I Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's Pro Basketball Game | ✔ | 15 | 0 | 20% | 7% | -100% | -65% | 6 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| FIBA Champions League Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| CFL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| French Women's Première Ligue Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 5 min |
| Liga Nacional de Basquetbol Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Men's Iceland Basketball Premier League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| BNXT League Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Colombia LBP Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Polish Hockey Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 9 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| EuroLeague (W) Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 7 min |
| United Rugby Championship Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 4 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Powerslap Match Winner | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 12 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Philippines PBA Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Israel Super League Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 16 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Ligue Magnus Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 7 min |
| GBL Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Ukraine SuperLeague Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 12 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Portugal LPB Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 49 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| Women's Bundesliga Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Serbia KLS Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Denmark Basketligaen Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 21 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| NBL Australia (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Hungary NB I. A Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 738 | 5% | 1% | 0% | -91% |
| 5–15 min | 416 | 17% | 7% | 1% | -70% |
| 15–30 min | 276 | 26% | 14% | 1% | -54% |
| 30–60 min | 201 | 18% | 10% | 0% | -68% |
| Over 60 min | 166 | 17% | 9% | 0% | -71% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 44 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-24 19:30 | Women's Pro Basketball Game | Atlanta | ✔ | 16.5 - 4th · GS 67 - ATL 62 | — | In play | — |
| 10-24 19:30 | Spain Liga ACB Game | CB Coruna | ✘ | — | — | In play | — |
| 10-24 19:28 | Hungarian NB I Game | Kisvarda FC | ✘ | — | — | In play | — |
| 10-24 19:28 | Hungarian NB I Game | Zalaegerszeg | ✘ | — | — | In play | — |
| 10-24 19:26 | Men's T20 Cricket Match | Emirates Reds | ✘ | — | — | In play | — |
| 10-24 19:25 | Russia Liga Pro Match | Pandur Ivan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:25 | Turkey BSL Game | Besiktas JK | ✘ | — | — | In play | — |
| 10-24 19:23 | eSoccer Game | FC Bayern (Krocs) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:23 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:22 | eBasketball Game | New York Knicks (Barry) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:22 | eSoccer Game | Crystal Palace (Declan) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:21 | eBasketball Game | Brooklyn Nets (Shaq) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:21 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:21 | Major League Soccer Game | Tie | ✔ | 83' · NSH 2 - MTL 0 | — | In play | — |
| 10-24 19:20 | Russia Liga Pro Match | Zubov Aleksei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:20 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:20 | eSoccer Game | England (Millie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:19 | eSoccer Game | Everton (Hazard) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:19 | eSoccer Game | Chelsea (Luis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:19 | eSoccer Game | Portugal (Olive) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:19 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:18 | Darts Match | Nathan Potter | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:16 | Serie B Game | Tie | ✘ | — | — | In play | — |
| 10-24 19:15 | eFootball Game | Atlanta (Cooper) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:15 | College Football Game | Bucknell | ✘ | — | — | In play | — |
| 10-24 19:12 | Major League Soccer Game | Montreal | ✔ | 75' · NSH 1 - MTL 0 | — | In play | — |
| 10-24 19:12 | Russia Liga Pro Match | Borisov Andrei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:10 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:09 | eSoccer Game | Real Madrid (Krocs) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 19:09 | French Women's Première Ligue Game | Marseille | ✘ | — | — | In play | — |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
