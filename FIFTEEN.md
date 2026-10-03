# 15-Minute 1¢ Study

*Updated Sat Oct 3, 2:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **33 buys a day** (~$4.90/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 414 | -$1.80 | -4% |
| Momentum model ≥ 5%, sell at 50¢ | 414 | -$9.05 | -21% |
| 5+ min left, sell at 50¢ | 171 | -$11.70 | -46% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6354 | 6348 | 23 (0%) | 1.07% | -$445.55 (-58%) | Hold to the close: -$445.55 (-58%) |

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
| Volatility model | 3812 | 4.0% | 0.3% (11) | -733% | ❌ Worse |
| Momentum model | 3812 | 4.1% | 0.3% (11) | -773% | ❌ Worse |
| Mean-reversion model | 3812 | 7.0% | 0.3% (11) | -894% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3812 | 11 | -63% | -86% | -87% | -84% |
| Volatility model ≥ 2% | 804 | 5 | -28% | -66% | -67% | -62% |
| Volatility model ≥ 5% | 413 | 2 | -37% | -46% | -48% | -43% |
| Volatility model ≥ 10% | 246 | 2 | +24% | -15% | -19% | -12% |
| Momentum model ≥ 2% | 705 | 4 | -31% | -66% | -69% | -65% |
| Momentum model ≥ 5% | 414 | 3 | -4% | -51% | -56% | -50% |
| Momentum model ≥ 10% | 281 | 2 | +4% | -33% | -36% | -31% |
| Mean-reversion model ≥ 2% | 1434 | 7 | -47% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 959 | 6 | -31% | -80% | -82% | -75% |
| Mean-reversion model ≥ 10% | 625 | 4 | -26% | -77% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4009 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6348 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$445.55 | -58% | — |
| Sell at 2¢ | 250 | 4% | -$688.55 | -90% | 43 sec |
| Sell at 3¢ | 156 | 2% | -$692.71 | -90% | 48 sec |
| Sell at 5¢ | 116 | 2% | -$678.15 | -88% | 64 sec |
| Sell at 10¢ | 77 | 1% | -$638.68 | -83% | 81 sec |
| Sell at 25¢ | 41 | 1% | -$589.84 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$541.80 | -71% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 2072 | 12 | 8% | 3% | -43% | -86% | -87% |
| 1–2 min | 1650 | 6 | 3% | 2% | -61% | -94% | -93% |
| Under 1 min | 2455 | 3 | 1% | 0% | -82% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 452 | 2 | 4% | 1% | -41% | -90% | -91% |
| ZEC | 449 | 2 | 5% | 3% | -47% | -89% | -90% |
| ETH | 448 | 2 | 6% | 3% | -44% | -85% | -85% |
| HYPE | 448 | 2 | 5% | 4% | -45% | -88% | -86% |
| BTC | 444 | 1 | 6% | 3% | -71% | -85% | -89% |
| SOL | 443 | 0 | 3% | 1% | -100% | -93% | -92% |
| BNB | 443 | 0 | 4% | 2% | -100% | -90% | -92% |
| XRP | 442 | 3 | 2% | 1% | -12% | -67% | -67% |
| NEAR | 440 | 1 | 6% | 2% | -69% | -85% | -87% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3228 | 14 | 4% | 2% | -49% | -91% | -91% |
| DOWN (bought NO) | 3120 | 9 | 4% | 2% | -67% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 527 | 2 | 1% | 1% | -29% | -60% | -60% |
| 0.05–0.1% | 599 | 0 | 3% | 1% | -100% | -91% | -94% |
| 0.1–0.2% | 982 | 2 | 4% | 2% | -73% | -90% | -91% |
| 0.2–0.5% | 1308 | 5 | 6% | 3% | -57% | -88% | -87% |
| Over 0.5% | 591 | 4 | 7% | 3% | -30% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1545 | 5 | 4% | 1% | -63% | -91% | -93% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,292 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 2:14:30 AM | SOL | DOWN | 30 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:14:14 AM | DOGE | DOWN | 46 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:13:58 AM | XRP | DOWN | 62 sec | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:13:58 AM | ETH | DOWN | 62 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:13:42 AM | HYPE | DOWN | 77 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:13:26 AM | ZEC | DOWN | 1.6 min | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:12:54 AM | BTC | DOWN | 2.1 min | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:12:39 AM | NEAR | DOWN | 2.4 min | +0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:59:56 AM | BNB | UP | 4 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:59:40 AM | BTC | DOWN | 19 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:59:24 AM | ZEC | DOWN | 35 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:59:08 AM | DOGE | DOWN | 51 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:58:52 AM | ETH | DOWN | 68 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:58:52 AM | NEAR | UP | 68 sec | -0.409% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:58:04 AM | HYPE | DOWN | 1.9 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:57:14 AM | XRP | DOWN | 2.8 min | +0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:57:14 AM | SOL | DOWN | 2.8 min | +0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:44:39 AM | ETH | DOWN | 21 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:44:23 AM | BTC | UP | 37 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:43:51 AM | SOL | UP | 68 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:43:19 AM | ZEC | UP | 1.7 min | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:42:48 AM | NEAR | UP | 2.2 min | -0.402% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:42:32 AM | BNB | UP | 2.5 min | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:42:16 AM | DOGE | UP | 2.7 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:42:16 AM | XRP | UP | 2.7 min | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:29:44 AM | BTC | DOWN | 16 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:29:28 AM | ETH | UP | 32 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:29:28 AM | BNB | DOWN | 32 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:29:28 AM | ZEC | DOWN | 32 sec | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:29:12 AM | XRP | UP | 48 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
