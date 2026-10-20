# 15-Minute 1¢ Study

*Updated Tue Oct 20, 5:10 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2108 finished bets | 1% | $85.45 | +36% | +4.05¢ | $24.35 / $61.10 |

*Expect about **95 buys a day** (~$14.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1939 | $66.85 | +31% |
| Momentum model ≥ 2%, hold to the close | 3234 | -$15.35 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 2108 | -$31.55 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24978 | 24969 | 92 (0%) | 1.07% | -$1,746.65 (-58%) | Hold to the close: -$1,746.65 (-58%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16341 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16341 | 4.6% | 0.4% (65) | -694% | ❌ Worse |
| Mean-reversion model | 16341 | 7.7% | 0.4% (65) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16341 | 65 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3822 | 31 | -7% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2108 | 23 | +36% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1226 | 15 | +72% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3234 | 26 | -4% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1939 | 20 | +31% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1283 | 13 | +39% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6377 | 42 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4436 | 34 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2933 | 22 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16539 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5876 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2554 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24969 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,746.65 | -58% | — |
| Sell at 2¢ | 899 | 4% | -$2,674.91 | -88% | 46 sec |
| Sell at 3¢ | 610 | 2% | -$2,670.75 | -88% | 47 sec |
| Sell at 5¢ | 434 | 2% | -$2,626.55 | -87% | 51 sec |
| Sell at 10¢ | 264 | 1% | -$2,534.81 | -84% | 64 sec |
| Sell at 25¢ | 145 | 1% | -$2,344.70 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,113.40 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 967 | 5 | 10% | 3% | -51% | -82% | -84% |
| 2–5 min | 8101 | 41 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6374 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9523 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1859 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1848 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1848 | 9 | 5% | 2% | -40% | -83% | -82% |
| ETH | 1838 | 9 | 6% | 3% | -41% | -87% | -87% |
| DOGE | 1837 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1834 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1828 | 7 | 3% | 1% | -53% | -87% | -87% |
| NEAR | 1824 | 10 | 6% | 3% | -29% | -79% | -79% |
| BTC | 1823 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 964 | 1 | 3% | 1% | -88% | -93% | -95% |
| SILVER | 931 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 906 | 3 | 3% | 1% | -61% | -94% | -95% |
| COPPER | 808 | 3 | 2% | 1% | -65% | -74% | -74% |
| PLATINUM | 799 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 740 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 736 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 728 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 693 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 643 | 3 | 1% | 1% | -56% | -99% | -98% |
| AUDUSD | 267 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 215 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12611 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12358 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2800 | 15 | 2% | 1% | -10% | -77% | -76% |
| 0.05–0.1% | 2874 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4183 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4820 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1859 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6386 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,794 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 5:10:06 AM | DOGE | DOWN | 4.9 min | +0.260% | — | In play | — |
| 10/20 5:09:02 AM | ZEC | DOWN | 6.0 min | +0.786% | — | In play | — |
| 10/20 4:59:57 AM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 4:59:41 AM | AUDUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:59:25 AM | BNB | DOWN | 35 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:59:25 AM | GBPUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:59:25 AM | BTC | DOWN | 35 sec | +0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:59:25 AM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:58:52 AM | PALLADIUM | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:58:36 AM | PLATINUM | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:58:20 AM | NEAR | DOWN | 1.6 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:58:20 AM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:58:04 AM | XRP | DOWN | 1.9 min | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:57:47 AM | ETH | DOWN | 2.2 min | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:57:47 AM | USDCAD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:57:31 AM | ZEC | DOWN | 2.5 min | +0.407% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:57:31 AM | HYPE | DOWN | 2.5 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:57:15 AM | NATGAS | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:56:40 AM | SOL | DOWN | 3.3 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:55:54 AM | DOGE | DOWN | 4.1 min | +0.141% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 4:44:50 AM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:44:34 AM | GOLD | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:44:03 AM | ZEC | UP | 57 sec | -0.186% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:43:31 AM | COPPER | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:43:14 AM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:57 AM | SOL | UP | 2.0 min | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:41 AM | HYPE | UP | 2.3 min | -0.290% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:41 AM | DOGE | UP | 2.3 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:41 AM | BNB | UP | 2.3 min | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:41 AM | BTC | UP | 2.3 min | -0.150% | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
