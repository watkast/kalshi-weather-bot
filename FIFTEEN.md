# 15-Minute 1¢ Study

*Updated Tue Oct 20, 2:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2094 finished bets | 1% | $87.40 | +37% | +4.17¢ | $25.25 / $62.15 |

*Expect about **95 buys a day** (~$14.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1931 | $67.90 | +32% |
| Momentum model ≥ 2%, hold to the close | 3217 | -$13.10 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 2094 | -$29.60 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24784 | 24777 | 90 (0%) | 1.07% | -$1,750.65 (-58%) | Hold to the close: -$1,750.65 (-58%) |

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
| Volatility model | 16236 | 4.6% | 0.4% (64) | -678% | ❌ Worse |
| Momentum model | 16236 | 4.6% | 0.4% (64) | -701% | ❌ Worse |
| Mean-reversion model | 16236 | 7.7% | 0.4% (64) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16236 | 64 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3793 | 30 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2094 | 23 | +37% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1221 | 15 | +73% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3217 | 26 | -3% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1931 | 20 | +32% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 1280 | 13 | +40% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6329 | 41 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4404 | 33 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2912 | 22 | -14% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16434 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5823 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2520 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24777 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,750.65 | -58% | — |
| Sell at 2¢ | 892 | 4% | -$2,666.73 | -89% | 45 sec |
| Sell at 3¢ | 603 | 2% | -$2,663.48 | -88% | 47 sec |
| Sell at 5¢ | 429 | 2% | -$2,619.80 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,530.05 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,341.32 | -78% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,116.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 956 | 5 | 10% | 3% | -50% | -81% | -84% |
| 2–5 min | 8045 | 40 | 7% | 3% | -51% | -88% | -88% |
| 1–2 min | 6320 | 24 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 9452 | 21 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1848 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1837 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1836 | 9 | 5% | 2% | -40% | -82% | -82% |
| ETH | 1826 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1825 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1822 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1816 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1812 | 9 | 6% | 3% | -36% | -79% | -79% |
| BTC | 1812 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 955 | 1 | 3% | 1% | -88% | -93% | -94% |
| SILVER | 924 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 898 | 3 | 3% | 1% | -61% | -94% | -96% |
| COPPER | 800 | 2 | 2% | 1% | -77% | -86% | -85% |
| PLATINUM | 791 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 734 | 5 | 2% | 1% | -36% | -84% | -83% |
| EURUSD | 729 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 721 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 684 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 636 | 3 | 1% | 1% | -56% | -99% | -98% |
| AUDUSD | 262 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 209 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12508 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12269 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2788 | 15 | 2% | 1% | -10% | -77% | -76% |
| 0.05–0.1% | 2862 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4141 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4784 | 22 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1856 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6194 | 24 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,812 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 1:59:41 AM | ZEC | UP | 19 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:59:41 AM | XRP | UP | 19 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:59:41 AM | GOLD | DOWN | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:59:41 AM | WTI | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:59:10 AM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:59:10 AM | NEAR | UP | 49 sec | -0.349% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:59:10 AM | BNB | UP | 49 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:58:53 AM | HYPE | UP | 66 sec | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:58:05 AM | SOL | UP | 1.9 min | -0.172% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 1:57:48 AM | BTC | UP | 2.2 min | -0.107% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 1:57:16 AM | ETH | UP | 2.7 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:56:09 AM | COPPER | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:56:09 AM | SILVER | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:55:06 AM | PLATINUM | UP | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:44:58 AM | ZEC | UP | 1 sec | -0.159% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:44:58 AM | NATGAS | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:44:42 AM | ETH | UP | 17 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:44:42 AM | SOL | UP | 17 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:44:26 AM | HYPE | UP | 33 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:44:26 AM | BTC | UP | 33 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:44:10 AM | EURUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:44:10 AM | NEAR | DOWN | 50 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:44:10 AM | DOGE | UP | 50 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:43:04 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:43:04 AM | XRP | UP | 1.9 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:43:04 AM | BNB | UP | 1.9 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:42:46 AM | PALLADIUM | UP | 2.2 min | — | 7¢ | ❌ Lost | -$0.15 |
| 10/20 1:41:43 AM | PLATINUM | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:41:11 AM | SILVER | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:40:22 AM | GOLD | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
