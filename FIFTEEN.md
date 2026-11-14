# 15-Minute 1¢ Study

*Updated Sat Nov 14, 1:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4350 finished bets | 1% | $230.70 | +48% | +5.30¢ | $76.15 / $154.55 |

*Expect about **91 buys a day** (~$13.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4091 | $129.85 | +29% |
| Volatility model ≥ 2%, hold to the close | 8050 | $79.80 | +8% |
| Momentum model ≥ 2%, hold to the close | 6688 | $14.35 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57096 | 57075 | 220 (0%) | 1.07% | -$3,875.35 (-56%) | Hold to the close: -$3,875.35 (-56%) |

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
| Volatility model | 34208 | 4.6% | 0.4% (141) | -644% | ❌ Worse |
| Momentum model | 34208 | 4.5% | 0.4% (141) | -669% | ❌ Worse |
| Mean-reversion model | 34208 | 7.9% | 0.4% (141) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34208 | 141 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8050 | 75 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4350 | 51 | +48% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2505 | 30 | +72% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6688 | 56 | +2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 4091 | 41 | +29% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2672 | 26 | +37% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14055 | 100 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9797 | 84 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6524 | 60 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34414 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57075 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 220 | 0% | -$3,875.35 | -56% | — |
| Sell at 2¢ | 2288 | 4% | -$6,066.47 | -87% | 47 sec |
| Sell at 3¢ | 1546 | 3% | -$6,058.41 | -87% | 48 sec |
| Sell at 5¢ | 1059 | 2% | -$5,945.00 | -85% | 62 sec |
| Sell at 10¢ | 645 | 1% | -$5,704.40 | -82% | 65 sec |
| Sell at 25¢ | 340 | 1% | -$5,297.95 | -76% | 80 sec |
| Sell at 50¢ | 225 | 0% | -$4,778.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2846 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18396 | 99 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14405 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21415 | 57 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3851 | 18 | 5% | 3% | -39% | -88% | -87% |
| SOL | 3846 | 17 | 4% | 2% | -43% | -86% | -86% |
| HYPE | 3844 | 12 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3830 | 9 | 4% | 2% | -70% | -90% | -90% |
| BNB | 3828 | 20 | 5% | 2% | -34% | -85% | -85% |
| ETH | 3824 | 16 | 7% | 3% | -48% | -82% | -82% |
| BTC | 3802 | 20 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3800 | 17 | 5% | 2% | -42% | -85% | -86% |
| XRP | 3789 | 14 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2031 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1754 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1674 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1646 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1162 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 777 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29041 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28034 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5327 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5750 | 22 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 8731 | 34 | 5% | 2% | -50% | -89% | -89% |
| 0.2–0.5% | 10527 | 44 | 6% | 3% | -53% | -86% | -86% |
| Over 0.5% | 4070 | 18 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13892 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13774 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13845 | 61 | 4% | 2% | -48% | -86% | -87% |
| Evening (6pm–12am) | 15564 | 48 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,945 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/14 1:44:15 PM | BTC | UP | 45 sec | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 1:43:41 PM | BNB | UP | 79 sec | -0.221% | 2¢ | ❌ Lost | -$0.15 |
| 11/14 1:43:25 PM | ETH | UP | 1.6 min | -0.421% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:43:10 PM | NEAR | UP | 1.8 min | -1.254% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:43:10 PM | SOL | UP | 1.8 min | -0.605% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:43:10 PM | XRP | UP | 1.8 min | -0.837% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:43:10 PM | HYPE | UP | 1.8 min | -1.537% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:43:10 PM | DOGE | UP | 1.8 min | -0.981% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:43:10 PM | ZEC | UP | 1.8 min | -1.720% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:29:39 PM | BNB | UP | 21 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:29:39 PM | XRP | UP | 21 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:29:23 PM | BTC | UP | 37 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 1:28:50 PM | HYPE | UP | 69 sec | -0.405% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:28:50 PM | NEAR | UP | 69 sec | -0.758% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:28:50 PM | ETH | UP | 69 sec | -0.239% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 1:28:50 PM | DOGE | UP | 69 sec | -0.350% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 1:28:03 PM | ZEC | UP | 1.9 min | -0.642% | 0¢ | ❌ Lost | $0.00 |
| 11/14 1:14:09 PM | SOL | UP | 51 sec | -0.234% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 1:13:51 PM | BTC | UP | 68 sec | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 1:13:51 PM | ZEC | UP | 68 sec | -0.420% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 1:13:35 PM | ETH | UP | 84 sec | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 1:13:35 PM | DOGE | UP | 84 sec | -0.317% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 1:12:48 PM | BNB | UP | 2.2 min | -0.281% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 1:12:32 PM | NEAR | UP | 2.5 min | -0.731% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 1:12:32 PM | XRP | UP | 2.5 min | -0.399% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 1:12:00 PM | HYPE | UP | 3.0 min | -0.577% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 12:59:17 PM | BNB | UP | 43 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 12:59:00 PM | BTC | UP | 59 sec | -0.161% | 0¢ | ❌ Lost | $0.00 |
| 11/14 12:59:00 PM | HYPE | UP | 59 sec | -0.268% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 12:58:44 PM | XRP | UP | 75 sec | -0.241% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
