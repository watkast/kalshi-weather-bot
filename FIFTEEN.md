# 15-Minute 1¢ Study

*Updated Tue Nov 3, 7:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3606 finished bets | 1% | $115.10 | +29% | +3.19¢ | $79.60 / $35.50 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3341 | $42.55 | +12% |
| Volatility model ≥ 2%, hold to the close | 6669 | $33.45 | +4% |
| Momentum model ≥ 2%, hold to the close | 5502 | -$47.40 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44573 | 44563 | 165 (0%) | 1.07% | -$3,116.55 (-57%) | Hold to the close: -$3,116.55 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27387 | 4.7% | 0.4% (107) | -680% | ❌ Worse |
| Momentum model | 27387 | 4.6% | 0.4% (107) | -705% | ❌ Worse |
| Mean-reversion model | 27387 | 8.1% | 0.4% (107) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27387 | 107 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6669 | 60 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3606 | 37 | +29% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2046 | 22 | +54% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5502 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3341 | 29 | +12% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2180 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11322 | 77 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7946 | 66 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5321 | 47 | +0% | -80% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27592 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10545 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6426 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44563 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,116.55 | -57% | — |
| Sell at 2¢ | 1756 | 4% | -$4,731.99 | -87% | 47 sec |
| Sell at 3¢ | 1202 | 3% | -$4,719.77 | -87% | 49 sec |
| Sell at 5¢ | 833 | 2% | -$4,619.10 | -85% | 63 sec |
| Sell at 10¢ | 502 | 1% | -$4,418.93 | -81% | 66 sec |
| Sell at 25¢ | 263 | 1% | -$4,094.02 | -75% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,725.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2157 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14330 | 79 | 7% | 3% | -46% | -86% | -86% |
| 1–2 min | 11244 | 39 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 16821 | 38 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3091 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3084 | 11 | 4% | 2% | -55% | -90% | -90% |
| BNB | 3078 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3077 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3065 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3062 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3048 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3048 | 14 | 5% | 2% | -38% | -88% | -89% |
| XRP | 3039 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1636 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1593 | 7 | 5% | 2% | -48% | -82% | -81% |
| WTI | 1592 | 5 | 3% | 1% | -62% | -92% | -93% |
| PLATINUM | 1424 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1366 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1346 | 6 | 2% | 1% | -58% | -70% | -69% |
| NATGAS | 1296 | 7 | 2% | 1% | -50% | -82% | -81% |
| GBPUSD | 1296 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1274 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1273 | 5 | 2% | 1% | -63% | -97% | -97% |
| AUDUSD | 824 | 4 | 2% | 1% | -55% | -86% | -85% |
| USDCAD | 790 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 384 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 223 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 215 | 2 | 4% | 0% | -13% | -7% | -6% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22664 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21899 | 77 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4480 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4716 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7151 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8180 | 33 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3057 | 12 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 11863 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,718 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 7:29:55 PM | GOLD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:29:55 PM | WTI | UP | 4 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:29:55 PM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:28:54 PM | XRP | UP | 65 sec | -0.096% | 2¢ | ❌ Lost | -$0.15 |
| 11/3 7:28:00 PM | ZEC | UP | 2.0 min | -0.497% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:28:00 PM | ETH | UP | 2.0 min | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:27:42 PM | USDCAD | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:27:42 PM | BRENT | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:27:26 PM | GBPUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:27:26 PM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:27:26 PM | NEAR | UP | 2.6 min | -0.675% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:27:26 PM | SILVER | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:26:39 PM | BTC | UP | 3.3 min | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:26:39 PM | SOL | UP | 3.3 min | -0.441% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:26:23 PM | BNB | UP | 3.6 min | -0.336% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:26:23 PM | DOGE | UP | 3.6 min | -0.451% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 7:25:51 PM | EURUSD | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:25:35 PM | HYPE | UP | 4.4 min | -0.889% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:14:59 PM | WTI | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 7:14:59 PM | SOL | UP | 0 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/3 7:14:43 PM | EURUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:14:27 PM | HYPE | DOWN | 32 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/3 7:14:27 PM | XRP | DOWN | 32 sec | +0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/3 7:14:27 PM | ZEC | DOWN | 32 sec | +0.169% | 0¢ | ❌ Lost | $0.00 |
| 11/3 7:14:27 PM | BNB | DOWN | 32 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/3 7:14:27 PM | DOGE | DOWN | 32 sec | +0.123% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:14:27 PM | NEAR | DOWN | 32 sec | +0.178% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:13:53 PM | BTC | UP | 67 sec | -0.097% | 26¢ | ❌ Lost | -$0.15 |
| 11/3 7:13:53 PM | PALLADIUM | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 7:13:37 PM | GOLD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
