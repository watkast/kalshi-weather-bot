# 15-Minute 1¢ Study

*Updated Mon Oct 5, 4:13 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 583 finished bets | 1% | $35.30 | +56% | +6.05¢ | -$17.80 / $53.10 |

*Expect about **82 buys a day** (~$12.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1084 | $23.35 | +18% |
| Momentum model ≥ 5%, hold to the close | 584 | $21.90 | +35% |
| 5+ min left, hold to the close | 211 | $10.80 | +35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8323 | 8314 | 37 (0%) | 1.07% | -$480.55 (-48%) | Hold to the close: -$480.55 (-48%) |

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
| Volatility model | 5504 | 4.2% | 0.5% (25) | -599% | ❌ Worse |
| Momentum model | 5504 | 4.2% | 0.5% (25) | -626% | ❌ Worse |
| Mean-reversion model | 5504 | 6.9% | 0.5% (25) | -698% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5504 | 25 | -43% | -85% | -85% | -82% |
| Volatility model ≥ 2% | 1084 | 11 | +18% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 583 | 7 | +56% | -55% | -54% | -50% |
| Volatility model ≥ 10% | 364 | 5 | +103% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 953 | 8 | +2% | -70% | -72% | -69% |
| Momentum model ≥ 5% | 584 | 6 | +35% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 407 | 5 | +76% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1917 | 14 | -20% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1285 | 12 | +4% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 852 | 9 | +22% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5701 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1981 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 632 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8314 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$480.55 | -48% | — |
| Sell at 2¢ | 327 | 4% | -$885.53 | -89% | 33 sec |
| Sell at 3¢ | 212 | 3% | -$887.87 | -89% | 48 sec |
| Sell at 5¢ | 157 | 2% | -$868.50 | -87% | 61 sec |
| Sell at 10¢ | 105 | 1% | -$819.00 | -82% | 66 sec |
| Sell at 25¢ | 58 | 1% | -$736.57 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$643.55 | -64% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 208 | 3 | 12% | 3% | +37% | -80% | -87% |
| 2–5 min | 2680 | 20 | 8% | 4% | -27% | -86% | -87% |
| 1–2 min | 2199 | 9 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 3224 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 645 | 5 | 5% | 3% | -8% | -89% | -89% |
| ETH | 636 | 5 | 6% | 3% | -1% | -86% | -86% |
| DOGE | 636 | 2 | 4% | 2% | -59% | -90% | -90% |
| HYPE | 635 | 3 | 5% | 3% | -42% | -88% | -86% |
| BNB | 634 | 2 | 4% | 2% | -62% | -91% | -93% |
| SOL | 631 | 0 | 3% | 1% | -100% | -92% | -91% |
| XRP | 630 | 4 | 2% | 1% | -19% | -76% | -76% |
| BTC | 628 | 3 | 6% | 2% | -37% | -86% | -90% |
| NEAR | 626 | 3 | 7% | 3% | -37% | -63% | -64% |
| GOLD | 336 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 323 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 304 | 2 | 3% | 1% | -30% | -95% | -96% |
| COPPER | 281 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 249 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 247 | 2 | 3% | 2% | -24% | -94% | -93% |
| PALLADIUM | 241 | 1 | 2% | 1% | -61% | -96% | -98% |
| EURUSD | 227 | 1 | 5% | 3% | -59% | -92% | -90% |
| GBPUSD | 216 | 1 | 4% | 2% | -57% | -94% | -94% |
| USDJPY | 189 | 3 | 2% | 2% | +48% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4195 | 20 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 4119 | 17 | 4% | 2% | -52% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 951 | 7 | 2% | 1% | +25% | -58% | -57% |
| 0.05–0.1% | 960 | 2 | 3% | 1% | -69% | -91% | -92% |
| 0.1–0.2% | 1419 | 6 | 4% | 2% | -46% | -90% | -91% |
| 0.2–0.5% | 1674 | 8 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 695 | 4 | 7% | 3% | -41% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2111 | 9 | 4% | 2% | -51% | -85% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,171 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 4:13:20 AM | NATGAS | DOWN | 1.6 min | — | — | In play | — |
| 10/5 4:12:13 AM | PALLADIUM | UP | 2.8 min | — | — | In play | — |
| 10/5 4:10:45 AM | XRP | DOWN | 4.2 min | +0.318% | — | In play | — |
| 10/5 3:59:45 AM | BNB | DOWN | 15 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:59:27 AM | PLATINUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:59:23 AM | ETH | UP | 37 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:59:21 AM | GBPUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:58:58 AM | XRP | UP | 62 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:58:19 AM | NEAR | UP | 1.7 min | -0.444% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:58:01 AM | SILVER | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:57:41 AM | ZEC | UP | 2.3 min | -0.380% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:56:08 AM | HYPE | UP | 3.9 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:44:51 AM | SOL | DOWN | 9 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:44:41 AM | BNB | DOWN | 19 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:44:33 AM | BTC | DOWN | 27 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:44:25 AM | XRP | DOWN | 35 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:44:17 AM | HYPE | UP | 43 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:43:49 AM | NATGAS | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:43:21 AM | WTI | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:43:11 AM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:43:05 AM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:42:39 AM | GOLD | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:42:25 AM | SILVER | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:42:13 AM | ZEC | UP | 2.8 min | -0.512% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:42:03 AM | EURUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:42:01 AM | NEAR | UP | 3.0 min | -0.471% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 3:29:53 AM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:29:20 AM | XRP | UP | 39 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/5 3:29:10 AM | USDJPY | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 3:29:02 AM | BTC | UP | 57 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
