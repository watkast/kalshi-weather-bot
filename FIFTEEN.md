# 15-Minute 1¢ Study

*Updated Sat Oct 24, 1:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2549 finished bets | 1% | $103.10 | +36% | +4.04¢ | $42.65 / $60.45 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2356 | $75.30 | +29% |
| Volatility model ≥ 2%, hold to the close | 4716 | $24.35 | +4% |
| Momentum model ≥ 2%, hold to the close | 3925 | $0.60 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30710 | 30702 | 119 (0%) | 1.07% | -$2,075.30 (-55%) | Hold to the close: -$2,075.30 (-55%) |

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
| Volatility model | 19495 | 4.7% | 0.4% (84) | -629% | ❌ Worse |
| Momentum model | 19495 | 4.6% | 0.4% (84) | -655% | ❌ Worse |
| Mean-reversion model | 19495 | 7.9% | 0.4% (84) | -759% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19495 | 84 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4716 | 43 | +4% | -78% | -76% | -73% |
| Volatility model ≥ 5% | 2549 | 28 | +36% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1453 | 18 | +74% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 3925 | 33 | +0% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2356 | 24 | +29% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1545 | 16 | +42% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7834 | 55 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5478 | 46 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3644 | 33 | +3% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19695 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30702 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,075.30 | -55% | — |
| Sell at 2¢ | 1145 | 4% | -$3,275.60 | -88% | 47 sec |
| Sell at 3¢ | 787 | 3% | -$3,266.37 | -87% | 48 sec |
| Sell at 5¢ | 552 | 2% | -$3,214.50 | -86% | 61 sec |
| Sell at 10¢ | 340 | 1% | -$3,085.90 | -82% | 64 sec |
| Sell at 25¢ | 187 | 1% | -$2,842.33 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,560.55 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1313 | 7 | 11% | 4% | -49% | -80% | -82% |
| 2–5 min | 9797 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7803 | 30 | 3% | 1% | -58% | -92% | -91% |
| Under 1 min | 11785 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2207 | 12 | 5% | 2% | -32% | -89% | -89% |
| HYPE | 2199 | 8 | 5% | 3% | -55% | -88% | -86% |
| BNB | 2197 | 12 | 5% | 2% | -32% | -83% | -82% |
| SOL | 2192 | 6 | 4% | 2% | -66% | -92% | -91% |
| ETH | 2189 | 11 | 6% | 3% | -40% | -86% | -85% |
| DOGE | 2184 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2180 | 9 | 3% | 1% | -49% | -88% | -88% |
| NEAR | 2175 | 12 | 5% | 3% | -28% | -81% | -81% |
| BTC | 2172 | 12 | 5% | 2% | -26% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15509 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15193 | 54 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3276 | 18 | 2% | 1% | -8% | -79% | -78% |
| 0.05–0.1% | 3393 | 11 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5068 | 19 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5752 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2202 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7594 | 32 | 4% | 2% | -52% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8385 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,640 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 1:44:53 AM | ETH | DOWN | 7 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:44:53 AM | HYPE | UP | 7 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:44:37 AM | SOL | DOWN | 23 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:44:37 AM | BNB | UP | 23 sec | -0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 1:44:21 AM | DOGE | UP | 39 sec | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 1:44:21 AM | BTC | DOWN | 39 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 1:44:06 AM | NEAR | UP | 53 sec | -0.292% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:44:06 AM | ZEC | UP | 53 sec | -0.143% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:43:18 AM | XRP | UP | 1.7 min | -0.194% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:29:43 AM | HYPE | UP | 16 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:29:27 AM | ETH | UP | 32 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 1:29:10 AM | NEAR | UP | 49 sec | -0.233% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:29:10 AM | XRP | UP | 49 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:29:10 AM | BNB | UP | 49 sec | -0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 1:28:54 AM | ZEC | UP | 65 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:28:22 AM | DOGE | UP | 1.6 min | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 1:27:49 AM | SOL | UP | 2.2 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 1:14:55 AM | DOGE | DOWN | 5 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:14:39 AM | XRP | DOWN | 21 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:14:39 AM | BTC | DOWN | 21 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:14:08 AM | ETH | DOWN | 52 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 1:14:08 AM | NEAR | DOWN | 52 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 1:14:08 AM | ZEC | UP | 52 sec | -0.234% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 1:13:52 AM | SOL | DOWN | 68 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/24 1:13:52 AM | BNB | DOWN | 68 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 1:10:22 AM | HYPE | UP | 4.6 min | -0.439% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 12:59:39 AM | ETH | DOWN | 20 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/24 12:59:23 AM | BTC | DOWN | 36 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 12:59:23 AM | XRP | DOWN | 36 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 12:59:23 AM | NEAR | DOWN | 36 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
