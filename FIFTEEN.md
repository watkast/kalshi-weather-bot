# 15-Minute 1¢ Study

*Updated Wed Oct 21, 8:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2308 finished bets | 1% | $75.30 | +29% | +3.26¢ | $42.60 / $32.70 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2139 | $56.25 | +24% |
| Volatility model ≥ 2%, hold to the close | 4247 | -$16.20 | -3% |
| Momentum model ≥ 2%, hold to the close | 3576 | -$43.80 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27480 | 27473 | 101 (0%) | 1.07% | -$1,934.90 (-58%) | Hold to the close: -$1,934.90 (-58%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 17717 | 4.6% | 0.4% (72) | -658% | ❌ Worse |
| Momentum model | 17717 | 4.6% | 0.4% (72) | -681% | ❌ Worse |
| Mean-reversion model | 17717 | 7.8% | 0.4% (72) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17717 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4247 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2308 | 24 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1322 | 16 | +70% | -62% | -60% | -58% |
| Momentum model ≥ 2% | 3576 | 27 | -10% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2139 | 21 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1406 | 14 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 7027 | 47 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4903 | 39 | -12% | -80% | -80% | -76% |
| Mean-reversion model ≥ 10% | 3265 | 27 | -6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17915 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6571 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2987 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27473 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 101 | 0% | -$1,934.90 | -58% | — |
| Sell at 2¢ | 1003 | 4% | -$2,948.12 | -88% | 46 sec |
| Sell at 3¢ | 681 | 2% | -$2,943.31 | -88% | 48 sec |
| Sell at 5¢ | 482 | 2% | -$2,895.60 | -86% | 57 sec |
| Sell at 10¢ | 295 | 1% | -$2,794.45 | -83% | 64 sec |
| Sell at 25¢ | 161 | 1% | -$2,591.99 | -77% | 82 sec |
| Sell at 50¢ | 104 | 0% | -$2,352.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1124 | 6 | 11% | 4% | -49% | -81% | -84% |
| 2–5 min | 8858 | 46 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6987 | 26 | 3% | 1% | -60% | -93% | -92% |
| Under 1 min | 10500 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2008 | 11 | 5% | 2% | -32% | -89% | -90% |
| BNB | 2003 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 2001 | 7 | 5% | 3% | -57% | -88% | -87% |
| ETH | 1990 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 1990 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 1988 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1982 | 7 | 3% | 1% | -57% | -88% | -88% |
| BTC | 1977 | 11 | 5% | 2% | -25% | -88% | -90% |
| NEAR | 1976 | 11 | 6% | 3% | -28% | -80% | -80% |
| GOLD | 1076 | 3 | 4% | 1% | -67% | -81% | -83% |
| SILVER | 1037 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1014 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 903 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 893 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 830 | 5 | 2% | 1% | -44% | -85% | -84% |
| EURUSD | 827 | 3 | 2% | 1% | -66% | -85% | -85% |
| PALLADIUM | 813 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 775 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 741 | 3 | 1% | 1% | -62% | -99% | -98% |
| AUDUSD | 336 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 292 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13837 | 51 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13636 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2990 | 15 | 2% | 1% | -16% | -78% | -78% |
| 0.05–0.1% | 3094 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4568 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5227 | 25 | 6% | 3% | -48% | -87% | -87% |
| Over 0.5% | 2033 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7494 | 22 | 3% | 1% | -66% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,742 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 8:14:59 PM | GBPUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:14:59 PM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:14:59 PM | NEAR | UP | 1 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:14:43 PM | AUDUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:14:27 PM | BNB | UP | 33 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/21 8:14:27 PM | ZEC | UP | 33 sec | -0.259% | 0¢ | ❌ Lost | $0.00 |
| 10/21 8:13:38 PM | NATGAS | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:13:38 PM | DOGE | UP | 82 sec | -0.255% | 0¢ | ❌ Lost | $0.00 |
| 10/21 8:13:38 PM | PLATINUM | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:13:38 PM | SOL | UP | 82 sec | -0.198% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:13:38 PM | ETH | UP | 82 sec | -0.174% | 0¢ | ❌ Lost | $0.00 |
| 10/21 8:12:51 PM | HYPE | UP | 2.1 min | -0.350% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 8:12:51 PM | BTC | UP | 2.1 min | -0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 8:12:51 PM | USDJPY | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:12:51 PM | XRP | UP | 2.1 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 8:12:19 PM | GOLD | UP | 2.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/21 8:12:19 PM | COPPER | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 8:09:51 PM | PALLADIUM | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 8:09:02 PM | SILVER | UP | 6.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:59:54 PM | GOLD | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:59:54 PM | USDCAD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:59:54 PM | BRENT | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:59:22 PM | COPPER | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:59:05 PM | DOGE | UP | 55 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:58:16 PM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:58:00 PM | NEAR | UP | 2.0 min | -0.575% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:57:28 PM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:57:28 PM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:57:28 PM | XRP | UP | 2.5 min | -0.259% | 5¢ | ❌ Lost | -$0.15 |
| 10/21 7:56:55 PM | HYPE | UP | 3.1 min | -0.298% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
