# 15-Minute 1¢ Study

*Updated Wed Nov 4, 9:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3680 finished bets | 1% | $136.05 | +33% | +3.70¢ | $89.70 / $46.35 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3414 | $63.80 | +17% |
| Volatility model ≥ 2%, hold to the close | 6815 | $45.40 | +6% |
| Momentum model ≥ 2%, hold to the close | 5622 | -$31.70 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46119 | 46108 | 170 (0%) | 1.07% | -$3,242.45 (-58%) | Hold to the close: -$3,242.45 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28088 | 4.7% | 0.4% (110) | -677% | ❌ Worse |
| Momentum model | 28088 | 4.6% | 0.4% (110) | -704% | ❌ Worse |
| Mean-reversion model | 28088 | 8.1% | 0.4% (110) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28088 | 110 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6815 | 62 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3680 | 39 | +33% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2095 | 24 | +64% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5622 | 44 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3414 | 31 | +17% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2230 | 20 | +26% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11632 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8163 | 69 | -6% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5467 | 49 | +2% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28293 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10999 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6816 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46108 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 170 | 0% | -$3,242.45 | -58% | — |
| Sell at 2¢ | 1813 | 4% | -$4,899.07 | -87% | 47 sec |
| Sell at 3¢ | 1238 | 3% | -$4,887.63 | -87% | 48 sec |
| Sell at 5¢ | 857 | 2% | -$4,785.40 | -85% | 63 sec |
| Sell at 10¢ | 518 | 1% | -$4,579.87 | -81% | 65 sec |
| Sell at 25¢ | 269 | 1% | -$4,256.06 | -76% | 83 sec |
| Sell at 50¢ | 173 | 0% | -$3,880.70 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2289 | 10 | 10% | 4% | -58% | -81% | -83% |
| 2–5 min | 14849 | 79 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11601 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17358 | 42 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3170 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3165 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3157 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3157 | 17 | 5% | 2% | -32% | -85% | -84% |
| DOGE | 3145 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3138 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3124 | 15 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 3122 | 16 | 5% | 2% | -34% | -84% | -84% |
| XRP | 3115 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1700 | 5 | 5% | 2% | -64% | -81% | -83% |
| SILVER | 1654 | 8 | 5% | 2% | -43% | -82% | -82% |
| WTI | 1653 | 5 | 4% | 1% | -64% | -92% | -92% |
| PLATINUM | 1483 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1425 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1397 | 6 | 2% | 1% | -60% | -70% | -70% |
| GBPUSD | 1352 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1341 | 8 | 2% | 1% | -44% | -76% | -75% |
| USDJPY | 1332 | 5 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1329 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 881 | 4 | 2% | 1% | -58% | -86% | -86% |
| USDCAD | 854 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 442 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 260 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 244 | 0 | 2% | 1% | -100% | -96% | -95% |
| 2YRRATE | 243 | 2 | 3% | 0% | -23% | -17% | -17% |
| 5YRRATE | 225 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23382 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22726 | 80 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4546 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4809 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7292 | 26 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 8443 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3195 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12450 | 41 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,684 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 9:14:50 PM | ZEC | DOWN | 9 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:14:34 PM | EURUSD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:14:34 PM | GBPUSD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:14:03 PM | PLATINUM | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:13:47 PM | SILVER | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:13:47 PM | BNB | UP | 72 sec | -0.182% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:13:47 PM | AUDUSD | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:13:47 PM | PALLADIUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:57 PM | XRP | UP | 3.0 min | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:25 PM | BTC | UP | 3.6 min | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:25 PM | SOL | UP | 3.6 min | -0.311% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:25 PM | NATGAS | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:25 PM | COPPER | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:10 PM | DOGE | UP | 3.8 min | -0.315% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:10 PM | ETH | UP | 3.8 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:10:05 PM | NEAR | UP | 4.9 min | -0.792% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:09:32 PM | HYPE | UP | 5.5 min | -0.589% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:59 PM | BRENT | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:59 PM | SILVER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:59 PM | AUDUSD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:27 PM | COPPER | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:58:54 PM | USDJPY | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:58:22 PM | HYPE | UP | 1.6 min | -0.280% | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:58:22 PM | PLATINUM | DOWN | 1.6 min | — | 10¢ | ❌ Lost | -$0.15 |
| 11/4 8:58:22 PM | NEAR | UP | 1.6 min | -0.421% | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:57:32 PM | NATGAS | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:57:16 PM | EURUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:57:01 PM | GBPUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:56:43 PM | GOLD | DOWN | 3.3 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/4 8:55:56 PM | BTC | UP | 4.0 min | -0.226% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
