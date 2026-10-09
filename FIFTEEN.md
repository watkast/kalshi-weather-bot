# 15-Minute 1¢ Study

*Updated Fri Oct 9, 3:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 888 finished bets | 1% | $29.40 | +30% | +3.31¢ | -$19.25 / $48.65 |

*Expect about **77 buys a day** (~$11.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 866 | $18.85 | +20% |
| 5+ min left, hold to the close | 383 | -$0.55 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 888 | -$7.85 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13242 | 13230 | 52 (0%) | 1.07% | -$878.50 (-55%) | Hold to the close: -$878.50 (-55%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 8406 | 4.0% | 0.4% (35) | -581% | ❌ Worse |
| Momentum model | 8406 | 4.1% | 0.4% (35) | -614% | ❌ Worse |
| Mean-reversion model | 8406 | 6.7% | 0.4% (35) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8406 | 35 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1623 | 13 | -7% | -75% | -75% | -72% |
| Volatility model ≥ 5% | 888 | 9 | +30% | -67% | -66% | -63% |
| Volatility model ≥ 10% | 543 | 7 | +89% | -52% | -52% | -48% |
| Momentum model ≥ 2% | 1435 | 11 | -8% | -76% | -78% | -75% |
| Momentum model ≥ 5% | 866 | 8 | +20% | -70% | -72% | -69% |
| Momentum model ≥ 10% | 593 | 6 | +45% | -62% | -62% | -59% |
| Mean-reversion model ≥ 2% | 2932 | 20 | -26% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1982 | 16 | -11% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1300 | 12 | +6% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8603 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3424 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13230 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$878.50 | -55% | — |
| Sell at 2¢ | 443 | 3% | -$1,449.32 | -90% | 33 sec |
| Sell at 3¢ | 295 | 2% | -$1,449.45 | -90% | 47 sec |
| Sell at 5¢ | 216 | 2% | -$1,424.10 | -89% | 56 sec |
| Sell at 10¢ | 142 | 1% | -$1,350.48 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,240.39 | -77% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,108.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 379 | 4 | 10% | 3% | +0% | -82% | -86% |
| 2–5 min | 4277 | 26 | 6% | 3% | -41% | -89% | -89% |
| 1–2 min | 3456 | 13 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 5114 | 9 | 1% | 0% | -74% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 962 | 6 | 4% | 3% | -25% | -90% | -90% |
| HYPE | 962 | 3 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 960 | 2 | 3% | 1% | -74% | -92% | -92% |
| BNB | 959 | 4 | 4% | 2% | -50% | -91% | -92% |
| ETH | 956 | 7 | 5% | 2% | -10% | -89% | -89% |
| NEAR | 952 | 5 | 6% | 3% | -31% | -73% | -73% |
| BTC | 952 | 4 | 5% | 2% | -45% | -88% | -90% |
| SOL | 951 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 949 | 6 | 2% | 1% | -21% | -82% | -82% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 522 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| NATGAS | 418 | 3 | 3% | 2% | -33% | -95% | -93% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6674 | 27 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 6556 | 25 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1384 | 8 | 2% | 1% | +0% | -69% | -69% |
| 0.05–0.1% | 1455 | 4 | 3% | 1% | -60% | -92% | -92% |
| 0.1–0.2% | 2199 | 7 | 4% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2517 | 13 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 1046 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3028 | 8 | 3% | 1% | -69% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,031 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 3:12:41 PM | BTC | DOWN | 2.3 min | +0.093% | — | In play | — |
| 10/9 3:12:41 PM | NEAR | DOWN | 2.3 min | +0.478% | — | In play | — |
| 10/9 3:11:54 PM | XRP | DOWN | 3.1 min | +0.173% | — | In play | — |
| 10/9 3:10:50 PM | BNB | DOWN | 4.2 min | +0.089% | — | In play | — |
| 10/9 3:10:50 PM | DOGE | DOWN | 4.2 min | +0.264% | — | In play | — |
| 10/9 2:59:50 PM | PLATINUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:18 PM | NATGAS | DOWN | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:18 PM | GBPUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:18 PM | USDJPY | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:03 PM | GOLD | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:57:59 PM | SOL | DOWN | 2.0 min | +0.236% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:57:59 PM | XRP | DOWN | 2.0 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:57:09 PM | DOGE | DOWN | 2.9 min | +0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:56:54 PM | ZEC | DOWN | 3.1 min | +0.415% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:56:06 PM | BTC | DOWN | 3.9 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:55:34 PM | BNB | DOWN | 4.4 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:55:18 PM | ETH | DOWN | 4.7 min | +0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:55:18 PM | HYPE | DOWN | 4.7 min | +0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:53:41 PM | NEAR | DOWN | 6.3 min | +0.691% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:52 PM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:44:52 PM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:52 PM | HYPE | DOWN | 7 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:44:36 PM | BTC | DOWN | 23 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:36 PM | PLATINUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:36 PM | DOGE | DOWN | 23 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:20 PM | ETH | UP | 39 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:20 PM | XRP | UP | 39 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:04 PM | COPPER | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:43:30 PM | SOL | UP | 89 sec | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:43:14 PM | ZEC | UP | 1.8 min | -0.281% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
