# 15-Minute 1¢ Study

*Updated Wed Nov 4, 6:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3668 finished bets | 1% | $122.80 | +30% | +3.35¢ | $90.60 / $32.20 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3401 | $50.55 | +14% |
| Volatility model ≥ 2%, hold to the close | 6801 | $32.45 | +4% |
| Momentum model ≥ 2%, hold to the close | 5604 | -$44.35 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45898 | 45880 | 169 (0%) | 1.07% | -$3,228.55 (-58%) | Hold to the close: -$3,228.55 (-58%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27985 | 4.7% | 0.4% (109) | -679% | ❌ Worse |
| Momentum model | 27985 | 4.6% | 0.4% (109) | -705% | ❌ Worse |
| Mean-reversion model | 27985 | 8.1% | 0.4% (109) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27985 | 109 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6801 | 61 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3668 | 38 | +30% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2086 | 23 | +58% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5604 | 43 | -7% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3401 | 30 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2220 | 19 | +20% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11598 | 79 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8142 | 68 | -7% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5453 | 48 | -0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28190 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10915 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6775 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45880 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 169 | 0% | -$3,228.55 | -58% | — |
| Sell at 2¢ | 1804 | 4% | -$4,873.51 | -87% | 47 sec |
| Sell at 3¢ | 1231 | 3% | -$4,862.46 | -87% | 48 sec |
| Sell at 5¢ | 854 | 2% | -$4,759.45 | -85% | 63 sec |
| Sell at 10¢ | 515 | 1% | -$4,555.90 | -81% | 65 sec |
| Sell at 25¢ | 268 | 1% | -$4,231.47 | -76% | 83 sec |
| Sell at 50¢ | 172 | 0% | -$3,859.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2274 | 10 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 14780 | 79 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11541 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17274 | 41 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3158 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3153 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3145 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3145 | 17 | 5% | 2% | -32% | -85% | -85% |
| DOGE | 3133 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3127 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3113 | 15 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 3111 | 15 | 5% | 2% | -38% | -84% | -84% |
| XRP | 3105 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1690 | 5 | 5% | 2% | -64% | -81% | -83% |
| WTI | 1644 | 5 | 4% | 1% | -63% | -92% | -92% |
| SILVER | 1642 | 8 | 5% | 2% | -42% | -82% | -81% |
| PLATINUM | 1471 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1418 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1386 | 6 | 2% | 1% | -60% | -70% | -70% |
| GBPUSD | 1342 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1331 | 8 | 2% | 1% | -44% | -75% | -75% |
| USDJPY | 1326 | 5 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1319 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 872 | 4 | 2% | 1% | -57% | -86% | -86% |
| USDCAD | 845 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 432 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 260 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 244 | 0 | 2% | 1% | -100% | -96% | -95% |
| 2YRRATE | 243 | 2 | 3% | 0% | -23% | -17% | -17% |
| 5YRRATE | 225 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23276 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22604 | 79 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4533 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4795 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7258 | 25 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8409 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3187 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12222 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,686 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 6:28:03 PM | ETH | UP | 1.9 min | -0.208% | — | In play | — |
| 11/4 6:27:29 PM | PLATINUM | UP | 2.5 min | — | — | In play | — |
| 11/4 6:27:29 PM | GOLD | UP | 2.5 min | — | — | In play | — |
| 11/4 6:27:13 PM | COPPER | UP | 2.8 min | — | — | In play | — |
| 11/4 6:24:49 PM | WTI | UP | 5.2 min | — | — | In play | — |
| 11/4 6:24:31 PM | BRENT | UP | 5.5 min | — | — | In play | — |
| 11/4 6:22:21 PM | BNB | UP | 7.7 min | -0.467% | — | In play | — |
| 11/4 6:14:44 PM | DOGE | UP | 15 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/4 6:14:44 PM | SILVER | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 6:14:44 PM | GBPUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:28 PM | USDCAD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:28 PM | NEAR | DOWN | 31 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/4 6:14:28 PM | XRP | UP | 31 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:28 PM | ZEC | DOWN | 31 sec | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:12 PM | WTI | UP | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:12 PM | SOL | UP | 48 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 11/4 6:14:12 PM | EURUSD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:12 PM | ETH | UP | 48 sec | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:13:37 PM | AUDUSD | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:13:21 PM | HYPE | UP | 1.6 min | -0.321% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:46 PM | USDJPY | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:14 PM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:14 PM | BNB | UP | 2.8 min | -0.259% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:14 PM | PLATINUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:14 PM | GOLD | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:09:16 PM | COPPER | UP | 5.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/4 5:59:44 PM | COPPER | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:59:28 PM | SILVER | DOWN | 32 sec | — | 1¢ | ❌ Lost | $0.00 |
| 11/4 5:58:41 PM | GBPUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:58:09 PM | SOL | UP | 1.8 min | -0.231% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
