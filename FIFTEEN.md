# 15-Minute 1¢ Study

*Updated Mon Oct 12, 1:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1174 finished bets | 1% | $40.80 | +32% | +3.48¢ | $35.00 / $5.80 |

*Expect about **84 buys a day** (~$12.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1125 | $20.00 | +17% |
| 5+ min left, hold to the close | 418 | -$5.80 | -9% |
| Volatility model ≥ 2%, hold to the close | 2061 | -$9.20 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15336 | 15319 | 62 (0%) | 1.07% | -$978.50 (-53%) | Hold to the close: -$978.50 (-53%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 10226 | 4.5% | 0.4% (45) | -662% | ❌ Worse |
| Momentum model | 10226 | 4.5% | 0.4% (45) | -689% | ❌ Worse |
| Mean-reversion model | 10226 | 7.2% | 0.4% (45) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10226 | 45 | -45% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2061 | 17 | -4% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1174 | 12 | +32% | -71% | -70% | -68% |
| Volatility model ≥ 10% | 742 | 8 | +57% | -61% | -61% | -58% |
| Momentum model ≥ 2% | 1814 | 14 | -6% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1125 | 10 | +17% | -75% | -75% | -72% |
| Momentum model ≥ 10% | 779 | 7 | +29% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3588 | 26 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2447 | 20 | -9% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1642 | 14 | -1% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10424 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3611 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1284 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15319 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$978.50 | -53% | — |
| Sell at 2¢ | 526 | 3% | -$1,667.74 | -90% | 33 sec |
| Sell at 3¢ | 349 | 2% | -$1,668.39 | -90% | 47 sec |
| Sell at 5¢ | 258 | 2% | -$1,636.80 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,553.80 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,430.74 | -77% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,274.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 414 | 4 | 10% | 3% | -8% | -82% | -86% |
| 2–5 min | 4928 | 32 | 6% | 3% | -36% | -88% | -88% |
| 1–2 min | 4042 | 16 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5931 | 10 | 1% | 0% | -75% | -91% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1171 | 7 | 4% | 3% | -26% | -90% | -90% |
| HYPE | 1168 | 4 | 4% | 2% | -57% | -90% | -89% |
| DOGE | 1161 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1160 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1157 | 8 | 5% | 3% | -16% | -89% | -89% |
| SOL | 1157 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1154 | 5 | 5% | 2% | -42% | -88% | -91% |
| NEAR | 1148 | 7 | 5% | 3% | -20% | -75% | -76% |
| XRP | 1148 | 7 | 2% | 1% | -24% | -84% | -84% |
| GOLD | 594 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 580 | 1 | 3% | 1% | -80% | -94% | -94% |
| WTI | 555 | 3 | 3% | 1% | -39% | -94% | -96% |
| COPPER | 515 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 479 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 447 | 3 | 3% | 2% | -37% | -95% | -94% |
| PALLADIUM | 441 | 1 | 1% | 0% | -79% | -98% | -99% |
| EURUSD | 433 | 3 | 3% | 2% | -35% | -74% | -72% |
| GBPUSD | 412 | 1 | 2% | 1% | -77% | -96% | -96% |
| USDJPY | 373 | 3 | 1% | 1% | -25% | -98% | -97% |
| USDCAD | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7671 | 34 | 3% | 2% | -49% | -90% | -89% |
| DOWN (bought NO) | 7648 | 28 | 3% | 2% | -57% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1891 | 9 | 2% | 1% | -20% | -76% | -76% |
| 0.05–0.1% | 1855 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2672 | 9 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2869 | 18 | 6% | 3% | -31% | -89% | -88% |
| Over 0.5% | 1134 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3770 | 20 | 4% | 2% | -39% | -86% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,543 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 1:14:37 AM | NEAR | UP | 22 sec | -0.185% | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:14:05 AM | BTC | DOWN | 54 sec | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:14:05 AM | USDJPY | DOWN | 54 sec | — | 0¢ | In play | — |
| 10/12 1:13:49 AM | ZEC | DOWN | 71 sec | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:13:18 AM | DOGE | DOWN | 1.7 min | +0.217% | 1¢ | In play | — |
| 10/12 1:13:18 AM | COPPER | DOWN | 1.7 min | — | 0¢ | In play | — |
| 10/12 1:13:18 AM | XRP | DOWN | 1.7 min | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:13:18 AM | HYPE | DOWN | 1.7 min | +0.157% | 0¢ | In play | — |
| 10/12 1:13:02 AM | NATGAS | UP | 2.0 min | — | 0¢ | In play | — |
| 10/12 1:13:02 AM | SOL | DOWN | 2.0 min | +0.178% | 1¢ | In play | — |
| 10/12 1:13:02 AM | GBPUSD | UP | 2.0 min | — | 0¢ | In play | — |
| 10/12 1:12:45 AM | BNB | DOWN | 2.2 min | +0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:12:45 AM | ETH | DOWN | 2.2 min | +0.165% | 1¢ | In play | — |
| 10/12 1:12:13 AM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | In play | — |
| 10/12 1:11:57 AM | SILVER | DOWN | 3.0 min | — | 1¢ | In play | — |
| 10/12 12:59:54 AM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 12:59:54 AM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:59:38 AM | USDCAD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:59:22 AM | NEAR | UP | 38 sec | -0.351% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:59:06 AM | WTI | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:59:06 AM | HYPE | UP | 54 sec | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:57:48 AM | PALLADIUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:56:44 AM | ZEC | DOWN | 3.2 min | +0.563% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:56:44 AM | SOL | DOWN | 3.2 min | +0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:56:28 AM | DOGE | DOWN | 3.5 min | +0.370% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:56:12 AM | XRP | DOWN | 3.8 min | +0.362% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:55:56 AM | BNB | DOWN | 4.1 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:55:41 AM | ETH | DOWN | 4.3 min | +0.221% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:55:22 AM | BTC | DOWN | 4.6 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:44:54 AM | WTI | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
