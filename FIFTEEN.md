# 15-Minute 1¢ Study

*Updated Wed Oct 21, 7:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2308 finished bets | 1% | $75.30 | +29% | +3.26¢ | $42.60 / $32.70 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2139 | $56.25 | +24% |
| Volatility model ≥ 2%, hold to the close | 4243 | -$15.75 | -3% |
| Momentum model ≥ 2%, hold to the close | 3573 | -$43.65 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27444 | 27437 | 101 (0%) | 1.07% | -$1,930.40 (-58%) | Hold to the close: -$1,930.40 (-58%) |

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
| Volatility model | 17700 | 4.6% | 0.4% (72) | -658% | ❌ Worse |
| Momentum model | 17700 | 4.6% | 0.4% (72) | -681% | ❌ Worse |
| Mean-reversion model | 17700 | 7.8% | 0.4% (72) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17700 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4243 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2308 | 24 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1322 | 16 | +70% | -62% | -60% | -58% |
| Momentum model ≥ 2% | 3573 | 27 | -10% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2139 | 21 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1406 | 14 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 7021 | 47 | -27% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4900 | 39 | -12% | -80% | -80% | -76% |
| Mean-reversion model ≥ 10% | 3264 | 27 | -6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17898 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6558 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2981 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27437 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 101 | 0% | -$1,930.40 | -58% | — |
| Sell at 2¢ | 1002 | 4% | -$2,943.88 | -88% | 46 sec |
| Sell at 3¢ | 680 | 2% | -$2,939.20 | -88% | 48 sec |
| Sell at 5¢ | 482 | 2% | -$2,891.10 | -86% | 57 sec |
| Sell at 10¢ | 295 | 1% | -$2,789.95 | -83% | 64 sec |
| Sell at 25¢ | 161 | 1% | -$2,587.49 | -77% | 82 sec |
| Sell at 50¢ | 104 | 0% | -$2,348.40 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1120 | 6 | 11% | 4% | -49% | -81% | -84% |
| 2–5 min | 8844 | 46 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6980 | 26 | 3% | 1% | -59% | -93% | -92% |
| Under 1 min | 10489 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2007 | 11 | 5% | 2% | -32% | -89% | -90% |
| BNB | 2001 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1999 | 7 | 5% | 3% | -57% | -88% | -87% |
| ETH | 1988 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 1988 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 1986 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1980 | 7 | 3% | 1% | -57% | -88% | -88% |
| BTC | 1975 | 11 | 5% | 2% | -25% | -88% | -90% |
| NEAR | 1974 | 11 | 6% | 3% | -28% | -80% | -80% |
| GOLD | 1074 | 3 | 4% | 1% | -67% | -81% | -83% |
| SILVER | 1035 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1013 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 901 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 891 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 829 | 5 | 2% | 1% | -44% | -85% | -84% |
| EURUSD | 826 | 3 | 2% | 1% | -66% | -85% | -85% |
| PALLADIUM | 811 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 774 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 740 | 3 | 1% | 1% | -62% | -99% | -98% |
| AUDUSD | 334 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 291 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13806 | 51 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13631 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2990 | 15 | 2% | 1% | -16% | -78% | -78% |
| 0.05–0.1% | 3092 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4564 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5217 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 2032 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7458 | 22 | 3% | 2% | -66% | -90% | -90% |

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
| 10/21 7:43:15 PM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:43:00 PM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:42:28 PM | GBPUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:42:28 PM | USDCAD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:42:12 PM | COPPER | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:42:12 PM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:42:12 PM | EURUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:41:41 PM | SILVER | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:40:22 PM | AUDUSD | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:39:06 PM | NEAR | UP | 5.9 min | -1.454% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:39:06 PM | HYPE | UP | 5.9 min | -0.683% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:38:33 PM | BTC | UP | 6.4 min | -0.566% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:38:33 PM | ETH | UP | 6.4 min | -0.561% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:38:17 PM | DOGE | UP | 6.7 min | -0.556% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:38:01 PM | XRP | UP | 7.0 min | -0.557% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:38:01 PM | BNB | UP | 7.0 min | -0.286% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:37:28 PM | ZEC | UP | 7.5 min | -0.764% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:37:12 PM | SOL | UP | 7.8 min | -0.524% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:55 PM | NATGAS | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:55 PM | XRP | DOWN | 5 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:29:55 PM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:23 PM | SILVER | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:08 PM | ETH | DOWN | 51 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:29:08 PM | BNB | DOWN | 51 sec | -0.004% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:28:52 PM | NEAR | UP | 67 sec | -0.379% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:28:52 PM | EURUSD | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:28:36 PM | DOGE | UP | 83 sec | -0.147% | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:28:36 PM | BTC | DOWN | 83 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:28:36 PM | SOL | UP | 83 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:28:20 PM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
