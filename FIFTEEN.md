# 15-Minute 1¢ Study

*Updated Thu Oct 8, 9:44 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 782 finished bets | 1% | $27.70 | +33% | +3.54¢ | -$13.40 / $41.10 |

*Expect about **75 buys a day** (~$11.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 774 | $15.50 | +19% |
| 5+ min left, hold to the close | 332 | $6.95 | +14% |
| Volatility model ≥ 5%, sell at 50¢ | 782 | -$2.30 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11797 | 11780 | 49 (0%) | 1.07% | -$745.75 (-52%) | Hold to the close: -$745.75 (-52%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7557 | 4.0% | 0.4% (33) | -564% | ❌ Worse |
| Momentum model | 7557 | 4.1% | 0.4% (33) | -596% | ❌ Worse |
| Mean-reversion model | 7557 | 6.7% | 0.4% (33) | -661% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7557 | 33 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1433 | 12 | -3% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 782 | 8 | +33% | -64% | -63% | -59% |
| Volatility model ≥ 10% | 487 | 6 | +82% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1273 | 10 | -5% | -75% | -76% | -73% |
| Momentum model ≥ 5% | 774 | 7 | +19% | -68% | -69% | -66% |
| Momentum model ≥ 10% | 534 | 6 | +62% | -57% | -58% | -54% |
| Mean-reversion model ≥ 2% | 2599 | 19 | -21% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1757 | 15 | -5% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1159 | 11 | +9% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7754 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3002 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1024 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11780 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$745.75 | -52% | — |
| Sell at 2¢ | 409 | 3% | -$1,283.41 | -90% | 34 sec |
| Sell at 3¢ | 271 | 2% | -$1,284.06 | -90% | 47 sec |
| Sell at 5¢ | 200 | 2% | -$1,259.75 | -88% | 50 sec |
| Sell at 10¢ | 131 | 1% | -$1,204.14 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,099.50 | -77% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$975.00 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 328 | 4 | 11% | 4% | +16% | -81% | -84% |
| 2–5 min | 3841 | 25 | 7% | 3% | -36% | -88% | -89% |
| 1–2 min | 3085 | 12 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4522 | 8 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 869 | 6 | 4% | 3% | -18% | -90% | -90% |
| HYPE | 868 | 3 | 5% | 3% | -57% | -89% | -87% |
| DOGE | 864 | 2 | 3% | 2% | -71% | -92% | -91% |
| BNB | 863 | 3 | 4% | 2% | -58% | -91% | -92% |
| ETH | 862 | 7 | 5% | 3% | +1% | -89% | -88% |
| NEAR | 858 | 5 | 6% | 3% | -24% | -71% | -73% |
| SOL | 858 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 857 | 4 | 5% | 2% | -39% | -87% | -90% |
| XRP | 855 | 5 | 2% | 1% | -27% | -82% | -82% |
| GOLD | 502 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 488 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 462 | 3 | 3% | 1% | -29% | -95% | -97% |
| COPPER | 430 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 392 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 367 | 3 | 3% | 2% | -24% | -95% | -93% |
| PALLADIUM | 361 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 360 | 3 | 3% | 2% | -22% | -68% | -67% |
| GBPUSD | 340 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 303 | 3 | 1% | 1% | -8% | -98% | -97% |
| AUDUSD | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 9 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6002 | 26 | 4% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 5778 | 23 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1263 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1311 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1967 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2286 | 12 | 6% | 3% | -42% | -89% | -88% |
| Over 0.5% | 925 | 5 | 6% | 2% | -45% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 2863 | 17 | 4% | 2% | -33% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,059 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 9:43:59 AM | DOGE | UP | 60 sec | -0.586% | — | In play | — |
| 10/8 9:43:43 AM | HYPE | UP | 77 sec | -0.524% | — | In play | — |
| 10/8 9:43:43 AM | BTC | UP | 77 sec | -0.163% | — | In play | — |
| 10/8 9:43:43 AM | ZEC | UP | 77 sec | -0.909% | — | In play | — |
| 10/8 9:43:43 AM | COPPER | UP | 77 sec | — | — | In play | — |
| 10/8 9:43:28 AM | PALLADIUM | UP | 1.5 min | — | — | In play | — |
| 10/8 9:42:56 AM | NEAR | UP | 2.1 min | -1.569% | — | In play | — |
| 10/8 9:42:23 AM | USDJPY | UP | 2.6 min | — | — | In play | — |
| 10/8 9:42:23 AM | AUDUSD | UP | 2.6 min | — | — | In play | — |
| 10/8 9:42:07 AM | ETH | UP | 2.9 min | -0.688% | — | In play | — |
| 10/8 9:29:59 AM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:29:59 AM | USDJPY | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:29:59 AM | AUDUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:29:59 AM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:29:59 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:29:28 AM | GBPUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:29:12 AM | SILVER | DOWN | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:28:25 AM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:28:09 AM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:28:09 AM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:28:09 AM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:27:03 AM | ZEC | UP | 2.9 min | -1.684% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:25:46 AM | XRP | UP | 4.2 min | -2.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:25:31 AM | DOGE | UP | 4.5 min | -2.530% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:25:15 AM | ETH | UP | 4.7 min | -1.571% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:24:43 AM | SOL | UP | 5.3 min | -1.786% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:23:40 AM | HYPE | UP | 6.3 min | -1.254% | 4¢ | ❌ Lost | -$0.15 |
| 10/8 9:23:40 AM | BTC | UP | 6.3 min | -0.840% | 3¢ | ❌ Lost | -$0.15 |
| 10/8 9:23:07 AM | BNB | UP | 6.9 min | -1.718% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:22:36 AM | NEAR | UP | 7.4 min | -2.731% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
