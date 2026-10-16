# 15-Minute 1¢ Study

*Updated Fri Oct 16, 2:57 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1660 finished bets | 1% | $81.50 | +44% | +4.91¢ | $36.00 / $45.50 |

*Expect about **89 buys a day** (~$13.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1528 | $44.55 | +27% |
| Momentum model ≥ 2%, hold to the close | 2592 | -$6.30 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1660 | -$21.00 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21252 | 21243 | 80 (0%) | 1.07% | -$1,468.85 (-57%) | Hold to the close: -$1,468.85 (-57%) |

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
| Volatility model | 13544 | 4.4% | 0.4% (54) | -637% | ❌ Worse |
| Momentum model | 13544 | 4.4% | 0.4% (54) | -660% | ❌ Worse |
| Mean-reversion model | 13544 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13544 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3040 | 24 | -9% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1660 | 19 | +44% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 959 | 11 | +64% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2592 | 21 | -2% | -80% | -81% | -77% |
| Momentum model ≥ 5% | 1528 | 15 | +27% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1018 | 10 | +38% | -72% | -72% | -66% |
| Mean-reversion model ≥ 2% | 5135 | 34 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3542 | 27 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2323 | 16 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13742 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5284 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21243 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,468.85 | -57% | — |
| Sell at 2¢ | 757 | 4% | -$2,294.03 | -89% | 42 sec |
| Sell at 3¢ | 508 | 2% | -$2,292.73 | -89% | 47 sec |
| Sell at 5¢ | 367 | 2% | -$2,252.30 | -87% | 50 sec |
| Sell at 10¢ | 221 | 1% | -$2,173.34 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,003.79 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,790.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 725 | 5 | 10% | 3% | -34% | -82% | -85% |
| 2–5 min | 6886 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5536 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8092 | 18 | 1% | 0% | -68% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1543 | 11 | 5% | 3% | -11% | -89% | -89% |
| HYPE | 1538 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1532 | 8 | 6% | 3% | -37% | -88% | -87% |
| BNB | 1529 | 6 | 5% | 2% | -52% | -89% | -89% |
| DOGE | 1528 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1526 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1517 | 7 | 3% | 1% | -43% | -86% | -87% |
| BTC | 1516 | 7 | 5% | 2% | -39% | -88% | -91% |
| NEAR | 1513 | 8 | 6% | 3% | -31% | -78% | -78% |
| GOLD | 863 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 840 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 805 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 660 | 5 | 2% | 2% | -29% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10718 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10525 | 40 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2249 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2348 | 7 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 3465 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4065 | 21 | 6% | 3% | -43% | -88% | -88% |
| Over 0.5% | 1612 | 6 | 6% | 3% | -61% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 4978 | 16 | 3% | 1% | -62% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,423 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 2:57:47 PM | ZEC | UP | 2.2 min | -0.544% | — | In play | — |
| 10/16 2:55:07 PM | SOL | DOWN | 4.9 min | +0.342% | — | In play | — |
| 10/16 2:44:57 PM | EURUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:44:41 PM | SILVER | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:44:41 PM | BNB | DOWN | 19 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:43:54 PM | DOGE | DOWN | 65 sec | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:43:54 PM | XRP | DOWN | 65 sec | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:43:54 PM | ETH | DOWN | 65 sec | +0.064% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 2:43:38 PM | NEAR | UP | 81 sec | -0.528% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:43:38 PM | ZEC | UP | 81 sec | -0.282% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:43:22 PM | SOL | DOWN | 1.6 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:43:06 PM | BTC | DOWN | 1.9 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:41:12 PM | HYPE | DOWN | 3.8 min | +0.363% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:56 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:56 PM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:56 PM | EURUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:40 PM | PLATINUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:24 PM | GOLD | DOWN | 35 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:28:54 PM | DOGE | DOWN | 65 sec | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:28:38 PM | BTC | DOWN | 81 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:28:38 PM | NEAR | DOWN | 81 sec | +0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:28:22 PM | SOL | DOWN | 1.6 min | +0.181% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:28:06 PM | ETH | DOWN | 1.9 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:28:06 PM | BNB | DOWN | 1.9 min | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:27:16 PM | HYPE | DOWN | 2.7 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:27:16 PM | ZEC | DOWN | 2.7 min | +0.376% | 1¢ | ❌ Lost | $0.00 |
| 10/16 2:26:28 PM | XRP | DOWN | 3.5 min | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:14:34 PM | DOGE | UP | 25 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:14:34 PM | BTC | UP | 25 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:14:34 PM | GOLD | UP | 25 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
