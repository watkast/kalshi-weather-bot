# 15-Minute 1¢ Study

*Updated Mon Oct 26, 6:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2742 finished bets | 1% | $80.45 | +26% | +2.93¢ | $31.40 / $49.05 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2547 | $54.00 | +19% |
| Volatility model ≥ 2%, hold to the close | 5087 | -$21.40 | -3% |
| Momentum model ≥ 2%, hold to the close | 4234 | -$34.50 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32687 | 32679 | 121 (0%) | 1.07% | -$2,276.95 (-57%) | Hold to the close: -$2,276.95 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21010 | 4.6% | 0.4% (85) | -661% | ❌ Worse |
| Momentum model | 21010 | 4.5% | 0.4% (85) | -685% | ❌ Worse |
| Mean-reversion model | 21010 | 7.9% | 0.4% (85) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21010 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5087 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2742 | 28 | +26% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1551 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4234 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2547 | 24 | +19% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1658 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8494 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5948 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3959 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21210 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7621 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3848 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32679 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 121 | 0% | -$2,276.95 | -57% | — |
| Sell at 2¢ | 1223 | 4% | -$3,484.97 | -88% | 47 sec |
| Sell at 3¢ | 838 | 3% | -$3,476.13 | -88% | 48 sec |
| Sell at 5¢ | 583 | 2% | -$3,424.00 | -86% | 61 sec |
| Sell at 10¢ | 362 | 1% | -$3,286.73 | -83% | 65 sec |
| Sell at 25¢ | 194 | 1% | -$3,048.81 | -77% | 82 sec |
| Sell at 50¢ | 125 | 0% | -$2,763.20 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1447 | 7 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 10475 | 56 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8275 | 30 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12478 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2377 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2369 | 8 | 5% | 3% | -58% | -88% | -87% |
| BNB | 2366 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2363 | 6 | 4% | 2% | -68% | -92% | -92% |
| ETH | 2357 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2349 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2346 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2345 | 12 | 5% | 2% | -34% | -82% | -82% |
| BTC | 2338 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1230 | 4 | 4% | 2% | -61% | -81% | -83% |
| SILVER | 1198 | 6 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1173 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1045 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1021 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 976 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 969 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 933 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 922 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 905 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 467 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 426 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16547 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 16132 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3529 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3640 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5490 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6200 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2347 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,796 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 5:59:18 AM | COPPER | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:18 AM | EURUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:18 AM | NATGAS | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:01 AM | AUDUSD | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:45 AM | DOGE | DOWN | 74 sec | +0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:29 AM | USDJPY | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:29 AM | NEAR | DOWN | 1.5 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:57:57 AM | BTC | DOWN | 2.0 min | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:57:57 AM | SILVER | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:57:41 AM | PLATINUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:56:52 AM | BNB | DOWN | 3.1 min | +0.259% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:56:36 AM | ETH | DOWN | 3.4 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:56:20 AM | XRP | DOWN | 3.6 min | +0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:56:20 AM | GBPUSD | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:55:35 AM | USDCAD | DOWN | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:55:35 AM | SOL | DOWN | 4.4 min | +0.466% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:55:35 AM | ZEC | DOWN | 4.4 min | +0.777% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:55:35 AM | HYPE | DOWN | 4.4 min | +0.388% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:44:44 AM | ETH | DOWN | 15 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:44:44 AM | PALLADIUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:44:28 AM | ZEC | UP | 31 sec | -0.190% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:43:55 AM | HYPE | DOWN | 64 sec | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:43:23 AM | BTC | DOWN | 1.6 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:43:07 AM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:43:07 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:42:34 AM | SOL | DOWN | 2.4 min | +0.177% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 5:42:18 AM | XRP | DOWN | 2.7 min | +0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:40:39 AM | DOGE | DOWN | 4.3 min | +0.295% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:40:07 AM | NEAR | DOWN | 4.9 min | +0.833% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:39:52 AM | BNB | DOWN | 5.1 min | +0.204% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
