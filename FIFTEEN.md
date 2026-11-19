# 15-Minute 1¢ Study

*Updated Wed Nov 18, 9:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4544 finished bets | 1% | $213.15 | +43% | +4.69¢ | $79.35 / $133.80 |

*Expect about **88 buys a day** (~$13.13/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4280 | $113.20 | +25% |
| Volatility model ≥ 2%, hold to the close | 8479 | $73.05 | +7% |
| Momentum model ≥ 2%, hold to the close | 7030 | -$7.95 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61522 | 61487 | 237 (0%) | 1.07% | -$4,163.40 (-56%) | Hold to the close: -$4,163.40 (-56%) |

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
| Volatility model | 36629 | 4.5% | 0.4% (154) | -631% | ❌ Worse |
| Momentum model | 36629 | 4.4% | 0.4% (154) | -656% | ❌ Worse |
| Mean-reversion model | 36629 | 7.9% | 0.4% (154) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36629 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8479 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4544 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2612 | 30 | +68% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7030 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4280 | 41 | +25% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2788 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14990 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10432 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6932 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36835 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14700 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9952 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61487 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,163.40 | -56% | — |
| Sell at 2¢ | 2486 | 4% | -$6,541.04 | -87% | 47 sec |
| Sell at 3¢ | 1678 | 3% | -$6,532.98 | -87% | 48 sec |
| Sell at 5¢ | 1144 | 2% | -$6,415.80 | -86% | 63 sec |
| Sell at 10¢ | 700 | 1% | -$6,158.40 | -82% | 65 sec |
| Sell at 25¢ | 375 | 1% | -$5,694.15 | -76% | 80 sec |
| Sell at 50¢ | 245 | 0% | -$5,155.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3130 | 17 | 10% | 4% | -48% | -82% | -83% |
| 2–5 min | 19951 | 108 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 15393 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23000 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4119 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4116 | 19 | 4% | 2% | -41% | -86% | -87% |
| HYPE | 4108 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4099 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4099 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4093 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4074 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4071 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4056 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2193 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2172 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2130 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1942 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1897 | 7 | 2% | 1% | -66% | -91% | -90% |
| COPPER | 1827 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1823 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1790 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1781 | 6 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1744 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1333 | 6 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1273 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 902 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 465 | 2 | 3% | 1% | -60% | -74% | -73% |
| 2YRRATE | 444 | 4 | 4% | 2% | -16% | -52% | -50% |
| 30YRRATE | 426 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 418 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31333 | 121 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 30154 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5514 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5987 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9221 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11450 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4654 | 23 | 7% | 3% | -48% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14961 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16821 | 49 | 4% | 2% | -67% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,023 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 9:26:37 PM | COPPER | UP | 3.4 min | — | — | In play | — |
| 11/18 9:14:40 PM | NATGAS | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:14:40 PM | DOGE | DOWN | 20 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/18 9:14:08 PM | SOL | DOWN | 52 sec | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/18 9:13:35 PM | HYPE | DOWN | 84 sec | +0.187% | 0¢ | ❌ Lost | $0.00 |
| 11/18 9:12:29 PM | PALLADIUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:12:29 PM | GBPUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:12:13 PM | ZEC | DOWN | 2.8 min | +0.583% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:12:13 PM | BRENT | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:58 PM | BTC | DOWN | 3.0 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:58 PM | ETH | DOWN | 3.0 min | +0.280% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:58 PM | PLATINUM | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:42 PM | WTI | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:42 PM | GOLD | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:42 PM | USDCAD | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:42 PM | SILVER | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:42 PM | COPPER | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:26 PM | EURUSD | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:11:10 PM | AUDUSD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:09:01 PM | NEAR | DOWN | 6.0 min | +1.093% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:09:01 PM | BNB | DOWN | 6.0 min | +0.356% | 2¢ | ❌ Lost | -$0.15 |
| 11/18 9:08:15 PM | XRP | DOWN | 6.8 min | +0.609% | 4¢ | ❌ Lost | -$0.15 |
| 11/18 8:59:46 PM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 8:59:30 PM | NATGAS | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 8:58:43 PM | GBPUSD | DOWN | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 8:58:27 PM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 8:58:27 PM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 8:58:11 PM | AUDUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 8:57:11 PM | BTC | DOWN | 2.8 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 8:56:55 PM | PALLADIUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
