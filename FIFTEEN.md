# 15-Minute 1¢ Study

*Updated Wed Oct 28, 2:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2943 finished bets | 1% | $88.05 | +27% | +2.99¢ | $89.10 / -$1.05 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2732 | $49.55 | +16% |
| Volatility model ≥ 2%, hold to the close | 5453 | $20.30 | +3% |
| Momentum model ≥ 2%, hold to the close | 4512 | -$50.05 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35928 | 35920 | 138 (0%) | 1.07% | -$2,447.25 (-56%) | Hold to the close: -$2,447.25 (-56%) |

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
| Volatility model | 22547 | 4.7% | 0.4% (92) | -665% | ❌ Worse |
| Momentum model | 22547 | 4.6% | 0.4% (92) | -690% | ❌ Worse |
| Mean-reversion model | 22547 | 8.0% | 0.4% (92) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22547 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5453 | 49 | +3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2943 | 30 | +27% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1672 | 19 | +60% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4512 | 34 | -10% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2732 | 25 | +16% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1796 | 17 | +30% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9184 | 63 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6446 | 53 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4308 | 38 | -0% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22747 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8541 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4632 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35920 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,447.25 | -56% | — |
| Sell at 2¢ | 1362 | 4% | -$3,829.13 | -87% | 47 sec |
| Sell at 3¢ | 935 | 3% | -$3,818.60 | -87% | 48 sec |
| Sell at 5¢ | 649 | 2% | -$3,761.40 | -86% | 62 sec |
| Sell at 10¢ | 397 | 1% | -$3,607.18 | -82% | 65 sec |
| Sell at 25¢ | 214 | 1% | -$3,320.91 | -76% | 86 sec |
| Sell at 50¢ | 142 | 0% | -$2,986.75 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1598 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11482 | 66 | 7% | 3% | -43% | -87% | -87% |
| 1–2 min | 9121 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13715 | 32 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2547 | 12 | 5% | 2% | -40% | -89% | -88% |
| HYPE | 2540 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2539 | 15 | 5% | 2% | -26% | -84% | -83% |
| SOL | 2533 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2527 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2525 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2515 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2512 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2509 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1353 | 5 | 5% | 2% | -56% | -81% | -83% |
| SILVER | 1323 | 6 | 4% | 2% | -47% | -82% | -82% |
| WTI | 1304 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1172 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1119 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1096 | 3 | 2% | 1% | -74% | -88% | -88% |
| NATGAS | 1078 | 6 | 2% | 1% | -48% | -79% | -79% |
| PALLADIUM | 1038 | 2 | 1% | 0% | -82% | -89% | -90% |
| GBPUSD | 1033 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1019 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 575 | 4 | 1% | 1% | -35% | -81% | -80% |
| USDCAD | 534 | 0 | 1% | 0% | -100% | -97% | -98% |
| BRENT | 154 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 102 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 93 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 91 | 1 | 3% | 1% | +3% | +8% | +8% |
| 5YRRATE | 89 | 1 | 4% | 2% | +5% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18172 | 77 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17748 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3755 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3915 | 14 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 5925 | 22 | 5% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6676 | 29 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2472 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8947 | 35 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,636 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 2:14:50 AM | USDJPY | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:14:34 AM | HYPE | DOWN | 25 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:14:34 AM | SOL | UP | 25 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:14:18 AM | DOGE | UP | 42 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:14:18 AM | NATGAS | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:14:18 AM | GOLD | DOWN | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:14:02 AM | PALLADIUM | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:14:02 AM | NEAR | DOWN | 57 sec | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:13:46 AM | ZEC | DOWN | 73 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:12:58 AM | XRP | DOWN | 2.0 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:12:26 AM | COPPER | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:12:09 AM | USDCAD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:12:09 AM | BTC | DOWN | 2.8 min | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:11:52 AM | ETH | DOWN | 3.1 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:07:20 AM | BNB | DOWN | 7.7 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:59:48 AM | AUDUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:41 AM | WTI | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:41 AM | HYPE | DOWN | 79 sec | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:41 AM | PALLADIUM | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:25 AM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:25 AM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:25 AM | BRENT | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:10 AM | 10YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:10 AM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:10 AM | 30YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:10 AM | 5YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:57:37 AM | ZEC | DOWN | 2.4 min | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:57:37 AM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:57:21 AM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:57:21 AM | BTC | DOWN | 2.6 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
