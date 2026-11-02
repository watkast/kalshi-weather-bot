# 15-Minute 1¢ Study

*Updated Mon Nov 2, 4:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3495 finished bets | 1% | $127.25 | +33% | +3.64¢ | $72.20 / $55.05 |

*Expect about **99 buys a day** (~$14.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6451 | $58.50 | +7% |
| Momentum model ≥ 5%, hold to the close | 3223 | $55.00 | +16% |
| Momentum model ≥ 2%, hold to the close | 5318 | -$27.45 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42500 | 42484 | 159 (0%) | 1.07% | -$2,943.90 (-57%) | Hold to the close: -$2,943.90 (-57%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26440 | 4.7% | 0.4% (106) | -674% | ❌ Worse |
| Momentum model | 26440 | 4.6% | 0.4% (106) | -697% | ❌ Worse |
| Mean-reversion model | 26440 | 8.1% | 0.4% (106) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26440 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6451 | 60 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3495 | 37 | +33% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1984 | 22 | +58% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5318 | 42 | -4% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3223 | 29 | +16% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2103 | 19 | +26% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 10931 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7666 | 65 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5126 | 46 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26642 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9972 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5870 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42484 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,943.90 | -57% | — |
| Sell at 2¢ | 1664 | 4% | -$4,513.26 | -87% | 47 sec |
| Sell at 3¢ | 1142 | 3% | -$4,500.52 | -87% | 48 sec |
| Sell at 5¢ | 794 | 2% | -$4,401.80 | -85% | 63 sec |
| Sell at 10¢ | 479 | 1% | -$4,220.41 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,905.09 | -76% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,544.90 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2031 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13640 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10731 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16071 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2985 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 2976 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2973 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2971 | 9 | 5% | 2% | -62% | -89% | -87% |
| DOGE | 2960 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2958 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2941 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2940 | 15 | 5% | 2% | -34% | -83% | -83% |
| XRP | 2938 | 12 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1554 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1513 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1509 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1344 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1285 | 5 | 2% | 1% | -64% | -76% | -75% |
| EURUSD | 1284 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1239 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1217 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1212 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1203 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 739 | 4 | 1% | 1% | -49% | -85% | -84% |
| USDCAD | 715 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 316 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 194 | 1 | 5% | 2% | -52% | -43% | -41% |
| 30YRRATE | 183 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 175 | 2 | 5% | 1% | +7% | +15% | +16% |
| 5YRRATE | 160 | 1 | 6% | 2% | -42% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21582 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20902 | 72 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4353 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4590 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6899 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7851 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2944 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10624 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,795 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 4:27:44 AM | WTI | UP | 2.3 min | — | — | In play | — |
| 11/2 4:27:44 AM | BTC | UP | 2.3 min | -0.110% | — | In play | — |
| 11/2 4:26:24 AM | HYPE | DOWN | 3.6 min | +0.234% | — | In play | — |
| 11/2 4:26:08 AM | EURUSD | DOWN | 3.9 min | — | — | In play | — |
| 11/2 4:25:52 AM | USDCAD | UP | 4.1 min | — | — | In play | — |
| 11/2 4:24:48 AM | GBPUSD | DOWN | 5.2 min | — | — | In play | — |
| 11/2 4:14:50 AM | PALLADIUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:14:34 AM | ZEC | DOWN | 26 sec | +0.041% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:14:34 AM | GOLD | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:14:34 AM | BTC | UP | 26 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:14:18 AM | BNB | UP | 42 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:14:18 AM | DOGE | DOWN | 42 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:14:03 AM | NATGAS | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:14:03 AM | ETH | DOWN | 56 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:14:03 AM | XRP | DOWN | 56 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:13:30 AM | HYPE | UP | 1.5 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:13:14 AM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:12:59 AM | USDCAD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:11:24 AM | SOL | UP | 3.6 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:10:04 AM | NEAR | UP | 4.9 min | -0.539% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:07:31 AM | GBPUSD | DOWN | 7.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 3:59:47 AM | BTC | UP | 12 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/2 3:59:31 AM | EURUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 3:59:31 AM | XRP | DOWN | 28 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/2 3:59:31 AM | ETH | DOWN | 28 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/2 3:59:15 AM | ZEC | DOWN | 44 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 3:58:59 AM | SOL | DOWN | 60 sec | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 11/2 3:58:59 AM | WTI | UP | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 3:58:59 AM | DOGE | DOWN | 60 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/2 3:58:44 AM | USDJPY | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
