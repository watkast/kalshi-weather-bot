# 15-Minute 1¢ Study

*Updated Wed Oct 21, 3:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2219 finished bets | 1% | $85.35 | +34% | +3.85¢ | $47.70 / $37.65 |

*Expect about **96 buys a day** (~$14.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2056 | $66.00 | +29% |
| Volatility model ≥ 2%, hold to the close | 4065 | -$22.30 | -4% |
| Momentum model ≥ 2%, hold to the close | 3428 | -$26.25 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26372 | 26365 | 97 (0%) | 1.07% | -$1,854.70 (-58%) | Hold to the close: -$1,854.70 (-58%) |

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
| Volatility model | 17116 | 4.6% | 0.4% (69) | -665% | ❌ Worse |
| Momentum model | 17116 | 4.6% | 0.4% (69) | -687% | ❌ Worse |
| Mean-reversion model | 17116 | 7.8% | 0.4% (69) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17116 | 69 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4065 | 34 | -4% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2219 | 24 | +34% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1276 | 16 | +75% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 3428 | 27 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2056 | 21 | +29% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1353 | 14 | +41% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6749 | 45 | -27% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4708 | 37 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3122 | 25 | -9% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17314 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6275 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2776 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26365 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 97 | 0% | -$1,854.70 | -58% | — |
| Sell at 2¢ | 958 | 4% | -$2,823.62 | -88% | 46 sec |
| Sell at 3¢ | 652 | 2% | -$2,818.42 | -88% | 48 sec |
| Sell at 5¢ | 461 | 2% | -$2,773.05 | -86% | 56 sec |
| Sell at 10¢ | 280 | 1% | -$2,677.90 | -83% | 64 sec |
| Sell at 25¢ | 152 | 1% | -$2,485.58 | -77% | 80 sec |
| Sell at 50¢ | 99 | 0% | -$2,250.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1060 | 6 | 10% | 4% | -46% | -81% | -84% |
| 2–5 min | 8505 | 43 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6730 | 25 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 10066 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1943 | 11 | 5% | 2% | -30% | -90% | -90% |
| BNB | 1935 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1933 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1925 | 10 | 6% | 3% | -38% | -87% | -86% |
| DOGE | 1923 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1922 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1915 | 7 | 3% | 1% | -55% | -88% | -88% |
| NEAR | 1909 | 11 | 6% | 3% | -26% | -79% | -79% |
| BTC | 1909 | 11 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 1028 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 990 | 4 | 3% | 1% | -53% | -82% | -81% |
| WTI | 968 | 3 | 3% | 1% | -63% | -94% | -95% |
| PLATINUM | 860 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 859 | 3 | 2% | 1% | -67% | -76% | -75% |
| NATGAS | 791 | 5 | 2% | 1% | -41% | -84% | -84% |
| EURUSD | 786 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 779 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 738 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 696 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 303 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 253 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13253 | 49 | 4% | 2% | -58% | -87% | -87% |
| DOWN (bought NO) | 13112 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2905 | 15 | 2% | 1% | -14% | -78% | -77% |
| 0.05–0.1% | 3013 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4399 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5043 | 25 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 1951 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6663 | 28 | 4% | 2% | -52% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,758 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 3:14:54 AM | PLATINUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:14:54 AM | USDCAD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:14:38 AM | NEAR | DOWN | 22 sec | +0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:14:38 AM | NATGAS | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:14:22 AM | HYPE | DOWN | 38 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:14:22 AM | SILVER | DOWN | 38 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 3:13:51 AM | COPPER | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:13:51 AM | GOLD | DOWN | 68 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 3:13:03 AM | USDJPY | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:12:31 AM | BTC | DOWN | 2.5 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 3:12:31 AM | SOL | DOWN | 2.5 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 3:12:31 AM | WTI | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:12:31 AM | BNB | DOWN | 2.5 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 3:12:07 AM | XRP | DOWN | 2.9 min | +0.312% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:11:34 AM | EURUSD | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:10:30 AM | ZEC | DOWN | 4.5 min | +0.421% | 4¢ | ❌ Lost | -$0.15 |
| 10/21 3:10:30 AM | DOGE | DOWN | 4.5 min | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 3:10:30 AM | ETH | DOWN | 4.5 min | +0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 3:10:14 AM | GBPUSD | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:59:52 AM | NEAR | DOWN | 7 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:59:52 AM | XRP | UP | 7 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:59:52 AM | GOLD | UP | 7 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:59:20 AM | BTC | UP | 39 sec | -0.143% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:59:06 AM | GBPUSD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:58:50 AM | ETH | UP | 69 sec | -0.156% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:58:34 AM | SOL | UP | 85 sec | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:58:34 AM | BNB | UP | 85 sec | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:58:34 AM | DOGE | UP | 85 sec | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:57:28 AM | NATGAS | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:57:28 AM | ZEC | UP | 2.5 min | -0.391% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
