# 15-Minute 1¢ Study

*Updated Wed Oct 21, 9:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2312 finished bets | 1% | $74.85 | +29% | +3.24¢ | $42.45 / $32.40 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2142 | $55.95 | +24% |
| Volatility model ≥ 2%, hold to the close | 4256 | -$17.10 | -3% |
| Momentum model ≥ 2%, hold to the close | 3579 | -$44.10 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27552 | 27545 | 101 (0%) | 1.07% | -$1,943.45 (-58%) | Hold to the close: -$1,943.45 (-58%) |

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
| Volatility model | 17751 | 4.6% | 0.4% (72) | -657% | ❌ Worse |
| Momentum model | 17751 | 4.6% | 0.4% (72) | -680% | ❌ Worse |
| Mean-reversion model | 17751 | 7.8% | 0.4% (72) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17751 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4256 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2312 | 24 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1322 | 16 | +70% | -62% | -60% | -58% |
| Momentum model ≥ 2% | 3579 | 27 | -10% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2142 | 21 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1407 | 14 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 7044 | 47 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4916 | 39 | -13% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3277 | 27 | -6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17949 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6589 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3007 | 1% | 1% | 1% | 0% | 0% | 0% |
| **All** | 27545 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 101 | 0% | -$1,943.45 | -58% | — |
| Sell at 2¢ | 1006 | 4% | -$2,955.89 | -88% | 46 sec |
| Sell at 3¢ | 683 | 2% | -$2,951.08 | -88% | 48 sec |
| Sell at 5¢ | 483 | 2% | -$2,903.50 | -86% | 58 sec |
| Sell at 10¢ | 295 | 1% | -$2,803.00 | -83% | 64 sec |
| Sell at 25¢ | 161 | 1% | -$2,600.54 | -77% | 82 sec |
| Sell at 50¢ | 104 | 0% | -$2,361.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1132 | 6 | 11% | 4% | -49% | -81% | -84% |
| 2–5 min | 8879 | 46 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 7008 | 26 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 10522 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2012 | 11 | 5% | 2% | -32% | -89% | -89% |
| BNB | 2007 | 11 | 5% | 2% | -33% | -83% | -82% |
| HYPE | 2005 | 7 | 5% | 3% | -57% | -88% | -87% |
| ETH | 1994 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 1993 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 1992 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1986 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 1980 | 11 | 6% | 3% | -28% | -80% | -80% |
| BTC | 1980 | 11 | 5% | 2% | -25% | -88% | -90% |
| GOLD | 1078 | 3 | 4% | 1% | -67% | -81% | -83% |
| SILVER | 1041 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1016 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 907 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 894 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 833 | 5 | 2% | 1% | -44% | -85% | -84% |
| EURUSD | 831 | 3 | 2% | 1% | -66% | -85% | -85% |
| PALLADIUM | 815 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 779 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 745 | 3 | 1% | 1% | -62% | -99% | -98% |
| AUDUSD | 340 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 296 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13882 | 51 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13663 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2992 | 15 | 2% | 1% | -16% | -78% | -78% |
| 0.05–0.1% | 3097 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4579 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5241 | 25 | 6% | 3% | -48% | -87% | -87% |
| Over 0.5% | 2037 | 7 | 7% | 3% | -65% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7566 | 22 | 3% | 1% | -67% | -91% | -90% |

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
| 10/21 9:14:55 PM | WTI | DOWN | 4 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:14:39 PM | SOL | UP | 20 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:14:25 PM | BNB | UP | 34 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:14:10 PM | PALLADIUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:14:10 PM | PLATINUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:38 PM | COPPER | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:38 PM | AUDUSD | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:22 PM | DOGE | UP | 1.6 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:22 PM | ETH | UP | 1.6 min | -0.173% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:13:07 PM | NEAR | UP | 1.9 min | -0.357% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:07 PM | XRP | UP | 1.9 min | -0.253% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:13:07 PM | GOLD | UP | 1.9 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:12:35 PM | BTC | UP | 2.4 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:12:35 PM | USDCAD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:12:35 PM | HYPE | UP | 2.4 min | -0.347% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:12:14 PM | NATGAS | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:12:14 PM | ZEC | UP | 2.8 min | -0.488% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:11:09 PM | SILVER | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:09:46 PM | GBPUSD | DOWN | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:09:30 PM | USDJPY | UP | 5.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:08:41 PM | EURUSD | DOWN | 6.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:59:44 PM | BTC | DOWN | 16 sec | +0.006% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 8:59:28 PM | AUDUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:59:13 PM | DOGE | DOWN | 46 sec | +0.171% | 0¢ | ❌ Lost | $0.00 |
| 10/21 8:59:13 PM | XRP | DOWN | 46 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/21 8:58:56 PM | ETH | DOWN | 63 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/21 8:58:56 PM | BNB | UP | 63 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 8:58:40 PM | NATGAS | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:58:40 PM | ZEC | UP | 79 sec | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 8:58:40 PM | NEAR | DOWN | 79 sec | +0.326% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
