# 15-Minute 1¢ Study

*Updated Sun Oct 25, 4:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2687 finished bets | 1% | $86.60 | +28% | +3.22¢ | $35.15 / $51.45 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2473 | $62.25 | +23% |
| Volatility model ≥ 2%, hold to the close | 4963 | -$6.70 | -1% |
| Momentum model ≥ 2%, hold to the close | 4125 | -$22.50 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31744 | 31734 | 120 (0%) | 1.07% | -$2,175.60 (-56%) | Hold to the close: -$2,175.60 (-56%) |

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
| Volatility model | 20523 | 4.6% | 0.4% (85) | -647% | ❌ Worse |
| Momentum model | 20523 | 4.5% | 0.4% (85) | -671% | ❌ Worse |
| Mean-reversion model | 20523 | 7.9% | 0.4% (85) | -784% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20523 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4963 | 43 | -1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2687 | 28 | +28% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1520 | 18 | +65% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 4125 | 33 | -5% | -80% | -80% | -76% |
| Momentum model ≥ 5% | 2473 | 24 | +23% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 1615 | 16 | +36% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8272 | 56 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5795 | 47 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3861 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20723 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3659 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31734 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,175.60 | -56% | — |
| Sell at 2¢ | 1172 | 4% | -$3,382.88 | -88% | 47 sec |
| Sell at 3¢ | 804 | 3% | -$3,374.04 | -88% | 48 sec |
| Sell at 5¢ | 561 | 2% | -$3,322.95 | -86% | 61 sec |
| Sell at 10¢ | 346 | 1% | -$3,192.34 | -83% | 64 sec |
| Sell at 25¢ | 189 | 1% | -$2,950.01 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,668.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1393 | 7 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 10173 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8034 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12130 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2322 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2316 | 8 | 5% | 3% | -57% | -89% | -87% |
| BNB | 2310 | 13 | 5% | 3% | -30% | -84% | -83% |
| SOL | 2307 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2303 | 11 | 6% | 3% | -43% | -86% | -86% |
| DOGE | 2297 | 4 | 4% | 2% | -78% | -91% | -90% |
| XRP | 2293 | 9 | 3% | 1% | -51% | -88% | -88% |
| NEAR | 2292 | 12 | 5% | 2% | -32% | -81% | -81% |
| BTC | 2283 | 12 | 5% | 2% | -30% | -88% | -90% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 940 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 885 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 867 | 5 | 1% | 1% | -46% | -98% | -97% |
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
| UP (bought YES) | 16078 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15656 | 54 | 4% | 1% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3473 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3568 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5363 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6023 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2292 | 10 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7474 | 24 | 4% | 2% | -62% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,823 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 3:58:18 PM | ZEC | UP | 1.7 min | -0.335% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:58:02 PM | SOL | UP | 1.9 min | -0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:57:31 PM | BNB | UP | 2.5 min | -0.192% | 1¢ | In play | — |
| 10/25 3:56:59 PM | ETH | UP | 3.0 min | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:56:44 PM | HYPE | UP | 3.3 min | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:56:44 PM | NEAR | UP | 3.3 min | -0.591% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:56:44 PM | DOGE | UP | 3.3 min | -0.361% | 1¢ | In play | — |
| 10/25 3:56:29 PM | BTC | UP | 3.5 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:56:29 PM | XRP | UP | 3.5 min | -0.286% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:44:57 PM | EURUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:44:57 PM | USDJPY | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:44:25 PM | GBPUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:44:25 PM | NEAR | DOWN | 35 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:44:25 PM | ZEC | UP | 35 sec | -0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:43:21 PM | XRP | UP | 1.6 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:43:21 PM | DOGE | UP | 1.6 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:42:50 PM | BNB | UP | 2.2 min | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:42:02 PM | BTC | UP | 3.0 min | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:42:02 PM | SOL | UP | 3.0 min | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:41:14 PM | HYPE | UP | 3.8 min | -0.472% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:41:14 PM | ETH | UP | 3.8 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:29:40 PM | HYPE | UP | 19 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:29:40 PM | BNB | DOWN | 19 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:29:24 PM | BTC | DOWN | 35 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:29:08 PM | XRP | UP | 51 sec | -0.123% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:29:08 PM | DOGE | DOWN | 51 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:28:37 PM | EURUSD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:25:10 PM | NEAR | UP | 4.8 min | -0.788% | 4¢ | ❌ Lost | -$0.15 |
| 10/25 3:25:10 PM | ZEC | UP | 4.8 min | -0.964% | 1¢ | ❌ Lost | $0.00 |
| 10/25 3:25:10 PM | ETH | UP | 4.8 min | -0.283% | 5¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
