# 15-Minute 1¢ Study

*Updated Tue Nov 24, 1:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4845 finished bets | 1% | $213.10 | +40% | +4.40¢ | $75.80 / $137.30 |

*Expect about **84 buys a day** (~$12.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4592 | $111.50 | +23% |
| Volatility model ≥ 2%, hold to the close | 9024 | $43.90 | +4% |
| Momentum model ≥ 2%, hold to the close | 7512 | -$28.40 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66717 | 66680 | 255 (0%) | 1.07% | -$4,503.60 (-56%) | Hold to the close: -$4,503.60 (-56%) |

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
| Volatility model | 39670 | 4.5% | 0.4% (164) | -642% | ❌ Worse |
| Momentum model | 39670 | 4.4% | 0.4% (164) | -665% | ❌ Worse |
| Mean-reversion model | 39670 | 7.8% | 0.4% (164) | -781% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39670 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9024 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4845 | 53 | +40% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2807 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7512 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4592 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2996 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16126 | 112 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11220 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7456 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39876 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15828 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10976 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66680 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,503.60 | -56% | — |
| Sell at 2¢ | 2727 | 4% | -$7,070.58 | -88% | 47 sec |
| Sell at 3¢ | 1835 | 3% | -$7,063.95 | -87% | 48 sec |
| Sell at 5¢ | 1250 | 2% | -$6,939.10 | -86% | 62 sec |
| Sell at 10¢ | 766 | 1% | -$6,664.14 | -83% | 65 sec |
| Sell at 25¢ | 412 | 1% | -$6,149.88 | -76% | 79 sec |
| Sell at 50¢ | 265 | 0% | -$5,542.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3437 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21587 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16677 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 24966 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4458 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4452 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4449 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4441 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4436 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4432 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4410 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4405 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4393 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2345 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2330 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2286 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2076 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2036 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1968 | 8 | 2% | 1% | -62% | -96% | -96% |
| COPPER | 1967 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1933 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1926 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1868 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1487 | 7 | 2% | 1% | -56% | -90% | -90% |
| USDCAD | 1403 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1030 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 533 | 2 | 3% | 1% | -65% | -77% | -75% |
| 2YRRATE | 500 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 493 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 485 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 123 | 1 | 2% | 1% | -24% | -97% | -98% |
| USDMXN | 15 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34130 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32550 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5814 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6351 | 26 | 3% | 2% | -35% | -91% | -90% |
| 0.1–0.2% | 9920 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12553 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5229 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16271 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15699 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16493 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,116 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 1:53:08 PM | NEAR | DOWN | 6.8 min | +1.199% | — | In play | — |
| 11/24 1:52:20 PM | HYPE | DOWN | 7.7 min | +1.042% | — | In play | — |
| 11/24 1:52:02 PM | BNB | DOWN | 8.0 min | +0.358% | — | In play | — |
| 11/24 1:44:50 PM | PALLADIUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:44:50 PM | PLATINUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:44:50 PM | 10YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:44:34 PM | GOLD | UP | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:44:34 PM | BTC | DOWN | 26 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:44:15 PM | BNB | DOWN | 44 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:44:15 PM | DOGE | DOWN | 44 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:44:15 PM | 30YRRATE | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:59 PM | ETH | DOWN | 60 sec | +0.078% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:59 PM | GBPUSD | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:59 PM | XRP | DOWN | 60 sec | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:59 PM | SOL | DOWN | 60 sec | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:43 PM | BRENT | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:09 PM | HYPE | UP | 1.9 min | -0.512% | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:42:53 PM | NEAR | DOWN | 2.1 min | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:42:37 PM | WTI | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:40:07 PM | ZEC | DOWN | 4.9 min | +0.597% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:29:33 PM | 2YRRATE | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:29:33 PM | 5YRRATE | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:29:14 PM | HYPE | UP | 45 sec | -0.207% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:29:14 PM | ZEC | UP | 45 sec | -0.373% | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:28:58 PM | USDCAD | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:28:58 PM | SOL | UP | 61 sec | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:28:42 PM | BTC | UP | 77 sec | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:28:42 PM | EURUSD | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:28:26 PM | INX | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:28:26 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
