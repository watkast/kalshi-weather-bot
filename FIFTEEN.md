# 15-Minute 1¢ Study

*Updated Tue Nov 3, 11:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3615 finished bets | 1% | $114.35 | +28% | +3.16¢ | $79.45 / $34.90 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3348 | $42.10 | +12% |
| Volatility model ≥ 2%, hold to the close | 6697 | $30.00 | +4% |
| Momentum model ≥ 2%, hold to the close | 5516 | -$48.90 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44836 | 44826 | 166 (0%) | 1.07% | -$3,135.40 (-57%) | Hold to the close: -$3,135.40 (-57%) |

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
| Volatility model | 27512 | 4.7% | 0.4% (108) | -675% | ❌ Worse |
| Momentum model | 27512 | 4.6% | 0.4% (108) | -701% | ❌ Worse |
| Mean-reversion model | 27512 | 8.1% | 0.4% (108) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27512 | 108 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6697 | 60 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3615 | 37 | +28% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2049 | 22 | +54% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5516 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3348 | 29 | +12% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2182 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11388 | 78 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7999 | 67 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5355 | 47 | -0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27717 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10629 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6480 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44826 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 166 | 0% | -$3,135.40 | -57% | — |
| Sell at 2¢ | 1764 | 4% | -$4,762.76 | -87% | 47 sec |
| Sell at 3¢ | 1210 | 3% | -$4,749.50 | -87% | 49 sec |
| Sell at 5¢ | 838 | 2% | -$4,648.70 | -85% | 63 sec |
| Sell at 10¢ | 506 | 1% | -$4,446.54 | -81% | 66 sec |
| Sell at 25¢ | 266 | 1% | -$4,116.94 | -75% | 83 sec |
| Sell at 50¢ | 170 | 0% | -$3,751.90 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2200 | 10 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 14417 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11301 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16897 | 38 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3105 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3099 | 12 | 4% | 2% | -51% | -90% | -90% |
| BNB | 3092 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3091 | 9 | 5% | 2% | -64% | -89% | -87% |
| DOGE | 3079 | 6 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3074 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3062 | 15 | 5% | 2% | -37% | -84% | -84% |
| BTC | 3062 | 14 | 5% | 2% | -38% | -88% | -89% |
| XRP | 3053 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1648 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1604 | 7 | 5% | 2% | -48% | -82% | -82% |
| WTI | 1603 | 5 | 3% | 1% | -62% | -92% | -93% |
| PLATINUM | 1435 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1375 | 3 | 3% | 1% | -80% | -89% | -88% |
| COPPER | 1356 | 6 | 2% | 1% | -59% | -70% | -69% |
| NATGAS | 1305 | 7 | 2% | 1% | -50% | -82% | -81% |
| GBPUSD | 1305 | 3 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 1286 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1284 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 835 | 4 | 2% | 1% | -55% | -86% | -85% |
| USDCAD | 802 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 394 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 223 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 215 | 2 | 4% | 0% | -13% | -7% | -6% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22780 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22046 | 77 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4484 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4725 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7172 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8229 | 33 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3099 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12126 | 39 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,722 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 10:59:45 PM | XRP | UP | 15 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/3 10:59:45 PM | NATGAS | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:59:45 PM | BTC | UP | 15 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:59:45 PM | DOGE | UP | 15 sec | -0.011% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:59:45 PM | NEAR | UP | 15 sec | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:59:29 PM | HYPE | UP | 31 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 11/3 10:58:58 PM | AUDUSD | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:58:58 PM | SOL | UP | 61 sec | -0.175% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:58:42 PM | ETH | UP | 77 sec | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:58:26 PM | BNB | UP | 1.6 min | -0.250% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:58:26 PM | ZEC | UP | 1.6 min | -0.631% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:57:38 PM | USDJPY | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:55:45 PM | USDCAD | UP | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:55:13 PM | PLATINUM | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:54:57 PM | SILVER | DOWN | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:54:39 PM | GOLD | DOWN | 5.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:54:23 PM | PALLADIUM | DOWN | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:44:37 PM | COPPER | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:43:47 PM | EURUSD | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:43:15 PM | AUDUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:43:15 PM | WTI | UP | 1.8 min | — | 4¢ | ❌ Lost | -$0.15 |
| 11/3 10:43:15 PM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:43:00 PM | GBPUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:43:00 PM | BRENT | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 10:42:12 PM | DOGE | DOWN | 2.8 min | +0.503% | 0¢ | ❌ Lost | $0.00 |
| 11/3 10:41:38 PM | XRP | DOWN | 3.4 min | +0.425% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:41:06 PM | ZEC | DOWN | 3.9 min | +1.028% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:40:19 PM | BTC | DOWN | 4.7 min | +0.413% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:40:19 PM | SOL | DOWN | 4.7 min | +0.648% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:40:19 PM | HYPE | DOWN | 4.7 min | +0.653% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
