# 15-Minute 1¢ Study

*Updated Wed Oct 21, 12:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2279 finished bets | 1% | $78.30 | +30% | +3.44¢ | $44.55 / $33.75 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2109 | $59.55 | +25% |
| Volatility model ≥ 2%, hold to the close | 4180 | -$8.25 | -2% |
| Momentum model ≥ 2%, hold to the close | 3526 | -$38.10 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26983 | 26966 | 99 (0%) | 1.07% | -$1,900.95 (-58%) | Hold to the close: -$1,900.95 (-58%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 17449 | 4.6% | 0.4% (71) | -657% | ❌ Worse |
| Momentum model | 17449 | 4.6% | 0.4% (71) | -680% | ❌ Worse |
| Mean-reversion model | 17449 | 7.8% | 0.4% (71) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17449 | 71 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4180 | 36 | -2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2279 | 24 | +30% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1304 | 16 | +72% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3526 | 27 | -9% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2109 | 21 | +25% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1386 | 14 | +38% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 6918 | 47 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4831 | 39 | -11% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3217 | 27 | -5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17647 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6433 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2886 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26966 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 99 | 0% | -$1,900.95 | -58% | — |
| Sell at 2¢ | 982 | 4% | -$2,891.63 | -88% | 46 sec |
| Sell at 3¢ | 669 | 2% | -$2,886.04 | -88% | 48 sec |
| Sell at 5¢ | 473 | 2% | -$2,839.50 | -86% | 56 sec |
| Sell at 10¢ | 288 | 1% | -$2,741.67 | -83% | 64 sec |
| Sell at 25¢ | 159 | 1% | -$2,536.66 | -77% | 81 sec |
| Sell at 50¢ | 102 | 0% | -$2,304.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1083 | 6 | 11% | 4% | -47% | -81% | -83% |
| 2–5 min | 8696 | 45 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6885 | 25 | 3% | 1% | -61% | -93% | -92% |
| Under 1 min | 10298 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1979 | 11 | 4% | 2% | -31% | -90% | -90% |
| BNB | 1973 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1971 | 7 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 1960 | 3 | 4% | 2% | -81% | -90% | -90% |
| ETH | 1959 | 10 | 6% | 3% | -39% | -87% | -86% |
| SOL | 1959 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1952 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1947 | 11 | 6% | 3% | -27% | -79% | -79% |
| BTC | 1947 | 11 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 1053 | 2 | 3% | 1% | -78% | -81% | -84% |
| SILVER | 1015 | 4 | 3% | 1% | -55% | -82% | -82% |
| WTI | 993 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 884 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 877 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 813 | 5 | 2% | 1% | -43% | -85% | -84% |
| EURUSD | 807 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 798 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 757 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 721 | 3 | 1% | 1% | -61% | -99% | -98% |
| AUDUSD | 320 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 277 | 0 | 0% | 0% | -100% | -99% | -99% |
| 2YRRATE | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13533 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13433 | 50 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2949 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3055 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4492 | 15 | 5% | 2% | -59% | -89% | -89% |
| 0.2–0.5% | 5151 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 1997 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6195 | 19 | 4% | 2% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,731 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 12:44:51 PM | PALLADIUM | DOWN | 9 sec | — | 0¢ | In play | — |
| 10/21 12:44:51 PM | AUDUSD | DOWN | 9 sec | — | 0¢ | In play | — |
| 10/21 12:44:35 PM | GOLD | UP | 25 sec | — | 0¢ | In play | — |
| 10/21 12:44:35 PM | SOL | UP | 25 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:44:35 PM | XRP | UP | 25 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:44:35 PM | USDJPY | DOWN | 25 sec | — | 0¢ | In play | — |
| 10/21 12:44:35 PM | USDCAD | UP | 25 sec | — | 0¢ | In play | — |
| 10/21 12:44:19 PM | BTC | UP | 41 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:44:19 PM | BNB | UP | 41 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:44:19 PM | ETH | UP | 41 sec | -0.085% | 0¢ | In play | — |
| 10/21 12:43:46 PM | DOGE | UP | 73 sec | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:43:46 PM | PLATINUM | DOWN | 73 sec | — | 0¢ | In play | — |
| 10/21 12:42:42 PM | ZEC | DOWN | 2.3 min | +0.431% | 5¢ | In play | — |
| 10/21 12:42:10 PM | HYPE | DOWN | 2.8 min | +0.268% | 5¢ | In play | — |
| 10/21 12:42:10 PM | NEAR | DOWN | 2.8 min | +0.437% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:40:50 PM | SILVER | DOWN | 4.2 min | — | 1¢ | In play | — |
| 10/21 12:29:58 PM | 2YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:58 PM | GBPUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:42 PM | AUDUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:42 PM | USDJPY | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:26 PM | ETH | DOWN | 33 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:29:10 PM | GOLD | DOWN | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:10 PM | ZEC | DOWN | 49 sec | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:28:38 PM | NEAR | UP | 82 sec | -0.528% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:26:46 PM | BTC | DOWN | 3.2 min | +0.146% | 9¢ | ❌ Lost | -$0.15 |
| 10/21 12:26:14 PM | BNB | DOWN | 3.8 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:25:43 PM | SOL | DOWN | 4.3 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:25:43 PM | DOGE | DOWN | 4.3 min | +0.357% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:25:43 PM | XRP | DOWN | 4.3 min | +0.359% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:25:19 PM | HYPE | DOWN | 4.7 min | +0.487% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
