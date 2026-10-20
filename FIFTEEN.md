# 15-Minute 1¢ Study

*Updated Tue Oct 20, 3:44 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2168 finished bets | 1% | $77.20 | +32% | +3.56¢ | $21.50 / $55.70 |

*Expect about **96 buys a day** (~$14.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2004 | $58.15 | +26% |
| Momentum model ≥ 2%, hold to the close | 3344 | -$29.60 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 2168 | -$39.80 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25662 | 25645 | 92 (0%) | 1.07% | -$1,834.85 (-59%) | Hold to the close: -$1,834.85 (-59%) |

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
| Volatility model | 16704 | 4.6% | 0.4% (65) | -675% | ❌ Worse |
| Momentum model | 16704 | 4.5% | 0.4% (65) | -697% | ❌ Worse |
| Mean-reversion model | 16704 | 7.8% | 0.4% (65) | -817% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16704 | 65 | -52% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3958 | 31 | -10% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2168 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1245 | 15 | +68% | -60% | -58% | -56% |
| Momentum model ≥ 2% | 3344 | 26 | -8% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2004 | 20 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1319 | 13 | +35% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 6564 | 42 | -30% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4570 | 34 | -18% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3027 | 22 | -17% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16902 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6074 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2669 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25645 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,834.85 | -59% | — |
| Sell at 2¢ | 933 | 4% | -$2,754.27 | -88% | 46 sec |
| Sell at 3¢ | 635 | 2% | -$2,749.20 | -88% | 48 sec |
| Sell at 5¢ | 450 | 2% | -$2,704.35 | -87% | 51 sec |
| Sell at 10¢ | 274 | 1% | -$2,609.91 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,426.28 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,201.60 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1024 | 5 | 11% | 4% | -53% | -81% | -84% |
| 2–5 min | 8295 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6548 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9774 | 22 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1900 | 11 | 4% | 2% | -28% | -90% | -90% |
| HYPE | 1889 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1888 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1877 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1877 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1876 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1869 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1864 | 10 | 6% | 3% | -31% | -79% | -79% |
| BTC | 1862 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 997 | 1 | 4% | 1% | -88% | -92% | -94% |
| SILVER | 958 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 934 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 834 | 3 | 2% | 1% | -66% | -75% | -75% |
| PLATINUM | 829 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 766 | 5 | 2% | 1% | -39% | -84% | -83% |
| EURUSD | 762 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 756 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 719 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 670 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 284 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 234 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12894 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12751 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2829 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2927 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4282 | 13 | 5% | 2% | -63% | -89% | -89% |
| 0.2–0.5% | 4944 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1917 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6020 | 19 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,764 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 3:44:19 PM | WTI | UP | 40 sec | — | — | In play | — |
| 10/20 3:44:03 PM | BNB | UP | 56 sec | -0.046% | — | In play | — |
| 10/20 3:44:03 PM | BTC | UP | 56 sec | -0.055% | — | In play | — |
| 10/20 3:43:31 PM | SOL | UP | 89 sec | -0.122% | — | In play | — |
| 10/20 3:42:14 PM | HYPE | UP | 2.8 min | -0.347% | — | In play | — |
| 10/20 3:42:06 PM | ETH | UP | 2.9 min | -0.126% | — | In play | — |
| 10/20 3:40:30 PM | ZEC | UP | 4.5 min | -0.577% | — | In play | — |
| 10/20 3:40:14 PM | XRP | UP | 4.8 min | -0.218% | — | In play | — |
| 10/20 3:40:14 PM | DOGE | UP | 4.8 min | -0.232% | — | In play | — |
| 10/20 3:40:14 PM | NEAR | UP | 4.8 min | -0.604% | — | In play | — |
| 10/20 3:29:31 PM | DOGE | UP | 29 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:29:31 PM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:29:31 PM | BTC | DOWN | 29 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:29:15 PM | BNB | DOWN | 45 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:29:00 PM | NEAR | DOWN | 59 sec | +0.224% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:28:43 PM | NATGAS | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:28:11 PM | SOL | UP | 1.8 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:25:47 PM | XRP | UP | 4.2 min | -0.232% | 3¢ | ❌ Lost | -$0.15 |
| 10/20 3:25:31 PM | HYPE | DOWN | 4.5 min | +0.418% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:14:39 PM | NATGAS | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:14:39 PM | AUDUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:14:39 PM | WTI | DOWN | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:14:23 PM | BNB | UP | 37 sec | -0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:14:02 PM | HYPE | DOWN | 57 sec | +0.208% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:14:02 PM | NEAR | UP | 57 sec | -0.330% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:14:02 PM | SOL | DOWN | 57 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:13:28 PM | XRP | DOWN | 1.5 min | +0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:13:28 PM | BTC | DOWN | 1.5 min | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:12:41 PM | DOGE | UP | 2.3 min | -0.159% | 17¢ | ❌ Lost | -$0.15 |
| 10/20 3:11:03 PM | ETH | DOWN | 4.0 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
