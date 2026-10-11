# 15-Minute 1¢ Study

*Updated Sun Oct 11, 3:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1068 finished bets | 1% | $23.15 | +20% | +2.17¢ | -$1.90 / $25.05 |

*Expect about **81 buys a day** (~$12.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1024 | $1.15 | +1% |
| 5+ min left, hold to the close | 400 | -$3.10 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1068 | -$21.35 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14390 | 14376 | 56 (0%) | 1.07% | -$953.75 (-55%) | Hold to the close: -$953.75 (-55%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 9531 | 4.4% | 0.4% (39) | -657% | ❌ Worse |
| Momentum model | 9531 | 4.4% | 0.4% (39) | -686% | ❌ Worse |
| Mean-reversion model | 9531 | 7.1% | 0.4% (39) | -763% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9531 | 39 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1875 | 14 | -14% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 1068 | 10 | +20% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 670 | 8 | +71% | -58% | -58% | -54% |
| Momentum model ≥ 2% | 1649 | 11 | -19% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1024 | 8 | +1% | -74% | -74% | -72% |
| Momentum model ≥ 10% | 709 | 6 | +19% | -66% | -66% | -63% |
| Mean-reversion model ≥ 2% | 3317 | 23 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2259 | 17 | -17% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1509 | 13 | -1% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9729 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14376 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$953.75 | -55% | — |
| Sell at 2¢ | 487 | 3% | -$1,569.13 | -90% | 33 sec |
| Sell at 3¢ | 320 | 2% | -$1,570.95 | -90% | 47 sec |
| Sell at 5¢ | 234 | 2% | -$1,543.65 | -89% | 50 sec |
| Sell at 10¢ | 153 | 1% | -$1,467.32 | -84% | 64 sec |
| Sell at 25¢ | 87 | 1% | -$1,351.78 | -78% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,213.00 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 396 | 4 | 11% | 3% | -4% | -81% | -86% |
| 2–5 min | 4641 | 28 | 6% | 3% | -41% | -89% | -89% |
| 1–2 min | 3782 | 15 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5553 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1089 | 6 | 4% | 3% | -33% | -90% | -90% |
| HYPE | 1089 | 3 | 4% | 2% | -66% | -90% | -89% |
| DOGE | 1086 | 2 | 4% | 2% | -77% | -91% | -91% |
| BNB | 1085 | 5 | 4% | 2% | -44% | -91% | -92% |
| ETH | 1080 | 8 | 5% | 2% | -9% | -89% | -89% |
| SOL | 1078 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1076 | 4 | 5% | 2% | -51% | -88% | -91% |
| NEAR | 1074 | 6 | 5% | 2% | -27% | -75% | -76% |
| XRP | 1072 | 6 | 2% | 1% | -30% | -84% | -84% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7234 | 29 | 3% | 2% | -54% | -89% | -89% |
| DOWN (bought NO) | 7142 | 27 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1727 | 9 | 2% | 1% | -14% | -74% | -74% |
| 0.05–0.1% | 1737 | 5 | 3% | 1% | -59% | -92% | -92% |
| 0.1–0.2% | 2492 | 8 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 2687 | 14 | 5% | 3% | -43% | -89% | -89% |
| Over 0.5% | 1083 | 5 | 6% | 2% | -53% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3628 | 19 | 4% | 2% | -39% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,421 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 3:12:48 AM | BTC | DOWN | 2.2 min | +0.059% | — | In play | — |
| 10/11 3:12:02 AM | SOL | DOWN | 3.0 min | +0.225% | — | In play | — |
| 10/11 3:12:02 AM | ZEC | DOWN | 3.0 min | +0.716% | — | In play | — |
| 10/11 3:12:02 AM | XRP | DOWN | 3.0 min | +0.179% | — | In play | — |
| 10/11 3:11:48 AM | DOGE | DOWN | 3.2 min | +0.171% | — | In play | — |
| 10/11 3:11:48 AM | HYPE | DOWN | 3.2 min | +0.356% | — | In play | — |
| 10/11 3:11:00 AM | ETH | DOWN | 4.0 min | +0.108% | — | In play | — |
| 10/11 2:59:33 AM | BNB | UP | 27 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:59:17 AM | ETH | DOWN | 43 sec | +0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:59:02 AM | BTC | UP | 58 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:58:46 AM | DOGE | DOWN | 74 sec | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:58:32 AM | SOL | DOWN | 88 sec | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:58:16 AM | ZEC | DOWN | 1.7 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:58:16 AM | HYPE | UP | 1.7 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:44:40 AM | ETH | DOWN | 20 sec | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:43:38 AM | XRP | DOWN | 81 sec | +0.122% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:43:24 AM | SOL | DOWN | 1.6 min | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:43:08 AM | BTC | DOWN | 1.9 min | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:41:27 AM | BNB | DOWN | 3.5 min | +0.035% | 2¢ | ❌ Lost | -$0.15 |
| 10/11 2:41:27 AM | DOGE | DOWN | 3.5 min | +0.180% | 2¢ | ❌ Lost | -$0.15 |
| 10/11 2:40:56 AM | HYPE | DOWN | 4.0 min | +0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:39:05 AM | NEAR | DOWN | 5.9 min | +0.903% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:38:18 AM | ZEC | DOWN | 6.7 min | +0.589% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:29:45 AM | HYPE | DOWN | 15 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:29:45 AM | ZEC | DOWN | 15 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:29:29 AM | NEAR | DOWN | 31 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:29:13 AM | DOGE | UP | 47 sec | -0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:28:58 AM | XRP | UP | 61 sec | -0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:28:58 AM | SOL | UP | 61 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:28:12 AM | BTC | UP | 1.8 min | -0.059% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
