# 15-Minute 1¢ Study

*Updated Mon Nov 2, 6:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3524 finished bets | 1% | $123.95 | +31% | +3.52¢ | $69.95 / $54.00 |

*Expect about **99 buys a day** (~$14.78/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3256 | $51.25 | +14% |
| Volatility model ≥ 2%, hold to the close | 6517 | $50.40 | +6% |
| Momentum model ≥ 2%, hold to the close | 5383 | -$34.95 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43092 | 43072 | 160 (0%) | 1.07% | -$3,004.00 (-57%) | Hold to the close: -$3,004.00 (-57%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26694 | 4.7% | 0.4% (106) | -675% | ❌ Worse |
| Momentum model | 26694 | 4.6% | 0.4% (106) | -699% | ❌ Worse |
| Mean-reversion model | 26694 | 8.1% | 0.4% (106) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26694 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6517 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3524 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1995 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5383 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3256 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2125 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11031 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7734 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5170 | 46 | +1% | -80% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26896 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 10141 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6035 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43072 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 160 | 0% | -$3,004.00 | -57% | — |
| Sell at 2¢ | 1692 | 4% | -$4,566.08 | -87% | 47 sec |
| Sell at 3¢ | 1162 | 3% | -$4,552.82 | -87% | 48 sec |
| Sell at 5¢ | 807 | 2% | -$4,453.45 | -85% | 63 sec |
| Sell at 10¢ | 488 | 1% | -$4,268.72 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,951.95 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,591.50 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2066 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13840 | 75 | 7% | 4% | -47% | -87% | -86% |
| 1–2 min | 10873 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16282 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3014 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3005 | 11 | 4% | 2% | -54% | -91% | -91% |
| BNB | 3002 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 3000 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2988 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2985 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2969 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2968 | 15 | 5% | 2% | -34% | -83% | -84% |
| XRP | 2965 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1576 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1536 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1534 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1366 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1306 | 3 | 2% | 1% | -79% | -89% | -88% |
| COPPER | 1302 | 6 | 2% | 1% | -57% | -69% | -68% |
| NATGAS | 1256 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1237 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1232 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1222 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 764 | 4 | 2% | 1% | -51% | -85% | -84% |
| USDCAD | 731 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 339 | 0 | 1% | 1% | -100% | -97% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21899 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21173 | 73 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4377 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4619 | 18 | 3% | 2% | -41% | -91% | -90% |
| 0.1–0.2% | 6964 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7950 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2981 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,763 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 6:13:16 PM | SOL | DOWN | 1.7 min | +0.125% | — | In play | — |
| 11/2 6:13:16 PM | ZEC | DOWN | 1.7 min | +0.384% | — | In play | — |
| 11/2 6:13:16 PM | COPPER | UP | 1.7 min | — | — | In play | — |
| 11/2 6:13:16 PM | BTC | DOWN | 1.7 min | +0.147% | — | In play | — |
| 11/2 6:12:57 PM | BRENT | DOWN | 2.0 min | — | — | In play | — |
| 11/2 6:12:10 PM | WTI | DOWN | 2.8 min | — | — | In play | — |
| 11/2 6:11:35 PM | GOLD | UP | 3.4 min | — | — | In play | — |
| 11/2 6:11:19 PM | PLATINUM | UP | 3.7 min | — | — | In play | — |
| 11/2 6:10:47 PM | PALLADIUM | UP | 4.2 min | — | — | In play | — |
| 11/2 6:09:39 PM | SILVER | UP | 5.3 min | — | — | In play | — |
| 11/2 5:59:48 PM | COPPER | DOWN | 12 sec | — | 0¢ | ✅ Won | $13.85 |
| 11/2 5:59:48 PM | BTC | DOWN | 12 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:59:48 PM | XRP | UP | 12 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:59:32 PM | PLATINUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:59:32 PM | ETH | DOWN | 28 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:59:17 PM | EURUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:58:59 PM | HYPE | UP | 61 sec | -0.173% | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:58:27 PM | SOL | UP | 1.6 min | -0.123% | 2¢ | ❌ Lost | -$0.15 |
| 11/2 5:58:27 PM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:58:12 PM | BRENT | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:57:38 PM | NEAR | UP | 2.4 min | -0.454% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:57:38 PM | DOGE | UP | 2.4 min | -0.207% | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:57:38 PM | ZEC | UP | 2.4 min | -0.450% | 3¢ | ❌ Lost | $0.00 |
| 11/2 5:57:07 PM | BNB | UP | 2.9 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:56:32 PM | WTI | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:56:01 PM | GBPUSD | DOWN | 4.0 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/2 5:56:01 PM | SILVER | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:55:43 PM | GOLD | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:55:27 PM | PALLADIUM | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:54:37 PM | AUDUSD | DOWN | 5.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
