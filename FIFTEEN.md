# 15-Minute 1¢ Study

*Updated Sat Nov 14, 12:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4347 finished bets | 1% | $230.85 | +48% | +5.31¢ | $76.45 / $154.40 |

*Expect about **91 buys a day** (~$13.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4088 | $130.15 | +29% |
| Volatility model ≥ 2%, hold to the close | 8045 | $80.25 | +8% |
| Momentum model ≥ 2%, hold to the close | 6681 | $15.25 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57037 | 57015 | 220 (0%) | 1.07% | -$3,871.00 (-56%) | Hold to the close: -$3,871.00 (-56%) |

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
| Volatility model | 34148 | 4.6% | 0.4% (141) | -643% | ❌ Worse |
| Momentum model | 34148 | 4.5% | 0.4% (141) | -669% | ❌ Worse |
| Mean-reversion model | 34148 | 8.0% | 0.4% (141) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34148 | 141 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8045 | 75 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4347 | 51 | +48% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2502 | 30 | +72% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 6681 | 56 | +2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 4088 | 41 | +29% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2670 | 26 | +37% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14043 | 100 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9793 | 84 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6521 | 60 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34354 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57015 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 220 | 0% | -$3,871.00 | -56% | — |
| Sell at 2¢ | 2287 | 4% | -$6,062.38 | -87% | 47 sec |
| Sell at 3¢ | 1545 | 3% | -$6,054.45 | -87% | 48 sec |
| Sell at 5¢ | 1058 | 2% | -$5,941.30 | -85% | 62 sec |
| Sell at 10¢ | 644 | 1% | -$5,701.36 | -82% | 65 sec |
| Sell at 25¢ | 339 | 1% | -$5,296.91 | -76% | 81 sec |
| Sell at 50¢ | 224 | 0% | -$4,781.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2846 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18387 | 99 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14381 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21388 | 57 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3844 | 18 | 5% | 3% | -39% | -88% | -87% |
| SOL | 3841 | 17 | 4% | 2% | -43% | -86% | -86% |
| HYPE | 3837 | 12 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3823 | 9 | 4% | 2% | -70% | -90% | -90% |
| BNB | 3821 | 20 | 5% | 2% | -34% | -85% | -85% |
| ETH | 3817 | 16 | 6% | 3% | -48% | -82% | -82% |
| BTC | 3796 | 20 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3793 | 17 | 5% | 2% | -42% | -85% | -86% |
| XRP | 3782 | 14 | 3% | 1% | -53% | -89% | -89% |
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
| UP (bought YES) | 28996 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28019 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5322 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5746 | 22 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 8720 | 34 | 5% | 2% | -50% | -89% | -89% |
| 0.2–0.5% | 10500 | 44 | 7% | 3% | -53% | -86% | -86% |
| Over 0.5% | 4057 | 18 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13892 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13774 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13785 | 61 | 4% | 2% | -48% | -86% | -87% |
| Evening (6pm–12am) | 15564 | 48 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,937 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/14 12:12:39 PM | NEAR | UP | 2.3 min | -0.817% | — | In play | — |
| 11/14 11:59:55 AM | HYPE | UP | 4 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:59:39 AM | ZEC | DOWN | 20 sec | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:59:39 AM | XRP | UP | 20 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:59:07 AM | NEAR | UP | 53 sec | -0.433% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 11:58:17 AM | DOGE | UP | 1.7 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:58:02 AM | SOL | UP | 1.9 min | -0.443% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 11:56:25 AM | BNB | UP | 3.6 min | -0.400% | 6¢ | ❌ Lost | -$0.15 |
| 11/14 11:56:25 AM | ETH | UP | 3.6 min | -0.500% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:56:09 AM | BTC | UP | 3.8 min | -0.479% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:44:49 AM | ZEC | UP | 11 sec | -0.525% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 11:44:33 AM | BNB | UP | 27 sec | -0.085% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 11:44:17 AM | HYPE | DOWN | 43 sec | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:44:02 AM | NEAR | UP | 58 sec | -0.387% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 11:44:02 AM | ETH | UP | 58 sec | -0.225% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:43:46 AM | DOGE | UP | 74 sec | -0.164% | 4¢ | ❌ Lost | -$0.15 |
| 11/14 11:43:30 AM | SOL | UP | 1.5 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:43:30 AM | BTC | UP | 1.5 min | -0.183% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:43:30 AM | XRP | UP | 1.5 min | -0.386% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 11:29:45 AM | SOL | UP | 15 sec | -0.096% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:29:30 AM | ETH | DOWN | 30 sec | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:29:13 AM | HYPE | UP | 46 sec | -0.315% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:27:19 AM | DOGE | UP | 2.7 min | -0.451% | 19¢ | ❌ Lost | -$0.15 |
| 11/14 11:27:01 AM | BTC | UP | 3.0 min | -0.299% | 4¢ | ❌ Lost | -$0.15 |
| 11/14 11:26:45 AM | BNB | UP | 3.2 min | -0.464% | 3¢ | ❌ Lost | -$0.15 |
| 11/14 11:25:26 AM | ZEC | UP | 4.5 min | -1.503% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:14:45 AM | XRP | DOWN | 14 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:14:29 AM | ETH | UP | 30 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:14:13 AM | BNB | DOWN | 46 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:13:56 AM | ZEC | UP | 63 sec | -0.430% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
