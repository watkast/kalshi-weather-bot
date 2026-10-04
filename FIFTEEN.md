# 15-Minute 1¢ Study

*Updated Sun Oct 4, 2:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 188 finished bets | 2% | $14.25 | +51% | +7.58¢ | $14.05 / $0.20 |

*Expect about **28 buys a day** (~$4.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 547 | $11.20 | +19% |
| Volatility model ≥ 2%, hold to the close | 1016 | $3.45 | +3% |
| Mean-reversion model ≥ 5%, hold to the close | 1206 | $2.05 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7593 | 7587 | 34 (0%) | 1.07% | -$433.90 (-48%) | Hold to the close: -$433.90 (-48%) |

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
| Volatility model | 5051 | 4.3% | 0.4% (22) | -636% | ❌ Worse |
| Momentum model | 5051 | 4.3% | 0.4% (22) | -668% | ❌ Worse |
| Mean-reversion model | 5051 | 7.0% | 0.4% (22) | -738% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5051 | 22 | -45% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1016 | 9 | +3% | -68% | -69% | -63% |
| Volatility model ≥ 5% | 547 | 5 | +19% | -54% | -54% | -49% |
| Volatility model ≥ 10% | 341 | 4 | +74% | -33% | -35% | -28% |
| Momentum model ≥ 2% | 893 | 6 | -19% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 550 | 4 | -4% | -60% | -63% | -59% |
| Momentum model ≥ 10% | 380 | 3 | +13% | -47% | -49% | -45% |
| Mean-reversion model ≥ 2% | 1788 | 12 | -27% | -82% | -84% | -78% |
| Mean-reversion model ≥ 5% | 1206 | 11 | +1% | -78% | -79% | -71% |
| Mean-reversion model ≥ 10% | 795 | 8 | +17% | -76% | -77% | -69% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5248 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7587 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 34 | 0% | -$433.90 | -48% | — |
| Sell at 2¢ | 310 | 4% | -$801.30 | -88% | 34 sec |
| Sell at 3¢ | 198 | 3% | -$804.68 | -88% | 48 sec |
| Sell at 5¢ | 146 | 2% | -$787.00 | -86% | 62 sec |
| Sell at 10¢ | 100 | 1% | -$736.90 | -81% | 78 sec |
| Sell at 25¢ | 55 | 1% | -$671.85 | -74% | 1.6 min |
| Sell at 50¢ | 33 | 0% | -$589.15 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 185 | 3 | 12% | 3% | +54% | -78% | -87% |
| 2–5 min | 2445 | 18 | 8% | 4% | -28% | -85% | -86% |
| 1–2 min | 1998 | 8 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 2956 | 5 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 592 | 4 | 5% | 3% | -20% | -88% | -89% |
| DOGE | 588 | 2 | 4% | 2% | -56% | -91% | -91% |
| HYPE | 587 | 2 | 5% | 3% | -59% | -88% | -86% |
| ETH | 585 | 5 | 6% | 3% | +8% | -85% | -85% |
| BNB | 582 | 2 | 4% | 2% | -59% | -90% | -92% |
| SOL | 581 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 579 | 3 | 6% | 2% | -32% | -86% | -89% |
| XRP | 579 | 4 | 2% | 1% | -12% | -74% | -74% |
| NEAR | 575 | 2 | 6% | 3% | -54% | -62% | -63% |
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
| UP (bought YES) | 3822 | 19 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3765 | 15 | 4% | 2% | -54% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 891 | 7 | 2% | 1% | +32% | -56% | -55% |
| 0.05–0.1% | 902 | 2 | 4% | 1% | -67% | -90% | -92% |
| 0.1–0.2% | 1291 | 4 | 4% | 2% | -61% | -90% | -91% |
| 0.2–0.5% | 1514 | 7 | 6% | 4% | -49% | -87% | -87% |
| Over 0.5% | 648 | 4 | 7% | 3% | -37% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1589 | 3 | 3% | 1% | -77% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,059 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 2:14:43 PM | DOGE | UP | 16 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:14:27 PM | BNB | DOWN | 32 sec | -0.010% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:14:11 PM | ZEC | DOWN | 48 sec | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:14:11 PM | XRP | UP | 48 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:13:40 PM | ETH | UP | 79 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:13:24 PM | HYPE | DOWN | 1.6 min | +0.101% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 2:09:59 PM | SOL | UP | 5.0 min | -0.393% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:59:54 PM | BTC | UP | 6 sec | -0.001% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:59:54 PM | HYPE | UP | 6 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 1:59:39 PM | DOGE | UP | 21 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:59:23 PM | NEAR | UP | 37 sec | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:59:07 PM | XRP | DOWN | 53 sec | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:59:07 PM | BNB | DOWN | 53 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:59:07 PM | ETH | UP | 53 sec | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:58:51 PM | ZEC | UP | 69 sec | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:57:32 PM | SOL | UP | 2.5 min | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:44:56 PM | DOGE | UP | 3 sec | -0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 1:44:39 PM | ZEC | UP | 21 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:44:39 PM | BNB | DOWN | 21 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:43:36 PM | BTC | UP | 84 sec | -0.070% | 3¢ | ❌ Lost | -$0.15 |
| 10/4 1:43:36 PM | HYPE | UP | 84 sec | -0.119% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 1:43:04 PM | SOL | UP | 1.9 min | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:43:04 PM | ETH | UP | 1.9 min | -0.065% | 14¢ | ❌ Lost | -$0.15 |
| 10/4 1:42:33 PM | XRP | UP | 2.5 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:29:39 PM | HYPE | DOWN | 21 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:29:39 PM | BNB | UP | 21 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:29:23 PM | ZEC | DOWN | 37 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:29:07 PM | DOGE | DOWN | 53 sec | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:28:37 PM | XRP | DOWN | 83 sec | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:28:21 PM | BTC | DOWN | 1.6 min | +0.096% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
