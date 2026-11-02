# 15-Minute 1¢ Study

*Updated Mon Nov 2, 9:13 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| 42561 | 42545 | 159 (0%) | 1.07% | -$2,952.15 (-57%) | Hold to the close: -$2,952.15 (-57%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26467 | 4.7% | 0.4% (106) | -675% | ❌ Worse |
| Momentum model | 26467 | 4.6% | 0.4% (106) | -697% | ❌ Worse |
| Mean-reversion model | 26467 | 8.1% | 0.4% (106) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26467 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6456 | 60 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3497 | 37 | +32% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1985 | 22 | +58% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5321 | 42 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3225 | 29 | +16% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2104 | 19 | +26% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 10942 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7674 | 65 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5130 | 46 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26669 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9989 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5887 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42545 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,952.15 | -57% | — |
| Sell at 2¢ | 1665 | 4% | -$4,521.25 | -87% | 47 sec |
| Sell at 3¢ | 1142 | 3% | -$4,508.77 | -87% | 48 sec |
| Sell at 5¢ | 794 | 2% | -$4,410.05 | -85% | 63 sec |
| Sell at 10¢ | 479 | 1% | -$4,228.66 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,913.34 | -76% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,553.15 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2036 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13658 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10748 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16092 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2988 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 2979 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2976 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2974 | 9 | 5% | 2% | -62% | -89% | -87% |
| DOGE | 2963 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2961 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2944 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2943 | 15 | 5% | 2% | -34% | -83% | -83% |
| XRP | 2941 | 12 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1556 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1515 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1511 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1347 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1287 | 3 | 2% | 1% | -78% | -89% | -89% |
| COPPER | 1286 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1241 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1219 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1215 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1205 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 742 | 4 | 1% | 1% | -50% | -85% | -84% |
| USDCAD | 717 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 318 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 195 | 1 | 5% | 2% | -52% | -43% | -41% |
| 30YRRATE | 183 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 177 | 2 | 5% | 1% | +5% | +13% | +14% |
| 5YRRATE | 162 | 1 | 6% | 2% | -42% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21619 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20926 | 72 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4354 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4594 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6908 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7862 | 33 | 7% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2946 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10552 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,794 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 9:13:10 AM | 30YRRATE | UP | 1.8 min | — | — | In play | — |
| 11/2 9:12:51 AM | 5YRRATE | UP | 2.1 min | — | — | In play | — |
| 11/2 9:12:51 AM | 10YRRATE | UP | 2.1 min | — | — | In play | — |
| 11/2 9:12:35 AM | WTI | UP | 2.4 min | — | — | In play | — |
| 11/2 9:12:04 AM | USDCAD | DOWN | 2.9 min | — | — | In play | — |
| 11/2 9:10:25 AM | BRENT | UP | 4.6 min | — | — | In play | — |
| 11/2 8:59:44 AM | GBPUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:59:28 AM | PLATINUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:59:28 AM | WTI | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:58:55 AM | USDCAD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:58:39 AM | PALLADIUM | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:58:39 AM | BRENT | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:58:23 AM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 8:58:23 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:58:04 AM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:56:29 AM | HYPE | UP | 3.5 min | -0.413% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:55:39 AM | XRP | UP | 4.3 min | -0.487% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:55:39 AM | ETH | UP | 4.3 min | -0.446% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:55:39 AM | BTC | UP | 4.3 min | -0.415% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:55:07 AM | SOL | UP | 4.9 min | -0.466% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:54:48 AM | BNB | UP | 5.2 min | -0.301% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:54:48 AM | NEAR | UP | 5.2 min | -0.985% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:54:32 AM | DOGE | UP | 5.5 min | -0.423% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:53:28 AM | ZEC | UP | 6.5 min | -0.931% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:44:58 AM | XRP | DOWN | 2 sec | +0.136% | 0¢ | ❌ Lost | $0.00 |
| 11/2 8:44:58 AM | ZEC | DOWN | 2 sec | +0.086% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:44:58 AM | BTC | DOWN | 2 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/2 8:44:43 AM | COPPER | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:44:43 AM | 2YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:44:43 AM | 5YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
