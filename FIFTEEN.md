# 15-Minute 1¢ Study

*Updated Tue Nov 17, 7:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4491 finished bets | 1% | $217.95 | +44% | +4.85¢ | $82.50 / $135.45 |

*Expect about **88 buys a day** (~$13.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4226 | $118.45 | +26% |
| Volatility model ≥ 2%, hold to the close | 8375 | $84.90 | +8% |
| Momentum model ≥ 2%, hold to the close | 6946 | $1.50 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60241 | 60195 | 237 (0%) | 1.07% | -$4,006.05 (-55%) | Hold to the close: -$4,006.05 (-55%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 36072 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 36072 | 4.4% | 0.4% (154) | -648% | ❌ Worse |
| Mean-reversion model | 36072 | 7.9% | 0.4% (154) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36072 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8375 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4491 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2580 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6946 | 57 | +0% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4226 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2753 | 26 | +34% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14782 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10281 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6828 | 64 | +7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36278 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14314 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9603 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60195 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,006.05 | -55% | — |
| Sell at 2¢ | 2428 | 4% | -$6,398.77 | -87% | 47 sec |
| Sell at 3¢ | 1641 | 3% | -$6,390.06 | -87% | 48 sec |
| Sell at 5¢ | 1122 | 2% | -$6,272.75 | -86% | 63 sec |
| Sell at 10¢ | 684 | 1% | -$6,022.01 | -82% | 65 sec |
| Sell at 25¢ | 366 | 1% | -$5,566.59 | -76% | 80 sec |
| Sell at 50¢ | 243 | 0% | -$5,011.80 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3037 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19499 | 108 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 15108 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22538 | 61 | 1% | 0% | -61% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4058 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4055 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4047 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 4037 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4036 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4030 | 19 | 7% | 3% | -41% | -82% | -82% |
| NEAR | 4010 | 18 | 5% | 2% | -41% | -85% | -86% |
| BTC | 4010 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 3995 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2142 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2121 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2079 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1893 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1847 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1777 | 6 | 2% | 1% | -68% | -76% | -76% |
| GBPUSD | 1773 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1747 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1733 | 6 | 2% | 1% | -68% | -96% | -96% |
| PALLADIUM | 1703 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1287 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1233 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 852 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 435 | 2 | 3% | 1% | -57% | -73% | -71% |
| 2YRRATE | 420 | 4 | 4% | 2% | -11% | -49% | -48% |
| 30YRRATE | 403 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 391 | 2 | 4% | 2% | -52% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30664 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29531 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5456 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5911 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9094 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11237 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4571 | 23 | 7% | 3% | -47% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16459 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,075 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 7:29:46 PM | PALLADIUM | DOWN | 14 sec | — | 0¢ | In play | — |
| 11/17 7:29:46 PM | USDCAD | DOWN | 14 sec | — | 0¢ | In play | — |
| 11/17 7:29:46 PM | PLATINUM | DOWN | 14 sec | — | 0¢ | In play | — |
| 11/17 7:29:30 PM | COPPER | DOWN | 30 sec | — | 0¢ | In play | — |
| 11/17 7:29:14 PM | GBPUSD | DOWN | 46 sec | — | 0¢ | In play | — |
| 11/17 7:29:14 PM | HYPE | DOWN | 46 sec | +0.160% | 0¢ | In play | — |
| 11/17 7:28:58 PM | DOGE | DOWN | 62 sec | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:28:58 PM | XRP | DOWN | 62 sec | +0.205% | 0¢ | ❌ Lost | $0.00 |
| 11/17 7:28:58 PM | BNB | DOWN | 62 sec | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:28:26 PM | BRENT | UP | 1.6 min | — | 0¢ | In play | — |
| 11/17 7:28:26 PM | ETH | DOWN | 1.6 min | +0.275% | 0¢ | In play | — |
| 11/17 7:28:10 PM | BTC | DOWN | 1.8 min | +0.223% | 1¢ | In play | — |
| 11/17 7:28:10 PM | SOL | DOWN | 1.8 min | +0.283% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:27:58 PM | AUDUSD | DOWN | 2.0 min | — | 0¢ | In play | — |
| 11/17 7:27:26 PM | ZEC | DOWN | 2.6 min | +0.721% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:26:42 PM | WTI | UP | 3.3 min | — | 1¢ | In play | — |
| 11/17 7:25:54 PM | NEAR | DOWN | 4.1 min | +0.886% | 3¢ | In play | — |
| 11/17 7:14:56 PM | BRENT | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:14:24 PM | WTI | UP | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:14:24 PM | GOLD | UP | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/17 7:14:09 PM | XRP | DOWN | 50 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/17 7:13:53 PM | GBPUSD | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:13:53 PM | ZEC | DOWN | 66 sec | +0.332% | 0¢ | ❌ Lost | $0.00 |
| 11/17 7:13:53 PM | USDJPY | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:13:53 PM | ETH | DOWN | 66 sec | +0.187% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:13:53 PM | NATGAS | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:13:37 PM | HYPE | DOWN | 82 sec | +0.201% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:13:11 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:13:11 PM | BTC | DOWN | 1.8 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:12:55 PM | BNB | DOWN | 2.1 min | +0.159% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
