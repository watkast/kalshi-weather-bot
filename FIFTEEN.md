# 15-Minute 1¢ Study

*Updated Sun Oct 11, 10:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1105 finished bets | 1% | $47.85 | +40% | +4.33¢ | $10.75 / $37.10 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1059 | $26.30 | +23% |
| 5+ min left, hold to the close | 401 | -$3.25 | -5% |
| Volatility model ≥ 2%, hold to the close | 1928 | -$7.90 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14592 | 14585 | 59 (0%) | 1.07% | -$933.50 (-53%) | Hold to the close: -$933.50 (-53%) |

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
| Volatility model | 9740 | 4.5% | 0.4% (42) | -667% | ❌ Worse |
| Momentum model | 9740 | 4.5% | 0.4% (42) | -694% | ❌ Worse |
| Mean-reversion model | 9740 | 7.2% | 0.4% (42) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9740 | 42 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1928 | 16 | -3% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1105 | 12 | +40% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 698 | 8 | +66% | -59% | -59% | -55% |
| Momentum model ≥ 2% | 1699 | 13 | -7% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1059 | 10 | +23% | -74% | -74% | -71% |
| Momentum model ≥ 10% | 734 | 7 | +36% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3395 | 25 | -20% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2319 | 19 | -9% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1554 | 13 | -3% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9938 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14585 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$933.50 | -53% | — |
| Sell at 2¢ | 500 | 3% | -$1,587.50 | -90% | 33 sec |
| Sell at 3¢ | 331 | 2% | -$1,588.41 | -90% | 47 sec |
| Sell at 5¢ | 242 | 2% | -$1,560.20 | -89% | 50 sec |
| Sell at 10¢ | 159 | 1% | -$1,481.21 | -84% | 64 sec |
| Sell at 25¢ | 90 | 1% | -$1,363.60 | -77% | 81 sec |
| Sell at 50¢ | 60 | 0% | -$1,214.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 397 | 4 | 11% | 3% | -5% | -81% | -86% |
| 2–5 min | 4714 | 31 | 6% | 3% | -36% | -88% | -89% |
| 1–2 min | 3828 | 15 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5642 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1113 | 6 | 4% | 3% | -34% | -90% | -90% |
| HYPE | 1113 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1109 | 2 | 4% | 2% | -77% | -91% | -90% |
| BNB | 1106 | 5 | 4% | 2% | -45% | -91% | -92% |
| ETH | 1104 | 8 | 5% | 2% | -12% | -90% | -89% |
| SOL | 1102 | 2 | 3% | 1% | -77% | -93% | -92% |
| BTC | 1099 | 5 | 5% | 2% | -40% | -88% | -91% |
| NEAR | 1096 | 6 | 5% | 2% | -29% | -75% | -76% |
| XRP | 1096 | 7 | 2% | 1% | -20% | -84% | -84% |
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
| UP (bought YES) | 7326 | 31 | 3% | 2% | -51% | -89% | -89% |
| DOWN (bought NO) | 7259 | 28 | 3% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1795 | 9 | 2% | 1% | -17% | -75% | -75% |
| 0.05–0.1% | 1774 | 6 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2542 | 8 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 2724 | 16 | 5% | 3% | -35% | -89% | -88% |
| Over 0.5% | 1100 | 5 | 6% | 2% | -53% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3563 | 20 | 4% | 2% | -35% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,448 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 10:29:58 AM | XRP | DOWN | 1 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 10:29:26 AM | SOL | DOWN | 33 sec | +0.058% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 10:29:10 AM | BTC | DOWN | 50 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/11 10:28:54 AM | ZEC | DOWN | 65 sec | +0.879% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 10:28:54 AM | NEAR | DOWN | 65 sec | +0.405% | 0¢ | ❌ Lost | $0.00 |
| 10/11 10:28:54 AM | BNB | DOWN | 65 sec | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 10:28:06 AM | ETH | DOWN | 1.9 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 10:28:06 AM | HYPE | UP | 1.9 min | -0.235% | 19¢ | ❌ Lost | -$0.15 |
| 10/11 10:27:42 AM | XRP | UP | 2.3 min | -0.204% | 99¢ | ✅ Won | $13.85 |
| 10/11 10:27:10 AM | SOL | UP | 2.8 min | -0.246% | 100¢ | ✅ Won | $13.85 |
| 10/11 10:26:07 AM | DOGE | UP | 3.9 min | -0.343% | 2¢ | ❌ Lost | -$0.15 |
| 10/11 10:14:57 AM | SOL | UP | 3 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/11 10:14:10 AM | ETH | UP | 49 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/11 10:14:10 AM | BNB | UP | 49 sec | -0.122% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 10:13:53 AM | HYPE | DOWN | 67 sec | +0.128% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 10:13:37 AM | BTC | UP | 83 sec | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 10:12:50 AM | ZEC | DOWN | 2.1 min | +0.499% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 10:12:50 AM | NEAR | UP | 2.1 min | -1.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 10:12:02 AM | XRP | UP | 3.0 min | -0.442% | 1¢ | ❌ Lost | $0.00 |
| 10/11 9:57:04 AM | ETH | DOWN | 2.9 min | +0.325% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:57:04 AM | BNB | DOWN | 2.9 min | +0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:57:04 AM | DOGE | DOWN | 2.9 min | +0.370% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:56:46 AM | BTC | DOWN | 3.2 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:55:59 AM | ZEC | DOWN | 4.0 min | +0.667% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:55:59 AM | SOL | DOWN | 4.0 min | +0.717% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:55:43 AM | XRP | DOWN | 4.3 min | +0.760% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:55:11 AM | NEAR | DOWN | 4.8 min | +3.440% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:55:11 AM | HYPE | DOWN | 4.8 min | +0.353% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:42:43 AM | BNB | DOWN | 2.3 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:41:08 AM | NEAR | DOWN | 3.9 min | +0.857% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
