# 15-Minute 1¢ Study

*Updated Tue Oct 6, 5:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 685 finished bets | 1% | $38.65 | +53% | +5.64¢ | -$9.05 / $47.70 |

*Expect about **79 buys a day** (~$11.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 683 | $25.70 | +36% |
| Mean-reversion model ≥ 5%, hold to the close | 1506 | $20.55 | +11% |
| 5+ min left, hold to the close | 254 | $18.35 | +49% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9978 | 9972 | 46 (0%) | 1.07% | -$559.45 (-46%) | Hold to the close: -$559.45 (-46%) |

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
| Volatility model | 6502 | 4.2% | 0.5% (33) | -554% | ❌ Worse |
| Momentum model | 6502 | 4.2% | 0.5% (33) | -581% | ❌ Worse |
| Mean-reversion model | 6502 | 6.8% | 0.5% (33) | -639% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6502 | 33 | -36% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1263 | 12 | +11% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 685 | 8 | +53% | -61% | -60% | -56% |
| Volatility model ≥ 10% | 425 | 6 | +111% | -43% | -44% | -39% |
| Momentum model ≥ 2% | 1126 | 10 | +7% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 683 | 7 | +36% | -65% | -67% | -64% |
| Momentum model ≥ 10% | 474 | 6 | +84% | -53% | -54% | -51% |
| Mean-reversion model ≥ 2% | 2230 | 19 | -7% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1506 | 15 | +11% | -81% | -80% | -74% |
| Mean-reversion model ≥ 10% | 995 | 11 | +28% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6699 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2471 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 802 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9972 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$559.45 | -46% | — |
| Sell at 2¢ | 362 | 4% | -$1,081.33 | -90% | 34 sec |
| Sell at 3¢ | 239 | 2% | -$1,082.24 | -90% | 47 sec |
| Sell at 5¢ | 178 | 2% | -$1,059.75 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$1,002.94 | -83% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$901.75 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$780.95 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 251 | 4 | 10% | 4% | +51% | -82% | -87% |
| 2–5 min | 3207 | 24 | 7% | 3% | -27% | -87% | -87% |
| 1–2 min | 2622 | 11 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 3889 | 7 | 1% | 0% | -73% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 758 | 6 | 5% | 3% | -5% | -89% | -89% |
| HYPE | 750 | 3 | 5% | 3% | -51% | -88% | -87% |
| DOGE | 748 | 2 | 3% | 1% | -66% | -92% | -91% |
| ETH | 744 | 7 | 5% | 3% | +18% | -88% | -87% |
| BNB | 742 | 3 | 4% | 2% | -51% | -91% | -92% |
| NEAR | 740 | 5 | 6% | 3% | -11% | -67% | -68% |
| SOL | 740 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 739 | 4 | 5% | 3% | -29% | -87% | -89% |
| XRP | 738 | 5 | 2% | 1% | -15% | -79% | -79% |
| GOLD | 415 | 0 | 4% | 1% | -100% | -92% | -95% |
| SILVER | 400 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 381 | 2 | 3% | 1% | -43% | -95% | -97% |
| COPPER | 356 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 314 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 304 | 3 | 3% | 2% | -8% | -94% | -92% |
| PALLADIUM | 301 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 289 | 1 | 4% | 2% | -68% | -93% | -92% |
| GBPUSD | 278 | 1 | 3% | 2% | -66% | -94% | -94% |
| USDJPY | 235 | 3 | 2% | 1% | +19% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5029 | 24 | 4% | 2% | -44% | -90% | -89% |
| DOWN (bought NO) | 4943 | 22 | 3% | 2% | -49% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1113 | 8 | 2% | 1% | +23% | -64% | -63% |
| 0.05–0.1% | 1156 | 4 | 3% | 1% | -49% | -91% | -92% |
| 0.1–0.2% | 1689 | 6 | 4% | 2% | -55% | -91% | -91% |
| 0.2–0.5% | 1958 | 12 | 6% | 3% | -33% | -88% | -87% |
| Over 0.5% | 781 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2230 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,076 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 5:44:53 PM | HYPE | DOWN | 6 sec | +0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:44:53 PM | BNB | DOWN | 6 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:44:53 PM | PLATINUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:44:37 PM | SOL | DOWN | 22 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:44:05 PM | ZEC | UP | 54 sec | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:44:05 PM | ETH | DOWN | 54 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:44:05 PM | SILVER | UP | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:44:05 PM | BTC | DOWN | 54 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:43:49 PM | GBPUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:43:33 PM | PALLADIUM | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:43:17 PM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:42:13 PM | DOGE | DOWN | 2.8 min | +0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:42:13 PM | EURUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:42:13 PM | COPPER | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:41:25 PM | GOLD | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:41:09 PM | XRP | UP | 3.9 min | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:37:34 PM | NEAR | UP | 7.4 min | -0.770% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:29:48 PM | BNB | DOWN | 12 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:29:32 PM | WTI | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:29:32 PM | BTC | UP | 28 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:29:16 PM | DOGE | DOWN | 44 sec | +0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:29:01 PM | SOL | UP | 58 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:29:01 PM | PLATINUM | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:28:43 PM | ETH | UP | 76 sec | -0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:28:11 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:27:57 PM | GOLD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:27:41 PM | PALLADIUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:27:41 PM | XRP | DOWN | 2.3 min | +0.073% | 4¢ | ❌ Lost | -$0.15 |
| 10/6 5:27:25 PM | HYPE | DOWN | 2.6 min | +0.179% | 9¢ | ❌ Lost | -$0.15 |
| 10/6 5:26:21 PM | ZEC | DOWN | 3.6 min | +0.587% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
