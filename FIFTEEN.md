# 15-Minute 1¢ Study

*Updated Fri Oct 2, 9:17 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **34 buys a day** (~$5.10/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 393 | $0.75 | +2% |
| Momentum model ≥ 5%, sell at 50¢ | 393 | -$6.50 | -16% |
| Volatility model ≥ 5%, sell at 25¢ | 390 | -$10.70 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6188 | 6182 | 23 (0%) | 1.07% | -$426.20 (-57%) | Hold to the close: -$426.20 (-57%) |

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
| Volatility model | 3648 | 3.8% | 0.3% (11) | -676% | ❌ Worse |
| Momentum model | 3648 | 4.0% | 0.3% (11) | -720% | ❌ Worse |
| Mean-reversion model | 3648 | 6.9% | 0.3% (11) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3648 | 11 | -61% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 769 | 5 | -24% | -65% | -66% | -60% |
| Volatility model ≥ 5% | 390 | 2 | -32% | -44% | -44% | -39% |
| Volatility model ≥ 10% | 229 | 2 | +35% | -10% | -12% | -4% |
| Momentum model ≥ 2% | 677 | 4 | -28% | -65% | -67% | -64% |
| Momentum model ≥ 5% | 393 | 3 | +2% | -50% | -53% | -47% |
| Momentum model ≥ 10% | 265 | 2 | +12% | -31% | -32% | -26% |
| Mean-reversion model ≥ 2% | 1376 | 7 | -45% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 920 | 6 | -28% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 595 | 4 | -22% | -77% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3845 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1782 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6182 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$426.20 | -57% | — |
| Sell at 2¢ | 244 | 4% | -$670.76 | -90% | 43 sec |
| Sell at 3¢ | 152 | 2% | -$674.92 | -90% | 48 sec |
| Sell at 5¢ | 113 | 2% | -$660.75 | -88% | 64 sec |
| Sell at 10¢ | 74 | 1% | -$623.26 | -83% | 81 sec |
| Sell at 25¢ | 39 | 1% | -$577.11 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$522.45 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 2016 | 12 | 8% | 3% | -42% | -86% | -87% |
| 1–2 min | 1606 | 6 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 2389 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 434 | 2 | 4% | 1% | -39% | -90% | -91% |
| ZEC | 431 | 2 | 5% | 3% | -45% | -88% | -90% |
| ETH | 429 | 2 | 6% | 3% | -42% | -86% | -86% |
| HYPE | 429 | 2 | 5% | 4% | -43% | -88% | -85% |
| BNB | 428 | 0 | 4% | 1% | -100% | -91% | -93% |
| BTC | 426 | 1 | 7% | 3% | -69% | -84% | -88% |
| XRP | 424 | 3 | 2% | 1% | -7% | -65% | -66% |
| SOL | 423 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 421 | 1 | 6% | 2% | -67% | -86% | -88% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 223 | 2 | 4% | 2% | -16% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3150 | 14 | 4% | 2% | -48% | -91% | -91% |
| DOWN (bought NO) | 3032 | 9 | 4% | 2% | -66% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 485 | 2 | 1% | 1% | -22% | -57% | -57% |
| 0.05–0.1% | 552 | 0 | 3% | 1% | -100% | -90% | -93% |
| 0.1–0.2% | 943 | 2 | 4% | 1% | -72% | -90% | -91% |
| 0.2–0.5% | 1276 | 5 | 6% | 3% | -56% | -87% | -87% |
| Over 0.5% | 587 | 4 | 7% | 3% | -29% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1763 | 6 | 3% | 2% | -60% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,191 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 9:14:46 PM | ETH | UP | 14 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:14:46 PM | WTI | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:14:30 PM | SOL | UP | 30 sec | -0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:14:14 PM | HYPE | DOWN | 46 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:13:59 PM | BNB | UP | 60 sec | -0.142% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:13:26 PM | BTC | UP | 1.6 min | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:13:10 PM | DOGE | UP | 1.8 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:11:19 PM | ZEC | DOWN | 3.7 min | +0.367% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:10:13 PM | NEAR | DOWN | 4.8 min | +0.478% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:58:15 PM | XRP | UP | 1.7 min | -0.181% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:58:15 PM | DOGE | UP | 1.7 min | -0.179% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:59 PM | SOL | UP | 2.0 min | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:57:59 PM | ZEC | UP | 2.0 min | -0.303% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:59 PM | BTC | UP | 2.0 min | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:41 PM | HYPE | UP | 2.3 min | -0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:25 PM | ETH | UP | 2.6 min | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:09 PM | BNB | UP | 2.9 min | -0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:09 PM | NEAR | UP | 2.9 min | -0.495% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:44:49 PM | SOL | UP | 10 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:44:33 PM | BNB | UP | 26 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:44:33 PM | DOGE | UP | 26 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:44:17 PM | BTC | DOWN | 42 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:44:01 PM | XRP | UP | 59 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:42:56 PM | HYPE | UP | 2.0 min | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:42:56 PM | ETH | DOWN | 2.0 min | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:42:39 PM | ZEC | DOWN | 2.4 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:41:52 PM | NEAR | UP | 3.1 min | -0.438% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:29:51 PM | WTI | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:29:51 PM | ZEC | DOWN | 8 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:29:35 PM | XRP | UP | 24 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
