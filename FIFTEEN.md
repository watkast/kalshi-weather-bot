# 15-Minute 1¢ Study

*Updated Wed Oct 21, 9:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2253 finished bets | 1% | $81.45 | +32% | +3.62¢ | $45.75 / $35.70 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2089 | $61.80 | +27% |
| Volatility model ≥ 2%, hold to the close | 4129 | -$15.95 | -3% |
| Momentum model ≥ 2%, hold to the close | 3489 | -$33.60 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26767 | 26758 | 98 (0%) | 1.07% | -$1,889.75 (-58%) | Hold to the close: -$1,889.75 (-58%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 17326 | 4.6% | 0.4% (70) | -663% | ❌ Worse |
| Momentum model | 17326 | 4.6% | 0.4% (70) | -686% | ❌ Worse |
| Mean-reversion model | 17326 | 7.8% | 0.4% (70) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17326 | 70 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4129 | 35 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2253 | 24 | +32% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1292 | 16 | +73% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3489 | 27 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2089 | 21 | +27% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1373 | 14 | +39% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6847 | 46 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4778 | 38 | -12% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3176 | 26 | -7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17524 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6388 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2846 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26758 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 98 | 0% | -$1,889.75 | -58% | — |
| Sell at 2¢ | 973 | 4% | -$2,868.77 | -88% | 46 sec |
| Sell at 3¢ | 663 | 2% | -$2,863.18 | -88% | 48 sec |
| Sell at 5¢ | 469 | 2% | -$2,816.90 | -86% | 58 sec |
| Sell at 10¢ | 286 | 1% | -$2,719.09 | -83% | 64 sec |
| Sell at 25¢ | 158 | 1% | -$2,514.77 | -77% | 81 sec |
| Sell at 50¢ | 101 | 0% | -$2,286.00 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1078 | 6 | 11% | 4% | -47% | -81% | -83% |
| 2–5 min | 8632 | 44 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6829 | 25 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 10215 | 23 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1966 | 11 | 5% | 2% | -30% | -90% | -90% |
| BNB | 1959 | 11 | 5% | 3% | -31% | -82% | -82% |
| HYPE | 1957 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1947 | 10 | 6% | 3% | -39% | -87% | -86% |
| DOGE | 1946 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1945 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1938 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1933 | 11 | 6% | 3% | -26% | -80% | -79% |
| BTC | 1933 | 11 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 1045 | 2 | 3% | 1% | -77% | -81% | -83% |
| SILVER | 1007 | 4 | 3% | 1% | -54% | -82% | -82% |
| WTI | 984 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 877 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 874 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 807 | 5 | 2% | 1% | -42% | -85% | -84% |
| EURUSD | 800 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 794 | 2 | 1% | 0% | -76% | -86% | -87% |
| GBPUSD | 751 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 712 | 3 | 1% | 1% | -61% | -99% | -98% |
| AUDUSD | 313 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 268 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13443 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13315 | 49 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2933 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3037 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4458 | 15 | 5% | 2% | -59% | -89% | -89% |
| 0.2–0.5% | 5108 | 25 | 6% | 3% | -46% | -87% | -87% |
| Over 0.5% | 1985 | 6 | 7% | 3% | -69% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6425 | 30 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
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
| 10/21 9:24:58 AM | GOLD | DOWN | 5.0 min | — | — | In play | — |
| 10/21 9:23:38 AM | SILVER | DOWN | 6.4 min | — | — | In play | — |
| 10/21 9:14:58 AM | USDJPY | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:14:58 AM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:14:42 AM | XRP | UP | 17 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:14:26 AM | PLATINUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:14:26 AM | EURUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:52 AM | COPPER | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:36 AM | GBPUSD | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:20 AM | GOLD | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:20 AM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:13:05 AM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:12:32 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:12:16 AM | BNB | DOWN | 2.7 min | +0.258% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:12:16 AM | BTC | DOWN | 2.7 min | +0.223% | 4¢ | ❌ Lost | -$0.15 |
| 10/21 9:12:01 AM | USDCAD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:12:01 AM | ZEC | DOWN | 3.0 min | +0.851% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:11:45 AM | DOGE | DOWN | 3.2 min | +0.526% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:11:45 AM | SOL | DOWN | 3.2 min | +0.440% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:10:57 AM | HYPE | DOWN | 4.0 min | +0.664% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:10:57 AM | ETH | DOWN | 4.0 min | +0.611% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:10:09 AM | NEAR | DOWN | 4.8 min | +1.923% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 8:59:50 AM | WTI | DOWN | 9 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 8:59:50 AM | NATGAS | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:59:34 AM | PLATINUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:59:34 AM | USDCAD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:59:34 AM | COPPER | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:58:46 AM | AUDUSD | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:56:53 AM | BNB | DOWN | 3.1 min | +0.185% | 3¢ | ❌ Lost | -$0.15 |
| 10/21 8:56:37 AM | ETH | DOWN | 3.4 min | +0.561% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
