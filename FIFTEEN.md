# 15-Minute 1¢ Study

*Updated Tue Nov 17, 4:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4483 finished bets | 1% | $218.70 | +44% | +4.88¢ | $82.80 / $135.90 |

*Expect about **88 buys a day** (~$13.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4218 | $119.20 | +26% |
| Volatility model ≥ 2%, hold to the close | 8360 | $86.70 | +9% |
| Momentum model ≥ 2%, hold to the close | 6929 | $3.60 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59983 | 59949 | 235 (0%) | 1.07% | -$4,004.35 (-55%) | Hold to the close: -$4,004.35 (-55%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35952 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 35952 | 4.4% | 0.4% (154) | -647% | ❌ Worse |
| Mean-reversion model | 35952 | 7.9% | 0.4% (154) | -754% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35952 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8360 | 78 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4483 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2573 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6929 | 57 | +0% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4218 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2748 | 26 | +34% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14740 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10258 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6813 | 64 | +7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36158 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14237 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9554 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59949 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 235 | 0% | -$4,004.35 | -55% | — |
| Sell at 2¢ | 2419 | 4% | -$6,371.41 | -87% | 47 sec |
| Sell at 3¢ | 1632 | 3% | -$6,363.87 | -87% | 48 sec |
| Sell at 5¢ | 1119 | 2% | -$6,245.00 | -86% | 63 sec |
| Sell at 10¢ | 682 | 1% | -$5,994.93 | -82% | 65 sec |
| Sell at 25¢ | 365 | 1% | -$5,554.20 | -76% | 80 sec |
| Sell at 50¢ | 242 | 0% | -$5,002.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3022 | 17 | 11% | 4% | -47% | -81% | -83% |
| 2–5 min | 19431 | 107 | 7% | 3% | -46% | -86% | -87% |
| 1–2 min | 15041 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22442 | 60 | 1% | 0% | -62% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4044 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4042 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4034 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 4023 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 4023 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4017 | 19 | 7% | 3% | -41% | -82% | -82% |
| NEAR | 3997 | 18 | 5% | 2% | -41% | -85% | -86% |
| BTC | 3997 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 3981 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2131 | 5 | 5% | 2% | -71% | -83% | -84% |
| WTI | 2110 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2068 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1884 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1835 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1766 | 6 | 2% | 1% | -68% | -76% | -76% |
| GBPUSD | 1762 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1741 | 10 | 2% | 1% | -46% | -75% | -75% |
| USDJPY | 1722 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1695 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1279 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1226 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 842 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 435 | 2 | 3% | 1% | -57% | -73% | -71% |
| 2YRRATE | 420 | 4 | 4% | 2% | -11% | -49% | -48% |
| 30YRRATE | 403 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 391 | 2 | 4% | 2% | -52% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30509 | 121 | 4% | 2% | -54% | -88% | -88% |
| DOWN (bought NO) | 29440 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5445 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5901 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9062 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11187 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4554 | 23 | 7% | 3% | -47% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14666 | 63 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 16360 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,066 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 3:59:56 PM | HYPE | UP | 3 sec | -0.123% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:59:56 PM | AUDUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:59:40 PM | DOGE | DOWN | 19 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:59:40 PM | ETH | UP | 19 sec | -0.135% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:59:40 PM | NEAR | UP | 19 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 3:59:09 PM | BNB | UP | 50 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:59:09 PM | ZEC | UP | 50 sec | -0.265% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:59:09 PM | SOL | DOWN | 50 sec | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 3:58:53 PM | BTC | UP | 66 sec | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 3:58:21 PM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:57:50 PM | XRP | DOWN | 2.2 min | +0.247% | 1¢ | ❌ Lost | $0.00 |
| 11/17 3:57:34 PM | USDJPY | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:44:46 PM | BRENT | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:44:46 PM | WTI | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:44:46 PM | AUDUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:44:30 PM | NEAR | DOWN | 30 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:43:59 PM | DOGE | DOWN | 60 sec | +0.069% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:43:59 PM | HYPE | DOWN | 60 sec | +0.179% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:43:26 PM | XRP | DOWN | 1.6 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 3:42:39 PM | SOL | DOWN | 2.3 min | +0.253% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:42:23 PM | BNB | DOWN | 2.6 min | +0.123% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:41:31 PM | ZEC | DOWN | 3.5 min | +0.477% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 3:41:15 PM | BTC | DOWN | 3.7 min | +0.305% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 3:41:15 PM | ETH | DOWN | 3.7 min | +0.336% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 3:29:53 PM | XRP | DOWN | 6 sec | +0.103% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:29:35 PM | BRENT | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:29:03 PM | AUDUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:29:03 PM | NEAR | DOWN | 57 sec | +0.172% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:28:47 PM | ETH | DOWN | 72 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:28:31 PM | DOGE | DOWN | 88 sec | +0.175% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
