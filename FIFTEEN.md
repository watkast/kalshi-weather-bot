# 15-Minute 1¢ Study

*Updated Fri Nov 27, 6:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 5034 finished bets | 1% | $196.00 | +36% | +3.89¢ | $92.85 / $103.15 |

*Expect about **83 buys a day** (~$12.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4771 | $96.65 | +19% |
| Volatility model ≥ 2%, hold to the close | 9391 | $18.90 | +2% |
| Momentum model ≥ 2%, hold to the close | 7813 | -$57.20 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69657 | 69621 | 258 (0%) | 1.07% | -$4,812.60 (-57%) | Hold to the close: -$4,812.60 (-57%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 41083 | 4.5% | 0.4% (166) | -660% | ❌ Worse |
| Momentum model | 41083 | 4.5% | 0.4% (166) | -683% | ❌ Worse |
| Mean-reversion model | 41083 | 7.9% | 0.4% (166) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 41083 | 166 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9391 | 81 | +2% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 5034 | 53 | +36% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2926 | 32 | +63% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 7813 | 59 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4771 | 43 | +19% | -76% | -75% | -72% |
| Momentum model ≥ 10% | 3116 | 28 | +31% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16770 | 113 | -26% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11682 | 93 | -11% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7748 | 66 | -2% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 41289 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16645 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11687 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69621 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 258 | 0% | -$4,812.60 | -57% | — |
| Sell at 2¢ | 2853 | 4% | -$7,374.82 | -88% | 47 sec |
| Sell at 3¢ | 1915 | 3% | -$7,369.75 | -87% | 48 sec |
| Sell at 5¢ | 1296 | 2% | -$7,246.20 | -86% | 62 sec |
| Sell at 10¢ | 795 | 1% | -$6,963.15 | -83% | 65 sec |
| Sell at 25¢ | 428 | 1% | -$6,433.92 | -76% | 80 sec |
| Sell at 50¢ | 272 | 0% | -$5,832.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3613 | 17 | 10% | 4% | -55% | -82% | -83% |
| 2–5 min | 22571 | 117 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17304 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 26120 | 66 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4620 | 20 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4608 | 16 | 4% | 2% | -55% | -89% | -88% |
| SOL | 4602 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4596 | 22 | 5% | 2% | -39% | -85% | -85% |
| DOGE | 4594 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4588 | 19 | 6% | 3% | -48% | -82% | -82% |
| BTC | 4567 | 25 | 5% | 2% | -25% | -86% | -88% |
| NEAR | 4560 | 18 | 5% | 2% | -48% | -85% | -86% |
| XRP | 4554 | 16 | 4% | 2% | -55% | -88% | -88% |
| GOLD | 2456 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2443 | 9 | 4% | 2% | -55% | -86% | -87% |
| SILVER | 2406 | 9 | 5% | 2% | -55% | -83% | -84% |
| PLATINUM | 2173 | 5 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 2134 | 7 | 3% | 1% | -69% | -91% | -90% |
| GBPUSD | 2078 | 8 | 2% | 1% | -64% | -96% | -95% |
| COPPER | 2061 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2028 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 2017 | 10 | 2% | 1% | -54% | -77% | -77% |
| PALLADIUM | 1963 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1604 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1504 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1126 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 564 | 2 | 3% | 1% | -67% | -78% | -76% |
| 30YRRATE | 526 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 523 | 4 | 4% | 2% | -29% | -58% | -57% |
| 5YRRATE | 514 | 2 | 4% | 2% | -64% | -94% | -95% |
| INX | 142 | 1 | 2% | 1% | -34% | -96% | -96% |
| USDMXN | 70 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35418 | 134 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 34203 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5976 | 25 | 2% | 1% | -23% | -79% | -78% |
| 0.05–0.1% | 6564 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10228 | 37 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 13013 | 56 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 5499 | 24 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16692 | 51 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16558 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 17081 | 74 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19290 | 51 | 4% | 2% | -70% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,080 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/27 6:44:13 PM | BNB | DOWN | 46 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:44:13 PM | SOL | DOWN | 46 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:43:55 PM | DOGE | DOWN | 65 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 6:43:55 PM | XRP | DOWN | 65 sec | +0.063% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 6:43:39 PM | ETH | DOWN | 81 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 6:43:07 PM | NEAR | DOWN | 1.9 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 6:42:50 PM | HYPE | DOWN | 2.1 min | +0.237% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:42:50 PM | BTC | DOWN | 2.1 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 6:39:18 PM | ZEC | DOWN | 5.7 min | +1.063% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 6:29:26 PM | NATGAS | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 6:29:26 PM | ZEC | DOWN | 33 sec | +0.705% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:29:26 PM | BNB | DOWN | 33 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:29:26 PM | DOGE | DOWN | 33 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:29:26 PM | NEAR | DOWN | 33 sec | +0.635% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:29:26 PM | SOL | DOWN | 33 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:29:26 PM | HYPE | DOWN | 33 sec | +0.189% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:29:26 PM | XRP | DOWN | 33 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:29:26 PM | BTC | DOWN | 33 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/27 6:29:26 PM | ETH | DOWN | 33 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:59:49 PM | BTC | UP | 10 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:59:49 PM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:59:33 PM | EURUSD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:59:33 PM | ZEC | DOWN | 27 sec | +0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:59:14 PM | DOGE | UP | 45 sec | -0.141% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:59:14 PM | BNB | UP | 45 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:59:14 PM | ETH | UP | 45 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:58:58 PM | XRP | DOWN | 61 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:58:58 PM | HYPE | DOWN | 61 sec | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:57:20 PM | BRENT | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:57:02 PM | NEAR | DOWN | 3.0 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
