# 15-Minute 1¢ Study

*Updated Mon Oct 12, 4:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1182 finished bets | 1% | $39.75 | +31% | +3.36¢ | $34.40 / $5.35 |

*Expect about **83 buys a day** (~$12.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1133 | $18.95 | +16% |
| 5+ min left, hold to the close | 423 | -$6.55 | -10% |
| Volatility model ≥ 2%, hold to the close | 2080 | -$11.90 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15534 | 15527 | 62 (0%) | 1.07% | -$1,005.20 (-54%) | Hold to the close: -$1,005.20 (-54%) |

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
| Volatility model | 10344 | 4.5% | 0.4% (45) | -666% | ❌ Worse |
| Momentum model | 10344 | 4.5% | 0.4% (45) | -692% | ❌ Worse |
| Mean-reversion model | 10344 | 7.2% | 0.4% (45) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10344 | 45 | -45% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2080 | 17 | -5% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1182 | 12 | +31% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 747 | 8 | +56% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1829 | 14 | -7% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1133 | 10 | +16% | -75% | -76% | -72% |
| Momentum model ≥ 10% | 784 | 7 | +28% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3622 | 26 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2475 | 20 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1655 | 14 | -2% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10542 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3683 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1302 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15527 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,005.20 | -54% | — |
| Sell at 2¢ | 532 | 3% | -$1,692.88 | -90% | 33 sec |
| Sell at 3¢ | 354 | 2% | -$1,693.14 | -90% | 46 sec |
| Sell at 5¢ | 259 | 2% | -$1,662.85 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,580.50 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,457.44 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,301.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 419 | 4 | 11% | 3% | -10% | -82% | -86% |
| 2–5 min | 4998 | 32 | 6% | 3% | -37% | -88% | -88% |
| 1–2 min | 4100 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6006 | 10 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1183 | 7 | 4% | 3% | -27% | -90% | -90% |
| HYPE | 1182 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1174 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1172 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1171 | 8 | 5% | 2% | -17% | -89% | -89% |
| SOL | 1171 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1167 | 5 | 5% | 2% | -43% | -88% | -90% |
| NEAR | 1161 | 7 | 5% | 2% | -21% | -76% | -76% |
| XRP | 1161 | 7 | 2% | 1% | -25% | -84% | -84% |
| GOLD | 603 | 0 | 3% | 1% | -100% | -92% | -94% |
| SILVER | 591 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 567 | 3 | 3% | 1% | -40% | -94% | -96% |
| COPPER | 528 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 488 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 453 | 3 | 3% | 2% | -38% | -95% | -94% |
| PALLADIUM | 453 | 1 | 1% | 0% | -79% | -98% | -98% |
| EURUSD | 437 | 3 | 3% | 2% | -36% | -74% | -73% |
| GBPUSD | 419 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 379 | 3 | 1% | 1% | -26% | -98% | -97% |
| USDCAD | 35 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7802 | 34 | 3% | 2% | -49% | -90% | -89% |
| DOWN (bought NO) | 7725 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1900 | 9 | 2% | 1% | -21% | -76% | -76% |
| 0.05–0.1% | 1880 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2707 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2912 | 18 | 6% | 3% | -32% | -89% | -88% |
| Over 0.5% | 1140 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3978 | 20 | 4% | 2% | -42% | -86% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,516 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 4:29:55 AM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:55 AM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:29:55 AM | DOGE | DOWN | 5 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:29:40 AM | WTI | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:24 AM | BTC | UP | 36 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:29:08 AM | USDJPY | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:08 AM | BNB | UP | 52 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:29:08 AM | COPPER | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:08 AM | HYPE | UP | 52 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:08 AM | ETH | UP | 52 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:28:52 AM | SOL | UP | 68 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:28:21 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:28:05 AM | NEAR | UP | 1.9 min | -0.580% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:28:05 AM | ZEC | UP | 1.9 min | -0.312% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:27:18 AM | GOLD | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:27:18 AM | XRP | UP | 2.7 min | -0.242% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:27:02 AM | PALLADIUM | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:14:45 AM | GOLD | DOWN | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:14:45 AM | COPPER | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:14:29 AM | EURUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:14:13 AM | SILVER | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:14:13 AM | XRP | UP | 47 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:13:26 AM | NEAR | UP | 1.6 min | -0.452% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:12:38 AM | SOL | UP | 2.4 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:12:06 AM | BTC | UP | 2.9 min | -0.114% | 7¢ | ❌ Lost | -$0.15 |
| 10/12 4:11:50 AM | DOGE | UP | 3.2 min | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:11:35 AM | ETH | UP | 3.4 min | -0.236% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:11:35 AM | ZEC | UP | 3.4 min | -0.479% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:11:19 AM | BNB | UP | 3.7 min | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:11:03 AM | HYPE | UP | 4.0 min | -0.338% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
