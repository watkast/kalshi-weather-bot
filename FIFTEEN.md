# 15-Minute 1¢ Study

*Updated Sun Oct 11, 9:15 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1159 finished bets | 1% | $42.30 | +34% | +3.65¢ | $35.60 / $6.70 |

*Expect about **84 buys a day** (~$12.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1111 | $21.35 | +18% |
| 5+ min left, hold to the close | 405 | -$3.85 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1159 | -$16.70 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15080 | 15070 | 59 (0%) | 1.07% | -$987.50 (-54%) | Hold to the close: -$987.50 (-54%) |

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
| Volatility model | 10087 | 4.5% | 0.4% (42) | -684% | ❌ Worse |
| Momentum model | 10087 | 4.5% | 0.4% (42) | -713% | ❌ Worse |
| Mean-reversion model | 10087 | 7.2% | 0.4% (42) | -789% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10087 | 42 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2030 | 16 | -8% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1159 | 12 | +34% | -71% | -70% | -68% |
| Volatility model ≥ 10% | 734 | 8 | +58% | -61% | -61% | -57% |
| Momentum model ≥ 2% | 1791 | 13 | -11% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1111 | 10 | +18% | -75% | -75% | -72% |
| Momentum model ≥ 10% | 768 | 7 | +31% | -67% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3529 | 25 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2406 | 19 | -12% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1615 | 13 | -6% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10285 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3532 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1253 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15070 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$987.50 | -54% | — |
| Sell at 2¢ | 510 | 3% | -$1,638.90 | -90% | 33 sec |
| Sell at 3¢ | 336 | 2% | -$1,640.46 | -90% | 47 sec |
| Sell at 5¢ | 247 | 2% | -$1,610.95 | -89% | 50 sec |
| Sell at 10¢ | 164 | 1% | -$1,528.66 | -84% | 64 sec |
| Sell at 25¢ | 93 | 1% | -$1,407.67 | -78% | 81 sec |
| Sell at 50¢ | 61 | 0% | -$1,261.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 401 | 4 | 10% | 3% | -5% | -82% | -86% |
| 2–5 min | 4852 | 31 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3979 | 15 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 5834 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1154 | 6 | 4% | 3% | -36% | -90% | -90% |
| HYPE | 1152 | 3 | 4% | 2% | -68% | -90% | -89% |
| DOGE | 1146 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1145 | 5 | 4% | 2% | -47% | -91% | -92% |
| ETH | 1142 | 8 | 5% | 2% | -15% | -90% | -89% |
| SOL | 1142 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1138 | 5 | 5% | 2% | -41% | -88% | -91% |
| NEAR | 1133 | 6 | 5% | 2% | -31% | -76% | -76% |
| XRP | 1133 | 7 | 2% | 1% | -23% | -84% | -84% |
| GOLD | 581 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 567 | 1 | 3% | 1% | -80% | -94% | -94% |
| WTI | 542 | 3 | 3% | 1% | -37% | -95% | -96% |
| COPPER | 506 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 465 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 440 | 3 | 3% | 2% | -36% | -95% | -94% |
| PALLADIUM | 431 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 425 | 3 | 3% | 2% | -34% | -73% | -72% |
| GBPUSD | 402 | 1 | 2% | 1% | -77% | -96% | -95% |
| USDJPY | 366 | 3 | 1% | 1% | -23% | -98% | -97% |
| USDCAD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7554 | 31 | 3% | 2% | -52% | -90% | -89% |
| DOWN (bought NO) | 7516 | 28 | 3% | 2% | -57% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1875 | 9 | 2% | 1% | -20% | -76% | -76% |
| 0.05–0.1% | 1836 | 6 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 2637 | 8 | 4% | 2% | -63% | -91% | -92% |
| 0.2–0.5% | 2812 | 16 | 5% | 3% | -37% | -89% | -88% |
| Over 0.5% | 1122 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4181 | 10 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,528 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 9:14:56 PM | GBPUSD | DOWN | 4 sec | — | 0¢ | In play | — |
| 10/11 9:14:23 PM | WTI | UP | 37 sec | — | 1¢ | In play | — |
| 10/11 9:13:52 PM | NEAR | UP | 67 sec | -0.400% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:13:52 PM | USDJPY | UP | 67 sec | — | 0¢ | In play | — |
| 10/11 9:13:37 PM | DOGE | UP | 82 sec | -0.126% | 1¢ | ❌ Lost | $0.00 |
| 10/11 9:13:05 PM | ZEC | UP | 1.9 min | -0.259% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:13:05 PM | ETH | UP | 1.9 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:13:05 PM | XRP | UP | 1.9 min | -0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:12:34 PM | HYPE | DOWN | 2.4 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:11:46 PM | BTC | UP | 3.2 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:11:29 PM | BNB | UP | 3.5 min | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:11:29 PM | SOL | UP | 3.5 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:59:39 PM | PALLADIUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:59:39 PM | HYPE | UP | 21 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:59:39 PM | BNB | UP | 21 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:59:39 PM | SOL | UP | 21 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:59:39 PM | XRP | UP | 21 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:59:23 PM | AUDUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:59:23 PM | ZEC | UP | 37 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:59:07 PM | DOGE | UP | 53 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:58:52 PM | PLATINUM | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:58:52 PM | BTC | UP | 67 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:58:52 PM | GOLD | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:58:52 PM | COPPER | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:58:19 PM | ETH | UP | 1.7 min | -0.122% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:58:19 PM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:58:19 PM | SILVER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:57:48 PM | NEAR | DOWN | 2.2 min | +0.541% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:57:48 PM | USDJPY | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:57:33 PM | EURUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
