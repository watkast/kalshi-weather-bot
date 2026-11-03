# 15-Minute 1¢ Study

*Updated Tue Nov 3, 4:43 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3596 finished bets | 1% | $116.45 | +29% | +3.24¢ | $80.20 / $36.25 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3333 | $43.45 | +12% |
| Volatility model ≥ 2%, hold to the close | 6648 | $36.15 | +4% |
| Momentum model ≥ 2%, hold to the close | 5483 | -$45.15 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44345 | 44328 | 165 (0%) | 1.07% | -$3,086.55 (-57%) | Hold to the close: -$3,086.55 (-57%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27279 | 4.7% | 0.4% (107) | -680% | ❌ Worse |
| Momentum model | 27279 | 4.6% | 0.4% (107) | -705% | ❌ Worse |
| Mean-reversion model | 27279 | 8.1% | 0.4% (107) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27279 | 107 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6648 | 60 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3596 | 37 | +29% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2043 | 22 | +54% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5483 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3333 | 29 | +12% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2176 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11288 | 77 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7920 | 66 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5303 | 47 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27484 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10471 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6373 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44328 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,086.55 | -57% | — |
| Sell at 2¢ | 1746 | 4% | -$4,704.59 | -87% | 47 sec |
| Sell at 3¢ | 1195 | 3% | -$4,692.50 | -87% | 49 sec |
| Sell at 5¢ | 828 | 2% | -$4,592.35 | -85% | 63 sec |
| Sell at 10¢ | 499 | 1% | -$4,392.86 | -81% | 66 sec |
| Sell at 25¢ | 262 | 1% | -$4,067.33 | -75% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,695.80 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2133 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14236 | 79 | 7% | 4% | -45% | -86% | -86% |
| 1–2 min | 11194 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16754 | 38 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3079 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3072 | 11 | 4% | 2% | -55% | -90% | -90% |
| BNB | 3066 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3065 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3053 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3050 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3036 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3036 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3027 | 12 | 3% | 1% | -51% | -89% | -88% |
| GOLD | 1625 | 5 | 5% | 2% | -63% | -81% | -83% |
| WTI | 1583 | 5 | 3% | 1% | -62% | -92% | -93% |
| SILVER | 1582 | 7 | 5% | 2% | -48% | -82% | -81% |
| PLATINUM | 1414 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1354 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1336 | 6 | 1% | 1% | -58% | -69% | -69% |
| NATGAS | 1288 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1286 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1266 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1261 | 5 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 816 | 4 | 2% | 1% | -54% | -86% | -85% |
| USDCAD | 779 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 377 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 223 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 215 | 2 | 4% | 0% | -13% | -7% | -6% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22512 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21816 | 77 | 4% | 2% | -59% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4476 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4710 | 18 | 3% | 2% | -42% | -91% | -91% |
| 0.1–0.2% | 7122 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8136 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3032 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10482 | 39 | 4% | 2% | -56% | -86% | -86% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,720 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 4:42:58 PM | BTC | UP | 2.0 min | -0.157% | — | In play | — |
| 11/3 4:42:42 PM | HYPE | UP | 2.3 min | -0.314% | — | In play | — |
| 11/3 4:42:09 PM | COPPER | UP | 2.8 min | — | — | In play | — |
| 11/3 4:42:09 PM | DOGE | UP | 2.8 min | -0.196% | — | In play | — |
| 11/3 4:42:09 PM | ETH | UP | 2.8 min | -0.221% | — | In play | — |
| 11/3 4:41:37 PM | ZEC | UP | 3.4 min | -0.515% | — | In play | — |
| 11/3 4:41:21 PM | SOL | UP | 3.6 min | -0.251% | — | In play | — |
| 11/3 4:29:50 PM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:29:50 PM | BNB | UP | 9 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:29:34 PM | XRP | DOWN | 25 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:29:34 PM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:29:34 PM | DOGE | DOWN | 25 sec | +0.005% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:29:11 PM | BTC | DOWN | 48 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:29:11 PM | ETH | UP | 48 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:28:06 PM | NEAR | DOWN | 1.9 min | +0.200% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:27:31 PM | SOL | DOWN | 2.5 min | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:26:45 PM | ZEC | DOWN | 3.2 min | +0.443% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:26:29 PM | AUDUSD | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:26:13 PM | HYPE | DOWN | 3.8 min | +0.246% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:26:13 PM | USDCAD | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:25:13 PM | GBPUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:24:05 PM | EURUSD | DOWN | 5.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:14:58 PM | XRP | UP | 2 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:14:58 PM | BTC | DOWN | 2 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:14:42 PM | GBPUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:14:26 PM | NEAR | DOWN | 34 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:14:26 PM | DOGE | UP | 34 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:13:55 PM | USDCAD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:13:55 PM | BNB | DOWN | 65 sec | +0.001% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:13:39 PM | USDJPY | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
