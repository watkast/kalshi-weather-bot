# 15-Minute 1¢ Study

*Updated Wed Oct 21, 5:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2299 finished bets | 1% | $76.35 | +29% | +3.32¢ | $43.20 / $33.15 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2131 | $57.30 | +24% |
| Volatility model ≥ 2%, hold to the close | 4225 | -$13.50 | -3% |
| Momentum model ≥ 2%, hold to the close | 3561 | -$42.15 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27250 | 27243 | 100 (0%) | 1.07% | -$1,920.10 (-58%) | Hold to the close: -$1,920.10 (-58%) |

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
| Volatility model | 17604 | 4.6% | 0.4% (72) | -658% | ❌ Worse |
| Momentum model | 17604 | 4.6% | 0.4% (72) | -681% | ❌ Worse |
| Mean-reversion model | 17604 | 7.8% | 0.4% (72) | -795% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17604 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4225 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2299 | 24 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1315 | 16 | +71% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 3561 | 27 | -10% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2131 | 21 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1403 | 14 | +36% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6977 | 47 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4872 | 39 | -12% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3246 | 27 | -5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17802 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6502 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2939 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27243 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 100 | 0% | -$1,920.10 | -58% | — |
| Sell at 2¢ | 997 | 4% | -$2,920.88 | -88% | 46 sec |
| Sell at 3¢ | 677 | 2% | -$2,916.07 | -88% | 48 sec |
| Sell at 5¢ | 480 | 2% | -$2,868.10 | -86% | 56 sec |
| Sell at 10¢ | 294 | 1% | -$2,766.96 | -83% | 64 sec |
| Sell at 25¢ | 160 | 1% | -$2,566.50 | -77% | 82 sec |
| Sell at 50¢ | 103 | 0% | -$2,330.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1104 | 6 | 11% | 4% | -48% | -81% | -84% |
| 2–5 min | 8781 | 45 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6932 | 26 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 10422 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1997 | 11 | 5% | 2% | -31% | -89% | -90% |
| BNB | 1990 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1989 | 7 | 5% | 3% | -57% | -88% | -87% |
| ETH | 1977 | 10 | 6% | 3% | -39% | -86% | -86% |
| SOL | 1977 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 1976 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1969 | 7 | 3% | 1% | -56% | -88% | -88% |
| BTC | 1964 | 11 | 5% | 2% | -25% | -88% | -90% |
| NEAR | 1963 | 11 | 6% | 3% | -27% | -80% | -79% |
| GOLD | 1064 | 2 | 3% | 1% | -78% | -82% | -84% |
| SILVER | 1026 | 4 | 3% | 1% | -55% | -82% | -82% |
| WTI | 1005 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 892 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 884 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 823 | 5 | 2% | 1% | -43% | -85% | -84% |
| EURUSD | 817 | 3 | 2% | 1% | -66% | -84% | -84% |
| PALLADIUM | 805 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 764 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 731 | 3 | 1% | 1% | -62% | -99% | -98% |
| AUDUSD | 326 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 285 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13690 | 50 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13553 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2974 | 15 | 2% | 1% | -16% | -78% | -77% |
| 0.05–0.1% | 3076 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4540 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5191 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 2018 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6472 | 20 | 4% | 2% | -63% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,742 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 4:59:44 PM | SOL | UP | 16 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:44 PM | NEAR | UP | 16 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:44 PM | SILVER | UP | 16 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:59:28 PM | ZEC | DOWN | 32 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:28 PM | NATGAS | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:59:13 PM | BTC | UP | 47 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:13 PM | XRP | UP | 47 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:58:56 PM | ETH | UP | 63 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:58:56 PM | HYPE | UP | 63 sec | -0.122% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:57:51 PM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:57:03 PM | BNB | UP | 3.0 min | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:55:25 PM | GOLD | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:44:55 PM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:44:55 PM | EURUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:44:55 PM | COPPER | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:44:23 PM | NEAR | UP | 37 sec | -0.256% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:44:04 PM | SILVER | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:44:04 PM | XRP | UP | 56 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:43:48 PM | ETH | UP | 72 sec | -0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:43:48 PM | BTC | UP | 72 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:43:32 PM | SOL | UP | 88 sec | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:43:17 PM | ZEC | UP | 1.7 min | -0.468% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:43:17 PM | PLATINUM | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:43:17 PM | DOGE | UP | 1.7 min | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:43:17 PM | HYPE | UP | 1.7 min | -0.163% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:42:43 PM | BNB | UP | 2.3 min | -0.125% | 1¢ | ❌ Lost | $0.00 |
| 10/21 4:42:27 PM | USDJPY | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:41:24 PM | GOLD | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:58 PM | GBPUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:58 PM | AUDUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
