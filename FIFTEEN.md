# 15-Minute 1¢ Study

*Updated Wed Oct 21, 10:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2264 finished bets | 1% | $80.10 | +31% | +3.54¢ | $45.30 / $34.80 |

*Expect about **97 buys a day** (~$14.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2095 | $61.20 | +26% |
| Volatility model ≥ 2%, hold to the close | 4146 | -$18.20 | -4% |
| Momentum model ≥ 2%, hold to the close | 3506 | -$35.55 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26852 | 26841 | 98 (0%) | 1.07% | -$1,899.80 (-58%) | Hold to the close: -$1,899.80 (-58%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 17371 | 4.6% | 0.4% (70) | -663% | ❌ Worse |
| Momentum model | 17371 | 4.6% | 0.4% (70) | -686% | ❌ Worse |
| Mean-reversion model | 17371 | 7.8% | 0.4% (70) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17371 | 70 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4146 | 35 | -4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2264 | 24 | +31% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1297 | 16 | +72% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3506 | 27 | -9% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2095 | 21 | +26% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1378 | 14 | +38% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6871 | 46 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4795 | 38 | -13% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3188 | 26 | -7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17569 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6409 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2863 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26841 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 98 | 0% | -$1,899.80 | -58% | — |
| Sell at 2¢ | 976 | 4% | -$2,878.04 | -88% | 46 sec |
| Sell at 3¢ | 664 | 2% | -$2,872.84 | -88% | 48 sec |
| Sell at 5¢ | 469 | 2% | -$2,826.95 | -86% | 58 sec |
| Sell at 10¢ | 286 | 1% | -$2,729.14 | -83% | 64 sec |
| Sell at 25¢ | 158 | 1% | -$2,524.82 | -77% | 81 sec |
| Sell at 50¢ | 101 | 0% | -$2,296.05 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1081 | 6 | 11% | 4% | -47% | -81% | -84% |
| 2–5 min | 8654 | 44 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6860 | 25 | 3% | 1% | -60% | -93% | -92% |
| Under 1 min | 10242 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1971 | 11 | 5% | 2% | -31% | -90% | -90% |
| BNB | 1964 | 11 | 5% | 2% | -31% | -83% | -82% |
| HYPE | 1962 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1952 | 10 | 6% | 3% | -39% | -87% | -86% |
| DOGE | 1951 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1950 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1943 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1938 | 11 | 6% | 3% | -27% | -79% | -79% |
| BTC | 1938 | 11 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 1048 | 2 | 3% | 1% | -78% | -81% | -83% |
| SILVER | 1011 | 4 | 3% | 1% | -54% | -82% | -82% |
| WTI | 988 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 881 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 875 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 810 | 5 | 2% | 1% | -42% | -85% | -84% |
| EURUSD | 803 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 796 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 754 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 716 | 3 | 1% | 1% | -61% | -99% | -98% |
| AUDUSD | 316 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 272 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13483 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13358 | 49 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2941 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3042 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4468 | 15 | 5% | 2% | -59% | -89% | -89% |
| 0.2–0.5% | 5124 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 1991 | 6 | 7% | 3% | -69% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6508 | 30 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,731 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 10:42:30 AM | NEAR | UP | 2.5 min | -0.716% | — | In play | — |
| 10/21 10:40:06 AM | EURUSD | DOWN | 4.9 min | — | — | In play | — |
| 10/21 10:40:06 AM | HYPE | DOWN | 4.9 min | +0.583% | — | In play | — |
| 10/21 10:39:50 AM | DOGE | DOWN | 5.2 min | +0.421% | — | In play | — |
| 10/21 10:29:53 AM | ETH | UP | 6 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:29:53 AM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:29:53 AM | DOGE | UP | 6 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:29:37 AM | ZEC | DOWN | 22 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:29:37 AM | SOL | DOWN | 22 sec | +0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:29:21 AM | XRP | DOWN | 38 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:29:05 AM | USDCAD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:28:49 AM | BNB | DOWN | 71 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:28:49 AM | GOLD | DOWN | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:28:49 AM | BTC | DOWN | 71 sec | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:28:49 AM | SILVER | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:28:31 AM | AUDUSD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:28:15 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:28:15 AM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:26:56 AM | PLATINUM | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:26:07 AM | HYPE | UP | 3.9 min | -0.690% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:26:07 AM | USDJPY | UP | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:25:51 AM | NEAR | UP | 4.1 min | -0.913% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:54 AM | SOL | UP | 6 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:14:38 AM | BNB | DOWN | 22 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:14:22 AM | PLATINUM | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:22 AM | NATGAS | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:05 AM | BTC | DOWN | 54 sec | +0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:05 AM | USDJPY | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:05 AM | WTI | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:05 AM | ETH | UP | 54 sec | -0.110% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
