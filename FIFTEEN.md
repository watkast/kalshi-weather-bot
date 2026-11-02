# 15-Minute 1¢ Study

*Updated Mon Nov 2, 3:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3489 finished bets | 1% | $127.70 | +33% | +3.66¢ | $72.50 / $55.20 |

*Expect about **99 buys a day** (~$14.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6441 | $59.55 | +8% |
| Momentum model ≥ 5%, hold to the close | 3216 | $55.60 | +16% |
| Momentum model ≥ 2%, hold to the close | 5310 | -$26.70 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42421 | 42410 | 159 (0%) | 1.07% | -$2,935.95 (-57%) | Hold to the close: -$2,935.95 (-57%) |

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
| Volatility model | 26405 | 4.7% | 0.4% (106) | -673% | ❌ Worse |
| Momentum model | 26405 | 4.6% | 0.4% (106) | -695% | ❌ Worse |
| Mean-reversion model | 26405 | 8.1% | 0.4% (106) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26405 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6441 | 60 | +8% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3489 | 37 | +33% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1978 | 22 | +58% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5310 | 42 | -4% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3216 | 29 | +16% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2099 | 19 | +26% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10916 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7654 | 65 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5118 | 46 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26607 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9950 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5853 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42410 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,935.95 | -57% | — |
| Sell at 2¢ | 1661 | 4% | -$4,506.09 | -87% | 47 sec |
| Sell at 3¢ | 1139 | 3% | -$4,493.74 | -87% | 48 sec |
| Sell at 5¢ | 792 | 2% | -$4,395.15 | -85% | 63 sec |
| Sell at 10¢ | 478 | 1% | -$4,213.77 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,897.14 | -75% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,536.95 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2027 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13628 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10708 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16036 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2981 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 2972 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2969 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2967 | 9 | 5% | 2% | -62% | -89% | -87% |
| DOGE | 2956 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2954 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2937 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2936 | 15 | 5% | 2% | -34% | -83% | -83% |
| XRP | 2935 | 12 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1550 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1510 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1506 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1342 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1284 | 5 | 1% | 1% | -64% | -76% | -75% |
| EURUSD | 1281 | 3 | 2% | 1% | -78% | -89% | -89% |
| NATGAS | 1236 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1214 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1208 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1201 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 737 | 4 | 1% | 1% | -49% | -85% | -84% |
| USDCAD | 713 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 314 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 193 | 1 | 5% | 2% | -52% | -43% | -41% |
| 30YRRATE | 182 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 173 | 2 | 5% | 1% | +8% | +16% | +17% |
| 5YRRATE | 159 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21543 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20867 | 72 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4339 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4579 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6895 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7847 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2942 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10550 | 37 | 4% | 2% | -60% | -86% | -87% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,796 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 3:25:25 AM | AUDUSD | UP | 4.6 min | — | — | In play | — |
| 11/2 3:14:47 AM | PLATINUM | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:14:47 AM | NEAR | UP | 12 sec | -0.223% | 0¢ | ❌ Lost | $0.00 |
| 11/2 3:14:31 AM | HYPE | UP | 28 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:14:31 AM | ZEC | DOWN | 28 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 3:14:31 AM | DOGE | UP | 28 sec | -0.062% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:13:59 AM | COPPER | UP | 61 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 11/2 3:13:59 AM | AUDUSD | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:13:27 AM | BTC | UP | 1.5 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 3:13:27 AM | GBPUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:13:27 AM | USDCAD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:13:27 AM | BNB | UP | 1.5 min | -0.143% | 0¢ | ❌ Lost | $0.00 |
| 11/2 3:13:11 AM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:13:11 AM | ETH | UP | 1.8 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 3:12:55 AM | SOL | UP | 2.1 min | -0.201% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:12:23 AM | XRP | UP | 2.6 min | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 3:12:07 AM | PALLADIUM | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:11:35 AM | SILVER | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 2:59:44 AM | COPPER | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:59:44 AM | BTC | UP | 15 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:59:44 AM | GBPUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:59:44 AM | SOL | UP | 15 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:59:44 AM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:59:28 AM | NATGAS | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:59:12 AM | GOLD | UP | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:59:12 AM | BNB | UP | 47 sec | -0.158% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:59:12 AM | NEAR | UP | 47 sec | -0.221% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:58:25 AM | ZEC | DOWN | 1.6 min | +0.249% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:58:25 AM | DOGE | DOWN | 1.6 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 2:57:21 AM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
