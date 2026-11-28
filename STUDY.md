# 1¢ Study

*Updated Fri Nov 27, 8:32 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 88 finished bets | 1% | $0.80 | +6% | +0.91¢ | $7.40 / -$6.60 |

*Expect about **2 buys a day**, roughly **$0.24/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 216 | -$4.40 | -14% |
| ESPN win probability ≥ 5%, sell at 50¢ | 88 | -$6.45 | -49% |
| ESPN win probability ≥ 5%, sell at 25¢ | 88 | -$6.58 | -50% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 77725 | 4227 | 20 (0%) | 1.1% | -$354.05 (-56%) | Hold to the end: -$354.05 (-56%) |

*In play right now: 29. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 1163 | 2.8% | 0.3% (4) | -160% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1163 | 4 | -68% | -70% | -68% | -69% |
| ESPN win probability ≥ 2% | 216 | 2 | -14% | -57% | -55% | -60% |
| ESPN win probability ≥ 5% | 88 | 1 | +6% | -82% | -85% | -85% |
| ESPN win probability ≥ 10% | 59 | 1 | +58% | -82% | -82% | -85% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 4227 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 73469 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 20 | 0% | -$354.05 | -56% |
| Sell at 2¢ | 603 | 14% | -$477.27 | -75% |
| Sell at 3¢ | 430 | 10% | -$466.35 | -74% |
| Sell at 5¢ | 287 | 7% | -$447.50 | -71% |
| Sell at 10¢ | 122 | 3% | -$474.23 | -75% |
| Sell at 25¢ | 49 | 1% | -$471.86 | -74% |
| Sell at 50¢ | 33 | 1% | -$411.30 | -65% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 37400 | 28 | 1% | 1% | -93% | -98% | 3 min |
| Russia Liga Pro Match | ✘ | 4929 | 0 | 2% | 1% | -100% | -97% | 4 min |
| eBasketball Game | ✘ | 3723 | 8 | 4% | 2% | -80% | -91% | 3 min |
| ITF Women's Match | ✘ | 2169 | 8 | 14% | 6% | -66% | -76% | 4 min |
| ITF Men's Match | ✘ | 2067 | 5 | 14% | 6% | -77% | -76% | 5 min |
| Counter-Strike 2 Game | ✘ | 1961 | 4 | 6% | 3% | -81% | -90% | 11 min |
| Challenger ATP  | ✘ | 1417 | 6 | 12% | 5% | -60% | -78% | 5 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Men's College Basketball Game | partly | 1110 | 5 | 19% | 9% | -58% | -67% | 24 min |
| Women's College Basketball Game | partly | 1037 | 3 | 15% | 6% | -73% | -75% | 29 min |
| eFootball Game | ✘ | 850 | 2 | 2% | 2% | -78% | -97% | 2 min |
| College Football Game | partly | 741 | 5 | 11% | 5% | -37% | -81% | 23 min |
| Darts Match | ✘ | 497 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Dota 2 Game | ✘ | 468 | 1 | 1% | 1% | -80% | -98% | 32 min |
| Women's College Volleyball Match | ✘ | 462 | 2 | 4% | 2% | -60% | -94% | 40 min |
| Men's T20 Cricket Match | ✘ | 452 | 2 | 15% | 6% | -59% | -74% | 27 min |
| Serie C Game | ✘ | 439 | 2 | 5% | 3% | -57% | -91% | 8 min |
| NHL Game | ✔ | 404 | 4 | 16% | 8% | -8% | -73% | 5 min |
| Challenger WTA | ✘ | 331 | 1 | 13% | 4% | -72% | -78% | 9 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| NBA Game | partly | 316 | 0 | 19% | 7% | -100% | -67% | 11 min |
| AHL Game | ✘ | 307 | 0 | 4% | 2% | -100% | -93% | 6 min |
| College Hockey Game | ✘ | 275 | 0 | 1% | 0% | -100% | -99% | 16 min |
| Major League Soccer Game | partly | 239 | 1 | 10% | 5% | -61% | -82% | 8 min |
| Valorant game winner | ✘ | 239 | 0 | 3% | 2% | -100% | -95% | 19 min |
| UEFA Nations League Game | ✔ | 215 | 0 | 13% | 7% | -100% | -78% | 10 min |
| Japan J2 League Game | ✘ | 209 | 1 | 11% | 4% | -55% | -82% | 7 min |
| WTA Tennis Match | ✘ | 203 | 0 | 13% | 3% | -100% | -77% | 5 min |
| Liga DIMAYOR Game | ✘ | 189 | 1 | 10% | 3% | -51% | -83% | 8 min |
| KHL Game | ✘ | 189 | 0 | 3% | 2% | -100% | -94% | 6 min |
| Argentina Primera Division Game | ✘ | 187 | 2 | 16% | 9% | -0% | -72% | 9 min |
| EFL Championship Game | ✔ | 178 | 1 | 8% | 5% | -48% | -85% | 9 min |
| Ettan Game | ✘ | 177 | 0 | 5% | 1% | -100% | -92% | 10 min |
| English National League Game | ✘ | 173 | 1 | 8% | 5% | -46% | -87% | 11 min |
| Brasileiro Serie B Game | ✘ | 168 | 1 | 7% | 3% | -44% | -88% | 10 min |
| Argentine Nacional B Game | ✘ | 165 | 0 | 8% | 5% | -100% | -86% | 8 min |
| League of Legends Game | ✘ | 165 | 0 | 7% | 2% | -100% | -87% | 12 min |
| Women's T20 Match | ✘ | 162 | 0 | 16% | 6% | -100% | -72% | 29 min |
| Brasileiro Serie A Game | partly | 158 | 1 | 12% | 6% | -41% | -79% | 8 min |
| CONCACAF Nations League Game | partly | 156 | 2 | 20% | 8% | +20% | -66% | 20 min |
| ATP Tennis Match | ✘ | 155 | 0 | 15% | 6% | -100% | -73% | 4 min |
| Japan J League Game | ✘ | 148 | 2 | 16% | 7% | +26% | -72% | 11 min |
| LaLiga 2 Game | partly | 147 | 1 | 16% | 7% | -37% | -72% | 8 min |
| EFL League One Game | ✔ | 145 | 1 | 9% | 3% | -36% | -84% | 10 min |
| Serie B Game | ✘ | 141 | 0 | 11% | 5% | -100% | -80% | 10 min |
| Liga MX Game | ✔ | 136 | 0 | 14% | 7% | -100% | -76% | 6 min |
| Liiga Game | ✘ | 136 | 0 | 0% | 0% | -100% | -100% | 6 min |
| German 3. Liga Game | ✘ | 135 | 0 | 10% | 4% | -100% | -83% | 11 min |
| Overwatch Game | ✘ | 133 | 0 | 2% | 1% | -100% | -96% | 6 min |
| Eerste Divisie Game | ✘ | 132 | 0 | 9% | 5% | -100% | -84% | 12 min |
| Serie A Game | ✔ | 129 | 0 | 10% | 6% | -100% | -83% | 13 min |
| R6 Game | ✘ | 121 | 1 | 10% | 4% | -23% | -83% | 8 min |
| Peru Liga 1 Game | ✘ | 120 | 0 | 15% | 7% | -100% | -74% | 14 min |
| USL Championship Game | partly | 120 | 0 | 11% | 4% | -100% | -81% | 5 min |
| Japan B League Game | ✘ | 119 | 0 | 8% | 1% | -100% | -87% | 13 min |
| National League Game | ✘ | 118 | 1 | 1% | 1% | -21% | -99% | 6 min |
| NFL Game | ✔ | 118 | 2 | 19% | 8% | +58% | -68% | 9 min |
| UEFA Champions League Game | partly | 114 | 1 | 12% | 5% | -18% | -79% | 10 min |
| ELH Game | ✘ | 112 | 0 | 1% | 1% | -100% | -98% | 5 min |
| English Premier League Game | ✔ | 111 | 1 | 8% | 5% | -16% | -86% | 10 min |
| Tweede Divisie Game | ✘ | 110 | 0 | 2% | 1% | -100% | -97% | 8 min |
| TFF 1. Lig Game | ✘ | 110 | 0 | 11% | 6% | -100% | -81% | 11 min |
| AFCON Game Winner | ✘ | 109 | 1 | 17% | 6% | -14% | -71% | 20 min |
| EuroCup Basketball Game | ✘ | 109 | 0 | 5% | 4% | -100% | -92% | 11 min |
| La Liga Game | ✔ | 108 | 0 | 18% | 10% | -100% | -70% | 8 min |
| UEFA Conference League Game | partly | 108 | 0 | 13% | 8% | -100% | -78% | 13 min |
| Indonesia Super League Game | ✘ | 107 | 0 | 13% | 8% | -100% | -77% | 12 min |
| International Friendly Game | partly | 106 | 1 | 16% | 5% | -12% | -72% | 17 min |
| UEFA Europa League Game | partly | 104 | 1 | 15% | 8% | -10% | -73% | 12 min |
| Euroleague Game | ✘ | 103 | 0 | 19% | 6% | -100% | -66% | 12 min |
| Liga Expansion Game | ✘ | 103 | 0 | 7% | 3% | -100% | -88% | 13 min |
| DEL Game | ✘ | 101 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Italy Serie A2 Game | ✘ | 101 | 1 | 2% | 1% | -8% | -97% | 6 min |
| Polish Ekstraklasa Game | ✘ | 101 | 0 | 12% | 6% | -100% | -79% | 12 min |
| Slovakian 2. Liga Game | ✘ | 100 | 0 | 5% | 4% | -100% | -91% | 44 min |
| Liga Leumit Game | ✘ | 100 | 0 | 5% | 3% | -100% | -91% | 18 min |
| Men's ODI Cricket Match | ✘ | 100 | 3 | 20% | 8% | +180% | -65% | 55 min |
| Ligue 1 Game | ✔ | 97 | 1 | 15% | 8% | -4% | -73% | 8 min |
| Uruguay Primera Division Game | ✘ | 96 | 0 | 12% | 6% | -100% | -78% | 10 min |
| SHL Game | ✘ | 96 | 0 | 3% | 2% | -100% | -95% | 6 min |
| Korea K-League 2 Game | ✘ | 96 | 0 | 10% | 5% | -100% | -82% | 9 min |
| Chinese Basketball Association Game  | ✘ | 95 | 0 | 8% | 2% | -100% | -85% | 10 min |
| Bundesliga Game | ✔ | 95 | 1 | 16% | 8% | -2% | -73% | 9 min |
| Ecuador Liga Pro Game | ✘ | 94 | 0 | 6% | 2% | -100% | -89% | 11 min |
| Ligue 2 Game | ✘ | 94 | 0 | 7% | 5% | -100% | -87% | 12 min |
| Allsvenskan Game | ✘ | 93 | 1 | 14% | 8% | +0% | -76% | 12 min |
| AFC Champions League Game | ✘ | 93 | 1 | 8% | 3% | +0% | -87% | 11 min |
| Eliteserien Game | ✘ | 90 | 0 | 12% | 3% | -100% | -79% | 14 min |
| Turkish Super Lig Game | ✘ | 90 | 0 | 19% | 4% | -100% | -67% | 14 min |
| Eredivisie Game | ✔ | 90 | 0 | 11% | 8% | -100% | -81% | 6 min |
| Bolivia Premier Division Game | ✘ | 90 | 0 | 7% | 1% | -100% | -88% | 11 min |
| APF Division de Honor Game | ✘ | 89 | 0 | 17% | 4% | -100% | -71% | 13 min |
| China League 1 Game | ✘ | 89 | 0 | 9% | 4% | -100% | -84% | 12 min |
| Czech First League Game | ✘ | 88 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Bundesliga 2 Game | ✔ | 87 | 0 | 13% | 6% | -100% | -78% | 8 min |
| Copa Del Rey Game | ✘ | 85 | 0 | 6% | 5% | -100% | -90% | 40 min |
| Belgian Pro League Game | ✘ | 83 | 0 | 11% | 2% | -100% | -81% | 19 min |
| Saudi Pro League Game | ✘ | 82 | 2 | 18% | 12% | +128% | -68% | 13 min |
| NWSL Game | ✔ | 81 | 0 | 6% | 1% | -100% | -89% | 7 min |
| England Women's Super League Game | ✘ | 81 | 0 | 14% | 6% | -100% | -76% | 20 min |
| Mobile Legends Bang Bang Game | ✘ | 81 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Thai League 1 Game | ✘ | 80 | 0 | 14% | 6% | -100% | -76% | 13 min |
| Chile Liga de Primera Game | ✘ | 79 | 0 | 15% | 4% | -100% | -74% | 13 min |
| Czech National Football League Game | ✘ | 79 | 0 | 14% | 8% | -100% | -76% | 11 min |
| Brazil NBB Basketball Game | ✘ | 79 | 0 | 6% | 3% | -100% | -89% | 18 min |
| FIBA Europe Cup Game | ✘ | 78 | 0 | 6% | 3% | -100% | -89% | 9 min |
| Spanish Liga F Game | ✘ | 78 | 0 | 10% | 6% | -100% | -82% | 14 min |
| LNB Elite 2 Game | ✘ | 77 | 0 | 1% | 0% | -100% | -98% | 6 min |
| Serie A Femminile Game | ✘ | 77 | 1 | 8% | 4% | +21% | -86% | 15 min |
| Serbian SuperLiga Game | ✘ | 75 | 0 | 5% | 1% | -100% | -91% | 16 min |
| Super League Greece Game | ✘ | 73 | 0 | 15% | 3% | -100% | -74% | 14 min |
| Taca de Portugal Game | ✘ | 73 | 0 | 16% | 5% | -100% | -72% | 14 min |
| Korea K League Game | ✘ | 72 | 1 | 15% | 7% | +30% | -74% | 8 min |
| Romanian Liga I Game | ✘ | 72 | 1 | 12% | 4% | +30% | -78% | 13 min |
| Vietnam V-League 1 Game | ✘ | 70 | 1 | 4% | 3% | +33% | -93% | 10 min |
| Israeli Premier League Game | ✘ | 70 | 0 | 6% | 1% | -100% | -90% | 13 min |
| Liga Portugal Game | ✘ | 69 | 0 | 7% | 3% | -100% | -87% | 13 min |
| Scottish Premiership Game | ✘ | 69 | 0 | 10% | 1% | -100% | -82% | 12 min |
| LNBP Basketball Game | ✘ | 68 | 0 | 10% | 3% | -100% | -82% | 12 min |
| Finland Korisliiga Game | ✘ | 68 | 1 | 6% | 3% | +37% | -90% | 9 min |
| Adriatic ABA Game | ✘ | 67 | 1 | 6% | 3% | +39% | -90% | 9 min |
| Spain Liga ACB Game | ✘ | 67 | 0 | 6% | 3% | -100% | -90% | 14 min |
| Egyptian Premier League Game | ✘ | 64 | 0 | 14% | 6% | -100% | -76% | 8 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Czech NBL Game | ✘ | 62 | 0 | 3% | 2% | -100% | -94% | 15 min |
| Chinese Super League Game | ✘ | 62 | 1 | 11% | 6% | +51% | -80% | 19 min |
| LNB Elite Game | ✘ | 61 | 0 | 2% | 0% | -100% | -97% | 9 min |
| Italy Serie A Game | ✘ | 60 | 0 | 3% | 2% | -100% | -94% | 7 min |
| Venezuela Liga FUTVE game | ✘ | 60 | 0 | 18% | 12% | -100% | -68% | 8 min |
| Bundesliga Basketball Game | ✘ | 59 | 0 | 7% | 3% | -100% | -88% | 13 min |
| Qatar Stars League | ✘ | 59 | 0 | 14% | 7% | -100% | -76% | 11 min |
| KBO Game | ✘ | 57 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Australia NBL Game | ✘ | 57 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Danish Superliga Game | ✘ | 57 | 0 | 9% | 5% | -100% | -85% | 12 min |
| Liga Nacional de Basquetbol Game | ✘ | 56 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Croatia HNL Game | ✘ | 55 | 0 | 7% | 4% | -100% | -87% | 11 min |
| French Women's Première Ligue Game | ✘ | 55 | 0 | 11% | 7% | -100% | -81% | 14 min |
| Champions League Women's Game | partly | 54 | 1 | 20% | 9% | +73% | -65% | 26 min |
| Swiss Super League Game | ✘ | 54 | 1 | 7% | 4% | +73% | -87% | 10 min |
| Hungarian NB I Game | ✘ | 54 | 0 | 6% | 6% | -100% | -90% | 8 min |
| Slovenian Prva Liga Game | ✘ | 53 | 0 | 9% | 2% | -100% | -84% | 13 min |
| Sweden SBL Game | ✘ | 52 | 0 | 6% | 6% | -100% | -90% | 13 min |
| Austria BSL Game | ✘ | 50 | 0 | 6% | 4% | -100% | -90% | 9 min |
| Rugby French 14 Match | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Korea KBL Game | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Australian A League Game | ✘ | 50 | 0 | 10% | 4% | -100% | -83% | 11 min |
| Indian Super League Game | ✘ | 50 | 0 | 12% | 6% | -100% | -79% | 8 min |
| German Women's Bundesliga Game | ✘ | 50 | 0 | 6% | 2% | -100% | -90% | 22 min |
| Turkey BSL Game | ✘ | 49 | 0 | 2% | 2% | -100% | -96% | 10 min |
| Eredivisie Vrouwen Game | ✘ | 48 | 0 | 4% | 4% | -100% | -93% | 8 min |
| Austrian Bundesliga Game | ✘ | 48 | 0 | 8% | 6% | -100% | -86% | 12 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Russia VTB United Game | ✘ | 45 | 0 | 4% | 0% | -100% | -92% | 16 min |
| Latvian Virsliga Game | ✘ | 45 | 0 | 16% | 7% | -100% | -73% | 22 min |
| BNXT League Game | ✘ | 42 | 0 | 5% | 2% | -100% | -92% | 11 min |
| Polish Hockey Game | ✘ | 42 | 0 | 2% | 2% | -100% | -96% | 7 min |
| Ligue Magnus Game | ✘ | 42 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Slovakia SBL Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 15 min |
| Canadian Premier League | ✘ | 40 | 1 | 15% | 12% | +133% | -74% | 17 min |
| England Super League Basketball Game | ✘ | 40 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| EFL League Two Game | ✔ | 40 | 0 | 10% | 5% | -100% | -83% | 3 min |
| EFL Trophy Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 46 min |
| FIBA Champions League Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 10 min |
| UAE Pro League | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 15 min |
| LKL Lithuania Game | ✘ | 37 | 0 | 3% | 0% | -100% | -95% | 10 min |
| Singapore Premier League Game | ✘ | 37 | 0 | 11% | 3% | -100% | -81% | 20 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Croatia Premijer Liga Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Slovenia 1. SKL Game | ✘ | 33 | 0 | 3% | 3% | -100% | -95% | 15 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| EuroBasket (W) Game | ✘ | 31 | 0 | 10% | 0% | -100% | -83% | 11 min |
| Slovakian Cup Game | ✘ | 30 | 0 | 7% | 3% | -100% | -88% | 16 min |
| Lithuania NKL Game | ✘ | 30 | 0 | 3% | 3% | -100% | -94% | 70 min |
| Women's ODI Cricket Match | ✘ | 29 | 0 | 14% | 7% | -100% | -76% | 40 min |
| Malaysia Super League Game | ✘ | 28 | 0 | 7% | 0% | -100% | -88% | 9 min |
| Men's Iceland Basketball Premier League Game | ✘ | 27 | 0 | 15% | 7% | -100% | -74% | 7 min |
| South African Premiership Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Call of Duty Games | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 38 min |
| EuroLeague (W) Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 17 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| Liga Portugal 2 Game | ✘ | 22 | 0 | 14% | 9% | -100% | -76% | 16 min |
| Coupe de France Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 118 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Colombia LBP Basketball Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Israel Super League Game | ✘ | 21 | 0 | 5% | 5% | -100% | -92% | 5 min |
| Slovakia Niké liga Game | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 19 min |
| CFL Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 8 min |
| Japan B.League One Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 325 min |
| Mexican Pacific League | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Women's Pro Basketball Game | ✔ | 18 | 0 | 22% | 6% | -100% | -61% | 6 min |
| Powerslap Match Winner | ✘ | 18 | 0 | 6% | 6% | -100% | -90% | 6 min |
| Philippines PBA Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Bare Knuckle Fight Match | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 23 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Ukrainian Premier League Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 14 min |
| GBL Basketball Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| Bulgaria First League Game | ✘ | 15 | 0 | 13% | 13% | -100% | -77% | 7 min |
| Women's Bundesliga Basketball Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Australia A League Women Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Scottish Championship Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 25 min |
| Belgium Challenger Pro League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Ukraine SuperLeague Game | ✘ | 13 | 0 | 8% | 0% | -100% | -87% | 12 min |
| Poland PLK Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 14 min |
| RAF Match Result | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 2840 min |
| Dominican Winter League (LIDOM) | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 58 min |
| Venezuelan Winter League (LVBP) | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 53 min |
| Champions League Hockey | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Portugal LPB Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 8 min |
| USL Super League Women Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 7 min |
| Uruguay LUB Basketball Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 8 min |
| FIBA Game | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 20 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| CONMEBOL Sudamericana Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 10 min |
| NBL Australia (W) Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 11 min |
| SAFF Championship Game | ✘ | 10 | 0 | 30% | 10% | -100% | -48% | 31 min |
| Scottish Women Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 8 min |
| Slovenian Cup Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 20 min |
| Israel National League Game | ✘ | 9 | 1 | 11% | 11% | +937% | -81% | 18 min |
| Puerto Rican Winter League (LBPRC) | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 57 min |
| Serbia KLS Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 8 min |
| Copa do Brasil Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 17 min |
| Liga MX Women Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Latvian-Estonian Basketball League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 7 min |
| China CBA (W) Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Puerto Rico BSN (W) Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 6 min |
| T10 Match | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 16 min |
| Romania Division A Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Padel Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Japan J League Cup Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Korea KBL (W) Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 17 min |
| AFC Champions League Two Game | ✘ | 6 | 0 | 33% | 17% | -100% | -42% | 18 min |
| Bosnia Division I Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 309 min |
| Italy Serie A (W) Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Womens TGL Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 71 min |
| Paraguay Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Serbian Cup Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 12 min |
| England Women League Cup Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 75 min |
| Turkey TBL Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 18 min |
| Davis Cup Match | ✘ | 4 | 0 | 50% | 0% | -100% | -13% | 11 min |
| Denmark Basketligaen Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 38 min |
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
| Men's Test Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2598 min |
| Colombian Winter League (LPB) | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| FIDE World Chess Championship Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 209 min |
| Australian Baseball League (ABL) | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 32 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Europe Adriatic League 2 Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Men's Rugby Union Nations Championship Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 34 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 1493 | 4% | 1% | 0% | -94% |
| 5–15 min | 957 | 16% | 8% | 1% | -72% |
| 15–30 min | 668 | 25% | 12% | 0% | -57% |
| 30–60 min | 530 | 20% | 12% | 1% | -65% |
| Over 60 min | 548 | 22% | 10% | 0% | -61% |

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
| 11-28 03:32 | AHL Game | Colorado Eagles | ✘ | — | — | In play | — |
| 11-28 03:31 | NBA Game | Minnesota | ✔ | 5:14 - 4th · MEM 103 - MIN 89 | — | In play | — |
| 11-28 03:28 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-28 03:27 | College Hockey Game | North Dakota | ✘ | — | — | In play | — |
| 11-28 03:27 | eSoccer Game | Crystal Palace (Mordor) | ✘ | — | — | In play | — |
| 11-28 03:25 | eFootball Game | Green Bay (Cooper) | ✘ | — | — | In play | — |
| 11-28 03:25 | eBasketball Game | Golden State Warriors (Tim) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:22 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:22 | eSoccer Game | Argentina (Mei) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:22 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:22 | eSoccer Game | FC Augsburg (Frost) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:22 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:21 | NBA Game | Boston | ✔ | 2.6 - 4th · ATL 87 - BOS 83 | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:21 | eSoccer Game | FSV Mainz 05 (Vini) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:17 | eBasketball Game | Los Angeles Lakers (Dirk) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:14 | eSoccer Game | Everton (Mordor) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:14 | eSoccer Game | Manchester City (Mantis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:10 | Dominican Winter League (LIDOM) | Gigantes del Cibao | ✘ | — | — | In play | — |
| 11-28 03:09 | Major League Soccer Game | Tie | ✔ | 90'+5' · MIA 0 - CLB 1 | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:09 | eSoccer Game | England (Millie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:08 | eSoccer Game | Dortmund (Kylian) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:08 | eSoccer Game | FSV Mainz 05 (Vini) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:08 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:08 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:08 | eSoccer Game | Spain (Florie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:08 | eSoccer Game | Portugal (Olive) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:07 | Venezuelan Winter League (LVBP) | Aguilas del Zulia | ✘ | — | — | In play | — |
| 11-28 03:07 | Dominican Winter League (LIDOM) | Aguilas Cibaenas | ✘ | — | — | In play | — |
| 11-28 03:07 | eSoccer Game | 1. FC Köln (Bradley) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-28 03:06 | Men's College Basketball Game | Idaho | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
