# 15-Minute 1¢ Study

*Updated Wed Oct 21, 6:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2302 finished bets | 1% | $76.05 | +29% | +3.30¢ | $43.05 / $33.00 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2133 | $57.00 | +24% |
| Volatility model ≥ 2%, hold to the close | 4229 | -$13.95 | -3% |
| Momentum model ≥ 2%, hold to the close | 3565 | -$42.75 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27321 | 27311 | 100 (0%) | 1.07% | -$1,928.95 (-58%) | Hold to the close: -$1,928.95 (-58%) |

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
| Volatility model | 17638 | 4.6% | 0.4% (72) | -657% | ❌ Worse |
| Momentum model | 17638 | 4.6% | 0.4% (72) | -680% | ❌ Worse |
| Mean-reversion model | 17638 | 7.8% | 0.4% (72) | -795% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17638 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4229 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2302 | 24 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1318 | 16 | +70% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 3565 | 27 | -10% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2133 | 21 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1404 | 14 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 6987 | 47 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4877 | 39 | -12% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3251 | 27 | -6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17836 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6520 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2955 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27311 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 100 | 0% | -$1,928.95 | -58% | — |
| Sell at 2¢ | 999 | 4% | -$2,929.21 | -88% | 46 sec |
| Sell at 3¢ | 678 | 2% | -$2,924.53 | -88% | 48 sec |
| Sell at 5¢ | 480 | 2% | -$2,876.95 | -86% | 56 sec |
| Sell at 10¢ | 294 | 1% | -$2,775.81 | -83% | 64 sec |
| Sell at 25¢ | 160 | 1% | -$2,575.35 | -77% | 82 sec |
| Sell at 50¢ | 103 | 0% | -$2,339.70 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1105 | 6 | 11% | 4% | -48% | -81% | -84% |
| 2–5 min | 8807 | 45 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6951 | 26 | 3% | 1% | -59% | -93% | -92% |
| Under 1 min | 10444 | 23 | 1% | 0% | -69% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2000 | 11 | 5% | 2% | -31% | -89% | -90% |
| BNB | 1994 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1993 | 7 | 5% | 3% | -57% | -88% | -87% |
| ETH | 1981 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 1981 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 1979 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1973 | 7 | 3% | 1% | -57% | -88% | -88% |
| BTC | 1968 | 11 | 5% | 2% | -25% | -88% | -90% |
| NEAR | 1967 | 11 | 6% | 3% | -28% | -80% | -79% |
| GOLD | 1067 | 2 | 3% | 1% | -78% | -81% | -84% |
| SILVER | 1029 | 4 | 3% | 1% | -55% | -82% | -82% |
| WTI | 1008 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 894 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 885 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 825 | 5 | 2% | 1% | -43% | -85% | -84% |
| EURUSD | 821 | 3 | 2% | 1% | -66% | -84% | -85% |
| PALLADIUM | 808 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 768 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 735 | 3 | 1% | 1% | -62% | -99% | -98% |
| AUDUSD | 328 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 287 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13739 | 50 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13572 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2979 | 15 | 2% | 1% | -16% | -78% | -77% |
| 0.05–0.1% | 3083 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4548 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5202 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 2021 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,744 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 6:07:41 PM | ZEC | DOWN | 7.3 min | +0.881% | — | In play | — |
| 10/21 6:07:41 PM | HYPE | DOWN | 7.3 min | +0.492% | — | In play | — |
| 10/21 6:07:07 PM | BNB | DOWN | 7.9 min | +0.303% | — | In play | — |
| 10/21 5:59:33 PM | SOL | DOWN | 26 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:59:33 PM | HYPE | UP | 26 sec | -0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:59:17 PM | DOGE | DOWN | 42 sec | +0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:59:02 PM | ETH | UP | 58 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:59:02 PM | EURUSD | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:58:46 PM | USDJPY | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:58:46 PM | NEAR | DOWN | 74 sec | +0.344% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:58:46 PM | PALLADIUM | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:58:46 PM | GBPUSD | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:58:46 PM | SILVER | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:58:46 PM | XRP | DOWN | 74 sec | +0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:57:59 PM | BNB | UP | 2.0 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:57:32 PM | WTI | DOWN | 2.5 min | — | 4¢ | ❌ Lost | -$0.15 |
| 10/21 5:57:16 PM | NATGAS | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:57:00 PM | PLATINUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:56:11 PM | BTC | UP | 3.8 min | -0.192% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:46 PM | EURUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:30 PM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:15 PM | SOL | UP | 44 sec | -0.151% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:44:15 PM | ETH | UP | 44 sec | -0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:15 PM | HYPE | UP | 44 sec | -0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:44:15 PM | BNB | UP | 44 sec | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:43:57 PM | BTC | UP | 63 sec | -0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:43:57 PM | USDJPY | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:43:41 PM | USDCAD | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:43:25 PM | ZEC | UP | 1.6 min | -0.565% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:43:25 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
