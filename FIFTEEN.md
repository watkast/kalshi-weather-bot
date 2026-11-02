# 15-Minute 1¢ Study

*Updated Mon Nov 2, 1:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3479 finished bets | 1% | $128.90 | +33% | +3.71¢ | $73.25 / $55.65 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6424 | $61.80 | +8% |
| Momentum model ≥ 5%, hold to the close | 3205 | $56.95 | +16% |
| Momentum model ≥ 2%, hold to the close | 5292 | -$24.45 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42303 | 42281 | 159 (0%) | 1.07% | -$2,919.75 (-57%) | Hold to the close: -$2,919.75 (-57%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26346 | 4.7% | 0.4% (106) | -672% | ❌ Worse |
| Momentum model | 26346 | 4.6% | 0.4% (106) | -694% | ❌ Worse |
| Mean-reversion model | 26346 | 8.1% | 0.4% (106) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26346 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6424 | 60 | +8% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3479 | 37 | +33% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1971 | 22 | +59% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5292 | 42 | -4% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3205 | 29 | +16% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2093 | 19 | +27% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10888 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7635 | 65 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5106 | 46 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26548 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 9914 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5819 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42281 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,919.75 | -57% | — |
| Sell at 2¢ | 1655 | 4% | -$4,491.45 | -87% | 47 sec |
| Sell at 3¢ | 1136 | 3% | -$4,478.71 | -87% | 48 sec |
| Sell at 5¢ | 790 | 2% | -$4,380.25 | -85% | 63 sec |
| Sell at 10¢ | 476 | 1% | -$4,200.19 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,880.94 | -75% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,520.75 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2012 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13584 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10682 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 15992 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2974 | 13 | 5% | 3% | -44% | -88% | -87% |
| SOL | 2965 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2962 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2961 | 9 | 5% | 2% | -62% | -89% | -87% |
| DOGE | 2949 | 6 | 4% | 2% | -74% | -90% | -89% |
| ETH | 2948 | 11 | 6% | 3% | -55% | -85% | -85% |
| NEAR | 2930 | 15 | 5% | 2% | -34% | -83% | -83% |
| BTC | 2930 | 14 | 5% | 2% | -36% | -88% | -89% |
| XRP | 2929 | 12 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1545 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1507 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1504 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1338 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1278 | 5 | 1% | 1% | -63% | -76% | -75% |
| EURUSD | 1276 | 3 | 2% | 1% | -78% | -89% | -89% |
| NATGAS | 1231 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1207 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1201 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1196 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 732 | 4 | 2% | 1% | -49% | -85% | -84% |
| USDCAD | 708 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 310 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 191 | 1 | 5% | 2% | -51% | -42% | -40% |
| 30YRRATE | 180 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 171 | 2 | 5% | 1% | +9% | +17% | +18% |
| 5YRRATE | 158 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21468 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20813 | 72 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4331 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4568 | 18 | 3% | 2% | -41% | -91% | -90% |
| 0.1–0.2% | 6879 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7824 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2941 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10421 | 37 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,804 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 1:41:06 AM | BTC | DOWN | 3.9 min | +0.268% | — | In play | — |
| 11/2 1:41:06 AM | XRP | DOWN | 3.9 min | +0.432% | — | In play | — |
| 11/2 1:41:06 AM | ZEC | DOWN | 3.9 min | +0.653% | — | In play | — |
| 11/2 1:40:50 AM | BNB | DOWN | 4.2 min | +0.185% | — | In play | — |
| 11/2 1:40:50 AM | DOGE | DOWN | 4.2 min | +0.305% | — | In play | — |
| 11/2 1:40:34 AM | NEAR | DOWN | 4.4 min | +0.429% | — | In play | — |
| 11/2 1:40:02 AM | SOL | DOWN | 5.0 min | +0.298% | — | In play | — |
| 11/2 1:39:46 AM | ETH | DOWN | 5.2 min | +0.261% | — | In play | — |
| 11/2 1:39:46 AM | USDCAD | UP | 5.2 min | — | — | In play | — |
| 11/2 1:39:14 AM | HYPE | DOWN | 5.8 min | +0.487% | — | In play | — |
| 11/2 1:38:58 AM | GBPUSD | DOWN | 6.0 min | — | — | In play | — |
| 11/2 1:38:42 AM | EURUSD | DOWN | 6.3 min | — | — | In play | — |
| 11/2 1:29:29 AM | EURUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:29 AM | 5YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:29 AM | 30YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:14 AM | SOL | DOWN | 46 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:14 AM | ETH | DOWN | 46 sec | +0.058% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:29:14 AM | GBPUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:14 AM | 10YRRATE | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:14 AM | DOGE | DOWN | 46 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:28:42 AM | 2YRRATE | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:28:26 AM | BNB | DOWN | 1.6 min | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:28:26 AM | NEAR | DOWN | 1.6 min | +0.225% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:28:10 AM | HYPE | DOWN | 1.8 min | +0.230% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:27:06 AM | PLATINUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:26:48 AM | GOLD | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:26:48 AM | COPPER | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:26:02 AM | USDCAD | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:25:13 AM | ZEC | UP | 4.8 min | -0.527% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:24:58 AM | PALLADIUM | UP | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
