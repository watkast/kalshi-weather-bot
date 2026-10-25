# 15-Minute 1¢ Study

*Updated Sun Oct 25, 10:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2661 finished bets | 1% | $89.90 | +30% | +3.38¢ | $36.80 / $53.10 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2449 | $65.10 | +24% |
| Volatility model ≥ 2%, hold to the close | 4918 | -$1.15 | -0% |
| Momentum model ≥ 2%, hold to the close | 4094 | -$19.05 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31533 | 31525 | 120 (0%) | 1.07% | -$2,152.65 (-56%) | Hold to the close: -$2,152.65 (-56%) |

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
| Volatility model | 20318 | 4.6% | 0.4% (85) | -645% | ❌ Worse |
| Momentum model | 20318 | 4.5% | 0.4% (85) | -669% | ❌ Worse |
| Mean-reversion model | 20318 | 7.9% | 0.4% (85) | -781% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20318 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4918 | 43 | -0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2661 | 28 | +30% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1508 | 18 | +67% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 4094 | 33 | -4% | -80% | -80% | -76% |
| Momentum model ≥ 5% | 2449 | 24 | +24% | -76% | -76% | -71% |
| Momentum model ≥ 10% | 1599 | 16 | +37% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 8198 | 56 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5743 | 47 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3826 | 33 | -3% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20518 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31525 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,152.65 | -56% | — |
| Sell at 2¢ | 1167 | 4% | -$3,361.23 | -88% | 47 sec |
| Sell at 3¢ | 799 | 3% | -$3,353.04 | -87% | 48 sec |
| Sell at 5¢ | 559 | 2% | -$3,301.30 | -86% | 61 sec |
| Sell at 10¢ | 345 | 1% | -$3,170.70 | -83% | 64 sec |
| Sell at 25¢ | 189 | 1% | -$2,927.06 | -76% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,645.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1387 | 7 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 10096 | 55 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7988 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12050 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2299 | 12 | 5% | 2% | -34% | -89% | -89% |
| HYPE | 2293 | 8 | 5% | 3% | -57% | -89% | -87% |
| BNB | 2288 | 13 | 5% | 2% | -30% | -84% | -83% |
| SOL | 2285 | 6 | 3% | 2% | -67% | -92% | -92% |
| ETH | 2281 | 11 | 6% | 3% | -42% | -86% | -86% |
| DOGE | 2274 | 4 | 4% | 2% | -78% | -91% | -90% |
| XRP | 2271 | 9 | 3% | 1% | -51% | -88% | -88% |
| NEAR | 2268 | 12 | 5% | 2% | -31% | -82% | -81% |
| BTC | 2259 | 12 | 5% | 2% | -29% | -88% | -89% |
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
| UP (bought YES) | 15950 | 66 | 4% | 2% | -52% | -87% | -87% |
| DOWN (bought NO) | 15575 | 54 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3424 | 18 | 2% | 1% | -11% | -80% | -79% |
| 0.05–0.1% | 3526 | 11 | 3% | 2% | -54% | -92% | -92% |
| 0.1–0.2% | 5306 | 20 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 5981 | 28 | 6% | 3% | -48% | -87% | -86% |
| Over 0.5% | 2277 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7714 | 35 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7332 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,787 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 9:59:56 AM | DOGE | DOWN | 4 sec | -0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:59:56 AM | BNB | DOWN | 4 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:59:08 AM | BTC | UP | 52 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:58:37 AM | SOL | UP | 83 sec | -0.095% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:58:37 AM | XRP | UP | 83 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:57:49 AM | BNB | UP | 2.2 min | -0.115% | 100¢ | ✅ Won | $13.85 |
| 10/25 9:57:33 AM | ETH | UP | 2.4 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:55:51 AM | ZEC | UP | 4.2 min | -0.493% | 2¢ | ❌ Lost | -$0.15 |
| 10/25 9:55:34 AM | HYPE | UP | 4.4 min | -0.518% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:54:00 AM | NEAR | DOWN | 6.0 min | +0.980% | 2¢ | ❌ Lost | -$0.15 |
| 10/25 9:40:59 AM | BTC | DOWN | 4.0 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:39:57 AM | BNB | DOWN | 5.0 min | +0.280% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:39:41 AM | SOL | DOWN | 5.3 min | +0.542% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:39:24 AM | DOGE | DOWN | 5.6 min | +0.419% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:39:24 AM | ZEC | DOWN | 5.6 min | +0.516% | 6¢ | ❌ Lost | -$0.15 |
| 10/25 9:39:24 AM | HYPE | DOWN | 5.6 min | +0.517% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:38:52 AM | XRP | DOWN | 6.1 min | +0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:38:37 AM | NEAR | DOWN | 6.4 min | +0.896% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:38:22 AM | ETH | DOWN | 6.6 min | +0.460% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:28:21 AM | ZEC | UP | 1.6 min | -0.334% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:26:46 AM | BNB | UP | 3.2 min | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:26:46 AM | HYPE | UP | 3.2 min | -0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:25:31 AM | NEAR | UP | 4.5 min | -0.873% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:25:15 AM | XRP | UP | 4.7 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:24:43 AM | BTC | UP | 5.3 min | -0.187% | 2¢ | ❌ Lost | -$0.15 |
| 10/25 9:24:25 AM | DOGE | UP | 5.6 min | -0.360% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:23:55 AM | SOL | UP | 6.1 min | -0.391% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:23:39 AM | ETH | UP | 6.3 min | -0.286% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:14:45 AM | ETH | DOWN | 15 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:14:29 AM | BNB | DOWN | 31 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
