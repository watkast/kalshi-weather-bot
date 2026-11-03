# 15-Minute 1¢ Study

*Updated Mon Nov 2, 10:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3531 finished bets | 1% | $123.65 | +31% | +3.50¢ | $69.65 / $54.00 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3264 | $50.80 | +14% |
| Volatility model ≥ 2%, hold to the close | 6541 | $48.00 | +6% |
| Momentum model ≥ 2%, hold to the close | 5395 | -$35.70 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43372 | 43350 | 161 (0%) | 1.07% | -$3,024.20 (-57%) | Hold to the close: -$3,024.20 (-57%) |

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
| Volatility model | 26829 | 4.7% | 0.4% (106) | -677% | ❌ Worse |
| Momentum model | 26829 | 4.6% | 0.4% (106) | -702% | ❌ Worse |
| Mean-reversion model | 26829 | 8.1% | 0.4% (106) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26829 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6541 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3531 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2000 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5395 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3264 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2132 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11076 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7765 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5190 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27032 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10228 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6090 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43350 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 161 | 0% | -$3,024.20 | -57% | — |
| Sell at 2¢ | 1711 | 4% | -$4,595.34 | -87% | 47 sec |
| Sell at 3¢ | 1173 | 3% | -$4,582.73 | -87% | 49 sec |
| Sell at 5¢ | 813 | 2% | -$4,483.75 | -85% | 63 sec |
| Sell at 10¢ | 490 | 1% | -$4,286.30 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,972.15 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,611.70 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2082 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13932 | 75 | 7% | 4% | -47% | -86% | -86% |
| 1–2 min | 10943 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16382 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3030 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3021 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3018 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3016 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3003 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3000 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2984 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 2983 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2977 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1588 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1548 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1545 | 4 | 3% | 1% | -69% | -92% | -93% |
| PLATINUM | 1379 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1319 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1312 | 6 | 2% | 1% | -57% | -69% | -69% |
| NATGAS | 1264 | 7 | 2% | 1% | -48% | -82% | -81% |
| GBPUSD | 1249 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1242 | 3 | 1% | 1% | -77% | -90% | -91% |
| USDJPY | 1231 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 776 | 4 | 2% | 1% | -52% | -85% | -84% |
| USDCAD | 740 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 350 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22063 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21287 | 74 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4394 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4635 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7004 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 8001 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2992 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11702 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,766 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 9:59:47 PM | PALLADIUM | DOWN | 13 sec | — | 0¢ | In play | — |
| 11/2 9:59:47 PM | EURUSD | DOWN | 13 sec | — | 0¢ | In play | — |
| 11/2 9:59:47 PM | HYPE | UP | 13 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:59:47 PM | USDCAD | UP | 13 sec | — | 0¢ | In play | — |
| 11/2 9:59:31 PM | NATGAS | DOWN | 29 sec | — | 0¢ | In play | — |
| 11/2 9:59:31 PM | AUDUSD | UP | 29 sec | — | 0¢ | In play | — |
| 11/2 9:59:16 PM | BTC | UP | 44 sec | -0.025% | 0¢ | In play | — |
| 11/2 9:59:16 PM | DOGE | UP | 44 sec | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:59:16 PM | BNB | DOWN | 44 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:59:16 PM | XRP | DOWN | 44 sec | +0.024% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:58:57 PM | GBPUSD | DOWN | 63 sec | — | 0¢ | In play | — |
| 11/2 9:58:57 PM | SOL | UP | 63 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:58:57 PM | ETH | DOWN | 63 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:58:57 PM | ZEC | UP | 63 sec | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:58:41 PM | SILVER | DOWN | 79 sec | — | 7¢ | In play | — |
| 11/2 9:58:41 PM | GOLD | DOWN | 79 sec | — | 5¢ | In play | — |
| 11/2 9:58:25 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | In play | — |
| 11/2 9:57:06 PM | COPPER | UP | 2.9 min | — | 0¢ | In play | — |
| 11/2 9:56:49 PM | NEAR | UP | 3.2 min | -0.624% | 1¢ | In play | — |
| 11/2 9:44:38 PM | EURUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:44:38 PM | HYPE | UP | 22 sec | -0.089% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:43:33 PM | AUDUSD | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:43:18 PM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:43:18 PM | SOL | UP | 1.7 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:42:44 PM | DOGE | UP | 2.3 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:42:13 PM | BTC | UP | 2.8 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:42:13 PM | ETH | UP | 2.8 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:42:13 PM | BNB | UP | 2.8 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:42:13 PM | NEAR | UP | 2.8 min | -0.453% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:41:54 PM | BRENT | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
