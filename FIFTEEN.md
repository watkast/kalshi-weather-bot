# 15-Minute 1¢ Study

*Updated Fri Oct 16, 1:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1650 finished bets | 1% | $82.85 | +45% | +5.02¢ | $36.60 / $46.25 |

*Expect about **89 buys a day** (~$13.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1519 | $45.75 | +28% |
| Momentum model ≥ 2%, hold to the close | 2578 | -$4.50 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1650 | -$19.65 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21169 | 21162 | 80 (0%) | 1.07% | -$1,458.65 (-57%) | Hold to the close: -$1,458.65 (-57%) |

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
| Volatility model | 13490 | 4.4% | 0.4% (54) | -637% | ❌ Worse |
| Momentum model | 13490 | 4.4% | 0.4% (54) | -660% | ❌ Worse |
| Mean-reversion model | 13490 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13490 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3013 | 24 | -8% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1650 | 19 | +45% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 956 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2578 | 21 | -2% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1519 | 15 | +28% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1013 | 10 | +39% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5101 | 34 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3515 | 27 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2310 | 16 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13688 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5269 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2205 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21162 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,458.65 | -57% | — |
| Sell at 2¢ | 752 | 4% | -$2,285.13 | -89% | 42 sec |
| Sell at 3¢ | 506 | 2% | -$2,283.31 | -89% | 47 sec |
| Sell at 5¢ | 366 | 2% | -$2,242.75 | -87% | 50 sec |
| Sell at 10¢ | 220 | 1% | -$2,164.45 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,993.59 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,780.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 718 | 5 | 10% | 3% | -34% | -82% | -85% |
| 2–5 min | 6863 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5510 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 8067 | 18 | 1% | 0% | -68% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1537 | 11 | 5% | 3% | -11% | -89% | -89% |
| HYPE | 1532 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1526 | 8 | 6% | 3% | -36% | -88% | -87% |
| BNB | 1523 | 6 | 5% | 2% | -52% | -89% | -89% |
| DOGE | 1522 | 2 | 4% | 2% | -83% | -90% | -90% |
| SOL | 1520 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1511 | 7 | 2% | 1% | -43% | -86% | -87% |
| BTC | 1510 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1507 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 860 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 835 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 804 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 718 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 659 | 5 | 2% | 2% | -29% | -82% | -81% |
| PALLADIUM | 658 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 654 | 3 | 3% | 1% | -57% | -81% | -81% |
| GBPUSD | 613 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 573 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 198 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 167 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10686 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10476 | 40 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2245 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2342 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3453 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 4040 | 21 | 6% | 3% | -43% | -88% | -88% |
| Over 0.5% | 1605 | 6 | 6% | 3% | -61% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 4897 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,421 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 1:14:50 PM | NEAR | UP | 9 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:14:50 PM | ZEC | DOWN | 9 sec | +0.202% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:14:34 PM | COPPER | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:34 PM | SILVER | DOWN | 25 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:14:18 PM | AUDUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:18 PM | SOL | DOWN | 41 sec | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:46 PM | EURUSD | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:46 PM | HYPE | DOWN | 74 sec | +0.225% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:13:46 PM | XRP | DOWN | 74 sec | +0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:13:46 PM | PLATINUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:30 PM | GBPUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:30 PM | DOGE | DOWN | 1.5 min | +0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:58 PM | GOLD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:41 PM | BNB | DOWN | 2.3 min | +0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:25 PM | ETH | DOWN | 2.6 min | +0.223% | 3¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:09 PM | BTC | DOWN | 2.8 min | +0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:52 PM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:36 PM | SILVER | UP | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 12:59:36 PM | BTC | DOWN | 24 sec | +0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:20 PM | NEAR | DOWN | 40 sec | +0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/16 12:59:20 PM | ETH | UP | 40 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:05 PM | XRP | UP | 55 sec | -0.178% | 0¢ | ❌ Lost | $0.00 |
| 10/16 12:58:49 PM | ZEC | UP | 71 sec | -0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:58:17 PM | WTI | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:57:11 PM | COPPER | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:56:56 PM | HYPE | UP | 3.0 min | -0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:56:40 PM | SOL | UP | 3.3 min | -0.490% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:56:24 PM | BNB | UP | 3.6 min | -0.289% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:56:24 PM | AUDUSD | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:44:59 PM | PLATINUM | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
