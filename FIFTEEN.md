# 15-Minute 1¢ Study

*Updated Sun Oct 11, 11:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1114 finished bets | 1% | $46.95 | +39% | +4.21¢ | $24.00 / $22.95 |

*Expect about **83 buys a day** (~$12.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1063 | $26.15 | +23% |
| 5+ min left, hold to the close | 402 | -$3.40 | -6% |
| Volatility model ≥ 2%, hold to the close | 1944 | -$9.70 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14635 | 14628 | 59 (0%) | 1.07% | -$938.30 (-53%) | Hold to the close: -$938.30 (-53%) |

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
| Volatility model | 9783 | 4.5% | 0.4% (42) | -671% | ❌ Worse |
| Momentum model | 9783 | 4.5% | 0.4% (42) | -698% | ❌ Worse |
| Mean-reversion model | 9783 | 7.2% | 0.4% (42) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9783 | 42 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1944 | 16 | -4% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1114 | 12 | +39% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 703 | 8 | +65% | -59% | -59% | -55% |
| Momentum model ≥ 2% | 1711 | 13 | -8% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1063 | 10 | +23% | -74% | -74% | -71% |
| Momentum model ≥ 10% | 738 | 7 | +36% | -66% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3421 | 25 | -20% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2337 | 19 | -10% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1567 | 13 | -4% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9981 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14628 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$938.30 | -53% | — |
| Sell at 2¢ | 504 | 3% | -$1,591.26 | -90% | 33 sec |
| Sell at 3¢ | 333 | 2% | -$1,592.43 | -90% | 47 sec |
| Sell at 5¢ | 244 | 2% | -$1,563.70 | -89% | 50 sec |
| Sell at 10¢ | 161 | 1% | -$1,483.39 | -84% | 64 sec |
| Sell at 25¢ | 92 | 1% | -$1,361.78 | -77% | 81 sec |
| Sell at 50¢ | 60 | 0% | -$1,219.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 398 | 4 | 11% | 3% | -5% | -81% | -86% |
| 2–5 min | 4734 | 31 | 6% | 3% | -36% | -88% | -89% |
| 1–2 min | 3838 | 15 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5654 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1118 | 6 | 4% | 3% | -34% | -90% | -90% |
| HYPE | 1117 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1114 | 2 | 4% | 2% | -77% | -91% | -90% |
| BNB | 1111 | 5 | 4% | 2% | -45% | -91% | -92% |
| ETH | 1109 | 8 | 5% | 2% | -12% | -89% | -89% |
| SOL | 1107 | 2 | 3% | 1% | -77% | -93% | -92% |
| BTC | 1103 | 5 | 5% | 2% | -40% | -88% | -91% |
| NEAR | 1101 | 6 | 5% | 2% | -29% | -75% | -76% |
| XRP | 1101 | 7 | 2% | 1% | -21% | -84% | -84% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7343 | 31 | 3% | 2% | -51% | -89% | -89% |
| DOWN (bought NO) | 7285 | 28 | 3% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1799 | 9 | 2% | 1% | -17% | -75% | -75% |
| 0.05–0.1% | 1779 | 6 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2553 | 8 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 2743 | 16 | 5% | 3% | -36% | -89% | -88% |
| Over 0.5% | 1104 | 5 | 6% | 2% | -53% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3606 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,460 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 11:44:53 AM | BTC | DOWN | 7 sec | -0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:44:37 AM | ETH | UP | 23 sec | -0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:44:37 AM | DOGE | UP | 23 sec | -0.002% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:44:21 AM | BNB | UP | 39 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/11 11:43:38 AM | XRP | UP | 81 sec | -0.162% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:42:35 AM | NEAR | UP | 2.4 min | -0.846% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:40:12 AM | SOL | DOWN | 4.8 min | +0.355% | 32¢ | ❌ Lost | -$0.15 |
| 10/11 11:38:26 AM | ZEC | DOWN | 6.5 min | +1.391% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:29:21 AM | NEAR | UP | 39 sec | -0.409% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:27:28 AM | DOGE | DOWN | 2.5 min | +0.301% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:27:28 AM | XRP | DOWN | 2.5 min | +0.247% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:26:56 AM | HYPE | DOWN | 3.1 min | +0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:26:39 AM | SOL | DOWN | 3.4 min | +0.343% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:26:23 AM | BTC | DOWN | 3.6 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:26:23 AM | ETH | DOWN | 3.6 min | +0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:26:23 AM | BNB | DOWN | 3.6 min | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:25:32 AM | ZEC | DOWN | 4.5 min | +0.544% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:14:20 AM | ZEC | UP | 40 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/11 11:13:31 AM | BTC | UP | 88 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:13:15 AM | XRP | UP | 1.7 min | -0.267% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:13:15 AM | HYPE | UP | 1.7 min | -0.315% | 0¢ | ❌ Lost | $0.00 |
| 10/11 11:12:59 AM | NEAR | DOWN | 2.0 min | +0.576% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:12:25 AM | DOGE | UP | 2.6 min | -0.349% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:11:54 AM | SOL | UP | 3.1 min | -0.309% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:11:54 AM | BNB | UP | 3.1 min | -0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:10:16 AM | ETH | UP | 4.7 min | -0.288% | 2¢ | ❌ Lost | -$0.15 |
| 10/11 10:59:44 AM | XRP | DOWN | 16 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/11 10:59:05 AM | NEAR | DOWN | 54 sec | +0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/11 10:59:05 AM | SOL | DOWN | 54 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/11 10:59:05 AM | BNB | UP | 54 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
