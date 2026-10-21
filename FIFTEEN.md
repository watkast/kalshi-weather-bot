# 15-Minute 1¢ Study

*Updated Wed Oct 21, 12:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2200 finished bets | 1% | $87.15 | +35% | +3.96¢ | $20.45 / $66.70 |

*Expect about **96 buys a day** (~$14.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2040 | $67.35 | +30% |
| Momentum model ≥ 2%, hold to the close | 3402 | -$23.40 | -6% |
| Volatility model ≥ 2%, hold to the close | 4032 | -$32.55 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26176 | 26169 | 96 (0%) | 1.07% | -$1,845.30 (-58%) | Hold to the close: -$1,845.30 (-58%) |

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
| Volatility model | 17010 | 4.6% | 0.4% (68) | -665% | ❌ Worse |
| Momentum model | 17010 | 4.5% | 0.4% (68) | -687% | ❌ Worse |
| Mean-reversion model | 17010 | 7.8% | 0.4% (68) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17010 | 68 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4032 | 33 | -7% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2200 | 24 | +35% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 1264 | 16 | +77% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3402 | 27 | -6% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2040 | 21 | +30% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1342 | 14 | +42% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6696 | 44 | -29% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4664 | 36 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3090 | 24 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17208 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6215 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2746 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26169 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 96 | 0% | -$1,845.30 | -58% | — |
| Sell at 2¢ | 952 | 4% | -$2,801.78 | -88% | 46 sec |
| Sell at 3¢ | 648 | 2% | -$2,796.58 | -88% | 48 sec |
| Sell at 5¢ | 459 | 2% | -$2,750.95 | -86% | 55 sec |
| Sell at 10¢ | 279 | 1% | -$2,655.81 | -83% | 64 sec |
| Sell at 25¢ | 151 | 1% | -$2,465.49 | -77% | 80 sec |
| Sell at 50¢ | 98 | 0% | -$2,233.80 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1052 | 5 | 10% | 4% | -55% | -81% | -84% |
| 2–5 min | 8452 | 43 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6675 | 25 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9986 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1933 | 11 | 5% | 2% | -29% | -90% | -90% |
| BNB | 1923 | 10 | 5% | 2% | -36% | -83% | -82% |
| HYPE | 1922 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1912 | 9 | 6% | 3% | -44% | -87% | -86% |
| DOGE | 1911 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1910 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1903 | 7 | 3% | 1% | -55% | -87% | -88% |
| NEAR | 1897 | 11 | 6% | 3% | -25% | -79% | -79% |
| BTC | 1897 | 11 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1019 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 982 | 4 | 3% | 1% | -53% | -82% | -81% |
| WTI | 958 | 3 | 3% | 1% | -63% | -94% | -95% |
| PLATINUM | 853 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 849 | 3 | 2% | 1% | -67% | -75% | -75% |
| NATGAS | 782 | 5 | 2% | 1% | -40% | -84% | -83% |
| EURUSD | 778 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 772 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 733 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 689 | 3 | 1% | 1% | -59% | -99% | -98% |
| AUDUSD | 299 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 247 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13181 | 48 | 4% | 2% | -58% | -87% | -87% |
| DOWN (bought NO) | 12988 | 48 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2886 | 15 | 2% | 1% | -13% | -77% | -77% |
| 0.05–0.1% | 2992 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4361 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5023 | 24 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1943 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6467 | 27 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,775 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 12:14:56 AM | SOL | UP | 3 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:56 AM | BNB | UP | 3 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:56 AM | SILVER | UP | 3 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:56 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:40 AM | BTC | UP | 19 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:40 AM | XRP | UP | 19 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:24 AM | WTI | DOWN | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:24 AM | ETH | UP | 35 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:24 AM | NATGAS | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:24 AM | ZEC | DOWN | 35 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:08 AM | NEAR | DOWN | 52 sec | +0.205% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:13:51 AM | DOGE | DOWN | 68 sec | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:13:51 AM | HYPE | DOWN | 68 sec | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:13:35 AM | GBPUSD | UP | 84 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:12:13 AM | BNB | DOWN | 2.8 min | +0.057% | 100¢ | ✅ Won | $13.85 |
| 10/21 12:09:16 AM | PLATINUM | UP | 5.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:09:16 AM | PALLADIUM | UP | 5.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:59:46 PM | BNB | UP | 13 sec | -0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:59:46 PM | USDCAD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:59:14 PM | SOL | UP | 45 sec | -0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:59 PM | BTC | UP | 60 sec | -0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:59 PM | XRP | UP | 60 sec | -0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:59 PM | ETH | UP | 60 sec | -0.074% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:43 PM | PLATINUM | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:43 PM | HYPE | UP | 76 sec | -0.181% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:58:43 PM | NATGAS | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:43 PM | ZEC | UP | 76 sec | -0.281% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:58:27 PM | USDJPY | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:57:49 PM | COPPER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:57:33 PM | DOGE | UP | 2.5 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
