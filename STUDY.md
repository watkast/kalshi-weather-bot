# 1¢ Study

*Updated Fri Oct 2, 10:47 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 181 finished bets | 1% | -$13.15 | -48% | -7.27¢ | -$13.50 / $0.35 |

*Expect about **38 buys a day**, roughly **$5.72/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 5¢ | 181 | -$20.00 | -74% |
| ESPN-verified leagues only, sell at 2¢ | 181 | -$20.13 | -74% |
| ESPN-verified leagues only, sell at 50¢ | 181 | -$20.40 | -75% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 2856 | 181 | 1 (1%) | 1.1% | -$13.15 (-48%) | Hold to the end: -$13.15 (-48%) |

*In play right now: 10. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 13 | 1.1% | 0.0% (0) | -15% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13 | 0 | -100% | -73% | -80% | -67% |
| ESPN win probability ≥ 2% | 3 | 0 | -100% | -42% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 181 | 15% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 2665 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 1% | -$13.15 | -48% |
| Sell at 2¢ | 27 | 15% | -$20.13 | -74% |
| Sell at 3¢ | 16 | 9% | -$20.91 | -77% |
| Sell at 5¢ | 11 | 6% | -$20.00 | -74% |
| Sell at 10¢ | 5 | 3% | -$20.60 | -76% |
| Sell at 25¢ | 1 | 1% | -$23.84 | -88% |
| Sell at 50¢ | 1 | 1% | -$20.40 | -75% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1177 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 231 | 0 | 9% | 5% | -100% | -85% | 5 min |
| ITF Women's Match | ✘ | 221 | 0 | 13% | 6% | -100% | -78% | 4 min |
| Counter-Strike 2 Game | ✘ | 200 | 1 | 3% | 2% | -53% | -95% | 9 min |
| Challenger ATP  | ✘ | 140 | 0 | 8% | 1% | -100% | -86% | 5 min |
| TT Star Series Match | ✘ | 101 | 1 | 3% | 3% | -8% | -95% | 4 min |
| League of Legends Game | ✘ | 74 | 0 | 8% | 3% | -100% | -86% | 11 min |
| UEFA Nations League Game | ✔ | 54 | 0 | 9% | 4% | -100% | -84% | 6 min |
| CONCACAF Nations League Game | partly | 48 | 0 | 21% | 6% | -100% | -64% | 28 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| Darts Match | ✘ | 38 | 0 | 3% | 3% | -100% | -95% | 11 min |
| Dota 2 Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 28 min |
| Men's T20 Cricket Match | ✘ | 28 | 0 | 14% | 7% | -100% | -75% | 18 min |
| Challenger WTA | ✘ | 25 | 0 | 16% | 12% | -100% | -72% | 10 min |
| R6 Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| English National League Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| International Friendly Game | partly | 22 | 0 | 5% | 0% | -100% | -92% | 12 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Women's College Volleyball Match | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 30 min |
| KHL Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 5 min |
| NHL Game | ✔ | 16 | 0 | 19% | 6% | -100% | -68% | 6 min |
| ATP Tennis Match | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 2 min |
| WTA Tennis Match | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 3 min |
| KBO Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 4 min |
| Euroleague Game | ✘ | 14 | 0 | 21% | 7% | -100% | -63% | 26 min |
| Japan NPB Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liga DIMAYOR Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 12 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie B Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 11 min |
| SHL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 10 | 1 | 10% | 10% | +833% | -83% | 6 min |
| USL Championship Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 11 min |
| Valorant game winner | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 16 min |
| LNBP Basketball Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 22 min |
| ELH Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Women's Pro Basketball Game | ✔ | 7 | 0 | 29% | 14% | -100% | -50% | 13 min |
| Uruguay Primera Division Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 10 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Women's ODI Cricket Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Czech NBL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Liiga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Professional Baseball Game | partly | 5 | 0 | 20% | 0% | -100% | -65% | 9 min |
| Australia NBL Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 20 min |
| Slovakia SBL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 35 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Overwatch Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Finland Korisliiga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 63 min |
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Slovenia 1. SKL Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 105 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Russia VTB United Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 37 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Canadian Premier League | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 18 min |
| College Football Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 13 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Croatia Premijer Liga Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 98 min |
| Austria BSL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 86 min |
| DEL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 44 min |
| Bundesliga Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 13 min |
| NFL Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 1 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 67 | 7% | 1% | 0% | -87% |
| 5–15 min | 34 | 18% | 3% | 0% | -69% |
| 15–30 min | 33 | 27% | 12% | 3% | -53% |
| 30–60 min | 25 | 20% | 12% | 0% | -65% |
| Over 60 min | 22 | 9% | 9% | 0% | -84% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 28 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-02 16:47 | Counter-Strike 2 Game | Nuclear TigeRES | ✘ | — | — | In play | — |
| 10-02 16:44 | TT Elite Series Match | Jacek Oracz | ✘ | — | — | In play | — |
| 10-02 16:44 | TT Elite Series Match | Krzysztof Juszczyk | ✘ | — | — | In play | — |
| 10-02 16:43 | Challenger ATP  | Keegan Smith | ✘ | — | — | In play | — |
| 10-02 16:38 | League of Legends Game | Colossal Gaming | ✘ | — | — | In play | — |
| 10-02 16:38 | League of Legends Game | PCIFIC | ✘ | — | — | In play | — |
| 10-02 16:37 | Counter-Strike 2 Game | x3pt | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:36 | Darts Match | Petri Rasmus | ✘ | — | — | In play | — |
| 10-02 16:34 | TT Elite Series Match | Mateusz Trela | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:31 | Challenger ATP  | Matheus Pucinelli de Almeida | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-02 16:27 | Counter-Strike 2 Game | Eternal Fire | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:27 | Counter-Strike 2 Game | Anteiku | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:26 | TT Elite Series Match | Kowalski Kamil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:26 | Dota 2 Game | Xtreme Gaming | ✘ | — | — | In play | — |
| 10-02 16:24 | Counter-Strike 2 Game | 9INE | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:23 | Counter-Strike 2 Game | Prestige | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:22 | ITF Men's Match | Miguel Damas | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:22 | Counter-Strike 2 Game | Sashi Esport | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:17 | TT Elite Series Match | Szymon Brud | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:16 | KHL Game | Salavat Yulaev UFA | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:16 | League of Legends Game | NightBirds | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:15 | Darts Match | Harry Ward | ✘ | — | — | In play | — |
| 10-02 16:14 | TT Elite Series Match | Pawel Slosarczyk | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-02 16:13 | Counter-Strike 2 Game | BASEMENT BOYS | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:13 | Men's T20 Cricket Match | Pro Sports Titans | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:12 | Counter-Strike 2 Game | HAVU | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:12 | TT Elite Series Match | Krzysztof Juszczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:11 | KHL Game | Amur Khabarovsk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:07 | Counter-Strike 2 Game | Matrix | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 16:01 | TT Elite Series Match | Piotr Strus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
