# 15-Minute 1¢ Study

*Updated Mon Sep 28, 5:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 149 finished bets | 2% | $22.50 | +115% | +15.10¢ | $18.40 / $4.10 |

*Expect **150 buys in the first 17 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 47 | $20.95 | +297% |
| Mean-reversion model ≥ 2%, hold to the close | 231 | $12.00 | +40% |
| 2–5 min left, hold to the close | 408 | $11.50 | +20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1208 | 1200 | 8 (1%) | 1.07% | -$33.35 (-23%) | Hold to the close: -$33.35 (-23%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 568 | 3.1% | 0.7% (4) | -315% | ❌ Worse |
| Momentum model | 568 | 3.2% | 0.7% (4) | -391% | ❌ Worse |
| Mean-reversion model | 568 | 6.3% | 0.7% (4) | -348% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 568 | 4 | -10% | -90% | -92% | -89% |
| Volatility model ≥ 2% | 113 | 1 | +3% | -87% | -86% | -81% |
| Volatility model ≥ 5% | 54 | 0 | -100% | -75% | -75% | -68% |
| Volatility model ≥ 10% | 29 | 0 | -100% | -74% | -74% | -57% |
| Momentum model ≥ 2% | 97 | 0 | -100% | -84% | -90% | -89% |
| Momentum model ≥ 5% | 55 | 0 | -100% | -79% | -87% | -79% |
| Momentum model ≥ 10% | 37 | 0 | -100% | -86% | -79% | -65% |
| Mean-reversion model ≥ 2% | 231 | 3 | +40% | -87% | -88% | -85% |
| Mean-reversion model ≥ 5% | 149 | 3 | +115% | -84% | -84% | -77% |
| Mean-reversion model ≥ 10% | 93 | 2 | +139% | -80% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 763 | 4% | 2% | 2% | 2% | 1% | 1% |
| Commodities | 374 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 63 | 3% | 3% | 3% | 3% | 3% | 3% |
| **All** | 1200 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$33.35 | -23% | — |
| Sell at 2¢ | 39 | 3% | -$135.21 | -93% | 47 sec |
| Sell at 3¢ | 24 | 2% | -$135.99 | -94% | 63 sec |
| Sell at 5¢ | 16 | 1% | -$134.95 | -93% | 81 sec |
| Sell at 10¢ | 15 | 1% | -$125.70 | -86% | 1.6 min |
| Sell at 25¢ | 11 | 1% | -$108.94 | -75% | 2.1 min |
| Sell at 50¢ | 8 | 1% | -$91.35 | -63% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 47 | 2 | 6% | 4% | +297% | -89% | -83% |
| 2–5 min | 408 | 5 | 6% | 2% | +20% | -88% | -91% |
| 1–2 min | 361 | 1 | 2% | 1% | -70% | -96% | -97% |
| Under 1 min | 384 | 0 | 1% | 1% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 87 | 2 | 5% | 2% | +183% | -89% | -88% |
| DOGE | 87 | 1 | 5% | 2% | +33% | -90% | -85% |
| ZEC | 86 | 1 | 6% | 1% | +44% | -87% | -96% |
| NEAR | 85 | 0 | 1% | 0% | -100% | -97% | -100% |
| BTC | 85 | 0 | 8% | 2% | -100% | -79% | -87% |
| XRP | 85 | 2 | 5% | 4% | +196% | -89% | -88% |
| SOL | 84 | 0 | 4% | 2% | -100% | -91% | -86% |
| BNB | 84 | 0 | 1% | 0% | -100% | -97% | -96% |
| HYPE | 80 | 0 | 2% | 1% | -100% | -95% | -96% |
| GOLD | 67 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 62 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 61 | 0 | 2% | 0% | -100% | -96% | -94% |
| NATGAS | 51 | 0 | 4% | 2% | -100% | -93% | -90% |
| COPPER | 50 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 46 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 18 | 2 | 11% | 11% | +937% | -81% | -71% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 648 | 5 | 3% | 1% | -9% | -93% | -93% |
| DOWN (bought NO) | 552 | 3 | 3% | 1% | -38% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 72 | 0 | 4% | 3% | -100% | -85% | -85% |
| 0.05–0.1% | 74 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 167 | 0 | 3% | 0% | -100% | -92% | -93% |
| 0.2–0.5% | 307 | 2 | 4% | 2% | -28% | -92% | -93% |
| Over 0.5% | 143 | 4 | 7% | 3% | +204% | -86% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 278 | 1 | 3% | 1% | -60% | -94% | -95% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,958 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 5:12:09 PM | BNB | UP | 2.9 min | -0.151% | — | In play | — |
| 9/28 5:11:53 PM | GOLD | DOWN | 3.1 min | — | — | In play | — |
| 9/28 4:59:52 PM | PLATINUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:59:36 PM | XRP | DOWN | 24 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:59:20 PM | NATGAS | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:59:04 PM | DOGE | DOWN | 56 sec | +0.037% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:59:04 PM | HYPE | UP | 56 sec | -0.133% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:59:04 PM | SILVER | UP | 56 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:33 PM | WTI | DOWN | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:33 PM | USDJPY | DOWN | 87 sec | — | 97¢ | ✅ Won | $13.85 |
| 9/28 4:58:33 PM | BNB | DOWN | 87 sec | +0.012% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:33 PM | GOLD | UP | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:01 PM | ETH | DOWN | 2.0 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:01 PM | BTC | DOWN | 2.0 min | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:01 PM | SOL | DOWN | 2.0 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:56:58 PM | ZEC | DOWN | 3.0 min | +0.430% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:56:27 PM | NEAR | DOWN | 3.5 min | +0.501% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:44:48 PM | COPPER | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:44:33 PM | GOLD | UP | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:43:29 PM | NATGAS | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:43:13 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:42:41 PM | GBPUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:42:26 PM | USDJPY | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:51 PM | DOGE | DOWN | 4.2 min | +0.571% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:51 PM | BNB | DOWN | 4.2 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:51 PM | NEAR | DOWN | 4.2 min | +0.675% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:35 PM | HYPE | DOWN | 4.4 min | +0.355% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:20 PM | XRP | DOWN | 4.7 min | +0.559% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:20 PM | ETH | DOWN | 4.7 min | +0.343% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:20 PM | WTI | DOWN | 4.7 min | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
