# 15-Minute 1¢ Study

*Updated Tue Oct 20, 7:58 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2121 finished bets | 1% | $83.65 | +35% | +3.94¢ | $23.75 / $59.90 |

*Expect about **95 buys a day** (~$14.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1951 | $65.20 | +30% |
| Momentum model ≥ 2%, hold to the close | 3258 | -$18.80 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 2121 | -$33.35 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25171 | 25150 | 92 (0%) | 1.07% | -$1,770.05 (-58%) | Hold to the close: -$1,770.05 (-58%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16436 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16436 | 4.5% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16436 | 7.7% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16436 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3847 | 31 | -8% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2121 | 23 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1232 | 15 | +71% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3258 | 26 | -5% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 1951 | 20 | +30% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1292 | 13 | +38% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6422 | 42 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4467 | 34 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2954 | 22 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16634 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5926 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2590 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25150 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,770.05 | -58% | — |
| Sell at 2¢ | 908 | 4% | -$2,695.97 | -88% | 46 sec |
| Sell at 3¢ | 615 | 2% | -$2,692.20 | -88% | 47 sec |
| Sell at 5¢ | 437 | 2% | -$2,648.00 | -87% | 51 sec |
| Sell at 10¢ | 266 | 1% | -$2,555.59 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,364.79 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,136.80 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 986 | 5 | 11% | 3% | -52% | -81% | -84% |
| 2–5 min | 8145 | 41 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6424 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9591 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1870 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1859 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1858 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1848 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1848 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1845 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1839 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1834 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1833 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 974 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 938 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 916 | 3 | 3% | 1% | -61% | -94% | -95% |
| COPPER | 812 | 3 | 2% | 1% | -66% | -74% | -74% |
| PLATINUM | 807 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 745 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 744 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 734 | 2 | 1% | 0% | -75% | -85% | -86% |
| GBPUSD | 702 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 652 | 3 | 1% | 1% | -57% | -99% | -98% |
| AUDUSD | 271 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 221 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12691 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12459 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2806 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2896 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4213 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4846 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1870 | 6 | 7% | 3% | -67% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 5931 | 29 | 4% | 2% | -44% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,789 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 7:58:32 AM | USDJPY | DOWN | 88 sec | — | — | In play | — |
| 10/20 7:58:16 AM | AUDUSD | DOWN | 1.7 min | — | — | In play | — |
| 10/20 7:58:16 AM | WTI | UP | 1.7 min | — | — | In play | — |
| 10/20 7:57:43 AM | NEAR | DOWN | 2.3 min | +0.470% | — | In play | — |
| 10/20 7:57:12 AM | COPPER | DOWN | 2.8 min | — | — | In play | — |
| 10/20 7:56:56 AM | USDCAD | DOWN | 3.1 min | — | — | In play | — |
| 10/20 7:56:25 AM | ETH | DOWN | 3.6 min | +0.314% | — | In play | — |
| 10/20 7:56:09 AM | SOL | DOWN | 3.9 min | +0.396% | — | In play | — |
| 10/20 7:56:09 AM | DOGE | DOWN | 3.9 min | +0.335% | — | In play | — |
| 10/20 7:55:53 AM | XRP | DOWN | 4.1 min | +0.354% | — | In play | — |
| 10/20 7:54:33 AM | BTC | DOWN | 5.4 min | +0.368% | — | In play | — |
| 10/20 7:54:18 AM | BNB | DOWN | 5.7 min | +0.303% | — | In play | — |
| 10/20 7:53:46 AM | HYPE | DOWN | 6.2 min | +0.670% | — | In play | — |
| 10/20 7:53:15 AM | ZEC | DOWN | 6.8 min | +1.248% | — | In play | — |
| 10/20 7:44:45 AM | AUDUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:29 AM | HYPE | DOWN | 31 sec | +0.081% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:13 AM | ETH | DOWN | 47 sec | +0.105% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:13 AM | BNB | UP | 47 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:44:13 AM | NEAR | DOWN | 47 sec | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:13 AM | SOL | UP | 47 sec | -0.119% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:43:43 AM | XRP | DOWN | 76 sec | +0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:43:43 AM | SILVER | DOWN | 76 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:43:43 AM | DOGE | DOWN | 76 sec | +0.232% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:42:55 AM | GBPUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:42:40 AM | WTI | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:42:40 AM | GOLD | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:42:40 AM | USDJPY | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:42:24 AM | ZEC | DOWN | 2.6 min | +0.644% | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:42:08 AM | PALLADIUM | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:41:21 AM | USDCAD | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
