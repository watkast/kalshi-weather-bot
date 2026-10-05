# 15-Minute 1¢ Study

*Updated Mon Oct 5, 3:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 580 finished bets | 1% | $35.45 | +57% | +6.11¢ | -$17.80 / $53.25 |

*Expect about **81 buys a day** (~$12.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1081 | $23.50 | +18% |
| Momentum model ≥ 5%, hold to the close | 583 | $21.90 | +35% |
| 5+ min left, hold to the close | 211 | $10.80 | +35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8297 | 8291 | 37 (0%) | 1.07% | -$478.00 (-48%) | Hold to the close: -$478.00 (-48%) |

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
| Volatility model | 5491 | 4.2% | 0.5% (25) | -594% | ❌ Worse |
| Momentum model | 5491 | 4.2% | 0.5% (25) | -623% | ❌ Worse |
| Mean-reversion model | 5491 | 6.9% | 0.5% (25) | -693% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5491 | 25 | -43% | -85% | -85% | -82% |
| Volatility model ≥ 2% | 1081 | 11 | +18% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 580 | 7 | +57% | -55% | -54% | -50% |
| Volatility model ≥ 10% | 362 | 5 | +103% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 949 | 8 | +2% | -69% | -72% | -69% |
| Momentum model ≥ 5% | 583 | 6 | +35% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 406 | 5 | +76% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1912 | 14 | -20% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1280 | 12 | +4% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 850 | 9 | +22% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5688 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1974 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 629 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8291 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$478.00 | -48% | — |
| Sell at 2¢ | 327 | 4% | -$882.98 | -89% | 33 sec |
| Sell at 3¢ | 212 | 3% | -$885.32 | -89% | 48 sec |
| Sell at 5¢ | 157 | 2% | -$865.95 | -87% | 61 sec |
| Sell at 10¢ | 105 | 1% | -$816.45 | -82% | 66 sec |
| Sell at 25¢ | 58 | 1% | -$734.02 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$641.00 | -64% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 208 | 3 | 12% | 3% | +37% | -80% | -87% |
| 2–5 min | 2673 | 20 | 8% | 4% | -27% | -86% | -86% |
| 1–2 min | 2192 | 9 | 3% | 2% | -55% | -93% | -93% |
| Under 1 min | 3215 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 643 | 5 | 5% | 3% | -7% | -89% | -89% |
| DOGE | 636 | 2 | 4% | 2% | -59% | -90% | -90% |
| ETH | 635 | 5 | 6% | 3% | -1% | -86% | -86% |
| HYPE | 633 | 3 | 5% | 3% | -42% | -88% | -86% |
| BNB | 632 | 2 | 4% | 2% | -62% | -91% | -93% |
| SOL | 630 | 0 | 3% | 1% | -100% | -92% | -91% |
| XRP | 628 | 4 | 2% | 1% | -18% | -76% | -76% |
| BTC | 627 | 3 | 6% | 2% | -37% | -86% | -90% |
| NEAR | 624 | 3 | 7% | 3% | -37% | -63% | -64% |
| GOLD | 335 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 321 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 303 | 2 | 3% | 1% | -30% | -95% | -96% |
| COPPER | 280 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 248 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 246 | 2 | 3% | 2% | -24% | -94% | -93% |
| PALLADIUM | 241 | 1 | 2% | 1% | -61% | -96% | -98% |
| EURUSD | 226 | 1 | 5% | 3% | -59% | -92% | -90% |
| GBPUSD | 214 | 1 | 4% | 2% | -56% | -94% | -94% |
| USDJPY | 189 | 3 | 2% | 2% | +48% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4180 | 20 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 4111 | 17 | 4% | 2% | -52% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 948 | 7 | 2% | 1% | +25% | -58% | -57% |
| 0.05–0.1% | 955 | 2 | 3% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1419 | 6 | 4% | 2% | -46% | -90% | -91% |
| 0.2–0.5% | 1670 | 8 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 694 | 4 | 7% | 3% | -41% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2088 | 9 | 4% | 2% | -50% | -85% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,192 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 3:29:53 AM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:29:20 AM | XRP | UP | 39 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:29:10 AM | USDJPY | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:29:02 AM | BTC | UP | 57 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:28:49 AM | SOL | UP | 70 sec | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:28:12 AM | ZEC | DOWN | 1.8 min | +0.253% | 1¢ | ❌ Lost | $0.00 |
| 10/5 3:27:45 AM | NEAR | DOWN | 2.2 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:27:14 AM | HYPE | UP | 2.8 min | -0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:26:58 AM | DOGE | UP | 3.0 min | -0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:26:42 AM | BNB | UP | 3.3 min | -0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:24:20 AM | WTI | UP | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:14:55 AM | PLATINUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:14:55 AM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:14:24 AM | HYPE | UP | 36 sec | -0.182% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:14:24 AM | NATGAS | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:14:24 AM | ZEC | UP | 36 sec | -0.187% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:14:24 AM | BNB | DOWN | 36 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:13:37 AM | GBPUSD | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:13:37 AM | DOGE | UP | 83 sec | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:13:37 AM | XRP | UP | 83 sec | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:13:21 AM | NEAR | UP | 1.6 min | -0.511% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:13:21 AM | WTI | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:13:05 AM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:13:05 AM | ETH | UP | 1.9 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:12:49 AM | SOL | UP | 2.2 min | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:11:14 AM | BTC | UP | 3.8 min | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:59:38 AM | PALLADIUM | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:59:22 AM | COPPER | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:59:06 AM | BTC | UP | 54 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:58:50 AM | GOLD | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
