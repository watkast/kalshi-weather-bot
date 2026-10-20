# 15-Minute 1¢ Study

*Updated Tue Oct 20, 3:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2167 finished bets | 1% | $77.35 | +32% | +3.57¢ | $21.65 / $55.70 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2002 | $58.45 | +26% |
| Momentum model ≥ 2%, hold to the close | 3342 | -$29.30 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 2167 | -$39.65 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25639 | 25624 | 92 (0%) | 1.07% | -$1,832.45 (-59%) | Hold to the close: -$1,832.45 (-59%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16688 | 4.6% | 0.4% (65) | -676% | ❌ Worse |
| Momentum model | 16688 | 4.5% | 0.4% (65) | -698% | ❌ Worse |
| Mean-reversion model | 16688 | 7.8% | 0.4% (65) | -817% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16688 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3957 | 31 | -10% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2167 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1244 | 15 | +69% | -60% | -58% | -56% |
| Momentum model ≥ 2% | 3342 | 26 | -7% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2002 | 20 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1318 | 13 | +35% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6557 | 42 | -30% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4564 | 34 | -18% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3023 | 22 | -17% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16886 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6071 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2667 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25624 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,832.45 | -59% | — |
| Sell at 2¢ | 930 | 4% | -$2,752.65 | -88% | 46 sec |
| Sell at 3¢ | 632 | 2% | -$2,747.97 | -88% | 48 sec |
| Sell at 5¢ | 448 | 2% | -$2,703.25 | -87% | 51 sec |
| Sell at 10¢ | 273 | 1% | -$2,608.82 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,423.88 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,199.20 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1024 | 5 | 11% | 4% | -53% | -81% | -84% |
| 2–5 min | 8290 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6544 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9762 | 22 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1899 | 11 | 4% | 2% | -28% | -90% | -90% |
| HYPE | 1887 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1886 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1876 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1875 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1874 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1867 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1862 | 10 | 6% | 3% | -31% | -79% | -79% |
| BTC | 1860 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 997 | 1 | 4% | 1% | -88% | -92% | -94% |
| SILVER | 958 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 933 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 834 | 3 | 2% | 1% | -66% | -75% | -75% |
| PLATINUM | 829 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 764 | 5 | 2% | 1% | -39% | -84% | -83% |
| EURUSD | 762 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 756 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 719 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 670 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 282 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 234 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12886 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12738 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2825 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2925 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4278 | 13 | 5% | 2% | -63% | -89% | -89% |
| 0.2–0.5% | 4939 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1916 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 5999 | 19 | 3% | 1% | -62% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,760 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 3:14:02 PM | HYPE | DOWN | 57 sec | +0.208% | — | In play | — |
| 10/20 3:14:02 PM | NEAR | UP | 57 sec | -0.330% | — | In play | — |
| 10/20 3:14:02 PM | SOL | DOWN | 57 sec | +0.025% | — | In play | — |
| 10/20 3:13:28 PM | XRP | DOWN | 1.5 min | +0.113% | — | In play | — |
| 10/20 3:13:28 PM | BTC | DOWN | 1.5 min | +0.087% | — | In play | — |
| 10/20 3:12:41 PM | DOGE | UP | 2.3 min | -0.159% | — | In play | — |
| 10/20 3:11:03 PM | ETH | DOWN | 4.0 min | +0.154% | — | In play | — |
| 10/20 3:10:48 PM | ZEC | DOWN | 4.2 min | +0.654% | — | In play | — |
| 10/20 2:59:48 PM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:59:15 PM | EURUSD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:58:58 PM | DOGE | DOWN | 62 sec | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:58:58 PM | NEAR | DOWN | 62 sec | +0.319% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:57:55 PM | HYPE | DOWN | 2.1 min | +0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:57:55 PM | BTC | DOWN | 2.1 min | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:57:39 PM | XRP | DOWN | 2.3 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:57:23 PM | ZEC | DOWN | 2.6 min | +0.536% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:57:23 PM | SOL | DOWN | 2.6 min | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:57:23 PM | SILVER | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:57:07 PM | ETH | DOWN | 2.9 min | +0.148% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:57:07 PM | BNB | DOWN | 2.9 min | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:57:07 PM | GOLD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:56:50 PM | PLATINUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:44:57 PM | NATGAS | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:44:57 PM | COPPER | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:44:57 PM | PALLADIUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:44:57 PM | BNB | UP | 2 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:44:57 PM | USDCAD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:44:25 PM | GBPUSD | DOWN | 34 sec | — | 23¢ | ❌ Lost | -$0.15 |
| 10/20 2:44:09 PM | PLATINUM | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:43:18 PM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
