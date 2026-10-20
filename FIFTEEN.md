# 15-Minute 1¢ Study

*Updated Tue Oct 20, 12:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2088 finished bets | 1% | $88.00 | +38% | +4.21¢ | $25.55 / $62.45 |

*Expect about **95 buys a day** (~$14.23/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1927 | $68.20 | +32% |
| Momentum model ≥ 2%, hold to the close | 3210 | -$12.50 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 2088 | -$29.00 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24702 | 24695 | 90 (0%) | 1.07% | -$1,740.90 (-58%) | Hold to the close: -$1,740.90 (-58%) |

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
| Volatility model | 16193 | 4.6% | 0.4% (64) | -677% | ❌ Worse |
| Momentum model | 16193 | 4.6% | 0.4% (64) | -700% | ❌ Worse |
| Mean-reversion model | 16193 | 7.7% | 0.4% (64) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16193 | 64 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3782 | 30 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2088 | 23 | +38% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1218 | 15 | +73% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3210 | 26 | -3% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1927 | 20 | +32% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 1278 | 13 | +40% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6314 | 41 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4393 | 33 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2906 | 22 | -14% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16391 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5792 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2512 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24695 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,740.90 | -58% | — |
| Sell at 2¢ | 891 | 4% | -$2,657.24 | -89% | 45 sec |
| Sell at 3¢ | 602 | 2% | -$2,654.12 | -88% | 47 sec |
| Sell at 5¢ | 428 | 2% | -$2,610.70 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,520.30 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,331.57 | -78% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,107.15 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 956 | 5 | 10% | 3% | -50% | -81% | -84% |
| 2–5 min | 8015 | 40 | 7% | 3% | -51% | -88% | -88% |
| 1–2 min | 6301 | 24 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 9419 | 21 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1843 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1832 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1831 | 9 | 5% | 2% | -40% | -82% | -82% |
| ETH | 1821 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1821 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1817 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1811 | 7 | 3% | 1% | -52% | -87% | -88% |
| NEAR | 1808 | 9 | 6% | 3% | -36% | -79% | -79% |
| BTC | 1807 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 950 | 1 | 3% | 1% | -88% | -93% | -94% |
| SILVER | 919 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 894 | 3 | 3% | 1% | -61% | -94% | -96% |
| COPPER | 796 | 2 | 2% | 1% | -77% | -85% | -85% |
| PLATINUM | 786 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 730 | 5 | 2% | 2% | -36% | -84% | -83% |
| EURUSD | 727 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 717 | 2 | 1% | 0% | -74% | -85% | -86% |
| GBPUSD | 682 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 634 | 3 | 1% | 1% | -56% | -99% | -98% |
| AUDUSD | 262 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 207 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12447 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12248 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2781 | 15 | 2% | 1% | -10% | -77% | -76% |
| 0.05–0.1% | 2850 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4124 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4777 | 22 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1856 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6112 | 24 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,815 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 12:44:39 AM | USDJPY | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:44:23 AM | AUDUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:44:07 AM | EURUSD | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:36 AM | NEAR | DOWN | 83 sec | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:36 AM | GBPUSD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:42:48 AM | WTI | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:42:01 AM | DOGE | DOWN | 3.0 min | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:42:01 AM | BTC | DOWN | 3.0 min | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:42:01 AM | ETH | DOWN | 3.0 min | +0.168% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:42:01 AM | XRP | DOWN | 3.0 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:41:45 AM | ZEC | DOWN | 3.2 min | +0.485% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:41:45 AM | BNB | DOWN | 3.2 min | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:41:13 AM | HYPE | DOWN | 3.8 min | +0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:41:13 AM | SOL | DOWN | 3.8 min | +0.292% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:29:56 AM | EURUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:29:09 AM | XRP | DOWN | 51 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/20 12:29:09 AM | PALLADIUM | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:28:53 AM | USDCAD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:28:53 AM | USDJPY | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:28:53 AM | GBPUSD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:28:37 AM | BNB | DOWN | 82 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:28:37 AM | AUDUSD | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:27:30 AM | BTC | DOWN | 2.5 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:27:30 AM | ETH | DOWN | 2.5 min | +0.155% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:27:14 AM | NEAR | DOWN | 2.8 min | +0.387% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 12:27:14 AM | SOL | DOWN | 2.8 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:25:22 AM | SILVER | DOWN | 4.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 12:24:50 AM | PLATINUM | DOWN | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:24:50 AM | DOGE | DOWN | 5.2 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:24:50 AM | HYPE | DOWN | 5.2 min | +0.387% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
