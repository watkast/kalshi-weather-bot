# 15-Minute 1¢ Study

*Updated Tue Oct 20, 5:41 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2109 finished bets | 1% | $85.30 | +36% | +4.04¢ | $24.35 / $60.95 |

*Expect about **95 buys a day** (~$14.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1940 | $66.70 | +31% |
| Momentum model ≥ 2%, hold to the close | 3236 | -$15.65 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 2109 | -$31.70 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25012 | 24999 | 92 (0%) | 1.07% | -$1,750.25 (-58%) | Hold to the close: -$1,750.25 (-58%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16357 | 4.6% | 0.4% (65) | -671% | ❌ Worse |
| Momentum model | 16357 | 4.5% | 0.4% (65) | -694% | ❌ Worse |
| Mean-reversion model | 16357 | 7.7% | 0.4% (65) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16357 | 65 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3823 | 31 | -7% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2109 | 23 | +36% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1227 | 15 | +72% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3236 | 26 | -4% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1940 | 20 | +31% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1284 | 13 | +39% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6382 | 42 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4439 | 34 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2935 | 22 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16555 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5883 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2561 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24999 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,750.25 | -58% | — |
| Sell at 2¢ | 901 | 4% | -$2,677.99 | -88% | 46 sec |
| Sell at 3¢ | 612 | 2% | -$2,673.57 | -88% | 47 sec |
| Sell at 5¢ | 435 | 2% | -$2,629.50 | -87% | 51 sec |
| Sell at 10¢ | 265 | 1% | -$2,537.10 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,344.99 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,117.00 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 969 | 5 | 10% | 3% | -51% | -82% | -84% |
| 2–5 min | 8108 | 41 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6385 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9533 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1861 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1850 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1849 | 9 | 5% | 2% | -40% | -83% | -82% |
| ETH | 1840 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1839 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1836 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1830 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1825 | 10 | 6% | 3% | -29% | -79% | -79% |
| BTC | 1825 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 965 | 1 | 3% | 1% | -88% | -93% | -95% |
| SILVER | 932 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 907 | 3 | 3% | 1% | -61% | -94% | -95% |
| COPPER | 809 | 3 | 2% | 1% | -65% | -74% | -74% |
| PLATINUM | 800 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 741 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 738 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 729 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 695 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 644 | 3 | 1% | 1% | -57% | -99% | -98% |
| AUDUSD | 268 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 216 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12623 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12376 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2801 | 15 | 2% | 1% | -10% | -77% | -76% |
| 0.05–0.1% | 2880 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4187 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4823 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1861 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6416 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,794 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 5:41:01 AM | HYPE | DOWN | 4.0 min | +0.472% | — | In play | — |
| 10/20 5:41:01 AM | ETH | DOWN | 4.0 min | +0.238% | — | In play | — |
| 10/20 5:41:01 AM | BNB | DOWN | 4.0 min | +0.129% | — | In play | — |
| 10/20 5:41:01 AM | BTC | DOWN | 4.0 min | +0.185% | — | In play | — |
| 10/20 5:40:12 AM | XRP | DOWN | 4.8 min | +0.316% | — | In play | — |
| 10/20 5:39:56 AM | DOGE | DOWN | 5.1 min | +0.166% | — | In play | — |
| 10/20 5:29:57 AM | NEAR | UP | 2 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:29:41 AM | PALLADIUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:29:41 AM | EURUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:29:09 AM | SOL | UP | 51 sec | -0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:28:38 AM | DOGE | UP | 81 sec | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:28:38 AM | XRP | DOWN | 81 sec | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:28:22 AM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:28:22 AM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:28:06 AM | BTC | UP | 1.9 min | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:26:14 AM | WTI | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:26:14 AM | ETH | UP | 3.8 min | -0.190% | 4¢ | ❌ Lost | $0.00 |
| 10/20 5:26:14 AM | ZEC | UP | 3.8 min | -0.537% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:24:23 AM | HYPE | UP | 5.6 min | -0.395% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:56 AM | PLATINUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:24 AM | COPPER | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:24 AM | GOLD | DOWN | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:14:09 AM | ETH | DOWN | 50 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:14:09 AM | BTC | DOWN | 50 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:14:09 AM | SOL | DOWN | 50 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:13:19 AM | USDCAD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:13:19 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:13:19 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:13:04 AM | AUDUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:13:04 AM | BNB | UP | 1.9 min | -0.052% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
