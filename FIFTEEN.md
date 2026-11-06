# 15-Minute 1¢ Study

*Updated Fri Nov 6, 1:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3783 finished bets | 1% | $126.00 | +30% | +3.33¢ | $83.40 / $42.60 |

*Expect about **96 buys a day** (~$14.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3527 | $53.30 | +14% |
| Volatility model ≥ 2%, hold to the close | 6997 | $25.60 | +3% |
| Momentum model ≥ 2%, hold to the close | 5777 | -$47.45 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48158 | 48141 | 174 (0%) | 1.07% | -$3,436.65 (-59%) | Hold to the close: -$3,436.65 (-59%) |

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
| Volatility model | 28990 | 4.7% | 0.4% (111) | -692% | ❌ Worse |
| Momentum model | 28990 | 4.6% | 0.4% (111) | -718% | ❌ Worse |
| Mean-reversion model | 28990 | 8.1% | 0.4% (111) | -841% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28990 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6997 | 62 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3783 | 39 | +30% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2165 | 24 | +60% | -71% | -70% | -67% |
| Momentum model ≥ 2% | 5777 | 44 | -7% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3527 | 31 | +14% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2306 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 11987 | 80 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8399 | 69 | -9% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5614 | 49 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29195 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11611 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7335 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48141 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 174 | 0% | -$3,436.65 | -59% | — |
| Sell at 2¢ | 1890 | 4% | -$5,129.25 | -87% | 47 sec |
| Sell at 3¢ | 1290 | 3% | -$5,117.55 | -87% | 49 sec |
| Sell at 5¢ | 894 | 2% | -$5,011.55 | -85% | 63 sec |
| Sell at 10¢ | 539 | 1% | -$4,802.56 | -82% | 66 sec |
| Sell at 25¢ | 281 | 1% | -$4,466.54 | -76% | 83 sec |
| Sell at 50¢ | 179 | 0% | -$4,090.40 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2389 | 10 | 11% | 4% | -60% | -81% | -83% |
| 2–5 min | 15469 | 82 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 12125 | 40 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18146 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3272 | 13 | 5% | 3% | -49% | -88% | -88% |
| SOL | 3265 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3257 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3256 | 10 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 3245 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3242 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3223 | 16 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3221 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3214 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1780 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1733 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1730 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1564 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1499 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| GBPUSD | 1425 | 4 | 2% | 1% | -74% | -96% | -96% |
| NATGAS | 1417 | 8 | 2% | 1% | -47% | -76% | -76% |
| PALLADIUM | 1403 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1403 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 957 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 926 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 513 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 299 | 1 | 4% | 1% | -69% | -61% | -59% |
| 2YRRATE | 282 | 3 | 4% | 1% | -1% | -26% | -26% |
| 30YRRATE | 281 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 258 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24434 | 93 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23707 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4650 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4945 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7506 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8755 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3331 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11477 | 41 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,620 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 1:29:45 PM | 5YRRATE | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:29:45 PM | 2YRRATE | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:29:13 PM | USDJPY | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:28:57 PM | GBPUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:28:26 PM | WTI | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:28:26 PM | BRENT | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:28:26 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:27:54 PM | NATGAS | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:27:22 PM | USDCAD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:27:22 PM | SILVER | UP | 2.6 min | — | 10¢ | ❌ Lost | -$0.15 |
| 11/6 1:27:06 PM | BTC | UP | 2.9 min | -0.171% | 2¢ | ❌ Lost | -$0.15 |
| 11/6 1:27:06 PM | AUDUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:26:50 PM | BNB | UP | 3.1 min | -0.219% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:26:35 PM | ZEC | UP | 3.4 min | -1.163% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:26:35 PM | ETH | UP | 3.4 min | -0.276% | 5¢ | ❌ Lost | -$0.15 |
| 11/6 1:26:03 PM | HYPE | UP | 3.9 min | -0.489% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:25:15 PM | SOL | UP | 4.7 min | -0.453% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:25:15 PM | NEAR | UP | 4.7 min | -0.632% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:24:47 PM | XRP | UP | 5.2 min | -0.474% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:24:01 PM | DOGE | UP | 6.0 min | -0.323% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:14:53 PM | DOGE | UP | 7 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:14:53 PM | NATGAS | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:14:53 PM | 2YRRATE | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:14:53 PM | BTC | UP | 7 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:14:53 PM | BRENT | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:14:08 PM | ZEC | UP | 52 sec | -0.311% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:14:08 PM | BNB | UP | 52 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:14:08 PM | NEAR | UP | 52 sec | -0.295% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:14:08 PM | ETH | UP | 52 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:14:08 PM | COPPER | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
