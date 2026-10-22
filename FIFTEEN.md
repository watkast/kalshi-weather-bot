# 15-Minute 1¢ Study

*Updated Wed Oct 21, 9:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2315 finished bets | 1% | $74.40 | +28% | +3.21¢ | $42.45 / $31.95 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2144 | $55.65 | +23% |
| Volatility model ≥ 2%, hold to the close | 4260 | -$17.70 | -3% |
| Momentum model ≥ 2%, hold to the close | 3583 | -$44.70 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27586 | 27579 | 102 (0%) | 1.07% | -$1,933.50 (-58%) | Hold to the close: -$1,933.50 (-58%) |

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
| Volatility model | 17768 | 4.6% | 0.4% (72) | -657% | ❌ Worse |
| Momentum model | 17768 | 4.5% | 0.4% (72) | -680% | ❌ Worse |
| Mean-reversion model | 17768 | 7.8% | 0.4% (72) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17768 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4260 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2315 | 24 | +28% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1323 | 16 | +70% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 3583 | 27 | -11% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2144 | 21 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1407 | 14 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 7052 | 47 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4922 | 39 | -13% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3280 | 27 | -6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17966 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6598 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3015 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27579 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 102 | 0% | -$1,933.50 | -58% | — |
| Sell at 2¢ | 1007 | 4% | -$2,959.68 | -88% | 46 sec |
| Sell at 3¢ | 684 | 2% | -$2,954.74 | -88% | 48 sec |
| Sell at 5¢ | 484 | 2% | -$2,906.90 | -86% | 59 sec |
| Sell at 10¢ | 296 | 1% | -$2,805.74 | -83% | 64 sec |
| Sell at 25¢ | 161 | 1% | -$2,590.59 | -77% | 82 sec |
| Sell at 50¢ | 104 | 0% | -$2,351.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1132 | 6 | 11% | 4% | -49% | -81% | -84% |
| 2–5 min | 8887 | 46 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 7020 | 27 | 3% | 1% | -58% | -93% | -92% |
| Under 1 min | 10536 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2014 | 11 | 5% | 2% | -32% | -89% | -89% |
| BNB | 2009 | 11 | 5% | 2% | -33% | -83% | -82% |
| HYPE | 2007 | 7 | 5% | 3% | -57% | -88% | -87% |
| ETH | 1996 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 1995 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 1994 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1987 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 1982 | 11 | 6% | 3% | -28% | -80% | -80% |
| BTC | 1982 | 11 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 1080 | 3 | 4% | 1% | -67% | -81% | -83% |
| SILVER | 1042 | 4 | 3% | 1% | -56% | -82% | -83% |
| WTI | 1017 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 909 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 895 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 834 | 5 | 2% | 1% | -44% | -85% | -84% |
| EURUSD | 833 | 3 | 2% | 1% | -66% | -85% | -85% |
| PALLADIUM | 816 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 780 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 747 | 4 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 342 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 297 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13904 | 52 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 13675 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2993 | 15 | 2% | 1% | -16% | -78% | -78% |
| 0.05–0.1% | 3101 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4587 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5244 | 25 | 6% | 3% | -48% | -87% | -87% |
| Over 0.5% | 2038 | 7 | 7% | 3% | -65% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7600 | 23 | 3% | 2% | -65% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,739 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 9:44:41 PM | EURUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:44:41 PM | XRP | DOWN | 19 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:44:41 PM | PALLADIUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:44:41 PM | GBPUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:44:25 PM | USDCAD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:44:25 PM | ZEC | DOWN | 35 sec | +0.175% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:44:09 PM | DOGE | DOWN | 51 sec | +0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:44:09 PM | WTI | UP | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:44:09 PM | HYPE | DOWN | 51 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:43:53 PM | SOL | DOWN | 67 sec | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:43:53 PM | NEAR | DOWN | 67 sec | +0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:43:21 PM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:43:21 PM | BTC | DOWN | 1.6 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:43:21 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:43:21 PM | USDJPY | UP | 1.6 min | — | 10¢ | ✅ Won | $13.85 |
| 10/21 9:43:21 PM | NATGAS | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:43:05 PM | ETH | DOWN | 1.9 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:43:05 PM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:42:33 PM | BNB | DOWN | 2.5 min | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:41:29 PM | GOLD | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:41:13 PM | COPPER | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:29:47 PM | PLATINUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:29:47 PM | HYPE | UP | 13 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:29:47 PM | USDJPY | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:29:16 PM | AUDUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:29:16 PM | BTC | UP | 43 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:28:11 PM | DOGE | UP | 1.8 min | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:28:11 PM | ETH | UP | 1.8 min | -0.134% | 1¢ | ❌ Lost | $0.00 |
| 10/21 9:28:11 PM | ZEC | UP | 1.8 min | -0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:27:54 PM | BNB | UP | 2.1 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
