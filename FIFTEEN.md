# 15-Minute 1¢ Study

*Updated Wed Nov 11, 4:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4206 finished bets | 1% | $177.05 | +38% | +4.21¢ | $86.20 / $90.85 |

*Expect about **95 buys a day** (~$14.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3926 | $92.90 | +22% |
| Volatility model ≥ 2%, hold to the close | 7715 | $51.50 | +6% |
| Momentum model ≥ 2%, hold to the close | 6397 | -$21.00 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53441 | 53412 | 203 (0%) | 1.07% | -$3,672.50 (-56%) | Hold to the close: -$3,672.50 (-56%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32184 | 4.7% | 0.4% (130) | -676% | ❌ Worse |
| Momentum model | 32184 | 4.6% | 0.4% (130) | -701% | ❌ Worse |
| Mean-reversion model | 32184 | 8.1% | 0.4% (130) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32184 | 130 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7715 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4206 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2429 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6397 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3926 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2578 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13325 | 92 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9326 | 78 | -7% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6237 | 56 | +2% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32389 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12753 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8270 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53412 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 203 | 0% | -$3,672.50 | -56% | — |
| Sell at 2¢ | 2128 | 4% | -$5,681.22 | -87% | 47 sec |
| Sell at 3¢ | 1447 | 3% | -$5,670.17 | -87% | 48 sec |
| Sell at 5¢ | 1005 | 2% | -$5,553.25 | -85% | 63 sec |
| Sell at 10¢ | 605 | 1% | -$5,329.95 | -82% | 65 sec |
| Sell at 25¢ | 320 | 1% | -$4,951.30 | -76% | 83 sec |
| Sell at 50¢ | 211 | 0% | -$4,488.25 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2674 | 13 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 17292 | 94 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13470 | 44 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 19964 | 52 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3625 | 16 | 5% | 2% | -43% | -88% | -88% |
| SOL | 3622 | 16 | 4% | 2% | -44% | -87% | -86% |
| HYPE | 3615 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3607 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3603 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3597 | 15 | 7% | 3% | -48% | -82% | -81% |
| BTC | 3578 | 17 | 5% | 2% | -35% | -87% | -88% |
| NEAR | 3577 | 17 | 5% | 2% | -38% | -85% | -85% |
| XRP | 3565 | 13 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1923 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1904 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1875 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1702 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1641 | 5 | 2% | 1% | -72% | -90% | -89% |
| COPPER | 1595 | 6 | 2% | 1% | -65% | -73% | -73% |
| GBPUSD | 1561 | 5 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1560 | 8 | 2% | 1% | -52% | -78% | -78% |
| USDJPY | 1543 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1532 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1101 | 6 | 2% | 1% | -49% | -88% | -88% |
| USDCAD | 1067 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 662 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27060 | 107 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 26352 | 96 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5161 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5500 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8321 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9711 | 40 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3688 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13131 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,869 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 4:44:57 AM | USDJPY | DOWN | 3 sec | — | 0¢ | In play | — |
| 11/11 4:44:57 AM | BTC | DOWN | 3 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:44:57 AM | WTI | DOWN | 3 sec | — | 0¢ | In play | — |
| 11/11 4:44:41 AM | SOL | DOWN | 19 sec | +0.019% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:44:25 AM | XRP | DOWN | 35 sec | +0.114% | 0¢ | In play | — |
| 11/11 4:44:25 AM | NEAR | DOWN | 35 sec | +0.071% | 0¢ | In play | — |
| 11/11 4:44:25 AM | ZEC | DOWN | 35 sec | +0.147% | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:44:10 AM | DOGE | DOWN | 50 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:43:52 AM | ETH | UP | 68 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:43:52 AM | COPPER | UP | 68 sec | — | 0¢ | In play | — |
| 11/11 4:43:36 AM | USDCAD | DOWN | 84 sec | — | 0¢ | In play | — |
| 11/11 4:43:20 AM | HYPE | UP | 1.7 min | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 4:43:20 AM | BNB | UP | 1.7 min | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 4:43:05 AM | PLATINUM | UP | 1.9 min | — | 0¢ | In play | — |
| 11/11 4:42:49 AM | PALLADIUM | UP | 2.2 min | — | 0¢ | In play | — |
| 11/11 4:42:33 AM | NATGAS | DOWN | 2.4 min | — | 0¢ | In play | — |
| 11/11 4:40:56 AM | SILVER | UP | 4.0 min | — | 1¢ | In play | — |
| 11/11 4:40:56 AM | AUDUSD | UP | 4.0 min | — | 0¢ | In play | — |
| 11/11 4:40:38 AM | GOLD | UP | 4.4 min | — | 1¢ | In play | — |
| 11/11 4:29:57 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:29:57 AM | SILVER | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:29:57 AM | NEAR | DOWN | 3 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:29:41 AM | USDJPY | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:29:41 AM | WTI | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:29:41 AM | BRENT | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:29:10 AM | USDCAD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:28:20 AM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:28:20 AM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:28:20 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:28:20 AM | SOL | UP | 1.7 min | -0.147% | 6¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
