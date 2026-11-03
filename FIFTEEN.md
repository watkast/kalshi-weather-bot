# 15-Minute 1¢ Study

*Updated Tue Nov 3, 2:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3585 finished bets | 1% | $117.35 | +29% | +3.27¢ | $66.95 / $50.40 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3324 | $44.05 | +12% |
| Volatility model ≥ 2%, hold to the close | 6625 | $38.40 | +5% |
| Momentum model ≥ 2%, hold to the close | 5470 | -$44.10 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44240 | 44230 | 165 (0%) | 1.07% | -$3,075.60 (-57%) | Hold to the close: -$3,075.60 (-57%) |

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
| Volatility model | 27211 | 4.7% | 0.4% (107) | -678% | ❌ Worse |
| Momentum model | 27211 | 4.6% | 0.4% (107) | -703% | ❌ Worse |
| Mean-reversion model | 27211 | 8.1% | 0.4% (107) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27211 | 107 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6625 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3585 | 37 | +29% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2035 | 22 | +54% | -70% | -69% | -65% |
| Momentum model ≥ 2% | 5470 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3324 | 29 | +12% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2169 | 19 | +22% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 11254 | 77 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7895 | 66 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5283 | 47 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27416 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10460 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6354 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44230 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,075.60 | -57% | — |
| Sell at 2¢ | 1742 | 4% | -$4,694.68 | -87% | 47 sec |
| Sell at 3¢ | 1195 | 3% | -$4,681.55 | -87% | 49 sec |
| Sell at 5¢ | 828 | 2% | -$4,581.40 | -85% | 63 sec |
| Sell at 10¢ | 499 | 1% | -$4,381.91 | -81% | 66 sec |
| Sell at 25¢ | 262 | 1% | -$4,056.38 | -75% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,684.85 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2130 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14198 | 79 | 7% | 4% | -45% | -86% | -86% |
| 1–2 min | 11174 | 39 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 16717 | 38 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3072 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3064 | 11 | 4% | 2% | -55% | -90% | -90% |
| HYPE | 3058 | 9 | 5% | 2% | -63% | -89% | -87% |
| BNB | 3058 | 17 | 5% | 2% | -30% | -85% | -84% |
| DOGE | 3045 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3043 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3028 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3028 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3020 | 12 | 3% | 1% | -51% | -89% | -88% |
| GOLD | 1624 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1581 | 7 | 5% | 2% | -48% | -82% | -81% |
| WTI | 1580 | 5 | 3% | 1% | -62% | -92% | -93% |
| PLATINUM | 1412 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1352 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1335 | 6 | 1% | 1% | -58% | -69% | -69% |
| NATGAS | 1286 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1282 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1265 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1257 | 5 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 813 | 4 | 2% | 1% | -54% | -86% | -85% |
| USDCAD | 775 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 377 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 222 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 214 | 2 | 4% | 0% | -13% | -6% | -5% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22458 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21772 | 77 | 4% | 2% | -59% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4461 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4696 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7104 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8118 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3029 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10384 | 39 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,715 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 2:29:52 PM | PALLADIUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:29:52 PM | 2YRRATE | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:29:52 PM | SOL | UP | 8 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/3 2:29:37 PM | GBPUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:29:37 PM | ETH | DOWN | 23 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/3 2:29:37 PM | BRENT | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:29:37 PM | AUDUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:29:37 PM | PLATINUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:29:37 PM | BTC | UP | 23 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/3 2:28:52 PM | USDCAD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:28:20 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:28:05 PM | BNB | DOWN | 1.9 min | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:27:47 PM | WTI | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:27:47 PM | SILVER | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:27:31 PM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:27:15 PM | DOGE | DOWN | 2.8 min | +0.117% | 4¢ | ❌ Lost | -$0.15 |
| 11/3 2:26:26 PM | NEAR | DOWN | 3.6 min | +0.528% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:25:12 PM | XRP | DOWN | 4.8 min | +0.281% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:24:18 PM | HYPE | DOWN | 5.7 min | +0.468% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:22:07 PM | ZEC | DOWN | 7.9 min | +1.134% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:14:54 PM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:14:38 PM | USDCAD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:14:38 PM | GOLD | DOWN | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 2:14:22 PM | GBPUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:14:22 PM | BTC | DOWN | 37 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 11/3 2:14:04 PM | NEAR | DOWN | 55 sec | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:13:50 PM | SOL | DOWN | 69 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/3 2:13:50 PM | HYPE | DOWN | 69 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:13:34 PM | BRENT | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:13:34 PM | ETH | DOWN | 85 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
