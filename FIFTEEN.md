# 15-Minute 1¢ Study

*Updated Wed Nov 11, 6:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4208 finished bets | 1% | $176.90 | +38% | +4.20¢ | $86.05 / $90.85 |

*Expect about **95 buys a day** (~$14.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3929 | $92.60 | +22% |
| Volatility model ≥ 2%, hold to the close | 7718 | $51.35 | +6% |
| Momentum model ≥ 2%, hold to the close | 6404 | -$21.60 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53567 | 53539 | 204 (0%) | 1.07% | -$3,672.75 (-56%) | Hold to the close: -$3,672.75 (-56%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32241 | 4.7% | 0.4% (131) | -673% | ❌ Worse |
| Momentum model | 32241 | 4.6% | 0.4% (131) | -697% | ❌ Worse |
| Mean-reversion model | 32241 | 8.1% | 0.4% (131) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32241 | 131 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7718 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4208 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2431 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6404 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3929 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2579 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13334 | 92 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9333 | 78 | -7% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6242 | 56 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32446 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12798 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8295 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53539 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 204 | 0% | -$3,672.75 | -56% | — |
| Sell at 2¢ | 2134 | 4% | -$5,693.91 | -87% | 47 sec |
| Sell at 3¢ | 1453 | 3% | -$5,682.08 | -87% | 48 sec |
| Sell at 5¢ | 1010 | 2% | -$5,564.25 | -85% | 63 sec |
| Sell at 10¢ | 609 | 1% | -$5,338.96 | -82% | 65 sec |
| Sell at 25¢ | 323 | 1% | -$4,955.62 | -76% | 82 sec |
| Sell at 50¢ | 212 | 0% | -$4,495.75 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2678 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17318 | 94 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13513 | 45 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20018 | 52 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3632 | 17 | 5% | 3% | -39% | -88% | -87% |
| SOL | 3628 | 16 | 4% | 2% | -44% | -87% | -86% |
| HYPE | 3621 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3613 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3609 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3603 | 15 | 7% | 3% | -48% | -81% | -81% |
| NEAR | 3584 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3584 | 17 | 5% | 2% | -35% | -87% | -88% |
| XRP | 3572 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1929 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1911 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1881 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1709 | 4 | 3% | 1% | -78% | -96% | -95% |
| EURUSD | 1646 | 5 | 2% | 1% | -72% | -90% | -89% |
| COPPER | 1600 | 6 | 2% | 1% | -65% | -74% | -73% |
| GBPUSD | 1566 | 5 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1565 | 8 | 2% | 1% | -52% | -79% | -78% |
| USDJPY | 1549 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1536 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1105 | 6 | 2% | 1% | -49% | -88% | -88% |
| USDCAD | 1072 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 667 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27121 | 108 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26418 | 96 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5167 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5514 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8336 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9730 | 41 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3691 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 12893 | 59 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,865 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 6:28:33 AM | XRP | DOWN | 87 sec | +0.161% | — | In play | — |
| 11/11 6:27:44 AM | SOL | DOWN | 2.3 min | +0.300% | — | In play | — |
| 11/11 6:27:44 AM | HYPE | DOWN | 2.3 min | +0.242% | — | In play | — |
| 11/11 6:27:12 AM | WTI | DOWN | 2.8 min | — | — | In play | — |
| 11/11 6:27:12 AM | GBPUSD | UP | 2.8 min | — | — | In play | — |
| 11/11 6:26:57 AM | GOLD | UP | 3.0 min | — | — | In play | — |
| 11/11 6:26:57 AM | ZEC | DOWN | 3.0 min | +0.847% | — | In play | — |
| 11/11 6:26:41 AM | USDCAD | DOWN | 3.3 min | — | — | In play | — |
| 11/11 6:25:36 AM | AUDUSD | UP | 4.4 min | — | — | In play | — |
| 11/11 6:23:43 AM | EURUSD | UP | 6.3 min | — | — | In play | — |
| 11/11 6:21:49 AM | USDJPY | DOWN | 8.2 min | — | — | In play | — |
| 11/11 6:14:41 AM | ETH | DOWN | 18 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:14:41 AM | AUDUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:14:41 AM | WTI | UP | 18 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:14:41 AM | DOGE | DOWN | 18 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:14:41 AM | BNB | DOWN | 18 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:14:41 AM | BTC | DOWN | 18 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 6:14:41 AM | ZEC | DOWN | 18 sec | +0.170% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:14:25 AM | USDCAD | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:14:25 AM | SOL | DOWN | 34 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:14:25 AM | PALLADIUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:14:09 AM | NEAR | DOWN | 51 sec | +0.286% | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:13:52 AM | BRENT | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:13:52 AM | HYPE | DOWN | 67 sec | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 6:13:36 AM | XRP | UP | 83 sec | -0.217% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 6:13:36 AM | ZEC | UP | 83 sec | -0.375% | 100¢ | ✅ Won | $13.85 |
| 11/11 6:13:20 AM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 6:12:13 AM | NATGAS | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:12:13 AM | EURUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:12:13 AM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
