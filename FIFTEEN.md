# 15-Minute 1¢ Study

*Updated Wed Oct 21, 4:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2299 finished bets | 1% | $76.35 | +29% | +3.32¢ | $43.20 / $33.15 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2130 | $57.45 | +24% |
| Volatility model ≥ 2%, hold to the close | 4222 | -$13.20 | -3% |
| Momentum model ≥ 2%, hold to the close | 3560 | -$42.00 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27222 | 27215 | 100 (0%) | 1.07% | -$1,917.25 (-58%) | Hold to the close: -$1,917.25 (-58%) |

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
| Volatility model | 17587 | 4.7% | 0.4% (72) | -658% | ❌ Worse |
| Momentum model | 17587 | 4.6% | 0.4% (72) | -681% | ❌ Worse |
| Mean-reversion model | 17587 | 7.8% | 0.4% (72) | -795% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17587 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4222 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2299 | 24 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1315 | 16 | +71% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 3560 | 27 | -10% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2130 | 21 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1402 | 14 | +36% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6974 | 47 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4870 | 39 | -12% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3246 | 27 | -5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17785 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6494 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2936 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27215 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 100 | 0% | -$1,917.25 | -58% | — |
| Sell at 2¢ | 997 | 4% | -$2,918.03 | -88% | 46 sec |
| Sell at 3¢ | 677 | 2% | -$2,913.22 | -88% | 48 sec |
| Sell at 5¢ | 480 | 2% | -$2,865.25 | -86% | 56 sec |
| Sell at 10¢ | 294 | 1% | -$2,764.11 | -83% | 64 sec |
| Sell at 25¢ | 160 | 1% | -$2,563.65 | -77% | 82 sec |
| Sell at 50¢ | 103 | 0% | -$2,328.00 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1104 | 6 | 11% | 4% | -48% | -81% | -84% |
| 2–5 min | 8775 | 45 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6923 | 26 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 10409 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1995 | 11 | 5% | 2% | -31% | -89% | -90% |
| BNB | 1988 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1987 | 7 | 5% | 3% | -57% | -88% | -87% |
| ETH | 1975 | 10 | 6% | 3% | -39% | -86% | -86% |
| DOGE | 1975 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1975 | 3 | 3% | 2% | -81% | -92% | -92% |
| XRP | 1967 | 7 | 3% | 1% | -56% | -88% | -88% |
| BTC | 1962 | 11 | 5% | 2% | -25% | -88% | -90% |
| NEAR | 1961 | 11 | 6% | 3% | -27% | -80% | -79% |
| GOLD | 1062 | 2 | 3% | 1% | -78% | -82% | -84% |
| SILVER | 1024 | 4 | 3% | 1% | -55% | -82% | -82% |
| WTI | 1005 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 890 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 883 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 822 | 5 | 2% | 1% | -43% | -85% | -84% |
| EURUSD | 816 | 3 | 2% | 1% | -66% | -84% | -84% |
| PALLADIUM | 805 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 763 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 730 | 3 | 1% | 1% | -62% | -99% | -98% |
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
| UP (bought YES) | 13665 | 50 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13550 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2973 | 15 | 2% | 1% | -16% | -78% | -77% |
| 0.05–0.1% | 3072 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4530 | 16 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5189 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 2018 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6444 | 20 | 4% | 2% | -63% | -88% | -89% |
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
| 10/21 4:29:58 PM | GBPUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:58 PM | AUDUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:58 PM | BRENT | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:58 PM | USDCAD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:42 PM | USDJPY | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:42 PM | BNB | UP | 17 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:29:26 PM | NEAR | UP | 33 sec | -0.188% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:10 PM | EURUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:10 PM | ZEC | DOWN | 50 sec | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:10 PM | PLATINUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:10 PM | NATGAS | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:28:53 PM | HYPE | DOWN | 66 sec | +0.153% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:28:37 PM | GOLD | UP | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:28:21 PM | WTI | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:28:21 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:27:16 PM | DOGE | UP | 2.7 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:27:00 PM | BTC | UP | 3.0 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:26:41 PM | SILVER | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:26:25 PM | ETH | UP | 3.6 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:26:25 PM | SOL | UP | 3.6 min | -0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:25:18 PM | XRP | UP | 4.7 min | -0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:14:58 PM | USDJPY | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:14:58 PM | BRENT | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:14:43 PM | BNB | UP | 16 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:14:43 PM | USDCAD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:14:27 PM | WTI | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:14:27 PM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:14:11 PM | NATGAS | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:11:44 PM | BTC | UP | 3.2 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:11:12 PM | ETH | UP | 3.8 min | -0.163% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
