# 15-Minute 1¢ Study

*Updated Wed Nov 4, 2:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3650 finished bets | 1% | $124.75 | +31% | +3.42¢ | $77.50 / $47.25 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3387 | $52.05 | +14% |
| Volatility model ≥ 2%, hold to the close | 6769 | $35.90 | +4% |
| Momentum model ≥ 2%, hold to the close | 5579 | -$41.50 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45608 | 45597 | 169 (0%) | 1.07% | -$3,191.80 (-57%) | Hold to the close: -$3,191.80 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27837 | 4.7% | 0.4% (109) | -678% | ❌ Worse |
| Momentum model | 27837 | 4.6% | 0.4% (109) | -705% | ❌ Worse |
| Mean-reversion model | 27837 | 8.1% | 0.4% (109) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27837 | 109 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6769 | 61 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3650 | 38 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2076 | 23 | +59% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5579 | 43 | -6% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3387 | 30 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2209 | 19 | +21% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11528 | 79 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8096 | 68 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5426 | 48 | +0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28042 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10845 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6710 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45597 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 169 | 0% | -$3,191.80 | -57% | — |
| Sell at 2¢ | 1795 | 4% | -$4,839.10 | -87% | 47 sec |
| Sell at 3¢ | 1227 | 3% | -$4,827.27 | -87% | 49 sec |
| Sell at 5¢ | 851 | 2% | -$4,724.65 | -85% | 63 sec |
| Sell at 10¢ | 513 | 1% | -$4,521.77 | -81% | 65 sec |
| Sell at 25¢ | 268 | 1% | -$4,194.72 | -75% | 83 sec |
| Sell at 50¢ | 172 | 0% | -$3,822.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2255 | 10 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 14677 | 79 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11487 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17167 | 41 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3141 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3136 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3128 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3128 | 17 | 5% | 2% | -32% | -85% | -84% |
| DOGE | 3116 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3110 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3099 | 15 | 5% | 2% | -34% | -87% | -89% |
| NEAR | 3095 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3089 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1680 | 5 | 5% | 2% | -64% | -81% | -83% |
| SILVER | 1632 | 8 | 5% | 2% | -42% | -82% | -81% |
| WTI | 1631 | 5 | 4% | 1% | -63% | -92% | -93% |
| PLATINUM | 1463 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1408 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1379 | 6 | 2% | 1% | -59% | -70% | -70% |
| GBPUSD | 1333 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1326 | 8 | 2% | 1% | -44% | -75% | -75% |
| USDJPY | 1315 | 5 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1311 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 862 | 4 | 2% | 1% | -57% | -86% | -86% |
| USDCAD | 832 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 423 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 259 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 240 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 239 | 2 | 3% | 0% | -22% | -16% | -15% |
| 5YRRATE | 222 | 1 | 5% | 2% | -58% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23155 | 90 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22442 | 79 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4518 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4773 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7224 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8344 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3175 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10696 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,683 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 1:59:52 PM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:59:52 PM | BNB | DOWN | 7 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:59:52 PM | USDCAD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:59:52 PM | XRP | DOWN | 7 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:59:52 PM | BTC | UP | 7 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:59:52 PM | NEAR | DOWN | 7 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:59:52 PM | ZEC | DOWN | 7 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:59:52 PM | PALLADIUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:59:36 PM | USDJPY | UP | 23 sec | — | 7¢ | ❌ Lost | -$0.15 |
| 11/4 1:59:36 PM | EURUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:59:36 PM | SILVER | DOWN | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:59:36 PM | DOGE | DOWN | 23 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:59:36 PM | ETH | DOWN | 23 sec | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:59:20 PM | 5YRRATE | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:59:20 PM | GOLD | DOWN | 40 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:58:46 PM | 10YRRATE | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:58:30 PM | SOL | UP | 1.5 min | -0.153% | 7¢ | ❌ Lost | -$0.15 |
| 11/4 1:58:15 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:58:15 PM | 30YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:57:41 PM | NATGAS | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:55:53 PM | HYPE | UP | 4.1 min | -0.406% | 3¢ | ❌ Lost | -$0.15 |
| 11/4 1:44:59 PM | 2YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:44:59 PM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:44:59 PM | PALLADIUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:44:43 PM | AUDUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:44:43 PM | NEAR | UP | 17 sec | -0.236% | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:44:27 PM | GOLD | UP | 33 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:44:27 PM | SOL | UP | 33 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:44:12 PM | SILVER | UP | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:44:12 PM | BTC | UP | 47 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
