# 15-Minute 1¢ Study

*Updated Fri Oct 16, 5:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1673 finished bets | 1% | $80.30 | +43% | +4.80¢ | $35.25 / $45.05 |

*Expect about **89 buys a day** (~$13.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1539 | $43.50 | +26% |
| Momentum model ≥ 2%, hold to the close | 2610 | -$8.25 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1673 | -$22.20 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21367 | 21360 | 80 (0%) | 1.07% | -$1,481.00 (-57%) | Hold to the close: -$1,481.00 (-57%) |

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
| Volatility model | 13647 | 4.4% | 0.4% (54) | -648% | ❌ Worse |
| Momentum model | 13647 | 4.4% | 0.4% (54) | -671% | ❌ Worse |
| Mean-reversion model | 13647 | 7.4% | 0.4% (54) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13647 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3064 | 24 | -9% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1673 | 19 | +43% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 968 | 11 | +63% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2610 | 21 | -3% | -80% | -81% | -77% |
| Momentum model ≥ 5% | 1539 | 15 | +26% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1026 | 10 | +37% | -72% | -72% | -67% |
| Mean-reversion model ≥ 2% | 5176 | 34 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3577 | 27 | -17% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2348 | 16 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13845 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5298 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21360 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,481.00 | -57% | — |
| Sell at 2¢ | 763 | 4% | -$2,304.62 | -89% | 41 sec |
| Sell at 3¢ | 513 | 2% | -$2,302.93 | -89% | 47 sec |
| Sell at 5¢ | 370 | 2% | -$2,262.50 | -87% | 50 sec |
| Sell at 10¢ | 222 | 1% | -$2,184.18 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,015.94 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,802.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 730 | 5 | 10% | 3% | -35% | -82% | -85% |
| 2–5 min | 6911 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5559 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8156 | 18 | 1% | 0% | -68% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1555 | 11 | 5% | 3% | -12% | -89% | -90% |
| HYPE | 1550 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1543 | 8 | 6% | 3% | -37% | -87% | -87% |
| BNB | 1541 | 6 | 5% | 2% | -52% | -89% | -89% |
| DOGE | 1540 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1537 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1529 | 7 | 2% | 1% | -43% | -86% | -87% |
| NEAR | 1525 | 8 | 6% | 3% | -31% | -77% | -78% |
| BTC | 1525 | 7 | 5% | 2% | -39% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 813 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 664 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10771 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10589 | 40 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2280 | 11 | 2% | 1% | -18% | -79% | -79% |
| 0.05–0.1% | 2371 | 7 | 3% | 1% | -57% | -92% | -91% |
| 0.1–0.2% | 3490 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4082 | 21 | 6% | 3% | -43% | -88% | -88% |
| Over 0.5% | 1619 | 6 | 7% | 3% | -62% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5095 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,438 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 5:44:59 PM | NEAR | DOWN | 1 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:44:59 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:44:59 PM | ZEC | UP | 1 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:44:27 PM | ETH | DOWN | 33 sec | +0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:44:12 PM | BTC | UP | 47 sec | -0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:43:08 PM | SOL | DOWN | 1.9 min | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:42:53 PM | BNB | UP | 2.1 min | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:42:21 PM | XRP | DOWN | 2.6 min | +0.099% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 5:42:05 PM | HYPE | DOWN | 2.9 min | +0.119% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:41:49 PM | DOGE | DOWN | 3.2 min | +0.169% | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:29:51 PM | HYPE | DOWN | 9 sec | +0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:29:35 PM | XRP | UP | 25 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:29:35 PM | WTI | DOWN | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:28:48 PM | ZEC | DOWN | 71 sec | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:28:48 PM | NEAR | UP | 71 sec | -0.349% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:28:16 PM | BTC | UP | 1.7 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:28:00 PM | SOL | UP | 2.0 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:27:41 PM | BNB | UP | 2.3 min | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:27:09 PM | DOGE | UP | 2.8 min | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:14:57 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:14:57 PM | BNB | DOWN | 3 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:14:41 PM | NEAR | UP | 19 sec | -0.266% | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:14:25 PM | DOGE | DOWN | 35 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:14:09 PM | XRP | DOWN | 51 sec | +0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:14:09 PM | ZEC | DOWN | 51 sec | +0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:14:09 PM | WTI | DOWN | 51 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:13:22 PM | HYPE | DOWN | 1.6 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:13:06 PM | ETH | UP | 1.9 min | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:59:52 PM | XRP | UP | 7 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:59:52 PM | WTI | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
