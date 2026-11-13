# 15-Minute 1¢ Study

*Updated Thu Nov 12, 9:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4265 finished bets | 1% | $170.60 | +36% | +4.00¢ | $82.15 / $88.45 |

*Expect about **93 buys a day** (~$13.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4005 | $97.75 | +23% |
| Volatility model ≥ 2%, hold to the close | 7863 | $33.50 | +4% |
| Momentum model ≥ 2%, hold to the close | 6531 | -$22.75 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 55512 | 55491 | 212 (0%) | 1.07% | -$3,802.55 (-56%) | Hold to the close: -$3,802.55 (-56%) |

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
| Volatility model | 33171 | 4.7% | 0.4% (133) | -669% | ❌ Worse |
| Momentum model | 33171 | 4.6% | 0.4% (133) | -695% | ❌ Worse |
| Mean-reversion model | 33171 | 8.0% | 0.4% (133) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33171 | 133 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7863 | 70 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4265 | 46 | +36% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2468 | 28 | +63% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 6531 | 52 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 4005 | 38 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2626 | 25 | +34% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13660 | 93 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9534 | 79 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6356 | 56 | +0% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33376 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13364 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8751 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 55491 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 212 | 0% | -$3,802.55 | -56% | — |
| Sell at 2¢ | 2213 | 4% | -$5,901.17 | -87% | 47 sec |
| Sell at 3¢ | 1505 | 3% | -$5,889.60 | -87% | 49 sec |
| Sell at 5¢ | 1036 | 2% | -$5,775.15 | -85% | 63 sec |
| Sell at 10¢ | 629 | 1% | -$5,540.56 | -82% | 65 sec |
| Sell at 25¢ | 330 | 1% | -$5,146.25 | -76% | 82 sec |
| Sell at 50¢ | 217 | 0% | -$4,661.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2762 | 13 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 17911 | 97 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 13986 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20819 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3736 | 17 | 5% | 3% | -41% | -88% | -87% |
| SOL | 3731 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3726 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3714 | 19 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3712 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3707 | 16 | 7% | 3% | -46% | -82% | -81% |
| BTC | 3689 | 18 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3687 | 17 | 5% | 2% | -40% | -85% | -85% |
| XRP | 3674 | 13 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 2008 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1989 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1950 | 9 | 5% | 2% | -45% | -83% | -83% |
| PLATINUM | 1778 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1722 | 6 | 2% | 1% | -67% | -90% | -90% |
| COPPER | 1667 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1649 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1640 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1619 | 6 | 2% | 1% | -65% | -96% | -96% |
| PALLADIUM | 1592 | 4 | 1% | 1% | -77% | -92% | -92% |
| AUDUSD | 1169 | 6 | 2% | 1% | -52% | -89% | -89% |
| USDCAD | 1130 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 740 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 375 | 2 | 4% | 2% | -50% | -68% | -66% |
| 2YRRATE | 360 | 4 | 4% | 2% | +4% | -41% | -40% |
| 30YRRATE | 356 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 330 | 2 | 4% | 2% | -43% | -93% | -94% |
| INX | 41 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28222 | 110 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 27269 | 102 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5251 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5646 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8532 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10093 | 41 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3846 | 18 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13478 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13343 | 62 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15217 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,830 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 9:29:48 PM | DOGE | UP | 11 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 11/12 9:29:48 PM | SOL | DOWN | 11 sec | +0.002% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:29:48 PM | SILVER | UP | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 9:29:48 PM | COPPER | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:29:48 PM | BRENT | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:29:32 PM | AUDUSD | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:29:32 PM | ETH | UP | 27 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 11/12 9:29:32 PM | BNB | UP | 27 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/12 9:29:16 PM | XRP | DOWN | 43 sec | +0.000% | 2¢ | ❌ Lost | -$0.15 |
| 11/12 9:29:16 PM | BTC | DOWN | 43 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 11/12 9:29:00 PM | NEAR | UP | 59 sec | -0.441% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:29:00 PM | GBPUSD | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:28:29 PM | USDCAD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:26:55 PM | HYPE | UP | 3.1 min | -0.991% | 0¢ | ❌ Lost | $0.00 |
| 11/12 9:26:24 PM | GOLD | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 9:25:52 PM | ZEC | UP | 4.1 min | -1.662% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 9:14:44 PM | NATGAS | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:14:44 PM | ZEC | UP | 15 sec | -0.132% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:14:28 PM | BNB | DOWN | 31 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:14:12 PM | SOL | UP | 47 sec | -0.198% | 0¢ | ❌ Lost | $0.00 |
| 11/12 9:14:12 PM | COPPER | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:13:56 PM | ETH | UP | 63 sec | -0.231% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:13:56 PM | DOGE | UP | 63 sec | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 9:13:56 PM | USDJPY | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:13:41 PM | BTC | UP | 79 sec | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 9:13:41 PM | NEAR | UP | 79 sec | -0.654% | 0¢ | ❌ Lost | $0.00 |
| 11/12 9:13:41 PM | HYPE | UP | 79 sec | -0.470% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 9:13:25 PM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:12:53 PM | AUDUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 9:12:53 PM | SILVER | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
