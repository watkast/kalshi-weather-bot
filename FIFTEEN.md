# 15-Minute 1¢ Study

*Updated Thu Oct 8, 3:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 801 finished bets | 1% | $39.45 | +46% | +4.93¢ | -$14.60 / $54.05 |

*Expect about **76 buys a day** (~$11.33/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 797 | $26.35 | +31% |
| 5+ min left, hold to the close | 350 | $4.40 | +9% |
| Volatility model ≥ 2%, hold to the close | 1476 | $3.95 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12078 | 12071 | 50 (0%) | 1.07% | -$766.40 (-52%) | Hold to the close: -$766.40 (-52%) |

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
| Volatility model | 7719 | 4.0% | 0.4% (34) | -557% | ❌ Worse |
| Momentum model | 7719 | 4.0% | 0.4% (34) | -588% | ❌ Worse |
| Mean-reversion model | 7719 | 6.7% | 0.4% (34) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7719 | 34 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1476 | 13 | +2% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 801 | 9 | +46% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 492 | 7 | +110% | -47% | -47% | -42% |
| Momentum model ≥ 2% | 1308 | 11 | +1% | -75% | -76% | -74% |
| Momentum model ≥ 5% | 797 | 8 | +31% | -68% | -70% | -67% |
| Momentum model ≥ 10% | 542 | 6 | +59% | -58% | -59% | -55% |
| Mean-reversion model ≥ 2% | 2668 | 20 | -18% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1798 | 16 | -1% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1185 | 12 | +17% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7916 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3088 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1067 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12071 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 50 | 0% | -$766.40 | -52% | — |
| Sell at 2¢ | 415 | 3% | -$1,316.50 | -90% | 33 sec |
| Sell at 3¢ | 273 | 2% | -$1,317.93 | -90% | 47 sec |
| Sell at 5¢ | 202 | 2% | -$1,293.10 | -88% | 50 sec |
| Sell at 10¢ | 132 | 1% | -$1,237.48 | -84% | 64 sec |
| Sell at 25¢ | 76 | 1% | -$1,130.84 | -77% | 82 sec |
| Sell at 50¢ | 50 | 0% | -$1,002.90 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 346 | 4 | 11% | 3% | +10% | -81% | -85% |
| 2–5 min | 3931 | 25 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3154 | 13 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 4636 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 887 | 6 | 5% | 3% | -19% | -90% | -90% |
| HYPE | 886 | 3 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 882 | 2 | 3% | 1% | -71% | -92% | -92% |
| BNB | 881 | 3 | 4% | 2% | -59% | -91% | -92% |
| ETH | 880 | 7 | 5% | 2% | -2% | -89% | -88% |
| NEAR | 876 | 5 | 6% | 3% | -25% | -71% | -73% |
| SOL | 876 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 875 | 4 | 5% | 2% | -40% | -87% | -90% |
| XRP | 873 | 6 | 2% | 1% | -14% | -81% | -81% |
| GOLD | 514 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 501 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 475 | 3 | 3% | 1% | -30% | -95% | -97% |
| COPPER | 440 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 403 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 381 | 3 | 3% | 2% | -27% | -95% | -93% |
| PALLADIUM | 374 | 1 | 1% | 1% | -75% | -98% | -99% |
| EURUSD | 369 | 3 | 3% | 2% | -24% | -69% | -68% |
| GBPUSD | 351 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 314 | 3 | 1% | 1% | -11% | -98% | -97% |
| AUDUSD | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6144 | 26 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 5927 | 24 | 3% | 2% | -53% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1277 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1326 | 4 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2004 | 7 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2326 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 981 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2689 | 8 | 3% | 1% | -65% | -89% | -90% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,045 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 2:59:47 PM | BTC | UP | 13 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:59:47 PM | PALLADIUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:59:47 PM | NATGAS | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:59:15 PM | NEAR | DOWN | 45 sec | +0.199% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:59:15 PM | SILVER | DOWN | 45 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:59:15 PM | DOGE | UP | 45 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:59:15 PM | XRP | DOWN | 45 sec | +0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:58:59 PM | ZEC | DOWN | 61 sec | +0.284% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:58:59 PM | WTI | DOWN | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:56 PM | PLATINUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:24 PM | ETH | DOWN | 2.6 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:24 PM | SOL | DOWN | 2.6 min | +0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:24 PM | HYPE | DOWN | 2.6 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:08 PM | BNB | DOWN | 2.9 min | +0.091% | 2¢ | ❌ Lost | -$0.15 |
| 10/8 2:56:52 PM | COPPER | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:44:58 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:44:58 PM | XRP | DOWN | 1 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:44:58 PM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:44:25 PM | GOLD | UP | 34 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:44:25 PM | COPPER | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:43:54 PM | BTC | DOWN | 65 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:43:54 PM | NEAR | DOWN | 65 sec | +0.264% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:43:54 PM | BNB | DOWN | 65 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:43:54 PM | DOGE | DOWN | 65 sec | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:43:38 PM | PALLADIUM | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:43:38 PM | SILVER | UP | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:43:38 PM | SOL | DOWN | 82 sec | +0.163% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:43:22 PM | HYPE | DOWN | 1.6 min | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:43:22 PM | ETH | DOWN | 1.6 min | +0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:41:31 PM | ZEC | DOWN | 3.5 min | +0.586% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
