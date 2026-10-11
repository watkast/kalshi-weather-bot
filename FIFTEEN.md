# 15-Minute 1¢ Study

*Updated Sun Oct 11, 3:44 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1125 finished bets | 1% | $45.90 | +38% | +4.08¢ | $23.40 / $22.50 |

*Expect about **83 buys a day** (~$12.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1078 | $24.35 | +21% |
| 5+ min left, hold to the close | 403 | -$3.55 | -6% |
| Volatility model ≥ 2%, hold to the close | 1963 | -$11.95 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14749 | 14733 | 59 (0%) | 1.07% | -$949.70 (-53%) | Hold to the close: -$949.70 (-53%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 9887 | 4.5% | 0.4% (42) | -678% | ❌ Worse |
| Momentum model | 9887 | 4.5% | 0.4% (42) | -706% | ❌ Worse |
| Mean-reversion model | 9887 | 7.2% | 0.4% (42) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9887 | 42 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1963 | 16 | -5% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 1125 | 12 | +38% | -70% | -69% | -67% |
| Volatility model ≥ 10% | 710 | 8 | +63% | -60% | -60% | -56% |
| Momentum model ≥ 2% | 1730 | 13 | -9% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1078 | 10 | +21% | -74% | -75% | -72% |
| Momentum model ≥ 10% | 747 | 7 | +34% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3449 | 25 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2356 | 19 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1581 | 13 | -4% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10085 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1204 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14733 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$949.70 | -53% | — |
| Sell at 2¢ | 506 | 3% | -$1,602.14 | -90% | 33 sec |
| Sell at 3¢ | 333 | 2% | -$1,603.83 | -90% | 47 sec |
| Sell at 5¢ | 244 | 2% | -$1,575.10 | -89% | 50 sec |
| Sell at 10¢ | 161 | 1% | -$1,494.79 | -84% | 64 sec |
| Sell at 25¢ | 92 | 1% | -$1,373.18 | -77% | 81 sec |
| Sell at 50¢ | 60 | 0% | -$1,230.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 399 | 4 | 11% | 3% | -5% | -81% | -86% |
| 2–5 min | 4768 | 31 | 6% | 3% | -36% | -88% | -89% |
| 1–2 min | 3866 | 15 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5696 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1131 | 6 | 4% | 3% | -35% | -90% | -90% |
| HYPE | 1130 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1124 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1122 | 5 | 4% | 2% | -46% | -91% | -92% |
| ETH | 1121 | 8 | 5% | 2% | -13% | -90% | -89% |
| SOL | 1119 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1115 | 5 | 5% | 2% | -41% | -88% | -91% |
| XRP | 1112 | 7 | 2% | 1% | -22% | -84% | -84% |
| NEAR | 1111 | 6 | 5% | 2% | -29% | -75% | -76% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 354 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7413 | 31 | 3% | 2% | -51% | -89% | -89% |
| DOWN (bought NO) | 7320 | 28 | 3% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1827 | 9 | 2% | 1% | -18% | -76% | -75% |
| 0.05–0.1% | 1796 | 6 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2574 | 8 | 4% | 2% | -62% | -91% | -92% |
| 0.2–0.5% | 2775 | 16 | 5% | 3% | -37% | -89% | -88% |
| Over 0.5% | 1110 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3428 | 9 | 3% | 1% | -69% | -90% | -91% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,516 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 3:44:22 PM | DOGE | DOWN | 37 sec | +0.079% | — | In play | — |
| 10/11 3:43:50 PM | ETH | DOWN | 70 sec | +0.129% | — | In play | — |
| 10/11 3:43:50 PM | HYPE | DOWN | 70 sec | +0.086% | — | In play | — |
| 10/11 3:43:33 PM | XRP | DOWN | 87 sec | +0.114% | — | In play | — |
| 10/11 3:43:01 PM | ZEC | DOWN | 2.0 min | +0.298% | — | In play | — |
| 10/11 3:42:46 PM | BNB | DOWN | 2.2 min | +0.072% | — | In play | — |
| 10/11 3:42:15 PM | BTC | DOWN | 2.7 min | +0.104% | — | In play | — |
| 10/11 3:41:59 PM | SOL | DOWN | 3.0 min | +0.232% | — | In play | — |
| 10/11 3:40:39 PM | NEAR | DOWN | 4.3 min | +1.992% | — | In play | — |
| 10/11 3:29:09 PM | USDJPY | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:27:18 PM | HYPE | UP | 2.7 min | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:26:47 PM | XRP | UP | 3.2 min | -0.384% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:26:31 PM | DOGE | UP | 3.5 min | -0.509% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:26:31 PM | ETH | UP | 3.5 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:26:31 PM | BNB | UP | 3.5 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:26:15 PM | SOL | UP | 3.7 min | -0.577% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:26:15 PM | BTC | UP | 3.7 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:26:15 PM | NEAR | UP | 3.7 min | -1.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:24:55 PM | ZEC | UP | 5.1 min | -0.837% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:14:42 PM | NEAR | UP | 17 sec | -0.140% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:13:08 PM | BTC | UP | 1.9 min | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:12:20 PM | ETH | UP | 2.6 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:12:20 PM | HYPE | UP | 2.6 min | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:12:20 PM | XRP | UP | 2.6 min | -0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:12:20 PM | ZEC | UP | 2.6 min | -0.375% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:12:04 PM | DOGE | UP | 2.9 min | -0.323% | 0¢ | ❌ Lost | $0.00 |
| 10/11 3:12:04 PM | SOL | UP | 2.9 min | -0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:12:04 PM | BNB | UP | 2.9 min | -0.177% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:59:26 PM | DOGE | DOWN | 34 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:59:26 PM | SOL | UP | 34 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
