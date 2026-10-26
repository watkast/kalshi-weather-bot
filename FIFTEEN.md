# 15-Minute 1¢ Study

*Updated Mon Oct 26, 2:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2726 finished bets | 1% | $82.55 | +27% | +3.03¢ | $32.45 / $50.10 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2532 | $55.95 | +20% |
| Volatility model ≥ 2%, hold to the close | 5049 | -$16.60 | -3% |
| Momentum model ≥ 2%, hold to the close | 4211 | -$31.80 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32432 | 32424 | 120 (0%) | 1.07% | -$2,258.85 (-57%) | Hold to the close: -$2,258.85 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20880 | 4.6% | 0.4% (85) | -660% | ❌ Worse |
| Momentum model | 20880 | 4.5% | 0.4% (85) | -685% | ❌ Worse |
| Mean-reversion model | 20880 | 7.9% | 0.4% (85) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20880 | 85 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5049 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2726 | 28 | +27% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1545 | 18 | +63% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4211 | 33 | -6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2532 | 24 | +20% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1653 | 16 | +33% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8419 | 56 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5897 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3924 | 33 | -5% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21080 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7544 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3800 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32424 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,258.85 | -57% | — |
| Sell at 2¢ | 1208 | 4% | -$3,456.77 | -88% | 47 sec |
| Sell at 3¢ | 830 | 3% | -$3,447.15 | -88% | 48 sec |
| Sell at 5¢ | 577 | 2% | -$3,395.80 | -86% | 61 sec |
| Sell at 10¢ | 358 | 1% | -$3,259.87 | -83% | 65 sec |
| Sell at 25¢ | 193 | 1% | -$3,020.02 | -77% | 82 sec |
| Sell at 50¢ | 124 | 0% | -$2,737.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1426 | 7 | 11% | 4% | -53% | -81% | -82% |
| 2–5 min | 10383 | 55 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8216 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12395 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2362 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2355 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2351 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2348 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2342 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2335 | 4 | 4% | 2% | -79% | -91% | -90% |
| NEAR | 2332 | 12 | 5% | 2% | -33% | -82% | -82% |
| XRP | 2332 | 9 | 3% | 1% | -52% | -89% | -89% |
| BTC | 2323 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1221 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1186 | 5 | 4% | 2% | -51% | -82% | -81% |
| WTI | 1163 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1035 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1010 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 967 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 960 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 923 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 911 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 896 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 456 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 418 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 46 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16421 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 16003 | 54 | 4% | 1% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3518 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3621 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5451 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6155 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2331 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8062 | 32 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,812 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 2:14:58 AM | USDJPY | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:26 AM | PLATINUM | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:26 AM | AUDUSD | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:13:55 AM | PALLADIUM | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:13:39 AM | USDCAD | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:13:06 AM | NEAR | UP | 1.9 min | -0.470% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:13:06 AM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:12:34 AM | NATGAS | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:12:34 AM | GOLD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 2:11:29 AM | ZEC | UP | 3.5 min | -0.650% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:11:13 AM | XRP | UP | 3.8 min | -0.415% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:10:57 AM | BTC | UP | 4.0 min | -0.411% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:10:40 AM | DOGE | UP | 4.3 min | -0.432% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:10:40 AM | WTI | UP | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:10:08 AM | HYPE | UP | 4.8 min | -0.579% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:09:35 AM | SOL | UP | 5.4 min | -0.418% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:08:14 AM | ETH | UP | 6.8 min | -0.477% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:07:25 AM | SILVER | DOWN | 7.6 min | — | 4¢ | ❌ Lost | -$0.15 |
| 10/26 2:07:25 AM | BNB | UP | 7.6 min | -0.462% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 1:59:44 AM | DOGE | UP | 16 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:59:44 AM | NATGAS | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:59:44 AM | SOL | UP | 16 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:59:28 AM | NEAR | DOWN | 32 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:59:13 AM | ETH | UP | 46 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:59:13 AM | BTC | UP | 46 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:58:57 AM | ZEC | UP | 62 sec | -0.198% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:58:57 AM | XRP | UP | 62 sec | -0.148% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:58:25 AM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:58:25 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:57:04 AM | USDCAD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
