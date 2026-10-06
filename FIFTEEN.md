# 15-Minute 1¢ Study

*Updated Tue Oct 6, 3:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 642 finished bets | 1% | $29.15 | +42% | +4.54¢ | -$7.10 / $36.25 |

*Expect about **79 buys a day** (~$11.86/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 243 | $20.00 | +56% |
| Mean-reversion model ≥ 5%, hold to the close | 1410 | $19.15 | +11% |
| Momentum model ≥ 5%, hold to the close | 640 | $15.90 | +23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9382 | 9376 | 44 (0%) | 1.07% | -$512.60 (-45%) | Hold to the close: -$512.60 (-45%) |

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
| Volatility model | 6134 | 4.0% | 0.5% (32) | -524% | ❌ Worse |
| Momentum model | 6134 | 4.1% | 0.5% (32) | -549% | ❌ Worse |
| Mean-reversion model | 6134 | 6.7% | 0.5% (32) | -606% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6134 | 32 | -34% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1189 | 11 | +8% | -71% | -71% | -67% |
| Volatility model ≥ 5% | 642 | 7 | +42% | -59% | -58% | -54% |
| Volatility model ≥ 10% | 396 | 5 | +89% | -40% | -41% | -36% |
| Momentum model ≥ 2% | 1052 | 9 | +4% | -72% | -73% | -71% |
| Momentum model ≥ 5% | 640 | 6 | +23% | -63% | -66% | -63% |
| Momentum model ≥ 10% | 443 | 5 | +62% | -51% | -52% | -50% |
| Mean-reversion model ≥ 2% | 2100 | 18 | -6% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1410 | 14 | +11% | -80% | -79% | -73% |
| Mean-reversion model ≥ 10% | 933 | 10 | +24% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6331 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2301 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 744 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 9376 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 44 | 0% | -$512.60 | -45% | — |
| Sell at 2¢ | 350 | 4% | -$1,009.60 | -89% | 33 sec |
| Sell at 3¢ | 230 | 2% | -$1,010.90 | -90% | 47 sec |
| Sell at 5¢ | 171 | 2% | -$989.45 | -88% | 50 sec |
| Sell at 10¢ | 116 | 1% | -$934.64 | -83% | 65 sec |
| Sell at 25¢ | 66 | 1% | -$840.14 | -74% | 82 sec |
| Sell at 50¢ | 43 | 0% | -$726.35 | -64% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 240 | 4 | 10% | 3% | +58% | -82% | -88% |
| 2–5 min | 3022 | 24 | 7% | 3% | -22% | -87% | -87% |
| 1–2 min | 2468 | 11 | 3% | 2% | -52% | -94% | -93% |
| Under 1 min | 3643 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 717 | 6 | 5% | 3% | +0% | -89% | -89% |
| HYPE | 707 | 3 | 5% | 3% | -48% | -89% | -86% |
| DOGE | 706 | 2 | 4% | 1% | -63% | -91% | -91% |
| ETH | 704 | 7 | 6% | 3% | +25% | -87% | -86% |
| BNB | 702 | 3 | 4% | 2% | -48% | -90% | -92% |
| XRP | 700 | 5 | 2% | 1% | -9% | -78% | -78% |
| BTC | 699 | 4 | 5% | 3% | -25% | -87% | -89% |
| SOL | 699 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 697 | 4 | 6% | 3% | -25% | -66% | -67% |
| GOLD | 388 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 371 | 0 | 2% | 1% | -100% | -96% | -97% |
| WTI | 351 | 2 | 3% | 1% | -38% | -95% | -97% |
| COPPER | 329 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 294 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 287 | 2 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 281 | 1 | 2% | 1% | -67% | -97% | -98% |
| EURUSD | 270 | 1 | 4% | 3% | -65% | -93% | -91% |
| GBPUSD | 256 | 1 | 4% | 2% | -64% | -94% | -94% |
| USDJPY | 218 | 3 | 2% | 1% | +28% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4739 | 22 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4637 | 22 | 4% | 2% | -45% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1042 | 7 | 2% | 1% | +15% | -61% | -61% |
| 0.05–0.1% | 1087 | 4 | 3% | 1% | -46% | -91% | -92% |
| 0.1–0.2% | 1582 | 6 | 4% | 2% | -52% | -91% | -91% |
| 0.2–0.5% | 1858 | 12 | 6% | 3% | -29% | -88% | -87% |
| Over 0.5% | 760 | 5 | 7% | 3% | -32% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2436 | 14 | 4% | 2% | -34% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,050 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 3:29:53 AM | NATGAS | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:21 AM | EURUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:21 AM | COPPER | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:06 AM | ZEC | UP | 53 sec | -0.780% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:29:06 AM | BTC | UP | 53 sec | -0.230% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:29:06 AM | PALLADIUM | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:06 AM | GBPUSD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:06 AM | BNB | UP | 53 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:28:16 AM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:28:16 AM | PLATINUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:28:16 AM | HYPE | UP | 1.7 min | -0.411% | 1¢ | ❌ Lost | $0.00 |
| 10/6 3:28:16 AM | DOGE | UP | 1.7 min | -0.571% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:28:01 AM | XRP | UP | 2.0 min | -0.411% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:27:27 AM | ETH | UP | 2.5 min | -0.358% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:27:27 AM | NEAR | UP | 2.5 min | -0.954% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:27:27 AM | SOL | UP | 2.5 min | -0.733% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:26:07 AM | GOLD | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:25:51 AM | XRP | DOWN | 4.2 min | +0.239% | 100¢ | ✅ Won | $13.85 |
| 10/6 3:25:35 AM | ZEC | DOWN | 4.4 min | +1.386% | 100¢ | ✅ Won | $13.85 |
| 10/6 3:25:35 AM | BTC | DOWN | 4.4 min | +0.214% | 100¢ | ✅ Won | $13.85 |
| 10/6 3:24:14 AM | BNB | DOWN | 5.8 min | +0.208% | 100¢ | ✅ Won | $13.85 |
| 10/6 3:14:42 AM | WTI | UP | 18 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:14:26 AM | SILVER | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:14:26 AM | BNB | UP | 34 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:14:11 AM | DOGE | DOWN | 48 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:14:11 AM | EURUSD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:53 AM | GBPUSD | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:53 AM | COPPER | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:21 AM | ZEC | UP | 1.6 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:06 AM | XRP | DOWN | 1.9 min | +0.153% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
