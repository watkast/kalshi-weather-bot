# 15-Minute 1¢ Study

*Updated Mon Oct 26, 5:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2740 finished bets | 1% | $80.75 | +26% | +2.95¢ | $31.55 / $49.20 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2545 | $54.30 | +19% |
| Volatility model ≥ 2%, hold to the close | 5083 | -$20.80 | -3% |
| Momentum model ≥ 2%, hold to the close | 4232 | -$34.20 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32646 | 32632 | 121 (0%) | 1.07% | -$2,270.35 (-57%) | Hold to the close: -$2,270.35 (-57%) |

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
| Volatility model | 20983 | 4.6% | 0.4% (85) | -661% | ❌ Worse |
| Momentum model | 20983 | 4.5% | 0.4% (85) | -685% | ❌ Worse |
| Mean-reversion model | 20983 | 7.9% | 0.4% (85) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20983 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5083 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2740 | 28 | +26% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1550 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4232 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2545 | 24 | +19% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 1657 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8476 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5935 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3950 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21183 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7610 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3839 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32632 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 121 | 0% | -$2,270.35 | -57% | — |
| Sell at 2¢ | 1222 | 4% | -$3,478.63 | -88% | 47 sec |
| Sell at 3¢ | 838 | 3% | -$3,469.53 | -88% | 48 sec |
| Sell at 5¢ | 583 | 2% | -$3,417.40 | -86% | 61 sec |
| Sell at 10¢ | 362 | 1% | -$3,280.13 | -83% | 65 sec |
| Sell at 25¢ | 194 | 1% | -$3,042.21 | -77% | 82 sec |
| Sell at 50¢ | 125 | 0% | -$2,756.60 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1440 | 7 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 10458 | 56 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8265 | 30 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12465 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2374 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2366 | 8 | 5% | 3% | -58% | -88% | -87% |
| BNB | 2363 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2360 | 6 | 4% | 2% | -68% | -92% | -92% |
| ETH | 2354 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2346 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2343 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2342 | 12 | 5% | 2% | -33% | -82% | -81% |
| BTC | 2335 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1229 | 4 | 4% | 2% | -61% | -81% | -83% |
| SILVER | 1196 | 6 | 4% | 2% | -41% | -82% | -81% |
| WTI | 1172 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1043 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1019 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 975 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 968 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 931 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 920 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 903 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 465 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 424 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16538 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 16094 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3528 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3636 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5484 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6187 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2344 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8270 | 33 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,797 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 5:24:51 AM | SOL | DOWN | 5.2 min | +0.268% | — | In play | — |
| 10/26 5:24:51 AM | XRP | DOWN | 5.2 min | +0.358% | — | In play | — |
| 10/26 5:24:51 AM | BNB | DOWN | 5.2 min | +0.163% | — | In play | — |
| 10/26 5:24:51 AM | HYPE | DOWN | 5.2 min | +0.371% | — | In play | — |
| 10/26 5:24:51 AM | DOGE | DOWN | 5.2 min | +0.330% | — | In play | — |
| 10/26 5:24:51 AM | NEAR | DOWN | 5.2 min | +0.694% | — | In play | — |
| 10/26 5:14:58 AM | AUDUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:14:42 AM | PLATINUM | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:14:42 AM | COPPER | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:14:42 AM | GBPUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:13:21 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:13:21 AM | BRENT | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:13:05 AM | USDCAD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:13:05 AM | NATGAS | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:12:32 AM | SILVER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:12:00 AM | ZEC | UP | 3.0 min | -0.442% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:11:43 AM | GOLD | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:11:43 AM | NEAR | UP | 3.3 min | -0.682% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:11:27 AM | USDJPY | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:11:11 AM | SOL | UP | 3.8 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:11:11 AM | XRP | UP | 3.8 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:11:11 AM | HYPE | UP | 3.8 min | -0.416% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:11:11 AM | WTI | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:11:11 AM | ETH | UP | 3.8 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:10:55 AM | BNB | UP | 4.1 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:10:55 AM | BTC | UP | 4.1 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:10:38 AM | DOGE | UP | 4.3 min | -0.301% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 4:59:59 AM | NATGAS | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:59:43 AM | USDCAD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:59:27 AM | EURUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
