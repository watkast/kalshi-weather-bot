# 15-Minute 1¢ Study

*Updated Wed Oct 21, 10:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2260 finished bets | 1% | $80.55 | +32% | +3.56¢ | $45.60 / $34.95 |

*Expect about **97 buys a day** (~$14.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2092 | $61.50 | +26% |
| Volatility model ≥ 2%, hold to the close | 4142 | -$17.75 | -3% |
| Momentum model ≥ 2%, hold to the close | 3502 | -$35.10 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26830 | 26823 | 98 (0%) | 1.07% | -$1,897.85 (-58%) | Hold to the close: -$1,897.85 (-58%) |

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
| Volatility model | 17362 | 4.6% | 0.4% (70) | -663% | ❌ Worse |
| Momentum model | 17362 | 4.6% | 0.4% (70) | -686% | ❌ Worse |
| Mean-reversion model | 17362 | 7.8% | 0.4% (70) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17362 | 70 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4142 | 35 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2260 | 24 | +32% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1294 | 16 | +73% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3502 | 27 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2092 | 21 | +26% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1375 | 14 | +39% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6867 | 46 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4791 | 38 | -13% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3185 | 26 | -7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17560 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6405 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2858 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26823 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 98 | 0% | -$1,897.85 | -58% | — |
| Sell at 2¢ | 976 | 4% | -$2,876.09 | -88% | 46 sec |
| Sell at 3¢ | 664 | 2% | -$2,870.89 | -88% | 48 sec |
| Sell at 5¢ | 469 | 2% | -$2,825.00 | -86% | 58 sec |
| Sell at 10¢ | 286 | 1% | -$2,727.19 | -83% | 64 sec |
| Sell at 25¢ | 158 | 1% | -$2,522.87 | -77% | 81 sec |
| Sell at 50¢ | 101 | 0% | -$2,294.10 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1081 | 6 | 11% | 4% | -47% | -81% | -84% |
| 2–5 min | 8650 | 44 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6853 | 25 | 3% | 1% | -60% | -93% | -92% |
| Under 1 min | 10235 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1970 | 11 | 5% | 2% | -30% | -90% | -90% |
| BNB | 1963 | 11 | 5% | 2% | -31% | -83% | -82% |
| HYPE | 1961 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1951 | 10 | 6% | 3% | -39% | -87% | -86% |
| DOGE | 1950 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1949 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1942 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1937 | 11 | 6% | 3% | -27% | -79% | -79% |
| BTC | 1937 | 11 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 1047 | 2 | 3% | 1% | -78% | -81% | -83% |
| SILVER | 1010 | 4 | 3% | 1% | -54% | -82% | -82% |
| WTI | 988 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 880 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 875 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 810 | 5 | 2% | 1% | -42% | -85% | -84% |
| EURUSD | 802 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 795 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 753 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 715 | 3 | 1% | 1% | -61% | -99% | -98% |
| AUDUSD | 315 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 271 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13477 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13346 | 49 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2936 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3041 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4467 | 15 | 5% | 2% | -59% | -89% | -89% |
| 0.2–0.5% | 5124 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 1989 | 6 | 7% | 3% | -69% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6490 | 30 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,736 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 10:14:54 AM | SOL | UP | 6 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:14:38 AM | BNB | DOWN | 22 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:14:22 AM | PLATINUM | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:22 AM | NATGAS | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:05 AM | BTC | DOWN | 54 sec | +0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:05 AM | USDJPY | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:05 AM | WTI | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:05 AM | ETH | UP | 54 sec | -0.110% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:49 AM | ZEC | UP | 70 sec | -0.327% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:49 AM | USDCAD | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:17 AM | XRP | UP | 1.7 min | -0.239% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:17 AM | NEAR | DOWN | 1.7 min | +0.457% | 4¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:17 AM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:01 AM | DOGE | UP | 2.0 min | -0.255% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:12:29 AM | HYPE | DOWN | 2.5 min | +0.345% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:59:51 AM | HYPE | UP | 8 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:59:35 AM | BNB | UP | 24 sec | -0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:59:35 AM | DOGE | UP | 24 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:59:35 AM | SOL | UP | 24 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:59:19 AM | ZEC | DOWN | 40 sec | +0.166% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:59:19 AM | NATGAS | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:58:45 AM | BTC | DOWN | 75 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:58:45 AM | USDCAD | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:58:13 AM | ETH | DOWN | 1.8 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:57:26 AM | WTI | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:57:10 AM | XRP | DOWN | 2.8 min | +0.349% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:55:17 AM | NEAR | DOWN | 4.7 min | +1.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:44:31 AM | DOGE | UP | 28 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 9:44:15 AM | PLATINUM | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:44:15 AM | NEAR | UP | 44 sec | -0.429% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
