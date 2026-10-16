# 15-Minute 1¢ Study

*Updated Fri Oct 16, 1:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1653 finished bets | 1% | $82.40 | +45% | +4.98¢ | $36.45 / $45.95 |

*Expect about **89 buys a day** (~$13.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1520 | $45.60 | +28% |
| Momentum model ≥ 2%, hold to the close | 2580 | -$4.80 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1653 | -$20.10 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21198 | 21191 | 80 (0%) | 1.07% | -$1,462.55 (-57%) | Hold to the close: -$1,462.55 (-57%) |

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
| Volatility model | 13508 | 4.4% | 0.4% (54) | -637% | ❌ Worse |
| Momentum model | 13508 | 4.4% | 0.4% (54) | -660% | ❌ Worse |
| Mean-reversion model | 13508 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13508 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3024 | 24 | -8% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1653 | 19 | +45% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 957 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2580 | 21 | -2% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1520 | 15 | +28% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1013 | 10 | +39% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5115 | 34 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3529 | 27 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2317 | 16 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13706 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5274 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2211 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21191 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,462.55 | -57% | — |
| Sell at 2¢ | 755 | 4% | -$2,288.25 | -89% | 42 sec |
| Sell at 3¢ | 507 | 2% | -$2,286.82 | -89% | 47 sec |
| Sell at 5¢ | 367 | 2% | -$2,246.00 | -87% | 50 sec |
| Sell at 10¢ | 221 | 1% | -$2,167.04 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,997.49 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,784.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 721 | 5 | 10% | 3% | -34% | -82% | -85% |
| 2–5 min | 6875 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5517 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8074 | 18 | 1% | 0% | -68% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1539 | 11 | 5% | 3% | -11% | -89% | -89% |
| HYPE | 1534 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1528 | 8 | 5% | 3% | -37% | -88% | -87% |
| BNB | 1525 | 6 | 5% | 2% | -52% | -89% | -89% |
| DOGE | 1524 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1522 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1513 | 7 | 2% | 1% | -43% | -86% | -87% |
| BTC | 1512 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1509 | 8 | 6% | 3% | -31% | -77% | -78% |
| GOLD | 861 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 836 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 805 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 719 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 659 | 5 | 2% | 2% | -29% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 656 | 3 | 3% | 1% | -57% | -81% | -81% |
| GBPUSD | 614 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 199 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 168 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10703 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10488 | 40 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2245 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2342 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3455 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 4054 | 21 | 6% | 3% | -43% | -88% | -88% |
| Over 0.5% | 1607 | 6 | 6% | 3% | -61% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 4926 | 16 | 3% | 1% | -62% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,422 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 1:44:19 PM | PALLADIUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:44:05 PM | NEAR | UP | 54 sec | -0.378% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:49 PM | EURUSD | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:49 PM | SILVER | UP | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:01 PM | AUDUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:42:44 PM | ZEC | UP | 2.2 min | -0.494% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:41:56 PM | HYPE | UP | 3.1 min | -0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:41:56 PM | DOGE | UP | 3.1 min | -0.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:40:51 PM | SOL | UP | 4.1 min | -0.376% | 3¢ | ❌ Lost | -$0.15 |
| 10/16 1:40:19 PM | BTC | UP | 4.7 min | -0.278% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:39:47 PM | XRP | UP | 5.2 min | -0.431% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:39:47 PM | ETH | UP | 5.2 min | -0.444% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:39:29 PM | BNB | UP | 5.5 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:29:50 PM | EURUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:29:50 PM | GOLD | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:29:34 PM | WTI | UP | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:29:34 PM | ZEC | UP | 25 sec | -0.110% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:29:02 PM | PLATINUM | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:28:30 PM | USDJPY | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:28:14 PM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:28:14 PM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:28:14 PM | NEAR | DOWN | 1.8 min | +0.663% | 14¢ | ❌ Lost | -$0.15 |
| 10/16 1:27:11 PM | DOGE | DOWN | 2.8 min | +0.325% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:27:11 PM | ETH | DOWN | 2.8 min | +0.300% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:26:55 PM | HYPE | DOWN | 3.1 min | +0.368% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:26:55 PM | XRP | DOWN | 3.1 min | +0.401% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:26:55 PM | SOL | DOWN | 3.1 min | +0.509% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:26:39 PM | BNB | DOWN | 3.4 min | +0.111% | 3¢ | ❌ Lost | -$0.15 |
| 10/16 1:26:23 PM | BTC | DOWN | 3.6 min | +0.308% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:50 PM | NEAR | UP | 9 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
