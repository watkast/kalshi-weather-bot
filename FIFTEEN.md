# 15-Minute 1¢ Study

*Updated Fri Oct 23, 5:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2493 finished bets | 1% | $96.00 | +34% | +3.85¢ | $45.65 / $50.35 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2308 | $52.85 | +21% |
| Volatility model ≥ 2%, hold to the close | 4634 | $6.70 | +1% |
| Momentum model ≥ 2%, hold to the close | 3857 | -$19.45 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30407 | 30399 | 117 (0%) | 1.07% | -$2,072.25 (-56%) | Hold to the close: -$2,072.25 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19210 | 4.6% | 0.4% (82) | -635% | ❌ Worse |
| Momentum model | 19210 | 4.5% | 0.4% (82) | -661% | ❌ Worse |
| Mean-reversion model | 19210 | 7.9% | 0.4% (82) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19210 | 82 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4634 | 41 | +1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2493 | 27 | +34% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1419 | 17 | +69% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 3857 | 31 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2308 | 22 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1515 | 15 | +37% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7719 | 54 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5389 | 45 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3582 | 32 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19410 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7334 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30399 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 117 | 0% | -$2,072.25 | -56% | — |
| Sell at 2¢ | 1132 | 4% | -$3,247.93 | -88% | 47 sec |
| Sell at 3¢ | 776 | 3% | -$3,239.61 | -87% | 48 sec |
| Sell at 5¢ | 544 | 2% | -$3,188.65 | -86% | 61 sec |
| Sell at 10¢ | 332 | 1% | -$3,065.33 | -83% | 64 sec |
| Sell at 25¢ | 185 | 1% | -$2,817.90 | -76% | 82 sec |
| Sell at 50¢ | 119 | 0% | -$2,543.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1294 | 7 | 11% | 4% | -48% | -81% | -83% |
| 2–5 min | 9734 | 53 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7736 | 29 | 3% | 1% | -59% | -91% | -91% |
| Under 1 min | 11631 | 28 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2176 | 12 | 5% | 2% | -31% | -89% | -89% |
| BNB | 2167 | 12 | 5% | 2% | -31% | -83% | -82% |
| HYPE | 2166 | 8 | 5% | 3% | -54% | -88% | -87% |
| SOL | 2159 | 5 | 4% | 2% | -71% | -92% | -92% |
| ETH | 2156 | 10 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2153 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2147 | 9 | 3% | 1% | -48% | -88% | -88% |
| NEAR | 2144 | 12 | 5% | 3% | -27% | -81% | -81% |
| BTC | 2142 | 12 | 5% | 2% | -25% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1132 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 931 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15354 | 64 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15045 | 53 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3189 | 17 | 2% | 1% | -10% | -79% | -78% |
| 0.05–0.1% | 3336 | 11 | 3% | 2% | -52% | -92% | -91% |
| 0.1–0.2% | 5002 | 18 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5688 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2191 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7280 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,597 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 5:29:51 PM | BRENT | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:29:51 PM | WTI | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:29:35 PM | NATGAS | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:27:10 PM | HYPE | DOWN | 2.8 min | +0.471% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:25:16 PM | BTC | DOWN | 4.7 min | +0.378% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:25:16 PM | XRP | DOWN | 4.7 min | +0.467% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:25:00 PM | ETH | DOWN | 5.0 min | +0.538% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:25:00 PM | ZEC | DOWN | 5.0 min | +1.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:24:14 PM | SOL | DOWN | 5.8 min | +0.603% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:24:14 PM | DOGE | DOWN | 5.8 min | +0.811% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:23:58 PM | NEAR | DOWN | 6.0 min | +1.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:23:41 PM | BNB | DOWN | 6.3 min | +0.422% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:14:46 PM | NEAR | UP | 14 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:13:09 PM | SOL | UP | 1.9 min | -0.336% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:12:53 PM | XRP | UP | 2.1 min | -0.404% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:12:37 PM | ZEC | UP | 2.4 min | -0.873% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:12:37 PM | BNB | UP | 2.4 min | -0.317% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:12:37 PM | HYPE | UP | 2.4 min | -0.516% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:12:37 PM | DOGE | UP | 2.4 min | -0.677% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:11:48 PM | BTC | UP | 3.2 min | -0.333% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:59:37 PM | NATGAS | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 4:59:06 PM | WTI | DOWN | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:54:14 PM | BTC | UP | 5.8 min | -0.478% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:54:14 PM | DOGE | UP | 5.8 min | -1.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:53:58 PM | ZEC | UP | 6.0 min | -1.958% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:53:58 PM | XRP | UP | 6.0 min | -1.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:53:58 PM | HYPE | UP | 6.0 min | -1.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:53:43 PM | SOL | UP | 6.3 min | -0.958% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:53:24 PM | NEAR | UP | 6.6 min | -1.480% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:53:24 PM | BNB | UP | 6.6 min | -0.448% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
