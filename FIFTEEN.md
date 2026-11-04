# 15-Minute 1¢ Study

*Updated Wed Nov 4, 7:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3641 finished bets | 1% | $111.65 | +27% | +3.07¢ | $78.10 / $33.55 |

*Expect about **98 buys a day** (~$14.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3376 | $39.25 | +11% |
| Volatility model ≥ 2%, hold to the close | 6739 | $25.20 | +3% |
| Momentum model ≥ 2%, hold to the close | 5554 | -$52.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45275 | 45255 | 167 (0%) | 1.07% | -$3,175.55 (-58%) | Hold to the close: -$3,175.55 (-58%) |

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
| Volatility model | 27696 | 4.7% | 0.4% (108) | -681% | ❌ Worse |
| Momentum model | 27696 | 4.6% | 0.4% (108) | -708% | ❌ Worse |
| Mean-reversion model | 27696 | 8.1% | 0.4% (108) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27696 | 108 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6739 | 60 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3641 | 37 | +27% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2069 | 22 | +52% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5554 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3376 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2202 | 19 | +21% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11458 | 78 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8052 | 67 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5394 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27901 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10748 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6606 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45255 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 167 | 0% | -$3,175.55 | -58% | — |
| Sell at 2¢ | 1776 | 4% | -$4,799.79 | -87% | 47 sec |
| Sell at 3¢ | 1218 | 3% | -$4,786.53 | -87% | 49 sec |
| Sell at 5¢ | 842 | 2% | -$4,686.25 | -85% | 63 sec |
| Sell at 10¢ | 509 | 1% | -$4,482.76 | -81% | 65 sec |
| Sell at 25¢ | 266 | 1% | -$4,157.09 | -75% | 83 sec |
| Sell at 50¢ | 170 | 0% | -$3,792.05 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2219 | 10 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 14557 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11417 | 39 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 17051 | 39 | 1% | 0% | -67% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3126 | 13 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3120 | 12 | 4% | 2% | -51% | -90% | -90% |
| HYPE | 3112 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3112 | 17 | 5% | 2% | -31% | -85% | -85% |
| DOGE | 3100 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3094 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3083 | 14 | 5% | 2% | -38% | -88% | -89% |
| NEAR | 3081 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3073 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1666 | 5 | 5% | 2% | -64% | -81% | -83% |
| WTI | 1622 | 5 | 4% | 1% | -63% | -92% | -93% |
| SILVER | 1619 | 7 | 5% | 2% | -49% | -82% | -82% |
| PLATINUM | 1449 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1394 | 3 | 3% | 1% | -80% | -89% | -89% |
| COPPER | 1367 | 6 | 2% | 1% | -59% | -70% | -69% |
| GBPUSD | 1319 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1315 | 8 | 2% | 1% | -43% | -75% | -74% |
| USDJPY | 1302 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1298 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 850 | 4 | 2% | 1% | -56% | -86% | -86% |
| USDCAD | 818 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 412 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 251 | 1 | 5% | 2% | -63% | -55% | -52% |
| 30YRRATE | 231 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 229 | 2 | 3% | 0% | -18% | -12% | -12% |
| 5YRRATE | 212 | 1 | 5% | 2% | -56% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22977 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22278 | 78 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4510 | 21 | 2% | 1% | -19% | -83% | -82% |
| 0.05–0.1% | 4761 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7205 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8297 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3120 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11178 | 48 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,696 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 7:40:13 AM | DOGE | DOWN | 4.8 min | +0.779% | — | In play | — |
| 11/4 7:40:13 AM | COPPER | DOWN | 4.8 min | — | — | In play | — |
| 11/4 7:39:57 AM | ZEC | DOWN | 5.0 min | +2.072% | — | In play | — |
| 11/4 7:39:57 AM | SOL | DOWN | 5.0 min | +0.827% | — | In play | — |
| 11/4 7:39:57 AM | BTC | DOWN | 5.0 min | +0.517% | — | In play | — |
| 11/4 7:39:26 AM | SILVER | DOWN | 5.5 min | — | — | In play | — |
| 11/4 7:38:55 AM | GOLD | DOWN | 6.1 min | — | — | In play | — |
| 11/4 7:38:55 AM | PLATINUM | DOWN | 6.1 min | — | — | In play | — |
| 11/4 7:38:39 AM | HYPE | DOWN | 6.3 min | +1.012% | — | In play | — |
| 11/4 7:38:39 AM | XRP | DOWN | 6.3 min | +0.679% | — | In play | — |
| 11/4 7:29:56 AM | ZEC | DOWN | 3 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:29:56 AM | USDJPY | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:56 AM | PLATINUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:56 AM | 30YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:39 AM | SOL | UP | 20 sec | -0.063% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:39 AM | USDCAD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:39 AM | PALLADIUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:39 AM | BNB | DOWN | 20 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:29:39 AM | 10YRRATE | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:23 AM | 5YRRATE | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:23 AM | ETH | UP | 36 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:29:23 AM | EURUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:23 AM | 2YRRATE | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:29:23 AM | XRP | DOWN | 36 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:29:23 AM | BTC | UP | 36 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:29:07 AM | BRENT | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:28:53 AM | AUDUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:28:53 AM | WTI | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:28:35 AM | HYPE | UP | 84 sec | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 7:27:34 AM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
