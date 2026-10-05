# 15-Minute 1¢ Study

*Updated Mon Oct 5, 11:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 607 finished bets | 1% | $32.45 | +50% | +5.35¢ | -$5.30 / $37.75 |

*Expect about **81 buys a day** (~$12.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 608 | $19.05 | +29% |
| Volatility model ≥ 2%, hold to the close | 1133 | $17.20 | +13% |
| 5+ min left, hold to the close | 224 | $8.85 | +27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8712 | 8701 | 37 (0%) | 1.07% | -$529.60 (-51%) | Hold to the close: -$529.60 (-51%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5731 | 4.1% | 0.4% (25) | -604% | ❌ Worse |
| Momentum model | 5731 | 4.2% | 0.4% (25) | -629% | ❌ Worse |
| Mean-reversion model | 5731 | 6.8% | 0.4% (25) | -708% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5731 | 25 | -45% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1133 | 11 | +13% | -70% | -70% | -65% |
| Volatility model ≥ 5% | 607 | 7 | +50% | -57% | -56% | -52% |
| Volatility model ≥ 10% | 375 | 5 | +97% | -37% | -39% | -33% |
| Momentum model ≥ 2% | 998 | 8 | -3% | -71% | -73% | -70% |
| Momentum model ≥ 5% | 608 | 6 | +29% | -62% | -64% | -61% |
| Momentum model ≥ 10% | 420 | 5 | +70% | -49% | -50% | -47% |
| Mean-reversion model ≥ 2% | 1995 | 14 | -24% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1338 | 12 | -0% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 883 | 9 | +18% | -78% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5928 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2097 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 676 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 8701 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$529.60 | -51% | — |
| Sell at 2¢ | 335 | 4% | -$932.50 | -89% | 33 sec |
| Sell at 3¢ | 218 | 3% | -$934.58 | -89% | 47 sec |
| Sell at 5¢ | 161 | 2% | -$914.95 | -87% | 61 sec |
| Sell at 10¢ | 107 | 1% | -$865.43 | -83% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$782.31 | -75% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$692.60 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 221 | 3 | 11% | 3% | +28% | -81% | -88% |
| 2–5 min | 2832 | 20 | 7% | 3% | -31% | -87% | -87% |
| 1–2 min | 2291 | 9 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 3354 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 670 | 5 | 5% | 3% | -11% | -89% | -89% |
| DOGE | 662 | 2 | 4% | 2% | -61% | -91% | -90% |
| ETH | 661 | 5 | 6% | 3% | -5% | -87% | -87% |
| HYPE | 661 | 3 | 5% | 3% | -45% | -89% | -87% |
| BNB | 657 | 2 | 4% | 2% | -64% | -90% | -92% |
| XRP | 656 | 4 | 2% | 1% | -23% | -77% | -77% |
| SOL | 656 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 654 | 3 | 6% | 2% | -40% | -87% | -89% |
| NEAR | 651 | 3 | 6% | 3% | -40% | -64% | -66% |
| GOLD | 353 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 338 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 322 | 2 | 3% | 1% | -34% | -94% | -96% |
| COPPER | 298 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 267 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 262 | 2 | 3% | 2% | -29% | -94% | -92% |
| PALLADIUM | 257 | 1 | 2% | 1% | -64% | -97% | -98% |
| EURUSD | 241 | 1 | 5% | 3% | -61% | -92% | -90% |
| GBPUSD | 232 | 1 | 3% | 2% | -60% | -94% | -94% |
| USDJPY | 203 | 3 | 2% | 1% | +38% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4400 | 20 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4301 | 17 | 4% | 2% | -54% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 973 | 7 | 2% | 1% | +22% | -59% | -58% |
| 0.05–0.1% | 987 | 2 | 3% | 1% | -70% | -91% | -92% |
| 0.1–0.2% | 1480 | 6 | 4% | 2% | -48% | -91% | -91% |
| 0.2–0.5% | 1756 | 8 | 6% | 3% | -50% | -88% | -87% |
| Over 0.5% | 730 | 4 | 7% | 3% | -44% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2328 | 17 | 5% | 3% | -17% | -90% | -88% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,125 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 11:43:18 AM | NATGAS | DOWN | 1.7 min | — | — | In play | — |
| 10/5 11:43:02 AM | HYPE | DOWN | 2.0 min | +0.221% | — | In play | — |
| 10/5 11:42:12 AM | WTI | UP | 2.8 min | — | — | In play | — |
| 10/5 11:41:57 AM | ZEC | DOWN | 3.0 min | +0.498% | — | In play | — |
| 10/5 11:40:53 AM | COPPER | UP | 4.1 min | — | — | In play | — |
| 10/5 11:29:59 AM | WTI | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:29:59 AM | GOLD | DOWN | 0 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:29:59 AM | COPPER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:29:43 AM | PLATINUM | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:29:43 AM | HYPE | DOWN | 16 sec | +0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:28:55 AM | NATGAS | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:27:52 AM | DOGE | DOWN | 2.1 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:27:36 AM | EURUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:27:20 AM | GBPUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:27:20 AM | BNB | DOWN | 2.6 min | +0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/5 11:27:04 AM | ETH | DOWN | 2.9 min | +0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:26:48 AM | BTC | DOWN | 3.2 min | +0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:26:48 AM | SOL | DOWN | 3.2 min | +0.210% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:25:12 AM | ZEC | DOWN | 4.8 min | +0.822% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:25:12 AM | XRP | DOWN | 4.8 min | +0.308% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:25:12 AM | NEAR | DOWN | 4.8 min | +0.645% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:14:21 AM | WTI | UP | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:14:21 AM | COPPER | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:13:47 AM | XRP | UP | 73 sec | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:13:31 AM | SOL | UP | 89 sec | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:13:15 AM | ETH | UP | 1.8 min | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:13:00 AM | ZEC | UP | 2.0 min | -0.258% | 4¢ | ❌ Lost | -$0.15 |
| 10/5 11:13:00 AM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:13:00 AM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:12:44 AM | SILVER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
