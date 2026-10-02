# 1¢ Study

*Updated Thu Oct 1, 8:07 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 162 finished bets | 1% | -$10.30 | -42% | -6.36¢ | -$12.15 / $1.85 |

*Expect about **39 buys a day**, roughly **$5.88/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 162 | -$17.55 | -72% |
| ESPN-verified leagues only, sell at 5¢ | 162 | -$18.45 | -76% |
| ESPN-verified leagues only, sell at 2¢ | 162 | -$18.58 | -76% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 2500 | 162 | 1 (1%) | 1.1% | -$10.30 (-42%) | Hold to the end: -$10.30 (-42%) |

*In play right now: 3. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 9 | 1.1% | 0.0% (0) | -13% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 2% | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 162 | 14% | 9% | 6% | 2% | 1% | 1% |
| Unverified | 2335 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 1% | -$10.30 | -42% |
| Sell at 2¢ | 22 | 14% | -$18.58 | -76% |
| Sell at 3¢ | 14 | 9% | -$18.84 | -78% |
| Sell at 5¢ | 9 | 6% | -$18.45 | -76% |
| Sell at 10¢ | 4 | 2% | -$19.06 | -78% |
| Sell at 25¢ | 1 | 1% | -$20.99 | -86% |
| Sell at 50¢ | 1 | 1% | -$17.55 | -72% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1018 | 0 | 1% | 0% | -100% | -99% | 5 min |
| ITF Men's Match | ✘ | 213 | 0 | 9% | 5% | -100% | -85% | 5 min |
| ITF Women's Match | ✘ | 206 | 0 | 12% | 6% | -100% | -80% | 4 min |
| Counter-Strike 2 Game | ✘ | 141 | 1 | 4% | 3% | -34% | -94% | 10 min |
| Challenger ATP  | ✘ | 129 | 0 | 8% | 2% | -100% | -87% | 5 min |
| TT Star Series Match | ✘ | 91 | 1 | 2% | 2% | +3% | -96% | 4 min |
| League of Legends Game | ✘ | 71 | 0 | 8% | 3% | -100% | -85% | 11 min |
| UEFA Nations League Game | ✔ | 52 | 0 | 10% | 4% | -100% | -83% | 6 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| CONCACAF Nations League Game | partly | 46 | 0 | 20% | 7% | -100% | -66% | 27 min |
| Men's T20 Cricket Match | ✘ | 26 | 0 | 15% | 8% | -100% | -73% | 18 min |
| Dota 2 Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 28 min |
| R6 Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| English National League Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Darts Match | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Challenger WTA | ✘ | 22 | 0 | 14% | 9% | -100% | -76% | 10 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| International Friendly Game | partly | 18 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's College Volleyball Match | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 30 min |
| KBO Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 4 min |
| Euroleague Game | ✘ | 14 | 0 | 21% | 7% | -100% | -63% | 26 min |
| KHL Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 5 min |
| Liga DIMAYOR Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 12 min |
| ATP Tennis Match | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 2 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Japan NPB Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 12 min |
| NHL Game | ✔ | 11 | 0 | 18% | 0% | -100% | -68% | 5 min |
| Brasileiro Serie B Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 11 min |
| SHL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 10 | 1 | 10% | 10% | +833% | -83% | 6 min |
| USL Championship Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 11 min |
| WTA Tennis Match | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 3 min |
| ELH Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Valorant game winner | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Uruguay Primera Division Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 10 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Women's Pro Basketball Game | ✔ | 6 | 0 | 17% | 17% | -100% | -71% | 15 min |
| Women's ODI Cricket Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Czech NBL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Liiga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Professional Baseball Game | partly | 5 | 0 | 20% | 0% | -100% | -65% | 9 min |
| Slovakia SBL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 35 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Major League Soccer Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 8 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Finland Korisliiga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 63 min |
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| Australia NBL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
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
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Croatia Premijer Liga Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 98 min |
| Austria BSL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 86 min |
| DEL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 44 min |
| Bundesliga Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 13 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 60 | 5% | 0% | 0% | -91% |
| 5–15 min | 30 | 17% | 3% | 0% | -71% |
| 15–30 min | 31 | 26% | 13% | 3% | -55% |
| 30–60 min | 22 | 23% | 14% | 0% | -61% |
| Over 60 min | 19 | 5% | 5% | 0% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 28 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-02 01:59 | TT Elite Series Match | Arkadiusz Skupinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:47 | NHL Game | Buffalo | ✔ | 2:39 - 3rd · BUF 3 - CBJ 5 | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:44 | NHL Game | Philadelphia | ✔ | 2:21 - OT · PHI 2 - NJ 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:44 | CONCACAF Nations League Game | Tie | ✔ | 76' · HAI 3 - DOM 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:43 | TT Elite Series Match | Adam Staniczek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:42 | Brasileiro Serie B Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:42 | TT Elite Series Match | Aleksander Barton | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:35 | NHL Game | Tampa Bay | ✔ | 8:44 - 3rd · TB 1 - NYR 4 | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:35 | CONCACAF Nations League Game | Dominican Republic | ✔ | 67' · HAI 2 - DOM 1 | 1¢ | ❌ Lost | -$0.15 |
| 10-02 01:31 | Brasileiro Serie B Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:26 | TT Elite Series Match | Kacper Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:22 | Brasileiro Serie B Game | Athletic Club Sjdr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:20 | Brasileiro Serie B Game | Goias | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:16 | Women's College Volleyball Match | Iowa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:06 | Women's College Volleyball Match | Northwestern | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:05 | TT Elite Series Match | Tkocz Marek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 01:04 | TT Elite Series Match | Jerzy Michalik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:55 | Counter-Strike 2 Game | BORRACHEIROS | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:50 | TT Elite Series Match | Arkadiusz Skupinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:49 | TT Elite Series Match | Jakub Lamperski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:48 | TT Elite Series Match | Linek Adam | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:45 | CONCACAF Nations League Game | Tie | ✔ | 45' · PUR 1 - CAY 0 | 1¢ | ❌ Lost | -$0.15 |
| 10-02 00:44 | CONCACAF Nations League Game | Cayman Islands | ✔ | 45' · PUR 1 - CAY 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:42 | TT Elite Series Match | Kacper Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:34 | Women's College Volleyball Match | Ohio State | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:30 | TT Elite Series Match | Dominik Solilo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:30 | TT Elite Series Match | Aleksander Barton | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:27 | TT Elite Series Match | Adrian Myszewski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:25 | CONCACAF Nations League Game | Tie | ✔ | 65' · ATG 1 - AIA 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-02 00:19 | Women's College Volleyball Match | Utah | ✘ | — | 4¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
