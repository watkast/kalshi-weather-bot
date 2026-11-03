# 15-Minute 1¢ Study

*Updated Tue Nov 3, 9:54 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3563 finished bets | 1% | $119.60 | +30% | +3.36¢ | $68.15 / $51.45 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3295 | $47.20 | +13% |
| Volatility model ≥ 2%, hold to the close | 6589 | $42.30 | +5% |
| Momentum model ≥ 2%, hold to the close | 5431 | -$39.75 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43866 | 43854 | 164 (0%) | 1.07% | -$3,044.00 (-57%) | Hold to the close: -$3,044.00 (-57%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27044 | 4.7% | 0.4% (106) | -682% | ❌ Worse |
| Momentum model | 27044 | 4.6% | 0.4% (106) | -706% | ❌ Worse |
| Mean-reversion model | 27044 | 8.1% | 0.4% (106) | -830% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27044 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6589 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3563 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2021 | 22 | +55% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5431 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3295 | 29 | +13% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2152 | 19 | +23% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11180 | 76 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7844 | 65 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5249 | 46 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27248 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10365 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6241 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43854 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 164 | 0% | -$3,044.00 | -57% | — |
| Sell at 2¢ | 1732 | 4% | -$4,651.68 | -87% | 47 sec |
| Sell at 3¢ | 1188 | 3% | -$4,638.68 | -87% | 49 sec |
| Sell at 5¢ | 825 | 2% | -$4,537.75 | -85% | 63 sec |
| Sell at 10¢ | 497 | 1% | -$4,338.93 | -81% | 66 sec |
| Sell at 25¢ | 261 | 1% | -$4,014.09 | -75% | 83 sec |
| Sell at 50¢ | 168 | 0% | -$3,646.00 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2113 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 14084 | 78 | 7% | 4% | -45% | -86% | -86% |
| 1–2 min | 11092 | 39 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 16554 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3053 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3046 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3041 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3040 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3026 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3023 | 11 | 7% | 3% | -56% | -85% | -85% |
| NEAR | 3009 | 15 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3009 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3001 | 12 | 3% | 1% | -50% | -89% | -88% |
| GOLD | 1608 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1569 | 7 | 5% | 2% | -47% | -82% | -82% |
| WTI | 1566 | 5 | 3% | 1% | -61% | -92% | -93% |
| PLATINUM | 1397 | 4 | 2% | 1% | -73% | -96% | -96% |
| EURUSD | 1340 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1326 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1276 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1268 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1256 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1245 | 5 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 799 | 4 | 2% | 1% | -53% | -85% | -85% |
| USDCAD | 761 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 367 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 226 | 1 | 5% | 2% | -59% | -50% | -48% |
| 30YRRATE | 212 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 203 | 2 | 4% | 0% | -8% | -1% | -0% |
| 5YRRATE | 187 | 1 | 5% | 2% | -50% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22295 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21559 | 76 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4433 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4666 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7055 | 24 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 8075 | 33 | 7% | 3% | -55% | -86% | -86% |
| Over 0.5% | 3012 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 10864 | 48 | 4% | 2% | -50% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,735 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 9:53:35 AM | SOL | DOWN | 6.4 min | +0.406% | — | In play | — |
| 11/3 9:53:19 AM | ZEC | DOWN | 6.7 min | +1.016% | — | In play | — |
| 11/3 9:44:44 AM | XRP | UP | 16 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:44:28 AM | PALLADIUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:44:28 AM | BTC | UP | 32 sec | -0.033% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:44:28 AM | USDJPY | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:44:12 AM | GOLD | UP | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:44:12 AM | NEAR | UP | 47 sec | -0.430% | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:43:46 AM | BRENT | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:43:46 AM | PLATINUM | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:43:31 AM | SOL | UP | 89 sec | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:43:31 AM | DOGE | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:43:31 AM | 2YRRATE | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:43:31 AM | HYPE | UP | 89 sec | -0.297% | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:42:58 AM | BNB | UP | 2.0 min | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:42:58 AM | WTI | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:42:58 AM | SILVER | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:42:42 AM | 30YRRATE | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:42:26 AM | 10YRRATE | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:42:11 AM | COPPER | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:42:11 AM | 5YRRATE | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:41:53 AM | AUDUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:41:53 AM | GBPUSD | UP | 3.1 min | — | 33¢ | ❌ Lost | -$0.15 |
| 11/3 9:41:37 AM | EURUSD | UP | 3.4 min | — | 9¢ | ❌ Lost | -$0.15 |
| 11/3 9:29:53 AM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:29:53 AM | WTI | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:29:53 AM | USDCAD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:29:37 AM | GOLD | UP | 23 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:29:37 AM | 30YRRATE | UP | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:29:07 AM | AUDUSD | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
