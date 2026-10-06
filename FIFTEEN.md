# 15-Minute 1¢ Study

*Updated Tue Oct 6, 5:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 683 finished bets | 1% | $38.80 | +53% | +5.68¢ | -$9.05 / $47.85 |

*Expect about **79 buys a day** (~$11.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 681 | $25.85 | +36% |
| Mean-reversion model ≥ 5%, hold to the close | 1499 | $21.45 | +11% |
| 5+ min left, hold to the close | 252 | $18.65 | +50% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9932 | 9925 | 46 (0%) | 1.07% | -$553.75 (-46%) | Hold to the close: -$553.75 (-46%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6475 | 4.1% | 0.5% (33) | -550% | ❌ Worse |
| Momentum model | 6475 | 4.2% | 0.5% (33) | -577% | ❌ Worse |
| Mean-reversion model | 6475 | 6.8% | 0.5% (33) | -633% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6475 | 33 | -36% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1259 | 12 | +11% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 683 | 8 | +53% | -61% | -60% | -56% |
| Volatility model ≥ 10% | 423 | 6 | +112% | -43% | -44% | -38% |
| Momentum model ≥ 2% | 1124 | 10 | +8% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 681 | 7 | +36% | -65% | -67% | -64% |
| Momentum model ≥ 10% | 472 | 6 | +84% | -53% | -54% | -51% |
| Mean-reversion model ≥ 2% | 2223 | 19 | -7% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1499 | 15 | +11% | -81% | -80% | -74% |
| Mean-reversion model ≥ 10% | 989 | 11 | +29% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6672 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2457 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 796 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9925 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$553.75 | -46% | — |
| Sell at 2¢ | 360 | 4% | -$1,076.15 | -90% | 33 sec |
| Sell at 3¢ | 237 | 2% | -$1,077.32 | -90% | 47 sec |
| Sell at 5¢ | 177 | 2% | -$1,054.70 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$997.24 | -83% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$896.05 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$775.25 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 249 | 4 | 10% | 4% | +52% | -82% | -87% |
| 2–5 min | 3191 | 24 | 7% | 3% | -27% | -87% | -87% |
| 1–2 min | 2615 | 11 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 3867 | 7 | 1% | 0% | -73% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 755 | 6 | 5% | 3% | -5% | -89% | -89% |
| HYPE | 747 | 3 | 5% | 3% | -51% | -89% | -87% |
| DOGE | 745 | 2 | 3% | 1% | -66% | -92% | -91% |
| ETH | 741 | 7 | 5% | 3% | +18% | -87% | -87% |
| BNB | 739 | 3 | 4% | 2% | -51% | -91% | -92% |
| NEAR | 737 | 5 | 6% | 3% | -11% | -67% | -68% |
| SOL | 737 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 736 | 4 | 5% | 3% | -29% | -87% | -89% |
| XRP | 735 | 5 | 1% | 1% | -14% | -79% | -79% |
| GOLD | 412 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 397 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 379 | 2 | 3% | 1% | -42% | -95% | -97% |
| COPPER | 354 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 312 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 304 | 3 | 3% | 2% | -8% | -94% | -92% |
| PALLADIUM | 299 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 287 | 1 | 4% | 2% | -67% | -93% | -92% |
| GBPUSD | 276 | 1 | 3% | 2% | -66% | -94% | -94% |
| USDJPY | 233 | 3 | 2% | 1% | +20% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5010 | 24 | 4% | 2% | -44% | -89% | -89% |
| DOWN (bought NO) | 4915 | 22 | 3% | 2% | -49% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1106 | 8 | 2% | 1% | +24% | -63% | -63% |
| 0.05–0.1% | 1147 | 4 | 3% | 1% | -49% | -91% | -92% |
| 0.1–0.2% | 1684 | 6 | 4% | 2% | -55% | -92% | -92% |
| 0.2–0.5% | 1955 | 12 | 6% | 3% | -33% | -88% | -87% |
| Over 0.5% | 778 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2183 | 7 | 3% | 1% | -62% | -88% | -89% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,068 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 5:09:28 PM | ZEC | DOWN | 5.5 min | +0.644% | — | In play | — |
| 10/6 4:59:49 PM | BTC | UP | 10 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:59:33 PM | BNB | UP | 27 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:59:17 PM | HYPE | UP | 43 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:59:17 PM | SILVER | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:58:43 PM | XRP | UP | 77 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:58:11 PM | DOGE | UP | 1.8 min | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:57:39 PM | ZEC | UP | 2.4 min | -0.310% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:56:20 PM | SOL | UP | 3.6 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:54:28 PM | NEAR | UP | 5.5 min | -0.490% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:44:49 PM | DOGE | UP | 11 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:44:33 PM | WTI | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:44:17 PM | NEAR | UP | 43 sec | -0.264% | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:44:17 PM | XRP | DOWN | 43 sec | -0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:44:17 PM | HYPE | DOWN | 43 sec | +0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:44:17 PM | GBPUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:44:17 PM | ZEC | DOWN | 43 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:44:02 PM | ETH | DOWN | 57 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:44:02 PM | COPPER | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:43:46 PM | BTC | DOWN | 73 sec | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:43:30 PM | EURUSD | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:43:14 PM | SOL | UP | 1.8 min | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:42:26 PM | BNB | UP | 2.5 min | -0.118% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:42:10 PM | GOLD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:42:10 PM | SILVER | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:29:49 PM | NEAR | DOWN | 11 sec | -0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:29:49 PM | WTI | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:29:33 PM | HYPE | DOWN | 27 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:29:17 PM | XRP | UP | 43 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:29:02 PM | ETH | UP | 57 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
