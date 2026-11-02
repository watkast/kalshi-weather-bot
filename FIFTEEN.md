# 15-Minute 1¢ Study

*Updated Mon Nov 2, 9:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3497 finished bets | 1% | $126.95 | +32% | +3.63¢ | $72.05 / $54.90 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6456 | $57.75 | +7% |
| Momentum model ≥ 5%, hold to the close | 3225 | $54.70 | +16% |
| Momentum model ≥ 2%, hold to the close | 5321 | -$27.90 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42578 | 42566 | 159 (0%) | 1.07% | -$2,954.55 (-57%) | Hold to the close: -$2,954.55 (-57%) |

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
| Volatility model | 26475 | 4.7% | 0.4% (106) | -675% | ❌ Worse |
| Momentum model | 26475 | 4.6% | 0.4% (106) | -697% | ❌ Worse |
| Mean-reversion model | 26475 | 8.1% | 0.4% (106) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26475 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6456 | 60 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3497 | 37 | +32% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1985 | 22 | +58% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5321 | 42 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3225 | 29 | +16% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2104 | 19 | +26% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 10943 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7674 | 65 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5130 | 46 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26677 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9994 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5895 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42566 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,954.55 | -57% | — |
| Sell at 2¢ | 1665 | 4% | -$4,523.65 | -87% | 47 sec |
| Sell at 3¢ | 1142 | 3% | -$4,511.17 | -87% | 48 sec |
| Sell at 5¢ | 794 | 2% | -$4,412.45 | -85% | 63 sec |
| Sell at 10¢ | 479 | 1% | -$4,231.06 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,915.74 | -76% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,555.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2036 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13663 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10752 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16104 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2989 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 2980 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2977 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2975 | 9 | 5% | 2% | -62% | -89% | -87% |
| DOGE | 2964 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2962 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2945 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2943 | 15 | 5% | 2% | -34% | -83% | -83% |
| XRP | 2942 | 12 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1557 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1515 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1512 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1348 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1288 | 3 | 2% | 1% | -78% | -89% | -89% |
| COPPER | 1286 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1241 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1219 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1216 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1206 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 743 | 4 | 1% | 1% | -50% | -85% | -84% |
| USDCAD | 718 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 319 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 196 | 1 | 5% | 2% | -52% | -44% | -42% |
| 30YRRATE | 184 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 178 | 2 | 4% | 1% | +5% | +13% | +14% |
| 5YRRATE | 163 | 1 | 6% | 2% | -43% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21637 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20929 | 72 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4355 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4595 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6910 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7866 | 33 | 7% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2946 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10573 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,790 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 9:23:29 AM | 5YRRATE | UP | 6.5 min | — | — | In play | — |
| 11/2 9:23:29 AM | 10YRRATE | UP | 6.5 min | — | — | In play | — |
| 11/2 9:14:51 AM | PALLADIUM | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:51 AM | BNB | UP | 9 sec | -0.088% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:51 AM | XRP | UP | 9 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:14:51 AM | AUDUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:35 AM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:19 AM | GOLD | DOWN | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:14:19 AM | ZEC | UP | 41 sec | -0.303% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:14:03 AM | PLATINUM | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:03 AM | DOGE | UP | 56 sec | -0.185% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:03 AM | EURUSD | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:03 AM | HYPE | UP | 56 sec | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:03 AM | BTC | UP | 56 sec | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:13:47 AM | SOL | UP | 72 sec | -0.311% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:13:47 AM | ETH | UP | 72 sec | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:13:31 AM | 2YRRATE | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:13:10 AM | 30YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:12:51 AM | 5YRRATE | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:12:51 AM | 10YRRATE | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:12:35 AM | WTI | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:12:04 AM | USDCAD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:10:25 AM | BRENT | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:59:44 AM | GBPUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:59:28 AM | PLATINUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:59:28 AM | WTI | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:58:55 AM | USDCAD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:58:39 AM | PALLADIUM | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:58:39 AM | BRENT | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:58:23 AM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
