# 15-Minute 1¢ Study

*Updated Sun Oct 18, 8:15 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1975 finished bets | 1% | $87.35 | +40% | +4.42¢ | $32.30 / $55.05 |

*Expect about **95 buys a day** (~$14.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1816 | $66.95 | +34% |
| Momentum model ≥ 2%, hold to the close | 3023 | -$3.10 | -1% |
| Volatility model ≥ 2%, hold to the close | 3560 | -$26.45 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23169 | 23150 | 88 (0%) | 1.07% | -$1,575.40 (-56%) | Hold to the close: -$1,575.40 (-56%) |

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
| Volatility model | 15339 | 4.6% | 0.4% (62) | -672% | ❌ Worse |
| Momentum model | 15339 | 4.6% | 0.4% (62) | -694% | ❌ Worse |
| Mean-reversion model | 15339 | 7.7% | 0.4% (62) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15339 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3560 | 29 | -6% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1975 | 22 | +40% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1161 | 14 | +69% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 3023 | 25 | -1% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1816 | 19 | +34% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1210 | 12 | +37% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5950 | 40 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4136 | 32 | -14% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2738 | 21 | -12% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15537 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5362 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2251 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23150 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,575.40 | -56% | — |
| Sell at 2¢ | 839 | 4% | -$2,491.26 | -89% | 44 sec |
| Sell at 3¢ | 569 | 2% | -$2,487.49 | -89% | 47 sec |
| Sell at 5¢ | 408 | 2% | -$2,444.20 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,357.83 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,171.93 | -77% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,941.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 843 | 5 | 10% | 3% | -44% | -82% | -84% |
| 2–5 min | 7555 | 39 | 7% | 3% | -49% | -88% | -87% |
| 1–2 min | 5941 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8807 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1745 | 11 | 4% | 2% | -22% | -90% | -90% |
| HYPE | 1735 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1735 | 8 | 5% | 2% | -43% | -89% | -88% |
| DOGE | 1729 | 3 | 4% | 2% | -78% | -91% | -90% |
| ETH | 1727 | 9 | 6% | 3% | -37% | -87% | -87% |
| SOL | 1723 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1718 | 7 | 3% | 1% | -50% | -87% | -87% |
| NEAR | 1713 | 9 | 6% | 3% | -32% | -79% | -79% |
| BTC | 1712 | 9 | 5% | 2% | -29% | -88% | -90% |
| GOLD | 875 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 850 | 4 | 3% | 1% | -46% | -80% | -80% |
| WTI | 831 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 739 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 727 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 675 | 5 | 2% | 2% | -31% | -82% | -81% |
| EURUSD | 669 | 3 | 3% | 1% | -58% | -82% | -81% |
| PALLADIUM | 665 | 2 | 1% | 0% | -72% | -84% | -84% |
| GBPUSD | 622 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 581 | 3 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 209 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 170 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11636 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11514 | 46 | 3% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2660 | 14 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 2698 | 10 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 3895 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4520 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1761 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6345 | 18 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,862 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 8:14:34 PM | WTI | UP | 25 sec | — | 0¢ | In play | — |
| 10/18 8:14:26 PM | COPPER | DOWN | 33 sec | — | 0¢ | In play | — |
| 10/18 8:14:17 PM | NATGAS | DOWN | 43 sec | — | 0¢ | In play | — |
| 10/18 8:13:50 PM | GBPUSD | DOWN | 69 sec | — | 0¢ | In play | — |
| 10/18 8:13:40 PM | PALLADIUM | DOWN | 79 sec | — | 0¢ | In play | — |
| 10/18 8:13:38 PM | USDJPY | UP | 81 sec | — | 0¢ | In play | — |
| 10/18 8:12:55 PM | PLATINUM | DOWN | 2.1 min | — | 0¢ | In play | — |
| 10/18 8:12:53 PM | NEAR | DOWN | 2.1 min | +0.378% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:12:23 PM | SILVER | DOWN | 2.6 min | — | 1¢ | In play | — |
| 10/18 8:11:45 PM | XRP | DOWN | 3.2 min | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:11:08 PM | BTC | DOWN | 3.9 min | +0.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:10:51 PM | ETH | DOWN | 4.2 min | +0.226% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:10:48 PM | DOGE | DOWN | 4.2 min | +0.290% | 1¢ | In play | — |
| 10/18 8:10:43 PM | HYPE | DOWN | 4.3 min | +0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:10:43 PM | BNB | DOWN | 4.3 min | +0.081% | 1¢ | In play | — |
| 10/18 8:10:13 PM | GOLD | DOWN | 4.8 min | — | 1¢ | In play | — |
| 10/18 8:09:53 PM | SOL | DOWN | 5.1 min | +0.343% | 1¢ | In play | — |
| 10/18 8:08:51 PM | ZEC | DOWN | 6.1 min | +1.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:59:59 PM | GOLD | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:59:55 PM | BNB | UP | 4 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:59:39 PM | AUDUSD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:59:26 PM | HYPE | UP | 34 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:59:12 PM | XRP | UP | 48 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:59:04 PM | SOL | UP | 56 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:58:50 PM | DOGE | UP | 70 sec | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:58:40 PM | BTC | UP | 80 sec | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:58:04 PM | ETH | UP | 1.9 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:57:22 PM | NEAR | UP | 2.6 min | -0.771% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:44:48 PM | HYPE | DOWN | 11 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:44:33 PM | EURUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
