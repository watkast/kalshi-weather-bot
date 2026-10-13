# 15-Minute 1¢ Study

*Updated Tue Oct 13, 2:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1289 finished bets | 1% | $40.70 | +29% | +3.16¢ | $28.85 / $11.85 |

*Expect about **83 buys a day** (~$12.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1229 | $21.55 | +16% |
| 5+ min left, hold to the close | 486 | -$15.70 | -22% |
| Volatility model ≥ 5%, sell at 50¢ | 1289 | -$18.30 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16888 | 16881 | 63 (0%) | 1.07% | -$1,160.85 (-57%) | Hold to the close: -$1,160.85 (-57%) |

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
| Volatility model | 11118 | 4.4% | 0.4% (46) | -656% | ❌ Worse |
| Momentum model | 11118 | 4.4% | 0.4% (46) | -684% | ❌ Worse |
| Mean-reversion model | 11118 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11118 | 46 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2294 | 18 | -9% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1289 | 13 | +29% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 793 | 9 | +62% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2014 | 15 | -10% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1229 | 11 | +16% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 836 | 8 | +35% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3990 | 27 | -26% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2725 | 20 | -19% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1794 | 14 | -10% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11316 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4082 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1483 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16881 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,160.85 | -57% | — |
| Sell at 2¢ | 577 | 3% | -$1,850.83 | -91% | 34 sec |
| Sell at 3¢ | 383 | 2% | -$1,851.48 | -91% | 46 sec |
| Sell at 5¢ | 274 | 2% | -$1,822.75 | -89% | 49 sec |
| Sell at 10¢ | 175 | 1% | -$1,743.60 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,617.16 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,456.85 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 482 | 4 | 11% | 3% | -21% | -81% | -86% |
| 2–5 min | 5443 | 32 | 6% | 3% | -42% | -88% | -89% |
| 1–2 min | 4455 | 16 | 3% | 2% | -61% | -94% | -94% |
| Under 1 min | 6497 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1270 | 7 | 4% | 2% | -32% | -90% | -90% |
| HYPE | 1265 | 4 | 4% | 2% | -61% | -90% | -89% |
| DOGE | 1261 | 2 | 4% | 2% | -80% | -91% | -90% |
| ETH | 1260 | 8 | 5% | 2% | -22% | -90% | -89% |
| BNB | 1260 | 5 | 4% | 2% | -52% | -90% | -91% |
| SOL | 1256 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1250 | 6 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1247 | 7 | 5% | 2% | -27% | -77% | -78% |
| XRP | 1247 | 7 | 2% | 1% | -30% | -85% | -85% |
| GOLD | 669 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 653 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 626 | 3 | 3% | 1% | -45% | -94% | -96% |
| COPPER | 578 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 544 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 510 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 502 | 3 | 3% | 2% | -44% | -96% | -94% |
| EURUSD | 487 | 3 | 3% | 2% | -43% | -76% | -75% |
| GBPUSD | 461 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 418 | 3 | 1% | 1% | -33% | -98% | -98% |
| AUDUSD | 61 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 56 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8503 | 34 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8378 | 29 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1977 | 10 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 2004 | 6 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2886 | 9 | 4% | 2% | -61% | -91% | -91% |
| 0.2–0.5% | 3197 | 18 | 6% | 3% | -38% | -89% | -88% |
| Over 0.5% | 1249 | 5 | 6% | 2% | -58% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 3964 | 9 | 3% | 1% | -73% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 2:44:46 PM | SILVER | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:44:36 PM | PALLADIUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:44:02 PM | XRP | UP | 57 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:43:40 PM | SOL | UP | 80 sec | -0.201% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:43:32 PM | BNB | DOWN | 88 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:43:20 PM | BTC | DOWN | 1.7 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:41:03 PM | NEAR | DOWN | 3.9 min | +0.625% | 2¢ | ❌ Lost | -$0.15 |
| 10/13 2:40:39 PM | ZEC | DOWN | 4.3 min | +0.630% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:40:33 PM | ETH | DOWN | 4.5 min | +0.204% | 3¢ | ❌ Lost | -$0.15 |
| 10/13 2:40:29 PM | DOGE | DOWN | 4.5 min | +0.249% | 4¢ | ❌ Lost | -$0.15 |
| 10/13 2:39:53 PM | HYPE | DOWN | 5.1 min | +0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:29:57 PM | NEAR | DOWN | 3 sec | +0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:29:33 PM | ZEC | UP | 27 sec | -0.176% | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:29:31 PM | PLATINUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:28:54 PM | DOGE | UP | 65 sec | -0.148% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:28:50 PM | SOL | UP | 69 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:28:44 PM | XRP | UP | 75 sec | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:28:36 PM | BNB | UP | 83 sec | -0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:28:18 PM | BTC | UP | 1.7 min | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:28:16 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:28:10 PM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:28:04 PM | ETH | UP | 1.9 min | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:27:24 PM | EURUSD | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:27:18 PM | HYPE | UP | 2.7 min | -0.207% | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:25:05 PM | GOLD | UP | 4.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/13 2:14:50 PM | DOGE | UP | 9 sec | -0.078% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:14:48 PM | BTC | UP | 11 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:14:38 PM | NATGAS | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:14:34 PM | PALLADIUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:14:30 PM | SOL | UP | 29 sec | -0.157% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
