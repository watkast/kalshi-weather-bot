# 15-Minute 1¢ Study

*Updated Tue Oct 27, 11:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2930 finished bets | 1% | $89.70 | +27% | +3.06¢ | $89.55 / $0.15 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2724 | $50.60 | +17% |
| Volatility model ≥ 2%, hold to the close | 5435 | $22.55 | +3% |
| Momentum model ≥ 2%, hold to the close | 4501 | -$48.85 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35743 | 35735 | 137 (0%) | 1.07% | -$2,437.70 (-56%) | Hold to the close: -$2,437.70 (-56%) |

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
| Volatility model | 22463 | 4.7% | 0.4% (92) | -664% | ❌ Worse |
| Momentum model | 22463 | 4.6% | 0.4% (92) | -689% | ❌ Worse |
| Mean-reversion model | 22463 | 8.0% | 0.4% (92) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22463 | 92 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5435 | 49 | +3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2930 | 30 | +27% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1665 | 19 | +61% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4501 | 34 | -9% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2724 | 25 | +17% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1790 | 17 | +31% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9149 | 63 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6420 | 53 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4288 | 38 | +0% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22663 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8479 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4593 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35735 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 137 | 0% | -$2,437.70 | -56% | — |
| Sell at 2¢ | 1357 | 4% | -$3,806.88 | -87% | 47 sec |
| Sell at 3¢ | 931 | 3% | -$3,796.61 | -87% | 48 sec |
| Sell at 5¢ | 647 | 2% | -$3,739.15 | -86% | 62 sec |
| Sell at 10¢ | 396 | 1% | -$3,584.94 | -82% | 65 sec |
| Sell at 25¢ | 213 | 1% | -$3,300.67 | -76% | 88 sec |
| Sell at 50¢ | 141 | 0% | -$2,969.95 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1590 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11432 | 65 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9060 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13649 | 32 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2538 | 12 | 5% | 2% | -40% | -89% | -88% |
| HYPE | 2530 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2529 | 15 | 5% | 2% | -26% | -84% | -83% |
| SOL | 2525 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2517 | 11 | 6% | 3% | -47% | -85% | -85% |
| DOGE | 2516 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2506 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2503 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2499 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1345 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1315 | 6 | 4% | 2% | -47% | -82% | -82% |
| WTI | 1296 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1166 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1112 | 4 | 1% | 1% | -66% | -73% | -72% |
| EURUSD | 1090 | 3 | 2% | 1% | -74% | -88% | -88% |
| NATGAS | 1069 | 6 | 2% | 1% | -48% | -79% | -79% |
| PALLADIUM | 1030 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1027 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1011 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 567 | 3 | 1% | 1% | -51% | -81% | -80% |
| USDCAD | 528 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 146 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18080 | 76 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17655 | 61 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3737 | 19 | 2% | 1% | -13% | -81% | -80% |
| 0.05–0.1% | 3894 | 14 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 5895 | 22 | 5% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6662 | 29 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2471 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9791 | 32 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,641 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 11:44:51 PM | NATGAS | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:44:51 PM | GBPUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:44:51 PM | NEAR | UP | 8 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:44:51 PM | SILVER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:44:51 PM | GOLD | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:44:51 PM | BTC | DOWN | 8 sec | -0.002% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:44:36 PM | PALLADIUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:44:06 PM | ZEC | UP | 53 sec | -0.195% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:43:34 PM | COPPER | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:43:18 PM | BNB | UP | 1.7 min | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:43:18 PM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:43:06 PM | DOGE | UP | 1.9 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:43:06 PM | USDCAD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:43:06 PM | XRP | UP | 1.9 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:42:50 PM | HYPE | UP | 2.1 min | -0.232% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:42:35 PM | BRENT | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:42:19 PM | SOL | UP | 2.7 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:42:03 PM | ETH | UP | 2.9 min | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:41:47 PM | EURUSD | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:40:59 PM | WTI | DOWN | 4.0 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/27 11:29:46 PM | GBPUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:29:46 PM | ZEC | DOWN | 13 sec | -0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:29:30 PM | USDCAD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:29:30 PM | PALLADIUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:29:30 PM | XRP | DOWN | 29 sec | +0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:29:14 PM | DOGE | DOWN | 45 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:29:14 PM | EURUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:29:14 PM | BTC | UP | 45 sec | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:29:14 PM | SOL | DOWN | 45 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:28:58 PM | AUDUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
