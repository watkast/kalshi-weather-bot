# 15-Minute 1¢ Study

*Updated Mon Nov 2, 12:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3512 finished bets | 1% | $125.30 | +32% | +3.57¢ | $70.85 / $54.45 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6493 | $53.40 | +7% |
| Momentum model ≥ 5%, hold to the close | 3246 | $52.30 | +15% |
| Momentum model ≥ 2%, hold to the close | 5361 | -$32.40 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42856 | 42838 | 159 (0%) | 1.07% | -$2,988.60 (-57%) | Hold to the close: -$2,988.60 (-57%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26590 | 4.7% | 0.4% (106) | -675% | ❌ Worse |
| Momentum model | 26590 | 4.6% | 0.4% (106) | -698% | ❌ Worse |
| Mean-reversion model | 26590 | 8.1% | 0.4% (106) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26590 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6493 | 60 | +7% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3512 | 37 | +32% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1991 | 22 | +58% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5361 | 42 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3246 | 29 | +15% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2119 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 10991 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7703 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5147 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26792 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 10070 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5976 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42838 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,988.60 | -57% | — |
| Sell at 2¢ | 1680 | 4% | -$4,553.80 | -87% | 47 sec |
| Sell at 3¢ | 1155 | 3% | -$4,540.15 | -87% | 48 sec |
| Sell at 5¢ | 804 | 2% | -$4,440.00 | -85% | 63 sec |
| Sell at 10¢ | 486 | 1% | -$4,255.94 | -82% | 65 sec |
| Sell at 25¢ | 254 | 1% | -$3,939.86 | -76% | 82 sec |
| Sell at 50¢ | 165 | 0% | -$3,582.85 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2047 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13754 | 75 | 7% | 4% | -46% | -87% | -86% |
| 1–2 min | 10827 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16199 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3002 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 2993 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 2990 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2988 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2976 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2975 | 11 | 6% | 3% | -55% | -86% | -85% |
| BTC | 2957 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2956 | 15 | 5% | 2% | -34% | -83% | -84% |
| XRP | 2955 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1566 | 5 | 5% | 2% | -61% | -81% | -83% |
| SILVER | 1525 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1523 | 4 | 3% | 1% | -68% | -92% | -93% |
| PLATINUM | 1358 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1299 | 3 | 2% | 1% | -78% | -89% | -88% |
| COPPER | 1295 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1250 | 7 | 2% | 1% | -48% | -81% | -80% |
| GBPUSD | 1229 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1224 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1215 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 753 | 4 | 2% | 1% | -50% | -85% | -84% |
| USDCAD | 725 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 329 | 0 | 2% | 1% | -100% | -97% | -96% |
| 10YRRATE | 205 | 1 | 5% | 2% | -54% | -46% | -44% |
| 30YRRATE | 192 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 187 | 2 | 4% | 1% | -0% | +7% | +8% |
| 5YRRATE | 171 | 1 | 6% | 2% | -45% | -90% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21795 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21043 | 72 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4364 | 21 | 2% | 1% | -16% | -82% | -82% |
| 0.05–0.1% | 4603 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6945 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7911 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2964 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 9964 | 37 | 4% | 2% | -56% | -86% | -86% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,772 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 12:40:25 PM | DOGE | UP | 4.6 min | -0.616% | — | In play | — |
| 11/2 12:40:09 PM | GOLD | UP | 4.8 min | — | — | In play | — |
| 11/2 12:40:09 PM | SOL | UP | 4.8 min | -0.867% | — | In play | — |
| 11/2 12:40:09 PM | ETH | UP | 4.8 min | -0.587% | — | In play | — |
| 11/2 12:39:35 PM | HYPE | UP | 5.4 min | -0.880% | — | In play | — |
| 11/2 12:39:03 PM | ZEC | UP | 6.0 min | -2.200% | — | In play | — |
| 11/2 12:39:03 PM | BNB | UP | 6.0 min | -0.437% | — | In play | — |
| 11/2 12:38:31 PM | PALLADIUM | UP | 6.5 min | — | — | In play | — |
| 11/2 12:29:47 PM | BNB | DOWN | 13 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:29:47 PM | ETH | DOWN | 13 sec | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:29:47 PM | 10YRRATE | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:29:31 PM | NEAR | UP | 29 sec | -0.372% | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:29:31 PM | HYPE | DOWN | 29 sec | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:29:31 PM | ZEC | DOWN | 29 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:29:16 PM | GBPUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:28:11 PM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:28:11 PM | XRP | DOWN | 1.8 min | +0.282% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:27:36 PM | PALLADIUM | UP | 2.4 min | — | 22¢ | ❌ Lost | -$0.15 |
| 11/2 12:27:36 PM | BRENT | DOWN | 2.4 min | — | 42¢ | ❌ Lost | -$0.15 |
| 11/2 12:27:36 PM | DOGE | UP | 2.4 min | -0.272% | 62¢ | ❌ Lost | $0.00 |
| 11/2 12:27:20 PM | EURUSD | UP | 2.7 min | — | 5¢ | ❌ Lost | -$0.15 |
| 11/2 12:27:05 PM | SOL | UP | 2.9 min | -0.455% | 6¢ | ❌ Lost | -$0.15 |
| 11/2 12:26:31 PM | USDCAD | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:26:15 PM | WTI | DOWN | 3.8 min | — | 38¢ | ❌ Lost | -$0.15 |
| 11/2 12:26:15 PM | AUDUSD | UP | 3.8 min | — | 8¢ | ❌ Lost | -$0.15 |
| 11/2 12:26:00 PM | PLATINUM | UP | 4.0 min | — | 11¢ | ❌ Lost | -$0.15 |
| 11/2 12:25:11 PM | SILVER | UP | 4.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/2 12:25:11 PM | COPPER | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:23:49 PM | GOLD | UP | 6.2 min | — | 12¢ | ❌ Lost | -$0.15 |
| 11/2 12:14:48 PM | USDCAD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
