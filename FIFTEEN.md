# 15-Minute 1¢ Study

*Updated Sun Oct 18, 9:57 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1980 finished bets | 1% | $86.90 | +39% | +4.39¢ | $31.85 / $55.05 |

*Expect about **95 buys a day** (~$14.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1819 | $66.80 | +34% |
| Momentum model ≥ 2%, hold to the close | 3032 | -$4.00 | -1% |
| Volatility model ≥ 2%, hold to the close | 3576 | -$28.55 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23251 | 23244 | 88 (0%) | 1.07% | -$1,586.35 (-56%) | Hold to the close: -$1,586.35 (-56%) |

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
| Volatility model | 15392 | 4.6% | 0.4% (62) | -671% | ❌ Worse |
| Momentum model | 15392 | 4.6% | 0.4% (62) | -694% | ❌ Worse |
| Mean-reversion model | 15392 | 7.7% | 0.4% (62) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15392 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3576 | 29 | -7% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1980 | 22 | +39% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1164 | 14 | +69% | -70% | -68% | -66% |
| Momentum model ≥ 2% | 3032 | 25 | -1% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1819 | 19 | +34% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1212 | 12 | +37% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5978 | 40 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4154 | 32 | -15% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2750 | 21 | -13% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15590 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5389 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2265 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23244 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,586.35 | -56% | — |
| Sell at 2¢ | 840 | 4% | -$2,501.95 | -89% | 44 sec |
| Sell at 3¢ | 569 | 2% | -$2,498.44 | -89% | 47 sec |
| Sell at 5¢ | 408 | 2% | -$2,455.15 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,368.78 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,182.88 | -77% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,952.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 853 | 5 | 10% | 3% | -44% | -82% | -84% |
| 2–5 min | 7586 | 39 | 7% | 3% | -49% | -88% | -88% |
| 1–2 min | 5963 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8838 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1751 | 11 | 4% | 2% | -22% | -90% | -90% |
| BNB | 1742 | 8 | 5% | 2% | -43% | -89% | -88% |
| HYPE | 1741 | 6 | 5% | 2% | -58% | -90% | -88% |
| DOGE | 1736 | 3 | 4% | 2% | -78% | -91% | -90% |
| ETH | 1731 | 9 | 6% | 3% | -37% | -87% | -87% |
| SOL | 1729 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1723 | 7 | 3% | 1% | -50% | -87% | -87% |
| NEAR | 1719 | 9 | 6% | 3% | -32% | -79% | -79% |
| BTC | 1718 | 9 | 5% | 2% | -30% | -89% | -90% |
| GOLD | 879 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 854 | 4 | 3% | 1% | -46% | -80% | -80% |
| WTI | 834 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 745 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 731 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 678 | 5 | 2% | 2% | -31% | -82% | -81% |
| EURUSD | 673 | 3 | 3% | 1% | -58% | -82% | -81% |
| PALLADIUM | 668 | 2 | 1% | 0% | -72% | -84% | -84% |
| GBPUSD | 625 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 585 | 3 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 212 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 170 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11680 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11564 | 46 | 3% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2663 | 14 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 2709 | 10 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 3909 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4538 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1768 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6439 | 18 | 3% | 2% | -68% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,865 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 9:44:53 PM | XRP | UP | 6 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:44:49 PM | BNB | UP | 10 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:44:43 PM | USDJPY | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:44:41 PM | SOL | UP | 18 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:44:23 PM | HYPE | DOWN | 36 sec | -0.016% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:44:23 PM | PLATINUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:44:19 PM | ZEC | DOWN | 40 sec | +0.129% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:44:14 PM | DOGE | UP | 46 sec | -0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:43:38 PM | BTC | UP | 82 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:30 PM | COPPER | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:14 PM | WTI | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:08 PM | ETH | UP | 1.9 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:04 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:41:40 PM | NEAR | DOWN | 3.3 min | +0.434% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:29:33 PM | AUDUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:29:27 PM | HYPE | UP | 32 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:29:16 PM | GBPUSD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:29:04 PM | BTC | UP | 56 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:28:50 PM | SOL | UP | 70 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:28:24 PM | XRP | UP | 1.6 min | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:27:20 PM | BNB | UP | 2.7 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:27:06 PM | DOGE | UP | 2.9 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:26:54 PM | ZEC | UP | 3.1 min | -0.660% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:26:19 PM | NEAR | UP | 3.7 min | -0.653% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:26:07 PM | EURUSD | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:14:52 PM | GOLD | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:14:48 PM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:14:30 PM | HYPE | DOWN | 30 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:14:20 PM | ZEC | UP | 40 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:13:45 PM | BTC | UP | 74 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
