# 15-Minute 1¢ Study

*Updated Mon Oct 19, 10:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2029 finished bets | 1% | $94.30 | +41% | +4.65¢ | $29.45 / $64.85 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1870 | $74.20 | +36% |
| Momentum model ≥ 2%, hold to the close | 3112 | -$0.50 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 2029 | -$22.70 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23952 | 23945 | 90 (0%) | 1.07% | -$1,646.85 (-57%) | Hold to the close: -$1,646.85 (-57%) |

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
| Volatility model | 15756 | 4.6% | 0.4% (64) | -660% | ❌ Worse |
| Momentum model | 15756 | 4.5% | 0.4% (64) | -682% | ❌ Worse |
| Mean-reversion model | 15756 | 7.7% | 0.4% (64) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15756 | 64 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3671 | 30 | -6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2029 | 23 | +41% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1187 | 15 | +77% | -58% | -57% | -54% |
| Momentum model ≥ 2% | 3112 | 26 | -0% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1870 | 20 | +36% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1240 | 13 | +44% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6127 | 41 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4260 | 33 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2820 | 22 | -11% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15954 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5589 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2402 | 1% | 1% | 1% | 0% | 0% | 0% |
| **All** | 23945 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,646.85 | -57% | — |
| Sell at 2¢ | 859 | 4% | -$2,571.51 | -88% | 46 sec |
| Sell at 3¢ | 583 | 2% | -$2,567.48 | -88% | 47 sec |
| Sell at 5¢ | 418 | 2% | -$2,523.15 | -87% | 50 sec |
| Sell at 10¢ | 254 | 1% | -$2,434.11 | -84% | 64 sec |
| Sell at 25¢ | 141 | 1% | -$2,244.14 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,013.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 887 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7802 | 40 | 7% | 3% | -49% | -88% | -88% |
| 1–2 min | 6136 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 9116 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1793 | 11 | 4% | 2% | -24% | -90% | -90% |
| HYPE | 1783 | 6 | 5% | 2% | -59% | -90% | -88% |
| BNB | 1781 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1774 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1772 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1768 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1764 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1760 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1759 | 10 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 916 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 886 | 4 | 3% | 1% | -48% | -80% | -80% |
| WTI | 859 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 774 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 760 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 703 | 3 | 2% | 1% | -60% | -83% | -82% |
| NATGAS | 701 | 5 | 2% | 2% | -33% | -83% | -82% |
| PALLADIUM | 693 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 654 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 612 | 3 | 1% | 0% | -54% | -99% | -98% |
| AUDUSD | 239 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 194 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12053 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11892 | 47 | 3% | 1% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2711 | 15 | 2% | 1% | -8% | -76% | -75% |
| 0.05–0.1% | 2772 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 4011 | 13 | 4% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4650 | 22 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1807 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5739 | 29 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,803 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 10:44:53 AM | GOLD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:53 AM | ETH | DOWN | 6 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:44:53 AM | BNB | DOWN | 6 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:44:53 AM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:53 AM | PLATINUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:37 AM | NATGAS | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:37 AM | WTI | UP | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:44:21 AM | DOGE | UP | 38 sec | -0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:44:21 AM | BTC | UP | 38 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:44:21 AM | USDCAD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:43:48 AM | HYPE | UP | 72 sec | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:43:48 AM | SOL | UP | 72 sec | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:43:48 AM | XRP | UP | 72 sec | -0.200% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:43:48 AM | ZEC | UP | 72 sec | -0.308% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:43:32 AM | NEAR | UP | 88 sec | -0.436% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:43:16 AM | USDJPY | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:29:51 AM | GOLD | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:29:51 AM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:29:51 AM | HYPE | UP | 9 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:29:51 AM | SOL | UP | 9 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:29:51 AM | AUDUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:29:35 AM | BTC | DOWN | 25 sec | +0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:29:35 AM | GBPUSD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:29:19 AM | WTI | DOWN | 41 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:29:04 AM | XRP | DOWN | 55 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:28:48 AM | SILVER | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:28:48 AM | DOGE | DOWN | 72 sec | +0.192% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:28:48 AM | COPPER | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:28:48 AM | EURUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:28:48 AM | NEAR | DOWN | 72 sec | +0.498% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
