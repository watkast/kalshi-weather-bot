# 15-Minute 1¢ Study

*Updated Thu Nov 12, 8:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4249 finished bets | 1% | $172.55 | +37% | +4.06¢ | $83.35 / $89.20 |

*Expect about **94 buys a day** (~$14.05/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3985 | $100.30 | +23% |
| Volatility model ≥ 2%, hold to the close | 7821 | $39.20 | +4% |
| Momentum model ≥ 2%, hold to the close | 6494 | -$18.25 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54850 | 54829 | 210 (0%) | 1.07% | -$3,751.35 (-56%) | Hold to the close: -$3,751.35 (-56%) |

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
| Volatility model | 32854 | 4.7% | 0.4% (133) | -667% | ❌ Worse |
| Momentum model | 32854 | 4.6% | 0.4% (133) | -693% | ❌ Worse |
| Mean-reversion model | 32854 | 8.0% | 0.4% (133) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32854 | 133 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7821 | 70 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4249 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2457 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6494 | 52 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3985 | 38 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2612 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13562 | 93 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9476 | 79 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6324 | 56 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33059 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13176 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8594 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54829 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 210 | 0% | -$3,751.35 | -56% | — |
| Sell at 2¢ | 2184 | 4% | -$5,829.51 | -87% | 47 sec |
| Sell at 3¢ | 1488 | 3% | -$5,817.03 | -87% | 49 sec |
| Sell at 5¢ | 1027 | 2% | -$5,701.80 | -85% | 63 sec |
| Sell at 10¢ | 622 | 1% | -$5,470.53 | -82% | 65 sec |
| Sell at 25¢ | 329 | 1% | -$5,084.36 | -76% | 82 sec |
| Sell at 50¢ | 216 | 0% | -$4,603.35 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2742 | 13 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 17738 | 97 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 13821 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20515 | 55 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3700 | 17 | 5% | 3% | -40% | -88% | -87% |
| SOL | 3696 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3689 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3681 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3676 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3672 | 16 | 7% | 3% | -46% | -82% | -81% |
| BTC | 3653 | 18 | 5% | 2% | -32% | -87% | -88% |
| NEAR | 3652 | 17 | 5% | 2% | -40% | -85% | -85% |
| XRP | 3640 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1979 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1964 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1929 | 9 | 5% | 2% | -45% | -83% | -82% |
| PLATINUM | 1759 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1698 | 6 | 3% | 1% | -67% | -90% | -89% |
| COPPER | 1644 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1626 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1613 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1599 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1576 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1152 | 6 | 2% | 1% | -51% | -88% | -89% |
| USDCAD | 1109 | 0 | 3% | 1% | -100% | -96% | -96% |
| BRENT | 712 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 365 | 2 | 4% | 2% | -49% | -67% | -65% |
| 2YRRATE | 347 | 4 | 4% | 2% | +8% | -39% | -38% |
| 30YRRATE | 345 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 321 | 2 | 4% | 2% | -42% | -92% | -94% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27867 | 109 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26962 | 101 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5217 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5610 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8464 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9963 | 41 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3797 | 18 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13478 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13258 | 61 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14961 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,841 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 7:59:59 AM | SOL | DOWN | 1 sec | +0.173% | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:59:59 AM | BNB | DOWN | 1 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:59:59 AM | XRP | DOWN | 1 sec | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:59:59 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:59:32 AM | ZEC | DOWN | 27 sec | +0.197% | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:59:32 AM | BRENT | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:59:32 AM | BTC | UP | 27 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:59:32 AM | HYPE | DOWN | 27 sec | +0.171% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:59:32 AM | PLATINUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:59:05 AM | ETH | DOWN | 54 sec | +0.258% | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:59:01 AM | WTI | DOWN | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:45 AM | NEAR | DOWN | 74 sec | +0.522% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:45 AM | USDJPY | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:45 AM | EURUSD | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:57 AM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:39 AM | AUDUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:39 AM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:35 AM | 10YRRATE | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:31 AM | 30YRRATE | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:31 AM | SILVER | UP | 2.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:57:09 AM | 5YRRATE | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:07 AM | USDCAD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:56:59 AM | 2YRRATE | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:56:59 AM | GOLD | UP | 3.0 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:44:53 AM | SILVER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:44:35 AM | BTC | UP | 25 sec | -0.202% | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:44:08 AM | PALLADIUM | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:43:50 AM | NATGAS | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:42:30 AM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:41:58 AM | GBPUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
