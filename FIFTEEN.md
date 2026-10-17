# 15-Minute 1¢ Study

*Updated Fri Oct 16, 10:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1707 finished bets | 1% | $76.25 | +40% | +4.47¢ | $33.45 / $42.80 |

*Expect about **90 buys a day** (~$13.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1572 | $39.45 | +23% |
| Momentum model ≥ 2%, hold to the close | 2659 | -$14.55 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1707 | -$26.25 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21559 | 21546 | 80 (0%) | 1.07% | -$1,501.70 (-57%) | Hold to the close: -$1,501.70 (-57%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13822 | 4.5% | 0.4% (54) | -658% | ❌ Worse |
| Momentum model | 13822 | 4.4% | 0.4% (54) | -681% | ❌ Worse |
| Mean-reversion model | 13822 | 7.5% | 0.4% (54) | -793% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13822 | 54 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3110 | 24 | -11% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1707 | 19 | +40% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 993 | 11 | +58% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 2659 | 21 | -5% | -80% | -81% | -78% |
| Momentum model ≥ 5% | 1572 | 15 | +23% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1045 | 10 | +34% | -73% | -72% | -67% |
| Mean-reversion model ≥ 2% | 5256 | 34 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3629 | 27 | -18% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2385 | 16 | -23% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14020 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21546 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,501.70 | -57% | — |
| Sell at 2¢ | 770 | 4% | -$2,323.50 | -89% | 39 sec |
| Sell at 3¢ | 516 | 2% | -$2,322.46 | -89% | 47 sec |
| Sell at 5¢ | 371 | 2% | -$2,282.55 | -87% | 50 sec |
| Sell at 10¢ | 223 | 1% | -$2,203.57 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,036.64 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,823.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 738 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 6972 | 37 | 7% | 3% | -48% | -88% | -88% |
| 1–2 min | 5594 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8238 | 18 | 1% | 0% | -69% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1575 | 11 | 5% | 3% | -13% | -89% | -90% |
| HYPE | 1570 | 5 | 4% | 2% | -61% | -90% | -88% |
| ETH | 1562 | 8 | 6% | 3% | -38% | -87% | -87% |
| BNB | 1560 | 6 | 5% | 2% | -53% | -89% | -89% |
| DOGE | 1559 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1557 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1549 | 7 | 3% | 1% | -44% | -86% | -87% |
| NEAR | 1545 | 8 | 6% | 3% | -32% | -78% | -78% |
| BTC | 1543 | 7 | 5% | 2% | -40% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10866 | 40 | 4% | 2% | -58% | -89% | -89% |
| DOWN (bought NO) | 10680 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2333 | 11 | 2% | 1% | -21% | -80% | -80% |
| 0.05–0.1% | 2403 | 7 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 3535 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4115 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1631 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 5979 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,474 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 10:58:39 PM | BTC | UP | 80 sec | -0.053% | — | In play | — |
| 10/16 10:58:23 PM | NEAR | UP | 1.6 min | -0.329% | — | In play | — |
| 10/16 10:58:07 PM | HYPE | UP | 1.9 min | -0.082% | — | In play | — |
| 10/16 10:57:20 PM | DOGE | UP | 2.7 min | -0.193% | — | In play | — |
| 10/16 10:56:33 PM | BNB | UP | 3.5 min | -0.100% | — | In play | — |
| 10/16 10:55:30 PM | ETH | UP | 4.5 min | -0.137% | — | In play | — |
| 10/16 10:44:49 PM | HYPE | DOWN | 10 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:44:33 PM | DOGE | DOWN | 26 sec | +0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:44:33 PM | BNB | DOWN | 26 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:44:33 PM | XRP | DOWN | 26 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:44:17 PM | NEAR | UP | 42 sec | -0.248% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:43:46 PM | BTC | DOWN | 73 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:43:46 PM | ETH | DOWN | 73 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:43:30 PM | SOL | DOWN | 89 sec | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:43:30 PM | ZEC | DOWN | 89 sec | +0.214% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:29:59 PM | DOGE | DOWN | 1 sec | -0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:29:59 PM | ETH | DOWN | 1 sec | +0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:29:44 PM | ZEC | DOWN | 16 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:29:28 PM | XRP | DOWN | 32 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:29:12 PM | BTC | UP | 48 sec | -0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:28:56 PM | HYPE | UP | 64 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:28:25 PM | NEAR | UP | 1.6 min | -0.406% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:28:01 PM | BNB | UP | 2.0 min | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:28:01 PM | SOL | UP | 2.0 min | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:37 PM | ETH | UP | 23 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:14:21 PM | XRP | UP | 39 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:14:21 PM | BTC | UP | 39 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:14:05 PM | ZEC | UP | 55 sec | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:13:34 PM | BNB | DOWN | 86 sec | +0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:14 PM | NEAR | DOWN | 2.8 min | +0.586% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
